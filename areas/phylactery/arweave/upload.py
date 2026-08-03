#!/usr/bin/env python3
"""
areas/phylactery/arweave/upload.py — STUB

Documents the intended interface for the nightly phylactery Arweave upload.
This file is NOT WIRED. It does not:
  - hold an Arweave wallet
  - hold an Ed25519 private key
  - actually upload anything

Both keys are operator-held, off any agent path (per STANDARDS §6 + ADR
20260803_arweave_permaweb.md).

Usage (target, once wired):
    python upload.py --dry-run           # bundle + manifest, no upload
    python upload.py --upload            # operator-signed real upload
    python upload.py --verify <tx_id>    # verify a prior upload's tree

Contract:
    - reads areas/phylactery/ tree
    - writes areas/phylactery/arweave/manifest.json (draft)
    - if --upload: expects OPERATOR_WALLET_PATH env var pointing at wallet JSON
    - if --upload: expects HFO_ED25519_PRIV env var pointing at private key
    - both env vars must be set outside any agent-visible session

Dependencies (not yet installed):
    - arweave-python-client (or equivalent)
    - cryptography (for Ed25519)
    - pyyaml (for reading soul.md frontmatter)

Chain-row every upload attempt (success or fail) to:
    state/olrun/PHYLACTERY_UPLOAD_LOG.jsonl

Author: PHYLACTERY_SCAFFOLDER lane · claude-opus-5 · operator mandate 2026-08-02
"""

import argparse
import json
import sys
from pathlib import Path


PHYLACTERY_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = PHYLACTERY_ROOT / "arweave" / "manifest.json"
RECEIPTS_DIR = PHYLACTERY_ROOT / "arweave" / "receipts"


def discover_souls() -> dict:
    """Walk apex/ and valkyries/ and return {callsign: soul_md_path} maps."""
    apex = {p.parent.name: str(p.relative_to(PHYLACTERY_ROOT))
            for p in (PHYLACTERY_ROOT / "apex").glob("*/soul.md")}
    valkyries = {p.parent.name: str(p.relative_to(PHYLACTERY_ROOT))
                 for p in (PHYLACTERY_ROOT / "valkyries").glob("*/soul.md")}
    return {"apex": apex, "valkyries": valkyries}


def build_manifest_stub() -> dict:
    """Rebuild manifest.json with discovered souls, all tx_ids null."""
    souls = discover_souls()
    manifest = {
        "manifest_version": "0.1",
        "generation": 133,
        "generated_utc": "PLACEHOLDER_ISO8601",
        "generated_by": "upload.py --dry-run STUB",
        "note": "STUB. Real upload not wired. See areas/phylactery/arweave/README.md",
        "signer_pubkey": None,
        "signature": None,
        "root": {
            "world_state": None,
            "apex": {name: None for name in sorted(souls["apex"])},
            "valkyries": {name: None for name in sorted(souls["valkyries"])},
            "skills": None,
            "tools": None,
            "memory_capsule": None,
        },
        "discovered_soul_paths": souls,
    }
    return manifest


def cmd_dry_run() -> int:
    manifest = build_manifest_stub()
    print(json.dumps(manifest, indent=2))
    return 0


def cmd_upload() -> int:
    print(
        "ERROR: upload not wired. See STANDARDS §6 (Ed25519) and ADR "
        "20260803_arweave_permaweb.md. Operator provides the wallet + key.",
        file=sys.stderr,
    )
    return 2


def cmd_verify(tx_id: str) -> int:
    print(
        f"ERROR: verify not wired. Target: fetch ar://{tx_id}, resolve manifest, "
        "walk each soul tx, verify Ed25519 sig against operator pubkey.",
        file=sys.stderr,
    )
    return 2


def main() -> int:
    ap = argparse.ArgumentParser(description="Phylactery Arweave upload (STUB)")
    ap.add_argument("--dry-run", action="store_true", help="print bundle, no upload")
    ap.add_argument("--upload", action="store_true", help="operator-signed upload")
    ap.add_argument("--verify", metavar="TX_ID", help="verify a prior upload")
    args = ap.parse_args()

    if args.dry_run:
        return cmd_dry_run()
    if args.upload:
        return cmd_upload()
    if args.verify:
        return cmd_verify(args.verify)
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
