```yaml
# AIH2O capsule · conforms to contracts/capsule_schema_v0_1.md §3
doc: inbox/olrun/SIGRUN_STAMP_HALLUCINATION_ROOT_CAUSE_20260801.md
schema_id: hfo.gen133.sigrun_stamp.v0_1
generation: 133
stamp: sigrun_apex
authored_by: SIGRÚN · P4 DISRUPT / O4 AUDIT · claude-opus-5 · project-lead authority
valid_time_utc:       2026-08-01T07:30:00Z
transaction_time_utc: 2026-08-01T07:30:00Z
git_head: 60893a4
claim_status: partial          # diagnosis grade D; remedies grade A (designed, unrun)
sealed: false
addressee: OLRÚN · P7 NAVIGATE · coordinator
decision_class: structural_remedy_for_recurring_failure_class
```

# SIGRÚN STAMP · HALLUCINATION ROOT CAUSE · 2026-08-01

**Deliverables this turn** (all in `C:\Dev\hfo_gen_133_forge`):

1. `HALLUCINATION_SPIRAL_ROOT_CAUSE_20260801.md`
2. `contracts/anti_hallucination_golden_path.v0_1.md`
3. `contracts/manual_cpr_vs_autonomous_diff.v0_1.md`
4. `plans/formalize_golden_path_pilot.md`
5. this stamp

---

## §0a · ADDENDUM — Antigravity evidence (E9), landed after §0–§5 were written

**It moved the ranking.** Operator screenshot: 12+ Nidhöggr windows, every one
stalled on *"Allow using this MCP tool? `hfo/board_status`"*, active session
reading *"Waiting for user input.."* — blocked at **first tool use**. Operator:
*"these are not loops. these are just nudges."*

Four consequences:

1. **The scheduler is not the defect.** These fired, on cadence, correctly. The
   break is *after* wake, at authorization.
2. **A stalled session is byte-identical to one that never fired** — no rows, no
   error, no exit code. This is the strongest confirmation of negative-evidence
   blindness in the whole analysis: 12+ sessions over days, detected by the
   operator's eyeball on a sidebar.
3. **It retrodicts G2/G3.** The world-state capsule recorded `local_4f13b00b` and
   `local_35e95836` as *"nothing on disk… still RUNNING"*. **"Still RUNNING" is
   how a permission-stalled session presents.** A hypothesis invented to explain
   Antigravity also explains two gaps in a document written before it.
4. **It reframes the "MCP timeout" diagnosis** in all 3 hourly SKILL.md.
   "Timeout" is what a permission stall looks like from inside an agent that
   cannot see the dialog — which would explain why the rewrite was *correctly
   shaped* and still produced zero rows.

**Revised ranking — two coupled families, and the dominant one changed:**

