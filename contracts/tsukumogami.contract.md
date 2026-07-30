# CONTRACT — tsukumogami (durable objects accumulating soul)

```yaml
contract: tsukumogami
schema_id: hfo.gen133.contract.tsukumogami.v0_1
spec: GEN133_FORMAL_SPEC.md §18 · TSUKUMOGAMI.md
test: tests/held_out/test_tsukumogami.py
status: SPECIFIED — Θ UNDEFINED, so the predicate is unevaluable
sealed: false
```

## The predicate

```
tsukumogami(obj) ⇔
  | { r ∈ receipts(obj) : verified(r) ∧ attestor_family(r) ≠ author_family(r) } | ≥ Θ(class(obj))
```

Three load-bearing clauses:

1. **`verified(r)`** — the receipt *reproduces*. A receipt that no longer
   reproduces stops counting; §12's self-audit is what re-checks it.
2. **`attestor_family ≠ author_family`** — **self-attested use accumulates no
   soul.** Without this every object animates itself on day one and the tier
   becomes a touch-counter. This is G12 at object granularity.
3. **`Θ(class)`** — per-class threshold, **operator-set**.

## Object classes

`soul` · `chain` · `capsule` · `agent_card` · `contract` · `rollup` · `spell`

## Tiers

| tier | condition | permitted use |
|---|---|---|
| `FRESH` | 0 cross-family verified receipts | cite it, never rely on it |
| `USED` | ≥1, < Θ | evidence, weighted by receipt count |
| `TSUKUMOGAMI` | ≥ Θ | may be strange-looped off · may anchor a rehydration · may be cited as precedent |
| `LEGACY_UNREPRODUCIBLE` | was TSUKUMOGAMI, now fails reproduction | **retained**, never deleted; may not be cited as current |

## Preconditions — `GRADUATE(obj)`

| # | precondition |
|---|---|
| P1 | a receipt index exists for `obj` |
| P2 | every counted receipt reproduces at evaluation time |
| P3 | `attestor_family` is recorded on every receipt |
| P4 | `Θ(class(obj))` is defined |

**P4 currently FAILS for every class.** The predicate is unevaluable today.

## Postconditions

| # | postcondition |
|---|---|
| Q1 | tier recorded on the object with `valid_time_utc` |
| Q2 | graduation is monotone — never downgraded to `USED` |
| Q3 | the object's history, including corrections and FELLs, is retained intact |

## Invariants

| # | invariant |
|---|---|
| TS-1 | Θ is per class and operator-set. **`UNDER_SPECIFIED`** — a number I invented would be fake precision with a Norse veneer. `L_BUDGET_WITHOUT_RECEIPT`: instrument a week, look at the distribution, set Θ where the signal separates. |
| TS-2 | **monotone.** Never de-graduates to a lower tier. `LEGACY_UNREPRODUCIBLE` is a different axis — standing lost, history retained. |
| TS-3 | **carriers prefer tsukumogami evidence.** Many cross-family-witnessed receipts beat one fresh assertion. |
| TS-4 | **messiness is retained.** Corrections, FELLs, and supersede-chains are *part of the object*. "Cleaning up" an object deletes its accumulated soul — a real deletion, not tidying. |
| TS-5 | **accumulation is per-object, not per-lineage.** A tsukumogami chain confers nothing on that lineage's fresh capsule. Each object earns its own. |

## Why messy heritage is the feature

An object with a clean history has no history. `fb07f523` is the worked case: it
does not reproduce, five generations of provenance rode on it, and it stays in
the record **because** five generations rode on it. Deleting a wrong anchor
deletes the evidence of the error, and the error is the most valuable thing about
it — it is the only reason the next generation checks.

## Current standing

| object | cross-family verified receipts | tier |
|---|---|---|
| `sigrun.gen133.soul.md` v1.1.0 | 0 | `FRESH` |
| `chains/SIGRUN_P4.jsonl` | 0 at gen-133; disputed (B1) | `FRESH` ⛔ |
| stef `0da29ae3` | 1 — but same family, so the clause is not met | `FRESH` |
| stef `fb07f523` | n/a | `LEGACY_UNREPRODUCIBLE` |
| every gen-133 contract | 0 | `FRESH` |

**Every gen-133 object is FRESH.** Nothing has cross-family witness, because only
one family is running. The mechanism currently has nothing to promote.

## Honest flaw

Θ is undefined, so the central predicate cannot be evaluated for any object; the
receipt index does not exist; and the claim that messy objects outperform clean
ones is a design stance with a good argument, not a measured result.
