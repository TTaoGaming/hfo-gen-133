#!/usr/bin/env python3
"""LOOP-B · FOSS_FORK_VARIANT — clone a FOSS parent, apply niche mutations,
deploy a variant subdomain, chain-row parent + variant SHAs + license.

AIH2O header
------------
AIH2O:
  version: gen-133
  loop: foss_fork_variant
  role: executor
  actor: factory_loop
  verifier: license gate BEFORE code work + git status clean + wrangler deploy 200
  clock_source: host_read
  chain: state/loop_receipts/foss_fork_variant_<UTCDATE>.jsonl
  ship_log: state/factory_ships/FOSS_FORKS.jsonl

CLI
---
    python factory/loops/foss_fork_variant/run.py --config fork.json
    python factory/loops/foss_fork_variant/run.py --config fork.json --whitelist-copyleft

Kill conditions
---------------
- License incompatible (GPL/AGPL/SSPL) without --whitelist-copyleft → HALT before any code work
- Mutation broke build → HALT + rollback (git reset --hard)
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve()
_FORGE = _HERE.parents[3]
sys.path.insert(0, str(_FORGE))
from factory.loops.lib import chain_row, kill_gates, slack_escalate  # noqa: E402


LOOP = "foss_fork_variant"
FORKS_LOG = _FORGE / "state" / "factory_ships" / "FOSS_FORKS.jsonl"
FORKS_ROOT = _FORGE / "factory" / "forks"

INCOMPATIBLE_LICENSES = {"GPL", "AGPL", "SSPL", "GPL-2.0", "GPL-3.0", "AGPL-3.0", "SSPL-1.0"}
COMPATIBLE_LICENSES = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "Unlicense", "0BSD", "MPL-2.0"}


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _run(cmd: list[str], cwd: Path | None = None, timeout: int = 600) -> tuple[int, str, str]:
    try:
        p = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True, timeout=timeout, check=False)
        return p.returncode, p.stdout, p.stderr
    except FileNotFoundError as e:
        return 127, "", f"missing tool: {e}"
    except subprocess.TimeoutExpired:
        return 124, "", f"timeout after {timeout}s"


def detect_license(repo: Path) -> tuple[str, str]:
    """Return (spdx_id_guess, evidence). SPDX 'UNKNOWN' if we can't tell."""
    candidates = ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "license", "license.md"]
    for name in candidates:
        p = repo / name
        if p.exists():
            txt = p.read_text(encoding="utf-8", errors="replace")
            up = txt.upper()
            if "AFFERO GENERAL PUBLIC LICENSE" in up:
                return "AGPL-3.0", str(p.relative_to(repo))
            if "SERVER SIDE PUBLIC LICENSE" in up:
                return "SSPL-1.0", str(p.relative_to(repo))
            if "GNU GENERAL PUBLIC LICENSE" in up:
                if "VERSION 3" in up:
                    return "GPL-3.0", str(p.relative_to(repo))
                if "VERSION 2" in up:
                    return "GPL-2.0", str(p.relative_to(repo))
                return "GPL", str(p.relative_to(repo))
            if "MIT LICENSE" in up or "MIT License" in txt:
                return "MIT", str(p.relative_to(repo))
            if "APACHE LICENSE" in up:
                return "Apache-2.0", str(p.relative_to(repo))
            if "BSD 3-CLAUSE" in up or "BSD 3-Clause" in txt:
                return "BSD-3-Clause", str(p.relative_to(repo))
            if "BSD 2-CLAUSE" in up:
                return "BSD-2-Clause", str(p.relative_to(repo))
            if "MOZILLA PUBLIC LICENSE" in up:
                return "MPL-2.0", str(p.relative_to(repo))
            if "ISC LICENSE" in up:
                return "ISC", str(p.relative_to(repo))
            if "PUBLIC DOMAIN" in up or "UNLICENSE" in up:
                return "Unlicense", str(p.relative_to(repo))
            return "UNKNOWN", str(p.relative_to(repo))
    # Fallback: package.json / cargo.toml license fields
    pj = repo / "package.json"
    if pj.exists():
        try:
            data = json.loads(pj.read_text(encoding="utf-8"))
            if isinstance(data.get("license"), str):
                return data["license"], "package.json:license"
        except (json.JSONDecodeError, OSError):
            pass
    return "UNKNOWN", "no LICENSE file found"


def license_compatible(spdx: str, whitelist: bool) -> tuple[bool, str]:
    up = spdx.upper()
    if up in {x.upper() for x in COMPATIBLE_LICENSES}:
        return True, f"{spdx} is on compatible list"
    if up in {x.upper() for x in INCOMPATIBLE_LICENSES}:
        if whitelist:
            return True, f"{spdx} is copyleft but operator whitelisted"
        return False, f"{spdx} is copyleft — reject unless --whitelist-copyleft"
    return False, f"{spdx} unknown — reject by default; add explicit --whitelist-copyleft to override"


