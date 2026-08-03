---
schema_id: hfo.gen133.phylactery.arweave.keys_readme.v0_1
doc_kind: KEYS_README
created_utc: 2026-08-02T00:00:00Z
---

# keys/ — private-key store (git-ignored)

**Everything in this directory is `.gitignore`d.** Do not remove that line. Do
not commit any private key. See `../KEYS_HANDOFF.md` for the full operator
protocol.

## Expected files (populated by operator on Tuesday)

- `hfo_gen133_master.json` — Arweave wallet JWK
- `hfo_gen133_master_ed25519.json` — HFO root ed25519 keypair
- `apex/<callsign>_ed25519.json` — per-apex ed25519 (up to 8)
- `valkyries/<callsign>_ed25519.json` — per-valkyrie ed25519 (up to 16, only LIVE ones)

## Expected files (safe to see, published INSIDE the daily upload)

- `../PUBLIC_KEYS.md` — roster of public halves (this file is tracked by git)

## Recovery

If the wallet is lost, funds sent to it are lost. Back up the JWK to an
encrypted volume outside this repo. The runner will refuse to upload if the
JWK is missing; no data is at risk (the tree in git is the source of truth),
but the tree stops being anchored to Arweave until a new wallet is funded.

If the ed25519 master is lost, all subsequent signatures cannot chain to it.
The prior signatures on-chain remain valid. Generate a new master and record
the rotation in a chain row at `state/olrun/PHYLACTERY_UPLOAD_LOG.jsonl` with
`action: master_key_rotation`.

*Réttu hönd, eigi spyr. Standa.*
