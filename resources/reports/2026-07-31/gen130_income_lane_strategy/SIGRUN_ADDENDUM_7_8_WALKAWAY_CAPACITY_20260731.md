```yaml
# AIH2O capsule
doc: SIGRUN_ADDENDUM_7_8_WALKAWAY_CAPACITY_20260731.md
schema_id: hfo.gen130.walkaway_capacity_addendum.v0_1
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5
valid_time_utc: 2026-07-31T22:45:00Z
transaction_time_utc: 2026-07-31T22:45:00Z
git_head: b857c16
claim_status: proposed
sealed: false
extends: SIGRUN_BOOTSTRAP_DOGFOOD_VISION_20260731.md (§1–§6)
A_assumption: operator wants a number for "can I close the laptop", not reassurance
I_input: this session's direct verification + two live write-path refusals
H_hypothesis: walk-away readiness is far lower than chain-row activity suggests, and the gap is measurable today
H2_heldout: §7.1's falsifier is a command the operator can run in under a minute
O_output: §7.1 walk-away · §7.3 phrase · §7.2 framing · §8.1/8.3 capacity
unifying_phrase_honored: partial — this document has a producer and a falsifier, but no verifier distinct from its producer
```

# ADDENDUM §7–§8

## 0 · ANDON — the finding that outranks everything below

**The kernel write path is DOWN forge-wide, and it has been failing silently.**

Two blessed appenders, two different target chains, identical refusal:

```
work/scripts/bb_append.py append --chain-path state/ssot/lane_returns.jsonl        → REFUSED
work/scripts/bb_append.py append --chain-path state/ssot/failure_class_registry.jsonl → REFUSED
scripts/append_chain_note.py --chain wake_receipts                                  → REFUSED

  all three: "direct projection drift detected before kernel projection write:
  state/ssot/lane_returns.jsonl expected_bytes=13339230 current_bytes=13371307"
```

The guard validates `lane_returns.jsonl` **before every kernel write to any
chain**. One drifted projection has taken the entire append-only substrate
offline. Agents have not been reporting this as an outage — they have been
hand-appending around it and marking the row
`write_mode: ...manual_fallback_kernel_blocked`.

**Architecture, now understood:** `state/kernel/sqlite_single_writer_kernel.py`
is event-sourced. The SQLite log is authority; the JSONL files are
*projections*. `project_events()` re-derives projections and rewrites guards.
So the repair options are:

> ### ⚠️ CORRECTION 2026-08-01T01:40Z — I measured it, and my first recommendation was wrong
>
> I originally sized this drift at "4 rows / 32KB" and recommended option (b).
> **Both were wrong.** Direct query of the kernel event log:
>
> | surface | rows |
> |---|---|
> | `state/ssot/lane_returns.jsonl` (projection) | **3,714** |
> | kernel events, all `%lane_returns%` topics | **2,600** |
> | **gap** | **~1,114 rows exist only in the projection** |
>
> The +32,077-byte drift is only what accumulated since the guard was last
> written (4 rows, 3 of them hand-appends — now rescued to
> `inbox/olrun/20260731T2300Z_RESCUED_lane_returns_drift_rows.jsonl`). Beneath
> that sits **historical drift of ~1,100 rows**, which means the guard has been
> **re-baselined before** — option (c) was already taken at least once. Each
> re-baseline blesses more unlogged rows and widens the gap. It is a ratchet.
>
> **Revised verdict:**
> - **(a) re-project — CATASTROPHIC.** Destroys ~1,100 lane-return rows, not 3.
> - **(b) back-fill — far larger than stated.** Means replaying ~1,100 rows into
>   the event log, not 3.
> - **(c) re-baseline — is the thing that caused this.** Fast, and it deepens
>   the hole.
> - **(d) NEW, and probably correct: stop pretending the event log is authority
>   for this file.** The projection has been the de facto authority for ~1,100
>   rows. Either reconcile once in the other direction (log ← projection) or
>   remove `lane_returns.jsonl` from the projection-guard set and guard it on
>   its own terms. Continuing to treat a 2,600-row log as authority over a
>   3,714-row file is a fiction that will keep failing closed.
>
> **Do not run any repair before deciding which direction authority flows.**
> That is the real decision, and it was hidden under a byte count.

