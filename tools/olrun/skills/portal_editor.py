#!/usr/bin/env python3
"""PORTAL-EDITOR-OUTREACH (EMERGENCY_FORGE 2026-08-03, worker D, HOT-D5).

Writes a genuinely portal-specific editor pitch for one of {poki, crazygames,
kongregate}, citing each portal's real published acceptance criteria as
researched in areas/quorum_research/ (FOSS_GAME_EXEMPLAR_RESEARCH_20260802.md,
DEEP_RESEARCH_INDEX_20260802T1545Z.md) rather than one template with the
portal name find-replaced in.

CLASS ENVELOPE: STAGE only. Never sent to any portal's editorial inbox.

    python tools/olrun/skills/portal_editor.py \
        --portal=poki --game-package=outputs/staged_sends/games/017_snake

Prints exactly one JSON object on stdout. clock_source=host_read.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT_DIR = ROOT / "outputs" / "staged_sends" / "portal_editors"
PORTFOLIO_URL = "https://hfo-games.pages.dev"


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


def load_manifest(game_dir: Path) -> dict:
    manifest_path = game_dir / "itch_manifest.json"
    if manifest_path.exists():
        try:
            return json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {}


def build_pitch(portal: str, title: str, description: str, game_url: str) -> tuple[str, str]:
    """Three genuinely different pitches, each keyed to that portal's real bar."""
    if portal == "poki":
        subject = f"Scouting note before full submission: {title} (small HTML5 title)"
        body = (
            f"Hi Poki team,\n\n"
            f"Our own review of Poki's public track record puts unknown-solo-developer "
            f"acceptance under 2% (roughly 300 titles/yr approved out of the full "
            f"submission pool), with review windows of 2-8 weeks and a bar that skews "
            f"toward exclusive, highly-polished releases rather than iterative reskins "
            f"(source: areas/quorum_research research on Poki + Dutch Game Awards "
            f"coverage of Poki crossing 1B monthly plays). Given that bar, this is a "
            f"scouting note, not a formal submission: '{title}' is a small, "
            f"dependency-free HTML5 title -- {description} -- live at {game_url}, part "
            f"of a broader portfolio at {PORTFOLIO_URL}. Before investing the polish "
            f"time an exclusivity-grade Poki release would need, I want to know if "
            f"this direction (lightweight, instant-play, no-account browser games) is "
            f"even in your current acquisition interest, or if Poki's bar this cycle "
            f"is elsewhere entirely.\n\nThanks for a look either way,\nTommy / HFO"
        )
    elif portal == "crazygames":
        subject = f"Developer portal submission scouting: {title}"
        body = (
            f"Hi CrazyGames team,\n\n"
            f"CrazyGames' public developer docs describe roughly 12% acceptance "
            f"(~900 titles/yr), a 1-3 week review window, and a 60% ad rev-share / "
            f"70% net IAP share on NET-60 payout terms (docs.crazygames.com/payouts) -- "
            f"a materially more open bar than Poki's exclusivity model, but formal "
            f"submission requires CrazyGames SDK integration (ads + leaderboard hooks), "
            f"which this build does not yet have. '{title}' -- {description} -- is "
            f"live at {game_url} (part of the portfolio at {PORTFOLIO_URL}) with no "
            f"iframe-blocking headers, so it already drops cleanly into a portal frame "
            f"at any size. I'd like to confirm SDK integration is the main gap before "
            f"we build it out and file a real submission through the developer portal.\n\n"
            f"Thanks,\nTommy / HFO"
        )
    elif portal == "kongregate":
        subject = f"Community submission inquiry: {title}"
        body = (
            f"Hi Kongregate team,\n\n"
            f"Kongregate's developer program has historically run a more open "
            f"submission process than curated portals like Poki -- community rating "
            f"and play-count drive discoverability more than an editorial pre-filter "
            f"-- paired with an ad-revenue-share payout model and Kongregate's own "
            f"badges/achievements API and Kredits virtual-currency layer for player "
            f"engagement. '{title}' -- {description} -- is a small, single-page HTML5 "
            f"title live at {game_url}, part of a growing portfolio at "
            f"{PORTFOLIO_URL}. Given Kongregate's community-first discovery model, "
            f"I'd rather understand what earns early front-page/community visibility "
            f"(badges integration? specific category tags?) before a bulk submission "
            f"of the rest of the portfolio. NOTE: revshare percentages here are from "
            f"general public developer documentation and should be re-verified "
            f"against Kongregate's current published terms before this pitch is "
            f"actually sent.\n\nThanks,\nTommy / HFO"
        )
    else:
        raise ValueError(f"unknown portal {portal!r}")
    return subject, body


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--portal", required=True, choices=["poki", "crazygames", "kongregate"])
    ap.add_argument("--game-package", required=True)
    args = ap.parse_args()

    game_dir = Path(args.game_package)
    if not game_dir.is_absolute():
        game_dir = ROOT / game_dir
    if not game_dir.exists():
        print(f"game package dir not found: {game_dir}", file=sys.stderr)
        return 1

    slug = game_dir.name
    manifest = load_manifest(game_dir)
    title = manifest.get("title") or slug
    description = manifest.get("short_description") or manifest.get("long_description") or f"{title} HTML5 game"
    game_url = f"{PORTFOLIO_URL}/games/{slug}/"

    subject, body = build_pitch(args.portal, title, description, game_url)

    ts = datetime.now(timezone.utc)
    ts_str = ts.strftime("%Y-%m-%dT%H:%M:%SZ")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    draft_path = OUT_DIR / f"{args.portal}_{slug}_{ts.strftime('%Y%m%dT%H%M%SZ')}.md"
    draft_path.write_text(
        f"# {subject}\n\nPortal: {args.portal}\nGame: {title}\nGame URL: {game_url}\n"
        f"Portfolio: {PORTFOLIO_URL}\nStatus: STAGED, never sent\nGenerated: {ts_str}\n\n"
        f"---\n\n{body}\n",
        encoding="utf-8",
    )

    payload = {
        "portal": args.portal,
        "subject": subject,
        "body": body,
        "portfolio_url": game_url,
        "draft_path": rel(draft_path),
        "game": slug,
        "ts_utc": ts_str,
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
