#!/usr/bin/env python3
"""ITCH-BUTLER-STAGER — worker E, EMERGENCY_FORGE 2026-08-03.

Stages an `butler push` plan for one staged game directory. Never invokes
butler (it is not installed on this host — verified `command not found`
16:10Z, re-checked via shutil.which() at runtime and reported honestly as
`butler_present`). Writes:

    outputs/staged_sends/games/<game_dir_name>/itch_butler_plan.json   (per-run, always fresh)
    outputs/staged_sends/games/itch_publish_runbook.md                (all staged titles)

Prints exactly one JSON payload line on stdout and exits 0.

clock_source=host_read.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
STAGED_GAMES = ROOT / "outputs" / "staged_sends" / "games"
PAGES_GAMES = ROOT / "outputs" / "pages" / "games" / "games"
ITCH_OWNER = "ttaogaming"


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slug_for(game_dir: Path) -> str:
    """017_snake -> snake (strip leading NNN_ ordinal)."""
    name = game_dir.name
    parts = name.split("_", 1)
    if len(parts) == 2 and parts[0].isdigit():
        return parts[1].replace("_", "-")
    return name.replace("_", "-")


def load_manifest(game_dir: Path) -> dict:
    mpath = game_dir / "itch_manifest.json"
    if mpath.exists():
        try:
            return json.loads(mpath.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def build_dir_for(game_dir: Path) -> Path:
    """Resolve the actual playable HTML tree for this staged game."""
    candidate = PAGES_GAMES / game_dir.name
    if candidate.exists():
        return candidate
    # fall back: staged dir itself, if it happens to hold the html tree
    return game_dir


def install_instructions() -> list:
    return [
        "1. Download the itch.io butler CLI for this OS from https://itchio.itch.io/butler",
        "2. Unzip and put the `butler` binary on PATH (or reference it by full path below).",
        "3. Run: butler login   (opens a browser, stores an API key in the butler config dir)",
        "4. Verify: butler version",
        "5. Then the butler_command in this plan can be run as-is from the repo root.",
        "NOTE: this host does NOT have butler installed (verified `command not found`, "
        "16:10Z 2026-08-03) — this skill does not download or install it (unapproved "
        "external fetch); the operator installs it by hand using the steps above.",
    ]


def write_runbook(all_games: list) -> Path:
    runbook = STAGED_GAMES / "itch_publish_runbook.md"
    lines = [
        "# itch.io publish runbook — all staged titles",
        "",
        f"generated_utc: {now_utc()}  (clock_source=host_read)",
        "",
        "## 0. One-time setup",
        "",
        "```",
        "\n".join(install_instructions()),
        "```",
        "",
        "## 1. Known blocker",
        "",
        "itch.io project pages require at least one screenshot before they can go public "
        "(`visibility: draft` in every `itch_manifest.json` here is a symptom of this — "
        "`cover_image_path` is `MISSING_NEEDS_SCREENSHOT` for every title). Screenshots must "
        "be captured per title before `butler push` output can be flipped from draft to "
        "public on itch.io's side; butler itself will happily push the build either way.",
        "",
        "## 2. Per-title push commands",
        "",
    ]
    for g in all_games:
        m = load_manifest(g)
        slug = slug_for(g)
        bdir = build_dir_for(g)
        title = m.get("title", g.name)
        lines.append(f"### {title}  (`{g.name}`)")
        lines.append("")
        lines.append("```")
        lines.append(f"butler push --if-changed {bdir.as_posix()} {ITCH_OWNER}/{slug}:html5")
        lines.append("```")
        lines.append("")
    runbook.parent.mkdir(parents=True, exist_ok=True)
    runbook.write_text("\n".join(lines), encoding="utf-8")
    return runbook


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    game_dir = Path(args.game)
    if not game_dir.is_absolute():
        game_dir = ROOT / game_dir
    if not game_dir.exists():
        print(f"itch_butler: game dir not found: {game_dir}", file=sys.stderr)
        return 1

    manifest = load_manifest(game_dir)
    slug = slug_for(game_dir)
    build_dir = build_dir_for(game_dir)
    target = f"{ITCH_OWNER}/{slug}:html5"
    channel = "html5"
    butler_present = shutil.which("butler") is not None
    butler_command = f"butler push --if-changed {build_dir.as_posix()} {target}"

    plan_dir = STAGED_GAMES / game_dir.name
    plan_dir.mkdir(parents=True, exist_ok=True)
    plan_path = plan_dir / "itch_butler_plan.json"

    plan = {
        "skill": "itch_butler",
        "ts_utc": now_utc(),
        "clock_source": "host_read",
        "game_dir": str(game_dir),
        "title": manifest.get("title", game_dir.name),
        "slug": slug,
        "target": target,
        "channel": channel,
        "build_dir": str(build_dir),
        "butler_command": butler_command,
        "butler_present": butler_present,
        "dry_run": bool(args.dry_run),
        "install_instructions": install_instructions(),
        "known_blocker": "itch.io pages require >=1 screenshot before going public; "
                          "cover_image_path is MISSING_NEEDS_SCREENSHOT in every manifest.",
    }
    plan_path.write_text(json.dumps(plan, indent=2), encoding="utf-8")

    # 21-title runbook, regenerated every invocation so it stays current.
    all_games = sorted(
        [p for p in STAGED_GAMES.iterdir() if p.is_dir() and (p / "itch_manifest.json").exists()]
    )
    if game_dir not in all_games and (game_dir / "itch_manifest.json").exists():
        all_games.append(game_dir)
        all_games.sort()
    runbook_path = write_runbook(all_games)

    payload = {
        "skill": "itch_butler",
        "ts_utc": plan["ts_utc"],
        "game": str(game_dir),
        "title": plan["title"],
        "target": target,
        "channel": channel,
        "build_dir": str(build_dir),
        "butler_command": butler_command,
        "butler_present": butler_present,
        "plan_path": str(plan_path.relative_to(ROOT)),
        "runbook_path": str(runbook_path.relative_to(ROOT)),
        "titles_in_runbook": len(all_games),
        "dry_run": bool(args.dry_run),
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
