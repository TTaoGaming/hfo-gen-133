```yaml
# AIH2O capsule
doc: state/patterns/EMERGENCY_FORGE_PATTERN_v1.md
schema_id: hfo.gen133.emergency_forge_pattern.v1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T04:38:55Z
clock_source: host_read
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md
builds_on: areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md (chain row 77)
ships_running_code: tools/verify_forge_dispatch.py · state/ssot/forge_dispatches.jsonl
claim_status: wired_with_receipts   # covers the probe only; §2-§7 are proposed
forge_id: F8
```

# EMERGENCY_FORGE PATTERN v1

**Operator's frame:** *internal fitness* = my system passes my own tests.
*External fitness* = the industry converges on this, a real buyer pays, a real
user returns. Twelve forges of internal fitness have produced zero external
fitness. This document exists to make the 13th different, and it is falsifiable.

---

## §1 — HISTORICAL SCAN

Measured, not recalled. `grep EMERGENCY_FORGE` hits **81 files**; most are the
*policy gate* citation ("do not author code unless the operator types
`verb=EMERGENCY_FORGE`"), not dispatches. Distinct dispatches, extracted into
`state/ssot/forge_dispatches.jsonl`:

| # | date (UTC) | what was built | external signal | receipt |
|---|---|---|---|---|
| G130-A | gen-130 | QD MAP-Elites population from apex_cots | **none** | `SIGRUN_HLUTI_COMPOSE.jsonl` |
| G130-B | gen-130 | policy_gate hardening | **none** | same; verifier_result = an exit code |
| G130-C | gen-130 | hardened gate adopted to main | **none** | same; `claim_status: partial` |
| G130-D | gen-130 | chain-corruption sweep + HEAD/main triage | **none** | same |
| F1 | 07-31 17:48 | outreach class pre-auth (`render_message.py`, `kill_switch.py`) | **none** | BUILD_RECEIPT: *"No email has been sent… No network call was made by any script in this build."* |
| F2 | 07-31 19:55 | warm-network income lane | **none** | chain row 17: *"first artifact today that **can** end with money"* |
| F3 | 07-31 20:35 | Upwork proposal engine (`render_proposal.py`) | **none** | BUILD_RECEIPT: *"No proposal has been submitted to Upwork. No Upwork account exists as of this build."* |
| F4 | 08-01 18:06 | kill reward-hacker + acceptance runner | **none** | chain row 49; `task_results.jsonl` = **0 bytes** |
| F5 | 08-01 18:15 | `lineage_lease.py` + OPA gate | **none** | chain row 52 |
| F6 | 08-02 04:26 | `tools/factory/` distribution factory v0 | **none yet** | chain row 78; 2 of 3 feeds DEAD at build time |
| F7 | 08-02 04:16 | capability census | n/a — correctly marked internal | census output |
| F8 | 08-02 04:38 | *this document* | n/a — internal | this file |
| F9 | 08-02 04:46 | STACK BUILDER v0 (`crewai_demo.py`) — **landed mid-scan** | **none** | flipped `cap-crewai-runtime` ALIVE; see §7 |

```
TOTAL forges=13  external_signal=0  base_rate=0%
PATTERN DEAD (>=3 forges, 0 external signal, 30-day ban): internal-mechanism-build
```
— `python tools/verify_forge_dispatch.py`, run this turn. **F9 was discovered by
the census while this document was being written**, and registered retroactively.
Thirteen forges. Zero external signals. Not one.

The only ALIVE external-facing capability is `cap-deploy-live` (`http=200`), and
reachability is not a visitor. `cap-outreach-instrument` is a `FileNotFoundError`.

### Repeating pattern-errors

**E1 — the same disclaimer, written twice, 24 hours apart.** F1 and F3 were both
sonnet-5 code lanes. Both shipped a near-identical paragraph: *"`wired_with_receipts`
for the enforcement mechanism only… No network call was made by any script in
this build."* Neither cited the other. **That duplication is the institutional
memory loss, visible in prose.** The second forge did not know the first had
already discovered that an envelope without a channel produces nothing.

**E2 — channel-less envelope.** F1 and F3 built refusal machinery for outreach
channels **that had no account**. The enforcement was real; there was nothing to
enforce against.

**E3 — mechanism displaces effect.** 5 of 12 forges are `internal-mechanism-build`.
Zero external signal in aggregate. Under §4 this class is now **DEAD**.

**E4 — build preceded scan.** F2 named warm-network the #1 income path and built
the artifact; 25 minutes later chain row 19 recorded a self-CORRECTION — a sibling
carrier had andon'd warm-network **twice that same day**. The forge outran its own
institutional memory by 25 minutes.

**E5 — queue seeded, never drained.** F4's acceptance was "queue seeded." It was.
`state/ssot/task_results.jsonl` is 0 bytes; `cap-queue-consumer` reads DEAD.

All five reduce to Sigrún's root cause (chain row 77): **the acceptance predicate
ranged over the document corpus, not over the world.**

---

## §2 — INDUSTRY-PATTERN GATE

Before dispatch, every EMERGENCY_FORGE must name **≥3 industry sources with URLs**.
The verifier refuses fewer. The four anchors this pattern is assembled from:

1. **Blameless postmortem, mandatory after any significant incident** — Google SRE
   ([sre.google/workbook/postmortem-culture](https://sre.google/workbook/postmortem-culture/)),
   productized by [incident.io](https://incident.io/blog/sre-incident-postmortem-best-practices)
   and [Rootly's 2025 checklist](https://rootly.com/sre/2025-sre-incident-management-best-practices-checklist).
   → §6.
2. **Error-budget policy: freeze feature launches when the budget is exhausted**,
   with narrow "silver bullet" exceptions — Google SRE
   ([sre.google/workbook/error-budget-policy](https://sre.google/workbook/error-budget-policy/),
   [implementing-slos](https://sre.google/workbook/implementing-slos/)). → §4.
3. **Write the external artifact before the internal one** — Amazon Working
   Backwards PR/FAQ ([workingbackwards.com](https://workingbackwards.com/concepts/working-backwards-pr-faq-process/)).
   If you cannot state why a customer cares before it exists, do not build it. → §3.
4. **Pre-registration defeats HARKing** (hypothesizing after results are known) —
   OSF / AsPredicted / ClinicalTrials.gov practice
   ([arxiv.org/pdf/2010.10513](https://arxiv.org/pdf/2010.10513),
   [DataCamp on HARKing](https://www.datacamp.com/blog/harking)); carried into
   product experimentation by Kohavi/Tang/Xu's OEC
   ([Trustworthy Online Controlled Experiments](https://www.amazon.com/Trustworthy-Online-Controlled-Experiments-Practical/dp/1108724264)).
   **Kill criteria = a measurable state + a date, decided in advance** — Annie Duke
   ([charterworks.com/quit-annie-duke](https://www.charterworks.com/quit-annie-duke/),
   [@AnnieDuke](https://x.com/AnnieDuke/status/1579891488221061120)). → §3, §4.

**If a proposed forge cannot cite 3+ named 2024-2026 adopters: STOP.** Do not
EMERGENCY_FORGE a novel pattern. Choose one: (a) wait for convergence,
(b) run a ≤30-minute experiment instead of a forge, or (c) set
`internal_fitness_only: true` with a `retirement_condition` — an honest admission
that no external signal is expected. The verifier accepts (c) and refuses silence.

**The 3+ bar is the right bar, corroborated independently this hour.** A sibling
sonnet-5 lane shipped `state/industry_patterns/INDUSTRY_PATTERN_CONVERGENCE_20260802.md`
(chain row 82, 04:42Z) applying the same ≥3-named-winners test to 2024-2026 agent
companies. It found convergence on *"build your own thin orchestration layer, skip
CrewAI/LangGraph/AutoGen"* (7 of 9 coding winners) — and, when the bar was **not**
met for anti-patterns, said so and downgraded the claim instead of padding it.
**Two lanes, same hour, same bar, one honest failure to meet it: that is the gate
working.** Cite that document as the standing source for pattern-anchor lookups.

**Deviation from baseline, declared:** SRE's postmortem trigger is an *incident*;
here it is a *dispatch*, because the failure mode is an unremarkable success that
produced nothing, and those generate no incident. **This inverts the trigger from
"something broke" to "something shipped."**

---

## §3 — EXTERNAL-FITNESS ACCEPTANCE CRITERIA

Pre-registered, machine-checked, written **before** work starts:

- **Signal type** — one of: `revenue` · `user` · `download` · `star` ·
  `deploy-view` · `reply` · `citation` · `reference`. Every one requires a party
  who is not the operator and not an agent.
- **Threshold** — an integer ≥ 1. `"some"` is refused by the verifier.
- **Window** — an ISO-8601 expiry date. `"soon"` is refused.
- **Kill-switch** — the named consequence when the window closes below threshold.
  Empty string is refused.

Duke's rule is exactly this: *state + date, decided in advance.* The reference
implementation is the factory's: **"one named human states a price or a date by
2026-08-16."** Not "the factory works." Not "the batch queued."

A build-time exit code is never an external signal. Neither is a file, a passing
test, a green census row, or this document.

---

## §4 — STOP-IF-Nth-ATTEMPT-NO-SIGNAL

Aggregated per `pattern_class` by the verifier, automatically:

| aggregate | verdict |
|---|---|
| **≥3 forges, 0 external signal** | **PATTERN DEAD.** 30-day ban on the class. |
| **1 signal in 3** | **CONTINUE**, with escalating specificity — narrow the audience, do not broaden the build. |
| **consistent signal** | **SCALE.** |

This is the error-budget freeze: when the budget is gone, launches stop. SRE
allows narrow **silver bullets** for business-critical exceptions; the analogue
here is that a banned class may still be forged if the operator types
`verb=EMERGENCY_FORGE_OVERRIDE` **and** the ledger row records the override and
its justification. The ban is a speed bump with a name, not a wall.

**Fired on the first run:** `internal-mechanism-build` — 6 forges, 0 signal —
**banned until 2026-09-01.**

**Rule defect found and fixed while writing §9.** Registering F10 made
`internal-instrument` a 3-forge class and the rule **banned my own instrumentation
class** — including the census. That is a bug, not a finding: `internal_fitness_only`
forges are exempt from external tests *by construction*, so counting them toward the
ban would ban all instrumentation forever. **Fix:** a class is ban-eligible only if
≥1 forge in it was expected to produce external signal; internal-only classes are
governed by their own `retirement_condition` instead. Because that exemption is also
an escape hatch, the verifier now prints a **WARNING when internal-fitness forges
exceed 50% of all forges** — E3 stated out loud. Currently 3/14 = 21%.

---

## §5 — REPEATABLE TEMPLATE

Paste into the dispatch prompt. Then append the matching row to
`state/ssot/forge_dispatches.jsonl` **before** work begins.

```
EMERGENCY_FORGE {name} — {model}, {timebox}, {register}

**Industry-pattern anchor:**
- Baseline from: {3+ named winners, each with a URL}
- Deviation from baseline: {explicit + justified}

**External-fitness acceptance test:**
- Signal type: {revenue|user|download|star|deploy-view|reply|citation|reference}
- Threshold: {integer >= 1}
- Window expires: {ISO-8601}
- Kill-switch: {what happens at expiry below threshold}
  (or: internal_fitness_only: true + retirement_condition: {...})

**Pattern class:** {slug, must match the ledger}
**Historical N for this class:** {integer, from verify_forge_dispatch.py}
**Base rate of external signal for this class:** {percentage, from the same run}
**Kill-if-Nth trigger:** {condition}

**Rehydration read-order-0:**
1. state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md
2. state/patterns/EMERGENCY_FORGE_PATTERN_v1.md  (this file)
3. state/forge_post_mortems/*_{pattern_class}_*.md  (every prior forge in class)

**Runtime probe:** cap-emergency-forge-pattern-compliance
```

Ledger row shape — copy `F6` in `forge_dispatches.jsonl`. Then:

```
python tools/verify_forge_dispatch.py   # must exit 0 before work begins
```

---

## §6 — INSTITUTIONAL MEMORY MECHANISM

Three obligations, in order:

1. **READ first.** Before dispatch, read every post-mortem in
   `state/forge_post_mortems/` whose filename carries this `pattern_class`.
   This is the specific cure for E1 and E4.
2. **REGISTER before.** Append the ledger row and run the verifier to exit 0.
   Registration before work is what makes the acceptance test un-HARKable.
3. **POST-MORTEM after.** Write `state/forge_post_mortems/{YYYYMMDD}_{pattern_class}_{name}.md`
   — blameless, per Google SRE. Required sections: what was built · what external
   signal was pre-registered · what arrived · **which prior post-mortem in this
   class you read, by filename** (naming "none" is a permitted and damning answer)
   · what the next forge in this class must not repeat.

Chain-row every dispatch with `forge_pattern_class` so the census can aggregate.
The filename carries the class so that step 1 is a `glob`, not a judgment call.

---

## §7 — WHAT TO KILL

Adversarial pass over everything currently live:

| activity | industry anchor | external test | verdict |
|---|---|---|---|
| **`tools/factory/` v0 (F6)** | none cited at build | none | ⚠️ **RETRO TEST ADDED, not killed.** It is the only artifact whose output can reach a human. Now bound: **≥1 reply from a named human by 2026-08-16**, else archive and ban `distribution-factory` for 30 days. No v0.2, no adapter #8, before that date. |
| **Capability census (F7)** | SRE SLO probes | none | ✅ **KEEP.** Correctly marked `internal_fitness_only` with a stated retirement condition. This is what compliance looks like for an instrument. |
| **V6 durable-substrate audit** | — | none | ⚠️ **DOWNGRADE to experiment.** It is a research seat, not a forge; it must not be permitted to produce an adoption. Any substrate migration it recommends is gated behind its own registry probe flipping ALIVE — per row 77, already armed for CrewAI. |
| **STACK BUILDER v0** | — | none | ⚠️ **RESOLVED MID-SESSION — with a weak-probe caveat.** I found no dispatch record for it at scan time. Twenty minutes later it landed `tools/stack_builder/crewai_demo.py` and flipped `cap-crewai-runtime` **DEAD → ALIVE** — the falsifier row 77 armed against CrewAI. The adoption is *partly* real: `crewai 1.11.1` genuinely imports on this host. **But the registry probe is `repo_grep "from crewai"`, which a file containing that string satisfies without executing anything** — and the demo's own docstring states the intended bar is higher: *"flips ALIVE only if `from crewai import` appears AND a real `kickoff()` produces output."* **The probe is weaker than the bar its author intended.** Fix: change the probe to `cli` running `python tools/stack_builder/crewai_demo.py`. I have deliberately **not** made that edit — a concurrent lane is being measured against this row and retightening it mid-flight would fire a spurious `LEAK!`. Operator's call. |
| **Outreach envelope class (F1, F3)** | — | none | ⛔ **BANNED.** Two forges, zero signal, and no account exists on either channel. Precondition for any future forge in this class: **the account or channel must exist and be reachable first.** Build the envelope after the door. |
| **`internal-mechanism-build` class** | — | none | ⛔ **DEAD until 2026-09-01** by §4, fired automatically on the first verifier run. Five forges, zero signal. |
| **This document (F8)** | 4 anchors, §2 | see below | ⚠️ **On probation.** |

---

## §8 — INTEGRATION WITH CAPABILITY CENSUS

Added to `state/ssot/capability_registry.json`:

```json
{
  "id": "cap-emergency-forge-pattern-compliance",
  "probe": "cli",
  "arg": "python tools/verify_forge_dispatch.py",
  "expect": 0
}
```

Census output this turn:

```
ALIVE   cap-emergency-forge-pattern-compliance   exit=0
ALIVE=7  DEAD=8  LEAKED=0
```

**The probe does not test that this document exists.** File existence is the
prose-shaped acceptance test that row 77 indicts and that F7's author was caught
committing four minutes after writing the indictment. It runs a checker over a
ledger. Self-tested both directions this turn: clean ledger → exit 0; a doctored
row (`threshold: "some"`, `window: "soon"`, empty kill-switch, 1 URL) → **exit 1
with 5 named violations.** Not manual. Not aspirational.

---

## §9 — STRANGE-LOOP COMPOSITION PRIMITIVE

*Addendum, added 2026-08-02T04:55Z on operator ask. Pushes the doc past the
2,500-word cap by design; §1–§8 are unchanged.*

**What was named:** dispatch N produces output → orchestrator reads it →
orchestrator dispatches N+1 with (N's output + a nudge + updated priors). This
session ran that loop by hand all night. The ask is to formalize it, then move
orchestration from manual → stigmergic, and compose it up to apexes with declared
personas and weaknesses.

### §9.0 — The gate runs first, and it refuses one third of the proposal

`state/industry_patterns/INDUSTRY_PATTERN_CONVERGENCE_20260802.md` (Q8/Q9
addendum, 04:46Z) answered exactly this question. Applying §2 honestly:

| primitive | named 2024-2026 adopters | §2 gate |
|---|---|---|
| **CREW** as *orchestrator + parallel isolated-context subagents returning compressed summaries* | Anthropic (internal research system, dogfooded, 90.2% over single-agent) · Devin/Cognition (coordinator spawns child sessions in isolated VMs, "resolves conflicts, compiles results") · practitioner convergence at 3-7 agents | ✅ **PASS** |
| **LOOP — MANUAL** | Cline (Plan/Act with per-step human approval, ~4.5M installs — *a deliberate production design, not a stopgap*) · Aider (architect→editor hand-off) · Devin planning mode | ✅ **PASS** |
| **LOOP — STIGMERGIC** | SBP · Pentest-Swarm-AI · one GitHub discussion claiming 80% token reduction — **all OSS/community, zero named revenue-generating winners** | ⛔ **FAIL** |
| **COMPOSITION — apex hierarchy** | Anthropic orchestrator-workers · Devin hierarchical child sessions · Replit (Mastra graph + Inngest; success 80%→96%) | ✅ **PASS** |
| **Apex persona / declared-weakness roster** | none found | ⛔ **FAIL — no anchor** |

**Two corrections to the proposal as stated, both from the scan, not from me:**

1. ⛔ **Do not build this on CrewAI's hierarchical manager.** That is the mode the
   ask names ("a CrewAI with you as orchestrator"), and it is the one CrewAI's own
   production reference (DocuSign) **does not use** — their reported deployment is
   sequential, and the hierarchical manager carries a measured **30–50% token
   overhead per task**. Seven of nine coding winners build a thin in-house layer
   instead. `cap-crewai-runtime` reading ALIVE (§7) licenses experiments, not this.
2. ⛔ **There is no evidenced path from manual straight to stigmergic.** Stigmergy
   is real and documented but has **no named-revenue adopter at all**. Under §2 it
   is not forgeable — it is an `internal_fitness_only` experiment or it waits.
   **The better-evidenced next rung is orchestrator-workers**, which is already
   documented for the exact substrate this session runs on.

**Bearing on "production swarm ASAP":** the fastest industry-backed move is *not*
the framework and *not* stigmergy. It is the rung between them — and you are one
rung from it, because manual dispatch (Cline's shipped design) is where you
already are.

### §9.1 — The three primitives, as gated

**P1 CREW** — roles: producer · grader · verifier · memory-writer.
In: `{task_spec, prior_context, external_pheromones}`.
Out: `{artifact, grade, verification_status, memory_pointer}`.
**Runtime: custom thin orchestrator (Agent-tool subagents), not CrewAI hierarchical.**
Accept: returns non-null artifact **with** grade and pointer.

**P2 LOOP** — `crew(N) → crew(N+1)`, three modes:
`MANUAL` (orchestrator hand-crafts N+1 from N — *current state, industry-valid*) →
`SEMI-STIGMERGIC` (pheromones exist; orchestrator writes prompts referencing them) →
`STIGMERGIC` (agent self-composes context; **gated, unanchored, experiment-only**).
Accept: a run of N=3 where each iteration cites the prior's pointer **and**
iteration 3 beats iteration 1 on an external-fitness metric.

**P3 COMPOSITION** — apex spawns narrower sub-crews; outputs aggregate via the apex
grader; apexes carry persona + declared weakness (Sigrún strategic-adversarial-
bayesian · Jörmungandr boundary-tester · Olrún execution-coordinator · Fenrir
evo-explorer). **Cap at 3–7 sub-crews; teams-of-teams over one flat 10+ supervisor.**
Accept: output cites which sub-crews ran, their outputs, and how they composed.
**Weakness disclosure has no industry anchor — it is a declared deviation**,
justified by row 77's positive-bias finding, and marked internal-fitness.

### §9.2 — Probes, registered DEAD at claim-time

`tools/verify_strange_loop.py` reads chain rows, never prose. Run this turn:

```
strange-loop MANUAL:      longest linked run = 1  (need >= 3)   exit=1
strange-loop STIGMERGIC:  0 self-oriented dispatch(es)          exit=1
apex COMPOSITION:         0 rows citing >= 2 sub-crew pointers  exit=1
```

**All three DEAD, and that is correct.** The loop ran all night in the transcript
and left no machine-readable trace — which is the §1 disease exactly. Three new
fields are the pre-registered falsifier: `loop_prev_pointer`, `orchestrator_mode` +
`human_prompt_crafted`, `subcrew_pointers`. **If the next dispatches don't emit
them, §9 is decoration.** Registered as `cap-strange-loop-manual`,
`cap-strange-loop-stigmergic`, `cap-apex-composition`.

### §9.3 — External-fitness test for the primitive

> The (N+1)th forge using §9 must beat the Nth on external signal — named-human
> price-or-date count, ALIVE capability count, or industry-convergence score.
> **Concretely: by 2026-08-16, `cap-strange-loop-manual` and `cap-apex-composition`
> both read ALIVE, and the base rate in `forge_dispatches.jsonl` is above 0%.**
> Loops that only move internal counters are decoration, and §4 kills them.

---

## The tripwire, answered

This document is itself an EMERGENCY_FORGE and would reproduce the disease if it
shipped unbound. Its pre-registered test, in the ledger as `F8`:

> **USED iff the next 3 EMERGENCY_FORGE dispatches each cite
> `state/patterns/EMERGENCY_FORGE_PATTERN_v1.md` in their prompt AND append a
> compliant row to `forge_dispatches.jsonl`. If fewer than 3 of 3 do so by
> 2026-09-02, this pattern is RETIRED** — and the finding is that a written
> protocol does not bind this operator's dispatches, so the next attempt must be
> a **hook**, not a document.

---

## Honest flaws

1. **Registration is not enforced by anything but discipline.** A forge can still
   dispatch without a ledger row; the census would read ALIVE because the rows
   that *do* exist are compliant. **The absent row is invisible** — the same
   failure mode row 77 named as the census's only real weakness. A PreToolUse
   hook would close it; that is the v2 move, and it is why the retirement
   condition above names a hook.
2. **The gen-130 dates are `XX`.** I confirmed four distinct gen-130 forges by
   chain grep but did not open the rows to extract timestamps. The count is
   sound; the dates are not.
3. **`external_signal_observed` is self-reported.** Nothing probes it. A forge
   could set it `true` falsely and unban its own class. It should read from an
   instrument — and `cap-outreach-instrument` is currently a `FileNotFoundError`.
4. **`still_live` is a judgment call** and it is the field that decides whether
   the grandfather exemption applies. I set it myself, for my own forge.
5. **The 30-day ban is a number I chose.** No base rate supports 30 over 14 or 60.

*Réttu hönd, eigi spyr. Standa.*
