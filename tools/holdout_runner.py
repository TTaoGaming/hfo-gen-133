#!/usr/bin/env python3
"""Gen-133 held-out test harness (arm_and_holdout_builder, 2026-08-01).

Reads a held-out manifest (tests/held_out/*.jsonl), runs each row's
protocol_under_test command against input_ref, and grep-checks stdout against
expected_output_regex. Emits one result row per test to
state/ssot/holdout_results.jsonl (append-only). Never writes to the manifest
itself -- the manifest is the held-out set and must stay untouched by a run.

clock_source=host_read: every ts_utc below comes from a real
datetime.now(timezone.utc) call at emit time, not a generated/assumed value.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_MANIFEST = Path("tests/held_out/spatial_factory_holdout_manifest.jsonl")
DEFAULT_RESULTS = Path("state/ssot/holdout_results.jsonl")
COMMAND_TIMEOUT_SECONDS = 30


def host_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_manifest(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as fh:
        for line_no, raw in enumerate(fh, start=1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                rows.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: malformed JSON: {exc}") from exc
    return rows


def run_one(row: dict) -> dict:
    test_id = row.get("test_id", "UNKNOWN")
    protocol = row.get("protocol_under_test", "")
    pattern = row.get("expected_output_regex", "")
    ts_utc = host_now_iso()

    result = {
        "schema_id": "hfo.gen133.holdout_result.v0_1",
        "ts_utc": ts_utc,
        "clock_source": "host_read",
        "test_id": test_id,
        "protocol": protocol,
        "cmd_run": protocol,
        "exit_code": None,
        "output_matched_regex": False,
        "status": "error",
        "honest_flaw": "",
    }

    if not protocol:
        result["honest_flaw"] = "manifest row has no protocol_under_test command"
        return result

    try:
        proc = subprocess.run(
            protocol,
            shell=True,
            capture_output=True,
            text=True,
            timeout=COMMAND_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        result["honest_flaw"] = f"command timed out after {COMMAND_TIMEOUT_SECONDS}s"
        return result
    except OSError as exc:
        result["honest_flaw"] = f"command failed to launch: {exc}"
        return result

    combined_output = (proc.stdout or "") + (proc.stderr or "")
    result["exit_code"] = proc.returncode

    matched = bool(re.search(pattern, combined_output)) if pattern else False
    result["output_matched_regex"] = matched

    if proc.returncode == 0 and matched:
        result["status"] = "pass"
        result["honest_flaw"] = "none"
    elif proc.returncode == 0 and not matched:
        result["status"] = "fail"
        snippet = combined_output.strip()[:200]
        result["honest_flaw"] = f"exit 0 but expected_output_regex {pattern!r} not found; output snippet: {snippet!r}"
    else:
        result["status"] = "fail"
        snippet = combined_output.strip()[:200]
        result["honest_flaw"] = f"nonzero exit {proc.returncode}; output snippet: {snippet!r}"

    return result


def append_results(results: list[dict], results_path: Path) -> None:
    results_path.parent.mkdir(parents=True, exist_ok=True)
    with results_path.open("a", encoding="utf-8") as fh:
        for row in results:
            fh.write(json.dumps(row, sort_keys=True, ensure_ascii=True))
            fh.write("\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Run the gen-133 held-out test manifest")
    ap.add_argument("manifest", nargs="?", default=str(DEFAULT_MANIFEST),
                     help=f"path to a held-out manifest JSONL (default: {DEFAULT_MANIFEST})")
    ap.add_argument("--results", default=str(DEFAULT_RESULTS),
                     help=f"path to append results to (default: {DEFAULT_RESULTS})")
    args = ap.parse_args(argv)

    manifest_path = Path(args.manifest)
    results_path = Path(args.results)

    if not manifest_path.is_file():
        print(json.dumps({"ok": False, "error": f"manifest not found: {manifest_path}"}))
        return 1

    rows = load_manifest(manifest_path)
    results = [run_one(row) for row in rows]
    append_results(results, results_path)

    passed = sum(1 for r in results if r["status"] == "pass")
    failed = sum(1 for r in results if r["status"] == "fail")
    errored = sum(1 for r in results if r["status"] == "error")

    summary = {
        "ok": failed == 0 and errored == 0,
        "manifest": str(manifest_path).replace("\\", "/"),
        "results_path": str(results_path).replace("\\", "/"),
        "total": len(results),
        "passed": passed,
        "failed": failed,
        "errored": errored,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=True))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
