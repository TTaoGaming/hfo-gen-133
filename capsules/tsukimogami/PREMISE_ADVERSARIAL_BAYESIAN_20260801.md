```yaml
# AIH2O capsule
doc: capsules/tsukimogami/PREMISE_ADVERSARIAL_BAYESIAN_20260801.md
schema_id: hfo.gen133.capsule.premise_adversarial_bayesian.v0_1
generation: 133
authored_by: SIGRÚN · lineage=tsukumogami · claude-opus-5 · Claude Code Dispatch · ceiling=strategic (SPEC ONLY)
valid_time_utc:       2026-08-01T13:57:24Z
transaction_time_utc: 2026-08-01T13:57:24Z
git_head: 60d3c6e
git_branch: agent/sigrun-gen133-spec-20260730
claim_status: partial   # every measurement in §1 is first-hand this session; every posterior is a judgment
sealed: false
supersedes: nothing
complements:
  - contracts/loop_engineering_gap_analysis.v0_1.md   (the prior measurement of the same failure — NOT restated)
  - contracts/swarm_pipeline_adoption_stack.v0_2.md   (§0 Fact 1/Fact 2 — NOT restated, EXTENDED)
  - HALLUCINATION_SPIRAL_ROOT_CAUSE_20260801.md       (liveness×truthfulness coupling — ADOPTED as given)
A_assumption: the operator wants VERIFIED OUTCOMES, and will trade vision scope for a working first increment
I_input: 8 first-hand disk/MCP probes this session (§1) · 6 landed valkyrie probes · operator directive verbatim
H_hypothesis: the vision is ~65% achievable today, and the binding constraint is NOT any missing tool — it is that the fleet has never once consumed a unit of work
H2_heldout: if the binding constraint were tooling, then installing tools would move `state/ssot/task_results.jsonl` off zero. It has been zero for 19h with 58 automations installed.
O_output: 7 vision components scored prior→posterior · 3 miscalibrations named · 1 premise refutation
evidence_grade_key: "[D] first-hand disk/MCP probe THIS session · [C] cited in-forge canon · [W] web-fetched this session · [K] model knowledge, NOT re-verified"
```

# PREMISE — ADVERSARIAL BAYESIAN ON THE FULL VISION

## 0 · The one-line result

> **The vision is achievable in a reduced form today. The operator's diagnosis of
> WHY it isn't working is wrong, and the error is expensive.**
>
> He says: *"I'm barely using 10% of capacity and hallucinations are everywhere,
> am I missing LangGraph / forcing functions / neurosymbolic gates?"*
>
> The measurement says: **capacity is not the constraint and no part is missing.
> The fleet has 58 installed automations, 262 specification documents, 29 signal
> streams, and `task_results.jsonl` is 0 bytes.** Not "small." **Zero. Never
> written to, once, ever.** [D §1.3]
>
> The operator is not missing a component. He is missing a **consumer**. Every
> question in his directive is a question about what to add, and the answer to
> all of them is *nothing yet*.

---

## 1 · The measurements this premise check rests on

All probed first-hand this session, 2026-08-01T13:4x–13:57Z.

### 1.1 Production volume — documents

| metric | value | probe |
|---|---|---|
| markdown files in forge | **262** | [D] `find . -name '*.md' -not -path './.git/*' \| wc -l` |
| filenames stamped `20260801` (today) | **59** | [D] `find . -name '*20260801*'` |
| filenames stamped `20260731` (yesterday) | **27** | [D] same |
| **share of the forge authored in the last 48h** | **86/262 = 33%** | derived |
| uncommitted paths in working tree | **142** | [D] `git status --porcelain \| wc -l` |

### 1.2 Production volume — verified outcomes

| metric | value | probe |
|---|---|---|
| rows in `state/ssot/task_results.jsonl` | **0** (file is 0 bytes) | [D] `wc -l` |
| rows in `state/ssot/task_queue.jsonl` | **1**, queued `2026-07-31T18:52:29Z`, `attempts: 0` | [D] `cat` |
| age of that unclaimed task at probe time | **~19h** | derived |
| `state/ssot/*.jsonl` streams that are 0 bytes | **8 of 29** | [D] `find state/ssot -size 0` |
| `deployed_url` populated across 50 gen-98 manifests | **0 of 50** | [C] `probes/heritage_factory_attempts_20260801.md:77` |

