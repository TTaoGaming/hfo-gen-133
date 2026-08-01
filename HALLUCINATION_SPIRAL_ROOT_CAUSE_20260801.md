```yaml
# AIH2O capsule · conforms to contracts/capsule_schema_v0_1.md §3
doc: HALLUCINATION_SPIRAL_ROOT_CAUSE_20260801.md
schema_id: hfo.gen133.root_cause_analysis.v0_1
generation: 133
authored_by: SIGRÚN · P4 DISRUPT / O4 AUDIT · claude-opus-5 · ceiling=strategic (SPEC ONLY)
valid_time_utc:       2026-08-01T06:50:00Z
transaction_time_utc: 2026-08-01T06:50:00Z
git_head: 60893a4
claim_status: partial
sealed: false
subject: "root cause of recurring hallucination class in autonomous HFO operation"
evidence_grade_key: "[D] first-hand disk probe this session · [C] cited in-forge canon · [O] operator statement this session · [A] asserted, no receipt"
falsifiers_declared: 6
```

# HALLUCINATION SPIRAL — ROOT CAUSE

> Operator's question: *"hallucinations are spiraling even with UTC and world
> state rehydration capsules. what's the root cause?"*

---

## §0 · First: challenge the framing

**"Hallucinations are spiraling" is probably the wrong description of what is
happening, and the wrong description is itself load-bearing** — it points repair
effort at the agents (prompt harder, add headers, add capsules) when the defect
is in the institution around them.

Two competing descriptions of the same evidence:

| description | implies the fix is |
|---|---|
| **(a)** "agents got worse; hallucination rate is rising" | better prompts, more context, bigger models |
| **(b)** "hallucination rate is roughly flat; the ratio of *unverified claims that get read as facts* is rising" | verification throughput + typed evidence |

**The evidence favors (b), and it is not close.**

Per-turn error rate did not visibly change. What changed is that the institution
grew claim-**production** capacity by roughly two orders of magnitude — **124
scheduled task registrations** `[D]`, 8 ratified apexes, 16 valkyrie roles —
while claim-**verification** capacity stayed at exactly **one** unit: the
operator. Every hallucination in the session log was caught by the operator or
by a sibling agent that the operator dispatched. **Zero** were caught by a
machine gate.

This distinction matters because (a) has no cure — you cannot prompt an LLM into
being reliably right about unobserved world state — while (b) has a boring,
well-understood cure that this forge has already half-built.

---

## §1 · Priors

Stated before looking at the evidence, so the update is honest:

| # | prior | P |
|---|---|---|
| P1 | Rehydration compression is lossy; capsules drop facts → agents fill gaps | 0.30 |
| P2 | Individual-agent reflex-before-reasoning (RBR); System-1 commits tokens first | 0.25 |
| P3 | Verification loop absent; nothing machine-checks claims | 0.20 |
| P4 | Inter-agent coordination: agents read each other's unverified output as fact | 0.15 |
| P5 | Canon is underdetermined; agents must guess where there is no fact of the matter | 0.10 |

---

## §2 · Evidence gathered this session

All probes run 2026-08-01 ~06:40–06:50Z against live disk.

### E1 — The three "fixed" hourly loops have never produced a single row `[D]`

The 2026-07-31 rewrite of the three hourly SKILL.md files is real and correct in
shape: in-process, no `mcp__dispatch__*`, bounded, with an explicit
`SILENT DRIFT PROHIBITION` clause. Each mandates a write:

- `olrun-cop-hourly/SKILL.md` step 6 → `$FORGE/state/ssot/olrun_cop_hourly.jsonl`
- `sigrun-apex-opus5-hourly/SKILL.md` step 5 → `$FORGE/state/ssot/sigrun_apex_4h.jsonl`
- `valkyrie-pack-sonnet5-hourly/SKILL.md` step 4 → `$FORGE/state/ssot/pheromones.jsonl`

Probe: `find` for each filename across **both** `hfo_gen_130_forge` and
`hfo_gen_133_forge`, excluding `.git`.

**Result: all three files do not exist. Anywhere. Zero bytes ever written.**

This is the single most important fact in this document. Not "the rows are
wrong" — *there are no rows*. The loops have been registered, described,
documented, audited, and rewritten. They have never produced output.

