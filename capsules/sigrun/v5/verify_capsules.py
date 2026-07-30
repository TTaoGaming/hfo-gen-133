#!/usr/bin/env python3
"""Verify v5 from a fresh base receipt and a self-sealed safe view."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from types import ModuleType
from typing import Any


ROOT = Path(__file__).resolve().parent
V3_VERIFIER = ROOT.parent / "v3" / "verify_capsules.py"
V4_VERIFIER = ROOT.parent / "v4" / "verify_capsules.py"
V5_LOADER = ROOT / "render_rehydration_view.py"
POLICY_ID = "hfo.sigrun.canonical_core_over_inert_sources.v1"
SELF_PLACEHOLDER = "SELF_HASH_PLACEHOLDER"


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frontmatter_value(raw: bytes, key: str) -> str | None:
    end = raw.find(b"\n---\n", 4)
    if end < 0:
        return None
    match = re.search(
        rb"(?m)^" + re.escape(key.encode("ascii")) + rb": ([^\r\n]+)$",
        raw[: end + 1],
    )
    return match.group(1).decode("utf-8") if match else None


def safe_self_hash(raw: bytes) -> tuple[str | None, str | None]:
    declared = frontmatter_value(raw, "self_hash")
    if declared is None:
        return None, None
    marker = f"self_hash: {declared}\n".encode("ascii")
    if raw.count(marker) != 1:
        return declared, None
    placeholder = raw.replace(
        marker, f"self_hash: {SELF_PLACEHOLDER}\n".encode("ascii"), 1
    )
    return declared, hashlib.sha256(placeholder).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()

    v3 = load_module("hfo_sigrun_v3_verifier_for_v5", V3_VERIFIER)
    v3.ROOT = ROOT
    v3.ENGINE_PATH = ROOT.parent / "v1" / "verify_capsules.py"
    v3.LOADER_PATH = V5_LOADER
    v4 = load_module("hfo_sigrun_v4_verifier_for_v5", V4_VERIFIER)
    v4.ROOT = ROOT
    saved_argv = sys.argv
    try:
        sys.argv = [saved_argv[0]]
        base_result, engine, receipt = v4.fresh_base_receipt(v3)
    finally:
        sys.argv = saved_argv

    index = json.loads((ROOT / "heritage_index.json").read_text(encoding="utf-8"))
    manifest = json.loads(
        (ROOT / "dist" / "CAPSULE_FAMILY_MANIFEST.json").read_text(encoding="utf-8")
    )
    loader = load_module("hfo_sigrun_v5_loader_for_verify", V5_LOADER)
    extra: list[dict[str, Any]] = []

    def check(name: str, passed: bool, detail: Any) -> None:
        extra.append(
            {"name": name, "result": "PASS" if passed else "FAIL", "detail": detail}
        )

    raws: dict[str, bytes] = {}
    expected_status = index["subject"]["soul_status"]
    for tier in ("S", "M", "L"):
        raw = (ROOT / manifest["capsules"][tier]["path"]).read_bytes()
        raws[tier] = raw
        check(
            f"{tier}.semantic_envelope",
            frontmatter_value(raw, "soul_status") == expected_status
            and frontmatter_value(raw, "effect_ceiling") == "T0_INTERNAL_ONLY"
            and raw.count(POLICY_ID.encode("ascii")) == 1
            and (
                raw.find(b"<!-- HFO_SOURCE_BEGIN ") < 0
                or raw.find(POLICY_ID.encode("ascii"))
                < raw.find(b"<!-- HFO_SOURCE_BEGIN ")
            ),
            {
                "soul_status": frontmatter_value(raw, "soul_status"),
                "effect_ceiling": frontmatter_value(raw, "effect_ceiling"),
            },
        )
        markers = list(re.finditer(rb"<!-- HFO_SOURCE_BEGIN [^>]+ -->", raw))
        check(
            f"{tier}.all_sources_inert_base64",
            all(b"encoding=base64" in marker.group(0) for marker in markers),
            {"markers": len(markers)},
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

    safe_raw = (ROOT / "dist" / "L_SAFE.view.md").read_bytes()
    recomputed_safe = loader.safe_view(raws["L"])
    declared_self, recomputed_self = safe_self_hash(safe_raw)
    safe_record = manifest["rehydration_payload"]
    archive_record = manifest["archive_payload"]
    check(
        "dedicated_safe_view_schema",
        frontmatter_value(safe_raw, "schema_id")
        == "hfo.gen133.sigrun_safe_rehydration_view.v5"
        and frontmatter_value(safe_raw, "view_kind") == "SAFE_REHYDRATION_INPUT"
        and frontmatter_value(safe_raw, "source_bodies") == "WITHHELD"
        and frontmatter_value(safe_raw, "archive_git_blob_sha1")
        == engine.git_blob_sha1(raws["L"])
        and frontmatter_value(safe_raw, "archive_sha256")
        == engine.sha256_hex(raws["L"]),
        {
            "schema_id": frontmatter_value(safe_raw, "schema_id"),
            "view_kind": frontmatter_value(safe_raw, "view_kind"),
        },
    )
    check(
        "safe_view_self_hash",
        declared_self is not None and declared_self == recomputed_self,
        {"declared": declared_self, "recomputed": recomputed_self},
    )
    check(
        "materialized_safe_view_exact",
        safe_raw == recomputed_safe,
        {"bytes": len(safe_raw)},
    )
    check(
        "safe_and_archive_payload_bindings",
        manifest["payload"] == safe_record
        and safe_record.get("path") == "capsules/sigrun/v5/dist/L_SAFE.view.md"
        and safe_record.get("git_blob_sha") == engine.git_blob_sha1(safe_raw)
        and safe_record.get("utf8_lf_bytes") == len(safe_raw)
        and safe_record.get("sha256") == engine.sha256_hex(safe_raw)
        and archive_record.get("path")
        == "capsules/sigrun/v5/dist/L_LARGE.bound.md"
        and archive_record.get("git_blob_sha") == engine.git_blob_sha1(raws["L"])
        and manifest["capsules"]["L"].get("admissibility")
        == "ARCHIVAL_EVIDENCE_ONLY_REFUSE_AS_PROMPT",
        {"safe": safe_record, "archive": archive_record},
    )
    legacy_tokens = (
        b"<!-- HFO_SOURCE_BEGIN ",
        b"You are S44",
        b"You are Sigrun",
        b"PROJECT_LEAD",
        b"effect_ceiling: FILE",
        b"advance the chain",
    )
    check(
        "safe_view_has_no_source_or_legacy_commands",
        not any(token in safe_raw for token in legacy_tokens),
        {
            "hits": [
                token.decode("ascii") for token in legacy_tokens if token in safe_raw
            ]
        },
    )
    all_sources = index["embedded_sources"] + index["pointer_sources"]
    check(
        "explicit_fail_closed_rights_status",
        all(source.get("rights_status") for source in all_sources)
        and index["source_rights_policy"]["public_rights_review"] == "ABSENT",
        {"sources": len(all_sources)},
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
    receipt["schema_id"] = "hfo.gen133.sigrun_capsule_verification_receipt.v5"
    receipt["verification_engine"] = (
        "../v1/verify_capsules.py + fresh v5 safe-view adapter"
    )
    receipt["result"] = "PASS" if passed else "FAIL"
    receipt["evidence_tier"] = "T2_BOUND_PROVISIONAL" if passed else "T0"
    receipt["honest_flaw"] = (
        "The dedicated safe view and archive are locally verified. Independent "
        "behavioral replay, source rights clearance, and distinct-provider "
        "provenance review remain absent."
    )
    receipt["next_safe_action"] = (
        "Commit and remotely read back v5, then review both bound payloads."
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
