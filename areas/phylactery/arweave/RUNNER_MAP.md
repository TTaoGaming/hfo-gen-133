---
schema_id: hfo.gen133.phylactery.arweave.runner_map.v0_1
doc_kind: RUNNER_MAP
claim_status: proposed
created_utc: 2026-08-02T00:00:00Z
---

# RUNNER_MAP — what the upload runner does to the tree

Operational companion to `../STANDARDS.md`. `STANDARDS.md` says what a valid
file looks like; this file says what the runner does with those files.

## Files the runner reads

The runner walks `areas/phylactery/` and picks up every file whose extension
matches:

```
.md .yaml .yml .json .txt .py .mjs .ps1 .jsonl .toml .rst .sig .pub
```

Extensions NOT in that list are skipped with a chain-row `skipped:extension`.
Binary blobs never get uploaded automatically — if you want one in the tree,
add its extension explicitly to `SPEC.md` §readable_extensions.

## Never-upload set

Hard-coded HALT patterns (in `secret_scan.py`):

```
**/.env             **/.env.*
**/*.key            **/*.pem
**/*_secret*        **/secrets/**
**/*.jwk            **/arweave-keyfile*.json
areas/phylactery/arweave/keys/**
areas/phylactery/arweave/AUTHORIZED_TO_UPLOAD.md   (see §arming)
```

A file matching ANY of those in the walk = HALT. No override flag.

## Body-scan regexes (also HALT)

```
BEGIN RSA PRIVATE KEY          BEGIN EC PRIVATE KEY
BEGIN OPENSSH PRIVATE KEY      BEGIN PRIVATE KEY
BEGIN PGP PRIVATE KEY
AWS_SECRET_ACCESS_KEY\s*=
SLACK_WEBHOOK_URL\s*=\s*https://hooks
xoxb-[A-Za-z0-9-]+
sk-[A-Za-z0-9]{20,}
ghp_[A-Za-z0-9]{20,}
```

False positives get added to `SCAN_ALLOWLIST.md` (path + one-line justification).

## Lineage → key ownership

The signer picks which private key signs which file based on path prefix:

| path pattern | signer |
|---|---|
| `apex/<callsign>/**` | `keys/apex/<callsign>_ed25519.json` |
| `valkyries/<callsign>/**` | `keys/valkyries/<callsign>_ed25519.json` |
| everything else | `keys/hfo_gen133_master_ed25519.json` |

Missing lineage key → fall back to master with `signature_provenance:
fallback_master_no_lineage_key` on the row. **Not a halt**; per Charter §7 open
holes, lineage keys are populated incrementally.

## Bitemporal enforcement

Enforced only on these three directories:

```
apex/**/soul.md
valkyries/**/soul.md
world_state/*.md
memory_capsules/**/*.md
```

Front-matter must have `valid_time_utc` and `transaction_time_utc`. Missing
either → chain row with `claim_status: partial`. Still uploads. Not a halt.

## Arming (first upload gate)

The runner reads `arweave/AUTHORIZED_TO_UPLOAD.md`. If missing or if front-matter
`sealed: false`, the runner exits `0` with a chain row `disarmed_no_upload`.

Once armed, no further per-run authorization is required. Disarm by deleting
the file OR flipping `sealed: false` in its front-matter.

## Two manifests per upload

1. **Arweave path manifest** (native `arweave/paths` v0.1.0) — root of the
   upload; makes `arweave.net/<tx>/apex/sigrun/soul.md` resolve. Content-type
   `application/x.arweave-manifest+json`.
2. **HFO semantic manifest** (JSON per `STANDARDS.md` §7) — human-readable
   role-slot → tx map, plus hashes + signatures. Written to
   `arweave/manifest.json` INSIDE the tree, so it becomes just another data
   item and is reachable at `arweave.net/<tx>/arweave/manifest.json`.

## Output paths

| what | where |
|---|---|
| per-file data-item tx_ids | `arweave/receipts/YYYYMMDD.jsonl` |
| daily upload summary | `arweave/receipts/YYYYMMDD.json` |
| latest permaweb URL | `arweave/CURRENT_ADDRESS.md` (front-matter + prose) |
| chain rows | `state/loop_receipts/phylactery_upload_YYYYMMDD.jsonl` |
| Olrún log | `state/olrun/PHYLACTERY_UPLOAD_LOG.jsonl` |
| reproduce info | `arweave/reproduce.md` (auto-generated) |

## Signature file convention

For every signed file `<path>`, the signature lives at `<path>.sig` in the same
directory. Format: raw ed25519 signature bytes, hex-encoded lowercase, no `0x`
prefix. Both `<path>` and `<path>.sig` are uploaded in the same daily bundle.

## What the runner never touches

- Any `.git/**` file (obvious)
- Anything under `keys/`
- `AUTHORIZED_TO_UPLOAD.md` itself (would be self-referential; the runner
  reads it but does not upload it)
- Files with modification time in the future (clock skew guard)

*Réttu hönd, eigi spyr. Standa.*
