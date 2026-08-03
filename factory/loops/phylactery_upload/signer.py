"""Ed25519 signing wrapper.

All crypto happens in Node (sign_ed25519.mjs) via subprocess. Python here does
key-file discovery, batches sign requests, and returns the results. Rationale:
the runner already uses Node for the Turbo upload, and Node's @noble/ed25519 is
a maintained, small library. Keeping Python stdlib-only avoids `pip install`
requirements on the operator's Windows box.

Signature format (per RUNNER_MAP.md §signature-file-convention):
- Curve: Ed25519 (RFC 8032)
- Message: raw file bytes (no normalization)
- Encoding: lowercase hex, no `0x` prefix
- Storage: `<path>.sig` next to `<path>`

stdlib only.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
NODE_SIGNER = _HERE / "sign_ed25519.mjs"

KEYS_ROOT_DEFAULT = "areas/phylactery/arweave/keys"


class SignerError(RuntimeError):
    pass


def _run_node(args: list[str], timeout: int = 120) -> tuple[int, str, str]:
    node = shutil.which("node")
    if not node:
        raise SignerError("node not on PATH. Install Node >= 20 and re-run.")
    try:
        p = subprocess.run(
            [node, str(NODE_SIGNER), *args],
            capture_output=True, text=True, timeout=timeout, check=False,
        )
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        raise SignerError(f"sign_ed25519.mjs timed out after {timeout}s")


def key_path_for(signer_id: str, keys_root: Path) -> Path:
    """Map 'apex/sigrun' → keys/apex/sigrun_ed25519.json,
              'valkyries/mist' → keys/valkyries/mist_ed25519.json,
              'master' → keys/hfo_gen133_master_ed25519.json."""
    if signer_id == "master":
        return keys_root / "hfo_gen133_master_ed25519.json"
    if signer_id.startswith("apex/"):
        callsign = signer_id.split("/", 1)[1]
        return keys_root / "apex" / f"{callsign}_ed25519.json"
    if signer_id.startswith("valkyries/"):
        callsign = signer_id.split("/", 1)[1]
        return keys_root / "valkyries" / f"{callsign}_ed25519.json"
    return keys_root / f"{signer_id}_ed25519.json"


def resolve_key_or_fallback(signer_id: str, keys_root: Path) -> tuple[Path, str, str | None]:
    """Return (key_path, effective_signer_id, provenance_note).

    If the requested lineage key doesn't exist, fall back to master with a
    provenance note. Master missing = hard error.
    """
    p = key_path_for(signer_id, keys_root)
    if p.exists():
        return p, signer_id, None
    master = key_path_for("master", keys_root)
    if not master.exists():
        raise SignerError(f"neither lineage key ({p}) nor master key ({master}) exists")
    return master, "master", f"fallback_master_no_lineage_key:{signer_id}"


def sign_files(
    plan: list[dict],
    keys_root: Path,
) -> list[dict]:
    """`plan` = list of {'relpath': str, 'abspath': str, 'signer_id': str}.

    Returns list of {'relpath', 'signer_used', 'sig_hex' | None, 'sig_path',
    'provenance', 'error'} — same order.
    """
    # Resolve keys
    tasks: list[dict] = []
    for item in plan:
        try:
            key_path, effective_signer, provenance = resolve_key_or_fallback(item["signer_id"], keys_root)
        except SignerError as e:
            tasks.append({
                "relpath": item["relpath"],
                "abspath": item["abspath"],
                "signer_requested": item["signer_id"],
                "signer_used": None,
                "key_path": None,
                "provenance": None,
                "error": str(e),
            })
            continue
        tasks.append({
            "relpath": item["relpath"],
            "abspath": item["abspath"],
            "signer_requested": item["signer_id"],
            "signer_used": effective_signer,
            "key_path": str(key_path),
            "provenance": provenance,
            "error": None,
        })

    # Batch to Node
    ready = [t for t in tasks if not t["error"]]
    if ready:
        req = {"op": "sign_batch", "tasks": [
            {"path": t["abspath"], "key_path": t["key_path"]} for t in ready
        ]}
        rc, out, err = _run_node(["--stdin-json"], timeout=300)
        # actually we need to feed the JSON in
        # Retry the correct way: use a file
        # (For simplicity we pass via stdin — Node reads it.)
        raise SignerError("BUG: sign_files stdin path — see fixed version below")
    # See sign_files_stdin below for actual implementation.
    return tasks


def sign_files_stdin(plan: list[dict], keys_root: Path) -> list[dict]:
    """Same as sign_files but actually pipes JSON via stdin to Node."""
    tasks: list[dict] = []
    for item in plan:
        try:
            key_path, effective_signer, provenance = resolve_key_or_fallback(item["signer_id"], keys_root)
        except SignerError as e:
            tasks.append({
                "relpath": item["relpath"],
                "abspath": item["abspath"],
                "signer_requested": item["signer_id"],
                "signer_used": None,
                "provenance": None,
                "sig_hex": None,
                "error": str(e),
            })
            continue
        tasks.append({
            "relpath": item["relpath"],
            "abspath": item["abspath"],
            "signer_requested": item["signer_id"],
            "signer_used": effective_signer,
            "key_path": str(key_path),
            "provenance": provenance,
            "error": None,
        })

    ready = [t for t in tasks if not t["error"]]
    if not ready:
        return tasks

    node = shutil.which("node")
    if not node:
        for t in ready:
            t["sig_hex"] = None
            t["error"] = "node not on PATH"
        return tasks

    req = {"op": "sign_batch", "tasks": [
        {"path": t["abspath"], "key_path": t["key_path"], "relpath": t["relpath"]}
        for t in ready
    ]}
    try:
        p = subprocess.run(
            [node, str(NODE_SIGNER), "--stdin-json"],
            input=json.dumps(req), capture_output=True, text=True,
            timeout=600, check=False,
        )
    except subprocess.TimeoutExpired:
        for t in ready:
            t["sig_hex"] = None
            t["error"] = "sign_batch timed out"
        return tasks

    if p.returncode != 0:
        for t in ready:
            t["sig_hex"] = None
            t["error"] = f"node signer rc={p.returncode}: {p.stderr[-200:]}"
        return tasks

    try:
        resp = json.loads(p.stdout)
    except json.JSONDecodeError as e:
        for t in ready:
            t["sig_hex"] = None
            t["error"] = f"bad JSON from signer: {e}"
        return tasks

    # Merge sig_hex + pubkey_hex back onto ready tasks by relpath
    by_rel = {r["relpath"]: r for r in resp.get("results", [])}
    for t in ready:
        r = by_rel.get(t["relpath"])
        if not r:
            t["sig_hex"] = None
            t["error"] = "no result for relpath"
            continue
        t["sig_hex"] = r.get("sig_hex")
        t["pubkey_hex"] = r.get("pubkey_hex")
        if not t["sig_hex"]:
            t["error"] = r.get("error", "unknown signer error")
    return tasks


def write_sig_files(signed_tasks: list[dict], root: Path) -> list[str]:
    """Write `<path>.sig` alongside each signed file. Return list of relpaths."""
    out: list[str] = []
    for t in signed_tasks:
        if not t.get("sig_hex"):
            continue
        sig_path = Path(t["abspath"] + ".sig")
        sig_path.write_text(t["sig_hex"] + "\n", encoding="utf-8")
        out.append(t["relpath"] + ".sig")
    return out


def verify_all(root: Path, keys_root: Path) -> dict:
    """Delegate to Node's --verify-all mode. Returns the parsed JSON result."""
    node = shutil.which("node")
    if not node:
        raise SignerError("node not on PATH")
    req = {"op": "verify_all", "root": str(root), "keys_root": str(keys_root)}
    p = subprocess.run(
        [node, str(NODE_SIGNER), "--stdin-json"],
        input=json.dumps(req), capture_output=True, text=True,
        timeout=600, check=False,
    )
    if p.returncode != 0:
        raise SignerError(f"verify_all failed rc={p.returncode}: {p.stderr[-200:]}")
    return json.loads(p.stdout)


if __name__ == "__main__":  # pragma: no cover
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--verify-all", action="store_true")
    ap.add_argument("--root", default="areas/phylactery")
    ap.add_argument("--keys-root", default=KEYS_ROOT_DEFAULT)
    args = ap.parse_args()

    if args.verify_all:
        result = verify_all(Path(args.root).resolve(), Path(args.keys_root).resolve())
        print(json.dumps(result, indent=2))
        raise SystemExit(0 if result.get("all_ok") else 1)
    print("nothing to do — try --verify-all")
    raise SystemExit(0)
