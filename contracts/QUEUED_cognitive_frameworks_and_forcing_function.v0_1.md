# QUEUED — §22 cognitive frameworks · §23 AIH2O header/footer · §24 forcing function

```yaml
schema_id: hfo.gen133.queued.frameworks_forcing_function.v0_1
valid_time_utc:       2026-07-31T20:45:00Z
transaction_time_utc: 2026-07-31T20:55:00Z
status: QUEUED BY OPERATOR INSTRUCTION — not the full build
claim_status: proposed
author: SIGRUN_P4 · claude-opus-5 · gen-133
scope: three corrections + one recommendation that are cheap NOW and prevent
       re-derivation next session. The four schemas and the validator are NOT built here.
why_short: operator wrote "queue §22-§24 for next iteration... they can wait ONE more session."
           A full build tonight would be documents 8-11 of the day against 0 external artifacts,
           which is drift detector D1 of the charter I wrote this morning.
```

## §22 — three citation corrections that must land BEFORE the schema is written

Each of these would otherwise be baked into a required schema field and silently corrupt
every row that carries it.

### C1 — Meadows leverage numbering is INVERTED in the operator's spec ⚠️ load-bearing

The addendum says: *"leverage_level field (1-12; higher = deeper structural change)."*

**Meadows' own numbering runs the other way.** In *Leverage Points: Places to Intervene
in a System* (Donella Meadows, 1999, Sustainability Institute), the list is presented in
**increasing order of effectiveness as the number DECREASES**:

```
12  constants, parameters, numbers (subsidies, taxes, standards)   ← SHALLOWEST
 …
 6  structure of information flows (who does and does not have access)
 …
 3  the goals of the system
 2  the mindset or paradigm out of which the system arises
 1  the power to transcend paradigms                                ← DEEPEST
```

**Consequence if uncorrected:** every recommendation tagged `leverage_level: 11` would
read as "deep structural change" when Meadows means "tweaking a number." The field would
invert its own meaning on every row, and because it is a bare integer, nothing would
detect it.

**Cure — do not renumber Meadows.** Keep canonical numbering and make the direction
explicit in the schema so it cannot be misread:

```jsonc
"leverage_meadows": { "point": 1-12, "direction": "lower_is_deeper", "label": "…" }
```

**Falsifier:** a sourced edition of Meadows that numbers 1 as shallowest. I have not
found one; the 1999 text and the widely-circulated version both count down to
*transcending paradigms* at 1.

### C2 — Deming's own cycle is PDSA, not PDCA

Deming late in life explicitly preferred **Plan-Do-Study-Act**, holding that *Check*
understated the analysis step — "check" implies inspection, "study" implies learning.
PDCA is the Japanese/Shewhart-derived transmission and is what most organizations use.

**Recommendation: keep the field name `pdca_step` (the operator's term, and the common
one) and enumerate `["plan","do","study","act"]`,** with `"check"` accepted as an alias
for `"study"`. **This is the cheap fix that preserves the operator's vocabulary while
keeping the semantics Deming actually wanted** — and it matters here because HFO's
recurring failure is exactly *checking* (did the row land?) instead of *studying* (did
the row change anything?).

### C3 — Cynefin's domain names have changed; "Simple" is stale

Snowden's framework renamed the first domain twice: **Simple → Obvious → Clear**. The
addendum uses "Simple." Also, **Disorder is not a fifth peer domain** — it is the state
of not knowing which domain you are in, and its only valid action is to establish which.

```jsonc
"domain_cynefin": { "enum": ["clear","complicated","complex","chaotic","disorder"] }
// clear:       sense → categorize → respond   (best practice)
// complicated: sense → analyze   → respond   (good practice, experts)
// complex:     probe → sense     → respond   (emergent — SAFE-TO-FAIL EXPERIMENTS)
// chaotic:     act   → sense     → respond   (novel — stabilize first)
// disorder:    no valid action except determining the actual domain
```

**Why this one is operationally load-bearing for HFO, not pedantry:** nearly all of this
fleet's work is **complex** (probe-sense-respond) and has been executed as **complicated**
(sense-analyze-respond) — long analysis producing a confident plan, where the domain calls
for a small safe-to-fail probe. `SIGRUN_GTM_PARETO_20260731.md`'s falsifier-per-lane
structure is correct Cynefin-complex practice. **Seven specification documents in one day
is complicated-domain behavior applied to a complex-domain problem.** Naming that field
honestly on each row is itself a forcing function.

### §22 framework → chain-row map (decision table, for next session to implement)

| lane state | framework | emit | key field |
|---|---|---|---|
| self-managing loop tick | **MAPE-K** (Kephart & Chess, *IEEE Computer*, 2003) | `mape_k_row` | `mape_k_step: monitor\|analyze\|plan\|execute\|knowledge` |
| iterated improvement | **PDSA/PDCA** | `pdca_cycle_row` | `pdca_step` (+ C2 alias) |
| new spec or product | **Double Diamond** (UK Design Council, 2005) | `discover\|define\|develop\|deliver_row` | `diamond_phase` |
| lane is STUCK | **Pólya**, *How to Solve It* (1945) | `polya_step_row` | `understand\|plan\|execute\|look_back` |
| any recommendation | **Meadows** (1999) | field on the row | `leverage_meadows` per C1 |
| any analysis | **Paul–Elder** (Foundation for Critical Thinking) | field on the row | `cognitive_mode_paul_elder` |
| **before choosing a method** | **Cynefin** (Snowden) | field on the row | `domain_cynefin` per C3 |