### E2 — The andon cord is chmod-cut `[D]`

`olrun-cop-hourly/SKILL.md` step 7 is the escalation path: on `health==CRITICAL`,
append to `$FORGE/state/ssot/andon_pulls.jsonl`. That file in gen-130 is:

```
-r--r--r-- 1 tommy 197609 21808 Jul 31 17:34 andon_pulls.jsonl
```

**Read-only** — set by the kernel_guard pass. And in gen-133 the file **does not
exist at all** (`ls state/ssot/ | grep -i andon` → empty).

So: even a perfectly-compliant agent that correctly detects CRITICAL **cannot
pull the andon**. The one path designed to reach the operator is physically
blocked in one forge and absent in the other. The escalation channel was never
tested end-to-end after the kernel_guard hardening.

### E3 — The cron surface points at the wrong forge and is outside version control `[D]`

All three SKILL.md files set `FORGE=C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge`
while declaring `generation=133`. The files live at
`C:/Users/tommy/OneDrive/Documents/Claude/Scheduled/*/SKILL.md` — **outside the
forge, outside git**.

Gen migration is a `git`-shaped operation. The cron surface is a
filesystem-shaped, unversioned, OneDrive-synced surface. **No migration
mechanism reaches it**, so it silently retains the previous generation's target
forever. `git log` shows a clean gen-133 migration; the machine that actually
wakes up still lives in gen-130.

### E4 — The failure-class canon is triple-sourced and non-authoritative `[D]`

| source | content | count |
|---|---|---|
| root `C:\Dev\CLAUDE.md` L-vector table | behavioral refusals (L-SJÁLFS-SKÁLD, L30–L34, …) | **19** |
| `hfo_gen_130_forge/state/ssot/failure_class_registry.jsonl` | empirical detections, `failure_class_id` + `detected_utc` | **8** |
| gen-133 forge | **file absent entirely** | **0** |

The registry did not migrate to gen-133. `find /c/Dev/hfo_gen_133_forge -name
"failure_class*"` → nothing.

This is the direct generator of the "6 vs 19 failure classes" incident. There is
**no fact of the matter** about how many failure classes exist. Two different
ontologies (behavioral refusal vectors vs. empirically detected failure classes)
share a colliding name, live in two forges, one of which is stale and one of
which lacks the file. An agent asked "how many failure classes are registered?"
is being asked an underdetermined question, and it does what LLMs do with
underdetermined questions: it produces a plausible number.

**That is not a hallucination in the interesting sense. That is the institution
declining to have a fact, and the agent supplying one.**

### E5 — The failure class describing this exact situation was already registered, and changed nothing `[D]`

Row 6 of `failure_class_registry.jsonl`:

> `ROSTER_REGISTRATION_WITHOUT_ACTIVATION` — *"An institution grows its registry
> of named capabilities far faster than its set of activated ones…"*
> detected 2026-07-31T06:00Z.

Twenty-four hours later there are **124 scheduled registrations and 0 producing
rows** `[D]`. The class was correctly named, correctly written down, and had
**zero causal effect on the system**.

Corollary, and it deserves to be canon: **registering a failure class is not a
control.** A registry entry is a description. A control is something that
*refuses a transition*. HFO has been accumulating descriptions and calling them
defenses.

### E6 — The rehydration capsules are actually good `[D]` — evidence AGAINST P1

I expected to find lossy, over-compressed capsules. I did not.
`capsules/world_state/WORLD_STATE_CAPSULE_20260801T_LOGO_100APPS_FACTORY.md`
declares 5 explicit gaps (G1–G5), stamps convergence as **"2 of 4"** rather than
implying synthesis it did not perform, and already carries an
`evidence_grade_key` distinguishing `[F]etched / [S]earch / [D]isk / [C]anon /
[A]sserted`. `state/operator_preferences_manifest.md` opens with *"⚠️ This file
was CREATED, not updated"* and marks 4 of 5 sections `NOT_DERIVED` rather than
inventing operator preferences.

These are exemplary artifacts. Compression is **not** the bottleneck. P1 must be
sharply demoted — and this is the most useful thing adversarial-Bayes bought us
here, because "write better capsules" was the intuitive next move and it is the
wrong move.

