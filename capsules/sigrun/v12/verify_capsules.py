#!/usr/bin/env python3
"""Verify the Sigrun v12 opaque-only successor and root bundle."""

from __future__ import annotations

import argparse
import base64
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
RECEIPT_BUILDER = ROOT / "build_receipt.py"
PROJECTION = ROOT / "opaque_source_receipts.json"
V11_PROJECTION = ROOT.parent / "v11" / "opaque_source_receipts.json"
HERITAGE_RECEIPT = (
    REPO_ROOT / "reviews" / "sigrun" / "v12" / "HERITAGE_GAP_SCAN_RECEIPT.json"
)
COVERAGE_RECEIPT = (
    REPO_ROOT / "reviews" / "sigrun" / "v12" / "HERITAGE_COVERAGE_RECEIPT.json"
)
REVIEW_ROOT = REPO_ROOT / "reviews" / "sigrun" / "v12"
V11_ARTIFACT_COMMIT = "35bb33162f58ee3c2a43e00c33a40a8f5666dddf"
EXPECTED_CANDIDATE_SCHEMA = (
    "hfo.gen133.sigrun_candidate_additions.v12_personal_ops_pending"
)
EXPECTED_CANDIDATE_BYTES = 9284
EXPECTED_CANDIDATE_SHA256 = (
    "323578294c2ec8123a187dc748b628d1751956e3178c4742b9a1e0b314301bb7"
)
PRIOR_SOURCE_COUNT = 175
HERITAGE_DELTA_COUNT = 8
SOURCE_COUNT = 183
SELF_PLACEHOLDER = "SELF_HASH_PLACEHOLDER"
EXACT_REQUIRED_KEYS = {
    "repo_root",
    "remote",
    "ref",
    "commit",
    "path",
    "blob_sha1",
    "bytes",
    "privacy_class",
    "disposition",
    "reason",
}
ALLOWED_PUBLIC_KEYS = {
    "opaque_receipt_id",
    "visibility_class",
    "disposition",
    "body_embedding",
}
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
    "ROOT_BUNDLE.safe.json",
    "PERMAWEB_PREUPLOAD_PACKET.hold.json",
}
V11_TREE_BINDINGS = {
    "capsules/sigrun/v11/dist/CAPSULE_FAMILY_MANIFEST.json": {
        "blob": "aa0095f2edf3954a0fb288d1461f715c0d0e5102",
        "bytes": 3342,
        "sha256": "754173de95112ef95dd7a5a1e7b0b1b005043d7e0ccdc708b30a306469e71277",
    },
    "capsules/sigrun/v11/dist/L_SAFE.view.md": {
        "blob": "654ceb0bf85030b0ba2cce5ac0dce86eadf778f8",
        "bytes": 22918,
        "sha256": "366e223167424ad048096195c2fa395cbb9e4757cf42c1636aadd89714ef7b92",
    },
    "capsules/sigrun/v11/dist/SOURCE_BINDING_RECEIPT.json": {
        "blob": "02674c6304a799d2cc79747ae4e5b1e7f96ea9ed",
        "bytes": 2012,
        "sha256": "47bf687613fd72f5cf2ea307cec45cfdb37a869b5c20a85d178e2c178d44da91",
    },
    "capsules/sigrun/v11/opaque_source_receipts.json": {
        "blob": "d61b9b56dfb456f1af5e3b6e31f8bdf63c21c777",
        "bytes": 37727,
        "sha256": "974aa8705dea37689ae5264776eb46651ceeb6e8c2b8e12ea785d94b03788279",
    },
}