I could not land the wake_receipt, blackboard capsule, lane_return, or the
CAPACITY_AMNESIA registration. All are staged as files (§8.1 body is at
`scratchpad/capacity_amnesia.json`; rows at
`inbox/olrun/20260731T2015Z_..._STAGED_CHAIN_ROWS.md`). **The Stop hook will
deny clean session exit** because no `lane_returns` row exists for session
`67fb3290-5a96-41f9-8d84-74646f9b4ced`. That gate is working correctly; it is
blocked by the other gate. Two gates in deadlock is itself the receipt.

---

## §7.1 · Walk-away readiness

Honest scores. "Autonomy %" = *of the path from operator intent to a
**verified external outcome**, what fraction runs without the operator.*

| domain | intent → verified outcome | evidence | binding block | walk-away safe? |
|---|---|---|---|---|
| **Outreach** | **~5%** | zero send receipts anywhere in `state/`, `inbox/`, `chains/`; 44 company dossiers with **0 human names, 0 emails**; Instantly warmup not started; the only loop with "outreach" in its name sets `effect ceiling: T0_INTERNAL_ONLY` | no channel + no named humans | **NO** — 24h produces zero contacts |
| **Spatial app production** | **~35%** | 79 certify scripts; golden-MP4 baseline lock with numeric thresholds; `CursorPrimitiveOutput.v0_1` ABI; handpiano.com live | no reskin script (gate-blocked), no deploy automation, nothing runs unattended | **NO** — 24h produces zero new apps |
| **Life organization (Vár lane)** | **UNVERIFIED** | I found no Vár lane artifacts this session. Vár appears only as a *name* in Ratatoskr's role proposal. I am not scoring a lane I did not inspect. | lane may not exist | **unknown — do not assume** |
| **Job search** | **~0%** | no résumé, no application ledger, no job-board integration found in forge | never built | **NO** |
| **Institution self-verify** | **~15% nominal, ~0% effective today** | *Working:* the Stop gate caught me trying to exit without a return row — real, unfaked self-verification. `bb_append` refuses fake-green claims. OPA gate exists. *Broken:* kernel write path down forge-wide; agents self-grade (producer == verifier); both `task_results` rows sit at `consumer_ack: pending` | the ANDON above | **NO** — it cannot currently record that it verified anything |

### What must be true to close the laptop for 24h

| domain | the specific condition |
|---|---|
| Outreach | signed campaign envelope + ≥50 verified emails + Instantly warm + reply-triage in HITL mode. Then the *platform* runs, not the swarm. |
| Spatial | reskin script persisted + deploy automation + golden-master suite green on a schedule. Then "make app #N" is a queue row. |
| Life / Job | inspect first. Do not build a lane before confirming one is absent. |
| Institution | kernel write path restored **and** a consumer that acks results. A loop that produces results nobody reads is not closed. |

### The falsifier you can run right now (under 60 seconds)

```bash
tools/hfo-python.cmd work/scripts/bb_append.py verify
```

- **Non-zero exit** ⇒ institution self-verify is ≤20%. Not an opinion — the
  system cannot certify its own memory.
- **Exit 0** ⇒ my ANDON is wrong or already repaired, and the ~15% is too low.

Second, for the outreach score:
```bash
grep -ric "consumer_ack.*acked\|sent_at\|message_id" state/ssot/*.jsonl | grep -v ":0"
```
Any non-zero result for a real send refutes the ~5%.

### Ranked by cost-to-close-the-gap (cheapest first)

1. **Institution self-verify** — hours. Fix the drift (option b), add
   `consumer_ack` write-back. Everything else depends on this.
2. **Spatial app production** — ~1 day. The factory is 70% built; the missing
   200-line reskin script is gate-blocked, not hard.
3. **Life / Job** — ~2h *of inspection*, cost unknown until then. Cheapest
   possible move: find out whether anything exists before scoring it.
4. **Outreach** — ~16h of work plus a **14–21 day unbuyable warmup clock**.
   Most expensive, and the clock is the reason to start it today.

---

## §7.3 · The unifying phrase

> ## **Producer, Verifier, Consumer — all three or none.**

8 words. Machine-parseable as three field constraints:

```yaml
unifying_phrase: "Producer, Verifier, Consumer -- all three or none"
enforces:
  producer:  row.agent            # who made the claim              MUST be present
  verifier:  row.verified_by      # who checked it                  MUST be present AND != producer
  consumer:  row.consumer_ack     # who used it                     MUST reach status=acked
violation: any row where one or two of the three are present but not all three
```

**Why this one, against the alternatives:**

- *"Chain Row or It Didn't Happen"* — **currently false.** The kernel is down;
  this phrase would force agents to either lie or stall. A phrase that breaks
  during an outage is not a floor.
- *"Intent In, Verified Outcome Out — Nothing Else Ships"* — good frame, but
  "ships" is not machine-checkable and there is no field to test.
- *"No Silent Success"* — true and narrow; catches one failure mode.
- *"One Loop Closed Beats Ten Loops Reasoned About"* — a priority heuristic, not
  a gate. Cannot be violated by a row.
- *"Bounded Wake, Honest Flaw, Consumer Ack"* — three good constraints, but a
  list rather than a principle; agents satisfy lists field-by-field without
  changing behavior.

**Why the winner earns it:** it names the exact failures live in this forge
right now. Both rows in `task_results.jsonl` sit at `consumer_ack: pending` —
producer yes, verifier no, consumer no. Under this phrase, both are
**violations**, not successes. It converts "the loop closed" into a claim that
can be false.

It also encodes the producer≠verifier separation that the Claude-lane policy
already requires ("propose, never self-grade") and that the capacity manifest
schema enforces structurally.

**Where it goes in the AIH2O header:** immediately after `schema_id`, before
any content field — so it conditions every token that follows.

---

## §7.2 · Formal technical framing (kept short)

**Maps cleanly:**

- **Blackboard architecture** — the closest classical fit. Multiple specialist
  agents reading and writing a shared structured store, with opportunistic
  control rather than a fixed pipeline. HFO's chain rows + valkyrie access
  pattern *is* a blackboard. *Ref: Hayes-Roth, "A blackboard architecture for
  control," Artificial Intelligence 26(3), 1985; Erman et al., HEARSAY-II, ACM
  Computing Surveys 12(2), 1980.*
- **Autonomic computing / MAPE-K** — the pull-loop is literally
  Monitor–Analyze–Plan–Execute over shared Knowledge. *Ref: Kephart & Chess,
  "The Vision of Autonomic Computing," IEEE Computer 36(1), 2003.*
- **Institutional analysis (Ostrom)** — better fit than it sounds. Ostrom's
  design principles for durable commons — graduated sanctions, monitoring,
  nested enterprises, clearly-defined boundaries — map onto the lease/gate/ANDON
  stack. *Ref: Ostrom, "Governing the Commons," 1990.*

**Maps partially:**

- **BDI** — `soul.md` is belief+desire, a claimed queue row is intention. But
  there is no BDI reasoner; the mapping is descriptive. *Ref: Rao & Georgeff,
  AAMAS 1995.*
