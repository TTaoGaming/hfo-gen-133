# software_factory_v0_1 — the HFO production line

```yaml
schema_id: hfo.gen133.contract.software_factory.v0_1
valid_time_utc: 2026-07-31T15:00:00Z
transaction_time_utc: 2026-07-31T15:00:00Z
claim_status: proposed
author: SIGRUN_P4 · claude-opus-5 · Claude Code · gen-133
companion: contracts/loop_engineering_gap_analysis.v0_1.md · contracts/proof_artifact_criteria.v0_1.md
```

## 0. What "software factory" means here

Industry meaning (Cusumano, *Japan's Software Factories*, 1991; later Microsoft
DevOps usage): a **standardized, repeatable production line** where different
products come off the same infrastructure via **configuration swaps**, not
bespoke rebuilds. The value is not automation — it is that the *line* is the
asset, and each new product costs a config file rather than a project.

**The failure mode this must avoid:** HFO has repeatedly built *loop machinery*
and called it a factory. A factory that produces nothing is a building. The
measured evidence (`loop_engineering_gap_analysis` §0) is that the most advanced
loop in the fleet spent 40 commits building and maintaining itself, and its last
work item was recording that its mailbox was empty.

**Therefore rule zero: a line is not commissioned until it has produced 3
products that passed QA. Building the line does not count as running the line.**

## 1. The standard line

Every product moves through the same 9 stations. Stations are invariant; only
their *configuration* changes per product class.

```
[0] TRIGGER    → schedule, queue depth > 0, or operator dispatch
[1] SUPERVISE  → runner registers PID, starts wall-clock deadline, writes start metric
[2] WAKE       → golden path (contracts/golden_waking_paths.v0_1.md) + W1-W3 witness
[3] CLAIM      → lease one work item with fencing token; refuse if depends_on unsealed
[4] GATE-IN    → effect ceiling check, kill-switch read, quota check, gate-expiry sweep
[5] WORK       → the product-specific step. THE ONLY STATION THAT VARIES IN KIND
[6] QA         → accept/reject test for this product class. Cannot be self-graded
[7] RECEIPT    → chain row + metrics row (fired_at, duration, exit_code, produced_artifact)
[8] RELEASE    → seal; on external effect, halt for operator signature
[9] SLEEP      → backoff with jitter; write next_due_utc
```

**Failure paths (currently missing — see gap analysis):**

```
any station exceeds deadline    → SIGKILL, deadletter row, supervisor restart (max 3, then halt)
station [5] returns no change   → increment unchanged_count; at 3 consecutive → ANDON, stop line
station [6] rejects             → deadletter with reason; do NOT retry the same input
downstream tool fails 3×        → open circuit breaker 1h
```

## 2. Product catalogue

| # | product class | station [5] does | station [6] QA gate | DRI | throughput target/day |
|---|---|---|---|---|---|
| P1 | **packaged proof artifact** | assemble an artifact per `proof_artifact_criteria.v0_1` | all 5 gates G1–G5 pass; ≥1 external reader passes F1 | code lane | **1** (7/week is the whole §3 backlog) |
| P2 | **outreach draft** | draft one message, compute `body_sha256`, `operator_signature: null` | ≤120 words, exactly 1 CTA, proof link resolves 200 | Garmr | **2** |
| P3 | **outreach send** | transmit a signed draft | operator signature present for THIS body_sha256 | **operator only** | **≤2, human-gated** |
| P4 | **spec / contract document** | author a contract with schema_id + falsifiers | has `schema_id`, `valid_time_utc`, `claim_status`, ≥3 falsifiers | Sigrún | 2 |
| P5 | **code commit / PR** | implement against a spec on a `codex/*` branch | tests exit 0; not on main; PR opened | Codex | 3 |
| P6 | **wake receipt** | rehydrate + answer W1–W3 | all 3 witness answers correct | any carrier | ~6 (1/session) |
| P7 | **quorum verdict** | run one of the 5 quorum variants (§3) | ≥3 voters from ≥2 families; dissent recorded | Olrún | 1 |
| P8 | **red-team audit** | adversarial audit of an HFO subsystem, by a non-owner | reproducible from the artifact alone; failure taxonomy present; honest_flaw non-empty | Hrist / external | 0.5 |
| P9 | **bulk classification** | $0-mesh schema-conforming extraction | schema validation passes; non-conforming discarded not repaired | Ollama | 100+ |
| P10 | **liveness heartbeat** | append one timestamped row, nothing else | row exists at the scheduled hour | scheduler | 24 |

