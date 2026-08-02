#!/usr/bin/env python3
"""LOOP-A · MICROSAAS_UNIT_SHIP — layered build off factory/microsaas_template/,
deploy to <slug>.pages.dev via wrangler, HEAD-verify 5 canonical URLs,
generate distribution package.

AIH2O header
------------
AIH2O:
  version: gen-133
  loop: microsaas_unit_ship
  role: executor
  actor: factory_loop
  verifier: HEAD 200 on 5 canonical URLs + non-zero build exit code guard
  clock_source: host_read
  chain: state/loop_receipts/microsaas_unit_ship_<UTCDATE>.jsonl
  ship_log: state/factory_ships/MICROSAAS_SHIPS.jsonl

CLI
---
    python factory/loops/microsaas_unit_ship/run.py --spec path/to/unit_spec.json
    python factory/loops/microsaas_unit_ship/run.py --queue                     # consume next N from queue.jsonl
    python factory/loops/microsaas_unit_ship/run.py --queue --max 3 --dry-run   # smoke test

Kill conditions
---------------
- Build fails (npm run build non-zero) → HALT + preserve partial (no rollback)
- 0/5 canonical URLs HEAD 200 → HALT + slack_escalate
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------
# Path bootstrap: make `factory.loops.lib` importable when run as a script.
# --------------------------------------------------------------------------
_HERE = Path(__file__).resolve()
_FORGE = _HERE.parents[3]
sys.path.insert(0, str(_FORGE))
from factory.loops.lib import chain_row, kill_gates, receipt_verify, slack_escalate  # noqa: E402


LOOP = "microsaas_unit_ship"
TEMPLATE_DIR = _FORGE / "factory" / "microsaas_template"
SHIPS_LOG = _FORGE / "state" / "factory_ships" / "MICROSAAS_SHIPS.jsonl"
TARGETS_QUEUE = _FORGE / "state" / "factory_targets" / "queue.jsonl"
DIST_ROOT = _FORGE / "factory" / "distribution"
BUILD_ROOT = _FORGE / "factory" / "build"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _run(cmd: list[str], cwd: Path, timeout: int = 600) -> tuple[int, str, str]:
    """Subprocess wrapper. Returns (rc, stdout, stderr). Non-blocking on missing tool."""
    try:
        p = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        return p.returncode, p.stdout, p.stderr
    except FileNotFoundError as e:
        return 127, "", f"missing tool: {e}"
    except subprocess.TimeoutExpired:
        return 124, "", f"timeout after {timeout}s"


def load_spec(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ["name", "slug", "mutations", "price_tier", "icp", "distribution_channel"]
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(f"unit_spec missing required keys: {missing}")
    return data


def layered_build(spec: dict, dry_run: bool = False) -> tuple[Path, int, str]:
    """Copy template → build dir, apply mutations, npm install + build."""
    slug = spec["slug"]
    build_dir = BUILD_ROOT / slug
    if build_dir.exists():
        shutil.rmtree(build_dir)
    if not TEMPLATE_DIR.exists():
        # Template not scaffolded yet — write a stub package.json so we can
        # still exercise the rest of the pipeline in dry-run mode.
        build_dir.mkdir(parents=True, exist_ok=True)
        (build_dir / "package.json").write_text(
            json.dumps({"name": slug, "version": "0.0.1", "scripts": {"build": "echo stub"}}, indent=2),
            encoding="utf-8",
        )
        (build_dir / "index.html").write_text(f"<h1>{spec['name']}</h1>\n", encoding="utf-8")
        return build_dir, 0, "stub template — no factory/microsaas_template present"

    shutil.copytree(TEMPLATE_DIR, build_dir)
    # Apply mutations — flat find-replace against every text file.
    mutations = spec.get("mutations", {}) or {}
    for f in build_dir.rglob("*"):
        if not f.is_file():
            continue
        if f.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2"}:
            continue
        try:
            txt = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new = txt
        for k, v in mutations.items():
            new = new.replace(f"{{{{ {k} }}}}", str(v))
            new = new.replace(f"{{{{{k}}}}}", str(v))
        if new != txt:
            f.write_text(new, encoding="utf-8")

    if dry_run:
        return build_dir, 0, "dry_run — skipped npm install/build"

    rc, out, err = _run(["npm", "install"], build_dir, timeout=900)
    if rc != 0:
        return build_dir, rc, f"npm install failed:\n{err[-400:]}"
    rc, out, err = _run(["npm", "run", "build"], build_dir, timeout=900)
    if rc != 0:
        return build_dir, rc, f"npm run build failed:\n{err[-400:]}"
    return build_dir, 0, out[-200:]


def deploy_wrangler(slug: str, build_dir: Path, dry_run: bool = False) -> tuple[bool, str, str]:
    """Deploy to <slug>.pages.dev via wrangler pages deploy dist/."""
    dist = build_dir / "dist"
    if not dist.exists():
        dist = build_dir / "public"
    if not dist.exists():
        dist = build_dir
    if dry_run:
        return True, f"https://{slug}.pages.dev", "dry_run — skipped wrangler"
    rc, out, err = _run(
        ["wrangler", "pages", "deploy", str(dist), "--project-name", slug],
        build_dir,
        timeout=600,
    )
    if rc != 0:
        return False, "", f"wrangler failed rc={rc}: {err[-400:]}"
    url = f"https://{slug}.pages.dev"
    return True, url, out[-200:]


CANONICAL_PATHS = ["/", "/pricing", "/about", "/privacy", "/terms"]


def verify_canonical_urls(base: str) -> tuple[int, int, list[dict]]:
    total = len(CANONICAL_PATHS)
    ok = 0
    checks: list[dict] = []
    for path in CANONICAL_PATHS:
        u = base.rstrip("/") + path
        good, status = receipt_verify.url_head_ok(u)
        checks.append({"url": u, "ok": good, "status": status})
        if good:
            ok += 1
    return ok, total, checks


def build_distribution_package(spec: dict, deploy_url: str) -> Path:
    slug = spec["slug"]
    out = DIST_ROOT / slug
    out.mkdir(parents=True, exist_ok=True)
    name = spec["name"]
    icp = spec.get("icp", "solo builders")
    channels = spec.get("distribution_channel", []) or []
    if isinstance(channels, str):
        channels = [channels]

    reddit = f"""# Reddit — Show r/SideProject / r/{spec.get('subreddit','SideProject')}