But note what E6 *also* shows: the evidence-grade vocabulary **already exists in
this forge**, as prose convention inside one document, applied by one agent, at
that agent's discretion. It is not a schema field. It is not validated. It does
not survive into the JSONL rows other agents read.

### E7 — Read surface is recency-biased at 13 MB `[D]`

`hfo_gen_130_forge/state/ssot/lane_returns.jsonl` is **13,278,788 bytes**. Every
wake protocol reads it with `tail -n 20` or `tail -n 50`. A tail of a 13 MB
append-only log is a *recency sample*, not a state read. Any fact older than the
last few dozen rows is structurally invisible to every scheduled agent, forever.
The system's working memory is therefore ~20 rows deep regardless of how much
history it has accumulated. **Capacity amnesia is architecturally guaranteed.**

### E8 — Operator ground truth contradicted an unprobed causal claim `[O]`

The "laptop slept overnight" hallucination: the agent had `lastRunAt` timestamps
showing 17–20h gaps, and emitted a *causal* claim — "Windows Task Scheduler
doesn't fire while the machine sleeps" — sourced from training-era knowledge, not
from a probe. Operator: the laptop runs 24/7. The claim was falsified by one
sentence of ground truth the agent never asked for and could have asked for.

Note the shape: the **observation** (gaps exist) was evidence-grade `[D]`. The
**cause** was evidence-grade `[A]`. They were emitted in the same breath, in the
same register, with the same confidence, and nothing in the pipeline
distinguished them.

### E9 — Antigravity: the loops fire, then stall on a permission dialog `[O]` `[D]`

**Landed after §1–§3 were written. It moved the ranking.**

Operator screenshot, 2026-08-01: Antigravity IDE, **12+ Nidhöggr conversation
windows** open in the Projects sidebar, **each stalled on the same modal**:

> *"Allow using this MCP tool? `hfo/board_status`"* — 1) this time · 2) always this
> conversation · 3) always this project · 4) always allow · 5) No

The active conversation shows **"Waiting for user input.."** after the tool call.
Blocked at *first tool use*.

Operator verdict, verbatim: *"antigravity seems to be broken, lots of nidhoggr
windows open, all of them stalled with questions, so these are not loops. these
are just nudges."*

Four things follow, and each is load-bearing:

**(i) The scheduler is not the defect.** These fired. On cadence. Correctly. The
loop broke *after* wake, at authorization. Anything that "fixes the scheduler"
addresses the wrong layer.

**(ii) A stalled session is byte-identical to a session that never fired.** From
the artifact store's view: no rows, no receipt, no error, exit code nothing. This
is the single strongest confirmation of **H_new** in the document — 12+ sessions
accumulated over days, and the detector was *the operator's eyeball on a
sidebar*. No machine in HFO can distinguish "stalled" from "never ran" from
"ran and had nothing to say," because all three produce the same silence.

**(iii) It retrodicts G2 and G3.** The world-state capsule recorded
`local_4f13b00b` (heritage mining) and `local_35e95836` (reskin executor) as
*"nothing on disk… Session still RUNNING"* `[C]`. **"Still RUNNING" is exactly
how a permission-stalled session presents.** A hypothesis introduced to explain
Antigravity also explains two previously-unexplained gaps in a document written
before it. That is retrodiction, and it is worth more than fit to the evidence it
was invented for.

**(iv) It reframes the "timeout" diagnosis.** All three rewritten hourly
SKILL.md files assert: *"Do NOT call `mcp__dispatch__*` or
`sigrun_proprioception` — both timeout."* Given E9, **"timeout" is what a
permission stall looks like from inside an agent that cannot see the dialog.**
The prior session diagnosed a transport failure and prescribed removing the MCP
calls. If the real defect was authorization scope, that prescription treated a
symptom — and would explain why the rewrite was shaped correctly (E1 confirms
the prompts are right) and *still produced zero rows*: the in-process rewrite
still calls `Bash` and `Write` on first step, which are themselves
permission-gated surfaces.

Supporting probe `[D]`: 11 of 124 scheduled SKILL.md files reference MCP tools.
Session-directory accumulation: 271 (gen-131), 64 (gen-130), 24 (gen-133).

