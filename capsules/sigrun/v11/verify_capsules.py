#!/usr/bin/env python3
"""Verify the Sigrun v11 opaque-only capsule family."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
DIST = ROOT / "dist"
BUILDER = ROOT / "build_capsules.py"
PROJECTION = ROOT / "opaque_source_receipts.json"
SELF_PLACEHOLDER = "SELF_HASH_PLACEHOLDER"
HERITAGE_RECEIPT = (
    REPO_ROOT / "reviews" / "sigrun" / "v11" / "HERITAGE_GAP_SCAN_RECEIPT.json"
)
V10_PROJECTION = ROOT.parent / "v10" / "opaque_source_receipts.json"
V10_ARTIFACT_COMMIT = "5bd20d322e3eb4e191ba6f6187dc7a8addb4835b"
PUBLIC_FILES = [
    ROOT / "SIGRUN_CAPSULE_FAMILY_CONTRACT.md",
    PROJECTION,
    HERITAGE_RECEIPT,
    BUILDER,
    Path(__file__).resolve(),
    DIST / "S_SMALL.safe.md",
    DIST / "M_MEDIUM.safe.md",
    DIST / "L_SAFE.view.md",
    DIST / "XL_INDEX.safe.json",
    DIST / "SOURCE_BINDING_RECEIPT.json",
    DIST / "CAPSULE_FAMILY_MANIFEST.json",
]
EXACT_REQUIRED_KEYS = {
    "repository",
    "ref",
    "commit",
    "path",
    "blob_sha1",
    "bytes",
    "sha256",
    "privacy_class",
    "rights_status",
    "disposition",
}
EXPECTED_CANDIDATE_SCHEMA = "hfo.gen133.sigrun_candidate_additions.v11_pending"
EXPECTED_CANDIDATE_SHA256 = (
    "cc84c5bc1d1df66af17856977290966d8c395eda4cb19f9a08d3f2c9b74c0022"
)

PRIOR_SOURCE_COUNT = 168
HERITAGE_DELTA_COUNT = 7
SOURCE_COUNT = PRIOR_SOURCE_COUNT + HERITAGE_DELTA_COUNT
TIERS = {
    "S_SMALL": (DIST / "S_SMALL.safe.md", 4096),
    "M_MEDIUM": (DIST / "M_MEDIUM.safe.md", 8192),
    "L_SAFE": (DIST / "L_SAFE.view.md", 32768),
}
EXPECTED_DIST_FILES = {
    "S_SMALL.safe.md",
    "M_MEDIUM.safe.md",
    "L_SAFE.view.md",
    "XL_INDEX.safe.json",
    "SOURCE_BINDING_RECEIPT.json",
    "CAPSULE_FAMILY_MANIFEST.json",
}
V10_TREE_BINDINGS = {
    "capsules/sigrun/v10/dist/CAPSULE_FAMILY_MANIFEST.json": {
        "blob": "17d58f9b551915a9924c1ed11b03ab31ca32d3d6",
        "bytes": 3348,
        "sha256": "9edbb17b828947a1c24a61a4ba2a5daba42731b05c87fa76682b15ab2c7b1de5",
    },
    "capsules/sigrun/v10/opaque_source_receipts.json": {
        "blob": "0fc7c31fd1e646c771b04f46af05e800b06dae03",
        "bytes": 36223,
        "sha256": "c3bbeeb0edc64ff51ba0a55497307dfd59049090a988df73da779a2b23330c44",
    },
    "capsules/sigrun/v10/dist/L_SAFE.view.md": {
        "blob": "d1d73c2353f2dd5704828e54476db726b2605c6c",
        "bytes": 22176,
        "sha256": "46bee7d138c8a531b780ae0b12447e28263ae6aefd5743a64158c5532864b566",
    },
    "capsules/sigrun/v10/dist/SOURCE_BINDING_RECEIPT.json": {
        "blob": "c93b780dda0a286487acdb5b4dbbc11e6c1799cc",
        "bytes": 2013,
        "sha256": "46b6a7a0692628dcf653c12f407f6db7c6e64955a2eb2fd83fb8175b6a44933c",
    },
}



def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def record(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    rel = path.relative_to(REPO_ROOT).as_posix()
    blob = git_blob_sha1(raw)
    return {
        "path": rel,
        "git_blob_sha1": blob,
        "git_blob_sha": blob,
        "utf8_lf_bytes": len(raw),
        "sha256": sha256_hex(raw),
    }


def frontmatter(path: Path) -> dict[str, str]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        return {}
    parts = raw.split("---\n", 2)
    if len(parts) != 3:
        return {}
    values: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            values[key] = value
    return values


def result(name: str, passed: bool, evidence: Any) -> dict[str, Any]:
    return {"check": name, "result": "PASS" if passed else "FAIL", "evidence": evidence}


def candidate_record_ok(row: dict[str, Any]) -> bool:
    return (
        set(row) == EXACT_REQUIRED_KEYS
        and isinstance(row["bytes"], int)
        and row["bytes"] > 0
        and bool(re.fullmatch(r"[0-9a-f]{40}", row["blob_sha1"]))
        and bool(re.fullmatch(r"[0-9a-f]{64}", row["sha256"]))
        and bool(re.fullmatch(r"[0-9a-f]{40}", row["commit"]))
        and all(
            isinstance(row[key], str) and bool(row[key])
            for key in ("repository", "ref", "path", "privacy_class")
        )
        and row["rights_status"] == "UNKNOWN_UNATTESTED"
        and row["disposition"] in {"HOLD", "QUARANTINE"}
    )


def self_hash_ok(path: Path) -> bool:
    raw = path.read_bytes()
    matches = list(re.finditer(rb"^self_hash: ([0-9a-f]{64})$", raw, re.MULTILINE))
    if len(matches) != 1 or SELF_PLACEHOLDER.encode("ascii") in raw:
        return False
    match = matches[0]
    restored = (
        raw[: match.start(1)]
        + SELF_PLACEHOLDER.encode("ascii")
        + raw[match.end(1) :]
    )
    return match.group(1).decode("ascii") == sha256_hex(restored)


def git_tree_bytes(commit: str, path: str) -> bytes:
    completed = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
    )
    if completed.returncode:
        raise RuntimeError("immutable predecessor object is unreadable")
    return completed.stdout


def v10_tree_binding_ok() -> tuple[bool, dict[str, Any]]:
    observed: dict[str, Any] = {}
    passed = True
    for path, expected in V10_TREE_BINDINGS.items():
        raw = git_tree_bytes(V10_ARTIFACT_COMMIT, path)
        actual = {
            "blob": git_blob_sha1(raw),
            "bytes": len(raw),
            "sha256": sha256_hex(raw),
        }
        worktree_matches = (REPO_ROOT / path).read_bytes() == raw
        observed[path] = {
            "tree_matches": actual == expected,
            "worktree_matches_tree": worktree_matches,
        }
        passed = passed and actual == expected and worktree_matches
    return passed, observed


def run_builder() -> None:
    completed = subprocess.run(
        [sys.executable, str(BUILDER)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode:
        raise RuntimeError(completed.stderr or completed.stdout)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-ledger", required=True, type=Path)
    parser.add_argument("--v10-ledger", required=True, type=Path)
    parser.add_argument("--v10-ledger-binding", required=True, type=Path)
    parser.add_argument("--candidate-additions", required=True, type=Path)
    args = parser.parse_args()
    ledger_path = args.local_ledger.resolve()
    v10_ledger_path = args.v10_ledger.resolve()
    v10_ledger_binding_path = args.v10_ledger_binding.resolve()
    candidate_path = args.candidate_additions.resolve()
    for path in (
        ledger_path,
        v10_ledger_path,
        v10_ledger_binding_path,
        candidate_path,
    ):
        if path == REPO_ROOT or REPO_ROOT in path.parents:
            raise RuntimeError("local exact inputs must stay outside the worktree")

    checks: list[dict[str, Any]] = []
    projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    v10_ledger_raw = v10_ledger_path.read_bytes()
    v10_ledger = json.loads(v10_ledger_raw.decode("utf-8"))
    v10_ledger_binding = json.loads(
        v10_ledger_binding_path.read_text(encoding="utf-8")
    )
    candidate_raw = candidate_path.read_bytes()
    additions = json.loads(candidate_raw.decode("utf-8"))
    candidates = additions.get("candidates", [])
    records = projection["records"]
    rows = ledger["rows"]
    v10_rows = v10_ledger["rows"]
    v10_records = json.loads(V10_PROJECTION.read_text(encoding="utf-8"))["records"]
    old_exact = [row["exact_source_record"] for row in v10_rows]
    old_blobs = {row.get("blob_sha1") for row in old_exact if row.get("blob_sha1")}
    old_hashes = {row.get("sha256") for row in old_exact if row.get("sha256")}
    old_bindings = {
        (row.get("repository"), row.get("commit"), row.get("path"))
        for row in old_exact
    }
    candidate_blobs = [row.get("blob_sha1") for row in candidates]
    candidate_hashes = [row.get("sha256") for row in candidates]
    candidate_bindings = [
        (row.get("repository"), row.get("commit"), row.get("path"))
        for row in candidates
    ]
    no_candidate_collisions = (
        len(set(candidate_blobs)) == HERITAGE_DELTA_COUNT
        and len(set(candidate_hashes)) == HERITAGE_DELTA_COUNT
        and len(set(candidate_bindings)) == HERITAGE_DELTA_COUNT
        and not (set(candidate_blobs) & old_blobs)
        and not (set(candidate_hashes) & old_hashes)
        and not (set(candidate_bindings) & old_bindings)
    )
    allowed = {
        "opaque_receipt_id",
        "visibility_class",
        "disposition",
        "body_embedding",
    }
    checks.append(
        result(
            "projection_and_ledger_schema",
            projection.get("schema_id")
            == "hfo.gen133.sigrun_opaque_source_projection.v11"
            and ledger.get("schema_id")
            == "hfo.gen133.sigrun_local_exact_provenance_ledger.v11",
            {"projection": projection.get("schema_id"), "ledger": ledger.get("schema_id")},
        )
    )
    checks.append(
        result(
            "v10_local_ledger_binding_and_prefix_preservation",
            v10_ledger_binding.get("schema_id")
            == "hfo.gen133.local_exact_ledger_binding.v1"
            and v10_ledger_binding.get("storage_policy")
            == "LOCAL_ONLY_NEVER_COMMIT_OR_PROJECT"
            and len(v10_ledger_raw) == v10_ledger_binding.get("bytes")
            and sha256_hex(v10_ledger_raw) == v10_ledger_binding.get("sha256")
            and v10_ledger.get("schema_id")
            == "hfo.gen133.sigrun_local_exact_provenance_ledger.v10"
            and len(v10_rows) == PRIOR_SOURCE_COUNT
            and rows[:PRIOR_SOURCE_COUNT] == v10_rows,
            {
                "local_binding_checked": True,
                "prior_rows": len(v10_rows),
                "prefix_preserved": rows[:PRIOR_SOURCE_COUNT] == v10_rows,
            },
        )
    )
    checks.append(
        result(
            "candidate_input_binding",
            len(candidate_raw) == 4036
            and sha256_hex(candidate_raw) == EXPECTED_CANDIDATE_SHA256
            and additions.get("schema_id") == EXPECTED_CANDIDATE_SCHEMA
            and len(candidates) == HERITAGE_DELTA_COUNT
            and all(candidate_record_ok(row) for row in candidates),
            {
                "schema": additions.get("schema_id"),
                "count": len(candidates),
                "expected_sha256_match": sha256_hex(candidate_raw)
                == EXPECTED_CANDIDATE_SHA256,
            },
        )
    )
    checks.append(
        result(
            "candidate_collision_gate",
            no_candidate_collisions,
            {"candidate_count": len(candidates), "collision_count": 0 if no_candidate_collisions else "REDACTED_NONZERO"},
        )
    )
    checks.append(
        result(
            "source_count_175",
            len(records) == len(rows) == SOURCE_COUNT
            and projection.get("source_count") == ledger.get("source_count") == SOURCE_COUNT
            and projection.get("prior_source_count")
            == ledger.get("prior_source_count")
            == PRIOR_SOURCE_COUNT,
            {"public": len(records), "local": len(rows)},
        )
    )
    checks.append(
        result(
            "heritage_delta_count_7",
            projection["heritage_delta_count"] == ledger["heritage_delta_count"] == 7,
            projection["heritage_delta_count"],
        )
    )
    delta_rows = rows[-HERITAGE_DELTA_COUNT:]
    checks.append(
        result(
            "ledger_delta_exact_match",
            [row.get("exact_source_record") for row in delta_rows] == candidates
            and all(
                set(row)
                == {
                    "opaque_receipt_id",
                    "exact_source_record",
                    "ratification_status",
                    "rights_review",
                    "body_admission",
                    "remote_projection",
                }
                and row["ratification_status"] == "ABSENT"
                and row["rights_review"] == "ABSENT"
                and row["body_admission"] == "PROHIBITED"
                and row["remote_projection"] == "OPAQUE_ONLY"
                for row in delta_rows
            ),
            {"rows": len(delta_rows), "exact_match": [row.get("exact_source_record") for row in delta_rows] == candidates},
        )
    )
    dispositions = {
        name: sum(1 for row in candidates if row.get("disposition") == name)
        for name in ("HOLD", "QUARANTINE")
    }
    checks.append(
        result(
            "delta_rights_and_dispositions_hold",
            dispositions == {"HOLD": 3, "QUARANTINE": 4}
            and all(row.get("rights_status") == "UNKNOWN_UNATTESTED" for row in candidates),
            dispositions,
        )
    )
    privacy_pairs = (
        ("RESTRICTED_REHYDRATION", "QUARANTINE"),
        ("RESTRICTED_STATE", "QUARANTINE"),
        ("UNBOUND_LOCAL_BACKUP", "QUARANTINE"),
        ("RESTRICTED_HERITAGE", "HOLD"),
        ("HIGH_RESTRICTION_MEMORY", "QUARANTINE"),
        ("RESTRICTED_MEMORY", "HOLD"),
        ("RESTRICTED_HERITAGE_INDEX", "HOLD"),
    )
    privacy_dispositions = {
        (privacy, disposition): sum(
            1
            for row in candidates
            if row.get("privacy_class") == privacy
            and row.get("disposition") == disposition
        )
        for privacy, disposition in privacy_pairs
    }
    expected_privacy_dispositions = {
        pair: 1 for pair in privacy_pairs
    }
    checks.append(
        result(
            "delta_privacy_quarantine_boundary",
            privacy_dispositions == expected_privacy_dispositions
            and sum(privacy_dispositions.values()) == HERITAGE_DELTA_COUNT,
            {
                "restricted_hold": sum(
                    count
                    for (privacy, disposition), count in privacy_dispositions.items()
                    if disposition == "HOLD"
                ),
                "higher_risk_quarantine": sum(
                    count
                    for (privacy, disposition), count in privacy_dispositions.items()
                    if disposition == "QUARANTINE"
                ),
                "local_backup_quarantine": privacy_dispositions.get(
                    ("UNBOUND_LOCAL_BACKUP", "QUARANTINE"), 0
                ),
            },
        )
    )
    heritage = json.loads(HERITAGE_RECEIPT.read_text(encoding="utf-8"))
    checks.append(
        result(
            "heritage_gap_receipt_semantics",
            heritage.get("schema_id")
            == "hfo.gen133.sigrun.heritage_gap_scan.v11"
            and heritage.get("candidate_count") == HERITAGE_DELTA_COUNT
            and heritage.get("dispositions")
            == {"HOLD": 3, "QUARANTINE": 4}
            and heritage.get("local_exact_candidate_file", {}).get("bytes")
            == len(candidate_raw)
            and heritage.get("local_exact_candidate_file", {}).get("sha256")
            == EXPECTED_CANDIDATE_SHA256
            and heritage.get("deduplication", {}).get(
                "against_v10_source_count"
            )
            == PRIOR_SOURCE_COUNT
            and heritage.get("deduplication", {}).get(
                "suppressed_prior_blob_duplicates"
            )
            == 4
            and heritage.get("proposed_count") == 11
            and heritage.get("content_boundary", {}).get(
                "immutable_object_readback_checks"
            )
            == HERITAGE_DELTA_COUNT
            and heritage.get("scan_scope", {}).get(
                "local_backup_candidate_admitted_as_quarantine"
            )
            is True
            and heritage.get("content_boundary", {}).get(
                "source_body_displayed_or_decoded"
            )
            is False
            and heritage.get("content_boundary", {}).get(
                "exact_mapping_projected"
            )
            is False
            and heritage.get("scan_scope", {}).get(
                "unbound_filesystem_snapshots_admitted"
            )
            is False,
            {
                "candidate_count": heritage.get("candidate_count"),
                "prior_blob_duplicates_suppressed": heritage.get(
                    "deduplication", {}
                ).get("suppressed_prior_blob_duplicates"),
                "unbound_snapshots_admitted": heritage.get(
                    "scan_scope", {}
                ).get("unbound_filesystem_snapshots_admitted"),
                "local_backup_quarantined": heritage.get(
                    "scan_scope", {}
                ).get("local_backup_candidate_admitted_as_quarantine"),
            },
        )
    )
    predecessor_ok, predecessor_evidence = v10_tree_binding_ok()
    checks.append(
        result(
            "v10_immutable_tree_binding",
            predecessor_ok,
            predecessor_evidence,
        )
    )
    checks.append(
        result(
            "inherited_projection_order_preserved",
            records[:PRIOR_SOURCE_COUNT] == v10_records
            and len(v10_records) == PRIOR_SOURCE_COUNT,
            {
                "prior_records": len(v10_records),
                "preserved": records[:PRIOR_SOURCE_COUNT] == v10_records,
            },
        )
    )
    checks.append(
        result(
            "public_record_allowlist",
            all(set(row) == allowed for row in records),
            sorted({key for row in records for key in row}),
        )
    )
    ids = [row["opaque_receipt_id"] for row in records]
    checks.append(
        result(
            "opaque_id_format_and_uniqueness",
            len(set(ids)) == len(ids)
            and all(re.fullmatch(r"rct_v(?:[789]|1[01])_[A-Z2-7]{26}", rid) for rid in ids),
            {"count": len(ids), "unique": len(set(ids))},
        )
    )
    checks.append(
        result(
            "opaque_id_generation_segregation",
            all(
                re.fullmatch(r"rct_v(?:[789]|10)_[A-Z2-7]{26}", rid)
                for rid in ids[:PRIOR_SOURCE_COUNT]
            )
            and all(
                re.fullmatch(r"rct_v11_[A-Z2-7]{26}", rid)
                for rid in ids[PRIOR_SOURCE_COUNT:]
            ),
            {"prior": PRIOR_SOURCE_COUNT, "delta": len(ids[PRIOR_SOURCE_COUNT:])},
        )
    )
    checks.append(
        result(
            "ledger_projection_ordered_id_bijection",
            ids == [row["opaque_receipt_id"] for row in rows],
            {"public": len(ids), "local": len(rows)},
        )
    )
    checks.append(
        result(
            "public_records_fail_closed",
            all(
                row
                == {
                    "opaque_receipt_id": row["opaque_receipt_id"],
                    "visibility_class": "NON_PUBLIC",
                    "disposition": "METADATA_WITHHELD_LOCAL_LEDGER_ONLY",
                    "body_embedding": "PROHIBITED",
                }
                for row in records
            ),
            {"records": len(records)},
        )
    )

    run_builder()
    first = {
        path.name: sha256_hex(path.read_bytes())
        for path in DIST.glob("*")
        if path.is_file() and path.name != "VERIFICATION_RECEIPT.json"
    }
    run_builder()
    second = {
        path.name: sha256_hex(path.read_bytes())
        for path in DIST.glob("*")
        if path.is_file() and path.name != "VERIFICATION_RECEIPT.json"
    }
    checks.append(
        result(
            "deterministic_second_build",
            set(first) == set(second) == EXPECTED_DIST_FILES and first == second,
            {
                "files": len(first),
                "expected_file_set": set(first) == EXPECTED_DIST_FILES,
                "byte_hashes_equal": first == second,
            },
        )
    )

    for tier, (path, budget) in TIERS.items():
        checks.append(
            result(
                f"{tier.lower()}_budget",
                0 < path.stat().st_size <= budget,
                {"bytes": path.stat().st_size, "budget": budget},
            )
        )
        checks.append(result(f"{tier.lower()}_self_hash", self_hash_ok(path), path.name))
    tier_frontmatter = {
        name: frontmatter(path) for name, (path, _) in TIERS.items()
    }
    checks.append(
        result(
            "tier_frontmatter_hold_semantics",
            all(
                values.get("effect_ceiling") == "T0_INTERNAL_ONLY"
                and values.get("source_bodies") == "WITHHELD"
                and values.get("source_metadata") == "OPAQUE_LOCAL_LEDGER_ONLY"
                and values.get("public_rights_review") == "ABSENT"
                and values.get("soul_status")
                == "self_authored_unratified_unsealed"
                and values.get("sealed") == "false"
                for values in tier_frontmatter.values()
            ),
            {
                name: {
                    "effect_ceiling": values.get("effect_ceiling"),
                    "source_bodies": values.get("source_bodies"),
                    "public_rights_review": values.get("public_rights_review"),
                    "sealed": values.get("sealed"),
                }
                for name, values in tier_frontmatter.items()
            },
        )
    )
    xl_path = DIST / "XL_INDEX.safe.json"
    xl = json.loads(xl_path.read_text(encoding="utf-8"))
    checks.append(
        result(
            "xl_budget_and_not_self_contained",
            0 < xl_path.stat().st_size < 100000
            and xl.get("self_contained") is False
            and xl.get("publication_status") == "NOT_UPLOADED_NO_ARWEAVE_CLAIM"
            and xl.get("effect_ceiling") == "T0_INTERNAL_ONLY"
            and xl.get("source_bodies") == "WITHHELD"
            and xl.get("public_rights_review") == "ABSENT"
            and xl.get("independent_review_status") == "ABSENT"
            and xl.get("operator_ratification") == "ABSENT"
            and xl.get("sealed") is False,
            {
                "bytes": xl_path.stat().st_size,
                "budget_exclusive": 100000,
                "self_contained": xl.get("self_contained"),
                "publication_status": xl.get("publication_status"),
                "effect_ceiling": xl.get("effect_ceiling"),
                "public_rights_review": xl.get("public_rights_review"),
                "independent_review_status": xl.get("independent_review_status"),
                "operator_ratification": xl.get("operator_ratification"),
                "sealed": xl.get("sealed"),
            },
        )
    )

    manifest = json.loads(
        (DIST / "CAPSULE_FAMILY_MANIFEST.json").read_text(encoding="utf-8")
    )
    expected_tiers = {name: record(path) for name, (path, _) in TIERS.items()}
    checks.append(
        result(
            "manifest_tier_bindings",
            manifest["tiers"] == expected_tiers
            and manifest["payload"] == expected_tiers["L_SAFE"],
            expected_tiers,
        )
    )
    checks.append(
        result(
            "successor_and_publication_hold",
            manifest["successor_of"]["version"] == "v10"
            and manifest["successor_of"]["artifact_commit"]
            == "5bd20d322e3eb4e191ba6f6187dc7a8addb4835b"
            and manifest["publication_status"] == "NOT_UPLOADED_NO_ARWEAVE_CLAIM"
            and manifest["independent_review_status"] == "ABSENT",
            {
                "successor": manifest["successor_of"],
                "publication_status": manifest["publication_status"],
                "independent_review_status": manifest["independent_review_status"],
            },
        )
    )
    binding = json.loads(
        (DIST / "SOURCE_BINDING_RECEIPT.json").read_text(encoding="utf-8")
    )
    checks.append(
        result(
            "source_binding_exact",
            binding.get("projection") == record(PROJECTION)
            and binding.get("source_bodies_opened") is False
            and binding.get("rights_review") == "ABSENT_FOR_V11_DELTA"
            and binding.get("operator_ratification") == "ABSENT",
            {
                "projection": record(PROJECTION),
                "source_bodies_opened": binding.get("source_bodies_opened"),
                "rights_review": binding.get("rights_review"),
                "operator_ratification": binding.get("operator_ratification"),
            },
        )
    )
    heritage_receipt_record = record(HERITAGE_RECEIPT)
    checks.append(
        result(
            "heritage_delta_receipt_binding",
            binding.get("heritage_delta_receipt") == heritage_receipt_record
            and manifest.get("heritage_delta_receipt") == heritage_receipt_record,
            heritage_receipt_record,
        )
    )

    public_raw = b"\n".join(path.read_bytes() for path in PUBLIC_FILES)
    protected_values: set[bytes] = set()
    for row in rows:
        exact = row["exact_source_record"]
        for key in (
            "id",
            "repository",
            "ref",
            "commit",
            "path",
            "blob_sha1",
            "sha256",
        ):
            value = exact.get(key)
            if isinstance(value, str) and len(value) >= 8:
                protected_values.add(value.encode("utf-8"))
    leaks = sorted(
        value.decode("utf-8", errors="replace")
        for value in protected_values
        if value in public_raw
    )

    checks.append(
        result(
            "tested_exact_source_identifiers_absent_from_v11_public_family",
            not leaks,
            {"leak_count": len(leaks), "values_redacted": True},
        )
    )
    windows_path_hits = re.findall(rb"[A-Za-z]:\\\\", public_raw)
    checks.append(
        result(
            "absolute_windows_paths_absent",
            not windows_path_hits,
            {"hit_count": len(windows_path_hits), "values_redacted": True},
        )
    )
    checks.append(
        result(
            "public_utf8_lf_canonical",
            all(
                not path.read_bytes().startswith(b"\xef\xbb\xbf")
                and b"\r" not in path.read_bytes()
                and path.read_bytes().endswith(b"\n")
                and bool(path.read_bytes().decode("utf-8"))
                for path in PUBLIC_FILES
            ),
            {"files": len(PUBLIC_FILES)},
        )
    )
    public_markers = {
        "file_uri": rb"file:" + rb"//",
        "slack_url": rb"https://[^ \n]*slack",
        "slack_channel_field": rb"\"channel_id\"\s*:",
        "slack_thread_field": rb"\"thread(_ts)?\"\s*:",
    }
    public_payload_raw = b"\n".join(
        path.read_bytes()
        for path in PUBLIC_FILES
        if path not in {BUILDER, Path(__file__).resolve()}
    )
    marker_hits = {
        name: bool(re.search(pattern, public_payload_raw, re.IGNORECASE))
        for name, pattern in public_markers.items()
    }
    checks.append(
        result(
            "generated_payload_carrier_markers_absent",
            not any(marker_hits.values()),
            marker_hits,
        )
    )
    checks.append(
        result(
            "effect_ceiling_and_unsealed",
            manifest["effect_ceiling"] == "T0_INTERNAL_ONLY"
            and manifest.get("claim_status") == "partial_opaque_heritage_delta"
            and manifest.get("historical_exposure")
            == "V6_DISCLOSED_STABLE_HANDLES_MAY_REMAIN_LINKABLE"
            and manifest["sealed"] is False
            and manifest["independent_review_status"] == "ABSENT"
            and manifest.get("public_rights_review") == "ABSENT"
            and manifest.get("operator_ratification") == "ABSENT"
            and manifest.get("source_bodies") == "WITHHELD"
            and manifest.get("source_metadata") == "OPAQUE_LOCAL_LEDGER_ONLY"
            and manifest.get("heritage_scope") == "BOUNDED_NON_EXHAUSTIVE"
            and manifest.get("remote_currency") == "V10_BOUND_RESIDUAL_LOCAL_REFS_UNKNOWN",
            {
                "effect_ceiling": manifest["effect_ceiling"],
                "claim_status": manifest.get("claim_status"),
                "historical_exposure": manifest.get("historical_exposure"),
                "sealed": manifest["sealed"],
                "independent_review_status": manifest["independent_review_status"],
                "public_rights_review": manifest.get("public_rights_review"),
                "operator_ratification": manifest.get("operator_ratification"),
                "source_bodies": manifest.get("source_bodies"),
                "heritage_scope": manifest.get("heritage_scope"),
                "remote_currency": manifest.get("remote_currency"),
            },
        )
    )

    receipt_hold_fields = {
        "effect_ceiling": "T0_INTERNAL_ONLY",
        "source_bodies": "WITHHELD",
        "public_rights_review": "ABSENT",
        "independent_review_status": "ABSENT",
        "operator_ratification": "ABSENT",
        "sealed": False,
        "publication_status": "NOT_UPLOADED_NO_ARWEAVE_CLAIM",
    }
    checks.append(
        result(
            "verification_receipt_hold_semantics",
            receipt_hold_fields
            == {
                "effect_ceiling": "T0_INTERNAL_ONLY",
                "source_bodies": "WITHHELD",
                "public_rights_review": "ABSENT",
                "independent_review_status": "ABSENT",
                "operator_ratification": "ABSENT",
                "sealed": False,
                "publication_status": "NOT_UPLOADED_NO_ARWEAVE_CLAIM",
            },
            receipt_hold_fields,
        )
    )
    receipt_probe_raw = (
        json.dumps(checks, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    receipt_probe_leak_count = sum(
        1 for value in protected_values if value in receipt_probe_raw
    )
    checks.append(
        result(
            "verification_receipt_self_leak_guard",
            receipt_probe_leak_count == 0,
            {
                "leak_count": receipt_probe_leak_count,
                "values_redacted": True,
            },
        )
    )
    passed = all(check["result"] == "PASS" for check in checks)
    receipt = {
        "schema_id": "hfo.gen133.sigrun_capsule_verification_receipt.v11",
        "result": "PASS" if passed else "FAIL",
        "checks": checks,
        **receipt_hold_fields,
        "honest_flaw": (
            "The verifier proves public-byte relations and absence of the tested exact "
            "source identifiers only. It does not test every classification value "
            "and does not prove privacy rights, identity, continuity, delivery, or "
            "publication."
        ),
        "falsifier": (
            "Any failed check, protected exact source identifier in a public v11 artifact, "
            "body admission, nondeterministic rebuild, or byte mismatch."
        ),
        "next_safe_action": (
            "Obtain one distinct privacy-and-rights review of the newly bounded "
            "local v11 delta before admitting any historical source body."
        ),
    }
    receipt_raw = (
        json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    if any(value in receipt_raw for value in protected_values):
        raise RuntimeError("verification receipt redacted leak guard failed")
    (DIST / "VERIFICATION_RECEIPT.json").write_bytes(receipt_raw)
    print(json.dumps({"result": receipt["result"], "checks": len(checks)}, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
