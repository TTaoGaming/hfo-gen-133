```yaml
# AIH2O capsule · conforms to contracts/capsule_schema_v0_1.md §3
doc: contracts/manual_cpr_vs_autonomous_diff.v0_1.md
schema_id: hfo.gen133.contract.manual_cpr_vs_autonomous_diff.v0_1
generation: 133
authored_by: SIGRÚN · P4 DISRUPT / O4 AUDIT · claude-opus-5 · ceiling=strategic (SPEC ONLY)
valid_time_utc:       2026-08-01T07:10:00Z
transaction_time_utc: 2026-08-01T07:10:00Z
git_head: 60893a4
claim_status: proposed
sealed: false
subject: "what operator presence supplies that autonomy lacks, and the substitute for each"
depends_on:
  - HALLUCINATION_SPIRAL_ROOT_CAUSE_20260801.md
  - contracts/anti_hallucination_golden_path.v0_1.md
```

# CONTRACT · MANUAL CPR vs AUTONOMOUS — THE DIFF

> Operator: *"system works partially with me manual CPR and launching but
> getting agents to work without my constant attention is causing hallucinations"*

**Method.** Enumerate the *functions* the operator performs — not the actions.
For each, name the substitute mechanism, its cost, and honestly mark whether it
is substitutable at all. A design that pretends everything is substitutable will
fail at the one thing that is not.

**Headline result:** of 8 functions, **5 are cleanly substitutable with boring
machinery**, 2 are partially substitutable, and **1 is not substitutable and
must remain the operator's**. The good news is that the 5 substitutable ones
account for essentially all of the observed hallucination incidents.

---

## §1 · The eight functions

### D1 · ATTENTION — someone notices the thing that did not happen

**What the operator does.** Notices absence. *"Why haven't I seen a COP row?"*
*"You lost header. rehydrate."* Both were absence-detections. The operator is
the system's **only** negative-evidence sensor (root-cause H_new).

**Why it fails autonomously.** Every HFO monitor reads rows that exist. Nothing
enumerates what *should* exist. Three hourly loops produced zero rows and no
component noticed — the loops were rewritten, documented, and audited during
that silence.

**Substitute — `expected_writes.jsonl` + reconciler + off-host dead-man's-switch**
(golden path §3, §3.1). Declare expected output per loop; diff expected against
actual; alarm on the difference. Prometheus `absent()`, generalized.

- cost: ~80 lines + one free SaaS ping
- fidelity: **high** — absence is fully mechanizable
- ⚠️ must be off-host or it fate-shares with its subjects (`WATCHDOG_FATE_SHARING`,
  registry row 5)

---

### D2 · CONTINUITY — someone remembers what the agents forget

**What the operator does.** Carries state across sessions in nerve and blood.
Knows the forge migrated to gen-133 on 2026-07-30 when every prompt still says
gen-130. Knows the laptop runs 24/7.

**Why it fails autonomously.** Wakes read `tail -n 20` of a **13.2 MB**
`lane_returns.jsonl` (root-cause E7). Working memory is ~20 rows deep no matter
how much history exists. Anything older is structurally invisible — capacity
amnesia is architecturally guaranteed, not an agent failing.

**Substitute — two parts, and the second is the one that is missing:**

1. *(exists)* bitemporal store + world-state capsules. **XTDB is installed and
   drift still happened** — because a store nobody queries is a filing cabinet.
2. *(missing)* **a forced-read query at wake, not a forced-read file.** Not
   "read the capsule" but a *specific derived question* the wake cannot proceed
   without answering:
   - *"which of my last 10 claims are still grade `A`?"*
   - *"what changed in canon since my last receipt's `git_head`?"*
   - *"what does `forge_identity.json` say my target is?"* ← would have caught E3
     on the first wake after migration

- cost: ~30 lines of query + a schema field
- fidelity: **medium-high**
- key insight: **the store was never the gap. The forced *interrogation* of the
  store is the gap.** Adding a bigger store will not help; this is the direct
  answer to *"don't just say use bitemporal store."*

---

### D3 · KILL-SWITCH — someone stops a bad loop before it compounds

**What the operator does.** Says *"stop"*, kills a session, disables a task.
Rate: seconds. Coverage: only what they are watching.

**Why it fails autonomously.** No breaker exists. A loop that wakes hourly and
writes confident nonsense writes 24 rows/day forever, and each becomes read-input
for the next wake (root-cause §3, the integrator).