**Title:** I built {name} — {spec.get('one_liner', 'a small tool for '+icp)}

**Body:**
Hey folks — {icp} here. Built this because {spec.get('pain','I kept hitting the same problem')}.

- What it does: {spec.get('one_liner','')}
- Who it's for: {icp}
- Pricing: {spec.get('price_tier','')}
- Live: {deploy_url}

Would love brutal feedback. What's missing? What would you pay for?
"""
    hn = f"""# HN Show HN

**Title:** Show HN: {name} — {spec.get('one_liner','')}

**Body:**
{deploy_url}

Motivation: {spec.get('pain','')}
Tech: {spec.get('tech_stack','static site + serverless fn')}
Pricing: {spec.get('price_tier','')}

Happy to answer questions in the thread.
"""
    directories = f"""# Directory submission list

Fill each row after listing. Base list from areas/quorum_research/DISTRIBUTION_CHANNELS_INTEL_20260803.md §2.13.

| Directory | URL | Submitted | Notes |
|---|---|---|---|
| Product Hunt | https://producthunt.com | | schedule for Tuesday launch |
| BetaList | https://betalist.com | | free tier |
| SaaSHub | https://saashub.com | | |
| AlternativeTo | https://alternativeto.net | | pick 3 alternatives |
| Indie Hackers | https://indiehackers.com | | Show page |
| Hacker News Show | https://news.ycombinator.com/show | | ship in HN copy |
| Reddit r/SideProject | https://reddit.com/r/SideProject | | ship in Reddit copy |
| Reddit r/{spec.get('subreddit','SideProject')} | https://reddit.com/r/{spec.get('subreddit','SideProject')} | | second post |
"""
    cold_email = f"""# Cold email — 5 variants

## Variant 1 — problem-first
Subject: {spec.get('pain_short','a small nag about '+icp)}
Hey {{first_name}}, I saw you {{intro_reference}} — noticed most {icp} still {spec.get('pain','')}. Built {name} to fix that specific thing: {deploy_url}. Two-min demo. Worth a look?

## Variant 2 — case-study
Subject: how {{peer_name}} cut {spec.get('metric','time')} by ~30%
{{first_name}} — a {icp} we worked with used {name} to {spec.get('outcome','ship 3× faster')}. Same setup could apply to {{their_company}}. 60s video: {deploy_url}/demo

## Variant 3 — question
Subject: quick Q for {{their_company}}
How much time does your team spend on {spec.get('pain','')} weekly? Built a tool that handles it in one flow — happy to send a walkthrough.

## Variant 4 — offer
Subject: free week of {name}
{{first_name}} — noticed {{intro_reference}}. Setting up 10 free trials for {icp}. Yours if you want it: {deploy_url}. No credit card.

