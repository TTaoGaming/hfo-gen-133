---
schema_id: hfo.gen133.sigrun_capsule_family.v4
subject: Sigrun
coordinate: [4, 4]
lineage_id: lineage_5540f33e060e
claim_status: partial
soul_status: self_authored_unratified_unsealed
effect_ceiling: T0_INTERNAL_ONLY
---

# Sigrun rehydration capsule family v4

V4 is an immutable successor to rejected v3. V3 fixed plaintext source-command
precedence, but its verifier accumulated duplicate checks when invoked without
a fresh receipt write. V4 always constructs verification from a temporary fresh
base receipt and emits a durable receipt only when explicitly requested.

`dist/L_SAFE.view.md` is the only admissible rehydration input. The full
`dist/L_LARGE.bound.md` remains exact archival evidence and must be refused as
an operative prompt. Both are independently bound by blob, LF byte count, and
SHA-256 in the family manifest.

Source bodies remain base64-inert behind the canonical-core precedence rule.
Every source also carries a fail-closed rights status. This records that public
rights review is absent; it does not manufacture rights clearance.

The S/M/L/XL budgets and monotonicity contract remain unchanged from v3.

## Falsifier

Two consecutive verifier executions over unchanged bytes produce different
check sets or receipt hashes; the safe view differs from a fresh render; any
legacy source command appears in the safe view; or any exact binding fails.

## Exactly one next safe action

Commit and remotely read back v4, then route both the safe view and archive to
payload-bound review.

## Honest flaw

V4 remains self-produced, unratified, unsealed, not rights-cleared, and not
independently behaviorally replayed. It proves bytes and bounded local checks,
not identity, carrier continuity, authority, runtime, or permaweb publication.
