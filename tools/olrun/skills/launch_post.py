#!/usr/bin/env python3
"""HN-PH-LAUNCH-DRAFT — worker E, EMERGENCY_FORGE 2026-08-03.

Drafts a platform-appropriate launch post for a given artifact URL. Three
genuinely different bodies, one file per platform, under
outputs/staged_sends/launch_drafts/. STAGE-ONLY — never posts anywhere.

Prints exactly one JSON payload line on stdout and exits 0.

clock_source=host_read.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
OUT_DIR = ROOT / "outputs" / "staged_sends" / "launch_drafts"


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def draft_hn_show(artifact: str) -> dict:
    title = "Show HN: 21 self-contained HTML5 games, one static Cloudflare Pages site"
    body = (
        "What it is: 21 small single-page HTML5 games (snake, memory match, a slide "
        "puzzle, a rhythm-tap game, and so on), each one a self-contained page with no "
        "build step, no account, and no external network calls once loaded, hosted as a "
        "static site.\n\n"
        f"Link: {artifact}\n\n"
        "What's novel here isn't any single game — they're deliberately small — it's the "
        "distribution shape: one static deploy, no server, no login wall, embeddable in a "
        "portal iframe at any size, and a manifest per title so the same catalog can be "
        "resubmitted to itch.io / CrazyGames / Poki without redoing the packaging by hand.\n\n"
        "Honest limits: no accounts, no leaderboards, no monetization wired up yet, and "
        "this is a first pass at the pipeline more than a curated 'best 21 games' pick — "
        "some are genuinely rough. Every title is now checked by a headless-chromium gate "
        "that presses start and asserts the game loop actually runs with a clean console; "
        "that gate found one title dead on a JS syntax error, which is fixed.\n\n"
        "I'd rather hear what's broken than get upvotes — if a game hangs, doesn't load, "
        "or the touch controls are wrong on your phone, that's exactly the kind of thing "
        "I want to know."
    )
    return {"title": title, "body": body}


def draft_product_hunt(artifact: str) -> dict:
    tagline = "21 tiny browser games, one link, zero installs"
    description = (
        "A small catalog of self-contained HTML5 games — snake, memory match, a "
        "slide puzzle, a physics-y hex-flip board, and more — deployed as one static "
        "site so any of them load instantly in a browser tab with nothing to install "
        "and no account to create. Built to be portable: the same build can be staged "
        "for itch.io, CrazyGames, Poki, or Kongregate without a rewrite."
    )
    first_comment = (
        "Maker here. This started as a distribution-pipeline experiment more than a "
        "game jam: can one small team package, host, and re-submit a batch of tiny "
        "games to multiple portals without hand-rebuilding each one? The games "
        "themselves are intentionally light — a few minutes of play each — the "
        "interesting part is the packaging. Screenshots/cover art are still missing on "
        "most titles (several portals require them before a listing can go public), so "
        f"treat this as an early look, not a finished catalog. Link: {artifact}. Happy "
        "to answer anything about the pipeline or take feedback on which games are "
        "worth polishing further."
    )
    body = f"{tagline}\n\n{description}\n\nFirst comment:\n{first_comment}"
    return {"title": tagline, "body": body, "tagline": tagline,
             "description": description, "first_comment": first_comment}


def draft_reddit(artifact: str) -> dict:
    title = "[Self-Promo] 21 small self-contained HTML5 games, one static site — feedback welcome"
    body = (
        "Flagging this as self-promo up front, posting where the sub's rules allow it "
        "(checking the self-promo/Feedback Friday thread norms for whichever sub this "
        "lands in before submitting for real).\n\n"
        f"Link: {artifact}\n\n"
        "21 tiny single-page HTML5 games — no installs, no accounts, no external calls "
        "once the page loads. This is a distribution-pipeline experiment as much as a "
        "game drop: everything is packaged so the same build can be re-staged for "
        "itch.io / CrazyGames / Poki without hand-editing each submission.\n\n"
        "What I actually want out of this post: which 2-3 of the 21 are worth "
        "polishing further, and any bug reports (mobile touch controls are the most "
        "likely place something's broken). Not looking for upvotes, looking for "
        "'this one's dead, don't bother' or 'this one's actually fun, do more like it.'"
    )
    return {"title": title, "body": body}


PLATFORMS = {
    "hn_show": draft_hn_show,
    "product_hunt": draft_product_hunt,
    "reddit": draft_reddit,
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--platform", required=True, choices=sorted(PLATFORMS))
    args = ap.parse_args()

    drafted = PLATFORMS[args.platform](args.artifact)
    ts = now_utc()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    draft_path = OUT_DIR / f"{args.platform}_{stamp}.md"

    md_lines = [
        f"# launch draft — {args.platform}",
        "",
        f"artifact: {args.artifact}",
        f"generated_utc: {ts}  (clock_source=host_read)",
        "status: STAGE_ONLY_NOT_POSTED",
        "",
        f"## title / tagline",
        "",
        drafted["title"],
        "",
        "## body",
        "",
        drafted["body"],
    ]
    draft_path.write_text("\n".join(md_lines), encoding="utf-8")

    payload = {
        "skill": "launch_post",
        "ts_utc": ts,
        "clock_source": "host_read",
        "platform": args.platform,
        "artifact": args.artifact,
        "title": drafted["title"],
        "body": drafted["body"],
        "draft_path": str(draft_path.relative_to(ROOT)),
        "status": "STAGE_ONLY_NOT_POSTED",
    }
    if "tagline" in drafted:
        payload["tagline"] = drafted["tagline"]
    if "first_comment" in drafted:
        payload["first_comment"] = drafted["first_comment"]
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