**Failure class — naming note.** The operator proposed
`L_SCHEDULER_FIRES_PERMISSION_STALLS`. I recommend **not** using the `L_` prefix,
per this document's own §8/R13 argument: `L_` denotes a *behavioral refusal
vector* — something an agent must decline to do. Nothing here is agent
misbehavior; the agent obeyed correctly and waited. This is an **incident
class**, empirically detected, and belongs in the incident registry:

- **`SCHEDULED_FIRE_WITHOUT_LOOP_CLOSURE`** *(incident class)* — a loop wakes on
  cadence but cannot complete without synchronous human authorization, so
  scheduled execution degrades to a queue of nudges. Fire ≠ completion.
- **`L-FIRE-COUNTED-AS-COMPLETION`** *(paired behavioral vector, for dispatchers)*
  — do not treat "the task fired" or "the session is RUNNING" as evidence of
  work performed. Only a receipt is evidence.

Registering the operator's insight under two names in two ontologies is not
pedantry — collapsing them is precisely the collision that produced the
"6 vs 19 failure classes" incident (E4).

**(v) The permission model is mis-sited, not too strict.** `hfo/board_status`
is a **read**. HFO's own genotype floor gates *world-effects*:
send/spend/publish/seal/git-push `[C]`. Antigravity applies a world-effect-grade
gate to a status read, at per-conversation scope, at fire time, **with no
timeout and no safe default**. Every mature admission system has
`timeoutSeconds` + an explicit `failurePolicy`; a gate that blocks forever is
not a safety mechanism, it is a **liveness bug wearing a safety costume**. And
the fix is one click — option 4 — which makes this the cheapest-to-repair defect
in the entire document and simultaneously the one blocking everything.

**(vi) Nobody bounded the concurrency.** Twelve-plus dead windows accumulated.
An OTP supervisor would have hit `max_restarts` within `max_seconds` and
escalated after three. Nothing reaped, nothing counted, nothing complained.

---

## §3 · Posteriors

| # | hypothesis | prior | evidence | posterior |
|---|---|---|---|---|
| **H_new** | **Negative-evidence blindness: nothing in the system observes absence** | — | FOR: E1, E2, E4, and decisively **E9** (12+ stalled sessions, days, detected by eyeball) | **0.34** ▲ |
| **H3** | **No verification loop: claims are not typed by evidence grade, so unverified claims are read back as facts** | 0.20 | FOR: E1, E2, E5, E6, E8. Still the truthfulness driver, but now shares causal load with H6 | **0.30** ▼ |
| **H6** | **Loop-closure failure: substrates advertise autonomy but require synchronous human authorization at fine granularity, so "loops" are nudges** | — *(new, E9)* | FOR: E9 directly `[D]`; retrodicts G2/G3; reframes the "MCP timeout" diagnosis in all 3 SKILL.md | **0.22** ✦ |
| **H5** | **Underdetermined canon: multiple non-authoritative sources for the same concept** | 0.10 | FOR: E4, E3 — directly generates the observed apex-name and failure-count incidents | **0.10** |
| **H2** | RBR / individual reflex | 0.25 | FOR: E8 shape. AGAINST: constant across time; does not explain the *increase* | **0.03** |
| **H4** | Inter-agent coordination | 0.15 | folded into H3 — coordination is only dangerous *because* claims are untyped | **0.01** |
| **H1** | Rehydration compression lossy | 0.30 | **AGAINST: E6.** Capsules are honest, gap-declaring, evidence-graded | **0.01** |

### §3.1 · The ranking reversed — two coupled families, not one cause

E9 forces a restructure I did not anticipate. The hypotheses are not competing
explanations of one phenomenon; they are **two families with a directed
coupling**, and the new evidence moved the dominant one.

| family | hypotheses | mass | failure mode |
|---|---|---|---|
| **B · LIVENESS** — work does not complete, and nothing notices | H_new + H6 | **0.56** ▲ | silence |
| **A · TRUTHFULNESS** — claims are untyped, unverified, and integrate | H3 + H5 | **0.40** ▼ | confident wrongness |

**The coupling, and it is the whole mechanism:**

```
Family B produces ABSENCES  →  Family A converts absences into CONTENT
```