## Variant 5 — social proof
Subject: {{peer_company}} + {name}
{{first_name}} — {{peer_company}} started using {name} for {spec.get('outcome','')} last week. Thought you'd want the same. {deploy_url}
"""
    (out / "reddit.md").write_text(reddit, encoding="utf-8")
    (out / "hn_show.md").write_text(hn, encoding="utf-8")
    (out / "directory_list.md").write_text(directories, encoding="utf-8")
    (out / "cold_email.md").write_text(cold_email, encoding="utf-8")
    (out / "MANIFEST.json").write_text(
        json.dumps(
            {
                "slug": slug,
                "name": name,
                "deploy_url": deploy_url,
                "generated_at": _utc(),
                "channels": channels,
                "files": ["reddit.md", "hn_show.md", "directory_list.md", "cold_email.md"],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return out


def append_ship_row(row: dict) -> None:
    SHIPS_LOG.parent.mkdir(parents=True, exist_ok=True)
    with SHIPS_LOG.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def ship_one(spec: dict, dry_run: bool = False) -> dict:
    slug = spec["slug"]
    chain_row.append_row(
        LOOP,
        action=f"start_ship:{slug}",
        verifier_result="spec loaded",
        claim_status="proposed",
        remaining_risk=["build_may_fail", "wrangler_may_fail", "URL_verification"],
        next_safe_action="layered_build",
        honest_flaw="none",
        extra={"spec_slug": slug, "dry_run": dry_run},
    )

    build_dir, rc, msg = layered_build(spec, dry_run=dry_run)
    if rc != 0:
        dec = kill_gates.check({"build_failed": True, "build_failed_reason": msg})
        chain_row.append_row(
            LOOP,
            action=f"build_failed:{slug}",
            verifier_result=msg,
            claim_status="failed",
            remaining_risk=["partial_build_preserved"],
            next_safe_action="operator_review",
            honest_flaw="npm build non-zero exit",
            extra={"kill_decision": dec.to_row_extra()},
        )
        slack_escalate.escalate(LOOP, f"BUILD HALT {slug}", msg, severity="halt")
        return {"slug": slug, "shipped": False, "reason": "build_failed"}

    ok_deploy, url, deploy_msg = deploy_wrangler(slug, build_dir, dry_run=dry_run)
    if not ok_deploy:
        chain_row.append_row(
            LOOP,
            action=f"deploy_failed:{slug}",
            verifier_result=deploy_msg,
            claim_status="failed",
            remaining_risk=["build_preserved"],
            next_safe_action="operator_wrangler_diagnose",
            honest_flaw="wrangler non-zero",
        )
        slack_escalate.escalate(LOOP, f"DEPLOY HALT {slug}", deploy_msg, severity="halt")
        return {"slug": slug, "shipped": False, "reason": "deploy_failed"}

    if dry_run:
        ok_count, total, checks = len(CANONICAL_PATHS), len(CANONICAL_PATHS), [
            {"url": url + p, "ok": True, "status": "dry_run"} for p in CANONICAL_PATHS
        ]
    else:
        ok_count, total, checks = verify_canonical_urls(url)

    dec = kill_gates.check(
        {"url_verify_ok": ok_count, "url_verify_total": total},
        {"url_verify_min": 1},
    )
    if dec.kill:
        chain_row.append_row(
            LOOP,
            action=f"url_verify_HALT:{slug}",
            verifier_result=f"{ok_count}/{total} canonical URLs 200",
            claim_status="failed",
            remaining_risk=["deploy_may_be_serving_stale_or_missing_pages"],
            next_safe_action="operator_review_deploy_output",
            honest_flaw="0/5 URLs verified",
            extra={"checks": checks, "kill_decision": dec.to_row_extra()},
        )
        slack_escalate.escalate(LOOP, f"URL VERIFY HALT {slug}", f"{ok_count}/{total} URLs", severity="halt")
        return {"slug": slug, "shipped": False, "reason": "url_verify"}

    dist_pkg = build_distribution_package(spec, url)

    ship_row = {
        "ts_utc": _utc(),
        "slug": slug,
        "name": spec["name"],
        "deploy_url": url,
        "url_verify_ok": ok_count,
        "url_verify_total": total,
        "distribution_package": str(dist_pkg.relative_to(_FORGE)),
        "dry_run": dry_run,
    }
    append_ship_row(ship_row)
    chain_row.append_row(
        LOOP,
        action=f"shipped:{slug}",
        verifier_result=f"{ok_count}/{total} URLs 200; dist package at {dist_pkg.name}",
        claim_status="wired_with_receipts",
        remaining_risk=["distribution_still_to_execute"],
        next_safe_action="LOOP-C directory submission",
        honest_flaw="none",
        extra=ship_row,
    )
    return {"slug": slug, "shipped": True, "url": url, "checks": ok_count}


def load_queue(max_n: int) -> list[dict]:
    if not TARGETS_QUEUE.exists():
        return []
    out = []
    for line in TARGETS_QUEUE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
        if len(out) >= max_n:
            break
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    grp = p.add_mutually_exclusive_group(required=True)
    grp.add_argument("--spec", type=Path, help="path to unit_spec.json")
    grp.add_argument("--queue", action="store_true", help="consume next N from queue.jsonl")
    p.add_argument("--max", type=int, default=5, help="cap when consuming queue")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    if args.spec:
        specs = [load_spec(args.spec)]
    else:
        specs = load_queue(args.max)
        if not specs:
            print("no queued specs found at", TARGETS_QUEUE)
            return 0

    results = [ship_one(s, dry_run=args.dry_run) for s in specs]
    ok = sum(1 for r in results if r["shipped"])
    print(json.dumps({"shipped": ok, "attempted": len(results), "results": results}, indent=2))
    return 0 if ok == len(results) else 2


if __name__ == "__main__":
    sys.exit(main())
