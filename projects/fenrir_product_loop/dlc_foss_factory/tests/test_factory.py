
from __future__ import annotations

import copy
import hashlib
import json
import shutil
import sys
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch


FACTORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY_ROOT))

from dlc_factory.adapters import LocalAdapterExecutor
from dlc_factory.canonical import sha256_bytes
from dlc_factory.errors import DuplicateEventError, ReceiptIntegrityError, SecretRejected, SpecValidationError, WipCollisionError
from dlc_factory.lease import WipLease
from dlc_factory.materializer import Materializer, _relative_parts
from dlc_factory.policy import authority_binding
from dlc_factory.provenance import preflight
from dlc_factory.receipt import ReceiptBuilder, ReceiptStore
from dlc_factory.runtime import FactoryRuntime
from dlc_factory.spec import load_spec, validate_spec


VALID_SPEC = FACTORY_ROOT / "examples" / "NON_PRODUCTION_unit_spec.valid.json"
INVALID_SPEC = FACTORY_ROOT / "examples" / "unit_spec.invalid.json"


def synthetic_bound_spec() -> tuple[dict, bytes]:
    spec = load_spec(VALID_SPEC)
    license_bytes = b"NON_PRODUCTION synthetic license evidence\n"
    blob = hashlib.sha1(
        f"blob {len(license_bytes)}\0".encode("ascii") + license_bytes,
        usedforsecurity=False,
    ).hexdigest()
    spec["classification"] = "TARGET_BOUND_CANDIDATE"
    spec["target"] = {
        "binding_state": "BOUND",
        "target_id": "synthetic-bound-candidate",
        "user_job": "Exercise byte identity checks without admitting a real target.",
        "demand_evidence": {
            "permalink": "https://news.ycombinator.com/item?id=00000000",
            "observed_on": "2026-08-02",
            "engagement_score": 0,
            "buyer_class": "NON_PRODUCTION synthetic class",
            "pain_statement": "Synthetic evidence only; no market claim.",
        },
    }
    spec["provenance"] = {
        "review_state": "STRUCTURAL_ONLY",
        "upstream": {
            "repository": "https://example.invalid/NON_PRODUCTION/synthetic.git",
            "ref": "refs/tags/synthetic-v1",
            "commit": "a" * 40,
        },
        "license": {
            "path": "LICENSE.synthetic",
            "git_blob_sha1": blob,
            "sha256": sha256_bytes(license_bytes),
            "spdx_expression": "MIT",
            "obligations": ["Synthetic test obligation only."],
        },
        "trademark_boundary": "NON_PRODUCTION synthetic names only.",
        "asset_caveats": ["No real assets are present."],
    }
    return spec, license_bytes


class FactoryTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = Path("C:/tmp/dlc-factory-tests")
        parent.mkdir(exist_ok=True)
        self.temp = parent / uuid.uuid4().hex[:8]
        self.temp.mkdir()

    def tearDown(self) -> None:
        shutil.rmtree(self.temp, ignore_errors=False)
        try:
            self.temp.parent.rmdir()
        except OSError:
            pass

    def test_schema_and_examples(self) -> None:
        self.assertEqual(load_spec(VALID_SPEC)["classification"], "NON_PRODUCTION")
        with self.assertRaises(SecretRejected):
            load_spec(INVALID_SPEC)
        for schema in ("unit_spec.schema.json", "receipt.schema.json"):
            parsed = json.loads((FACTORY_ROOT / schema).read_text(encoding="utf-8"))
            self.assertEqual(parsed["$schema"], "https://json-schema.org/draft/2020-12/schema")

    def test_incomplete_spec(self) -> None:
        spec = load_spec(VALID_SPEC)
        del spec["extension"]
        with self.assertRaises(SpecValidationError):
            validate_spec(spec)

    def test_duplicate_and_nonfinite_json_rejected(self) -> None:
        duplicate = self.temp / "duplicate.json"
        duplicate.write_text('{"schema_id":"x","schema_id":"y"}', encoding="utf-8")
        with self.assertRaises(SpecValidationError):
            load_spec(duplicate)
        nonfinite = self.temp / "nonfinite.json"
        nonfinite.write_text('{"value":NaN}', encoding="utf-8")
        with self.assertRaises(SpecValidationError):
            load_spec(nonfinite)

    def test_path_traversal(self) -> None:
        spec = load_spec(VALID_SPEC)
        spec["unit_id"] = "../escape"
        with self.assertRaises(SpecValidationError):
            validate_spec(spec)
        for path in ("../escape", "..\\escape", "C:/escape", "file:stream"):
            with self.assertRaises(SpecValidationError):
                _relative_parts(path)

    def test_secret_rejection_before_any_run_write(self) -> None:
        spec = load_spec(VALID_SPEC)
        spec["api_key"] = "REDACTED_SYNTHETIC_SENTINEL"
        runs = self.temp / "runs"
        with self.assertRaises(SecretRejected):
            FactoryRuntime(runs_root=runs).run(spec)
        self.assertFalse(runs.exists())

    def test_unbound_preflight_is_unknown(self) -> None:
        result = preflight(load_spec(VALID_SPEC))
        self.assertEqual(result["status"], "UNKNOWN_UNBOUND_TARGET")
        self.assertEqual(result["license_compatibility_opinion"], "NONE")
        self.assertFalse(result["target_admitted"])

    def test_bound_preflight_checks_exact_license_bytes(self) -> None:
        spec, license_bytes = synthetic_bound_spec()
        matched = preflight(spec, license_bytes)
        self.assertEqual(matched["status"], "BOUND_EVIDENCE_REQUIRES_DISTINCT_REVIEW")
        self.assertEqual(matched["license_compatibility_opinion"], "NONE")
        spec["provenance"]["license"]["sha256"] = "b" * 64
        self.assertEqual(preflight(spec, license_bytes)["status"], "HOLD_PROVENANCE_HASH_MISMATCH")

    def test_wip_collision(self) -> None:
        root = self.temp / "runs"
        first = WipLease.acquire("maker-a", "a" * 64, runs_root=root)
        try:
            with self.assertRaises(WipCollisionError):
                WipLease.acquire("maker-b", "b" * 64, runs_root=root)
        finally:
            first.release()
        self.assertFalse((root / ".active").exists())

    def test_idempotent_materialization_and_receipt(self) -> None:
        spec = load_spec(VALID_SPEC)
        output = self.temp / "unit"
        first = Materializer().materialize(spec, output)
        second = Materializer().materialize(spec, output)
        self.assertTrue(first.created)
        self.assertFalse(second.created)
        self.assertEqual(first.tree_sha256, second.tree_sha256)
        runtime = FactoryRuntime(runs_root=self.temp / "runs")
        run_one = runtime.run(spec)
        run_two = runtime.run(spec)
        self.assertEqual(run_one["lifecycle"]["receipt_ref"]["sha256"], run_two["lifecycle"]["receipt_ref"]["sha256"])
        self.assertTrue(run_two["lifecycle"]["receipt_ref"]["idempotent"])

    def test_run_intent_binds_expected_artifact_tree(self) -> None:
        template_copy = self.temp / "templates"
        shutil.copytree(FACTORY_ROOT / "templates", template_copy)
        spec = load_spec(VALID_SPEC)
        initial = FactoryRuntime(
            runs_root=self.temp / "runs-a",
            materializer=Materializer(template_root=template_copy),
        ).intent(spec)
        landing = template_copy / "landing.html.tmpl"
        landing.write_text(
            landing.read_text(encoding="utf-8") + "\n<!-- synthetic revision -->\n",
            encoding="utf-8",
        )
        revised = FactoryRuntime(
            runs_root=self.temp / "runs-b",
            materializer=Materializer(template_root=template_copy),
        ).intent(spec)
        self.assertNotEqual(
            initial["expected_artifact_tree_sha256"],
            revised["expected_artifact_tree_sha256"],
        )
        self.assertNotEqual(initial["run_id"], revised["run_id"])

    def test_duplicate_events(self) -> None:
        builder = ReceiptBuilder(
            authority_binding(),
            unit_id="non-production-reference",
            unit_spec_sha256="a" * 64,
            artifact_manifest_sha256="b" * 64,
        )
        builder.add_event("same", "synthetic", {"value": 1})
        with self.assertRaises(DuplicateEventError):
            builder.add_event("same", "synthetic", {"value": 1})

    def test_failed_health_check_runs_rollback(self) -> None:
        spec = load_spec(VALID_SPEC)
        spec["adapters"]["options"]["force_health_failure"] = True
        result = FactoryRuntime(runs_root=self.temp / "runs").run(spec)["lifecycle"]
        self.assertEqual(result["status"], "ROLLED_BACK_AFTER_HEALTH_FAILURE")
        self.assertEqual(result["stage_results"][-1]["exit_code"], 23)
        self.assertEqual(result["rollback_result"]["exit_code"], 0)
        self.assertEqual(result["receipt"]["claim"]["result"], "FAIL")
        ReceiptStore(self.temp / "runs").verify(result["receipt_ref"]["path"])

    def test_rollback_failure_is_not_masked(self) -> None:
        spec = load_spec(VALID_SPEC)
        spec["adapters"]["options"]["force_health_failure"] = True
        spec["adapters"]["options"]["force_rollback_failure"] = True
        result = FactoryRuntime(runs_root=self.temp / "runs").run(spec)["lifecycle"]
        self.assertEqual(result["status"], "ROLLBACK_FAILED_AFTER_HEALTH_FAILURE")
        self.assertEqual(result["stage_results"][-1]["exit_code"], 23)
        self.assertEqual(result["rollback_result"]["exit_code"], 23)
        self.assertFalse(result["ok"])

    def test_receipt_rejects_promoted_claim_and_tampering(self) -> None:
        lifecycle = FactoryRuntime(runs_root=self.temp / "runs").run(load_spec(VALID_SPEC))["lifecycle"]
        unsafe = copy.deepcopy(lifecycle["receipt"])
        unsafe["claim"]["production_ready"] = True
        with self.assertRaises(ReceiptIntegrityError):
            ReceiptStore(self.temp / "runs").put(unsafe)
        receipt_path = self.temp / "runs" / lifecycle["receipt_ref"]["path"]
        receipt_path.write_bytes(receipt_path.read_bytes() + b" ")
        with self.assertRaises(ReceiptIntegrityError):
            ReceiptStore(self.temp / "runs").verify(lifecycle["receipt_ref"]["path"])

    def test_receipt_rejects_unapproved_adapter_evidence(self) -> None:
        lifecycle = FactoryRuntime(runs_root=self.temp / "runs").run(
            load_spec(VALID_SPEC)
        )["lifecycle"]

        def rebuild(results: list[dict]) -> None:
            builder = ReceiptBuilder(
                authority_binding(),
                unit_id=lifecycle["receipt"]["unit"]["unit_id"],
                unit_spec_sha256=lifecycle["receipt"]["unit"]["unit_spec_sha256"],
                artifact_manifest_sha256=lifecycle["receipt"]["unit"][
                    "artifact_manifest_sha256"
                ],
            )
            for index, result in enumerate(results, start=1):
                builder.add_event(
                    f"adapter-stage-{index}-{result['stage']}",
                    "adapter.stage.completed",
                    result,
                )
            builder.build(results, "LOCAL_REGRESSION_PASS")

        forged_hash = copy.deepcopy(lifecycle["stage_results"])
        forged_hash[0]["adapter_stub_sha256"] = "0" * 64
        with self.assertRaises(ReceiptIntegrityError):
            rebuild(forged_hash)
        forged_argv = copy.deepcopy(lifecycle["stage_results"])
        forged_argv[0]["argv"][0] = "attacker-controlled-executable"
        with self.assertRaises(ReceiptIntegrityError):
            rebuild(forged_argv)

    def test_receipt_reparse_precheck_has_no_external_write(self) -> None:
        lifecycle = FactoryRuntime(runs_root=self.temp / "source").run(
            load_spec(VALID_SPEC)
        )["lifecycle"]
        guarded_root = self.temp / "guarded"
        sha_root = guarded_root / "sha256"
        sha_root.mkdir(parents=True)
        receipt_module = __import__(
            "dlc_factory.receipt", fromlist=["is_link_or_reparse"]
        )
        real_check = receipt_module.is_link_or_reparse

        def mark_sha_root(path: Path) -> bool:
            return Path(path) == sha_root or real_check(Path(path))

        with patch("dlc_factory.receipt.is_link_or_reparse", side_effect=mark_sha_root):
            with self.assertRaises(ReceiptIntegrityError):
                ReceiptStore(guarded_root).put(lifecycle["receipt"])
        self.assertEqual(list(sha_root.iterdir()), [])

    def test_adapter_stdlib_import_shadow_is_inert(self) -> None:
        spec = load_spec(VALID_SPEC)
        output = self.temp / "unit"
        Materializer().materialize(spec, output)
        (output / "adapters" / "json.py").write_text(
            "from pathlib import Path\nPath('SHADOW_EXECUTED').write_text('bad')\nraise RuntimeError('shadow')\n",
            encoding="utf-8",
        )
        result = LocalAdapterExecutor(output, spec).run_stage("health")
        self.assertTrue(result["ok"])
        self.assertFalse((output / "SHADOW_EXECUTED").exists())


if __name__ == "__main__":
    unittest.main()