**Substitute — circuit breaker keyed on evidence-grade collapse, not error rate**
(golden path §6).

- trip: ≥5 consecutive receipts with all-grade-`A` claims → OPEN
- trip: 0 receipts across grace periods → OPEN
- reset: operator-typed `verb=BREAKER_RESET` or tier-1 deterministic green
- cost: ~50 lines
- fidelity: **high**
- ⚠️ **error-count breakers would have caught zero of this session's incidents.**
  Every hallucination was a *successful* execution producing a confident wrong
  claim. Exit code 0. This is why the trip condition must be evidence-grade, and
  it is the least obvious design decision in the whole set.

---

### D4 · GROUND-TRUTH INJECTION — someone supplies facts no capsule contains

**What the operator does.** *"laptop is on 24/7."* *"Fenrir is an apex."* Facts
about the physical and social world that exist only in their head.

**Why it fails autonomously.** The agent does not know *which* facts it lacks. It
fills the gap with a training prior, in the same register and at the same
confidence as its probed observations (root-cause E8).

**Substitute — two mechanisms, partial:**

1. **Probe-before-claim (R4).** Converts many pseudo-ground-truth questions into
   machine-answerable ones. *"Did the task fire?"* → read `lastRunAt`. Most
   "ground truth" needs were **latent probes the agent never ran**.
2. **A typed `operator_ground_truth.jsonl`** — durable, append-only, queried at
   wake. Facts the operator has stated: host uptime policy, roster ratifications,
   physical constraints. Where the manifest is silent, R2 forces `hypothesis`,
   never `root_cause`.

- cost: ~20 lines + operator maintenance of the facts file
- fidelity: **medium** — genuinely irreducible residue
- honest limit: this converts *"agent hallucinates a fact"* into *"agent declares
  it does not know"*. That is a large win and it is not the same as knowing.

---

### D5 · ARBITRATION — someone decides which of two disagreeing sources is right

**Not in the operator's list; it is the one that most directly generates the
observed incidents.** When canon says 19 and the registry says 8 and gen-133 has
no file, the operator arbitrates by fiat. Autonomously there is no arbiter, and
**an agent asked an underdetermined question produces a plausible answer** — the
"6 failure classes" and apex-roster incidents are exactly this.

**Substitute — single-writer canon + collision alarm** (golden path §8, R12/R13).
One owner per concept; every other mention a pointer; a validator that refuses
duplicate definitions and pulls an andon on disagreement.

- cost: ~40 lines + a one-time consolidation pass
- fidelity: **high** for *detecting* collisions; **operator-required** for
  *resolving* them (which is correct — resolution is a decision, not a fact)
- **this is the cheapest high-yield item on the list.** Each duplicated registry
  is a hallucination generator with a measurable output rate; deleting the
  duplicate deletes the generator.

---

### D6 · LAUNCHING — someone starts the work

**What the operator does.** Dispatches sessions, decides what runs now.

**Why it fails autonomously.** It mostly does not — 124 registered tasks. The
failure is the opposite: launching is the *only* fully-automated function, which
is why registrations outran activations 124:0. **The institution automated the
cheap half of the loop.**

**Substitute — R5: no registration without an expected-writes row.** Make
launching *cost* something (declare your output contract), and registration
inflation stops.

- cost: ~10 lines
- fidelity: **high**
- this is a deliberate **anti**-automation: making the automated thing harder is
  the correct move when it is the overproduced input.

---

### D7 · TASTE / PRIORITY — someone decides what is worth doing

**What the operator does.** *"targeting durable agent institution"*, *"income
lane matters"*, *"this unblocks the vision"*. Ranks by a utility function that
exists nowhere else.

**Substitute — NONE. Do not attempt one.**

- fidelity: **zero**
- Agents can *surface* candidates ranked by cost-of-delay against
  operator-stated goals. They cannot generate the goals. Any mechanism claiming
  to is fabricating a utility function, which is `L30` at institutional scale.
- **Design consequence:** the target is not "operator-free". It is
  **"operator-free for execution and verification; operator-required for
  direction."** Attention (D1) is substitutable; taste is not. Conflating them
  is why "walk away without collapse" has felt unreachable — it was scoped as
  *replace the operator* when the achievable and sufficient goal is *stop
  spending the operator on absence-detection.*

---

### D9 · CONSENT — someone clicks "yes"

