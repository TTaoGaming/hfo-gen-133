#!/usr/bin/env python3
"""ANALYTICS-POLL-COLLECTOR — worker E, EMERGENCY_FORGE 2026-08-03.

Polls one distribution source and appends one row to
state/experiments/<YYYY-MM-DD>/analytics.jsonl. Honesty over green: a source
with no configured API key reports status="staged_no_key" and names the exact
env var needed, rather than fabricating a metric to look "live".

Two sources get a genuinely live read without needing any new secret:
  - cloudflare: an unauthenticated GET of the operator's own
    https://hfo-games.pages.dev/ (explicitly in-envelope per the worker brief)
    records real reachability/latency/bytes. The Cloudflare *analytics API*
    itself still needs CLOUDFLARE_API_TOKEN, which is absent, so status stays
    staged_no_key and the `metrics` block for the analytics API is None -- the
    reachability read is reported in a separate honest field, not smuggled
    into `metrics` to force a "live" status.
  - github: this host already has an authenticated `gh` CLI session (verified
    `gh auth status` -> logged in as TTaoGaming) with no GITHUB_TOKEN env var
    needed. `gh api repos/<owner>/<repo>` is a read of the operator's own repo
    through his own already-authenticated session, so status="live" here is
    real, not fabricated.

itchio has no cached API key anywhere in this host's env -> staged_no_key.

Prints exactly one JSON payload line on stdout and exits 0.

clock_source=host_read.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
EXPERIMENTS = ROOT / "state" / "experiments"
PAGES_URL = "https://hfo-games.pages.dev/"
GH_REPO = "TTaoGaming/hfo-gen-133"

ENV_VAR_NEEDED = {
    "cloudflare": "CLOUDFLARE_API_TOKEN",
    "itchio": "ITCH_API_KEY",
    "github": "GITHUB_TOKEN",
    "crazygames": "CRAZYGAMES_API_KEY",
}


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def reachability_probe(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "hfo-analytics-poll/1"})
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            body = r.read()
            latency_ms = round((time.monotonic() - t0) * 1000, 1)
            return {
                "url": url,
                "http_status": r.status,
                "latency_ms": latency_ms,
                "bytes": len(body),
                "error": None,
            }
    except Exception as exc:  # noqa: BLE001 - report the real error, never fake success
        latency_ms = round((time.monotonic() - t0) * 1000, 1)
        return {
            "url": url,
            "http_status": None,
            "latency_ms": latency_ms,
            "bytes": None,
            "error": f"{type(exc).__name__}: {exc}",
        }


def poll_cloudflare() -> dict:
    token = os.environ.get("CLOUDFLARE_API_TOKEN")
    reach = reachability_probe(PAGES_URL)
    if not token:
        return {
            "status": "staged_no_key",
            "metrics": None,
            "reachability_probe": reach,
            "env_var_needed": ENV_VAR_NEEDED["cloudflare"],
            "note": "Cloudflare Pages Analytics API needs CLOUDFLARE_API_TOKEN; not set on "
                    "this host. reachability_probe above is a real unauthenticated GET of "
                    "the operator's own site, kept separate from `metrics` so status is not "
                    "fabricated to 'live'.",
        }
    # token present but this skill does not (yet) call the authenticated API -
    # honest partial rather than a fabricated metrics body.
    return {
        "status": "staged_no_key",
        "metrics": None,
        "reachability_probe": reach,
        "env_var_needed": ENV_VAR_NEEDED["cloudflare"],
        "note": "CLOUDFLARE_API_TOKEN is set but the authenticated analytics call is not "
                "wired up in this skill yet.",
    }


def poll_itchio() -> dict:
    key = os.environ.get("ITCH_API_KEY") or os.environ.get("ITCHIO_API_KEY") or os.environ.get("BUTLER_API_KEY")
    if not key:
        return {
            "status": "staged_no_key",
            "metrics": None,
            "env_var_needed": ENV_VAR_NEEDED["itchio"],
            "note": "No itch.io API key on this host. itch.io's traffic/analytics API "
                    "requires an authenticated key scoped to the account; staging honestly "
                    "rather than fabricating download/view counts.",
        }
    return {
        "status": "staged_no_key",
        "metrics": None,
        "env_var_needed": ENV_VAR_NEEDED["itchio"],
        "note": "Key present but the itch.io API call is not wired up in this skill yet.",
    }


def poll_github() -> dict:
    try:
        r = subprocess.run(
            ["gh", "api", f"repos/{GH_REPO}",
             "--jq", "{stargazers_count,forks_count,open_issues_count,watchers_count,pushed_at}"],
            capture_output=True, text=True, timeout=20,
        )
    except FileNotFoundError:
        return {
            "status": "staged_no_account",
            "metrics": None,
            "env_var_needed": ENV_VAR_NEEDED["github"],
            "note": "`gh` CLI is not on PATH on this host.",
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "status": "staged_no_key",
            "metrics": None,
            "env_var_needed": ENV_VAR_NEEDED["github"],
            "note": f"gh api call raised {type(exc).__name__}: {exc}",
        }
    if r.returncode != 0:
        return {
            "status": "staged_no_account",
            "metrics": None,
            "env_var_needed": ENV_VAR_NEEDED["github"],
            "note": f"gh api repos/{GH_REPO} exited {r.returncode}: "
                    f"{(r.stderr or '').strip()[:200]}",
        }
    try:
        metrics = json.loads(r.stdout.strip())
    except Exception as exc:  # noqa: BLE001
        return {
            "status": "staged_no_account",
            "metrics": None,
            "env_var_needed": ENV_VAR_NEEDED["github"],
            "note": f"gh api returned unparseable output: {exc}",
        }
    return {
        "status": "live",
        "metrics": metrics,
        "source_detail": f"gh api repos/{GH_REPO} via already-authenticated gh CLI session "
                          "(no GITHUB_TOKEN env var needed on this host)",
    }


def poll_crazygames() -> dict:
    key = os.environ.get("CRAZYGAMES_API_KEY")
    if not key:
        return {
            "status": "staged_no_account",
            "metrics": None,
            "env_var_needed": ENV_VAR_NEEDED["crazygames"],
            "note": "No CrazyGames developer account/API key configured on this host; "
                    "nothing has been submitted there yet either (see crazygames_submit.py "
                    "dry-run plans).",
        }
    return {
        "status": "staged_no_key",
        "metrics": None,
        "env_var_needed": ENV_VAR_NEEDED["crazygames"],
        "note": "Key present but the CrazyGames analytics call is not wired up in this skill yet.",
    }


POLLERS = {
    "cloudflare": poll_cloudflare,
    "itchio": poll_itchio,
    "github": poll_github,
    "crazygames": poll_crazygames,
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, choices=sorted(POLLERS))
    args = ap.parse_args()

    result = POLLERS[args.source]()
    ts = now_utc()
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    row = {
        "skill": "analytics_poll",
        "source": args.source,
        "ts_utc": ts,
        "clock_source": "host_read",
        **result,
    }

    log_dir = EXPERIMENTS / day
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "analytics.jsonl"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")

    payload = {
        "skill": "analytics_poll",
        "source": args.source,
        "ts_utc": ts,
        "clock_source": "host_read",
        "status": result["status"],
        "metrics": result["metrics"],
        "log_path": str(log_path.relative_to(ROOT)),
    }
    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
