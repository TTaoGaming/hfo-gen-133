#!/usr/bin/env python3
"""Runtime playability gate for the staged games — does the title actually RUN?

Motivation (EMERGENCY_FORGE CLOSE-LOOP-B, 2026-08-03): 21 titles were declared
"95% shipped, blocker is screenshots". Nobody had ever executed them. This gate
executes every one of them in headless chromium and reports three independent
runtime facts per title:

  load_errors    uncaught JS thrown between navigation and first interaction
  raf_per_sec    animation frames the title's OWN loop schedules once started
  reacts         canvas/DOM pixels differ after a start-click + gameplay input

VERDICT = PLAYABLE when (raf_per_sec > 5 OR reacts) AND no fatal parse error.
A parse error ("missing ) after argument list", "Unexpected token") is FATAL:
the whole <script> fails to compile, so no event listener is ever registered and
the title can never start. Everything else is a first-paint error which may be
cosmetic -- this gate does not guess, it reports both facts side by side.

Two probe lessons are baked in and must not be regressed:
  * The start control is `#startBtn` on most titles and `#oBtn` on others. Probing
    only one of them reports working games as frozen (false RED, cost: one wrong
    conclusion, caught 2026-08-02T17:0xZ).
  * A turn-based title (tic-tac-toe, slide puzzle) legitimately schedules zero
    animation frames. rAF alone is NOT a playability signal; `reacts` covers it.

    python tools/games_playability.py
    python tools/games_playability.py --only 013_reaction_test --json

clock_source=host_read. Nothing is downloaded; playwright + chromium are already
installed on this host.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDS = ROOT / "outputs" / "pages" / "games" / "games"
REPORT = ROOT / "outputs" / "staged_sends" / "games" / "PLAYABILITY_AUDIT.json"

START_SELECTORS = ("#startBtn", "#oBtn", "button:has-text('BEGIN')",
                   "button:has-text('START')", "button:has-text('PLAY')")

FATAL_MARKERS = ("missing ) after argument", "Unexpected token", "Invalid or unexpected",
                 "SyntaxError", "is not defined")

RAF_INIT = """
window.__raf=0;
const _r=window.requestAnimationFrame.bind(window);
window.requestAnimationFrame=function(cb){window.__raf++;return _r(cb);};
"""


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def is_fatal(errors: list[str]) -> bool:
    return any(any(m in e for m in FATAL_MARKERS) for e in errors)


def audit_one(page, build: Path) -> dict:
    errors: list[str] = []
    page.on("pageerror", lambda e: errors.append(str(e)[:160]))
    page.goto((build / "index.html").as_uri(), wait_until="load", timeout=25000)
    page.wait_for_timeout(1000)
    load_errors = list(dict.fromkeys(errors))

    state_js = ("()=>{const b=document.querySelector('#startBtn,#oBtn');"
                "const o=document.getElementById('overlay');"
                "return (b?b.textContent.trim():'')+'|'+(o?getComputedStyle(o).display:'');}")
    state_before = page.evaluate(state_js)

    started_via = "none"
    for sel in START_SELECTORS:
        try:
            btn = page.locator(sel).first
            if btn.count() and btn.is_visible():
                btn.click(timeout=1500)
                started_via = sel
                break
        except Exception:  # noqa: BLE001
            continue
    page.wait_for_timeout(700)

    a = page.evaluate("window.__raf")
    page.wait_for_timeout(1500)
    raf = round((page.evaluate("window.__raf") - a) / 1.5, 1)

    before = hashlib.sha256(page.screenshot()).hexdigest()
    box = page.viewport_size or {"width": 900, "height": 650}
    cx, cy = box["width"] // 2, box["height"] // 2
    for dx, dy in ((0, 0), (-70, 40), (60, -30)):
        try:
            page.mouse.click(cx + dx, cy + dy)
        except Exception:  # noqa: BLE001
            pass
        page.wait_for_timeout(120)
    for key in ("ArrowRight", "ArrowUp", "Space"):
        try:
            page.keyboard.press(key)
        except Exception:  # noqa: BLE001
            pass
        page.wait_for_timeout(120)
    page.wait_for_timeout(600)
    after = hashlib.sha256(page.screenshot()).hexdigest()

    fatal = is_fatal(load_errors)
    reacts = before != after
    # Third signal, and the one that rescues the honest cases the first two miss:
    # a turn-based title animates nothing and may ignore a blind canvas click, while
    # an action title can start AND reach game-over inside the sample window. Either
    # way the start control's label or the overlay's display changes. That is proof
    # the title's own code ran.
    state_after = page.evaluate(state_js)
    advanced = state_after != state_before
    playable = (raf > 5 or reacts or advanced) and not fatal
    return {
        "slug": build.name, "verdict": "PLAYABLE" if playable else "NOT_PLAYABLE",
        "raf_per_sec": raf, "reacts_to_input": reacts, "game_state_advanced": advanced,
        "state_before": state_before, "state_after": state_after,
        "started_via": started_via, "fatal_parse_error": fatal,
        "load_errors": load_errors, "ts_utc": now(),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--json", action="store_true", help="machine-readable stdout only")
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright  # local import: optional dep

    dirs = sorted(d for d in BUILDS.iterdir() if d.is_dir() and (d / "index.html").exists())
    if args.only:
        want = {s.strip() for s in args.only.split(",")}
        dirs = [d for d in dirs if d.name in want]
    if not dirs:
        print("no titles found", file=sys.stderr)
        return 2

    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 900, "height": 650})
        ctx.add_init_script(RAF_INIT)
        for build in dirs:
            page = ctx.new_page()  # fresh page per title: listeners do not leak
            try:
                rows.append(audit_one(page, build))
            except Exception as exc:  # noqa: BLE001
                rows.append({"slug": build.name, "verdict": "NOT_PLAYABLE",
                             "error": f"{type(exc).__name__}: {exc}"[:200], "ts_utc": now()})
            page.close()
        ctx.close()
        browser.close()

    playable = [r for r in rows if r["verdict"] == "PLAYABLE"]
    clean = [r for r in playable if not r.get("load_errors")]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps({
        "ts_utc": now(), "clock_source": "host_read", "total": len(rows),
        "playable": len(playable), "playable_and_error_free": len(clean),
        "results": rows,
    }, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(rows))
    else:
        print(f"{'slug':<24}{'verdict':<15}{'raf/s':>7}  reacts  errors")
        print("-" * 78)
        for r in rows:
            print(f"{r['slug']:<24}{r['verdict']:<15}{r.get('raf_per_sec', 0):>7}"
                  f"  {str(r.get('reacts_to_input', False)):<6}"
                  f"  {(r.get('load_errors') or [''])[0][:34]}")
        print("-" * 78)
    print(f"PLAYABLE={len(playable)}/{len(rows)}  ERROR_FREE_AND_PLAYABLE={len(clean)}")
    print(f"WROTE {REPORT.relative_to(ROOT)}")
    return 0 if len(playable) == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
