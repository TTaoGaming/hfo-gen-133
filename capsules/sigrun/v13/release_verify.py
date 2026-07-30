#!/usr/bin/env python3
"""Read-only release verification for the Sigrun v13 public capsule tree."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import subprocess
from typing import Any
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
REVIEW_ROOT = REPO_ROOT / "reviews" / "sigrun" / "v13"
BUILD_RECEIPT = REVIEW_ROOT / "V13_BUILD_RECEIPT.json"
VERIFICATION_RECEIPT = ROOT / "dist" / "VERIFICATION_RECEIPT.json"
ALLOWED_POSTCOMMIT_FILES = {
    "reviews/sigrun/v13/REMOTE_READBACK_RECEIPT.json",
}
PROHIBITED_POSITIVE_CLAIMS = (
    re.compile(rb'"tier"\s*:\s*"T[3-5]'),
    re.compile(rb'"publication_status"\s*:\s*"(?!NOT_UPLOADED_NO_ARWEAVE_CLAIM)'),
    re.compile(rb'"slack_delivery"\s*:\s*"(?!ABSENT|HOLD)'),
)
_BACKSLASH = bytes((92,))
ABSOLUTE_PATH_PATTERNS = (
    re.compile(rb"(?<![A-Za-z0-9])[A-Za-z]:[\\/]"),
    re.compile(
        re.escape(_BACKSLASH * 2)
        + rb"(?:[?.]|[^"
        + re.escape(_BACKSLASH)
        + bytes((13, 10))
        + rb"]+)"
        + re.escape(_BACKSLASH)
    ),
    re.compile(rb"(?<![A-Za-z0-9])/(?:home|Users)/[^/\r\n]+/"),
    re.compile(rb"(?i)" + rb"file:" + rb"//"),
)


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def check(name: str, passed: bool, evidence: Any) -> dict[str, Any]:
    return {
        "check": name,
        "result": "PASS" if passed else "FAIL",
        "evidence": evidence,
    }


def canonical_public_files() -> list[Path]:
    return sorted(
        [
            *ROOT.glob("*"),
            *ROOT.joinpath("dist").glob("*"),
            *REVIEW_ROOT.glob("*"),
        ],
        key=lambda path: path.as_posix(),
    )


def public_path(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def collect_protected_values(value: Any) -> set[bytes]:
    protected_keys = {
        "repo_root",
        "remote",
        "repository",
        "ref",
        "commit",
        "path",
        "blob_sha1",
        "sha256",
        "last_path_commit",
    }
    values: set[str] = set()

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            for key, child in node.items():
                if (
                    key in protected_keys
                    and isinstance(child, str)
                    and len(child) >= 8
                ):
                    values.add(child)
                walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    walk(value)
    transformed: set[bytes] = set()
    for item in values:
        raw = item.encode("utf-8")
        variants = {
            item,
            item.replace("\\", "/"),
            item.replace("/", "\\"),
            quote(item, safe=""),
            base64.b64encode(raw).decode("ascii"),
            base64.urlsafe_b64encode(raw).decode("ascii"),
        }
        for variant in variants:
            if len(variant) >= 8:
                transformed.add(variant.encode("utf-8"))
    return transformed


def exact_tuple(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {
        "path": public_path(path),
        "utf8_lf_bytes": len(raw),
        "git_blob_sha1": git_blob_sha1(raw),
        "sha256": sha256(raw),
    }


def verify_postcommit_receipt(
    receipt_path: Path, expected_commit: str
) -> tuple[bool, dict[str, Any]]:
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    if receipt.get("artifact_commit") != expected_commit:
        errors.append("artifact_commit")
    if receipt.get("remote_ls_remote_commit") != expected_commit:
        errors.append("remote_ls_remote_commit")
    if receipt.get("tier") != "T2_BOUND":
        errors.append("tier")
    for binding in receipt.get("bindings", []):
        path = binding.get("path")
        if not isinstance(path, str) or path.startswith(("/", "\\")):
            errors.append("path")
            continue
        blob = subprocess.run(
            ["git", "rev-parse", f"{expected_commit}:{path}"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if blob.returncode:
            errors.append("missing_blob")
            continue
        observed_blob = blob.stdout.strip()
        size = subprocess.run(
            ["git", "cat-file", "-s", observed_blob],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if (
            size.returncode
            or observed_blob != binding.get("git_blob_sha1")
            or int(size.stdout.strip()) != binding.get("bytes")
        ):
            errors.append("binding")
    return not errors, {"binding_count": len(receipt.get("bindings", [])), "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-ledger", required=True, type=Path)
    parser.add_argument("--candidate-additions", required=True, type=Path)
    parser.add_argument("--postcommit-receipt", type=Path)
    parser.add_argument("--expected-commit")
    args = parser.parse_args()

    exact_inputs = [
        args.local_ledger.resolve(),
        args.candidate_additions.resolve(),
    ]
    if any(path == REPO_ROOT or REPO_ROOT in path.parents for path in exact_inputs):
        raise RuntimeError("protected inputs must stay outside the Git worktree")

    ledger = json.loads(exact_inputs[0].read_text(encoding="utf-8"))
    candidates = json.loads(exact_inputs[1].read_text(encoding="utf-8"))
    protected = collect_protected_values(
        {
            "exact_rows": [
                row.get("exact_source_record", {})
                for row in ledger.get("rows", [])
            ],
            "candidates": candidates.get("candidates", []),
        }
    )
    files = [path for path in canonical_public_files() if path.is_file()]
    public_raw = b"\n".join(path.read_bytes() for path in files)
    checks: list[dict[str, Any]] = []

    canonical_failures = []
    for path in files:
        raw = path.read_bytes()
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError:
            canonical_failures.append(public_path(path))
            continue
        if (
            not raw
            or raw.startswith(b"\xef\xbb\xbf")
            or b"\r" in raw
            or b"\x00" in raw
            or not raw.endswith(b"\n")
        ):
            canonical_failures.append(public_path(path))
    checks.append(
        check(
            "public_utf8_lf_canonical",
            not canonical_failures,
            {"file_count": len(files), "failure_count": len(canonical_failures)},
        )
    )

    protected_hits = sum(public_raw.count(value) for value in protected)
    absolute_hits = sum(len(pattern.findall(public_raw)) for pattern in ABSOLUTE_PATH_PATTERNS)
    checks.append(
        check(
            "protected_values_and_transforms_absent",
            protected_hits == 0 and absolute_hits == 0,
            {
                "protected_variant_count": len(protected),
                "protected_hit_count": protected_hits,
                "absolute_path_hit_count": absolute_hits,
                "values_redacted": True,
            },
        )
    )

    positive_claim_hits = sum(
        len(pattern.findall(public_raw)) for pattern in PROHIBITED_POSITIVE_CLAIMS
    )
    checks.append(
        check(
            "claim_ceiling_at_most_t2_candidate",
            positive_claim_hits == 0,
            {"prohibited_positive_claim_hits": positive_claim_hits},
        )
    )

    verification = json.loads(VERIFICATION_RECEIPT.read_text(encoding="utf-8"))
    verification_checks = verification.get("checks", [])
    checks.append(
        check(
            "author_verification_fully_passes",
            verification.get("result") == "PASS"
            and bool(verification_checks)
            and all(row.get("result") == "PASS" for row in verification_checks),
            {
                "result": verification.get("result"),
                "checks": len(verification_checks),
                "passes": sum(
                    row.get("result") == "PASS" for row in verification_checks
                ),
            },
        )
    )

    build = json.loads(BUILD_RECEIPT.read_text(encoding="utf-8"))
    tuple_errors = []
    for expected in build.get("public_outputs", []):
        path = REPO_ROOT / expected["path"]
        if not path.is_file() or exact_tuple(path) != expected:
            tuple_errors.append(expected.get("path"))
    expected_scope = {
        public_path(path)
        for path in files
        if path != BUILD_RECEIPT
        and public_path(path) not in ALLOWED_POSTCOMMIT_FILES
    }
    listed_scope = {row["path"] for row in build.get("public_outputs", [])}
    checks.append(
        check(
            "build_receipt_exact_tuples_and_scope",
            not tuple_errors and expected_scope == listed_scope,
            {
                "tuple_count": len(build.get("public_outputs", [])),
                "tuple_error_count": len(tuple_errors),
                "scope_difference_count": len(expected_scope ^ listed_scope),
            },
        )
    )

    if args.postcommit_receipt or args.expected_commit:
        if not args.postcommit_receipt or not args.expected_commit:
            raise RuntimeError("postcommit receipt and expected commit are paired")
        passed, evidence = verify_postcommit_receipt(
            args.postcommit_receipt.resolve(), args.expected_commit
        )
        checks.append(check("postcommit_remote_receipt", passed, evidence))

    passed = all(row["result"] == "PASS" for row in checks)
    print(
        json.dumps(
            {
                "schema_id": "hfo.gen133.sigrun_v13_release_verification.v1",
                "result": "PASS" if passed else "FAIL",
                "checks": checks,
                "tier_ceiling": "T2_BOUND",
                "independent_weight": 0,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
