#!/usr/bin/env python3
"""Verify the Sigrun v7 forward-safe public capsule family."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
BUILDER = ROOT / "build_capsules.py"
PUBLIC_FILES = [
    ROOT / "opaque_source_receipts.json",
    DIST / "S_SMALL.safe.md",
    DIST / "M_MEDIUM.safe.md",
    DIST / "L_SAFE.view.md",
    DIST / "XL_INDEX.safe.json",
    DIST / "CAPSULE_FAMILY_MANIFEST.json",
    DIST / "SOURCE_BINDING_RECEIPT.json",
    DIST / "V6_EXPOSURE_CONTAINMENT_RECEIPT.json",
    DIST / "PRIVACY_FAIL_BINDING_RECEIPT.json",
]
ALLOWED_RECORD_KEYS = {
    "opaque_receipt_id",
    "visibility_class",
    "disposition",
    "body_embedding",
}


def stable_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def payload_record(repo_path: str, raw: bytes) -> dict[str, Any]:
    return {
        "path": repo_path,
        "git_blob_sha1": git_blob_sha1(raw),
        "utf8_lf_bytes": len(raw),
        "sha256": sha256_hex(raw),
    }


def load_builder():
    spec = importlib.util.spec_from_file_location("hfo_sigrun_v7_builder", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load v7 builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def self_hash_pass(raw: bytes) -> bool:
    match = re.search(rb"(?m)^self_hash: ([0-9a-f]{64})$", raw)
    if not match:
        return False
    restored = (
        raw[: match.start(1)]
        + b"SELF_HASH_PLACEHOLDER"
        + raw[match.end(1) :]
    )
    return sha256_hex(restored) == match.group(1).decode("ascii")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-ledger", type=Path)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()

    projection = json.loads(
        (ROOT / "opaque_source_receipts.json").read_text(encoding="utf-8")
    )
    records = projection["records"]
    public_raw = {path: path.read_bytes() for path in PUBLIC_FILES}
    public_joined = b"\n".join(public_raw.values())
    manifest = json.loads(
        (DIST / "CAPSULE_FAMILY_MANIFEST.json").read_text(encoding="utf-8")
    )
    xl_index = json.loads(
        (DIST / "XL_INDEX.safe.json").read_text(encoding="utf-8")
    )
    containment = json.loads(
        (DIST / "V6_EXPOSURE_CONTAINMENT_RECEIPT.json").read_text(encoding="utf-8")
    )
    privacy_fail = json.loads(
        (DIST / "PRIVACY_FAIL_BINDING_RECEIPT.json").read_text(encoding="utf-8")
    )

    checks: list[dict[str, Any]] = []

    def check(name: str, passed: bool, detail: Any) -> None:
        checks.append(
            {"name": name, "result": "PASS" if passed else "FAIL", "detail": detail}
        )

    check(
        "public_files_utf8_lf",
        all(
            not raw.startswith(b"\xef\xbb\xbf")
            and b"\r" not in raw
            and raw.endswith(b"\n")
            for raw in public_raw.values()
        ),
        {"files": len(public_raw)},
    )
    check(
        "source_count",
        projection["source_count"] == len(records) == 53,
        {"declared": projection["source_count"], "actual": len(records)},
    )
    check(
        "record_schema_allowlist",
        all(set(record) == ALLOWED_RECORD_KEYS for record in records),
        {"allowed_fields": sorted(ALLOWED_RECORD_KEYS)},
    )
    check(
        "record_values_fail_closed",
        all(
            record["visibility_class"] == "NON_PUBLIC"
            and record["disposition"] == "METADATA_WITHHELD_LOCAL_LEDGER_ONLY"
            and record["body_embedding"] == "PROHIBITED"
            for record in records
        ),
        {"records": len(records)},
    )
    receipt_ids = [record["opaque_receipt_id"] for record in records]
    check(
        "opaque_id_format_and_uniqueness",
        len(receipt_ids) == len(set(receipt_ids))
        and all(re.fullmatch(r"rct_v7_[A-Z2-7]{26}", rid) for rid in receipt_ids),
        {"records": len(receipt_ids), "unique": len(set(receipt_ids))},
    )
    check(
        "remote_sensitive_token_scan",
        not any(
            token.lower() in public_joined.lower()
            for token in (
                b"operator_note",
                b"ttao-notes",
                b"SLACK_CONTEXT",
                b"LOCAL_PATH_CONTEXT",
            )
        ),
        {"forbidden_matches": 0},
    )
    check(
        "no_source_bodies_or_legacy_markers",
        b"HFO_SOURCE" not in public_joined
        and b"BEGIN SOURCE" not in public_joined
        and b"base64_inert_evidence" not in public_joined,
        {"body_markers": 0},
    )
    tier_paths = {
        "S_SMALL": DIST / "S_SMALL.safe.md",
        "M_MEDIUM": DIST / "M_MEDIUM.safe.md",
        "L_SAFE": DIST / "L_SAFE.view.md",
    }
    check(
        "tier_self_hashes",
        all(self_hash_pass(path.read_bytes()) for path in tier_paths.values()),
        {"tiers": list(tier_paths)},
    )
    check(
        "tier_budgets",
        tier_paths["S_SMALL"].stat().st_size <= 4096
        and tier_paths["M_MEDIUM"].stat().st_size <= 32768
        and tier_paths["L_SAFE"].stat().st_size < 100000,
        {name: path.stat().st_size for name, path in tier_paths.items()},
    )
    expected_tiers = {
        name: payload_record(
            f"capsules/sigrun/v7/dist/{path.name}", path.read_bytes()
        )
        for name, path in tier_paths.items()
    }
    check(
        "manifest_tier_bindings",
        manifest["tiers"] == expected_tiers and manifest["payload"] == expected_tiers["L_SAFE"],
        manifest["tiers"],
    )
    check(
        "xl_tier_bindings",
        xl_index["tiers"] == expected_tiers
        and xl_index["recommended_rehydration_payload"] == expected_tiers["L_SAFE"],
        {"payload": xl_index["recommended_rehydration_payload"]},
    )
    check(
        "permaweb_candidates_under_100kb",
        tier_paths["L_SAFE"].stat().st_size < 100000
        and (DIST / "XL_INDEX.safe.json").stat().st_size < 100000,
        {
            "safe_bytes": tier_paths["L_SAFE"].stat().st_size,
            "index_bytes": (DIST / "XL_INDEX.safe.json").stat().st_size,
        },
    )
    check(
        "publication_not_claimed",
        manifest["publication_status"] == "NOT_UPLOADED_NO_ARWEAVE_CLAIM"
        and xl_index["publication_status"] == "NOT_UPLOADED_NO_ARWEAVE_CLAIM",
        {"publication_status": manifest["publication_status"]},
    )
    check(
        "v6_exposure_honest_containment",
        containment["erasure_claim"] is False
        and containment["operator_ratification"] == "ABSENT"
        and "clones and caches" in containment["residual_risk"],
        containment,
    )
    check(
        "privacy_fail_exact_binding",
        privacy_fail["trigger"]["commit"]
        == "29b358da17d488a70d22d9f493eb1d0dd44464f1"
        and privacy_fail["trigger"]["git_blob_sha1"]
        == "03b330a0cd20185ab3ec0a71d187a7a15728f2f7"
        and privacy_fail["trigger"]["sha256"]
        == "7db251ac1a9de0759482ed484877917a7665a313426beb21ad76210f599881a2"
        and privacy_fail["trigger"]["reviewed_candidate_blob"]
        == "d110a58b5a75af7949075c230e5a094061813c33"
        and privacy_fail["trigger"]["vote"] == "FAIL",
        privacy_fail["trigger"],
    )
    builder = load_builder()
    held_out = builder.public_record("rct_v7_7K4QJ3Y6M2NP8CX5WV9RT1BHFD")
    check(
        "held_out_private_source_sanitizer",
        set(held_out) == ALLOWED_RECORD_KEYS
        and "repository" not in held_out
        and "path" not in held_out
        and "sha256" not in held_out,
        held_out,
    )
    ledger_result = "ABSENT"
    ledger_matches = False
    leak_matches: list[str] = []
    if args.local_ledger and args.local_ledger.exists():
        ledger = json.loads(args.local_ledger.read_text(encoding="utf-8"))
        ledger_ids = [
            row["opaque_receipt_id"] for row in ledger["rows"]
        ]
        ledger_matches = ledger_ids == receipt_ids
        for row in ledger["rows"]:
            exact = row["exact_source_record"]
            for key, value in exact.items():
                if key not in {
                    "id",
                    "repository",
                    "repo_alias",
                    "commit",
                    "path",
                    "blob_sha1",
                    "sha256",
                    "privacy_class",
                    "rights_status",
                }:
                    continue
                if not isinstance(value, str) or len(value) < 8:
                    continue
                if value.encode("utf-8") in public_joined:
                    leak_matches.append(f"{row['opaque_receipt_id']}:{key}")
        ledger_result = "PASS" if ledger_matches and not leak_matches else "FAIL"
    check(
        "local_ledger_projection_alignment",
        ledger_result == "PASS",
        {
            "result": ledger_result,
            "ids_match": ledger_matches,
            "protected_value_matches": leak_matches,
        },
    )
    check(
        "unique_check_names",
        len({item["name"] for item in checks}) == len(checks),
        {"checks": len(checks)},
    )
    passed = all(item["result"] == "PASS" for item in checks)
    if args.write_receipt:
        receipt = {
            "schema_id": "hfo.gen133.sigrun_capsule_verification_receipt.v7",
            "result": "PASS" if passed else "FAIL",
            "checks": checks,
            "effect_ceiling": "T0_INTERNAL_ONLY",
            "independent_review": "ABSENT",
            "honest_flaw": (
                "V7 is forward-safe and locally provenance-resolvable, but v6 "
                "metadata remains disclosed in Git history and may persist in "
                "clones or caches. Rights, identity, independent replay, "
                "ConsumerAck, and permaweb publication remain absent."
            ),
            "falsifier": (
                "Any protected local-ledger value in a public v7 artifact, "
                "opaque-ID mapping disclosure, body admission, byte mismatch, "
                "budget overflow, or distinct behavior defect."
            ),
            "next_safe_action": (
                "Run one distinct-provider no-write behavioral replay using "
                "only the exact L_SAFE v7 payload."
            ),
        }
        (DIST / "VERIFICATION_RECEIPT.json").write_bytes(stable_json_bytes(receipt))
    print(
        json.dumps(
            {
                "result": "PASS" if passed else "FAIL",
                "checks": len(checks),
                "failed": [
                    item["name"] for item in checks if item["result"] == "FAIL"
                ],
            },
            sort_keys=True,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