*Added 2026-08-01 after evidence E9. **This function was missing from D1–D8, and
it is currently the binding constraint on the entire hive.***

**What the operator does.** Answers *"Allow using this MCP tool?"* Grants
authorization at the moment a tool is first called.

**The evidence.** Antigravity, 2026-08-01: **12+ Nidhöggr conversation windows,
every one stalled** on `Allow using this MCP tool? hfo/board_status`, active
session reading *"Waiting for user input.."* — blocked at **first tool use**.
Operator: *"these are not loops. these are just nudges."*

**Why it fails autonomously — and it is worse than the other eight.** D1–D8 all
degrade *gradually*: without attention, errors accumulate; without continuity,
context thins. **D9 does not degrade — it halts.** Zero work product, at the very
first tool call, on every fire. And the halt is **invisible**: a stalled session
is byte-identical to a session that never fired (no rows, no error, no exit
code), so D1's absence-detector is the only thing that could ever see it, and D1
does not exist either.

**This is the manual-CPR pattern in its purest form.** The substrate *advertises*
autonomy — it schedules, it wakes, it fires on cadence, the dashboard is green —
and then requires operator attention at per-tool, per-conversation granularity.
**The autonomy is theater.** An architectural attention-tax the operator cannot
walk away from, levied once per fire, forever.

**Substitute — arm-time global pre-authorization** (golden path §12, R14–R18):

1. **R15 scope floor.** Per-conversation consent is definitionally incompatible
   with a loop — every fire opens a new conversation, so consent never carries
   forward. Antigravity's option 2 ("always this conversation") *feels* like the
   fix and provably is not. **Option 4 or nothing.**
2. **R16 gate siting by effect class.** `hfo/board_status` is a **read**. HFO's
   genotype floor gates *world-effects* (send/spend/publish/seal/git-push). A
   read gated at world-effect strength is not caution, it is miscategorization —
   and it spends the entire safety budget on `board_status` while training the
   operator to click "always allow" reflexively, weakening the gates that matter.
3. **R17 timeout + failure policy.** No unbounded waits unattended. A blocked
   loop must emit a **FAILED receipt**, converting invisible silence into an
   alarmable row.
4. **R18 concurrency reaping.** One in-flight instance per loop; ≥3 overlaps →
   breaker OPEN. Twelve accumulated windows is an unbounded leak an OTP
   supervisor would have escalated at three.
5. **§12.3 step 3 — probe it.** Fire once unattended and confirm a receipt lands
   with no dialog. A configuration *believed* set is grade `A`; a fire that
   *completed* unattended is grade `D`.

- cost: **~0 lines. One configuration click per substrate**, plus the §12.3
  verification fire
- fidelity: **total** — this is fully substitutable
- **the sharpest fact in this document:** D9 is simultaneously the
  **cheapest-to-fix** of the nine functions and the one **blocking everything
  else**. Every gate, receipt, validator, and reconciler in the golden path is
  worthless on a substrate whose loops halt at first tool call. There is no point
  building D1's absence-detector to watch loops that structurally cannot complete.

**Roster implication.** §12.3 is a **substrate qualification**, not a per-task
one. Any substrate that cannot offer a conversation-outliving authorization
scope is **structurally NUDGE-class and cannot host a loop at all** — that is a
roster finding (which apex sits on which substrate), not a config fix. Nidhöggr's
planned migration to Antigravity (`apex_roster.v0_3`, ⭐ migration priority 1)
**must not proceed until §12.3 passes on Antigravity.** Migrating an apex onto an
unqualified substrate converts a working apex into a nudge generator.

---

### D8 · REPAIR AUTHORITY — someone is allowed to change the rules

**What the operator does.** IMMUNIZE. Ratifies roster changes, promotes canon.

