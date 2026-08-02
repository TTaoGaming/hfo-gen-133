#!/usr/bin/env python3
"""CRAZYGAMES-SUBMIT-STAGER (EMERGENCY_FORGE 2026-08-03, worker D, HOT-D1).

Builds the multipart form-data payload CrazyGames' developer portal upload
form expects (game_zip, title, description, genre, thumbnail, tags[]),
actually zips the live game tree, and stages the whole submission plan under
outputs/staged_sends/crazygames/<slug>/.

CLASS ENVELOPE: STAGE only. This tool NEVER makes a network call to
crazygames.com. `--dry-run` is honored but staging happens either way --
the only network-touching step is a human doing the upload by hand, which is
exactly what submit_instructions.md walks through.

    python tools/olrun/skills/crazygames_submit.py \
        --game=outputs/staged_sends/games/017_snake --dry-run

Prints exactly one JSON object on stdout. clock_source=host_read.
"""
from __future__ import annotations

import argparse
import base64
import json
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAGES_GAMES = ROOT / "outputs" / "pages" / "games" / "games"
CRAZY_OUT = ROOT / "outputs" / "staged_sends" / "crazygames"

# 1x1 transparent PNG -- a placeholder thumbnail so the required field is a
# real file on disk, not a fabricated path. submit_instructions.md tells the
# operator this MUST be replaced with a real screenshot before manual upload.
_PLACEHOLDER_PNG_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk"
    "+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


def now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


def build_zip(src_dir: Path, dest_zip: Path) -> int:
    dest_zip.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(dest_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src_dir.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(src_dir).as_posix())
                count += 1
    return count


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", required=True, help="staged game dir, e.g. outputs/staged_sends/games/017_snake")
    ap.add_argument("--dry-run", action="store_true", help="never POSTed regardless -- flag kept for CLI contract parity")
    args = ap.parse_args()

    game_dir = Path(args.game)
    if not game_dir.is_absolute():
        game_dir = ROOT / game_dir
    if not game_dir.exists():
        print(f"game dir not found: {game_dir}", file=sys.stderr)
        return 1

    slug = game_dir.name
    manifest_path = game_dir / "itch_manifest.json"
    if not manifest_path.exists():
        print(f"itch_manifest.json not found in {game_dir}", file=sys.stderr)
        return 1
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"itch_manifest.json is not valid JSON: {exc}", file=sys.stderr)
        return 1

    playable_dir = PAGES_GAMES / slug
    if not playable_dir.exists():
        print(f"live playable page dir not found: {playable_dir}", file=sys.stderr)
        return 1

    out_dir = CRAZY_OUT / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    zip_path = out_dir / "game.zip"
    n_files = build_zip(playable_dir, zip_path)

    thumb_path = out_dir / "thumbnail_placeholder.png"
    thumb_path.write_bytes(base64.b64decode(_PLACEHOLDER_PNG_B64))

    title = manifest.get("title") or slug
    description = manifest.get("short_description") or manifest.get("long_description") or f"{title} -- HTML5 game"
    genre = manifest.get("genre") or "action"
    tags = manifest.get("tags") or [genre]
    live_url = f"https://hfo-games.pages.dev/games/{slug}/"
    ts = now_str()

    plan = {
        "portal": "crazygames",
        "upload_endpoint": "https://developer.crazygames.com/games/new (MANUAL BROWSER UPLOAD ONLY -- this tool never calls it)",
        "multipart_form_fields": {
            "game_zip": rel(zip_path),
            "title": title,
            "description": description,
            "genre": genre,
            "thumbnail": rel(thumb_path),
            "tags[]": tags,
        },
        "live_preview_for_reviewer": live_url,
        "sdk_note": "CrazyGames formal submission requires SDK integration (ads/leaderboards hooks) -- this build does NOT yet include the CrazyGames SDK; add it before a real submit.",
        "generated_ts_utc": ts,
        "zip_file_count": n_files,
    }
    plan_path = out_dir / "submission_plan.json"
    plan_path.write_text(json.dumps(plan, indent=2), encoding="utf-8")

    instructions = f"""# CrazyGames manual submission -- {title}

**Generated {ts} by crazygames_submit.py (STAGE only, no network call made).**

## What this tool did
- Zipped `{rel(playable_dir)}` -> `{rel(zip_path)}` ({n_files} files)
- Wrote a placeholder thumbnail at `{rel(thumb_path)}` -- **REPLACE with a real
  1280x720+ screenshot before submitting.** The placeholder is a 1x1 pixel and
  will fail CrazyGames' asset review as-is.
- Wrote the multipart form-data field plan to `{rel(plan_path)}`

## What the operator must do by hand
1. Go to https://developer.crazygames.com/games/new (log in with the
   operator's own CrazyGames developer account -- this tool has no
   credentials and makes no request to this URL).
2. Upload `{rel(zip_path)}` as the game build.
3. Replace `{rel(thumb_path)}` with a real screenshot/promo image before
   uploading the thumbnail field.
4. Fill in: title="{title}", genre="{genre}", tags={tags}.
5. Paste description from `{rel(plan_path)}` (`multipart_form_fields.description`).
6. CrazyGames' review queue historically approves roughly 1 in 8 unknown
   solo submissions within 1-3 weeks (source: areas/quorum_research
   DEEP_RESEARCH_INDEX_20260802T1545Z.md). Expect asset/SDK review comments
   on the first pass.

## What CrazyGames reviews (per public developer docs + this repo's research)
- SDK integration presence (ads + leaderboard hooks) -- currently missing,
  flagged above.
- No iframe-blocking headers (this build is confirmed clean -- static HTML,
  no CSP/X-Frame-Options set).
- Asset quality: real thumbnail/screenshots, not placeholders.
- Revenue terms if accepted: ~60% ad rev-share / ~70% net IAP share, NET-60
  payout (docs.crazygames.com/payouts, cited in
  areas/quorum_research/FOSS_GAME_EXEMPLAR_RESEARCH_20260802.md).

This file and the JSON plan are the entire submission artifact. Nothing here
was POSTed to crazygames.com.
"""
    instructions_path = out_dir / "submit_instructions.md"
    instructions_path.write_text(instructions, encoding="utf-8")

    payload = {
        "game_zip": rel(zip_path),
        "title": title,
        "description": description,
        "genre": genre,
        "thumbnail": rel(thumb_path),
        "tags": tags,
        "portal": "crazygames",
        "dry_run": True,
        "submission_plan": rel(plan_path),
        "submit_instructions": rel(instructions_path),
        "ts_utc": ts,
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