A stalled or silent loop produces no receipt. The dispatcher must nonetheless
report status. With no field distinguishing *"I verified nothing happened"* from
*"I have no information,"* the dispatcher **fills the gap with a plausible
account**. That is not a metaphor — it is the precise mechanism of this session's
own *"rewrite deployed successfully"* hallucination (E8), and of the world-state
capsule's G2/G3 gaps.

**Family B is upstream.** You cannot verify what never ran. Fixing truthfulness
gates on a system whose loops do not close yields a well-typed record of nothing.

This is a genuine correction to §3 as first written, where H_new was labeled a
"supporting defect" subordinate to H3. **It is not subordinate; on the current
evidence it is primary.** The practical consequence is that the pilot's P1 phase
(reconciler running against a still-broken loop) is now the *main event* rather
than instrumentation, and the loop-closure invariant (golden path §12) moves
ahead of the validator in build order.

### The single-sentence root cause (revised after E9)

> **HFO scaled claim-production ~100× while claim-verification stayed at 1 (the
> operator); its loops do not close without synchronous human authorization; and
> nothing observes absence — so loops fire without completing, the silence is
> invisible, and the artifact store has no type distinction between a verified
> claim and an asserted one, so downstream agents fill the silence with plausible
> content that then reads as canon.**

Three clauses, three mechanisms, three fixes: **close the loops** (§12
pre-authorization), **observe the absence** (§3 reconciler), **type the claims**
(§1 evidence grade). In that order.

The two supporting structural defects:

1. **Negative-evidence blindness (H_new).** Every monitoring surface in HFO is a
   *positive-evidence* surface: it reads rows that exist. Nothing asks *"which
   loop was supposed to write and did not?"* Absence is the system's blind spot,
   and absence is exactly what failure looks like here — E1, E2, and E4 are all
   absences, all invisible, all lasting days.

2. **Underdetermined canon (H5).** Where the institution declines to have a
   single authoritative fact, the agent must supply one. It always will. Every
   duplicated, unmigrated, or split registry is a **hallucination generator**
   with a predictable output rate.

### Why it is a *spiral* and not a constant error rate

This is the part the framing "hallucinations are spiraling" gets right, for the
wrong reason. It spirals because the error term is **integrated, not damped**:

```
claim_t  →  written to artifact store, untyped  →  read as input at t+1
```

Yesterday's `[A]`-grade assertion is today's `[C]`-grade canon, purely by virtue
of having been written down. There is no decay, no expiry, no re-verification,
and no field that would let a reader tell the difference. **This is a positive
feedback loop with gain ≥ 1 and no damping term.** Agent quality is the *input*
to that loop, not the loop itself — which is why better models, better headers,
and better capsules have not helped and will not help.

### What is NOT the root cause (say it plainly)

- **Not the model.** Opus-5 caught its own two hallucinations this turn once
  given ground truth. The information was retrievable; nothing required it to be
  retrieved.
- **Not missing UTC.** Every artifact examined has correct UTC. Timestamps
  answer *when*; they never answered *how do you know*.
- **Not missing capsules.** E6.
- **Not the scheduler bug.** That is one instance of E1/E3. Fixing the hardcoded
  path fixes three loops and leaves the generator intact.

---

## §4 · Falsifiers

State them so this document can be killed by evidence rather than argued with.

