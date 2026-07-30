#!/usr/bin/env python3
"""Verify the Sigrun v8 opaque-only capsule family."""

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
PUBLIC_FILES = [
    ROOT / "SIGRUN_CAPSULE_FAMILY_CONTRACT.md",
    PROJECTION,
    BUILDER,
    Path(__file__).resolve(),
    DIST / "S_SMALL.safe.md",
    DIST / "M_MEDIUM.safe.md",
    DIST / "L_SAFE.view.md",
    DIST / "XL_INDEX.safe.json",
    DIST / "SOURCE_BINDING_RECEIPT.json",
    DIST / "CAPSULE_FAMILY_MANIFEST.json",
]
TIERS = {
    "S_SMALL": (DIST / "S_SMALL.safe.md", 4096),
    "M_MEDIUM": (DIST / "M_MEDIUM.safe.md", 8192),
    "L_SAFE": (DIST / "L_SAFE.view.md", 32768),
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


def result(name: str, passed: bool, evidence: Any) -> dict[str, Any]:
    return {"check": name, "result": "PASS" if passed else "FAIL", "evidence": evidence}


def self_hash_ok(path: Path) -> bool:
    raw = path.read_bytes()
    match = re.search(rb"^self_hash: ([0-9a-f]{64})$", raw, re.MULTILINE)
    if not match:
        return False
    restored = (
        raw[: match.start(1)]
        + SELF_PLACEHOLDER.encode("ascii")
        + raw[match.end(1) :]
    )
    return match.group(1).decode("ascii") == sha256_hex(restored)


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
    args = parser.parse_args()
    ledger_path = args.local_ledger.resolve()
    if ledger_path == REPO_ROOT or REPO_ROOT in ledger_path.parents:
        raise RuntimeError("local exact ledger must stay outside the worktree")

    checks: list[dict[str, Any]] = []
    projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    records = projection["records"]
    rows = ledger["rows"]
    allowed = {
        "opaque_receipt_id",
        "visibility_class",
        "disposition",
        "body_embedding",
    }
    checks.append(result("source_count_104", len(records) == len(rows) == 104, len(records)))
    checks.append(
        result(
            "heritage_delta_count_51",
            projection["heritage_delta_count"] == ledger["heritage_delta_count"] == 51,
            projection["heritage_delta_count"],
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
            and all(re.fullmatch(r"rct_v[78]_[A-Z2-7]{26}", rid) for rid in ids),
            {"count": len(ids), "unique": len(set(ids))},
        )
    )
    checks.append(
        result(
            "ledger_projection_id_bijection",
            set(ids) == {row["opaque_receipt_id"] for row in rows},
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
        path: sha256_hex(path.read_bytes())
        for path in DIST.glob("*")
        if path.is_file() and path.name != "VERIFICATION_RECEIPT.json"
    }
    run_builder()
    second = {
        path: sha256_hex(path.read_bytes())
        for path in DIST.glob("*")
        if path.is_file() and path.name != "VERIFICATION_RECEIPT.json"
    }
    checks.append(result("deterministic_second_build", first == second, {"files": len(first)}))

    for tier, (path, budget) in TIERS.items():
        checks.append(
            result(
                f"{tier.lower()}_budget",
                path.stat().st_size <= budget,
                {"bytes": path.stat().st_size, "budget": budget},
            )
        )
        checks.append(result(f"{tier.lower()}_self_hash", self_hash_ok(path), path.name))
    xl_path = DIST / "XL_INDEX.safe.json"
    checks.append(
        result(
            "xl_budget_and_not_self_contained",
            xl_path.stat().st_size <= 100 * 1024
            and json.loads(xl_path.read_text(encoding="utf-8"))["self_contained"] is False,
            {"bytes": xl_path.stat().st_size, "budget": 100 * 1024},
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
            manifest["successor_of"]["version"] == "v7"
            and manifest["successor_of"]["artifact_commit"]
            == "84d25515da13cf5e227ba35737116b9b9a4e4a31"
            and manifest["publication_status"] == "NOT_UPLOADED_NO_ARWEAVE_CLAIM"
            and manifest["independent_review_status"] == "ABSENT",
            {
                "successor": manifest["successor_of"],
                "publication_status": manifest["publication_status"],
                "independent_review_status": manifest["independent_review_status"],
            },
        )
    )
    checks.append(
        result(
            "source_binding_exact",
            json.loads(
                (DIST / "SOURCE_BINDING_RECEIPT.json").read_text(encoding="utf-8")
            )["projection"]
            == record(PROJECTION),
            record(PROJECTION),
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
    # The v8 source itself must name its own public successor commit and public
    # artifact paths. Remove only those two intentional, non-source values.
    intentional = {
        "84d25515da13cf5e227ba35737116b9b9a4e4a31",
    }
    leaks = [value for value in leaks if value not in intentional]
    checks.append(
        result(
            "protected_exact_values_absent_from_v8_public_family",
            not leaks,
            {"leak_count": len(leaks), "leaks": leaks[:10]},
        )
    )
    checks.append(
        result(
            "effect_ceiling_and_unsealed",
            manifest["effect_ceiling"] == "T0_INTERNAL_ONLY"
            and manifest["sealed"] is False,
            {"effect_ceiling": manifest["effect_ceiling"], "sealed": manifest["sealed"]},
        )
    )

    passed = all(check["result"] == "PASS" for check in checks)
    receipt = {
        "schema_id": "hfo.gen133.sigrun_capsule_verification_receipt.v8",
        "result": "PASS" if passed else "FAIL",
        "checks": checks,
        "effect_ceiling": "T0_INTERNAL_ONLY",
        "honest_flaw": (
            "The verifier proves public-byte relations and absence of exact local "
            "ledger values only. It does not prove privacy rights, identity, "
            "continuity, delivery, or publication."
        ),
        "falsifier": (
            "Any failed check, protected exact value in a public v8 artifact, "
            "body admission, nondeterministic rebuild, or byte mismatch."
        ),
        "next_safe_action": (
            "Obtain one distinct privacy-and-rights review of the newly bounded "
            "local v8 delta before admitting any historical source body."
        ),
    }
    (DIST / "VERIFICATION_RECEIPT.json").write_bytes(
        (json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
            "utf-8"
        )
    )
    print(json.dumps({"result": receipt["result"], "checks": len(checks)}, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
