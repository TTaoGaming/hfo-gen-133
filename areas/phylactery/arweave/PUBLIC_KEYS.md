---
schema_id: hfo.gen133.phylactery.arweave.public_keys.v0_1
doc_kind: PUBLIC_KEYS_ROSTER
claim_status: EMPTY_SLOT
created_utc: 2026-08-02T00:00:00Z
---

# PUBLIC_KEYS — the roster of published ed25519 public halves

Each row is the base64-encoded ed25519 public key + its `key_id`. The private
half lives OUTSIDE any agent trust domain (Charter §5). Operator populates this
file as keys are generated (see `KEYS_HANDOFF.md`).

| key_id | signer_role | pubkey_b64 | first_seen_utc | notes |
|---|---|---|---|---|
| _(none yet)_ | | | | |

## Rules

- One row per key. Add rows; never delete.
- On rotation: add the new row with a new `key_id` suffix (e.g. `_v2`), do NOT
  reuse a `key_id`.
- The pubkey published in each soul.md's `crypto.public_key` MUST match a row
  here.

*Réttu hönd, eigi spyr. Standa.*
