#!/usr/bin/env python3
"""LOOP-C · DIRECTORY_SUBMISSION_BATCH — auto-submit where possible, stage
web-form directories for operator sign, log every outcome.

AIH2O header
------------
AIH2O:
  version: gen-133
  loop: directory_submission_batch
  role: executor
  actor: factory_loop
  verifier: gate_reader.gate_active('directory_submissions') + per-directory HEAD 200
  clock_source: host_read
  chain: state/loop_receipts/directory_submission_batch_<UTCDATE>.jsonl
  ship_log: state/outreach/directory_submissions.jsonl
  operator_queue: state/outreach/PENDING_DIRECTORY_APPROVALS.md

CLI
---
    python factory/loops/directory_submission_batch/run.py \\
        --unit-id promptbin --directories dirs.csv --url https://promptbin.pages.dev

    python factory/loops/directory_submission_batch/run.py \\
        --unit-id promptbin --directories dirs.csv --url https://... --dry-run

Kill conditions
---------------
- CAPTCHA required → stage for operator + move to next
- Site down (URL_HEAD non-200 for the directory itself) → skip + log
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve()
_FORGE = _HERE.parents[3]
sys.path.insert(0, str(_FORGE))
from factory.loops.lib import chain_row, gate_reader, receipt_verify, slack_escalate  # noqa: E402


LOOP = "directory_submission_batch"
CLASS_NAME = "directory_submissions"
SUBMISSIONS_LOG = _FORGE / "state" / "outreach" / "directory_submissions.jsonl"
PENDING_QUEUE = _FORGE / "state" / "outreach" / "PENDING_DIRECTORY_APPROVALS.md"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_directories(csv_path: Path) -> list[dict]:
    """Expected columns: directory,url,submit_kind,notes
    submit_kind ∈ {api, web_form, manual_only}
    """
    rows: list[dict] = []
    with csv_path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            r = {k.strip(): (v or "").strip() for k, v in r.items()}
            if not r.get("directory") or not r.get("url"):
                continue
            r.setdefault("submit_kind", "web_form")
            rows.append(r)
    return rows


def append_submission(row: dict) -> None:
    SUBMISSIONS_LOG.parent.mkdir(parents=True, exist_ok=True)
    with SUBMISSIONS_LOG.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def append_pending(unit_id: str, entry: dict) -> None:
    PENDING_QUEUE.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"- [ ] **{entry['directory']}** — {entry['url']}\n"
        f"  - unit: `{unit_id}` · staged: `{entry['staged_at']}` · reason: {entry['reason']}\n"
        f"  - submit URL: {entry.get('submit_url', entry['url'])}\n"
    )
    if not PENDING_QUEUE.exists():
        PENDING_QUEUE.write_text("# Pending directory submissions\n\n", encoding="utf-8")
    with PENDING_QUEUE.open("a", encoding="utf-8") as fh:
        fh.write(line)


def submit_api(directory: dict, unit_id: str, unit_url: str, dry_run: bool) -> tuple[bool, str]:
    """API submitters. We ship stubs — extend per-directory when the API
    is wired. Returns (posted?, detail)."""
    name = directory["directory"].lower()
    if dry_run:
        return True, f"dry_run — would POST to {name} API"
    # Known API-driven directories (extend as integrations land)
    if name in {"alternativeto", "openhunt", "producthunt_api"}:
        return False, f"{name} API integration not yet implemented — staged manually"
    return False, f"unknown api submitter for {name}"


def probe_directory(url: str) -> tuple[bool, int | None]:
    return receipt_verify.url_head_ok(url)


def build_submission_package(unit_id: str, unit_url: str, directory: dict) -> Path:
    slug = "".join(c if c.isalnum() else "_" for c in directory["directory"].lower())
    out = _FORGE / "factory" / "distribution" / unit_id / "directory_submissions" / f"{slug}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    body = f"""# Submission package — {directory['directory']}

Unit: `{unit_id}` — {unit_url}

## Submit URL
{directory.get('submit_url', directory['url'])}

## Copy-paste fields

- **Name:** {unit_id}
- **URL:** {unit_url}
- **Tagline:** (paste from factory/distribution/{unit_id}/MANIFEST.json)
- **Category:** {directory.get('category', '(pick best fit)')}
- **Screenshot:** factory/distribution/{unit_id}/screenshot.png  (generate before submitting)

## Instructions

1. Open the submit URL above in a browser
2. Sign in with the operator account (see sigrun-secrets/directory_accounts.md)
3. Paste each field from above
4. Attach screenshot from the path listed
5. Submit
6. When approved, tick the box in state/outreach/PENDING_DIRECTORY_APPROVALS.md
   and update state/outreach/directory_submissions.jsonl with status=approved

