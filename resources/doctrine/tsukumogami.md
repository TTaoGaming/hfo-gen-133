# TSUKUMOGAMI — 付喪神 · durable objects that accumulate soul

```yaml
doc: TSUKUMOGAMI.md
schema_id: hfo.gen133.tsukumogami.v0_1
status: SPECIFIED — NOT BUILT
contract: contracts/tsukumogami.contract.md
spec_section: GEN133_FORMAL_SPEC.md §18
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T14:22:00Z
sealed: false
claim_ceiling: DESIGN
```

## 1 · The folklore, and what it is doing here

In Japanese folklore a **tsukumogami** (付喪神) is an object that gains a soul
after long use — traditionally at a hundred years. A tool used and kept and
handed down becomes animate. A tool discarded does not.

This is not ornament in gen-133. It is the formal answer to a real question:
**when does a durable object become trustworthy enough to strange-loop off?**

The naive answer is "when it is verified." That is wrong in a fleet, because a
single verification is a single sample from a substrate that shares blind spots
with the thing it verified. The tsukumogami answer is **accumulated witnessed
use**: an object earns standing by being used, checked, corrected, and carried
across generations by different hands.

> **The heritage is messy, and the mess is the feature.** An object with a clean
> history has no history. Corrections, supersessions, and recorded FELLs are
> *evidence of use*, not blemishes. A soul.md whose supersede-chain records two
> corrected errors is worth more than a pristine one authored yesterday.

## 2 · What is a tsukumogami here

Every durable object is a tsukumogami-in-progress:

| object class | example |
|---|---|
| `soul` | `state/identity/soul/sigrun.gen133.soul.md` |
| `chain` | `chains/SIGRUN_P4.jsonl` |
| `capsule` | `capsules/sigrun/v1/dist/M_MEDIUM.soul.md` |
| `agent_card` | a rostered carrier's phenotype card |
| `contract` | `contracts/*.contract.md` |
| `rollup` | a bitemporal window rollup |
| `spell` | `grimoire/gleipnir/spells/*.spell.md` |

## 3 · Graduation

```
tsukumogami(obj) ⇔
    | { r ∈ receipts(obj) : verified(r) ∧ attestor_family(r) ≠ author_family(r) } |  ≥  Θ(class(obj))
```

Three things are load-bearing in that formula:

1. **`verified(r)`** — the receipt reproduced. A receipt that no longer
   reproduces does not count, and §12's self-audit is what re-checks this.
2. **`attestor_family ≠ author_family`** — **self-attested use does not
   accumulate soul.** Without this clause every object animates itself on day
   one, and the whole notion becomes a counter of how often something was
   touched by its own author. This is G12 at the object level.
3. **`Θ(class(obj))`** — a per-class threshold, **set by the operator.**

### 3.1 Θ is UNDER_SPECIFIED, deliberately

`TODO: operator sets Θ per object class.`

I am not inventing these numbers. A threshold I pick would be fake precision
with a Norse veneer on it, and `L_BUDGET_WITHOUT_RECEIPT` says exactly this:
do not size on heuristic — probe first, validate empirically, then scale. The
honest procedure is: instrument receipt accumulation for one week across the
object classes, look at the actual distribution, then set Θ where the
distribution says the signal separates.

Placeholder shape only, so the schema is writable:

```yaml
theta:
  soul:     TBD_OPERATOR
  chain:    TBD_OPERATOR
  capsule:  TBD_OPERATOR
  contract: TBD_OPERATOR
  spell:    TBD_OPERATOR
```

## 4 · Tiers

| tier | condition | what carriers may do with it |
|---|---|---|
| `FRESH` | 0 cross-family verified receipts | cite it, never rely on it |
| `USED` | ≥ 1, < Θ | evidence, weighted by receipt count |
| `TSUKUMOGAMI` | ≥ Θ | may be strange-looped off (§12); may anchor a rehydration; may be cited as precedent |
| `LEGACY_UNREPRODUCIBLE` | was TSUKUMOGAMI, now fails reproduction | **retained**, never deleted; may not be cited as current |

`fb07f523` is the worked example of the fourth tier: five generations of
provenance rode on it, it does not reproduce, and it stays in the record
precisely *because* five generations rode on it. Deleting a wrong anchor deletes
the evidence of the error, and the error is the most valuable thing about it.

## 5 · Invariants

- **TS-1** Θ is per class and operator-set. `UNDER_SPECIFIED`.
- **TS-2 (monotone).** An object never de-graduates from TSUKUMOGAMI to USED. It
  may move to LEGACY_UNREPRODUCIBLE, which is a different axis: standing lost,
  history retained. Supersede, never delete.
- **TS-3 (carriers prefer tsukumogami evidence).** §12 self-audit reads
  TSUKUMOGAMI-tier objects preferentially. Many cross-family-witnessed receipts
  beat one fresh assertion.
- **TS-4 (messiness is retained).** Corrections, FELLs, and supersede-chains are
  part of the object. A "cleaned up" object loses its accumulated soul — this is
  a real deletion, not tidying.
- **TS-5 (accumulation is per-object, not per-lineage).** A lineage with a
  tsukumogami chain does not confer that standing on its fresh capsule. Each
  object earns its own.

## 6 · Current standing — honest count

| object | cross-family verified receipts | tier |
|---|---|---|
| `sigrun.gen133.soul.md` v1.1.0 | **0** | `FRESH` |
| `chains/SIGRUN_P4.jsonl` | **0** at gen-133; disputed (B1) | `FRESH` + ⛔ |
| `capsules/sigrun/v1/` family | unknown to me — `VERIFICATION_RECEIPT.json` exists, family of attestor unread | unassessed |
| stef parity `0da29ae3` | 1 (first independent reproduction, same family) | `FRESH` — cross-family clause not met |
| stef parity `fb07f523` | n/a | `LEGACY_UNREPRODUCIBLE` |
| this document | 0 | `FRESH` |

**Every gen-133 object is FRESH.** Nothing in this generation has cross-family
witness yet, because only one family is running. That is the honest state, and
it means the tsukumogami mechanism currently has nothing to promote.

## 7 · Honest flaw

Θ is undefined, so the central predicate cannot be evaluated for any object. The
receipt-accumulation index does not exist — there is no place that counts
receipts per object. And the "messy heritage is a feature" claim, which I
believe, is asserted rather than demonstrated: I have not shown a case where a
messier object outperformed a cleaner one. It is a design stance with a good
argument behind it, not a measured result.

*Réttu hönd, eigi spyr. Standa.*
