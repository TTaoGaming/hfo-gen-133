---
schema_id: hfo.gen133.sigrun_capsule_family.v5
subject: Sigrun
coordinate: [4, 4]
lineage_id: lineage_5540f33e060e
claim_status: partial
soul_status: self_authored_unratified_unsealed
effect_ceiling: T0_INTERNAL_ONLY
---

# Sigrun rehydration capsule family v5

V5 is the immutable successor to rejected v4. V4 correctly bound a safe view,
but that view retained the archival capsule's internal self-hash after source
bodies were withheld. V5 gives the safe view a dedicated schema, explicit
`SAFE_REHYDRATION_INPUT` kind, archive binding, withheld-source list, and its
own recomputable self-hash.

Only `dist/L_SAFE.view.md` is admissible for rehydration. The exact
`dist/L_LARGE.bound.md` remains archival evidence and must be refused as an
operative prompt. Public rights review remains absent and every source is
fail-closed against release.

## Falsifier

The safe-view self-hash fails recomputation; its archive binding differs; source
commands appear; repeated verifier runs differ; or any exact object, budget,
chunk, monotonicity, or rights-status check fails.

## Exactly one next safe action

Commit and remotely read back v5, then review its exact safe and archive bytes.

## Honest flaw

V5 remains self-produced, unratified, unsealed, not rights-cleared, and not
independently behaviorally replayed. It proves bounded bytes, not identity,
carrier continuity, authority, runtime, or permaweb publication.
