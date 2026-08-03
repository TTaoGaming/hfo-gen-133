"""Arming gate.

`preflight_gate.py --arm` runs the preflight checklist (adapted from
permaweb/PREFLIGHT.md for the tree instead of the bound artifact) and writes
`areas/phylactery/arweave/AUTHORIZED_TO_UPLOAD.md`. The runner reads that file
on every invocation; missing OR `sealed: false` → the runner exits `0` with a
chain-row `disarmed_no_upload`.

Arming is a one-time operator action. Re-arm after any structural change to
the tree or key rotation.

stdlib only.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE = _HERE.parents[2]
sys.path.insert(0, str(_FORGE))

from factory.loops.phylactery_upload import bitemporal, manifest_builder, secret_scan  # noqa: E402


DEFAULT_TREE = "areas/phylactery"
DEFAULT_KEYS = "areas/phylactery/arweave/keys"
AUTH_FILE = "areas/phylactery/arweave/AUTHORIZED_TO_UPLOAD.md"
ALLOWLIST = "areas/phylactery/arweave/SCAN_ALLOWLIST.md"


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def check_wallet_present(keys_root: Path) -> tuple[bool, str]:
    wallet = keys_root / "hfo_gen133_master.json"
    if wallet.exists():
        return True, str(wallet)
    return False, f"missing: {wallet}"


def check_master_ed25519(keys_root: Path) -> tuple[bool, str]:
    ed = keys_root / "hfo_gen133_master_ed25519.json"
    if ed.exists():
        return True, str(ed)
    return False, f"missing: {ed}"


def check_wallet_balance(keys_root: Path) -> tuple[bool, str]:
    """Runs `node balance_check.mjs`. On failure returns (False, reason).
    Balance floor is enforced inside the runner too; this check is preflight-only."""
    node = shutil.which("node")
    if not node:
        return False, "node not on PATH"
    balance_script = _HERE / "balance_check.mjs"
    if not balance_script.exists():
        return False, f"missing: {balance_script}"
    wallet = keys_root / "hfo_gen133_master.json"
    if not wallet.exists():
        return False, f"missing wallet: {wallet}"
    try:
        p = subprocess.run(
            [node, str(balance_script), "--wallet", str(wallet), "--json"],
            capture_output=True, text=True, timeout=30, check=False,
        )
    except subprocess.TimeoutExpired:
        return False, "balance_check timed out"
    if p.returncode != 0:
        return False, f"balance_check rc={p.returncode}: {p.stderr[-200:]}"
    try:
        data = json.loads(p.stdout)
        if data.get("balance_credits", 0) < 0.01 and data.get("balance_ar", 0) < 0.001:
            return False, f"balance too low: {data}"
        return True, json.dumps(data)
    except json.JSONDecodeError:
        return False, f"balance_check bad JSON: {p.stdout[:200]}"


def run_checks(tree_root: Path, keys_root: Path, skip_balance: bool = False) -> list[dict]:
    """Return list of {'check', 'ok', 'detail'}."""
    checks: list[dict] = []

    # 1 — tree exists and non-empty
    if tree_root.exists() and any(tree_root.iterdir()):
        n = sum(1 for _ in tree_root.rglob("*") if _.is_file())
        checks.append({"check": "tree_exists_nonempty", "ok": True, "detail": f"{n} files"})
    else:
        checks.append({"check": "tree_exists_nonempty", "ok": False, "detail": f"{tree_root} empty or missing"})

    # 2 — wallet JWK present
    ok, detail = check_wallet_present(keys_root)
    checks.append({"check": "wallet_jwk_present", "ok": ok, "detail": detail})

    # 3 — master ed25519 present
    ok, detail = check_master_ed25519(keys_root)
    checks.append({"check": "master_ed25519_present", "ok": ok, "detail": detail})

    # 4 — secret scan clean
    scan = secret_scan.scan_tree(tree_root, allowlist_path=Path(ALLOWLIST).resolve() if Path(ALLOWLIST).exists() else None)
    if scan["halt"]:
        checks.append({
            "check": "secret_scan",
            "ok": False,
            "detail": f"HALT — path_hits={len(scan['path_hits'])} active_body_halts={len(scan['active_body_halts'])}",
        })
    else:
        checks.append({
            "check": "secret_scan",
            "ok": True,
            "detail": f"{scan['files_scanned']} files scanned, {len(scan['body_hits'])} body hits (all allowlisted)",
        })

    # 5 — bitemporal warnings enumerated (informational, does not fail arming)
    bt = bitemporal.check_tree(tree_root)
    partial = [r for r in bt if not r["ok"]]
    checks.append({
        "check": "bitemporal_frontmatter",
        "ok": True,  # partial is not a fail here
        "detail": f"{len(bt)} enforced files; {len(partial)} partial (see runner chain rows)",
    })

    # 6 — walkable + summarize
    rows = manifest_builder.walk(tree_root)
    summary = manifest_builder.summarize(rows)
    checks.append({"check": "walk_summary", "ok": True, "detail": json.dumps(summary)})

    # 7 — wallet balance (optional; slow, needs network)
    if not skip_balance:
        ok, detail = check_wallet_balance(keys_root)
        checks.append({"check": "wallet_balance", "ok": ok, "detail": detail})
    else:
        checks.append({"check": "wallet_balance", "ok": True, "detail": "skipped by --skip-balance"})

    return checks


def render_authorization(checks: list[dict], armed: bool) -> str:
    now = _utc()
    all_ok = all(c["ok"] for c in checks)
    sealed = "true" if (armed and all_ok) else "false"
    status = "AUTHORIZED" if sealed == "true" else "NOT_AUTHORIZED"
    lines: list[str] = [
        "---",
        "schema_id: hfo.gen133.phylactery.arweave.authorized_to_upload.v0_1",
        "doc_kind: AUTHORIZED_TO_UPLOAD",
        f"claim_status: {'wired_with_receipts' if sealed == 'true' else 'proposed'}",
        f"created_utc: {now}",
        f"sealed: {sealed}",
        f"status: {status}",
        "authorized_by: operator-typed-via-preflight_gate.py",
        "---",
        "",
        f"# {status} — {now}",
        "",
        "The runner reads this file on every invocation. `sealed: true` means",
        "the phylactery_upload runner may fire. Delete this file OR flip",
        "`sealed: false` in the front-matter to disarm without unregistering the",
        "scheduled task.",
        "",
        "## Preflight checks",
        "",
        "| check | ok | detail |",
        "|---|---|---|",
    ]
    for c in checks:
        ok_mark = "✔" if c["ok"] else "✘"
        detail = c["detail"].replace("|", "\\|")
        if len(detail) > 200:
            detail = detail[:200] + "…"
        lines.append(f"| {c['check']} | {ok_mark} | {detail} |")
    lines.append("")
    if not all_ok:
        lines.append("**Arming refused.** Fix the failing checks and re-run `preflight_gate.py --arm`.")
    else:
        lines.append("**All checks passed. Runner armed.**")
    lines.append("")
    lines.append("*Réttu hönd, eigi spyr. Standa.*")
    return "\n".join(lines) + "\n"


def is_armed(auth_file: Path) -> tuple[bool, str]:
    """Read AUTHORIZED_TO_UPLOAD.md; return (armed, reason)."""
    if not auth_file.exists():
        return False, f"missing: {auth_file}"
    text = auth_file.read_text(encoding="utf-8", errors="replace")
    # cheap YAML front-matter scan
    import re as _re
    m = _re.search(r"^sealed:\s*(true|false)\s*$", text, _re.MULTILINE)
    if not m:
        return False, "no `sealed:` key in front-matter"
    return (m.group(1) == "true"), f"sealed={m.group(1)}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--arm", action="store_true", help="run checklist and write AUTHORIZED_TO_UPLOAD.md")
    ap.add_argument("--disarm", action="store_true", help="remove the arming file")
    ap.add_argument("--status", action="store_true", help="report armed/disarmed")
    ap.add_argument("--tree", default=DEFAULT_TREE)
    ap.add_argument("--keys", default=DEFAULT_KEYS)
    ap.add_argument("--skip-balance", action="store_true", help="skip network wallet check")
    ap.add_argument("--force", action="store_true", help="write AUTHORIZED even if some checks fail")
    args = ap.parse_args(argv)

    tree_root = Path(args.tree).resolve()
    keys_root = Path(args.keys).resolve()
    auth_file = Path(AUTH_FILE).resolve()

    if args.status:
        armed, reason = is_armed(auth_file)
        print(json.dumps({"armed": armed, "reason": reason, "path": str(auth_file)}, indent=2))
        return 0

    if args.disarm:
        if auth_file.exists():
            auth_file.unlink()
            print(f"disarmed — removed {auth_file}")
        else:
            print(f"already disarmed — {auth_file} does not exist")
        return 0

    if not args.arm:
        ap.print_help()
        return 2

    checks = run_checks(tree_root, keys_root, skip_balance=args.skip_balance)
    all_ok = all(c["ok"] for c in checks)
    armed_now = args.force or all_ok
    content = render_authorization(checks, armed=armed_now)
    auth_file.parent.mkdir(parents=True, exist_ok=True)
    auth_file.write_text(content, encoding="utf-8")

    report = {
        "arm_attempted": True,
        "all_ok": all_ok,
        "sealed": armed_now,
        "auth_file": str(auth_file),
        "checks": checks,
    }
    print(json.dumps(report, indent=2))
    return 0 if all_ok else (0 if args.force else 3)


if __name__ == "__main__":
    sys.exit(main())
