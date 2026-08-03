#!/usr/bin/env python3
"""Stage cold-email drafts from state/outreach/cold_email_targets_*.csv.

Produces:
  outputs/staged_sends/cold_email/<seq>_<slug>/draft.json      -- per-target draft
  outputs/staged_sends/cold_email/<seq>_<slug>/README.md       -- human-readable
  outputs/staged_sends/OPERATOR_APPROVAL_INDEX_20260803.md      -- APPENDED with market=cold_email rows

Does NOT send. Does NOT touch state/experiments/approvals/latest.txt (that is
the operator's turn). Once run, operator adds a single class line to the gate
and the sender picks up all cold_email rows in the index.

Usage:
  python tools/outreach/stage_cold_emails.py \
      --targets state/outreach/cold_email_targets_20260803.csv \
      --seq-start 151  # continues after the existing 150 staged drafts
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGED_ROOT = ROOT / "outputs" / "staged_sends" / "cold_email"
INDEX_PATH = ROOT / "outputs" / "staged_sends" / "OPERATOR_APPROVAL_INDEX_20260803.md"

# Sigrún envelope ENV_COLD_EMAIL_001 §D.message_class.template
TEMPLATE = """Subject: {subject}
Hi {first_name} — I saw {public_signal_url}.
{one_sentence_specific_observation}
I do a fixed $350 diagnostic: I map the failure, show you the fix, and you keep the write-up whether or not we work together.
Worth 20 minutes? {{{{BOOKING_LINK}}}}
— {{{{SENDER_NAME}}}}, agentreleasegate.com
{{{{UNSUBSCRIBE_LINK}}}} · {{{{POSTAL_ADDRESS}}}}
"""


def slugify(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")[:60] or "unknown"


def load_targets(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def build_draft(row: dict) -> dict:
    fname = (row.get("first_name") or "").strip()
    if not fname:
        # envelope §D.reject_if forbids generic first-name — flag for operator review
        return {"error": f"row for {row.get('email')} missing first_name; envelope requires personalized greeting"}
    company = row.get("company", "").strip()
    pain = row.get("one_line_pain_signal", "").strip()
    source = row.get("source_url", "").strip()
    subject = f"{pain[:60].rstrip()} on {company}"
    body = TEMPLATE.format(
        subject=subject,
        first_name=fname,
        public_signal_url=source,
        one_sentence_specific_observation=f"That signal — \"{pain}\" — is exactly the shape of thing I fix.",
    )
    return {
        "to": row["email"],
        "first_name": fname,
        "company": company,
        "subject": subject,
        "body": body,
        "priority": int(row.get("priority") or 3),
        "source_url": source,
        "pain_signal": pain,
        # required_slots per envelope §D:
        "required_slots_filled": {
            "company": bool(company),
            "first_name": bool(fname),
            "public_signal_url": bool(source),
            "one_sentence_specific_observation": bool(pain),
            "booking_link": "TEMPLATE_TOKEN",  # substituted at send time from .env
            "unsubscribe_link": "TEMPLATE_TOKEN",
            "postal_address": "TEMPLATE_TOKEN",
        },
    }


def append_index_rows(rows: list[tuple[int, str, str, str, str, str]]) -> None:
    """rows: list of (seq, market, target, subject, expires_utc, package_path)"""
    with INDEX_PATH.open("a", encoding="utf-8") as fh:
        fh.write("\n<!-- cold_email rows appended 2026-08-02 by tools/outreach/stage_cold_emails.py -->\n")
        for seq, market, target, subject, expires, pkg in rows:
            fh.write(f"| {seq:03d} | {market} | {target} | {subject} | {expires} | `{pkg}` |\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", required=True, type=Path)
    ap.add_argument("--seq-start", type=int, default=151)
    ap.add_argument("--expires-days", type=int, default=14)
    args = ap.parse_args()

    targets = load_targets(args.targets)
    expires = (datetime.now(timezone.utc) + timedelta(days=args.expires_days)).strftime("%Y-%m-%dT%H:%M:%SZ")

    STAGED_ROOT.mkdir(parents=True, exist_ok=True)
    index_rows: list[tuple[int, str, str, str, str, str]] = []
    staged_count = skipped_count = 0
    seq = args.seq_start
    for row in targets:
        draft = build_draft(row)
        if "error" in draft:
            skipped_count += 1
            print(f"SKIP seq={seq} {row.get('email')}: {draft['error']}")
            continue
        slug = slugify(f"{seq:03d}_{row.get('company','unknown')}")
        pkg_dir = STAGED_ROOT / slug
        pkg_dir.mkdir(parents=True, exist_ok=True)
        (pkg_dir / "draft.json").write_text(json.dumps(draft, indent=2), encoding="utf-8")
        (pkg_dir / "README.md").write_text(
            f"# Cold email seq={seq:03d} — {draft['company']}\n\n"
            f"- to: {draft['to']}\n"
            f"- priority: {draft['priority']}\n"
            f"- source: {draft['source_url']}\n"
            f"- pain: {draft['pain_signal']}\n\n"
            f"## Subject\n{draft['subject']}\n\n## Body\n```\n{draft['body']}\n```\n",
            encoding="utf-8",
        )
        pkg_rel = f"outputs/staged_sends/cold_email/{slug}"
        subject_col = draft["subject"].replace("|", "\\|")
        index_rows.append((seq, "cold_email", draft["to"], subject_col, expires, pkg_rel))
        staged_count += 1
        seq += 1

    if index_rows:
        append_index_rows(index_rows)
    print(json.dumps({"staged": staged_count, "skipped": skipped_count, "index_rows_appended": len(index_rows), "seq_last": seq - 1}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
