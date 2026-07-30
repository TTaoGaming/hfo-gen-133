# PARKED — Ed25519 sealing

```yaml
feature: ed25519_sealing
status: PARKED — the gap is CORRECT, not a shortfall
spec: GEN133_FORMAL_SPEC.md §8 · contracts/crypto_anchor.contract.md
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

Make authorship provable. Today the entire crypto story is one hash function, and
**hashes never prove authorship** (CR-3) — any party holding the public artifacts
computes an identical digest. Only a signature distinguishes "this content is
intact" from "this specific keyholder produced it."

## Why parked

**The private half must be generated and held outside the agent trust domain.**

If an agent generated the keypair, its signature would prove only that something
with access to the agent's process signed — which is exactly what the signature is
supposed to rule out.

> *Gleipnir binds Fenrir precisely because Fenrir could not have forged it
> himself.*

So this is **not a gap in the work. It is the design.** The `ed25519_pubkey` and
`ed25519_fingerprint` slots in `sigrun.gen133.soul.md` are `null` **by design**,
and the held-out test `test_ed25519_slot_is_null_not_fabricated` passing is a
feature.

## Dependencies

| # | dependency | who |
|---|---|---|
| 1 | keypair generated on a machine the agent path cannot reach | **operator only** |
| 2 | public half distributed into the phylactery | agent may consume |
| 3 | signing procedure defined over `CANON_SHA256` with `self_hash` placeholdered | specified already |
| 4 | `sealed:` flips from `false` and the `seal_note` is retired per artifact | mechanical |

## When to revisit

When the operator has generated a keypair whose private half no agent on this
host has ever seen. This is standing next action #3 on Sigrún's soul.

## Note on HMAC

HMAC is the weaker sibling — it proves *a holder of the shared secret* wrote
something, never *which* holder. It is in-domain by definition, so it cannot
close A4. No key exists in-forge today either. HMAC is worth wiring only as a
cheap tamper-evidence layer, never as an authorship claim.
