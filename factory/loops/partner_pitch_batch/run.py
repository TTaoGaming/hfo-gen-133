#!/usr/bin/env python3
"""LOOP-E · PARTNER_PITCH_BATCH — fetch partner content, extract ONE
genuine reference, personalize a template, stage for operator sign.

Never sends. Never generic. Staging path is the deliverable.

AIH2O header
------------
AIH2O:
  version: gen-133
  loop: partner_pitch_batch
  role: executor
  actor: factory_loop
  verifier: receipt_verify.verify_before_send required_slots + gate_reader.gate_active('partner_pitch')
  clock_source: host_read
  chain: state/loop_receipts/partner_pitch_batch_<UTCDATE>.jsonl
  staged_out: state/outreach/partner_pitches/<partner_slug>_<UTCDATE>.md
  index: state/outreach/PARTNER_PITCH_INDEX_<isoweek>.md

CLI
---
    python factory/loops/partner_pitch_batch/run.py \\
        --partners partners.csv --template template.md --intro intro.txt

Kill conditions
---------------
- Can't fetch partner content → mark UNVERIFIED + skip
- Personalization produces still-unfilled required slots → REJECT
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

_HERE = Path(__file__).resolve()
_FORGE = _HERE.parents[3]
sys.path.insert(0, str(_FORGE))
from factory.loops.lib import chain_row, gate_reader, litellm_client, receipt_verify, slack_escalate  # noqa: E402


LOOP = "partner_pitch_batch"
CLASS_NAME = "partner_pitch"
STAGED_ROOT = _FORGE / "state" / "outreach" / "partner_pitches"
USER_AGENT = "hfo-gen133-factory-loop/0.1 (partner-outreach-personalizer)"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _iso_week() -> str:
    now = datetime.now(timezone.utc)
    y, w, _ = now.isocalendar()
    return f"{y}-W{w:02d}"


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9_-]+", "-", s.lower()).strip("-")


class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.chunks: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript"}:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript"} and self._skip > 0:
            self._skip -= 1

    def handle_data(self, data):
        if self._skip == 0:
            data = data.strip()
            if data:
                self.chunks.append(data)


def fetch_public_url(url: str, timeout: float = 15.0) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read(400_000)  # cap at ~400KB
            enc = resp.headers.get_content_charset() or "utf-8"
            return raw.decode(enc, errors="replace")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError):
        return None


def extract_text(html: str, max_chars: int = 6000) -> str:
    p = _TextExtractor()
    try:
        p.feed(html)
    except Exception:  # noqa: BLE001
        return html[:max_chars]
    joined = " ".join(p.chunks)
    return joined[:max_chars]


def fetch_partner_content(partner: dict) -> tuple[str, list[str]]:
    """Returns (concatenated_text, urls_actually_fetched)."""
    urls = []
    for key in ("blog_url", "site_url", "twitter_url", "youtube_url"):
        v = partner.get(key)
        if v:
            urls.append(v)
    fetched: list[str] = []
    combined: list[str] = []
    for u in urls[:4]:
        html = fetch_public_url(u)
        if html:
            fetched.append(u)
            combined.append(f"--- {u} ---\n{extract_text(html)}")
    return "\n\n".join(combined), fetched


def extract_genuine_reference(text: str, partner_name: str) -> str:
    """Use LLM to pull one specific, quote-able reference — never generic.
    Returns empty string if nothing distinct enough."""
    if not text.strip():
        return ""
    prompt = (
        f"Extract ONE specific, quotable sentence from the following content by "
        f"{partner_name}. Rules:\n"
        f"- Must be a genuine, verifiable claim they made (not paraphrase)\n"
        f"- Must be specific enough that it could ONLY be about them\n"
        f"- Must be under 25 words\n"
        f"- Return ONLY the sentence, no framing\n\n"
        f"If nothing meets these criteria, return the literal token: NONE\n\n"
        f"CONTENT:\n{text[:5000]}"
    )
    r = litellm_client.complete(prompt, max_tokens=80, temperature=0.2)
    if not r.ok:
        return ""
    out = r.text.strip().strip("\"'`").split("\n")[0][:250]
    if out.upper() == "NONE" or len(out) < 15:
        return ""
    return out


def render_template(template: str, values: dict) -> str:
    body = template
    for k, v in values.items():
        body = body.replace("{" + k + "}", str(v))
    return body


def load_partners(csv_path: Path) -> list[dict]:
    with csv_path.open(encoding="utf-8", newline="") as fh:
        return [dict(r) for r in csv.DictReader(fh)]


def pitch_one(partner: dict, template: str, intro: str, dry_run: bool) -> dict:
    name = partner.get("name") or partner.get("partner_name") or "partner"
    slug = _slug(name)
    ts = _utc()
    day = ts[:10].replace("-", "")

    text, fetched = fetch_partner_content(partner)
    if not text.strip():
        chain_row.append_row(
            LOOP,
            action=f"unverified_skip:{slug}",
            verifier_result="no fetchable public content",
            claim_status="failed",
            remaining_risk=["operator_may_pitch_manually"],
            next_safe_action="skip",
            honest_flaw="content fetch returned empty",
            extra={"partner": partner, "fetched": fetched},
        )
        return {"partner": name, "staged": False, "reason": "content_fetch_empty"}

    reference = extract_genuine_reference(text, name) if not dry_run else f"[DRY_RUN reference for {name}]"
    if not reference:
        chain_row.append_row(
            LOOP,
            action=f"rejected_generic:{slug}",
            verifier_result="LLM found no genuine reference",
            claim_status="failed",
            remaining_risk=["operator_can_read_partner_content_manually"],
            next_safe_action="skip_or_pick_different_partner",
            honest_flaw="only generic pitch possible",
            extra={"partner": name, "fetched": fetched},
        )
        return {"partner": name, "staged": False, "reason": "no_genuine_reference"}

    values = {
        "first_name": partner.get("first_name") or name.split()[0],
        "partner_name": name,
        "partner_company": partner.get("company") or partner.get("org") or name,
        "intro_reference": reference,
        "operator_intro": intro.strip(),
        "our_offer": partner.get("offer") or "revshare on any unit we co-launch",
    }
    body = render_template(template, values)

    # Verify no slot remains unfilled
    ok, missing = receipt_verify.required_slots_filled(body, [
        f"{{{k}}}" for k in values.keys()
    ])
    if not ok:
        chain_row.append_row(
            LOOP,
            action=f"rejected_missing_slots:{slug}",
            verifier_result=f"unfilled slots: {missing}",
            claim_status="failed",
            remaining_risk=["template_needs_fix"],
            next_safe_action="operator_fix_template_or_add_partner_fields",
            honest_flaw="slot leftover",
            extra={"missing": missing, "partner": name},
        )
        return {"partner": name, "staged": False, "reason": "unfilled_slots", "missing": missing}

    STAGED_ROOT.mkdir(parents=True, exist_ok=True)
    out = STAGED_ROOT / f"{slug}_{day}.md"
    frontmatter = (
        "---\n"
        f"partner: {name}\n"
        f"partner_slug: {slug}\n"
        f"staged_at: {ts}\n"
        f"reference_source: {(fetched[0] if fetched else 'unknown')}\n"
        f"reference: {json.dumps(reference)}\n"
        f"awaiting_operator_sign: true\n"
        "---\n\n"
    )
    out.write_text(frontmatter + body, encoding="utf-8")

    row = {
        "ts_utc": ts,
        "partner": name,
        "partner_slug": slug,
        "staged_path": str(out.relative_to(_FORGE)),
        "reference_source": fetched[0] if fetched else None,
        "dry_run": dry_run,
    }
    chain_row.append_row(
        LOOP,
        action=f"staged:{slug}",
        verifier_result=f"reference from {row['reference_source']}",
        claim_status="wired_with_receipts",
        remaining_risk=["operator_must_sign_before_send"],
        next_safe_action="operator_review_and_send",
        honest_flaw="none",
        extra=row,
    )
    return {"partner": name, "staged": True, "path": str(out)}


def update_weekly_index(week: str, rows: list[dict]) -> Path:
    out = _FORGE / "state" / "outreach" / f"PARTNER_PITCH_INDEX_{week}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# Partner Pitch Index — {week}\n\n"]
    lines.append(f"Staged this week: {sum(1 for r in rows if r.get('staged'))}\n\n")
    for r in rows:
        status = "staged" if r.get("staged") else f"skipped ({r.get('reason','?')})"
        path = r.get("path", "")
        lines.append(f"- **{r['partner']}** — {status}  \n  {path}\n")
    out.write_text("".join(lines), encoding="utf-8")
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--partners", type=Path, required=True, help="CSV: name,first_name,company,blog_url,site_url,twitter_url,youtube_url,offer")
    p.add_argument("--template", type=Path, required=True, help="template.md with {first_name} {intro_reference} etc.")
    p.add_argument("--intro", type=Path, required=True, help="operator_intro_paragraph.txt")
    p.add_argument("--skip-gate", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    if not args.skip_gate:
        active, quota = gate_reader.gate_active(CLASS_NAME)
        if not active:
            chain_row.append_row(
                LOOP,
                action="gate_missing",
                verifier_result=f"no live class:{CLASS_NAME}",
                claim_status="failed",
                remaining_risk=["nothing_staged"],
                next_safe_action=f"operator_add: class:{CLASS_NAME}:quota=25:seq_range=001-999:expires=<UTC>",
                honest_flaw="gate missing",
            )
            print(f"HALT: no live class:{CLASS_NAME} line.")
            return 2
    else:
        quota = None

    partners = load_partners(args.partners)
    template = args.template.read_text(encoding="utf-8")
    intro = args.intro.read_text(encoding="utf-8")

    limit = quota if quota is not None else len(partners)
    rows = []
    for prt in partners[:limit]:
        rows.append(pitch_one(prt, template, intro, args.dry_run))

    week = _iso_week()
    idx = update_weekly_index(week, rows)
    summary = {
        "week": week,
        "attempted": len(rows),
        "staged": sum(1 for r in rows if r.get("staged")),
        "skipped": sum(1 for r in rows if not r.get("staged")),
        "index": str(idx.relative_to(_FORGE)),
    }
    chain_row.append_row(
        LOOP,
        action=f"finish_batch:{week}",
        verifier_result=json.dumps(summary),
        claim_status="wired_with_receipts",
        remaining_risk=["operator_must_sign_each_pitch"],
        next_safe_action="operator_review_index",
        honest_flaw="none",
        extra=summary,
    )
    if summary["staged"] >= 10:
        slack_escalate.escalate(
            LOOP,
            f"{summary['staged']} partner pitches staged this week",
            f"index: {idx.relative_to(_FORGE)}",
            severity="info",
        )
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