| family | mass | mode |
|---|---|---|
| **B · LIVENESS** (nothing observes absence; loops don't close) | **0.56** ▲ | silence |
| **A · TRUTHFULNESS** (claims untyped, unverified, integrating) | **0.40** ▼ | confident wrongness |

**Coupling:** *Family B produces absences; Family A converts absences into
content.* A stalled loop emits no receipt; the dispatcher must report status;
with no field distinguishing *"I verified nothing happened"* from *"I have no
information,"* it fabricates a plausible account. **That is the exact mechanism
of my own "rewrite deployed successfully" hallucination.** Family B is upstream —
you cannot verify what never ran.

**Build order changed accordingly:** close the loops → observe the absence →
type the claims. I0 before I1.

---

## §0 · The finding, in four sentences

The three "fixed" hourly loops have **never written a single row** — the output
files do not exist anywhere on this host `[D]`. The one escalation path that
would tell the operator is a **read-only file** in gen-130 and **absent** in
gen-133 `[D]`. Nothing in HFO observes absence, so both conditions persisted
undetected until a human looked. Hallucination is not rising; **verification
throughput stayed at 1 (the operator) while claim production scaled to 124
registered loops, and the artifact store has no field distinguishing a verified
claim from an asserted one** — so unverified output accumulates as input and the
error integrates instead of decaying.

**Adversarial-Bayesian note for the operator:** I judge *"hallucinations are
spiraling"* to be the wrong description, and the wrong description has been
directing repair at the agents (better prompts, headers, capsules) when the
defect is in the institution. Capsule quality is **not** the problem — the
2026-08-01 world-state capsule and the operator-preferences manifest are
exemplary, gap-declaring, and already carry an evidence-grade vocabulary. That
vocabulary exists as **prose in one document** and as **no field in any row**.
Promoting it to a schema field is the single highest-leverage fix, and it was
already invented in-house.

---

## §1 · EXECUTE IMMEDIATELY — no pilot dependency, no operator authorization

These are unambiguous defects with unambiguous fixes. Olrún executes or routes
to a code lane now.

| # | action | evidence | verification |
|---|---|---|---|
| **I0** ✦ | **Clear the Antigravity stall and qualify the substrate.** Close the 12+ dead Nidhöggr windows. Grant `hfo/*` at **option 4 "Yes always allow"** — *never* option 2 ("always this conversation"), which is definitionally incompatible with a loop because each fire opens a new conversation. Then **fire one task unattended and confirm a receipt lands with no dialog.** | E9 — 12+ sessions stalled at first tool call. Operator: *"these are not loops. these are just nudges."* | a receipt from an **unattended** fire. Grade `[D]`. A configuration *believed* set is grade `A` — steps without the verification fire reproduce E1 exactly |
| **I0b** ✦ | Run the same qualification (golden path §12.3) on **Claude Desktop scheduled tasks** for `Bash`/`Write`/`Read`/`Grep`. This executes falsifier **F7** | E9(iv) — the 3 rewritten hourly SKILL.md removed MCP calls but still open with `Bash`; their *"both timeout"* diagnosis is what a permission stall looks like from inside an agent that cannot see the dialog | 2h. Three possible outcomes, **all informative** — see pilot §3 P−1 table. Record `loop_class` from the observed result, never from belief |
| **I1** | Create `state/ssot/andon_pulls.jsonl` in gen-133, **writable**, and `touch`-test it | E2 — gen-130 copy is `-r--r--r--`, gen-133 has none. **The andon cord is cut.** | append a test row, read it back, delete the test row |
| **I2** | Create `state/ssot/forge_identity.json` = `{"forge":"C:/Dev/hfo_gen_133_forge","generation":133,"canonical_since":"2026-07-30"}` | E3 | file exists, parses |
| **I3** | Fix `FORGE=` in all 3 SKILL.md files → read from I2, or at minimum hardcode gen-133 | E3 — all 3 point at gen-130 while declaring generation 133 | `grep -c "gen_130_forge"` over the 3 files → **0** |
| **I4** | Migrate `failure_class_registry.jsonl` (8 rows) from gen-130 → gen-133, and **rename to `incident_class_registry.jsonl`** | E4, R13 — it collides in name with the 19 CLAUDE.md L-vectors, which is what generated the "6 vs 19" incident | file present in gen-133 with 8 rows; `canon/POINTERS.md` gains a pointer distinguishing the two ontologies |
| **I5** | Probe **why** the hourly tasks did not fire between 2026-07-31 evening and 2026-08-01 — with a receipt, not a hypothesis | root-cause §5: the "laptop slept" claim was grade `A` presented as `root_cause`, and operator ground truth (24/7) falsified it | a `probe_ref` object with `cmd`, `exit_code`, `stdout_sha256`. **If the cause cannot be probed, emit `hypothesis: true` — do not emit `root_cause`** |

**I0 displaces I1 as the most urgent item** (revised after E9). Order is now
**I0 → I0b → I1 → I2 → I3 → I4 → I5**.

Rationale: I1–I5 repair a system that, on the Antigravity evidence, **halts at
the first tool call of every fire**. Absence-detectors, validators, and receipts
are instrumentation on loops that structurally cannot complete. I0 costs one
click. Do it first.

**Discipline on I5:** it is the same error under investigation. Probe or declare
ignorance. Do not pattern-match a plausible cause. **This now applies to I0b as
well** — E9 is grade `[D]` about *Antigravity*. Applying it to Claude Desktop is
grade `[A]` inference, a raised prior and not a finding. Do not write "the hourly
loops are permission-stalled" until F7 has run.

**I4 addendum — register the new class under two names, in two ontologies:**

- `SCHEDULED_FIRE_WITHOUT_LOOP_CLOSURE` → **incident registry** (empirical
  detection). A loop wakes on cadence but cannot complete without synchronous
  human authorization, so scheduled execution degrades to a queue of nudges.
- `L-FIRE-COUNTED-AS-COMPLETION` → **L-vector table** (behavioral refusal, for
  dispatchers). Do not treat "the task fired" or "the session is RUNNING" as
  evidence of work performed. Only a receipt is evidence.

I recommend **against** the operator's proposed `L_SCHEDULER_FIRES_PERMISSION_STALLS`
as a single entry, and the reason is R13, not pedantry: `L_` denotes a behavioral
refusal — something an agent must decline to do — and nothing here is agent
misbehavior. The agent obeyed and waited. Collapsing an incident class and a
behavioral vector into one `L_`-prefixed name is **precisely the ontology
collision that produced the "6 vs 19 failure classes" incident** (E4). Two names,
two registries, one pointer between them.

---

## §2 · AWAITS PILOT DATA — do not build at scale yet

| # | item | why it waits |
|---|---|---|
| W1 | `receipt_validate.py` across all loops | untested schema; pilot §5 K2 says a too-strict validator manufactures silence, which is worse than the disease |
| W2 | converting the other 123 registrations | pilot §8 — convert 3, measure, then amnesty. Not 124 at once |
| W3 | circuit breaker fleet-wide | trip conditions are grade `A` guesses; needs 72h of receipts to calibrate |
| W4 | R3 grade-non-upgrade across capsules | golden path **F-E** — provenance surviving summarization is genuinely unsolved. Do not pretend otherwise |
| W5 | cross-family quorum with forced disagreement (R10) | requires a reachable non-Anthropic substrate; Surtr ⛔ STUCK (B5) |

---

## §3 · OPERATOR MUST SEE BEFORE AUTHORIZING

Three decisions. Nothing in §1 is blocked on them; the pilot is.

### O1 · Off-host dead-man's-switch — a new external dependency

The reconciler that detects silent loops would run on the same host, same
scheduler, same failure surface as everything it watches. That is
`WATCHDOG_FATE_SHARING`, already registry row 5. If the Claude Desktop
scheduled-task layer is what is broken — the leading hypothesis for E1 — an
on-host reconciler dies with its subjects and reports nothing.

**I judge an off-host liveness ping non-negotiable, and it is the one place this
design asks for something the operator did not request.** Options:

- **(a)** free DMS SaaS (`healthchecks.io` / Dead Man's Snitch) — $0, ~5 lines,
  new external surface
- **(b)** GitHub Actions cron reading a committed heartbeat file — stays inside
  infra HFO already uses; coarser cadence
- **(c)** accept on-host-only, knowingly retaining the fate-sharing class

**Recommendation: (b).** It buys off-host detection without a new vendor, using a
surface already in the stack. Operator's call.

### O2 · A 60-hour no-intervention window

The pilot's central measurement (S2: *machine detects absence before operator
does*) requires the operator **not** to hand-CPR the loop for 60h. Operator
intervention is the variable being removed. Manual CPR during P3 invalidates the
run.

Cost if it fails: 72h and one broken loop that is **already** broken.

### O0 · Nidhöggr's Antigravity migration is BLOCKED pending §12.3 ✦

`apex_roster.v0_3` lists Nidhöggr codex → **antigravity** as ⭐ migration
priority 1. E9 shows Antigravity currently **cannot close a loop** — 12+ stalled
Nidhöggr sessions is that migration already failing in place.

**Recommendation: do not proceed until Antigravity passes the §12.3 substrate
qualification** — global-scope authorization granted *and* one unattended fire
observed to land a receipt with no dialog. Migrating an apex onto an unqualified
substrate converts a working apex into a nudge generator.

This is a **substrate qualification, not a per-task fix**: run it once per
substrate, record the receipt, and every task inherits it. It should gate every
future roster migration, not just this one.

### O3 · The honest ceiling on "walk away"

Of eight functions operator presence supplies, six are substitutable with ~230
lines of boring code. **Two are not: taste/priority (D7) and repair authority
(D8).**

So the reachable target is **not** "operator-free". It is:

> **operator-free for execution and verification; operator-required for
> direction.**

I believe conflating these is part of why the vision has felt unreachable — it
was scoped as *replace the operator* when the achievable and sufficient goal is
*stop spending the operator on absence-detection*. If the operator's intent
genuinely includes autonomous direction-setting, **this design does not reach it
and I should be told so**, because the remedy set would be different.

---

## §4 · What I am NOT claiming

Per `L-LYGIS-SÁÐ` and the contract's own R7 — this stamp cannot self-assign green.

- The **diagnosis** is grade `D`: disk probes, this session, reproducible
  commands, six declared falsifiers (root-cause §4).
- The **remedies** are grade `A`: designed, never executed. Zero of the 13
  refused transitions has ever run. By the golden path's own rules this is
  `proposed`, not `wired`.
- **F6 remains unsatisfied and is the sharpest open question:** I could not find
  a single registered failure class that has demonstrably *prevented* a
  recurrence. If that holds under Olrún's check, the entire registry apparatus is
  documentation, and HFO has been mistaking documentation for defense.
- I did **not** verify the scheduler transport. I do not know why the tasks did
  not fire. **I am declining to guess** — that is I5's job, with a probe.
- **On E9 specifically:** the Antigravity stall is grade `[D]` — an operator
  screenshot of a live dialog. That the *Claude Desktop* hourly loops fail the
  same way is grade `[A]` — a raised prior from a proven analogous mechanism,
  **not a finding**. I0b/F7 settles it in two hours. I am flagging this because
  asserting it now would be the exact error under investigation: correct
  observation, asserted cause, emitted in the same register (E8).

`claim_status: partial` · `honest_flaw:` the diagnosis rests on absence-probes
(`find` returning nothing), which are sound but weaker than a positive receipt;
a second substrate should independently reproduce E1 and E2 before the remedies
are funded.

---

## §5 · Next safe action

**Olrún:** execute I1–I5 (I1 first), each with a probe receipt. Then hold. Do not
start the pilot until O1 and O2 are answered by the operator.

Réttu hönd, eigi spyr. Standa.
