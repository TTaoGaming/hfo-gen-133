#!/usr/bin/env python3
"""Headless cover-art + screenshot capture for the staged omega_games titles.

Unblocks the one thing standing between 21 finished games and a public itch.io /
CrazyGames listing: `cover_image_path: "MISSING_NEEDS_SCREENSHOT"` on every manifest
(GAMES_SHIP_20260802.md blocker #1). Playwright 1.58 + chromium 145 are already
installed on this host -- nothing is downloaded.

Each title is loaded from its LOCAL file:// build (self-contained single HTML, zero
network calls), given a moment to paint, nudged once with a click+arrow-key so the
frame captured is gameplay rather than a bare splash, then captured at two sizes:

    media/cover.png        630x500   itch.io cover art dimensions
    media/screenshot_1.png 1280x720  portal screenshot / CrazyGames thumbnail source

    python tools/games_screenshot.py                 # all titles
    python tools/games_screenshot.py --only 017_snake
    python tools/games_screenshot.py --write-manifests   # patch cover paths in place

clock_source=host_read.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDS = ROOT / "outputs" / "pages" / "games" / "games"
STAGED = ROOT / "outputs" / "staged_sends" / "games"

COVER = (630, 500)
SHOT = (1280, 720)


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def titles(only: str = "") -> list[Path]:
    dirs = sorted(d for d in BUILDS.iterdir() if d.is_dir() and (d / "index.html").exists())
    if only:
        want = {s.strip() for s in only.split(",")}
        dirs = [d for d in dirs if d.name in want]
    return dirs


def capture(page, build: Path, out_dir: Path, size: tuple[int, int], name: str) -> dict:
    page.set_viewport_size({"width": size[0], "height": size[1]})
    page.goto((build / "index.html").as_uri(), wait_until="load", timeout=20000)
    page.wait_for_timeout(900)
    # Nudge into gameplay: most titles hold on a splash until a PLAY/START button is
    # pressed, so a naive capture yields a menu screenshot that no portal editor wants.
    # Press the start control if there is one, then click the canvas and send a
    # direction key. All three are no-ops for titles that animate on load.
    started_via = "none"
    for sel in ("#startBtn", "#oBtn", "button:has-text('BEGIN')",
                "button:has-text('START')", "button:has-text('PLAY')"):
        try:
            btn = page.locator(sel).first
            if btn.count() and btn.is_visible():
                btn.click(timeout=1500)
                started_via = sel
                break
        except Exception:  # noqa: BLE001 - fall through to the generic nudge
            continue
    try:
        page.mouse.click(size[0] // 2, size[1] // 2)
        page.keyboard.press("ArrowRight")
    except Exception:  # noqa: BLE001 - a title that refuses input still gets captured
        pass
    page.wait_for_timeout(1400)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / name
    page.screenshot(path=str(path))
    return {"file": str(path.relative_to(ROOT)).replace("\\", "/"),
            "bytes": path.stat().st_size, "w": size[0], "h": size[1],
            "started_via": started_via}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--write-manifests", action="store_true",
                    help="patch cover_image_path / screenshots in each itch_manifest.json")
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright  # local import: optional dep

    dirs = titles(args.only)
    if not dirs:
        print("no titles found", file=sys.stderr)
        return 2

    results, errors = [], []
    started = now()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(device_scale_factor=1)
        page = ctx.new_page()
        console_errors: list[str] = []
        page.on("pageerror", lambda e: console_errors.append(str(e)[:160]))
        for build in dirs:
            slug = build.name
            out_dir = STAGED / slug / "media"
            try:
                console_errors.clear()
                cover = capture(page, build, out_dir, COVER, "cover.png")
                shot = capture(page, build, out_dir, SHOT, "screenshot_1.png")
                rec = {"slug": slug, "cover": cover, "screenshot": shot,
                       "page_errors": list(console_errors), "ts_utc": now()}
                results.append(rec)
                print(f"OK   {slug:<22} cover={cover['bytes']:>7}B  shot={shot['bytes']:>7}B"
                      + (f"  page_errors={len(console_errors)}" if console_errors else ""))
            except Exception as exc:  # noqa: BLE001
                errors.append({"slug": slug, "error": f"{type(exc).__name__}: {exc}"[:300]})
                print(f"FAIL {slug:<22} {type(exc).__name__}: {str(exc)[:120]}", file=sys.stderr)
        ctx.close()
        browser.close()

    patched = 0
    if args.write_manifests:
        for rec in results:
            mf = STAGED / rec["slug"] / "itch_manifest.json"
            if not mf.exists():
                continue
            data = json.loads(mf.read_text(encoding="utf-8"))
            data["cover_image_path"] = rec["cover"]["file"]
            data["screenshots"] = [rec["screenshot"]["file"]]
            data["cover_captured_utc"] = rec["ts_utc"]
            data["cover_capture_method"] = "playwright chromium headless, local file:// build"
            mf.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            patched += 1

    report = {"started_utc": started, "finished_utc": now(), "clock_source": "host_read",
              "captured": len(results), "failed": len(errors), "manifests_patched": patched,
              "results": results, "errors": errors}
    rp = STAGED / "SCREENSHOT_REPORT.json"
    rp.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"CAPTURED={len(results)} FAILED={len(errors)} MANIFESTS_PATCHED={patched}")
    print(f"WROTE {rp.relative_to(ROOT)}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
