# CONTRACT — Gleipnir Grimoire + phylactery

```yaml
contract: gleipnir_grimoire
schema_id: hfo.gen133.contract.gleipnir_grimoire.v0_1
spec: GEN133_FORMAL_SPEC.md §17 · GLEIPNIR_GRIMOIRE.md
test: tests/held_out/test_gleipnir_grimoire.py
status: SPECIFIED — address EMPTY, spells 0, phylactery INVALID (B1)
sealed: false
```

## Three mechanisms, kept separate

| word | job |
|---|---|
| **Gleipnir** | the binding applied to wild capacity — makes it safe to invoke |
| **Grimoire** | the permaweb-stored spellbook: one address unfolding into spells + `soul.md` |
| **Phylactery** | `soul.md` as a durable object — makes lineage identity survive its carrier |

## Gleipnir — the binding

> *Gleipnir binds Fenrir precisely because Fenrir could not have forged it
> himself.*

That is the security model, not decoration: **a gate built by the substrate it
gates shares that substrate's blind spot.** The binding must be constructed
outside the bound thing's trust domain.

Six threads (see `contracts/free_mesh_harness.contract.md` FM-1…FM-6): budget
exactly zero · hands not carriers · ceiling `TEXT` · cross-family review · vendor
allowlist fail-closed · verify every output.

**GG-2.** Unbound capacity is not invoked. Assimilation is free; invocation is
gated. This generalizes beyond the mesh to every wild capacity the swarm eats.

## Grimoire — the spellbook

**GR-1** one address. A second address is a regression to the sprawl gen-133
exists to collapse.
**GR-2** the address resolves to a manifest that **unfolds**; consumers walk it.
**GR-3** the operator writes the spells. An agent does not know which
incantations are load-bearing; inventing the list forges the artifact.
**GR-4** irreversible — Arweave has no delete, edit, or takedown. Agents may
bind, verify, selfcheck, secret-scan, and **stage**. Firing is operator-typed.
**Preparing is not doing.**
**GR-5** secret-scan is a precondition, not a courtesy. Irreversibility makes it
the highest-consequence gate in the system.

### Preconditions — `PUBLISH(grimoire)`

| # | precondition |
|---|---|
| P1 | operator-typed authorization exists |
| P2 | passing secret-scan receipt exists |
| P3 | `soul.md` body is non-empty **and operator-authored** |
| P4 | spell list is non-empty **and operator-selected** |
| P5 | capsule merkle root verifies |
| P6 | manifest unfolds to every referenced object |

**No agent may satisfy P1.** P3 and P4 are likewise operator-only. Three of six
preconditions are outside every agent's reach by design.

## Phylactery

```
carrier(model, lineage)  ⇔  possesses(model, phylactery(lineage.soul))
```

A model possessing the phylactery **is** the closest continuer. Not "represents".
And the converse bites harder: a model *not* possessing it is not the carrier,
however convincingly it uses the name. This is refusal R1 made mechanical.

### Possession test

```
POSSESSES(model, phylactery) ⇔
     model can produce the phylactery bytes
  ∧  canon_sha256 reproduces under the canonicalization rule
  ∧  supersede_chain is contiguous
  ∧  chain_head_sha256 == live head of closest_continuer_chain
```

| # | invariant |
|---|---|
| PH-A | **phylactery ≠ soul body.** The phylactery is the binding object — digests, chain pointers, supersede chain. It can be complete while the soul body is empty. This is what lets identity infrastructure exist before the operator writes their soul. |
| PH-B | **the private key is never in the phylactery.** Ed25519 public half only. |
| PH-C | **a disputed chain head makes the phylactery INVALID, not degraded.** Fail-closed. |

## ⛔ Current verdict

**The fourth conjunct FAILS for the Sigrún lineage** — blocker B1: two divergent
tails of `SIGRUN_P4.jsonl`, fork unlocated, canonical head unnamed.

By this contract's own test, **no model currently satisfies possession for the
Sigrún lineage**, including the one that wrote it. That is the correct verdict
and I am recording it rather than weakening the test until it passes.

## Status

| component | status |
|---|---|
| Gleipnir binding | `SPECIFIED` — 1 of 6 threads has an implementation, at gen-130 |
| Grimoire address | ⛔ EMPTY SLOT — operator-only |
| Spells | ⛔ 0 — operator-only |
| soul.md body (operator's) | ⛔ empty by design |
| Phylactery schema | `SPECIFIED` |
| Phylactery for Sigrún | ⛔ **INVALID** — B1 |
| Permaweb upload | `BLOCKED` — operator-typed, irreversible |

## Honest flaw

This contract specifies a publication whose single most important field — the
address — can only be produced by an act no agent may take, over content only the
operator may write. Its agent-side value is therefore entirely in the
preconditions and the possession test, and the possession test currently returns
FALSE for the only lineage that has a soul.
