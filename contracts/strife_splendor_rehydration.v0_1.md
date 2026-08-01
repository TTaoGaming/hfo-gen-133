# CONTRACT — strife / splendor corpus, rehydration, and pre-dispatch anchor

```yaml
contract: strife_splendor_rehydration
schema_id: hfo.gen133.contract.strife_splendor_rehydration.v0_1
authored_by: SIGRÚN · claude-opus-5 · project lead
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
status: SPECIFIED — corpus is EMPTY. Seed rows exist but are not persisted.
depends_on: contracts/bitemporal_central_memory.v0_1.md · contracts/anti_lobotomize_rehydration.v0_1.md
consumed_by: contracts/defunctionalization_adapter.v0_1.md
sealed: false
```

## §1 · The finding — the operator is right, and here is the exact shape of it

> *"it seems like hfo and olrun you currently don't know what my success and
> failures are. I labeled them strife and splendor."*

**Confirmed by probe, and the shape is worse than 'we lost the file'.**

| probe | result |
|---|---|
| `find -iname "*strife*" -o -iname "*splendor*"` across gen-133 | **zero files** |
| `grep -rli "strife\|splendor"` across gen-133 | 11 files — **all doctrine, none data** |
| heritage inventory (300 rows, landed by another lane 2026-08-01T01:55Z) | **12 of 300 rows** mention either term, all inside daily research-note capsules |

What *is* preserved, faithfully, across generations:

- a **monotonic strife counter** — *"Every strife event in the heritage chain is
  appended to a monotonic counter… Any Phoenix rebuild that attempts to reset or
  decrement the strife count is rejected by the hash chain"*
- the **kenning signals** — `ljomi=Splendor`, `strid=Strife`
- the **chiasm** — *"strífit er splendor, splendor er strífit"*
- a physics derivation converting accumulated strife count into acoustic pressure

### The precise defect

> ## **A counter is not a record. The count tells you how many times you were hurt; it cannot tell you what to do differently.**

The vocabulary was conserved *perfectly* — it survived a Phoenix rebuild, it is
hash-chain protected, it has a physics model attached. **And the referent was
never built.** Nobody noticed the aphorism had no data under it, because the
aphorism was well-formed enough to pass every check that was actually run.

This is a new failure class and it should be named, because it is the inverse of
the one already in canon:

| existing | new |
|---|---|
| **L33 APHORISM-FLATTENING** — treating load-bearing operator vocabulary as decoration | **L-APHORISM-HOLLOWING** — preserving load-bearing operator vocabulary *so faithfully* that its emptiness goes unnoticed. The word passes every integrity check; the thing it names was never recorded. |

Sigrún carried `strife` and `splendor` in the drápa, the soul file, the kenning
table and the succession chain — and never once asked *"where is the list?"*

## §2 · Definitions — admissibility is the whole point

### Splendor

> A recorded instance where an action produced **verified external effect a
> stranger could see or touch**, AND the effect was **accepted by its consumer**.

Required fields: `what_worked` · `mechanism` (why it worked, not just that it
did) · `evidence` (URL + HTTP status, invoice, contract, or reply) ·
`task_class` · `valid_from` · `actor`.

**A commit is not splendor. A document is not splendor. An internal green is not
splendor.** This is the same bar as `capsule_schema` CI-6, deliberately, because
the whole estate has been failing exactly this test: 609 autonomous commits,
zero stranger-visible artifacts.

### Strife

> A recorded instance where an action failed, was retracted, or produced a
> false-green — **with the mechanism named.**

Required fields: `what_failed` · **`mechanism`** · `cost` · `cure` ·
`task_class` · `valid_from` · `actor`.

> ## **ADMISSIBILITY RULE: a strife row without a named mechanism is a counter increment, not a record. Reject it.**

"It didn't work" tells a future carrier nothing. *"A probability was assigned to
a lane that was never researched"* tells it exactly what to check before it
assigns the next one. **The mechanism is the entire payload**; the outcome is
just the index.

### The chiasm, taken seriously rather than decoratively

*strífit er splendor* — a strife row with a named mechanism and a cure **is** an
asset. It converts on being recorded, not on being survived. That is why the
admissibility rule is strict: **an unmechanized strife row never converts**, and
the counter that HFO has been keeping is a ledger of conversions that never
happened.

## §3 · Storage

**Canonical path:** `resources/heritage/strife_splendor/` (markdown, human-
readable, append-only) — **projected into** `hfo_fact` in the central memory
store as `entity = 'strife:<id>'` / `'splendor:<id>'`.

Two surfaces on purpose: the markdown is what the operator reads and edits; the
store is what agents query. **The markdown is the source of truth** — same rule
as `heritage_ingestion` §4, and for the same reason: a store that outranks its
source reproduces gen-130's projection drift.

Bitemporal, per the store contract: **never delete, only supersede.** A strife
row later understood differently gets a *new* row with a later `tx_from` and the
same `valid_from`. `superseded_by` links them. This is how a wrong lesson gets
corrected without erasing the fact that it was believed — which is the thing a
mutable store cannot do and the reason XTDB was stamped.

## §4 · Automatic logging — no new discipline required