## 3. Quorum variants as distinct products

A quorum is not one thing. Five variants, five schemas, five DRIs. The
distinguishing question is **what the voters are instructed to do**, because
that determines what a "pass" means.

| variant | voter instruction | pass condition | weighting | used for |
|---|---|---|---|---|
| **Approval quorum** | *"Should this proceed?"* | weighted majority yes | `1/√(n_family)` — dampens one vendor packing the vote | spec promotion, plan approval |
| **Red-team quorum** | *"Find the failure mode. Do not approve."* | **passes only if ≥3 voters, instructed to break it, fail to find a defect** | equal weight; family diversity **mandatory** (≥3 families) | anything about to acquire external effect |
| **Safety quorum** | *"Is this catastrophic?"* — financial, credential, irreversible, public | **unanimous** no-catastrophe, or it halts | veto-weighted: **any single voter can halt** | send / spend / publish / merge / seal |
| **Brand / voice quorum** | *"Does this match the voice guide, and is it free of internal jargon?"* | ≥2/3 pass + jargon-lint exit 0 | equal | outbound artifacts only |
| **Reproducibility quorum** | *"Re-execute the claim using ONLY the artifact. Do not ask the author."* | ≥1 independent voter reproduces the stated number | binary — one success suffices; **zero attempts ≠ pass** | any artifact making a numeric claim (G3) |

**Design notes that are load-bearing:**

- **Red-team quorum inverts the null hypothesis.** Approval quorum defaults to
  reject-until-approved. Red-team defaults to **fail-until-nobody-can-break-it**.
  A red-team quorum where everyone agrees quickly is a *failed* quorum — either
  the voters were not adversarial or they shared a blind spot.
- **Safety quorum is the only one with a veto.** Majority rules are wrong for
  catastrophic actions; one credible objection is sufficient.
- **Reproducibility quorum is the only one that requires a voter to run code.**
  It is the most expensive and the only one that produces evidence rather than
  opinion. It is what makes G3 of the proof-artifact contract real rather than
  aspirational.
- **Same-family voters are correlated.** Three Claude sessions are close to one
  vote. Family diversity is not a nicety; without it the quorum measures
  agreement with a prior, not truth.

## 4. Reconfiguration seam

| VARIES per product (the config file) | INVARIANT across all products (the line) |
|---|---|
| prompt template | 9-station sequence |
| tool subset granted | chain-row schema |
| target substrate (Claude / Codex / cloud / Ollama) | metrics-row schema |
| effect ceiling | gate discipline at station [4] |
| QA gate at station [6] | supervisor + deadline + reaper |
| DRI | no-self-grading rule |
| cadence + throughput target | andon-on-no-progress (3 unchanged ⇒ halt) |
| token budget | human gate at irreversibility |

**A new product class should be a YAML file, not a project.** If standing up a
new line requires writing code, the seam is in the wrong place.

Proposed: `areas/factory/lines/<line_id>.yaml`.

## 5. Throughput and cost

**Honest position: I do not know the operator's real N/day requirement.** The
numbers in §2 are my proposals derived from the §3 artifact backlog, not
elicited. Treat them as a starting hypothesis to be corrected in one sentence.

The one number that is not a guess:

```
external receipts required in the next 30 days = 1
```

Everything else is instrumental. A factory producing 100 specs/day and 0
external receipts is at **zero throughput** by the only metric with a liveness
property.

### Cost model (to be measured, currently unmeasured)

| line | est. tokens/product | daily ceiling | cost-per-outcome spot check |
|---|---|---|---|
| P1 proof artifact | ~80k | 200k | $/artifact that passed all 5 gates |
| P2 outreach draft | ~20k | 60k | $/draft that the operator actually signed |
| P4 spec | ~100k | 200k | $/spec that produced a shipped implementation |
| P5 code | ~150k | 400k | $/PR merged |
| P9 bulk | **$0** | unbounded | — (local) |
| P10 heartbeat | ~2k | 50k | — |

**Enforcement:** the runner refuses to start a line that has exceeded its daily
ceiling. Recorded per `loop_id` in `state/ssot/loop_metrics.jsonl`.

**Prior evidence this matters:** a gen-130 note records ~$65–70/day of Opus burn
from four scheduled runners, with the countermeasure "drop p0 to haiku." That
was a correct diagnosis that was never enforced by a mechanism. A ceiling in a
config file that the runner reads is a mechanism; a note is not.

## 6. First three lines to stand up, ranked by income-now leverage

### Line 1 — **P10 liveness heartbeat** (30 min)
The cheapest possible product. Its purpose is not the product; it is to
**instrument the scheduler itself**. Until one row lands unattended, every claim
about autonomy is a guess. Build first because everything else's cadence
assumption depends on the answer.

*QA gate:* a row exists at the scheduled hour with no operator present.

### Line 2 — **P1 packaged proof artifact** (3h for the first product)
The only line whose output can reach a stranger. First product: the case-study
1-pager from the gen-131 OSS teardown. **Income-now leverage: highest.**

*QA gate:* all 5 gates + one external reader passes F1.

### Line 3 — **P2 outreach draft** (2h for the first product)
Consumes Line 2's output as its proof link. Ends at a signed-and-held draft.
**Line 3 does not send** — P3 is a separate, operator-only product.

*QA gate:* ≤120 words, one CTA, proof link returns 200.

**Deliberately NOT in the first three:** P7 quorum, P8 red-team audit, P5 code.
All three are valuable and all three are *internal*. Standing them up first
would be the exact failure §0 names — building line machinery instead of
shipping product. **P8 in particular is tempting because HFO is unusually good
at it; it belongs in the long-horizon lane, not this week.**

## 7. FALSIFIERS

| # | falsifier | test |
|---|---|---|
| F1 | The factory framing is overhead for a one-operator shop; 3 ad-hoc artifacts would ship faster than 1 artifact + a line | **Ship artifact #1 manually first. Only build the line if artifact #2 is faster than #1 was.** This is the honest test and it is cheap |
| F2 | Throughput targets in §2 are invented; the operator's real requirement is different | ask, in one sentence. Until then they are marked as hypothesis |
| F3 | The 9-station line adds latency without adding yield | measure wall-clock and QA-pass rate for 3 products with the line vs. 3 without |
| F4 | Quorum variants are over-specification — HFO has never run a single quorum of any kind to completion | **check: has any quorum ever produced a verdict row? If no, §3 is a design for a thing that has never existed once.** Ship one approval quorum before specifying five |
| F5 | Rule zero gets violated: the line is declared "commissioned" on the strength of the spec | count products with QA-passed status. Fewer than 3 ⇒ the line is not commissioned, regardless of how complete the config looks |

**F4 and F5 are the ones most likely to bite.** This document is itself a P4
product — a spec — and specs are the product class HFO already overproduces.

---

*claim_status: proposed · zero lines commissioned · zero products QA-passed ·
honest_flaw: this is a factory design written by a lane that has historically
produced specs instead of products, and it specifies five quorum variants for a
system that has never completed one quorum*