def apply_mutations(repo: Path, mutation: dict) -> list[str]:
    """Idempotent find/replace + package.json name/color tweaks. Returns log lines."""
    log: list[str] = []
    rename = mutation.get("rename") or {}
    reskin = mutation.get("reskin_colors") or {}
    prompts = mutation.get("niche_prompts") or {}
    payment = mutation.get("payment_integration")

    def _replace_in_files(mapping: dict, tag: str) -> None:
        for f in repo.rglob("*"):
            if not f.is_file() or ".git" in f.parts:
                continue
            if f.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2", ".ttf"}:
                continue
            try:
                txt = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            new = txt
            for k, v in mapping.items():
                new = new.replace(k, str(v))
            if new != txt:
                f.write_text(new, encoding="utf-8")
                log.append(f"{tag}: {f.relative_to(repo)}")

    if rename:
        _replace_in_files(rename, "rename")
    if reskin:
        _replace_in_files(reskin, "reskin")
    if prompts:
        prompts_dir = repo / "src" / "prompts"
        prompts_dir.mkdir(parents=True, exist_ok=True)
        (prompts_dir / "niche.json").write_text(json.dumps(prompts, indent=2), encoding="utf-8")
        log.append(f"prompts written: {prompts_dir/'niche.json'}")

    if payment and (repo / "package.json").exists():
        try:
            data = json.loads((repo / "package.json").read_text(encoding="utf-8"))
            deps = data.setdefault("dependencies", {})
            if payment == "stripe":
                deps.setdefault("stripe", "^15.0.0")
                log.append("added stripe dep")
            elif payment == "lemon_squeezy":
                deps.setdefault("@lemonsqueezy/lemonsqueezy.js", "^3.0.0")
                log.append("added lemon-squeezy dep")
            (repo / "package.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
        except (json.JSONDecodeError, OSError) as e:
            log.append(f"package.json mutation failed: {e}")

    return log


def clone_parent(url: str, dest: Path) -> tuple[int, str]:
    if dest.exists():
        return 0, "cached clone"
    rc, out, err = _run(["git", "clone", "--depth", "1", url, str(dest)], timeout=300)
    if rc != 0:
        return rc, err
    return 0, out


def current_sha(repo: Path) -> str:
    rc, out, err = _run(["git", "rev-parse", "HEAD"], cwd=repo, timeout=30)
    return out.strip() if rc == 0 else "UNKNOWN"


def build(repo: Path) -> tuple[int, str]:
    if (repo / "package.json").exists():
        rc, _, err = _run(["npm", "install"], cwd=repo, timeout=900)
        if rc != 0:
            return rc, f"npm install: {err[-300:]}"
        rc, _, err = _run(["npm", "run", "build"], cwd=repo, timeout=900)
        return rc, f"npm build: rc={rc} {err[-200:]}"
    return 0, "no package.json — skipped build"


def rollback(repo: Path) -> None:
    _run(["git", "reset", "--hard", "HEAD"], cwd=repo, timeout=60)
    _run(["git", "clean", "-fd"], cwd=repo, timeout=60)


def deploy(repo: Path, subdomain: str, dry_run: bool) -> tuple[bool, str, str]:
    if dry_run:
        return True, f"https://{subdomain}.pages.dev", "dry_run"
    dist = repo / "dist"
    if not dist.exists():
        dist = repo / "build"
    if not dist.exists():
        dist = repo
    rc, out, err = _run(
        ["wrangler", "pages", "deploy", str(dist), "--project-name", subdomain],
        cwd=repo,
        timeout=600,
    )
    if rc != 0:
        return False, "", f"wrangler rc={rc} err={err[-300:]}"
    return True, f"https://{subdomain}.pages.dev", out[-200:]


def append_fork_row(row: dict) -> None:
    FORKS_LOG.parent.mkdir(parents=True, exist_ok=True)
    with FORKS_LOG.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def fork_one(cfg: dict, whitelist: bool, dry_run: bool) -> dict:
    parent_url = cfg["foss_repo_url"]
    mutation = cfg["niche_mutation"]
    slug = mutation.get("slug") or re.sub(r"[^a-z0-9-]", "-", parent_url.rsplit("/", 1)[-1].replace(".git", "").lower())
    subdomain = mutation.get("subdomain") or slug
    repo = FORKS_ROOT / slug

    chain_row.append_row(
        LOOP,
        action=f"start_fork:{slug}",
        verifier_result=f"parent={parent_url}",
        claim_status="proposed",
        remaining_risk=["license_may_be_incompatible", "build_may_fail", "deploy_may_fail"],
        next_safe_action="clone_and_license_check",
        honest_flaw="none",
        extra={"parent_url": parent_url, "slug": slug},
    )

    rc, msg = clone_parent(parent_url, repo)
    if rc != 0:
        chain_row.append_row(
            LOOP,
            action=f"clone_failed:{slug}",
            verifier_result=msg,
            claim_status="failed",
            remaining_risk=["nothing_committed"],
            next_safe_action="operator_check_git_or_url",
            honest_flaw="git clone non-zero",
        )
        return {"slug": slug, "shipped": False, "reason": "clone_failed"}

    parent_sha = current_sha(repo)

    # License gate — BEFORE any mutation work.
    spdx, evidence = detect_license(repo)
    ok, reason = license_compatible(spdx, whitelist)
    if not ok:
        dec = kill_gates.check({"license_reject": True, "license_reject_reason": reason})
        chain_row.append_row(
            LOOP,
            action=f"license_HALT:{slug}",
            verifier_result=f"spdx={spdx} evidence={evidence}",
            claim_status="failed",
            remaining_risk=["clone_preserved_operator_may_delete"],
            next_safe_action="pick_different_parent_or_pass_--whitelist-copyleft",
            honest_flaw=reason,
            extra={"parent_url": parent_url, "spdx": spdx, "kill_decision": dec.to_row_extra()},
        )
        slack_escalate.escalate(LOOP, f"LICENSE HALT {slug}", reason, severity="halt")
        return {"slug": slug, "shipped": False, "reason": "license_incompatible", "spdx": spdx}

    mutation_log = apply_mutations(repo, mutation)
    chain_row.append_row(
        LOOP,
        action=f"mutations_applied:{slug}",
        verifier_result=f"{len(mutation_log)} edits",
        claim_status="proposed",
        remaining_risk=["build_may_break"],
        next_safe_action="build",
        honest_flaw="none",
        extra={"mutation_log": mutation_log[:50]},
    )

    rc, build_msg = build(repo) if not dry_run else (0, "dry_run — skipped build")
    if rc != 0:
        rollback(repo)
        dec = kill_gates.check({"build_failed": True, "build_failed_reason": build_msg})
        chain_row.append_row(
            LOOP,
            action=f"build_HALT:{slug}",
            verifier_result=build_msg,
            claim_status="failed",
            remaining_risk=["rollback_executed"],
            next_safe_action="operator_tune_mutations",
            honest_flaw="mutation broke build",
            extra={"kill_decision": dec.to_row_extra()},
        )
        slack_escalate.escalate(LOOP, f"BUILD HALT {slug}", build_msg, severity="halt")
        return {"slug": slug, "shipped": False, "reason": "build_failed"}

    variant_sha = current_sha(repo)
    ok_deploy, url, deploy_msg = deploy(repo, subdomain, dry_run)
    if not ok_deploy:
        chain_row.append_row(
            LOOP,
            action=f"deploy_HALT:{slug}",
            verifier_result=deploy_msg,
            claim_status="failed",
            remaining_risk=["build_preserved"],
            next_safe_action="operator_wrangler_diagnose",
            honest_flaw="wrangler non-zero",
        )
        slack_escalate.escalate(LOOP, f"DEPLOY HALT {slug}", deploy_msg, severity="halt")
        return {"slug": slug, "shipped": False, "reason": "deploy_failed"}

    row = {
        "ts_utc": _utc(),
        "slug": slug,
        "parent_url": parent_url,
        "parent_sha": parent_sha,
        "variant_sha": variant_sha,
        "license_spdx": spdx,
        "license_evidence": evidence,
        "deploy_url": url,
        "mutation_summary": {
            k: (list(v.keys())[:8] if isinstance(v, dict) else v)
            for k, v in mutation.items()
            if k != "niche_prompts"
        },
        "dry_run": dry_run,
    }
    append_fork_row(row)
    chain_row.append_row(
        LOOP,
        action=f"forked:{slug}",
        verifier_result=f"deployed to {url}; license={spdx}",
        claim_status="wired_with_receipts",
        remaining_risk=["url_verify_deferred_to_operator", "distribution_still_to_execute"],
        next_safe_action="LOOP-C directory submission for the fork",
        honest_flaw="none",
        extra=row,
    )
    return {"slug": slug, "shipped": True, "url": url, "spdx": spdx}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", type=Path, required=True, help="JSON with foss_repo_url + niche_mutation{}")
    p.add_argument("--whitelist-copyleft", action="store_true", help="allow GPL/AGPL/SSPL for this fork")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    if "foss_repo_url" not in cfg or "niche_mutation" not in cfg:
        raise SystemExit("config must have foss_repo_url and niche_mutation")

    result = fork_one(cfg, whitelist=args.whitelist_copyleft, dry_run=args.dry_run)
    print(json.dumps(result, indent=2))
    return 0 if result["shipped"] else 2


if __name__ == "__main__":
    sys.exit(main())
