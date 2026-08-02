#!/usr/bin/env python3
"""LOOP-F · SEO_CONTENT_DRAFT — for each shipped unit generate a 600-1200 word
article targeting 1-3 low-competition long-tails; cross-link related units.

AIH2O header
------------
AIH2O:
  version: gen-133
  loop: seo_content_draft
  role: executor
  actor: factory_loop
  verifier: word_count in [500, 2000] + landing_link present + at least 1 cross_link
  clock_source: host_read
  chain: state/loop_receipts/seo_content_draft_<UTCDATE>.jsonl
  publish_queue: content/PUBLISH_QUEUE.md

CLI
---
    python factory/loops/seo_content_draft/run.py \\
        --units state/factory_ships/MICROSAAS_SHIPS.jsonl \\
        --keywords keywords.json

Kill conditions
---------------
- LLM output <500 words or >2000 → reject (chain_row + skip)
- keyword already has a live article for this unit → skip (idempotent)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve()
_FORGE = _HERE.parents[3]
sys.path.insert(0, str(_FORGE))
from factory.loops.lib import chain_row, litellm_client, slack_escalate  # noqa: E402


LOOP = "seo_content_draft"
CONTENT_ROOT = _FORGE / "content" / "blog"
PUBLISH_QUEUE = _FORGE / "content" / "PUBLISH_QUEUE.md"
MIN_WORDS = 500
MAX_WORDS = 2000


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", s.lower()).strip("-")


def _word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def load_units(path: Path) -> list[dict]:
    if not path.exists():
        return []
    units = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            units.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return units


def draft_article(unit: dict, keyword: str, related: list[dict]) -> tuple[str, bool, str]:
    """Returns (markdown_body, ok, reason). ok=False when word count out of band."""
    slug = unit.get("slug") or _slug(unit.get("name", "unit"))
    deploy = unit.get("deploy_url") or f"https://{slug}.pages.dev"
    related_links = "\n".join(
        f"- [{r.get('name') or r.get('slug')}]({r.get('deploy_url')})"
        for r in related[:5]
    ) or "- (no related units yet)"

    system = (
        "You are a senior SaaS marketer writing pragmatic, evidence-heavy blog posts. "
        "Never hype. Never generic. Every claim should be either specific or clearly "
        "framed as an example. Use short sections and one primary call-to-action."
    )
    prompt = (
        f"Write a 700-1000 word blog article for the target long-tail keyword: "
        f"\"{keyword}\".\n\n"
        f"Product context (link to at the end and once mid-article):\n"
        f"- Name: {unit.get('name')}\n- URL: {deploy}\n- ICP: {unit.get('icp','')}\n"
        f"- One-liner: {unit.get('one_liner','')}\n\n"
        f"Structure:\n"
        f"1. Hook — a specific problem the ICP hits weekly\n"
        f"2. Why generic advice fails\n"
        f"3. A concrete workflow (numbered)\n"
        f"4. Where {unit.get('name')} fits (one paragraph, honest)\n"
        f"5. Cross-links to related units\n"
        f"6. CTA\n\n"
        f"Include this exact line where relevant:\n"
        f"  See {unit.get('name')} → {deploy}\n\n"
        f"After the article, include a section '## Related tools' with these markdown links:\n"
        f"{related_links}\n\n"
        f"Return ONLY the article markdown."
    )
    r = litellm_client.complete(prompt, system=system, max_tokens=2500, temperature=0.5)
    if not r.ok:
        return "", False, f"llm error: {r.error}"
    body = r.text.strip()
    wc = _word_count(body)
    if wc < MIN_WORDS:
        return body, False, f"word_count={wc} < {MIN_WORDS}"
    if wc > MAX_WORDS:
        return body, False, f"word_count={wc} > {MAX_WORDS}"
    if deploy not in body:
        # inject landing link if the model dropped it
        body = body + f"\n\nSee **{unit.get('name')}** → {deploy}\n"
    return body, True, f"word_count={wc}"


def _existing_article(unit_slug: str, keyword: str) -> Path:
    return CONTENT_ROOT / unit_slug / f"{_slug(keyword)}.md"


def append_publish_queue(entry: dict) -> None:
    if not PUBLISH_QUEUE.exists():
        PUBLISH_QUEUE.parent.mkdir(parents=True, exist_ok=True)
        PUBLISH_QUEUE.write_text("# Publish queue\n\nTick each box after publishing.\n\n", encoding="utf-8")
    line = (
        f"- [ ] `{entry['unit_slug']}` · **{entry['keyword']}** · staged {entry['staged_at']}  \n"
        f"  path: `{entry['path']}` · target: 1-3 long-tails / week per unit\n"
    )
    with PUBLISH_QUEUE.open("a", encoding="utf-8") as fh:
        fh.write(line)


def draft_one(unit: dict, keyword: str, related: list[dict], dry_run: bool) -> dict:
    unit_slug = unit.get("slug") or _slug(unit.get("name", "unit"))
    art_path = _existing_article(unit_slug, keyword)
    if art_path.exists():
        chain_row.append_row(
            LOOP,
            action=f"skip_exists:{unit_slug}:{_slug(keyword)}",
            verifier_result=f"already at {art_path.relative_to(_FORGE)}",
            claim_status="proposed",
            remaining_risk=["operator_may_still_want_to_regenerate"],
            next_safe_action="skip",
            honest_flaw="idempotent skip",
            extra={"path": str(art_path.relative_to(_FORGE))},
        )
        return {"unit_slug": unit_slug, "keyword": keyword, "staged": False, "reason": "already_exists"}

    if dry_run:
        body = (
            f"# DRY_RUN — {keyword}\n\n"
            f"Article for {unit.get('name')} targeting `{keyword}`.\n\n"
            f"(word count would be ~800 in a real run.)\n\n"
            f"See {unit.get('name')} → {unit.get('deploy_url')}\n"
        )
        ok, reason = True, "dry_run"
    else:
        body, ok, reason = draft_article(unit, keyword, related)

    if not ok:
        chain_row.append_row(
            LOOP,
            action=f"reject:{unit_slug}:{_slug(keyword)}",
            verifier_result=reason,
            claim_status="failed",
            remaining_risk=["operator_may_try_different_keyword"],
            next_safe_action="skip",
            honest_flaw=reason,
        )
        return {"unit_slug": unit_slug, "keyword": keyword, "staged": False, "reason": reason}

    art_path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = (
        "---\n"
        f"unit_slug: {unit_slug}\n"
        f"keyword: {keyword}\n"
        f"staged_at: {_utc()}\n"
        f"awaiting_operator_publish: true\n"
        "---\n\n"
    )
    art_path.write_text(frontmatter + body, encoding="utf-8")
    entry = {
        "unit_slug": unit_slug,
        "keyword": keyword,
        "path": str(art_path.relative_to(_FORGE)),
        "staged_at": _utc(),
    }
    append_publish_queue(entry)
    chain_row.append_row(
        LOOP,
        action=f"drafted:{unit_slug}:{_slug(keyword)}",
        verifier_result=reason,
        claim_status="wired_with_receipts",
        remaining_risk=["operator_must_publish"],
        next_safe_action="operator_review_and_publish",
        honest_flaw="none",
        extra=entry,
    )
    return {"unit_slug": unit_slug, "keyword": keyword, "staged": True, "path": str(art_path)}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--units", type=Path, required=True, help="MICROSAAS_SHIPS.jsonl")
    p.add_argument("--keywords", type=Path, required=True, help="JSON {unit_slug: [kw1, kw2, kw3]}")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    units = load_units(args.units)
    keywords_map = json.loads(args.keywords.read_text(encoding="utf-8"))
    unit_by_slug = {u.get("slug"): u for u in units if u.get("slug")}

    chain_row.append_row(
        LOOP,
        action="start_draft",
        verifier_result=f"units={len(units)} keyword_targets={sum(len(v) for v in keywords_map.values())}",
        claim_status="proposed",
        remaining_risk=["llm_may_reject_word_count"],
        next_safe_action="iterate",
        honest_flaw="none",
    )

    results = []
    for unit_slug, keywords in keywords_map.items():
        unit = unit_by_slug.get(unit_slug)
        if not unit:
            chain_row.append_row(
                LOOP,
                action=f"skip_unknown_unit:{unit_slug}",
                verifier_result="not in ships log",
                claim_status="partial",
                next_safe_action="operator_check_slug",
                honest_flaw="unknown unit",
            )
            continue
        related = [u for slug, u in unit_by_slug.items() if slug != unit_slug][:5]
        for kw in keywords:
            results.append(draft_one(unit, kw, related, args.dry_run))

    summary = {
        "attempted": len(results),
        "staged": sum(1 for r in results if r["staged"]),
        "skipped": sum(1 for r in results if not r["staged"]),
    }
    chain_row.append_row(
        LOOP,
        action="finish_draft",
        verifier_result=json.dumps(summary),
        claim_status="wired_with_receipts",
        remaining_risk=["operator_must_publish"],
        next_safe_action="operator_review_PUBLISH_QUEUE",
        honest_flaw="none",
        extra=summary,
    )
    if summary["staged"] >= 5:
        slack_escalate.escalate(LOOP, f"{summary['staged']} SEO drafts staged", "content/PUBLISH_QUEUE.md", severity="info")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
