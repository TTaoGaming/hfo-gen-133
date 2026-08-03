"""Ed25519 keygen — delegates to Node.

`keygen.py --master` generates the HFO root ed25519 keypair.
`keygen.py --lineage apex/sigrun` generates a per-lineage keypair.
`keygen.py --lineage valkyries/mist` same.

Writes to `areas/phylactery/arweave/keys/`, .gitignore'd. Prints the public
key so the operator can paste it into the corresponding soul.md's
`crypto.public_key` field and into `arweave/PUBLIC_KEYS.md`.

Charter §5: private half lives OUTSIDE any agent trust domain. This script
does generate the private half, so **run it on an operator-only machine.**

stdlib only (delegates crypto to Node).
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
KEYGEN_NODE = _HERE / "sign_ed25519.mjs"
KEYS_DEFAULT = Path("areas/phylactery/arweave/keys").resolve()


def _run_node_json(payload: dict, timeout: int = 30) -> dict:
    node = shutil.which("node")
    if not node:
        raise SystemExit("node not on PATH. Install Node >= 20 and re-run.")
    p = subprocess.run(
        [node, str(KEYGEN_NODE), "--stdin-json"],
        input=json.dumps(payload), capture_output=True, text=True,
        timeout=timeout, check=False,
    )
    if p.returncode != 0:
        raise SystemExit(f"keygen failed rc={p.returncode}: {p.stderr[-200:]}")
    return json.loads(p.stdout)


def key_path_for(signer_id: str, keys_root: Path) -> Path:
    if signer_id == "master":
        return keys_root / "hfo_gen133_master_ed25519.json"
    if signer_id.startswith("apex/"):
        callsign = signer_id.split("/", 1)[1]
        (keys_root / "apex").mkdir(parents=True, exist_ok=True)
        return keys_root / "apex" / f"{callsign}_ed25519.json"
    if signer_id.startswith("valkyries/"):
        callsign = signer_id.split("/", 1)[1]
        (keys_root / "valkyries").mkdir(parents=True, exist_ok=True)
        return keys_root / "valkyries" / f"{callsign}_ed25519.json"
    return keys_root / f"{signer_id}_ed25519.json"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--master", action="store_true", help="generate the HFO master ed25519 keypair")
    g.add_argument("--lineage", type=str, help="e.g. apex/sigrun, valkyries/mist")
    ap.add_argument("--keys-root", default=str(KEYS_DEFAULT))
    ap.add_argument("--force", action="store_true", help="overwrite existing key")
    args = ap.parse_args(argv)

    keys_root = Path(args.keys_root).resolve()
    signer_id = "master" if args.master else args.lineage
    if signer_id != "master" and "/" not in signer_id:
        print("--lineage must look like apex/<callsign> or valkyries/<callsign>", file=sys.stderr)
        return 2

    key_path = key_path_for(signer_id, keys_root)
    if key_path.exists() and not args.force:
        print(f"key already exists: {key_path}\nUse --force to overwrite (rotates the key — updates soul.md required).", file=sys.stderr)
        return 3
    key_path.parent.mkdir(parents=True, exist_ok=True)

    result = _run_node_json({"op": "keygen", "out_path": str(key_path)})
    if not result.get("ok"):
        print(f"keygen returned no-ok: {result}", file=sys.stderr)
        return 4

    print(json.dumps({
        "wrote": str(key_path),
        "signer_id": signer_id,
        "pubkey_hex": result.get("pubkey_hex"),
        "pubkey_b64": result.get("pubkey_b64"),
        "note": "PASTE pubkey_b64 into arweave/PUBLIC_KEYS.md and into the matching soul.md `crypto.public_key`.",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
