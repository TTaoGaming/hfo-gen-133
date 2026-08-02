#!/usr/bin/env python3
"""LINKEDIN-OUTBOUND-STAGER — worker E, EMERGENCY_FORGE 2026-08-03.

STAGE-ONLY. Never sends a DM, never scrapes LinkedIn live. Reads cached public
profile fields from state/factory_input/linkedin_targets.jsonl (creating it
with a documented schema + placeholder rows if absent), drafts one personalized
DM, and writes it under outputs/staged_sends/linkedin_dms/. Actually sending is
a SEND-class action and is out of envelope for this skill.

Prints exactly one JSON payload line on stdout and exits 0.

clock_source=host_read.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
TARGETS = ROOT / "state" / "factory_input" / "linkedin_targets.jsonl"
OUT_DIR = ROOT / "outputs" / "staged_sends" / "linkedin_dms"

TARGETS_SCHEMA_DOC = {
    "source": "schema_doc",
    "_schema": {
        "profile_url": "canonical https://www.linkedin.com/in/<handle>/ URL, required, key field",
        "name": "public display name as shown on the profile",
        "headline": "the LinkedIn headline line under the name",
        "company": "current company shown on the profile (public)",
        "recent_post": "one-line gist of a recent public post/activity, if known",
        "mutual_connection": "name of a shared connection, if known",
        "source": "'placeholder' (operator must fill in) | 'manual' (operator entered) | "
                  "'probe_uncached' (auto-created stub for an unknown URL, do not send on)",
    },
    "_note": "This file is STAGE-ONLY input. No row here was produced by scraping "
             "LinkedIn live; rows are seeded manually by the operator from what he "
             "already sees on a profile, or filled in by hand later. linkedin_outbound.py "
             "reads this file; it never writes scraped data into it.",
}

PLACEHOLDER_ROWS = [
    {
        "source": "placeholder",
        "profile_url": "https://www.linkedin.com/in/example-genai-founder/",
        "name": "(placeholder - fill in from the profile)",
        "headline": "(placeholder - fill in)",
        "company": "(placeholder - fill in)",
        "recent_post": "(placeholder - fill in)",
        "mutual_connection": "(placeholder - fill in)",
    },
    {
        "source": "placeholder",
        "profile_url": "https://www.linkedin.com/in/example-indie-studio-lead/",
        "name": "(placeholder - fill in from the profile)",
        "headline": "(placeholder - fill in)",
        "company": "(placeholder - fill in)",
        "recent_post": "(placeholder - fill in)",
        "mutual_connection": "(placeholder - fill in)",
    },
    {
        "source": "placeholder",
        "profile_url": "https://www.linkedin.com/in/example-webxr-researcher/",
        "name": "(placeholder - fill in from the profile)",
        "headline": "(placeholder - fill in)",
        "company": "(placeholder - fill in)",
        "recent_post": "(placeholder - fill in)",
        "mutual_connection": "(placeholder - fill in)",
    },
]

TEMPLATES = {
    "spatial_pilot_v1": {
        "subject": "Quick question re: spatial / hand-tracking pilots",
        "opener": "Saw your profile{headline_clause}{company_clause} and figured it was worth a direct note.",
        "pitch": (
            "I've been shipping a small library of self-contained HTML5 games and a "
            "hand-tracking / spatial-input prototype (no install, runs in the browser tab "
            "it's loaded in) and I'm looking for a couple of early pilot users to kick the "
            "tires and tell me honestly where it breaks."
        ),
        "ask": "If that's at all in your lane, would you be open to a 15-minute look? No pitch deck, just the running thing.",
    },
}


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slug_from_url(url: str) -> str:
    m = re.search(r"linkedin\.com/in/([^/]+)/?", url)
    return m.group(1) if m else url.rstrip("/").rsplit("/", 1)[-1]


def guess_name(slug: str) -> str:
    words = re.split(r"[-_]+", slug)
    words = [w for w in words if not w.isdigit()]
    return " ".join(w.capitalize() for w in words) if words else slug


def ensure_targets_file() -> bool:
    """Return True if the file was just created."""
    if TARGETS.exists():
        return False
    TARGETS.parent.mkdir(parents=True, exist_ok=True)
    rows = [TARGETS_SCHEMA_DOC] + PLACEHOLDER_ROWS
    with TARGETS.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    return True


def load_cached(profile_url: str) -> dict | None:
    """Match on `profile_url` (this skill's own schema) or `url` (an existing
    factory_input/linkedin_targets.jsonl authored by another worker/session with
    a different column set) — read compatibility, never rewrites the file."""
    if not TARGETS.exists():
        return None
    target = profile_url.rstrip("/")
    for line in TARGETS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        try:
            row = json.loads(line)
        except Exception:
            continue
        if row.get("source") == "schema_doc":
            continue
        row_url = row.get("profile_url") or row.get("url") or ""
        if row_url.rstrip("/") == target:
            return row
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile-url", required=True)
    ap.add_argument("--template", required=True)
    args = ap.parse_args()

    created = ensure_targets_file()
    row = load_cached(args.profile_url)

    slug = slug_from_url(args.profile_url)
    cited_fields: list = []
    row_name = str(row.get("name", "")) if row else ""
    is_unusable = (
        not row
        or row.get("source") == "placeholder"
        or row_name.startswith("(")
        or "EXAMPLE" in row_name.upper()
        or "PLACEHOLDER" in row_name.upper()
        or "DO_NOT_SEND" in row_name.upper()
    )
    if not is_unusable:
        name = row.get("name") or guess_name(slug)
        headline = row.get("headline") or row.get("role") or ""
        company = row.get("company") or ""
        why = row.get("why") or row.get("recent_post") or ""
        if row.get("name"):
            cited_fields.append("name")
        if headline:
            cited_fields.append("headline" if row.get("headline") else "role")
        if company:
            cited_fields.append("company")
        if why:
            cited_fields.append("why")
    else:
        # no usable cache hit -> honest fallback, cite only the URL itself
        name = guess_name(slug)
        headline = ""
        company = ""
        why = ""
        cited_fields.append("profile_url")

    tmpl = TEMPLATES.get(args.template, TEMPLATES["spatial_pilot_v1"])
    headline_clause = f" ({headline})" if headline else ""
    company_clause = f" at {company}" if company else ""
    opener = tmpl["opener"].format(headline_clause=headline_clause, company_clause=company_clause)
    why_line = f"{why}\n\n" if why else ""

    body = (
        f"Hi {name},\n\n"
        f"{opener}\n\n"
        f"{why_line}"
        f"{tmpl['pitch']}\n\n"
        f"{tmpl['ask']}\n\n"
        f"Either way, thanks for reading this far — {args.profile_url}\n"
        f"— Tommy"
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fname = f"{slug}_{args.template}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    draft_path = OUT_DIR / fname

    draft = {
        "skill": "linkedin_outbound",
        "ts_utc": now_utc(),
        "clock_source": "host_read",
        "profile_url": args.profile_url,
        "template": args.template,
        "target_profile": {"slug": slug, "name": name, "headline": headline, "company": company},
        "subject": tmpl["subject"],
        "body": body,
        "cited_fields": cited_fields,
        "cache_hit": not is_unusable,
        "targets_file_created_this_run": created,
        "send_mode": "STAGE_ONLY_NOT_SENT",
    }
    draft_path.write_text(json.dumps(draft, indent=2), encoding="utf-8")

    payload = {
        "skill": "linkedin_outbound",
        "ts_utc": draft["ts_utc"],
        "target_profile": name,
        "subject": tmpl["subject"],
        "body": body,
        "draft_path": str(draft_path.relative_to(ROOT)),
        "cited_fields": cited_fields,
        "cache_hit": draft["cache_hit"],
        "send_mode": "STAGE_ONLY_NOT_SENT",
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