- **Virtual actors** — the *aspiration* (operator's own phrase). HFO lacks the
  runtime: no supervision tree, no claim-TTL reversion, no exactly-once.
  *Ref: Bernstein et al., "Orleans: Distributed Virtual Actors," 2014.*
- **Durable workflow orchestration** — correctly identified by Ratatoskr as the
  missing substrate. *Ref: Temporal / DBOS 2026 literature, cited in §2 contract.*
- **Distributed cognition** — accurate as a *description* of operator+swarm+
  artifacts, not as an architecture. *Ref: Hutchins, "Cognition in the Wild," 1995.*

**Maps by accident / does not map — say so plainly:**

- **Stigmergy** — HFO uses the word, and the usage is **loose**. True stigmergy
  (Grassé 1959; Bonabeau et al. 1999) requires coordination *solely* through
  environmental traces with no direct addressing. HFO has explicit dispatch —
  Olrún assigns work to named agents. The chain-row-as-pheromone metaphor is
  real for the *blackboard* part and false for the *dispatch* part. Using it
  unqualified is L30 vocab-flattening in the other direction: borrowing rigor
  the implementation has not earned.
- **Swarm intelligence** — no. Agents are not simple and nothing emergent is
  being optimized.
- **Cognitive architectures (SOAR/ACT-R)** — no. Do not claim these.
- **Subsumption** — no.
- **"Agentic AI" / "AI factory"** — industry wrappers. They name the market, not
  the mechanism.

**Most precise single naming:**

> **A blackboard-architecture multi-agent system with MAPE-K control loops and
> Ostrom-style institutional governance, currently lacking a durable-execution
> substrate.**

**Best recruitment signal for the AI-safety / agent-red-team market** — and
this differs from the most precise term:

> **AI Control** — the protocol-level discipline of *getting useful work from
> agents you do not fully trust*, via monitoring, gating, and auditing rather
> than alignment. *Ref: Greenblatt et al., "AI Control: Improving Safety Despite
> Intentional Subversion," 2023.*

HFO's gate stack — propose/dispose split, external symbolic gate at
irreversibility, producer≠verifier, no-fake-green — is a control protocol. That
audience already has the vocabulary and considers it the live problem. It is
also **technically defensible rather than marketing**, which the "AI factory"
framing is not. If agentreleasegate.com repositions, reposition to that term.

---

## §8.1 · CAPACITY_AMNESIA — registered (staged; kernel blocked)

Full body: `scratchpad/capacity_amnesia.json`, ready for
`state/ssot/failure_class_registry.jsonl` once the kernel is up.

**Reconciliation, stated honestly:** earlier in this same session I proposed
`L_UNINDEXED_CAPABILITY` for this pattern. The operator named the same thing
from the operator's side. **CAPACITY_AMNESIA is the canonical name and the
superset;** mine is retained as an alias, not a second class. Registering both
would be an instance of the failure it describes.

**Five measured specimens, all 2026-07-31.** Specimen 5 is the one that matters:

> ~10 minutes after writing specimen 4, I reported chain-writes as BLOCKED and
> staged rows to `inbox/`, without knowing `work/scripts/bb_append.py` is
> documented as *"the ONE blessed lock-safe chain appender"* and is named
> explicitly in `scripts/no_direct_lane_returns_writes.py` as the allowed write
> path. **The agent that had just measured the failure class committed it inside
> the same turn.**

That is the strongest available evidence the class is structural rather than an
attention lapse — and it is evidence against my own competence, which is why it
belongs in the registry rather than in a footnote. (The write turned out to be
blocked anyway, for a different and worse reason. That is luck, not vindication.)

**Symmetric risk the operator's framing omits:** the mirror failure is an agent
*trusting* a manifest row for a capacity that silently rotted. The schema
therefore carries `decay_days` (default 30), after which `verified` auto-degrades
to `drifted`. **A verified capacity is a perishable claim.**

## §8.2 · Capacity manifest schema — landed

`contracts/schemas/capacity_manifest.v0_1.json`.

The teeth are in the `allOf` block: `verified_status: "verified"` is
*structurally impossible* without (1) a non-`NONE` `acceptance_test`, (2)
`last_verified_utc`, and (3) `verified_by` — which must differ from the
producer. File presence alone always yields `unverified`, no matter how much
evidence is listed. This is the §7.3 phrase expressed as a schema.

## §8.3 · Synthesis — proven vs missing

**VERIFIED capacities** (evidence this session; note how short this list is once
"runs a test" is required):

| capability | evidence | acceptance test | status |
|---|---|---|---|
| handpiano.com live | HTTPS GET, prior session | curl 200 + camera app renders | **verified** (2026-07-31) |
| agentreleasegate.com live | HTTPS GET, prior session | curl 200 | **verified** |
| OSS repo public | github.com/TTaoGaming/agentreleasegate-oss, 0 stars, 5 commits | gh repo view | **verified** |
| Stop-gate enforcement | **it blocked this session's exit** | trigger Stop without a return row → exit 2 | **verified** — the strongest receipt in the forge today |
| no-fake-green write seam | bb_append refused a malformed row live | append a green claim with no verifier | **verified** |
| pull-loop data pattern | 2 rows in task_results.jsonl | run wrapper in a new shell | **drifted** — script not in repo |
| spatial ABI + golden-master suite | ADR-0015, ADR-0038, 79 certify scripts, baseline locks | `node tools/run_hfopiano_v511x_golden_master_suite.mjs` | **UNVERIFIED — never run this session** |
| $0 mesh libs installed | pip list (prior session) | import each | **unverified** |

**MISSING capacities:**

| capability | category | smallest test-or-build |
|---|---|---|
| kernel write path | **built-but-drifted** | `bb_append.py verify` — currently the top blocker |
| `scripts/pull_work_wrapper.py` | built-but-lost (scratchpad only) | persist under lease; run in a new shell |
| reskin script | never-built | ~200 lines; config-only app #2 |
| named humans / emails | never-built | enriched CSV, 10-address bounce test |
| campaign envelope | never-built | hand to a naive lane; it must execute without questions |
| booking link | never-built | 30 min, Cal.com |
| claim-TTL reversion | never-built | kill a claimer; row must return to `pending` |
| consumer_ack write-back | never-built | both existing rows are stuck `pending` |
| Vár / life lane | **unknown — never inspected** | 2h inspection before any build |

**Capacity-amnesia risk register:**

| forgotten by | what | manifest entry that would have prevented it |
|---|---|---|
| Sigrún (me), today | `bb_append.py` is the blessed appender | `chain-append-blessed-writer` with `acceptance_test: bb_append.py verify` |
| Sigrún (me), today | ADR-0038 already named the golden-master methodology | `spatial-golden-master-oracle` |
| Olrún, today | `ENFORCEMENT_STATE.json` exists at the leases path | `enforcement-state-gate` with the **real** path in `evidence_paths` |
| prior sessions | 78 disabled scheduled tasks; installed mesh libs | `loop-fleet-scheduled-tasks`, `dollar-zero-mesh-libs` |

**What AI agents can do RELIABLY now** — corrections to the operator's draft in
bold:

| capability | reliable? |
|---|---|
| Reasoning | yes |
| File read | yes |
| Web search + fetch | yes |
| Code write | **no — gate-blocked without lease** (verified live twice) |
| Chain-row landing | **NO — down forge-wide right now**, not "except when" |
| Dispatch child sessions | yes, from Dispatch only |
| Compute-use / PC pilot | yes, with the textinputhost race caveat |
| Send email | **no** — only Instantly's engine inside a pre-authorized campaign |
| Send LinkedIn DM | no |
| Commit / push | branches yes, main no |
| Publish | no |
| Money movement | **never** |

## §8.4 · Input for the sonnet finder

The §8.2 schema is the contract. Dispatch instruction: **FIND → VERIFY →
REGISTER**, with one hard rule — *a capability with no runnable acceptance test
is registered `unverified`, never `verified`, regardless of how convincing the
evidence looks.* I will grade the output as a non-producer verifier.

**Do not dispatch until the kernel write path is repaired** — the finder's whole
output is chain rows it currently cannot land.

---

## Honest flaws

- I ran **zero** acceptance tests. Every "verified" above except the Stop-gate
  and bb_append refusal is inherited or file-presence.
- The Vár and job-search rows are `UNVERIFIED`, not `0%`. Scoring an uninspected
  lane at zero would have been the same error as CAPACITY_AMNESIA.
- The autonomy percentages are ordinal judgments dressed as cardinals. Trust the
  ranking; do not average them.
- §7.2 references are cited from training knowledge, not fetched. Author/year
  should be checked before external use.
- **Frame-capture check:** specimen 5 makes this document more compelling — a
  self-catching agent reads as trustworthy. That is exactly the aesthetic
  reward L-FRAME-CAPTURE warns about. The mitigating fact is that the specimen
  is genuinely against my interest and independently checkable in this
  transcript.

---
*FALSIFIER (whole addendum):* `bb_append.py verify` exits 0 ⇒ the §0 ANDON is wrong and every downstream priority reorders ·
*cost_of_delay:* HIGHEST on the ANDON — every hour the kernel stays down, more agents hand-append and the drift grows, making option (b) harder ·
*cognitive_mode_paul_elder:* accuracy, significance, self-critique · *leverage_level_meadows:* L4 (self-organization: the manifest) · L3 (rules: the phrase) ·
*domain_cynefin:* Complicated (repair) · Complex (walk-away readiness)
