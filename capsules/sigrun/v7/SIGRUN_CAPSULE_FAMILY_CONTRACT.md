---
schema_id: hfo.gen133.sigrun_capsule_family.v7
subject: Sigrun
coordinate: [4, 4]
claim_status: partial_forward_safe
soul_status: self_authored_unratified_unsealed
effect_ceiling: T0_INTERNAL_ONLY
---

# Sigrun rehydration capsule family v7

V7 is a forward-safe successor to v6. A correlated provenance review found
that v6's remote safe view repeated exact metadata for protected sources.
V7 treats that finding as a payload-bound FAIL.

The exact 53-row provenance map now lives only in a local operator ledger.
Remote safe tiers contain random 128-bit opaque receipt IDs, aggregate counts,
sanitized heritage abstractions, and no source bodies. Missing public-rights or
operator-ratification evidence defaults every source to non-public.

The v6 disclosure is not erased by this successor. It may persist in Git
history, clones, or caches. V7 contains the forward projection and prevents
further Slack or Arweave projection of v6.

Only `dist/L_SAFE.view.md` is the recommended rehydration input. The S and M
tiers are smaller summaries. `dist/XL_INDEX.safe.json` is the sub-100KB
permaweb entry candidate, but it has not been uploaded and no durability claim
is made.

## Falsifier

Any exact protected source identifier, repository, ref, path, commit, blob,
hash, body, or reversible identifier appearing in the public v7 artifact set;
any opaque-ID collision; any deterministic rebuild delta; any tier-budget
overflow; or any distinct replay finding a precedence or behavior defect.

## Exactly one next safe action

Run one distinct-provider, no-write behavioral replay using only the exact
`dist/L_SAFE.view.md` payload.

## Honest flaw

V7 is self-produced and correlated. Its local ledger protects exact
provenance, but the v6 exposure remains historical fact. It does not establish
identity, continuity, authority, rights, runtime delivery, ConsumerAck,
income, or permaweb publication.