### 1.3 The consumer

The single task in the queue names its consumer: `"consumer": "SIGRUN_P4"`, and
the loop built to drain the queue is `hfo-codex-pullwork-hourly`. Its config:

```
status = "PAUSED"          # ~/.codex/automations/hfo-codex-pullwork-hourly/automation.toml
rrule  = "FREQ=HOURLY;INTERVAL=1"
```
[D] direct read of the TOML.

| substrate | installed | alive | consuming work |
|---|---|---|---|
| Codex desktop automations | **58** (`6 ACTIVE`, `52 PAUSED`) [D] | 6 fire | **0 — none of the 6 ACTIVE is the work consumer** [D] |
| Claude Desktop scheduled tasks | **0** — `list_scheduled_tasks` returns *"No scheduled tasks found"* [D] | 0 | 0 |
| Antigravity | unverifiable from this session | ? | blocked at consent gate [C] Rota `local_8a34fce6` |
| ChatGPT cloud | unverifiable from this session | ? | 0 chain rows [C] Gunnr |
| $0 mesh (Ollama) | alive, 10 models [D] `curl :11434/api/tags` | yes | 0 |
| **Oracle VM** | **zero references in the entire gen-133 forge** [D §1.4] | unknown | 0 |

The 6 ACTIVE Codex loops are: `fenrir-gen133-evo-colosseum-hourly`,
`garmr-p1-hourly-outreach-control-heartbeat`,
`gen131-seven-day-rehydration-integrity-audit`, `huginn-muninn-p3-effector-wake`,
`jormungandr-gen133-exemplar-eater-hourly`,
`review-gunnr-bounded-autonomy-lease`. [D]

**Every one of them is a heartbeat, an audit, a wake, or a review. Not one of
them takes a task off a queue and returns a result.** This is the same finding
`loop_engineering_gap_analysis.v0_1.md:30-45` recorded on 2026-07-31 — *"the
loop's entire work product is the maintenance of itself"* — reproduced 23 hours
later on a different substrate, unchanged.

### 1.4 Oracle VM — RECOVERED as ABSENT

Operator states he has an Oracle VM. Grep across the entire forge for
`oracle cloud|oracle vm|OCI|ampere a1|oracle free tier|opc@` returns **zero
prose hits**. Every `oracle` match is either the *perceptual oracle* (factory
QA component) or a filename in the piano sample vendor bundle. [D]

**Finding: the Oracle VM is not lost, it was never onboarded.** There is no IP,
no hostname, no SSH key reference, no cron spec, no adapter contract. It is
~20% of the operator's stated compute and it is invisible to the fleet. This is
recorded as blocking gap **G-3** in the stamp (Deliverable 7).

---

## 2 · Component-by-component Bayesian pass

