#!/usr/bin/env python3
"""Gen-133 chain-row hash verifier (EMERGENCY_FORGE build, 2026-08-01).

Ported hashing convention from gen-130's
`hfo_dev_2026_5_30/hfo_gen_130_forge/scripts/verify_chain_integrity.py`
(`canonical_bytes`/`sha256_hex`/`is_hex64`) -- this is also the exact
`hash_rule` the gen-133 SIGRUN_P4 chain itself declares on its own rows:
    sha256(json.dumps(row_without_row_sha256, sort_keys=True,
                       separators=(",", ":"), ensure_ascii=True).encode("utf-8"))

Simplified relative to the gen-130 tool per this task's spec: single-file CLI,
first-broken-link reporting (not an aggregate multi-file sweep), no queue-
repair/grandfather-manifest machinery (gen-133 has neither yet).

A row is "hash-checkable" only if it carries a `row_sha256` field. Rows
without one (documented in this chain's own `L_CHAIN_HASH_ABANDONED_SILENTLY`
failure-class row as rows 2-8, dropped silently by the second carrier) are
reported as UNHASHED, not as broken links -- they carry no verifiable claim
either way. prev_sha256 continuity is only checked between two
hash-checkable rows; a gap through unhashed rows is reported as
UNLINKABLE_THROUGH_UNHASHED_ROWS, not as a hash mismatch.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

HEX64 = set("0123456789abcdef")


def canonical_bytes(obj: dict[str, Any]) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_hex64(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(ch in HEX64 for ch in value)


def recompute_row_sha256(row: dict[str, Any]) -> str:
    without = dict(row)
    without.pop("row_sha256", None)
    without.pop("_line_no", None)
    return sha256_hex(canonical_bytes(without))


def verify_chain(path: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    malformed: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig") as fh:
        for line_no, raw in enumerate(fh, start=1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                row = json.loads(raw)
            except json.JSONDecodeError as exc:
                malformed.append({"line": line_no, "detail": str(exc)})
                continue
            if not isinstance(row, dict):
                malformed.append({"line": line_no, "detail": "row is not a JSON object"})
                continue
            row["_line_no"] = line_no
            rows.append(row)

    row_reports: list[dict[str, Any]] = []
    unhashed_lines: list[int] = []
    hash_mismatches: list[dict[str, Any]] = []
    prev_breaks: list[dict[str, Any]] = []

    last_hashed: dict[str, Any] | None = None  # last row with a verified-present row_sha256
    for row in rows:
        line_no = row["_line_no"]
        declared = row.get("row_sha256")
        prev_declared = row.get("prev_sha256")

        if not is_hex64(declared):
            unhashed_lines.append(line_no)
            row_reports.append({"line": line_no, "status": "UNHASHED"})
            continue

        recomputed = recompute_row_sha256(row)
        hash_ok = recomputed == declared
        if not hash_ok:
            hash_mismatches.append({
                "line": line_no, "expected": recomputed, "observed": declared,
            })

        if last_hashed is None:
            # First hash-checkable row: prev_sha256 should be null (genesis)
            # or absent -- both are accepted as "no predecessor claimed".
            link_ok = prev_declared in (None, "")
            if not link_ok:
                prev_breaks.append({
                    "line": line_no,
                    "reason": "first hash-checkable row declares a non-null prev_sha256 "
                              "but no predecessor hash exists to verify it against",
                    "declared_prev": prev_declared,
                })
        else:
            expected_prev = last_hashed["row_sha256"]
            link_ok = prev_declared == expected_prev
            if not link_ok:
                prev_breaks.append({
                    "line": line_no,
                    "reason": "prev_sha256 does not match the last hash-checkable row's row_sha256"
                    if last_hashed["line"] == line_no - 1
                    else "prev_sha256 does not match the last hash-checkable row's row_sha256 "
                         f"(gap: {line_no - last_hashed['line'] - 1} unhashed row(s) in between)",
                    "expected_prev": expected_prev,
                    "declared_prev": prev_declared,
                    "last_hashed_line": last_hashed["line"],
                })

        row_reports.append({
            "line": line_no,
            "status": "OK" if (hash_ok and link_ok) else "BROKEN",
            "row_sha256": declared,
            "hash_ok": hash_ok,
            "prev_link_ok": link_ok,
        })
        last_hashed = {"line": line_no, "row_sha256": declared}

    first_break = next((r for r in row_reports if r["status"] == "BROKEN"), None)
    if malformed:
        first_break = first_break or {"line": malformed[0]["line"], "status": "MALFORMED_JSON"}

    context: dict[str, Any] | None = None
    if first_break is not None:
        idx = next(i for i, r in enumerate(row_reports) if r.get("line") == first_break["line"])
        context = {
            "row_before": row_reports[idx - 1] if idx > 0 else None,
            "broken_row": row_reports[idx],
            "row_after": row_reports[idx + 1] if idx + 1 < len(row_reports) else None,
        }

    ok = not malformed and not hash_mismatches and not prev_breaks
    return {
        "path": str(path).replace("\\", "/"),
        "ok": ok,
        "row_count": len(rows) + len(malformed),
        "hash_checkable_count": len(rows) - len(unhashed_lines),
        "unhashed_count": len(unhashed_lines),
        "unhashed_lines": unhashed_lines,
        "hash_mismatch_count": len(hash_mismatches),
        "hash_mismatches": hash_mismatches,
        "prev_link_break_count": len(prev_breaks),
        "prev_link_breaks": prev_breaks,
        "malformed_count": len(malformed),
        "malformed": malformed,
        "first_break": first_break,
        "first_break_context": context,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Verify a gen-133 chain JSONL file's row_sha256/prev_sha256 hash chain")
    ap.add_argument("path", help="path to a chains/*.jsonl file")
    ap.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Stricter than the default report: ok is TRUE only if every hash-checkable "
            "row's hash verifies, all prev_sha256 links between hash-checkable rows are "
            "continuous, no row is malformed JSON, AND there are zero UNHASHED rows "
            "(the default report tolerates UNHASHED rows as 'no verifiable claim either "
            "way'; --strict treats any gap in hash coverage as a break). Adds an explicit "
            "break_count/breaks field summing every category of problem found."
        ),
    )
    args = ap.parse_args(argv)

    path = Path(args.path)
    if not path.is_file():
        print(json.dumps({"ok": False, "error": f"file not found: {path}"}))
        return 1

    report = verify_chain(path)

    if args.strict:
        lenient_ok = report["ok"]
        break_count = (
            report["malformed_count"]
            + report["hash_mismatch_count"]
            + report["prev_link_break_count"]
            + report["unhashed_count"]
        )
        report["strict"] = True
        report["lenient_ok"] = lenient_ok
        report["ok"] = lenient_ok and report["unhashed_count"] == 0
        report["break_count"] = break_count
        report["breaks"] = break_count  # alias key for callers that look for "breaks"

    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
