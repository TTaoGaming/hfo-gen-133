"""Write one sample directory per opportunity, in the format the brief specifies."""
from __future__ import annotations

import json
import os

from .core import Artifact, Grade, Opportunity, today_utc, utc_now


def sample_dir(root: str, op: Opportunity, seq: int) -> str:
    return os.path.join(root, today_utc(), op.adapter, f"{seq:03d}_{op.slug()}")


def emit(root: str, op: Opportunity, artifacts: list[Artifact], grades: list[Grade],
         seq: int, legal_note: str = "") -> str:
    d = sample_dir(root, op, seq)
    os.makedirs(d, exist_ok=True)

    with open(os.path.join(d, "source_listing.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump({**op.to_json(), "captured_utc": utc_now(),
                   "source_attribution": legal_note}, fh, indent=2, ensure_ascii=False)

    by_id = {g.variant_id: g for g in grades}
    for i, art in enumerate(artifacts, 1):
        g = by_id[art.variant_id]
        with open(os.path.join(d, f"variant_{i:02d}.md"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(f"# variant_{i:02d} · {art.strategy}\n\n")
            fh.write(f"- **channel:** {art.channel}\n")
            fh.write(f"- **target:** {art.named_target}\n")
            fh.write(f"- **listing:** {op.url}\n")
            fh.write(f"- **the ask (falsifiable):** {art.price_or_date_ask}\n")
            fh.write(f"- **grade:** rank {g.rank} · total {g.total:.3f} · "
                     f"reward_hack_risk **{g.reward_hack_risk}**\n\n")
            fh.write("---\n\n")
            fh.write(f"**Subject:** {art.subject}\n\n")
            fh.write(art.body.rstrip() + "\n")

    with open(os.path.join(d, "apex_grade.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump({
            "opportunity_uid": op.uid,
            "graded_utc": utc_now(),
            "grader": "tools.factory.grade (deterministic, structural, no model call)",
            "fit_components": op.fit_components,
            "fit_signals": op.fit_signals,
            "grades": [g.to_json() for g in grades],
        }, fh, indent=2, ensure_ascii=False)

    best = min(grades, key=lambda g: g.rank)
    best_art = next(a for a in artifacts if a.variant_id == best.variant_id)
    best_idx = artifacts.index(best_art) + 1

    risk_flag = {"low": "🟢 LOW", "medium": "🟡 MEDIUM", "high": "🔴 HIGH"}[best.reward_hack_risk]
    with open(os.path.join(d, "HUMAN_REVIEW.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f"# {op.entity} — {op.title}\n\n")
        fh.write(f"**Listing:** {op.url}\n\n")
        fh.write(f"| | |\n|---|---|\n")
        fh.write(f"| market | {op.market} ({op.adapter}) |\n")
        fh.write(f"| fit score | **{op.fit_score:.2f}** — {', '.join(op.fit_signals[:6]) or 'n/a'} |\n")
        fh.write(f"| compensation | {op.compensation or 'not stated'} |\n")
        fh.write(f"| location | {op.location or 'not stated'} |\n")
        fh.write(f"| contact published | {op.contact or 'no — apply via the listing'} |\n")
        fh.write(f"| posted | {op.posted_utc or 'not stated'} |\n\n")
        fh.write(f"## Top pick: `variant_{best_idx:02d}.md` — {best_art.strategy}\n\n")
        fh.write(f"**Reward-hack risk: {risk_flag}**\n\n")
        fh.write(f"{best.one_line_verdict}\n\n")
        fh.write(f"**The ask:** {best_art.price_or_date_ask}\n\n")
        fh.write("**Risk notes:**\n\n")
        for r in best.reward_hack_reasons:
            fh.write(f"- {r}\n")
        fh.write("\n**Failed checks:** ")
        failed = [k for k, v in best.checks.items() if not v]
        fh.write((", ".join(failed) if failed else "none") + "\n\n")
        fh.write("## All variants\n\n| # | strategy | total | risk | ask |\n|---|---|---|---|---|\n")
        for i, a in enumerate(artifacts, 1):
            g = by_id[a.variant_id]
            fh.write(f"| {i} | {a.strategy} | {g.total:.3f} | {g.reward_hack_risk} | "
                     f"{a.price_or_date_ask} |\n")
        fh.write("\n## Their stated requirements (parsed)\n\n")
        for r in op.requirements[:8]:
            fh.write(f"- {r}\n")
        if legal_note:
            fh.write(f"\n---\n\n*{legal_note}*\n")
        fh.write("\n> ⛔ NOT SENT. Nothing in this directory has been transmitted anywhere. "
                 "Sending requires operator approval per the class-preauthorization envelope.\n")
    return d