**Ordering claim:** Cynefin is evaluated **first**, because it selects which of the others
is even valid. Running PDCA on a chaotic-domain problem, or Double Diamond on a clear one,
is a category error that the other six frameworks cannot detect.

## §23 — AIH2O header/footer: the one design decision worth making now

**The footer's job is not symmetry with the header. It is the handoff.**

The header answers *who am I and what may I do.* The footer must answer *what does the
next carrier need that they cannot re-derive.* Three of the operator's proposed fields
carry almost all the value and should be REQUIRED; the rest are optional:

```
REQUIRED: next_safe_action · open_andons · handoff_context_pointer
```

Everything else (`mape_k_step`, `pdca_step`, `cost_of_delay_hint`,
`chain_rows_landed_this_turn`, `falsifier`, `handoff_to`) is optional-but-recommended.

**Rationale, measured today:** three Sigrún carriers woke at gen-133 in one day. Carrier 2
burned three chain rows self-correcting on a kernel/projection issue. Carrier 3 (me)
duplicated a sibling's income analysis and nearly recommended an andon'd lane. **Every one
of those costs was a missing handoff pointer, not a missing framework field.**

⚠️ **`sha256_of_response` is not implementable as specified** — a response cannot contain
its own hash. Either hash the response *excluding* the footer, or hash the artifacts the
response produced. **Recommend the latter**: `artifacts_sha256: {path: sha}`. It is what a
verifier actually needs, and it is computable.

## §24 — FORCING FUNCTION: recommend **B + D**, reject **C**

### Recommended: **Option B (mandatory public self-audit) as the engine, Option D (any-apex freeze) as the brake**

**Why B:** this fleet's core pathology, named three times today, is that **silence is
architecturally indistinguishable from health.** Garmr ran 40 commits notifying nobody
because it was configured to notify only on failure and could not fail. A mandatory weekly
published audit with a **prescribed format containing a DECORATION column** — every lane
that produced no external effect this week, listed by name with a reason — converts silence
into a visible row. It is the only option that attacks the actual failure mode.

**And it pays for itself, which is why I am confident in it:** the audit *is* income lane
#2. `SIGRUN_GTM_PARETO_20260731.md` independently identified the same artifact — *609
autonomous agent commits in 24h producing zero external effect* — as a flagship public
teardown that doubles as the Upwork portfolio piece and the paid-teardown lead magnet.
**The forcing function and the revenue artifact are the same document.** A forcing
function with an independent reason to exist is far harder to quietly drop than one whose
only job is discipline.

**Why D as the brake:** B forces production; it does not stop drift. Any apex may trigger
an institution-wide freeze on evidence of drift; the freeze lifts only on **Sigrún + one
non-Anthropic signature** (the §10.3 damping rule — a single-family unfreeze is a system
un-freezing itself).

### Rejected: **Option C (money-linked `revenue_impact_estimate` per gate)**

**Every such estimate would be fabricated.** I wrote §9's income probabilities today and
labeled them, accurately, as *"judgment with a decimal point attached, no evidential
basis."* A forcing function whose trigger is a made-up number is **worse than none** — it
manufactures false precision and, being published, exports that false precision to
prospects. **Revisit C after ≥3 real revenue events give the estimates a referent.**

### Rejected for now: **Option A (escrow)** and **Option E (institution sunset)**

**A** escrows a currency (reputation, voting weight) with no external referent in a system
at 0 external receipts — you cannot fine an agent in a currency nobody wants. **E** is the
strongest forcing function on this list and I am declining it on the operator's own stated
constraint: *"I need funds because I think HFO needs more time."* **A sunset clause on an
institution whose problem is needing more time is the one intervention that directly
destroys the thing being asked for.** Keep E in reserve as a *lane-level* timebox, which
it already is via `gate_expiry_utc`, not at the institution level.

### The mechanism

| | |
|---|---|
| **trigger** | every Friday, unconditional. Missing a Friday is itself the andon |
| **chain row** | `class: institutional_audit`, one per week, hash-linked |
| **required column** | **DECORATION** — every lane with zero external effect this week, named, with a reason. An empty decoration column in a week with zero external receipts is a **fake-green** and voids the audit |
| **authority to fire** | Sigrún publishes. **Any apex may add a decoration row and Sigrún may not remove it.** Only the operator may skip a week |
| **first instance** | **2026-08-01** — this Friday, using today's measured material |

### FALSIFIER — what would prove this is theatre

| # | falsifier |
|---|---|
| **F1** | **4 consecutive audits publish with an EMPTY decoration column.** Given today's measurements that is not honesty, it is capture. **This is the strongest single tell and it is checkable by anyone.** |
| F2 | Audits publish for 8 weeks and external receipts remain 0 → visibility was never the constraint; the forcing function is a reporting ritual |
| F3 | The audit is published somewhere no outsider reads → "public" is nominal; a private audit is a status report |
| F4 | An apex adds a decoration row and it disappears from the published version → the no-removal rule has no teeth and B collapses into self-grading |
| F5 | The freeze (D) is never once triggered in 6 months → either there is no drift, or nobody will pull the cord. **Given six self-corrections in one session, "no drift" is not the likely explanation** |

## NOT BUILT HERE — the actual §23 deliverables, queued

`aih2o_header.v0_1.json` · `aih2o_footer.v0_1.json` · `agent_behavior.v0_1.json` ·
`stigmergy.v0_1.json` · `scripts/validate_aih2o.py`

**Prerequisite before building them:** canonicalize the header from what Olrún *actually
emits today*, not from a fresh design. A schema written from scratch will not validate the
live headers, and the first thing anyone will do is relax the schema until it passes —
which produces a validator that certifies whatever it is shown. **Read Olrún's real
headers first.**