| # | claim | falsifier |
|---|---|---|
| F1 | Verification throughput, not agent quality, is the binding constraint | Add a mandatory evidence-grade field + validator to all emitted rows, change nothing else, and observe **no** reduction in operator-caught errors over 2 weeks |
| F2 | Nothing observes absence | Produce any existing artifact, script, or loop in either forge that alerts on a *missing* expected write. If one exists, H_new is wrong and this is a deployment failure, not a design gap |
| F3 | The three hourly loops have never produced a row | Locate `olrun_cop_hourly.jsonl`, `sigrun_apex_4h.jsonl`, or `pheromones.jsonl` with ≥1 row anywhere on this host |
| F4 | Underdetermined canon generates hallucination at a predictable rate | Consolidate the failure-class registries to one authoritative file, then ask 5 fresh agents "how many failure classes are registered?" — if answers still diverge, the mechanism is elsewhere |
| F5 | Capsule compression is not the problem (E6) | Find a session hallucination whose specific content is traceable to a fact **present** in the source and **dropped** by the capsule |
| F6 | Registration is not a control | Point to any registered failure class that has demonstrably prevented a recurrence, with a receipt showing the refused transition |
| **F7** | **E9 generalizes: the Claude Desktop hourly loops are permission-stalled, not un-fired** | Grant global pre-authorization for `Bash`/`Write` on `olrun-cop-hourly`, change nothing else, and observe whether rows appear. **Rows appear → H6 confirmed on this substrate. Still zero → the defect is upstream of authorization and H6 is Antigravity-specific.** Either result is decisive within 2 hours |
| **F8** | The permission gate is mis-sited (read-grade call, world-effect-grade gate) | Find a substrate whose permission model distinguishes read from world-effect and *still* stalls on `board_status`. Then the model is fine and the scope config is the defect |

**F7 is now the single highest-value probe in the document** and costs one click
plus a two-hour wait. Note carefully what it is *not*: E9 is grade `[D]` about
**Antigravity**. Applying it to Claude Desktop is grade `[A]` inference — a
raised prior, not a finding. Asserting "the hourly loops are permission-stalled"
without running F7 would be the exact error class this document was written to
diagnose (E8: correct observation, asserted cause, same register). **State it as
hypothesis; run the probe.**

**F6 is the important one.** If it cannot be satisfied for *any* of the 8
registered classes, then the entire registry apparatus is documentation, and the
institution has been mistaking documentation for defense for its whole life.

---

## §5 · Where the "laptop slept" error escaped — the machine-checkable gate

Traced precisely, because the operator asked for exactly this.

| stage | what happened | gate that would have caught it |
|---|---|---|
| observe | `list_scheduled_tasks` → 17–20h gaps. **Correct, grade `[D]`** | — (this stage was fine) |
| explain | training-prior retrieval → "scheduler doesn't fire when asleep". **Grade `[A]`** | ⛔ **none existed** |
| emit | observation and cause emitted in one register, indistinguishable | ⛔ **none existed** |
| verify | operator supplied ground truth | ✅ human, rate-limited, not scalable |

**The escape point is between `explain` and `emit`.** The gate is not "think
harder" — it is a *schema refusal*:

> A row asserting a **cause** must carry `probe_ref` (a command + its output
> hash) or be typed `evidence_grade: A` and rendered as `hypothesis`, never as
> `root_cause`.

This is machine-checkable in ~40 lines. It does not require the model to be
smarter; it requires the *store* to refuse an untyped causal claim. That is the
propose/dispose split from `C:\Dev\CLAUDE.md` RBR doctrine #3, applied at the
schema layer instead of the prose layer — which is the difference between
doctrine and a control.

Applied to the second hallucination ("rewrite deployed successfully"): the claim
`deployed=true` had no `probe_ref`. A validator requiring `probe_ref` for any
`status: deployed|wired|complete` would have forced the `Read` of the SKILL.md
files — which is exactly the action that revealed the gen-130 path bug. **The
gate does not just catch the error; it performs the investigation.**

---

## §6 · The uncomfortable implication

The forge has built, to a high standard: a bitemporal store, world-state
capsules, a failure-class registry, an L-vector table, chain receipts, kernel
guards, and 124 scheduled loops.

**Almost none of it refuses anything.**

The kernel_guard is the one component in the stack that genuinely enforces —
and its enforcement (read-only `andon_pulls.jsonl`) severed the escalation path,
undetected, because nothing observes absence. That is not an argument against
enforcement. It is an argument that **enforcement without a negative-evidence
monitor is how you get a silent, confident, dead system** — which is precisely
the state the operator is describing when they say autonomy produces
hallucination.

The institution is not short on doctrine. It is short on **refusals** and
**absence-detectors**. Two mechanisms, both boring, both ~100 lines each.

---

*Next: `contracts/anti_hallucination_golden_path.v0_1.md` (the refusals),
`contracts/manual_cpr_vs_autonomous_diff.v0_1.md` (what the operator is
substituting for), `plans/formalize_golden_path_pilot.md` (the 72h test).*
