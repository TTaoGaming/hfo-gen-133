---
schema_id: hfo.gen133.permaweb.publication_model.v0_1
claim_status: proposed
valid_time_utc: 2026-07-30T05:37:26Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
---

# One address, daily immutable roots

The requirement has two distinct address layers:

1. **Evidence address:** each sanitized daily Gleipnir release is an immutable
   Arweave path-manifest transaction. Its transaction ID is permanent and is
   the exact evidence anchor for that release.
2. **Navigation address:** one optional ArNS name points to the latest immutable
   manifest transaction. It can be updated daily, so it is convenient but not
   itself immutable authority.

An Arweave transaction ID cannot both remain immutable and change to reveal a
new daily root. The stable one-address experience therefore requires an ArNS
pointer (or another explicitly mutable name) over a sequence of immutable
manifest transaction IDs. Every release record keeps both.

## Unfolding path-manifest contract

```json
{
  "manifest": "arweave/paths",
  "version": "0.2.0",
  "index": { "path": "index.html" },
  "paths": {
    "index.html": { "id": "<txid-of-reader-index>" },
    "capsule.json": { "id": "<txid-of-machine-capsule>" },
    "souls/4-4.soul.md": { "id": "<txid-of-sanitized-sigrun-seed>" },
    "receipts/publication.json": { "id": "<txid-of-publication-receipt>" }
  }
}
```

The public reader index may link to additional immutable heritage leaves by
address. It does not copy the private corpus.

## Conservative first-release allowlist

The first candidate stays below 100 KiB and contains only:

- a reader index;
- `capsule.json` with exact Git/blob/digest pointers and bitemporal fields;
- the inherited Sigrun `[4,4]` v0 seed, clearly marked unratified;
- the electronic-institution architecture candidate;
- a public publication receipt template.

It excludes:

- the operator's unfinished root `soul.md`;
- inferred or agent-invented spells;
- raw Slack, chain, database, or private world-state bodies;
- paths, contact data, personal records, credentials, keys, tokens, or secrets;
- anything whose rights or sanitization status is unknown.

## Gates

Before an immutable upload:

1. Bind exact bytes and record byte count and SHA-256.
2. Keep the aggregate release below 100 KiB; re-check current service terms.
3. Apply the sanitization and rights-review allowlist.
4. Run held-out verification against the exact staged bytes.
5. Obtain operator-typed publication authorization.
6. Upload; preserve the provider receipt and immutable transaction ID.
7. Read back exact bytes through two independently operated gateways.
8. Commit the readback receipt to Git and obtain ConsumerAck.
9. Only then update the optional ArNS pointer to the new immutable manifest.

## Current state

`HOLD_NOT_UPLOADED`. There is no Gen133 transaction ID, gateway readback,
ArNS registration, provider receipt, or ConsumerAck. The inherited
`w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M` object is a lineage lifeboat,
not the Gen133 Gleipnir release.

## Honest flaw

Official documentation currently describes Turbo uploads below 100 KiB as
free, but that is a service policy, not a permanence or future-price
guarantee. ArNS registration and updates also introduce a mutable control
plane, possible cost, and cache convergence delay.
