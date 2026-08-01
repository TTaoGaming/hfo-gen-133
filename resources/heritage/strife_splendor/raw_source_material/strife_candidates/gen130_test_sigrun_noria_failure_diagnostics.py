#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "sigrun_noria_failure_diagnostics.py"


def load_module():
    spec = importlib.util.spec_from_file_location("sigrun_noria_failure_diagnostics", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class SigrunNoriaFailureDiagnosticsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mod = load_module()

    def test_replays_existing_p0_p6_quarantine_samples(self) -> None:
        result = self.mod.report(list(self.mod.DEFAULT_RUN_DIRS))

        self.assertEqual(result["status"], "LOCAL_REPLAY_COMPLETE")
        self.assertFalse(result["external_action_performed"])
        self.assertFalse(result["network_call_performed"])
        self.assertFalse(result["secret_values_printed"])
        self.assertIn("family_b_absent", result["aggregate_failure_classes"])
        self.assertIn("family_c_missing_question_id", result["aggregate_failure_classes"])
        self.assertIn("family_c_json_parse_failed", result["aggregate_failure_classes"])
        self.assertTrue(result["can_classify"]["family_b_absent"])
        self.assertTrue(result["can_classify"]["family_c_missing_question_id"])
        self.assertTrue(result["can_classify"]["family_c_json_parse_failed"])
        self.assertEqual([run["sample_count"] for run in result["runs"]], [2, 2])

    def test_schema_id_mismatch_classifier_without_live_call(self) -> None:
        classified = self.mod.classify_ballot(
            json.dumps(
                {
                    "schema_id": "wrong.schema",
                    "ballot_id": "b1",
                    "family_id": "family_c",
                    "question_id": "q1",
                    "vote": "accept",
                    "confidence": 0.5,
                    "native_quorum_effect": False,
                    "external_action_authorized": False,
                    "payload_kind": "public_synthetic",
                }
            ),
            family="family_c",
            question_id="q1",
        )

        self.assertEqual(classified["status"], "invalid")
        self.assertIn("family_c_schema_id_mismatch", classified["failure_classes"])

    def test_local_wrapper_replay_detects_absent_family_b(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "noria-p0-example"
            qdir = run_dir / "quarantine_in"
            qdir.mkdir(parents=True)
            wrapper = {
                "family_key": "family_a",
                "raw_text": json.dumps(
                    {
                        "schema_id": self.mod.BALLOT_SCHEMA,
                        "ballot_id": "a1",
                        "family_id": "family_a",
                        "question_id": "noria-p0-example",
                        "vote": "accept",
                        "confidence": 0.5,
                        "native_quorum_effect": False,
                        "external_action_authorized": False,
                        "payload_kind": "public_synthetic",
                    }
                ),
            }
            (qdir / "noria-p0-example_family_a.raw.json").write_text(json.dumps(wrapper), encoding="utf-8")

            result = self.mod.report([run_dir])

        self.assertIn("family_b_absent", result["aggregate_failure_classes"])
        self.assertIn("family_c_absent", result["aggregate_failure_classes"])
        self.assertEqual(result["runs"][0]["valid_families"], ["family_a"])


if __name__ == "__main__":
    unittest.main()