Notes: {directory.get('notes', '(none)')}
"""
    out.write_text(body, encoding="utf-8")
    return out


def submit_one(unit_id: str, unit_url: str, directory: dict, dry_run: bool) -> dict:
    d_url = directory["url"]
    reachable, status = probe_directory(d_url) if not dry_run else (True, 200)
    if not reachable:
        row = {
            "ts_utc": _utc(),
            "unit_id": unit_id,
            "directory": directory["directory"],
            "url": d_url,
            "status": "skipped_site_down",
            "detail": f"HEAD status={status}",
        }
        append_submission(row)
        chain_row.append_row(
            LOOP,
            action=f"skip_site_down:{directory['directory']}",
            verifier_result=f"HEAD status={status}",
            claim_status="partial",
            remaining_risk=["retry_later"],
            next_safe_action="skip",
            honest_flaw="directory unreachable",
            extra=row,
        )
        return row

    kind = directory.get("submit_kind", "web_form")
    if kind == "api":
        posted, detail = submit_api(directory, unit_id, unit_url, dry_run)
        if posted:
            row = {
                "ts_utc": _utc(),
                "unit_id": unit_id,
                "directory": directory["directory"],
                "url": d_url,
                "status": "submitted_api",
                "detail": detail,
                "dry_run": dry_run,
            }
            append_submission(row)
            chain_row.append_row(
                LOOP,
                action=f"api_submit:{directory['directory']}",
                verifier_result=detail,
                claim_status="wired_with_receipts",
                remaining_risk=["approval_pending"],
                next_safe_action="await_approval_email",
                honest_flaw="none",
                extra=row,
            )
            return row
        # Fall through to web_form staging
        directory = {**directory, "submit_kind": "web_form", "notes": (directory.get("notes", "") + f"; api fallback: {detail}").strip("; ")}

    pkg = build_submission_package(unit_id, unit_url, directory)
    entry = {
        "directory": directory["directory"],
        "url": d_url,
        "submit_url": directory.get("submit_url", d_url),
        "staged_at": _utc(),
        "reason": "web_form or captcha",
    }
    append_pending(unit_id, entry)
    row = {
        "ts_utc": _utc(),
        "unit_id": unit_id,
        "directory": directory["directory"],
        "url": d_url,
        "status": "staged_for_operator",
        "package_path": str(pkg.relative_to(_FORGE)),
        "dry_run": dry_run,
    }
    append_submission(row)
    chain_row.append_row(
        LOOP,
        action=f"stage_operator:{directory['directory']}",
        verifier_result=f"package at {pkg.name}",
        claim_status="proposed",
        remaining_risk=["operator_may_not_get_to_it"],
        next_safe_action="operator_submit_via_browser",
        honest_flaw="requires human",
        extra=row,
    )
    return row


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--unit-id", required=True, help="shipped unit slug (must exist in MICROSAAS_SHIPS.jsonl)")
    p.add_argument("--url", required=True, help="deployed unit URL")
    p.add_argument("--directories", type=Path, required=True, help="CSV: directory,url,submit_kind,notes")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--skip-gate", action="store_true", help="bypass class-preauth (single-shot only)")
    args = p.parse_args(argv)

    if not args.skip_gate:
        active, quota = gate_reader.gate_active(CLASS_NAME)
        if not active:
            chain_row.append_row(
                LOOP,
                action="gate_missing",
                verifier_result=f"no live class:{CLASS_NAME} line in approvals/latest.txt",
                claim_status="failed",
                remaining_risk=["nothing_submitted"],
                next_safe_action=f"operator_add: class:{CLASS_NAME}:quota=N:seq_range=001-999:expires=<UTC>",
                honest_flaw="pre-authorization missing",
            )
            print(f"HALT: no live class:{CLASS_NAME} line. Add one to state/experiments/approvals/latest.txt")
            return 2
    else:
        quota = None

    directories = load_directories(args.directories)
    if not directories:
        print("no directories in CSV")
        return 0

    chain_row.append_row(
        LOOP,
        action=f"start_batch:{args.unit_id}",
        verifier_result=f"{len(directories)} dirs; quota={quota}",
        claim_status="proposed",
        remaining_risk=["some_dirs_may_fail"],
        next_safe_action="iterate_directories",
        honest_flaw="none",
        extra={"unit_id": args.unit_id, "n_directories": len(directories), "quota": quota},
    )

    limit = quota if quota is not None else len(directories)
    results = []
    for d in directories[:limit]:
        results.append(submit_one(args.unit_id, args.url, d, args.dry_run))

    summary = {
        "unit_id": args.unit_id,
        "attempted": len(results),
        "submitted_api": sum(1 for r in results if r.get("status") == "submitted_api"),
        "staged_for_operator": sum(1 for r in results if r.get("status") == "staged_for_operator"),
        "skipped_site_down": sum(1 for r in results if r.get("status") == "skipped_site_down"),
    }
    chain_row.append_row(
        LOOP,
        action=f"finish_batch:{args.unit_id}",
        verifier_result=json.dumps(summary),
        claim_status="wired_with_receipts",
        remaining_risk=["operator_still_owes_web_form_submits"],
        next_safe_action="operator_process_PENDING_DIRECTORY_APPROVALS",
        honest_flaw="none",
        extra=summary,
    )
    if summary["staged_for_operator"] > 5:
        slack_escalate.escalate(
            LOOP,
            f"{summary['staged_for_operator']} pending dir approvals for {args.unit_id}",
            f"See {PENDING_QUEUE.relative_to(_FORGE)}",
            severity="warn",
        )
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
