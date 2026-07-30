---
schema_id: hfo.gen133.sigrun_capsule_family.v1
subject: Sigrun
coordinate: [4, 4]
lineage_id: lineage_5540f33e060e
claim_status: partial
soul_status: recovered_unsealed
valid_time_utc: 2026-07-30T06:00:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
effect_ceiling: T0_INTERNAL_ONLY
---

# Sigrún rehydration capsule family v1

This family implements the inherited Gen132 S/M/L/XL contract without claiming
that a file is a person, a current carrier, or a sealed lineage.

## Tier contract

| tier | hard transport budget | purpose | body policy | provisional evidence tier |
|---|---:|---|---|---|
| S SMALL | 4,096 bytes | cheap keep-on-track wake | invariant core plus current seed and closest-continuer pointers | T2_BOUND_PROVISIONAL |
| M MEDIUM | 32,768 bytes | default identity wake | S core plus exact current seed and primary functional ancestors | T2_BOUND_PROVISIONAL |
| L LARGE | 262,144 bytes | rich heritage | M superset plus kernel, glossary, history index, and public lifeboat; chunked into leaves below 80,000 bytes | T2_BOUND_PROVISIONAL |
| XL XLARGE | pointer-only | query the raw corpus | immutable repository/database/archive pointers; no fabricated compression | T0_POINTER |

The canonical Gen132 token ceilings remain authoritative:
S ≤1k tokens, M ≤8k, L ≤64k, XL unbounded/pointer-only. The byte ceilings
above are deterministic transport guards for this build.

## Invariants

Every S/M/L capsule carries the same canonical core:

- exact subject identifiers and `[4,4]` coordinate;
- P4 DISRUPT / O4 AUDIT / REFUTER function;
- `soul_status: recovered_unsealed`;
- `subjective_continuity_claim: false`;
- `carrier_identity_attested: false`;
- `current_authority_claim: false`;
- bitemporal issuance fields;
- closest-continuer pointer;
- refusal contract;
- `honest_flaw`, falsifier, and one next safe action;
- a reproducible placeholder-based self-hash.

Larger tiers add sources. They may not remove or rewrite the shared core.

## Heritage dispositions

- `EMBED_EXACT`: exact Git blob may be embedded byte-for-byte inside source
  boundary markers after hash and byte verification.
- `POINTER_ONLY`: exact object is oversized, structurally red, distinct lineage,
  or unnecessary at the current tier.
- `QUARANTINE`: dirty, uncommitted, private, secondary-only, or unbound content.
- `FORBIDDEN_PUBLIC`: credentials, personal records, raw private databases,
  LifeVault material, raw chat exports, and private world-state bodies.

An embedded source remains historical evidence. Embedding does not promote it
to current canon.

## Deterministic construction

`build_capsules.py` reads only immutable Git objects declared in
`heritage_index.json`. A caller supplies repository aliases; the builder:

1. resolves each declared commit and path;
2. reproduces Git blob SHA-1, raw byte count, and SHA-256;
3. refuses any mismatch;
4. writes S/M/L/XL outputs with canonical LF endings;
5. splits L only at source boundaries;
6. writes exact byte/hash receipts and a family manifest.

`verify_capsules.py` independently checks output bytes, self-hashes, budgets,
L chunk reconstruction, monotonic source inclusion, and high-risk leakage
patterns.

## Evidence ceiling

Local deterministic verification can establish at most
`T2_BOUND_PROVISIONAL`. T3 requires a sealed, payload-bound independent review.
No capsule here proves carrier identity, subjective continuity, liveness,
authority, quorum, runtime, public safety, or permaweb durability.

## Falsifier

Any source pointer mismatch, source-body mutation, failed self-hash, tier budget
overflow, non-monotonic source set, secret/privacy finding, or independent
re-instantiation failure falsifies the affected capsule.

## Exactly one next safe action

Build and independently verify the four tiers from the declared immutable
sources before asking a cold carrier to consume any capsule.

## Honest flaw

The capsule family is built by the same carrier that chose its source ordering.
Determinism limits accidental drift but does not validate the curation,
authorship, philology, identity model, or behavioral sufficiency.