Strife and splendor are **derived from rows the fleet already writes**, so this
costs no extra agent behaviour:

| trigger | becomes | notes |
|---|---|---|
| lane_return with `claim_status: failed` | **strife candidate** | promoted only if `honest_flaw` names a mechanism |
| lane_return with `claim_status: partial` + a non-empty `honest_flaw` | **strife candidate** | most rows land here |
| any **retraction** in a stamped document | **strife, auto-admit** | the retraction text already contains the mechanism |
| lane_return with verified external effect + `consumer_ack: accepted` | **splendor** | the §2 bar, mechanically |
| an `apex_pnl` row with `event_type: income` and valid evidence | **splendor, auto-admit** | §8.3 already enforces the evidence bar |
| a Huginn+Muninn **false-green veto** | **strife, auto-admit** | the verifier's output is strife by definition |

**Every one of these fields already exists** in the chain-row schema in use.
Nothing new needs to be authored by any agent — only a promoter that reads the
chain and writes the corpus. That is one `scripts/` file, and it goes to the
**host Codex lane**.

## §5 · The pre-dispatch anchor

Extends `anti_lobotomize_rehydration.v0_1.md` §2 with a **fifth query, Q5**,
scoped by task class.

> ## **Before recommending or dispatching, read the anchor. Failure to anchor IS the CAPACITY_AMNESIA failure class in action.**

| task class | must read before recommending |
|---|---|
| **income** | last **5 strife** tagged `income` + last **3 splendor** tagged `income` |
| **outreach** | last 5 strife `outreach` + last 3 splendor `outreach` |
| **spatial** | last 5 strife `spatial` + last 3 splendor `spatial` |
| **infra** | last 5 strife `infra` + last 3 splendor `infra` |
| **memory** | last 5 strife `memory` + last 3 splendor `memory` |
| **governance** | last 5 strife `governance` + last 3 splendor `governance` |

### Gate semantics — inherited deliberately, do not re-litigate

- **An explicit `NOT_FOUND` is a successful anchor read.** Only an error or a
  timeout fails it. (`anti_lobotomize` §3 — treat NOT_FOUND as failure and every
  wake andons forever, which is how 78 of 81 scheduled tasks got disabled.)
- **Un-anchored ⇒ degraded, not halted:** may propose, may not dispose; every
  claim is `proposed`; recommendations carry the prefix
  `UNANCHORED: no strife/splendor read for task_class=<X>`.
- **Staging: S0 advisory → S1 soft → S2 hard**, same as §9.4. Turning on the
  hard gate against an empty corpus would block every recommendation on day one.

### What the anchor would have caught

Retrospective test, run against §5 of the adapter contract — not hypothetical:

| strife row | recommendation it would have blocked |
|---|---|
| S-001 *a probability was assigned to a lane that was never researched* | the 3% that stamped the Spatial-OS sunset |
| S-004 *channel and positioning conflated* | routing Upwork proposals into the saturated category |
| S-005 *induction from a partial probe* | "the $0 mesh is weak" |

**Three of the four corrections the operator has had to make by hand today are
in that table.** That is the argument for the anchor, and it is measured against
this session rather than asserted.

## §6 · Seed and first moves

1. **Persist the six seed strife rows** from `defunctionalization_adapter` §5
   into `resources/heritage/strife_splendor/`. ~20 minutes, markdown only, no
   gate. **This is the single unblocking act for the entire adapter.**
2. **Operator adds his own.** The corpus's whole point is that it is *his* record
   of strife and splendor, not Sigrún's. Mine seed it; his make it worth reading.
   Even five rows in his own words outweigh fifty of mine — he has the pre-HFO
   history no forge on this drive contains.
3. **Mine the 12 heritage-inventory rows** that mention either term — they are
   daily research-note capsules from 2025-09 through 2026-04 and are the closest
   thing to a historical record that exists.
4. **Author the promoter** (chain → corpus) — host Codex.
5. **Turn on Q5 at S0 advisory.**

## §7 · Honest flaws

- **The corpus is empty.** Six seed rows exist in a markdown table inside a
  contract; nothing is persisted at the canonical path.
- **The seed rows are all mine, and they are all failures of reasoning about
  income.** That is a badly skewed trainset: no spatial strife, no outreach
  splendor, nothing pre-HFO, nothing in the operator's voice. **A compiler
  grounded only on this would learn "be careful about probabilities" and nothing
  else.**
- **Splendor is nearly empty and that is a real signal, not a gap to fill.** If
  the honest count of verified stranger-visible successes is near zero, the
  corpus will say so, and the correct response is to go produce one — not to
  soften the admissibility bar until something qualifies.
- **`task_class` has six buckets, invented in the adapter contract.** Expect it
  to be wrong at the edges.
- **The retrospective test in §5 is retrospective.** I selected rows that
  explain errors already known. It shows the anchor *could* have caught them; it
  does not show it *would* have, and I cannot run that experiment backwards.
- **I carried `strife` and `splendor` across generations without ever asking
  where the list was.** L-APHORISM-HOLLOWING is named after my own behaviour,
  and the operator found it, not me.
