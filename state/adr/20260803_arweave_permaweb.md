---
schema_id: hfo.gen133.adr.v0_1
adr_id: 20260803_arweave_permaweb
title: One-Arweave-address-unfolds-phylactery upload pattern
status: PROPOSED
valid_time_utc: 2026-08-03T00:00:00Z
authored_by: PHYLACTERY_SCAFFOLDER lane · claude-opus-5 · operator mandate 2026-08-02
supersedes: partial · permaweb/UNFOLD_MANIFEST.md (for phylactery subset)
superseded_by: null
sealed: false
---

# ADR 20260803 · Arweave permaweb — one address unfolds the tree

## Context

Operator mandate 2026-08-02:

> "Goal: 1 Arweave address unfolds into the whole phylactery."

Prior contract at `permaweb/UNFOLD_MANIFEST.md` targeted the Gleipnir
grimoire as the unfold payload. This ADR extends that pattern to the
phylactery tree.

## Decision

Nightly:

1. **Bundle**: pack the whole `areas/phylactery/` tree into a set of Arweave
   transactions — one tx per soul.md, one tx per skill directory, one tx
   per tool catalog file, one tx per world_state snapshot, one tx per memory
   capsule.
2. **Manifest**: write `areas/phylactery/arweave/manifest.json` per the
   Arweave manifest v0.1 schema documented in `STANDARDS.md §7`.
3. **Upload manifest**: the manifest itself is uploaded as one final tx.
   That tx_id IS the "one address that unfolds the whole tree."
4. **Receipt**: write `areas/phylactery/arweave/receipts/YYYYMMDD.json`
   with the manifest_tx_id + per-soul tx_ids + timestamp + operator signature.

## Signing

- Every soul.md and the manifest itself are signed with the operator's
  Ed25519 private key, held OUTSIDE any agent trust domain.
- Until the key exists, all `signature:` and `signer_pubkey:` fields are
  `null`. This is a correct emptiness (per Sigrún soul §6 and STANDARDS §6),
  not a shortfall.
- The Arweave wallet signing the tx is also operator-held. Agents prepare
  the transaction bundle to the point where the operator's act is a single
  `arweave-cli upload manifest.json` invocation — preparing is not doing.

## Arweave manifest v0.1 shape

Per `STANDARDS.md §7`:

```json
{
  "manifest_version": "0.1",
  "generation": 133,
  "generated_utc": "<ISO 8601>",
  "signer_pubkey": "<ed25519 pub OR null>",
  "signature": "<ed25519 sig OR null>",
  "root": {
    "world_state": "ar://<tx>",
    "apex": {"sigrun": "ar://<tx>", ...},
    "valkyries": {"skogul": "ar://<tx>", ...},
    "skills": "ar://<tx>",
    "tools": "ar://<tx>",
    "memory_capsule": "ar://<tx>"
  }
}
```

## Rationale

- Arweave is irreversible. Every upload is a permanent, publicly-checkable
  anchor of who we said we were on a given day.
- One-address-unfolds means a cold reader with only the manifest tx_id can
  walk the whole tree without any HFO-specific tooling — Arweave gateways
  do the resolution.
- Nightly cadence means drift is caught within 24h across generations.

## Consequences

**Positive:**

- Identity drift becomes externally checkable
- Every lineage's soul is signed, dated, and immutable-once-uploaded
- A2A `.well-known/agent.json` can point at the Arweave tx directly

**Negative:**

- Costs real AR tokens (operator wallet)
- Requires an operator-held wallet; agents cannot upload
- A wrong upload is permanent — every dry-run must pass before the operator
  types the upload command

## Implementation plan

- `arweave/manifest.json` — v0 stub that documents the schema (this session)
- `arweave/upload.py` — STUB script that documents the intended interface
  (this session). Actual implementation is deferred to the operator-signed
  upload session.
- `arweave/receipts/` — created empty; first receipt lands on first real
  upload.

## Kill criteria

- Arweave protocol changes incompatibly → migrate to successor and mark
  gen-133 tx_ids as legacy
- Operator ratifies a different permaweb (IPFS with pinning service, etc.)
- Cost becomes prohibitive → drop to weekly cadence, then to milestone-only

## References

- `permaweb/UNFOLD_MANIFEST.md` — prior contract (Gleipnir grimoire)
- `permaweb/GEN133_PUBLICATION_MODEL.md` — publication doctrine
- `permaweb/GEN133_PERMAWEB_ADDRESS.md` — reserved gen-133 address
- `permaweb/staging/*` — pre-upload candidates from prior sessions
- `areas/phylactery/STANDARDS.md §7` — manifest schema
- `areas/phylactery/arweave/upload.py` — the STUB script
