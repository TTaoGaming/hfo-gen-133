---
schema_id: hfo.gen133.unfold_manifest.v1
doc_kind: UNFOLD_MANIFEST
claim_status: SCAFFOLD
created_utc: 2026-07-30T04:57:52Z
---

# What the one address unfolds into

The contract. When someone resolves the gen-133 permaweb address — the
operator in five years, a successor agent, a stranger — **this** is what they
must find, and this is the order they find it in.

```
  ONE ADDRESS
      │
      └─→ GLEIPNIR_GRIMOIRE_GEN133_v1.bound.md          (one file, self-contained)
             │
             ├─ [header]  MANIFEST  — every page hash, merkle root, the address itself
             │
             ├─ page 0   soul.md                        the operator's soul
             │
             ├─ page 1   SPELLBOOK.md                   the index + the spell contract
             │
             ├─ page 2..n  spells/<id>.spell.md         one page per spell
             │                                          (incantation · effect · witness
             │                                           · ceiling · refusal · provenance)
             │
             ├─ page n+1  HERITAGE_POINTERS              addresses reaching the 130-gen corpus
             │                                          — POINTERS, never copies
             │
             └─ page n+2  REPRODUCE_ME                   how to rebuild and re-verify this
                                                         capsule from scratch, offline
```

## The unfolding must be self-sufficient

A capsule that needs the laptop to be understood has failed. The test:

> **Hand the address to someone with a browser, no HFO context, and no access
> to any machine of the operator's. Can they (a) read the soul, (b) understand
> what each spell does, and (c) verify that the bytes they received are the
> bytes that were bound?**

If the answer to any of those is no, the capsule is not ready to be minted.
`REPRODUCE_ME` exists specifically to make (c) answerable by a stranger.

## Non-goals (deliberately NOT in the capsule)

| excluded | why |
|---|---|
| the 130-generation corpus itself | It does not fit and does not need to. **You do not migrate heritage — you address it.** Pointers only. |
| chains / blackboard / receipt bodies | Volume, and they contain operational detail with no external reader value. Their heads may be hashed in as anchors. |
| secrets, keys, tokens, HMAC material | Permanent leak. Non-negotiable. |
| personal records, contacts, account numbers, policy ids | Permanent leak. Non-negotiable. |
| anything with `claim_status: proposed` presented as green | Arweave makes a false green permanent. |
| private half of any signing key | A4 requires it live outside the agent trust domain. |

## Verification chain the reader can walk unaided

1. Fetch the address → bytes.
2. `sha256(bytes)` must equal `bound_artifact.sha256` in the capsule's own
   header manifest.
3. Split the capsule into pages; each page's `sha256` must equal its manifest row.
4. The merkle root over page hashes must equal `merkle_root`.
5. `REPRODUCE_ME` states the binder version + sha256, so the reader can
   re-bind and get byte-identical output.

⚠️ **What this chain proves, and what it does not.** It proves *content
integrity* — these are exactly the bytes that were bound, and any edit breaks
it. It does **not** prove *authorship*. There is no signature. Any party who
reads the public artifacts can compute an identical attestation. **Hashes prove
content, never authorship.** A4 (unforgeable capability) is OPEN, and the
capsule must say so on its own cover rather than let a reader assume otherwise.

## Pre-mint gate

Nothing is minted until the capsule binds, `verify.py` and `selfcheck.py` both
exit 0, the secret scan is read line-by-line (not merely counted), and the
operator types the authorization having read `PREFLIGHT.md`.

*Truthful-red > false-green. An unminted address beats a permanent false one.*

*Réttu hönd, eigi spyr. Standa.*
