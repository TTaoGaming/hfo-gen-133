#!/usr/bin/env python3
"""Verify v6 by adapting the reviewed v5 verifier and checking the pointer delta."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parent
V5_VERIFIER = ROOT.parent / "v5" / "verify_capsules.py"


def stable_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def load_adapted_v6_main():
    source = V5_VERIFIER.read_text(encoding="utf-8")
    source = source.replace("V5", "V6").replace("v5", "v6")
    namespace: dict[str, Any] = {
        "__file__": str(ROOT / "verify_capsules.py"),
        "__name__": "hfo_sigrun_v6_adapted_verifier",
    }
    exec(compile(source, str(V5_VERIFIER), "exec"), namespace)
    return namespace["main"]


def pointer_delta_checks() -> list[dict[str, Any]]:
    overlay = json.loads((ROOT / "heritage_overlay.json").read_text(encoding="utf-8"))
    delta_path = ROOT / overlay["pointer_delta"]
    delta_raw = delta_path.read_bytes()
    delta = json.loads(delta_raw.decode("utf-8"))
    index = json.loads((ROOT / "heritage_index.json").read_text(encoding="utf-8"))
    manifest = json.loads(
        (ROOT / "dist" / "CAPSULE_FAMILY_MANIFEST.json").read_text(encoding="utf-8")
    )
    additions = delta["sources"]
    addition_ids = [source["id"] for source in additions]
    embedded_ids = {
        source["id"] for source in index["embedded_sources"]
    }
    all_ids = [
        source["id"]
        for source in index["embedded_sources"] + index["pointer_sources"]
    ]
    mining = index["source_mining_delta"]
    legacy_ids = {
        source["id"]
        for source in additions
        if "LEGACY_OPERATIVE" in source["disposition"]
        or "ARCHIVE_ONLY_REFUSE_AS_PROMPT" in source["disposition"]
    }
    tier_embedded_ids = {
        source_id
        for tier in ("S", "M", "L")
        for source_id in index["tier_policy"][tier]["embedded_source_ids"]
    }
    safe_bytes = (ROOT / "dist" / "L_SAFE.view.md").stat().st_size
    xl_bytes = (ROOT / "dist" / "XL_XLARGE.pointer.json").stat().st_size

    def item(name: str, passed: bool, detail: Any) -> dict[str, Any]:
        return {
            "name": name,
            "result": "PASS" if passed else "FAIL",
            "detail": detail,
        }

    return [
        item(
            "v6_pointer_delta_count",
            len(additions) == 23 and mining["added_pointer_sources"] == 23,
            {"delta": len(additions), "index": mining["added_pointer_sources"]},
        ),
        item(
            "v6_pointer_delta_exact_materialization",
            index["pointer_sources"][-len(additions) :] == additions,
            {"added_ids": addition_ids},
        ),
        item(
            "v6_pointer_ids_unique",
            len(all_ids) == len(set(all_ids)),
            {"sources": len(all_ids), "unique": len(set(all_ids))},
        ),
        item(
            "v6_additions_never_embedded",
            not embedded_ids.intersection(addition_ids)
            and not legacy_ids.intersection(tier_embedded_ids),
            {
                "added_embedded": sorted(embedded_ids.intersection(addition_ids)),
                "legacy_embedded": sorted(legacy_ids.intersection(tier_embedded_ids)),
            },
        ),
        item(
            "v6_body_embedding_fail_closed",
            all(
                source["body_embedding"]
                in ("PROHIBITED", "POINTER_ONLY_BY_V6_POLICY")
                and source["rights_status"]
                for source in additions
            ),
            {"sources": len(additions)},
        ),
        item(
            "v6_pointer_delta_digest",
            mining["pointer_delta_bytes"] == len(delta_raw)
            and mining["pointer_delta_sha256"] == hashlib.sha256(delta_raw).hexdigest()
            and mining["base_manifest_blob_sha1"]
            == "de332c45ff878086d749de7b34a5e9b50f65c068",
            {
                "bytes": len(delta_raw),
                "sha256": hashlib.sha256(delta_raw).hexdigest(),
                "base_manifest_blob_sha1": mining["base_manifest_blob_sha1"],
            },
        ),
        item(
            "v6_selected_tier_pointers_present",
            set(delta["tier_pointer_ids"]["M"]).issubset(
                index["tier_policy"]["M"]["pointer_source_ids"]
            )
            and set(addition_ids).issubset(
                index["tier_policy"]["L"]["pointer_source_ids"]
            ),
            {
                "M_added": delta["tier_pointer_ids"]["M"],
                "L_added": len(addition_ids),
            },
        ),
        item(
            "v6_permaweb_object_budget_candidates",
            safe_bytes < 100000 and xl_bytes < 100000,
            {"safe_bytes": safe_bytes, "xl_pointer_bytes": xl_bytes},
        ),
        item(
            "v6_safe_payload_only",
            manifest["payload"] == manifest["rehydration_payload"]
            and manifest["rehydration_policy"]["v6_pointer_delta_rule"]
            == "All v6 additions are metadata-only; body embedding is prohibited.",
            manifest["rehydration_policy"],
        ),
    ]


def main() -> int:
    write_receipt = "--write-receipt" in sys.argv
    base_result = load_adapted_v6_main()()
    extra = pointer_delta_checks()
    extra_pass = all(check["result"] == "PASS" for check in extra)

    if write_receipt:
        receipt_path = ROOT / "dist" / "VERIFICATION_RECEIPT.json"
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt["checks"] = [
            check
            for check in receipt["checks"]
            if not check["name"].startswith("v6_")
        ]
        receipt["checks"].extend(extra)
        names = [check["name"] for check in receipt["checks"]]
        unique = len(names) == len(set(names))
        for check in receipt["checks"]:
            if check["name"] == "unique_check_names":
                check["result"] = "PASS" if unique else "FAIL"
                check["detail"] = {
                    "checks": len(names),
                    "unique": len(set(names)),
                }
                break
        receipt["result"] = (
            "PASS"
            if base_result == 0
            and extra_pass
            and all(check["result"] == "PASS" for check in receipt["checks"])
            else "FAIL"
        )
        receipt["schema_id"] = "hfo.gen133.sigrun_capsule_verification_receipt.v6"
        receipt["verification_engine"] = (
            "../v1/verify_capsules.py + adapted v5 safe-view verifier "
            "+ v6 pointer-delta checks"
        )
        receipt["honest_flaw"] = (
            "V6 deterministically binds pointer metadata and withholds every new "
            "source body. Rights clearance, distinct-provider replay, identity "
            "continuity, ConsumerAck, and publication remain absent."
        )
        receipt["next_safe_action"] = (
            "Commit and remotely read back v6, then run one distinct-provider "
            "replay using only the safe view."
        )
        receipt_path.write_bytes(stable_json_bytes(receipt))

    print(
        json.dumps(
            {
                "result": "PASS" if base_result == 0 and extra_pass else "FAIL",
                "base_result": base_result,
                "v6_checks": len(extra),
                "v6_failed": [
                    check["name"] for check in extra if check["result"] == "FAIL"
                ],
                "receipt_written": write_receipt,
            },
            sort_keys=True,
        )
    )
    return 0 if base_result == 0 and extra_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