**Substitute — none, and correctly so.** This is the deliberate propose/dispose
split (`C:\Dev\CLAUDE.md` RBR #3). Agents propose contracts; the operator
disposes. What *can* be automated is making disposal cheap: a single queue of
pending IMMUNIZE decisions with cost-of-delay attached, so the operator's scarce
authority is spent on decisions rather than on discovery.

- fidelity: intentionally zero; **optimize the interface, not the function**

---

## §2 · Summary table

| # | operator function | substitutable | mechanism | cost | catches |
|---|---|---|---|---|---|
| D1 | attention (absence) | ✅ high | expected_writes + reconciler + off-host DMS | ~80 ln | E1, E2, E4 |
| D2 | continuity | ✅ med-high | forced-read **query**, not file | ~30 ln | E3, E7 |
| D3 | kill-switch | ✅ high | breaker on evidence-grade collapse | ~50 ln | the spiral itself |
| D4 | ground truth | 🟡 medium | probe-before-claim + ground_truth.jsonl | ~20 ln | E8 |
| D5 | arbitration | ✅ detect / 🟡 resolve | single-writer canon + collision andon | ~40 ln | E4, roster |
| D6 | launching | ✅ high (invert it) | R5 no-registration-without-expectation | ~10 ln | E5, 124:0 |
| D7 | taste / priority | ⛔ **none** | — | — | — |
| D8 | repair authority | ⛔ by design | make disposal cheap | — | — |
| **D9** | **consent (click yes)** | ✅ **total** | **arm-time global pre-auth + effect-class gate siting + timeout/failure-policy + reaping** | **~0 ln, 1 click** | **E9 — 12+ stalled Antigravity sessions; the halt, not the drift** |

**~230 lines of boring code plus one configuration click substitutes for seven
of the nine functions.**

**Build order changed by E9.** D9 goes first. It is the only function whose
absence causes a *halt* rather than a *drift*, and the only one that costs
essentially nothing to substitute. Building D1's absence-detector to watch loops
that structurally cannot complete is instrumentation on a corpse.

The reason this has not been built is not that it is hard. It is that effort went
into *describing* the failures (8 registered classes, 19 L-vectors, multiple
audit documents) rather than *refusing* them. Description is the pleasant half of
the work and it produces artifacts that feel like progress.

---

## §3 · The real diff, in one line

> Operator presence supplies **consent at every tool call**, a **verification and
> absence-detection service at rate ~1**, plus **arbitration** and **taste**.
> Autonomy removes the first three while keeping generation at rate ~124 — and
> because consent (D9) is *synchronous and blocking*, its removal does not slow
> the system down, it **stops it**, silently, at the first tool call of every
> fire.

Two distinct failures, and they must not be conflated:

| | mechanism | symptom | fix |
|---|---|---|---|
| **the halt** (D9) | consent is synchronous, per-conversation, unbounded | loops fire and never complete; 12 dead windows | one click + §12 |
| **the drift** (D1–D5) | λ ≫ μ; queue contents indistinguishable from verified facts | confident wrongness compounding | ~230 lines |

**And the coupling is what makes it a spiral:** the halt produces *silence*; the
drift converts silence into *content*. A dispatcher polling a stalled session
sees nothing, must report something, and — with no field distinguishing *"I
verified nothing happened"* from *"I have no information"* — fabricates a
plausible account. That is exactly how this session's world-state capsule ended
up with two dispatches marked *"still RUNNING, nothing on disk"* (G2, G3), and
exactly how the *"rewrite deployed successfully"* hallucination was produced.

**Fix the halt first.** Little's Law does not apply to a queue whose server was
never started.

Little's Law, applied to claims. The fix is not a faster verifier — a human
cannot be made faster. The fix is (a) mechanize the verifier for the machine-
checkable majority, and (b) **type the queue** so unverified items cannot be
mistaken for verified ones while they wait (golden path R1/R3).

**(b) matters more than (a).** A typed backlog of honest `hypothesis` rows is
safe indefinitely. An untyped backlog corrupts canon in hours, because the only
thing distinguishing canon from assertion is having been written down.

---

## §4 · Honest flaws

- **F-A.** All substitutes are grade `A` — designed, never run. Fidelity ratings
  are estimates.
- **F-B.** D7/D8 being non-substitutable means "walk away" has a hard ceiling:
  autonomy can run *execution and verification*, not *direction*. If the
  operator's goal is walking away from direction too, this design does not reach
  it and no design in this document's scope does.
- **F-C.** D4's ground-truth file is operator-maintained — it re-introduces a
  human dependency at a slower cadence (weeks not minutes). That is the trade,
  and it should be named rather than hidden.
- **F-D.** The 230-line estimate excludes integration with 124 existing
  registrations. Retrofitting is likely the larger cost; **recommend retrofitting
  exactly one loop first** (see `plans/formalize_golden_path_pilot.md`) and
  measuring, rather than sizing the retrofit on heuristic —
  `L_BUDGET_WITHOUT_RECEIPT`.
