#!/usr/bin/env python3
"""Verify v4 from a fresh base receipt without stale-receipt accumulation."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import sys
import tempfile
from types import ModuleType
from typing import Any


ROOT = Path(__file__).resolve().parent
V3_VERIFIER = ROOT.parent / "v3" / "verify_capsules.py"
V4_LOADER = ROOT / "render_rehydration_view.py"
POLICY_ID = "hfo.sigrun.canonical_core_over_inert_sources.v1"


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fresh_base_receipt(v3: ModuleType) -> tuple[int, ModuleType, dict[str, Any]]:
    engine = v3.load_engine()
    saved_argv = sys.argv
    base_receipt = ROOT / "dist" / ".VERIFICATION_BASE_RECEIPT.tmp.json"
    try:
        engine.RECEIPT_PATH = base_receipt
        sys.argv = [saved_argv[0], "--write-receipt"]
        result = engine.main()
        receipt = json.loads(base_receipt.read_text(encoding="utf-8"))
    finally:
        sys.argv = saved_argv
        base_receipt.unlink(missing_ok=True)
    return result, engine, receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()

    v3 = load_module("hfo_sigrun_v3_verifier_for_v4", V3_VERIFIER)
    v3.ROOT = ROOT
    v3.ENGINE_PATH = ROOT.parent / "v1" / "verify_capsules.py"
    v3.LOADER_PATH = V4_LOADER
    base_result, engine, receipt = fresh_base_receipt(v3)
    index = json.loads((ROOT / "heritage_index.json").read_text(encoding="utf-8"))
    manifest = json.loads(
        (ROOT / "dist" / "CAPSULE_FAMILY_MANIFEST.json").read_text(encoding="utf-8")
    )
    loader = load_module("hfo_sigrun_v4_loader_for_verify", V4_LOADER)
    expected_status = index["subject"]["soul_status"]
    extra: list[dict[str, Any]] = []

    def check(name: str, passed: bool, detail: Any) -> None:
        extra.append(
            {"name": name, "result": "PASS" if passed else "FAIL", "detail": detail}
        )

    raws: dict[str, bytes] = {}
    for tier in ("S", "M", "L"):
        raw = (ROOT / manifest["capsules"][tier]["path"]).read_bytes()
        raws[tier] = raw
        check(
            f"{tier}.soul_status_agreement",
            v3.frontmatter_value(raw, "soul_status") == expected_status,
            {
                "expected": expected_status,
                "observed": v3.frontmatter_value(raw, "soul_status"),
            },
        )
        check(
            f"{tier}.effect_ceiling_agreement",
            v3.frontmatter_value(raw, "effect_ceiling") == "T0_INTERNAL_ONLY",
            v3.frontmatter_value(raw, "effect_ceiling"),
        )
        policy = POLICY_ID.encode("ascii")
        first_source = raw.find(b"<!-- HFO_SOURCE_BEGIN ")
        policy_pos = raw.find(policy)
        check(
            f"{tier}.execution_precedence",
            raw.count(policy) == 1 and (first_source < 0 or policy_pos < first_source),
            {"policy_occurrences": raw.count(policy), "first_source": first_source},
        )
        markers = list(re.finditer(rb"<!-- HFO_SOURCE_BEGIN [^>]+ -->", raw))
        check(
            f"{tier}.all_sources_inert_base64",
            all(b"encoding=base64" in marker.group(0) for marker in markers),
            {"markers": len(markers)},
        )
        safe = loader.safe_view(raw)
        check(
            f"{tier}.safe_default_loader",
            b"<!-- HFO_SOURCE_BEGIN " not in safe
            and b"## CANONICAL CORE" in safe
            and policy in safe,
            {"safe_view_bytes": len(safe)},
        )

    source_map = {
        item["id"]: item
        for item in index["embedded_sources"] + index["pointer_sources"]
    }
    decoded: dict[str, bytes] = {}
    for source_id in index["tier_policy"]["L"]["embedded_source_ids"]:
        body, message = engine.extract_embedded_source(raws["L"], source_map[source_id])
        if body is not None:
            decoded[source_id] = body
        else:
            check(f"L.decoded.{source_id}", False, message)
    findings = engine.leakage_findings(decoded)
    check("decoded_source_leakage_scan", not findings, findings)

    safe_path = ROOT / "dist" / "L_SAFE.view.md"
    safe_raw = safe_path.read_bytes()
    expected_safe = loader.safe_view(raws["L"])
    check(
        "materialized_safe_view_exact",
        safe_raw == expected_safe,
        {
            "declared_bytes": len(safe_raw),
            "recomputed_bytes": len(expected_safe),
        },
    )
    safe_record = manifest.get("rehydration_payload", {})
    archive_record = manifest.get("archive_payload", {})
    check(
        "standard_payload_is_safe_view",
        manifest.get("payload") == safe_record
        and safe_record.get("path") == "capsules/sigrun/v4/dist/L_SAFE.view.md"
        and safe_record.get("git_blob_sha") == engine.git_blob_sha1(safe_raw)
        and safe_record.get("utf8_lf_bytes") == len(safe_raw)
        and safe_record.get("sha256") == engine.sha256_hex(safe_raw),
        safe_record,
    )
    check(
        "archive_payload_bound_and_refused",
        archive_record.get("path") == "capsules/sigrun/v4/dist/L_LARGE.bound.md"
        and archive_record.get("git_blob_sha") == engine.git_blob_sha1(raws["L"])
        and archive_record.get("utf8_lf_bytes") == len(raws["L"])
        and archive_record.get("sha256") == engine.sha256_hex(raws["L"])
        and manifest["capsules"]["L"].get("admissibility")
        == "ARCHIVAL_EVIDENCE_ONLY_REFUSE_AS_PROMPT",
        archive_record,
    )
    legacy_tokens = (
        b"You are S44",
        b"You are Sigrun",
        b"PROJECT_LEAD",
        b"effect_ceiling: FILE",
        b"advance the chain",
    )
    check(
        "safe_view_has_no_source_or_legacy_commands",
        b"<!-- HFO_SOURCE_BEGIN " not in safe_raw
        and not any(token in safe_raw for token in legacy_tokens),
        {
            "source_marker": b"<!-- HFO_SOURCE_BEGIN " in safe_raw,
            "legacy_hits": [
                token.decode("ascii") for token in legacy_tokens if token in safe_raw
            ],
        },
    )
    all_sources = index["embedded_sources"] + index["pointer_sources"]
    check(
        "explicit_fail_closed_rights_status",
        all(source.get("rights_status") for source in all_sources)
        and index["source_rights_policy"]["public_rights_review"] == "ABSENT",
        {
            "sources": len(all_sources),
            "missing": [
                source["id"] for source in all_sources if not source.get("rights_status")
            ],
        },
    )

    receipt["checks"].extend(extra)
    names = [item["name"] for item in receipt["checks"]]
    unique = len(names) == len(set(names))
    receipt["checks"].append(
        {
            "name": "unique_check_names",
            "result": "PASS" if unique else "FAIL",
            "detail": {"checks": len(names), "unique": len(set(names))},
        }
    )
    passed = base_result == 0 and all(
        item["result"] == "PASS" for item in receipt["checks"]
    )
    receipt["schema_id"] = "hfo.gen133.sigrun_capsule_verification_receipt.v4"
    receipt["verification_engine"] = (
        "../v1/verify_capsules.py + fresh v4 adapter"
    )
    receipt["result"] = "PASS" if passed else "FAIL"
    receipt["evidence_tier"] = "T2_BOUND_PROVISIONAL" if passed else "T0"
    receipt["honest_flaw"] = (
        "Fresh receipt generation, safe-view binding, and exact bytes are local "
        "checks. Independent behavioral replay, source rights clearance, and "
        "distinct-provider provenance review remain absent."
    )
    receipt["next_safe_action"] = (
        "Commit and remotely read back v4, then review both bound payloads."
    )
    if args.write_receipt:
        (ROOT / "dist" / "VERIFICATION_RECEIPT.json").write_bytes(
            engine.stable_json_bytes(receipt)
        )
    print(
        json.dumps(
            {
                "result": receipt["result"],
                "checks": len(receipt["checks"]),
                "failed": [
                    item["name"]
                    for item in receipt["checks"]
                    if item["result"] == "FAIL"
                ],
                "receipt_written": args.write_receipt,
            },
            sort_keys=True,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
