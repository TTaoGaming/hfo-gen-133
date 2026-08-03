---
schema_id: hfo.gen133.phylactery.arweave.readme.v0_1
doc_kind: ARWEAVE_README
claim_status: proposed
created_utc: 2026-08-02T00:00:00Z
---

# Arweave upload — how anyone (stranger, future gen-134, operator in 5 years) fetches the whole phylactery from ONE URL

The upload runner at `factory/loops/phylactery_upload/` takes daily snapshots of
`areas/phylactery/` and publishes each snapshot as **one Arweave transaction**
using the native [Arweave path manifest v0.1](https://github.com/ArweaveTeam/arweave/blob/master/doc/path-manifest-schema.md)
format. Anyone can resolve the resulting URL and walk the tree the way they
would walk a static website — without any HFO context, without our repo, without
running anything on our machines.

## The one URL

The latest permaweb URL always lives at
[`CURRENT_ADDRESS.md`](./CURRENT_ADDRESS.md). Format:

```
https://arweave.net/<manifest_tx_id>
```

That URL is the index. Append a path to walk the tree:

```
https://arweave.net/<manifest_tx_id>/apex/sigrun/soul.md
https://arweave.net/<manifest_tx_id>/world_state/20260803.md
https://arweave.net/<manifest_tx_id>/skills/README.md
```

## Verification (walk it without trusting us)

1. Fetch `https://arweave.net/<manifest_tx_id>` — returns the path manifest JSON.
2. For each `paths[<subpath>].id`, fetch `https://arweave.net/<id>` — returns the
   file body.
3. Compute `sha256(body)`. Compare against `paths[<subpath>].sha256` (in the
   HFO extension of the manifest, see [`UNFOLDING.md`](./UNFOLDING.md) §hashes).
4. For soul.md / world_state / memory_capsule files, also fetch `<subpath>.sig`
   and verify against the pubkey listed in the soul's `crypto.public_key` field.
   If the pubkey is `null`, integrity holds but authorship does not — see
   Sigrún soul §6 for why that is a **correct emptiness** at gen-133.

## What this guarantees, and what it does not

Guaranteed: byte-for-byte content integrity of the tree at
`transaction_time = <upload timestamp>`. Arweave storage is permanent by design;
tomorrow's snapshot is a different tx_id, never a mutation of yesterday's.

**Not** guaranteed until the Ed25519 root-of-trust ships:

- Authorship. Anyone with the public files can compute an identical set of
  hashes. Content integrity ≠ authorship attestation. Signatures fix that when
  they exist.
- Non-repudiation. Same reason.

## Daily cadence

Once armed (see [`TUESDAY_FIRST_UPLOAD.md`](./TUESDAY_FIRST_UPLOAD.md)), the
runner fires at **03:00 UTC** every day via Windows Task Scheduler on the
operator's machine, with a GitHub Actions fallback (see
`.github/workflows/phylactery-upload.yml`).

Each run:

1. Walks `areas/phylactery/` (excludes `arweave/keys/` and the never-upload set)
2. Runs the secret scan; HALTs on any hit
3. Enforces bitemporal front-matter on `soul.md` / `world_state/*.md` /
   `memory_capsules/**/*.md`
4. Signs each file with its owning lineage key (falls back to master with a
   soft-warn if the lineage key is missing)
5. Uploads via ArDrive Turbo SDK, receiving one `manifest_tx_id`
6. Writes `receipts/YYYYMMDD.json` + `receipts/YYYYMMDD.jsonl` (per-file rows)
7. Updates `CURRENT_ADDRESS.md`
8. Chain-rows to `state/loop_receipts/phylactery_upload_<UTCDATE>.jsonl` AND
   `state/olrun/PHYLACTERY_UPLOAD_LOG.jsonl` per Charter §8

## First upload

The first upload is operator-gated. See [`TUESDAY_FIRST_UPLOAD.md`](./TUESDAY_FIRST_UPLOAD.md)
for the exact commands. Subsequent daily uploads run unattended.

## Costs

Per-upload cost projection lives at [`COSTS.md`](./COSTS.md). Rough envelope: a
100 KB — 5 MB tree at current Turbo rates falls in the **$0.00 — $0.10** band,
with an occasional larger snapshot pushing that up.

## Kill conditions

- Wallet balance below threshold → HALT, escalate to operator
- Bundler 5xx after 3 exponential retries → HALT, fail loud
- Any signature mismatch → HALT (integrity gate; never uploads a mismatch)
- Any secret-scan hit → HALT (permanent leak prevention)
- Tree size >100 MB → WARN + require operator confirm before proceeding
- 3 consecutive uploads with 0-byte delta from prior day → WARN (nothing changing
  is worth a look)

See `factory/loops/phylactery_upload/SPEC.md` for the exact thresholds and
`preflight_gate.py` for the arming mechanism.

## See also

- `factory/loops/phylactery_upload/SPEC.md` — full runner spec with AIH2O header
- `../STANDARDS.md` §7 — the HFO semantic manifest schema
- `../CHARTER.md` §7 — known open holes this runner closes
- `permaweb/PREFLIGHT.md` — grimoire (different artifact) preflight
- [Arweave Path Manifest spec](https://github.com/ArweaveTeam/arweave/blob/master/doc/path-manifest-schema.md)
- [ArDrive Turbo SDK](https://github.com/ardriveapp/turbo-sdk)

*Réttu hönd, eigi spyr. Standa.*