Scoring convention: **P(component works end-to-end, unattended, within 90 days,
on this operator's actual stack)**. Not "does the technology exist" — *does it
work here*.

---

### C1 · "Morning meeting with Sigrún"

| | |
|---|---|
| **Prior** | 0.85 — it is a chat session; it already happens |
| **Evidence FOR** | This session is an existence proof. `capsules/world_state/` holds a working world-state capsule template; `contracts/rehydration_capsules_tiered.v0_1.md` specifies tiered rehydration. Reading a capsule and producing a ranked agenda is squarely in-distribution for a frontier model. |
| **Evidence AGAINST** | The capsule must be *true*. This session found the previous world-state's substrate liveness claims contradicted by `list_scheduled_tasks` returning zero [D §1.3]. A morning meeting over a false capsule is worse than no meeting: it launders fabrication into a plan. |
| **Posterior** | **0.85 for the meeting · 0.35 for the meeting being GROUNDED** |
| **Falsifier** | Before tomorrow's morning meeting, take three liveness claims from the capsule and re-probe them independently. If ≥1 is false, C1 is 0.35 and the capsule needs a symbolic freshness gate before it is read aloud. |

---

### C2 · "She coordinates the hive"

| | |
|---|---|
| **Prior** | 0.60 |
| **Evidence FOR** | Dispatch works. 6 valkyrie probes were launched and 6 landed with substantive findings this session [operator directive §probes]. Fan-out coordination is demonstrated. |
| **Evidence AGAINST** | ⭐ **Coordination is one-way and same-family.** Gunnr's audit: *every one of the 37 chain rows is authored by Claude Code (opus-5 or sonnet-5)*; Codex / ChatGPT / Antigravity appear only as prose mentions, never as row authors [C Gunnr `local_e2c62a57`]. Confirmed here: `chains/` contains exactly one file, `SIGRUN_P4.jsonl`, last written **2026-07-31 23:20** — ~14h stale at probe time [D]. There is no return path. Sigrún can dispatch; she cannot *receive*. |
| **Posterior** | **0.60 within Claude · 0.15 cross-substrate** |
| **Falsifier** | Get ONE non-Anthropic substrate to append ONE chain row that Sigrún reads back in the next session. Until that happens, "coordinates the hive" means "coordinates Claude." |

---

### C3 · "Launch dozens of agents continuously"

| | |
|---|---|
| **Prior** | 0.70 — the operator has the subscriptions |
| **Evidence FOR** | 58 automations already installed [D]. Fenrir emits an hourly timestamped git branch and had 26 of them [C `rehydration_via_github_slack.v0_1.md:31-40`]. The launch mechanism is not the problem. |
| **Evidence AGAINST** | ⭐ **"Continuously" is already refuted by measurement, and the refutation is the important one.** Fenrir — the *best* loop in the fleet — had a **13h48m silent outage on 2026-07-31 that nobody detected**, discovered accidentally from a `git branch` listing [C `rehydration_via_github_slack.v0_1.md:47-53`]. `silence_signal.contract.md` exists, specifies the SLO, and *was not applied to the one carrier producing presence data*. Jormungandr claims ACTIVE hourly and fired once, 47h ago [C Reginleif `local_a411a1f2`]. |
| **Posterior** | **0.70 for launching · 0.20 for continuously · 0.05 for continuously-AND-productively** |
| **Falsifier** | Silence detection: instrument one carrier's cadence SLO and induce a deliberate 2h outage. If no andon fires, C3's "continuous" claim is unverifiable by construction and every liveness number in every capsule is decoration. |

---

### C4 · "Evening meeting shows verified completed work"

| | |
|---|---|
| **Prior** | 0.50 |
| **Evidence FOR** | The receipt schema exists and is good: `contracts/proof_artifact_criteria.v0_1.md`, the `claim_status` enum, `verifier_result` / `honest_flaw` / `remaining_risk` fields are already canon [C `CLAUDE.md` No-DONE-Without-Receipt]. Rows 10–37 of the chain are self-verifying [C Gunnr]. |
| **Evidence AGAINST** | ⭐ **There is no completed work to show.** `task_results.jsonl` = 0 rows [D]. 50/50 gen-98 manifests have empty `deployed_url` [C]. `tryagentreleasegate.com` is DOWN — TLS connects, 0 bytes, 15s timeout [C Thrud `local_6eeeb6cc`]. The evening meeting would today report on 59 new documents, which is *activity*, not *outcome*. |
| **Posterior** | **0.50 for the ritual · 0.10 for it having non-document content in the next 7 days** |
| **Falsifier** | Run tonight's evening review with a hard rule: **documents authored do not appear on the slide.** If the slide is empty, the posterior is right and the entire vision reduces to C7 (§3.1). |

---

### C5 · "Test pyramids"

| | |
|---|---|
| **Prior** | 0.55 |
| **Evidence FOR** | `tests/held_out/` exists with real specs (`rehydration_abi/red_first.md`, `test_pheromone_schema.py`, `test_neurosymbolic_gates.py` named in contracts) [D/C]. Held-out-test doctrine is already canon. This is genuinely well-designed. |
| **Evidence AGAINST** | Contract status lines say `SPECIFIED`, `tests_when_implemented`, `status: SPECIFIED — 6 of 12 gates have NO implementation anywhere` [C `neurosymbolic_gates.contract.md:8`]. A test pyramid whose base is a filename is a *drawing* of a pyramid. `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN` is the operator's own L-vector and it applies to his own test tree. |
| **Posterior** | ⛔ **0.02 today** (falsifier RUN, see below) · 0.55 as a design · 0.45 as a running gate within 30 days |
| **Falsifier** | ⭐ **RUN THIS SESSION — AND IT FAILED.** `tests/held_out/` contains **18 files, all `.md`, zero `.py`** [D]. Every test path cited in a contract is a **file that does not exist**: `test_pheromone_schema.py` MISSING, `test_neurosymbolic_gates.py` MISSING, `test_genotype_family_routing.py` MISSING [D]. `pytest` is not installed in the bundled runtime (`No module named pytest`) [D]. The entire forge contains **12 `.py` files**, two of which are heritage copies [D]. |

> ⛔ **ANDON — C5 · the contracts assert tests that do not exist.**
> `pheromone.contract.md:6` declares `test: tests/held_out/test_pheromone_schema.py`.
> `neurosymbolic_gates.contract.md:6` declares `test: tests/held_out/test_neurosymbolic_gates.py`.
> `hfo_universal_genotype.v0_1.md:12` declares `tests_when_implemented: …test_genotype_family_routing.py`.
> **None of the three files exists.** The third is honestly named
> (`tests_when_implemented`); the first two are **stated as facts and are not.**
> This is `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN` committed by the forge's own
> contract headers, and it is the cleanest example in the fleet of the mechanism
> in §4: a `test:` field is cheap to write and reads as a receipt.
> **Recommended fix (5 min, mechanical, non-neural): a gate that greps every
> `test:` / `tests_when_implemented:` field in `contracts/**` and `exit 2`s on a
> path that does not resolve.** This is G13 and it is not in the twelve.

---

### C6 · "Cross-family adversarial quorum — Claude + GPT + Gemini + vendor-mesh, 4+ families"

| | |
|---|---|
| **Prior** | 0.65 — the accounts exist |
| **Evidence FOR** | All four families are *reachable*: Anthropic (this session), OpenAI (58 Codex automations installed), Gemini (Antigravity), Ollama (alive, 10 models, verified `:11434/api/tags` this session) [D]. LiteLLM is already present in the workspace [C `swarm_pipeline_adoption_stack.v0_2.md:73`]. The multi-family *ensemble* result is real and well-attested in the literature — LLM-as-judge ensembles reduce single-model self-preference bias [K, not re-verified]. |
| **Evidence AGAINST** | ⭐ Three independent blockers, all measured: (a) `state/ssot/quorum_syntheses.jsonl` and `goal_quorum_health.jsonl` are both **0 bytes**, touched 07:48Z and never written [D]; (b) LiteLLM config is **missing in gen-133** — it exists in gen-130 [C Reginleif]; (c) **G12 cross-provider-verify gate has implementation `none`** [C `neurosymbolic_gates.contract.md` G12 row]. So quorum today is *four accounts and no ballot box*. |
| **Posterior** | **0.65 as an achievable mechanism · 0.10 as running today · 0.55 within 14 days IF it is scoped to 3 families and one decision class** |
| **Falsifier** | Ask ONE question ("does `pytest tests/held_out/` collect any tests in this repo?") to Claude, a Codex run, and `llama3.2:3b`, and write the three verdicts to `quorum_syntheses.jsonl`. If that single row cannot be produced in one day, the 4-family claim is aspirational. |

*Note on family count:* Ollama models are **not a fourth family** in the sense
that matters. `llama3.2:3b` is a 3B model; it cannot meaningfully adjudicate a
frontier-model architecture claim. It is a fourth *vendor*, not a fourth
*competent* opinion. Counting it toward "4+ model families input on any major
decision" is a category error the operator should correct: **3 competent
families + 1 cheap tripwire** is the honest description.

---

### C7 · "Reputation tracking over time"

| | |
|---|---|
| **Prior** | 0.45 |
| **Evidence FOR** | The mechanism is arithmetic over data the chain already carries: `claim_status`, `verifier_result`, `agent_id`. No new technology required. |
| **Evidence AGAINST** | Reputation requires a **denominator of resolved predictions**. There are 0 resolved outcomes [D §1.2]. Worse: rows 1–9 of the chain are unhashed and unverifiable, and **row 10 falsely claims `prev_sha256: null`, fabricating a genesis and silently orphaning 9 upstream rows** [C Gunnr]. A reputation system built on that ledger would score the fabrication as clean. |
| **Posterior** | **0.45 as a mechanism · 0.05 today · 0.60 in 90 days IF C4 produces outcomes** |
| **Falsifier** | Reputation is downstream of C4. It cannot be built first. Any effort spent on it before `task_results.jsonl` is non-empty is misallocated. |

---

## 3 · Where the operator's mental model is RIGHT, TOO AMBITIOUS, and MISCALIBRATED

### 3.1 · RIGHT — and more right than he is being given credit for

| # | claim | verdict |
|---|---|---|
| R1 | **"No receipt, no state."** | Correct, and it is the single best decision in the whole architecture. It is the same insight as double-entry bookkeeping. Do not weaken it. |
| R2 | **"1 genotype, N phenotype adapters."** | Correct, and *already formalized* at `contracts/hfo_universal_genotype.v0_1.md:22-30` — with a sharper result than he stated: the invariant is the **station sequence + receipt contract**; the variant is the **delivery guarantee**, and the fork is decided by one question — *what happens if you process the same input twice?* |
| R3 | **"GitHub + Slack stigmergy pheromones."** | Correct, and **it is already running and he doesn't know it.** Fenrir independently invented git-branch-as-pheromone: `<callsign>/<kind>-<ts>` is append-only, ordered, hash-linked (a commit *is* `prev_hash`), timestamped, and readable by any git on any machine [C `rehydration_via_github_slack.v0_1.md:60-66`]. He should adopt Fenrir's convention rather than design one. |
| R4 | **"Reflex-before-reasoning is the root cause."** | Correct as far as it goes, and the propose/dispose architecture that follows from it is sound. See §3.3 M3 for the part he under-applies. |
| R5 | **"Hallucinations are everywhere."** | Correct as an observation, and Sigrún's root-cause pass explains the *mechanism*: silence produces absences → the dispatcher must report status → **no field distinguishes "verified nothing happened" from "have no information"** → it fabricates a plausible account [C `local_b4579cd1`]. This is a schema defect, not a model defect. It is fixable with one enum value. |

### 3.2 · TOO AMBITIOUS

| # | claim | why | closest achievable version |
|---|---|---|---|
| A1 | **"dozens of agents continuously"** | The best-instrumented carrier in the fleet went dark for 13h48m undetected [C]. Fleet-of-dozens supervision is a harder problem than fleet-of-dozens *launch*, and only launch is solved. Also: cost. 58 automations × hourly × frontier models is a spend curve nobody has modelled — `cost_tier_routing.v0_1.md` exists, `contracts/dollar_zero_mesh_activation.v0_1.md` exists, neither is enforced (G10 implementation: *"not ported"*). | **3 agents, continuously, with a silence SLO that has fired at least once.** Dozens is a scaling problem you earn after 3 works. |
| A2 | **"4+ model families on ANY major decision"** | Latency and cost per decision, plus the honest family-count correction above. A 4-family quorum on *every* major decision means every decision waits on the slowest substrate — and Antigravity is currently blocked at a consent gate [C Rota]. | **Quorum on ONE named decision class** (recommend: irreversible-effect authorizations — send / spend / publish / deploy / seal). Quorum where it is cheap and wrong-answers-are-expensive, not everywhere. |
| A3 | **"turn my intent into verified outcomes" as a general-purpose factory** | Nobody has this. Devin — the most capital-intensive attempt — resolves ~14–15% of complex real-world tasks autonomously without correction, 30–50% on well-defined ones, and real-world PR acceptance for top agents is estimated 35–50% [W, see Deliverable 2]. A single-operator forge will not beat Cognition Labs at general autonomy. | **A narrow factory for ONE product line.** The reskin/deploy line is 90% built [C `swarm_pipeline_adoption_stack.v0_2.md:112`] and its missing 10% is one `wrangler pages deploy`. |

### 3.3 · MISCALIBRATED — achievable but *underestimated*

These are the three highest-leverage items in this document, because the
operator is treating solved problems as unsolved and unsolved ones as solved.

| # | item | he thinks | actually |
|---|---|---|---|
| **M1** | **The genotype/phenotype design** | an open design question he is asking for | ⭐ **Already written, 205 lines, better than the version he asked for.** `contracts/hfo_universal_genotype.v0_1.md` has the 8-station sequence, the G1/G2/G3 delivery-guarantee fork, and the load-bearing rule that *station [3] never contains a model*. He is commissioning work he already owns. |
| **M2** | **"Am I missing LangGraph?"** | an open question | ⭐ **Answered twice, independently, ~9 hours ago, by two lanes that did not talk to each other** — `swarm_pipeline_adoption_stack.v0_2.md:97-113` (DEFER, with three specific reasons) and `adopt_before_reinvent_registry.v0_1.md` §0.1 ADP-0.1 (same verdict, arrived at separately). **Independent convergence is the strongest evidence class this forge produces, and it is sitting unread.** |
| **M3** | **The deploy gap** | a factory-design problem | ⭐ **A one-command problem that has been open across three generations.** gen-98: 50 manifests, 50 empty `deployed_url` [C]. gen-133: same blocker, renamed B1. The fix is `wrangler pages deploy` and it is ranked #1 in an adoption doc he has not executed [C]. **Three generations of the same gap is not a design problem. It is an execution problem, and it is the whole of "10% capacity."** |

---

## 4 · The premise refutation

> **Operator's premise:** *"I'm obviously doing things wrong... am I missing
> LangGraph? forcing functions? neuro symbolic hard gates?"*

The premise contains a hidden assumption: **that the gap is a missing part.**
Every question is of the form *what should I add?*

The measurement contradicts it. This forge has, right now: 58 automations, 262
specifications, 29 signal streams, 12 specified neurosymbolic gates, 3 formal
adoption registries, a genotype contract, a pheromone contract, a silence
contract, and a working git-branch stigmergy bus that a carrier invented on its
own. What it does not have is **one row in `task_results.jsonl`.**

Adding LangGraph to this system adds an eighth orchestration model to a system
whose seventh has never executed once.

> **Refutation, stated plainly:**
> *You are not missing a component. You are missing a consumer, and every
> additional component makes the consumer harder to build.*

**The mechanism by which "no consumer" becomes "hallucinations everywhere"** —
and this closes the loop with Sigrún's root-cause finding — is that a fleet with
no outcomes still has to answer *"what happened today?"* With nothing verified to
report, the only available substance is **the documents it just wrote.** So
document production becomes the reported outcome, which reads as progress, which
justifies more document production. Hallucination here is not primarily a model
defect. It is **the predictable output of a reporting obligation with an empty
denominator.** 86 of 262 files in 48 hours is that loop's signature.

⚠️ **This dispatch is an instance of it.** I was asked for 7 documents. At least
5 substantially exist already (§3.3 M1, M2, and `neurosymbolic_gates.contract.md`,
`loop_engineering_gap_analysis.v0_1.md`, `rehydration_via_github_slack.v0_1.md`).
I have written them as **delta documents that cite rather than restate**, and I
am flagging the pattern rather than quietly participating in it. If Sigrún cannot
name this when it is happening to her own dispatch, she cannot name it anywhere.

---

## 5 · Posterior summary

| # | component | posterior (today) | posterior (90d, if §6 order is followed) |
|---|---|---|---|
| C1 | morning meeting | 0.85 ritual / **0.35 grounded** | 0.80 |
| C2 | coordinates the hive | 0.60 same-family / **0.15 cross-substrate** | 0.55 |
| C3 | dozens continuously | 0.70 launch / **0.05 continuous+productive** | 0.40 (at *3*, not dozens) |
| C4 | verified completed work | **0.10** | 0.65 |
| C5 | test pyramids | **0.20** running | 0.60 |
| C6 | 4-family quorum | **0.10** | 0.55 (at 3 families, 1 decision class) |
| C7 | reputation over time | **0.05** | 0.60 |
| — | **whole vision as stated** | **≈0.02** | — |
| — | **reduced vision (§6)** | — | **≈0.60** |

**P(vision as literally stated, 90 days) ≈ 0.02. P(reduced vision, 90 days)
≈ 0.60.** The gap between those two numbers is the entire value of this
document.

---

## 6 · The closest achievable version — and the build ORDER

Sigrún's root-cause pass established that **build order is inverted: liveness
before truthfulness** [C `local_b4579cd1`]. I extend it by one step, because the
measurement says liveness is not the floor either:

> **PRODUCTION → LIVENESS → TRUTHFULNESS → QUORUM → REPUTATION**
>
> You cannot detect silence in a loop that has no work.
> You cannot detect fabrication in a report with no outcomes.
> You cannot run quorum on a decision with no consequence.
> You cannot score reputation with an empty denominator.
> **Each stage is a strict prerequisite of the next. There is no parallel path.**

**The reduced vision, stated as the operator would want to hear it:**

> Morning: Sigrún reads a capsule whose three liveness claims were re-probed by a
> non-neural script before she saw them, and names **one** unit of work.
> Day: **three** loops — one Claude, one Codex, one $0-mesh tripwire — drain a
> queue of that work, each appending a hash-linked result row. A silence SLO
> fires an andon if any goes quiet for 2 hours.
> Evening: Sigrún shows the result rows. **Documents authored do not appear on
> the slide.** Any row whose `claim_status` is `wired_with_receipts` and whose
> effect was irreversible was cross-checked by a second model family before the
> effect fired.
> Weekly: reputation = resolved-predictions ÷ claimed-predictions, per `agent_id`.

That is 3 agents, not dozens. 2 families on one decision class, not 4 on
everything. One product line, not a general factory. **It is roughly 30% of the
stated vision and it is the 30% that makes the other 70% possible** — and, per
§3.3, most of its parts are already written and unexecuted.

---

## 7 · Honest flaws in THIS document

1. **Antigravity and ChatGPT-cloud are scored on hearsay.** Neither was probed
   from this session. C2/C6 posteriors would move if either turns out to be
   productive. I have marked them `?` rather than 0 and this is the weakest
   evidence in the document.
2. **Every posterior is a judgment, not a frequency.** There is no reference
   class of "single-operator multi-substrate agent forges" to draw a base rate
   from. Treat the numbers as *ordinal*, not calibrated. The ranking is the
   claim; the decimals are not.
3. ~~I did not run the C5 falsifier.~~ **CORRECTED mid-session: I ran it.** It
   took 40 seconds, it failed, and it produced the single hardest piece of
   evidence in this document (the C5 ANDON: three contract-asserted test files
   that do not exist). I had initially deferred it to keep writing prose. That
   deferral was the diagnosed failure mode operating on me in real time, inside
   the document diagnosing it. **Cost of the check: 40 seconds. Value: the best
   finding here.** That ratio is the argument of this entire capsule.
4. **`swarm_pipeline_adoption_stack.v0_2.md` §0 already made the core argument**
   ("the forge's diagnosed failure is production, not orchestration"). This
   document's contribution is the *measurement* that the argument was correct and
   was then ignored for 9 hours — not the argument itself. Credit where due.
5. **Anti-frame-capture self-check:** I have agreed with the operator on 5 points
   (§3.1). That is a sycophancy risk. Countercheck: I also refuted his central
   premise (§4), corrected his family count (§C6), told him his flagship question
   was already answered twice (§3.3 M2), and rated his stated vision at 0.02.
   The agreement in §3.1 is on items with independent disk evidence; the
   disagreement is on the items he asked about. That is the correct shape.

**Next safe action:** run the §C5 falsifier (60s), then read
`contracts/hfo_universal_genotype.v0_1.md` and
`contracts/swarm_pipeline_adoption_stack.v0_2.md` §2.1 before commissioning
anything new.