def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def record(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    blob = git_blob_sha1(raw)
    return {
        "path": path.relative_to(REPO_ROOT).as_posix(),
        "git_blob_sha1": blob,
        "git_blob_sha": blob,
        "utf8_lf_bytes": len(raw),
        "sha256": sha256_hex(raw),
    }


def check(name: str, passed: bool, evidence: Any) -> dict[str, Any]:
    return {"check": name, "result": "PASS" if passed else "FAIL", "evidence": evidence}


def candidate_ok(row: dict[str, Any]) -> bool:
    return (
        set(row) == EXACT_REQUIRED_KEYS
        and isinstance(row["bytes"], int)
        and row["bytes"] > 0
        and bool(re.fullmatch(r"[0-9a-f]{40}", row["blob_sha1"]))
        and bool(re.fullmatch(r"[0-9a-f]{40}", row["commit"]))
        and all(
            isinstance(row[key], str) and bool(row[key])
            for key in EXACT_REQUIRED_KEYS - {"bytes"}
        )
        and row["privacy_class"] == "PRIVATE_PERSONAL_OPS_METADATA_ONLY"
        and row["disposition"] == "QUARANTINE_NON_PUBLIC"
        and "BODY_UNOPENED" in row["reason"]
    )


def git_metadata_binding(row: dict[str, Any]) -> bool:
    repo = Path(row["repo_root"]).resolve()
    if repo == REPO_ROOT or REPO_ROOT in repo.parents:
        return False
    blob = subprocess.run(
        ["git", "rev-parse", f"{row['commit']}:{row['path']}"],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    if blob.returncode:
        return False
    observed = blob.stdout.strip()
    size = subprocess.run(
        ["git", "cat-file", "-s", observed],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    return (
        size.returncode == 0
        and observed == row["blob_sha1"]
        and int(size.stdout.strip()) == row["bytes"]
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


def predecessor_binding_ok() -> tuple[bool, dict[str, Any]]:
    evidence: dict[str, Any] = {}
    passed = True
    for path, expected in V11_TREE_BINDINGS.items():
        raw = git_tree_bytes(V11_ARTIFACT_COMMIT, path)
        actual = {
            "blob": git_blob_sha1(raw),
            "bytes": len(raw),
            "sha256": sha256_hex(raw),
        }
        worktree_match = (REPO_ROOT / path).read_bytes() == raw
        evidence[path] = {
            "tree_matches": actual == expected,
            "worktree_matches_tree": worktree_match,
        }
        passed = passed and actual == expected and worktree_match
    return passed, evidence


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
    parser.add_argument("--v11-ledger", required=True, type=Path)
    parser.add_argument("--v11-ledger-binding", required=True, type=Path)
    parser.add_argument("--candidate-additions", required=True, type=Path)
    args = parser.parse_args()
    ledger_path = args.local_ledger.resolve()
    v11_ledger_path = args.v11_ledger.resolve()
    v11_binding_path = args.v11_ledger_binding.resolve()
    candidate_path = args.candidate_additions.resolve()
    for path in (ledger_path, v11_ledger_path, v11_binding_path, candidate_path):
        if path == REPO_ROOT or REPO_ROOT in path.parents:
            raise RuntimeError("local exact inputs must stay outside the worktree")

    checks: list[dict[str, Any]] = []
    projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    v11_ledger_raw = v11_ledger_path.read_bytes()
    v11_ledger = json.loads(v11_ledger_raw.decode("utf-8"))
    v11_binding = json.loads(v11_binding_path.read_text(encoding="utf-8"))
    candidate_raw = candidate_path.read_bytes()
    additions = json.loads(candidate_raw.decode("utf-8"))
    candidates = additions.get("candidates", [])
    records = projection.get("records", [])
    rows = ledger.get("rows", [])
    old_rows = v11_ledger.get("rows", [])
    old_records = json.loads(V11_PROJECTION.read_text(encoding="utf-8")).get(
        "records", []
    )

    checks.append(
        check(
            "schema_and_source_counts",
            projection.get("schema_id")
            == "hfo.gen133.sigrun_opaque_source_projection.v12"
            and ledger.get("schema_id")
            == "hfo.gen133.sigrun_local_exact_provenance_ledger.v12"
            and len(records) == len(rows) == SOURCE_COUNT
            and projection.get("source_count")
            == ledger.get("source_count")
            == SOURCE_COUNT
            and projection.get("prior_source_count")
            == ledger.get("prior_source_count")
            == PRIOR_SOURCE_COUNT
            and projection.get("heritage_delta_count")
            == ledger.get("heritage_delta_count")
            == HERITAGE_DELTA_COUNT,
            {"source_count": len(records), "delta_count": HERITAGE_DELTA_COUNT},
        )
    )
    checks.append(
        check(
            "v11_local_binding_and_full_prefix",
            v11_binding.get("schema_id")
            == "hfo.gen133.local_exact_ledger_binding.v1"
            and v11_binding.get("storage_policy")
            == "LOCAL_ONLY_NEVER_COMMIT_OR_PROJECT"
            and v11_binding.get("bytes") == len(v11_ledger_raw)
            and v11_binding.get("sha256") == sha256_hex(v11_ledger_raw)
            and len(old_rows) == PRIOR_SOURCE_COUNT
            and rows[:PRIOR_SOURCE_COUNT] == old_rows
            and records[:PRIOR_SOURCE_COUNT] == old_records,
            {
                "prior_rows": len(old_rows),
                "private_prefix_preserved": rows[:PRIOR_SOURCE_COUNT] == old_rows,
                "public_prefix_preserved": records[:PRIOR_SOURCE_COUNT] == old_records,
            },
        )
    )
    checks.append(
        check(
            "candidate_packet_exact_binding",
            len(candidate_raw) == EXPECTED_CANDIDATE_BYTES
            and sha256_hex(candidate_raw) == EXPECTED_CANDIDATE_SHA256
            and additions.get("schema_id") == EXPECTED_CANDIDATE_SCHEMA
            and additions.get("candidate_bodies_opened") is False
            and len(candidates) == HERITAGE_DELTA_COUNT
            and all(candidate_ok(row) for row in candidates),
            {
                "bytes": len(candidate_raw),
                "sha256_match": sha256_hex(candidate_raw)
                == EXPECTED_CANDIDATE_SHA256,
                "candidate_count": len(candidates),
                "bodies_opened": additions.get("candidate_bodies_opened"),
            },
        )
    )
    old_blobs = {
        row["exact_source_record"].get("blob_sha1")
        for row in old_rows
        if row.get("exact_source_record", {}).get("blob_sha1")
    }
    candidate_blobs = [row.get("blob_sha1") for row in candidates]
    candidate_bindings = [
        (row.get("remote"), row.get("commit"), row.get("path"))
        for row in candidates
    ]
    collision_free = (
        len(set(candidate_blobs)) == HERITAGE_DELTA_COUNT
        and len(set(candidate_bindings)) == HERITAGE_DELTA_COUNT
        and not (set(candidate_blobs) & old_blobs)
    )
    checks.append(
        check(
            "candidate_collision_and_metadata_only_object_binding",
            collision_free and all(git_metadata_binding(row) for row in candidates),
            {
                "candidate_count": len(candidates),
                "collision_count": 0 if collision_free else "REDACTED_NONZERO",
                "body_reads": 0,
            },
        )
    )
    delta_rows = rows[-HERITAGE_DELTA_COUNT:]
    checks.append(
        check(
            "ledger_delta_exact_and_quarantined",
            [row.get("exact_source_record") for row in delta_rows] == candidates
            and all(
                row.get("ratification_status") == "ABSENT"
                and row.get("rights_review") == "ABSENT"
                and row.get("body_admission") == "PROHIBITED"
                and row.get("remote_projection") == "OPAQUE_ONLY"
                for row in delta_rows
            ),
            {"delta_rows": len(delta_rows), "quarantine_count": len(candidates)},
        )
    )
    consumption = ledger.get("candidate_packet_consumption", {})
    checks.append(
        check(
            "candidate_consumed_once_receipt",
            consumption
            == {
                "state": "CONSUMED_EXACTLY_ONCE_DURING_INITIALIZATION",
                "schema_id": EXPECTED_CANDIDATE_SCHEMA,
                "bytes": EXPECTED_CANDIDATE_BYTES,
                "sha256": EXPECTED_CANDIDATE_SHA256,
                "candidate_count": HERITAGE_DELTA_COUNT,
            }
            and ledger.get("source_bodies_opened_by_v12_builder") is False,
            {"state": consumption.get("state"), "body_reads": 0},
        )
    )
    checks.append(
        check(
            "public_record_allowlist_and_fail_closed",
            all(
                set(row) == ALLOWED_PUBLIC_KEYS
                and row.get("visibility_class") == "NON_PUBLIC"
                and row.get("disposition") == "METADATA_WITHHELD_LOCAL_LEDGER_ONLY"
                and row.get("body_embedding") == "PROHIBITED"
                for row in records
            ),
            {"record_count": len(records), "allowed_keys": sorted(ALLOWED_PUBLIC_KEYS)},
        )
    )
    ids = [row["opaque_receipt_id"] for row in records]
    checks.append(
        check(
            "opaque_id_format_uniqueness_and_generation_separation",
            len(set(ids)) == SOURCE_COUNT
            and all(
                re.fullmatch(r"rct_v(?:[789]|1[01])_[A-Z2-7]{26}", rid)
                for rid in ids[:PRIOR_SOURCE_COUNT]
            )
            and all(
                re.fullmatch(r"rct_v12_[A-Z2-7]{26}", rid)
                for rid in ids[PRIOR_SOURCE_COUNT:]
            )
            and ids == [row["opaque_receipt_id"] for row in rows],
            {"total": len(ids), "unique": len(set(ids)), "v12_delta": 8},
        )
    )

    heritage = json.loads(HERITAGE_RECEIPT.read_text(encoding="utf-8"))
    coverage = json.loads(COVERAGE_RECEIPT.read_text(encoding="utf-8"))
    checks.append(
        check(
            "aggregate_heritage_receipts",
            heritage.get("schema_id") == "hfo.gen133.sigrun.heritage_gap_scan.v12"
            and heritage.get("candidate_count") == 8
            and heritage.get("dispositions") == {"QUARANTINE_NON_PUBLIC": 8}
            and heritage.get("content_boundary", {}).get("candidate_bodies_opened")
            is False
            and heritage.get("content_boundary", {}).get("exact_mapping_projected")
            is False
            and coverage.get("schema_id")
            == "hfo.gen133.sigrun.heritage_coverage.v12"
            and coverage.get("local_paths_projected") is False
            and coverage.get("exact_candidate_mappings_projected") is False,
            {"candidate_count": heritage.get("candidate_count"), "coverage": "PARTIAL"},
        )
    )
    predecessor_ok, predecessor_evidence = predecessor_binding_ok()
    checks.append(
        check(
            "v11_exact_commit_blob_byte_bindings",
            predecessor_ok,
            predecessor_evidence,
        )
    )

    overwrite = subprocess.run(
        [
            sys.executable,
            str(BUILDER),
            "--initialize-successor",
            "--v11-ledger",
            str(v11_ledger_path),
            "--v11-ledger-binding",
            str(v11_binding_path),
            "--candidate-additions",
            str(candidate_path),
            "--v12-ledger",
            str(ledger_path),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    in_worktree = subprocess.run(
        [
            sys.executable,
            str(BUILDER),
            "--initialize-successor",
            "--v11-ledger",
            str(PROJECTION),
            "--v11-ledger-binding",
            str(v11_binding_path),
            "--candidate-additions",
            str(candidate_path),
            "--v12-ledger",
            str(ledger_path),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    checks.append(
        check(
            "one_time_overwrite_and_in_worktree_refusal",
            overwrite.returncode != 0
            and "refusing to replace" in (overwrite.stderr + overwrite.stdout)
            and in_worktree.returncode != 0
            and "outside the Git worktree" in (in_worktree.stderr + in_worktree.stdout),
            {"overwrite_refused": overwrite.returncode != 0, "in_worktree_refused": in_worktree.returncode != 0},
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
        check(
            "deterministic_repeated_build",
            set(first) == set(second) == EXPECTED_DIST_FILES and first == second,
            {
                "file_count": len(first),
                "expected_file_set": set(first) == EXPECTED_DIST_FILES,
                "byte_hashes_equal": first == second,
            },
        )
    )

    for tier, (path, budget) in TIERS.items():
        checks.append(
            check(
                f"{tier.lower()}_budget_and_self_hash",
                0 < path.stat().st_size <= budget and self_hash_ok(path),
                {"bytes": path.stat().st_size, "budget": budget},
            )
        )
    frontmatters = {name: frontmatter(path) for name, (path, _) in TIERS.items()}
    checks.append(
        check(
            "tier_hold_semantics",
            all(
                data.get("effect_ceiling") == "T0_INTERNAL_ONLY"
                and data.get("source_bodies") == "WITHHELD"
                and data.get("source_metadata") == "OPAQUE_LOCAL_LEDGER_ONLY"
                and data.get("public_rights_review") == "ABSENT"
                and data.get("soul_status") == "self_authored_unratified_unsealed"
                and data.get("sealed") == "false"
                for data in frontmatters.values()
            ),
            {"tier_count": len(frontmatters)},
        )
    )

    expected_tiers = {name: record(path) for name, (path, _) in TIERS.items()}
    manifest_path = DIST / "CAPSULE_FAMILY_MANIFEST.json"
    binding_path = DIST / "SOURCE_BINDING_RECEIPT.json"
    xl_path = DIST / "XL_INDEX.safe.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    binding = json.loads(binding_path.read_text(encoding="utf-8"))
    xl = json.loads(xl_path.read_text(encoding="utf-8"))
    checks.append(
        check(
            "tier_manifest_xl_and_source_bindings",
            manifest.get("tiers") == expected_tiers
            and manifest.get("payload") == expected_tiers["L_SAFE"]
            and xl.get("tiers") == expected_tiers
            and xl.get("self_contained") is False
            and xl.get("publication_status") == "NOT_UPLOADED_NO_ARWEAVE_CLAIM"
            and binding.get("projection") == record(PROJECTION)
            and binding.get("source_bodies_opened") is False
            and binding.get("candidate_packet", {}).get("sha256")
            == EXPECTED_CANDIDATE_SHA256
            and manifest.get("candidate_packet", {}).get("sha256")
            == EXPECTED_CANDIDATE_SHA256,
            {"tier_count": len(expected_tiers), "candidate_binding": True},
        )
    )
    checks.append(
        check(
            "successor_publication_hold",
            manifest.get("successor_of", {}).get("version") == "v11"
            and manifest.get("successor_of", {}).get("artifact_commit")
            == V11_ARTIFACT_COMMIT
            and manifest.get("publication_status")
            == "NOT_UPLOADED_NO_ARWEAVE_CLAIM"
            and manifest.get("independent_review_status") == "ABSENT"
            and manifest.get("public_rights_review") == "ABSENT"
            and manifest.get("operator_ratification") == "ABSENT"
            and manifest.get("sealed") is False
            and manifest.get("remote_currency") == "LOCAL_COMMIT_NOT_REMOTE_MAIN",
            {"successor_commit_bound": True, "publication_status": manifest.get("publication_status")},
        )
    )
    heritage_record = record(HERITAGE_RECEIPT)
    checks.append(
        check(
            "heritage_receipt_exact_public_binding",
            binding.get("heritage_delta_receipt") == heritage_record
            and manifest.get("heritage_delta_receipt") == heritage_record,
            {"bytes": heritage_record["utf8_lf_bytes"], "sha256": heritage_record["sha256"]},
        )
    )

    root_path = DIST / "ROOT_BUNDLE.safe.json"
    root_raw = root_path.read_bytes()
    root = json.loads(root_raw.decode("utf-8"))
    canonical_paths = {
        "capsules/sigrun/v12/dist/S_SMALL.safe.md": DIST / "S_SMALL.safe.md",
        "capsules/sigrun/v12/dist/M_MEDIUM.safe.md": DIST / "M_MEDIUM.safe.md",
        "capsules/sigrun/v12/dist/L_SAFE.view.md": DIST / "L_SAFE.view.md",
        "capsules/sigrun/v12/dist/XL_INDEX.safe.json": xl_path,
        "capsules/sigrun/v12/dist/CAPSULE_FAMILY_MANIFEST.json": manifest_path,
        "capsules/sigrun/v12/dist/SOURCE_BINDING_RECEIPT.json": binding_path,
    }
    embedded_ok = True
    embedded_paths: set[str] = set()
    for item in root.get("records", []):
        path = item.get("path")
        embedded_paths.add(path)
        try:
            decoded = base64.b64decode(item.get("content_base64", ""), validate=True)
        except Exception:
            embedded_ok = False
            continue
        expected_path = canonical_paths.get(path)
        if expected_path is None:
            embedded_ok = False
            continue
        expected = expected_path.read_bytes()
        embedded_ok = embedded_ok and (
            decoded == expected
            and item.get("content_encoding") == "base64"
            and item.get("utf8_lf_bytes") == len(expected)
            and item.get("sha256") == sha256_hex(expected)
            and item.get("git_blob_sha1") == git_blob_sha1(expected)
            and item.get("git_blob_sha") == git_blob_sha1(expected)
        )
    checks.append(
        check(
            "root_bundle_self_contained_child_reproduction",
            0 < len(root_raw) < 100000
            and root.get("self_contained") is True
            and root.get("canonical_record_count") == len(canonical_paths)
            and embedded_paths == set(canonical_paths)
            and embedded_ok
            and root.get("publication_status")
            == "NOT_UPLOADED_NO_ARWEAVE_CLAIM",
            {
                "bytes": len(root_raw),
                "budget_exclusive": 100000,
                "record_count": len(embedded_paths),
                "child_bytes_reproduced": embedded_ok,
            },
        )
    )
    checks.append(
        check(
            "root_bundle_no_external_urls_or_mutable_refs",
            not re.search(rb"https?://", root_raw, re.IGNORECASE)
            and not re.search(rb'"ref"\s*:', root_raw, re.IGNORECASE),
            {"external_url_hits": 0, "mutable_ref_field_hits": 0},
        )
    )

    preupload_path = DIST / "PERMAWEB_PREUPLOAD_PACKET.hold.json"
    preupload_raw = preupload_path.read_bytes()
    preupload = json.loads(preupload_raw.decode("utf-8"))
    tags = preupload.get("proposed_tags", [])
    tag_map = {row.get("name"): row.get("value") for row in tags}
    expected_receipt_fields = [
        "id",
        "owner",
        "winc",
        "dataCaches",
        "fastFinalityIndexes",
        "timestamp",
        "version",
        "public",
        "signature",
    ]
    required_gateway_fields = [
        "gateway_id",
        "hostname",
        "request_url",
        "fetched_utc",
        "http_status",
        "response_content_type_raw",
        "response_media_type_normalized",
        "content_length_header",
        "fetched_bytes",
        "fetched_sha256",
        "raw_body_receipt_path",
        "raw_body_sha256",
        "exact_artifact_match",
        "json_parse",
        "schema_validation",
        "result",
    ]
    required_verdict_fields = [
        "distinct_hostnames",
        "both_http_200",
        "both_application_json",
        "both_exact_bytes",
        "both_sha256_match_artifact",
        "gateways_match_each_other",
        "result",
    ]
    forbidden_preupload = re.search(
        rb"upload_command|private[_-]?key|seed[_-]?phrase|mnemonic|PENDING_CONTAINING_COMMIT|CURRENT_GEN133_REMOTE",
        preupload_raw,
        re.IGNORECASE,
    )
    checks.append(
        check(
            "preupload_exact_root_binding_and_hold_gates",
            preupload.get("root_bundle")
            == {
                **record(root_path),
                "content_type": "application/json",
                "self_contained": True,
            }
            and tags == sorted(tags, key=lambda row: (row["name"], row["value"]))
            and len(tag_map) == len(tags)
            and tag_map.get("Content-Type") == "application/json"
            and tag_map.get("App-Name") == "HFO-Sigrun-Capsule-v12"
            and "Git-Repository" not in tag_map
            and "Git-Commit" not in tag_map
            and preupload.get("tag_packet_state")
            == "PENDING_EXACT_GIT_COMMIT_AND_DISTINCT_RIGHTS_REVIEW"
            and preupload.get("required_post_commit_tags")
            == [
                "Git-Commit",
                "Git-Repository",
                "Privacy-Rights-Review-Receipt-SHA256",
            ]
            and preupload.get("rights_review") == "HOLD"
            and preupload.get("independent_review") == "ABSENT"
            and preupload.get("operator_authorization") == "ABSENT"
            and preupload.get("spend") == "HOLD_NO_QUOTE_OR_AUTHORIZATION"
            and preupload.get("wallet") is None
            and preupload.get("txid") is None
            and preupload.get("free_upload_eligibility")
            == "SIZE_ONLY_SERVICE_TERMS_UNVERIFIED_AT_EXECUTION"
            and preupload.get("upload_receipt")
            == {
                "state": "ABSENT",
                "raw_response_path": None,
                "raw_response_sha256": None,
                "capture_where_returned": expected_receipt_fields,
            }
            and preupload.get("retrieval_readback")
            == {
                "state": "ABSENT",
                "required_distinct_gateway_count": 2,
                "required_gateway_fields": required_gateway_fields,
                "required_two_gateway_verdict_fields": required_verdict_fields,
                "gateway_receipts": [],
                "two_gateway_verdict": None,
                "durability_checkpoints": {
                    "t_plus_7d": "PENDING",
                    "t_plus_30d": "PENDING",
                },
            }
            and preupload.get("publication_status")
            == "NOT_UPLOADED_NO_ARWEAVE_CLAIM"
            and forbidden_preupload is None,
            {
                "root_bytes": len(root_raw),
                "root_sha256": sha256_hex(root_raw),
                "tag_count": len(tags),
                "receipt_status": preupload.get("upload_receipt", {}).get("state"),
                "retrieval_status": preupload.get("retrieval_readback", {}).get("state"),
            },
        )
    )

    public_files = [
        ROOT / "SIGRUN_CAPSULE_FAMILY_CONTRACT.md",
        BUILDER,
        RECEIPT_BUILDER,
        Path(__file__).resolve(),
        PROJECTION,
        *sorted(REVIEW_ROOT.glob("*.json")),
        *[DIST / name for name in sorted(EXPECTED_DIST_FILES)],
    ]
    public_raw = b"\n".join(path.read_bytes() for path in public_files)
    protected_values: set[bytes] = set()
    protected_keys = {
        "id",
        "repository",
        "repo_alias",
        "repo_root",
        "remote",
        "ref",
        "commit",
        "path",
        "blob_sha1",
        "sha256",
        "reason",
    }
    for row in rows:
        exact = row.get("exact_source_record", {})
        for key in protected_keys:
            value = exact.get(key)
            if isinstance(value, str) and len(value) >= 8:
                protected_values.add(value.encode("utf-8"))
    leaks = [value for value in protected_values if value in public_raw]
    absolute_hits = re.findall(rb"(?<![A-Za-z0-9])[A-Za-z]:[\\/]", public_raw)
    file_uri_hit = (rb"file:" + rb"//") in public_raw
    checks.append(
        check(
            "protected_values_and_absolute_paths_absent",
            not leaks and not absolute_hits and not file_uri_hit,
            {
                "protected_value_leak_count": len(leaks),
                "absolute_path_hit_count": len(absolute_hits) + int(file_uri_hit),
                "values_redacted": True,
            },
        )
    )
    checks.append(
        check(
            "public_utf8_lf_canonical",
            all(
                not path.read_bytes().startswith(b"\xef\xbb\xbf")
                and b"\r" not in path.read_bytes()
                and path.read_bytes().endswith(b"\n")
                and bool(path.read_bytes().decode("utf-8"))
                for path in public_files
            ),
            {"file_count": len(public_files)},
        )
    )

    hold_fields = {
        "effect_ceiling": "T0_INTERNAL_ONLY",
        "source_bodies": "WITHHELD",
        "public_rights_review": "ABSENT",
        "independent_review_status": "ABSENT",
        "operator_ratification": "ABSENT",
        "sealed": False,
        "publication_status": "NOT_UPLOADED_NO_ARWEAVE_CLAIM",
    }
    probe = (
        json.dumps(checks, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    checks.append(
        check(
            "verification_receipt_self_leak_guard",
            not any(value in probe for value in protected_values),
            {"leak_count": 0, "values_redacted": True},
        )
    )
    passed = all(row["result"] == "PASS" for row in checks)
    receipt = {
        "schema_id": "hfo.gen133.sigrun_capsule_verification_receipt.v12",
        "result": "PASS" if passed else "FAIL",
        "checks": checks,
        **hold_fields,
        "honest_flaw": (
            "The verifier proves deterministic public-byte relations and absence "
            "of tested exact identifiers. Filename-guided discovery is incomplete, "
            "the local source commit is not current remote main, and no rights, identity, "
            "continuity, independent review, delivery, or publication is proven."
        ),
        "falsifier": (
            "Any failed check, changed v11 prefix, protected mapping in public bytes, "
            "source-body access, nondeterministic rebuild, root-child mismatch, "
            "wallet material, upload command, or publication claim."
        ),
        "next_safe_action": (
            "Obtain one distinct privacy-and-rights review of the eight-row v12 "
            "delta before any body access or publication authorization."
        ),
    }
    raw = (
        json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    if any(value in raw for value in protected_values):
        raise RuntimeError("verification receipt protected-value leak")
    (DIST / "VERIFICATION_RECEIPT.json").write_bytes(raw)
    print(json.dumps({"result": receipt["result"], "checks": len(checks)}, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
