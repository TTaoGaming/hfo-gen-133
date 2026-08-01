```yaml
# AIH2O capsule
doc: capsules/tsukimogami/CASE_STUDIES_SYSTEMS_THAT_WORK_IN_PART_20260801.md
schema_id: hfo.gen133.capsule.case_studies_partial_systems.v0_1
generation: 133
authored_by: SIGRÚN · lineage=tsukumogami · claude-opus-5 · ceiling=strategic (SPEC ONLY)
valid_time_utc:       2026-08-01T14:05:00Z
transaction_time_utc: 2026-08-01T14:05:00Z
git_head: 60d3c6e
claim_status: partial   # [W] rows web-verified this session; [K] rows are model knowledge NOT re-verified — grades are marked per row and MUST NOT be read as uniform
sealed: false
complements:
  - contracts/swarm_pipeline_adoption_stack.v0_2.md   (the ADOPT/DEFER/REJECT verdicts — this doc does NOT overturn them)
  - contracts/adopt_before_reinvent_registry.v0_1.md  (16-layer registry — NOT restated)
A_assumption: operator wants to know which parts of his vision are already SOLVED by someone else, so he stops rebuilding them
I_input: 2 web searches this session (Devin real-world rates; LangGraph/Temporal 2026 state) · model knowledge · in-forge canon
H_hypothesis: every component of the vision exists in production somewhere; NO ONE has the whole thing; the integration is the unsolved part and it is unsolved for everybody
H2_heldout: name one shipped system that does morning-intent → dozens of continuous agents → evening verified-outcomes with cross-family quorum. If one exists, buy it instead of building it.
O_output: 18 systems · verdict + integration cost + what it substitutes for · 4 ADOPT · 6 DEFER · 8 STUDY-ONLY
evidence_grade_key: "[W] web-verified 2026-08-01 · [C] in-forge canon · [K] model knowledge, NOT re-verified this session — treat as a lead, not a receipt"
```

# CASE STUDIES — SYSTEMS THAT WORK IN PART

## 0 · The answer to the operator's actual question

> *"I know there are systems that work in part, but I'm struggling to integrate
> and get the whole system working."*

**Nobody has the whole system.** Not Cognition, not Microsoft, not LangChain.
The reason is not that it is hard to build — it is that **each component has a
different failure mode, and the failure modes compose multiplicatively.**

The industry has converged on a much smaller claim than the operator's vision,
and the convergence is informative:

| the vision's promise | what the market actually ships in 2026 |
|---|---|
| autonomous agents complete work | agents complete **well-scoped** work at 30–50%, **complex real-world** work at ~14–15% [W] |
| agents run continuously | agents run **durably** (survive process death) via an external workflow engine — Temporal, not the agent framework [W] |
| cross-family quorum decides | **human review** decides; multi-model is used for *eval*, not for *authorization* [K] |
| reputation over time | **eval suites + traces** (Langfuse/LangSmith/Braintrust); agent-level reputation scoring is not a shipped product category [K] |

⭐ **The single most transferable finding:** the 2026 production pattern is
**durability lives OUTSIDE the agent framework.** Temporal owns the multi-hour
lifecycle; the agent framework owns one reasoning step inside a Temporal
activity. Temporal ships an official LangGraph plugin, and OpenAI itself uses
Temporal for Codex, handling millions of production coding-agent requests daily
[W]. Temporal Cloud reports 9.1 trillion lifetime action executions, 380% YoY
growth [W].

**HFO already made this architectural choice and did not notice.** The
git-committed JSONL chain with `prev_sha256` links *is* an event-sourced durable
log external to every agent. That is the same architecture, hand-rolled. The
question is not whether to adopt Temporal — it is whether the hand-rolled
version needs replacing. **It does not, yet.** See §3.

---

## 1 · Autonomous SWE agents — the closest analogues to the operator's vision

| system | 1-line role | what works | what doesn't | HFO verdict | link |
|---|---|---|---|---|---|
| **Devin / Cognition** [W] | long-running autonomous SWE agent with its own VM, browser, shell | scoped bug-fix rates reported 78% on clearly-scoped issues; Devin 2.0 reportedly >50% on SWE-Bench Pro | **~14–15% of complex real-world tasks autonomously without correction**; real-world PR acceptance for *top* agents estimated 35–50% because real codebases carry implicit conventions benchmarks miss | **STUDY-ONLY.** The most capital-intensive attempt at exactly the operator's C3+C4 and it lands at 14–15% unattended. This is the **base rate to calibrate against**, and it is the strongest argument for §6 of the premise doc: narrow the scope. | [cognition.ai](https://cognition.ai) · [benchmark roundup](https://presenc.ai/research/coding-agent-benchmarks-2026) |
| **SWE-agent** (Princeton) [K] | agent-computer interface for repo-level issue resolution; the reference open implementation | established the ACI idea: **the interface the agent sees matters more than the model** | benchmark-shaped; not a fleet | **STUDY-ONLY** — but the ACI lesson applies directly: HFO's agents see a *filesystem*, and the queue schema IS their ACI. A bad queue schema caps the whole fleet. | [github.com/SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) |
| **OpenHands** (ex-OpenDevin) [K] | OSS Devin-equivalent, sandboxed runtime + multi-agent | genuinely runnable, OSS, self-hostable | needs Docker — **the measured 0%-success blocker on this host** [C `swarm_pipeline_adoption_stack.v0_2.md` §0 Fact 2] | ⛔ **REJECT this quarter** — Docker. Revisit on the Oracle VM. | [github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) |
| **Aider** [K] | terminal pair-programmer, git-commit-per-change | **git-native**: every change is a commit with a message — receipts by construction | single-session, human-in-loop, not a fleet | ⏸️ **DEFER, but steal the pattern.** Aider's commit-per-change is the same insight as Fenrir's branch-per-cycle. Convergent evidence for git-as-receipt-bus. | [aider.chat](https://aider.chat) |
| **Cursor Composer / Windsurf / Cline** [K] | IDE-surface agents | fastest human-in-loop iteration available | require a human at the keyboard — **structurally cannot be a continuous loop** | ⛔ **NOT APPLICABLE.** These are the opposite of the vision: they optimize supervised throughput. Listing them to close the option, not to adopt. | [cursor.com](https://cursor.com) · [windsurf.com](https://windsurf.com) · [github.com/cline/cline](https://github.com/cline/cline) |
| **Claude Code** (this substrate) | CLI/dispatch agent with subagent fan-out, MCP tool surface, scheduled tasks | ⭐ **demonstrated in this session**: 6 parallel probes dispatched, 6 landed with substantive findings. Fan-out works. | ⭐ **no cross-session persistence and no inbound channel.** Sessions are turn-based; a dispatched agent returns to *this* session or nowhere. `mcp__scheduled-tasks__list_scheduled_tasks` returns **zero** on this host [D] — the persistence surface the operator believed was populated is empty. | ✅ **KEEP as the coordination substrate**, but see Deliverable 6: the persistence gap is the load-bearing constraint on "Sigrún as lead." | [claude.com/claude-code](https://claude.com/claude-code) |

---

## 2 · Multi-agent orchestration frameworks

| system | 1-line role | adoption profile | HFO verdict | link |
|---|---|---|---|---|
| **AutoGen / AG2** (Microsoft) [K] | conversational multi-agent; agents talk to each other to converge | Strong research traction, real enterprise pilots. The conversation-as-protocol idea is powerful and **also its failure mode**: agents converge on agreement rather than truth — the same L-FRAME-CAPTURE the operator already named. | ⏸️ **DEFER.** HFO's coordination is file/contract-based across *heterogeneous vendor substrates*; AutoGen orchestrates in-process Python. Most of the fleet is not in that process. | [github.com/microsoft/autogen](https://github.com/microsoft/autogen) |
| **MetaGPT** [K] | role-based SWE team (PM → architect → engineer → QA), SOP-encoded | Very high GitHub traction. Produced the "agents + SOPs" framing that HFO's station sequence independently rediscovered. | ⏸️ **DEFER — but note the convergence.** MetaGPT's core claim (*encode the SOP, not just the role*) is exactly `hfo_universal_genotype.v0_1.md`'s station sequence. **Independent arrival at the same design raises confidence in the genotype contract.** | [github.com/FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) |
| **ChatDev** [K] | virtual software company, waterfall phases | Research artifact. Demos are toy-scale; the honest read is that role-play does not survive real repos. | ⛔ **STUDY-ONLY.** Cautionary: the aesthetic of a working org chart is not an org. Directly relevant to HFO's 40-card roster. | [github.com/OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) |
| **CrewAI** [K] | role/task/crew orchestration, deliberately simple API | Large adoption in the "get something running today" tier. Lighter than LangGraph. | ⏸️ **DEFER.** Same objection as AutoGen: in-process Python, single vendor. Would substitute for nothing HFO has. | [github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) |
| **LangGraph** [W] | graph state machine for agents; v1.0 GA Oct 2025, zero breaking changes; built-in checkpointing/persistence | ⭐ **Most-deployed OSS agent framework.** Production pattern in 2026: LangGraph *inside* a Temporal activity [W]. | ⏸️ **DEFER — verdict already reached twice, independently, on 2026-08-01** [C `swarm_pipeline_adoption_stack.v0_2.md:97-113` and `adopt_before_reinvent_registry.v0_1.md` ADP-0.1]. Full answer in Deliverable 5. | [langchain.com/langgraph](https://www.langchain.com/langgraph) · [1.0 announcement](https://www.langchain.com/blog/langchain-langgraph-1dot0) |
| **BabyAGI / AutoGPT** [K] | 2023 task-list-driven autonomous loops | ⭐ **The most instructive failures on this list.** Both went viral, both stalled. Cause of death: **an open-ended goal, an unbounded task list, and no external verifier.** They generated tasks about tasks and looped forever. | ⛔ **STUDY-ONLY — and this is the closest historical analogue to HFO's current state.** HFO has 58 automations whose products are heartbeats, audits, and wakes, and a `task_results.jsonl` of 0 rows [D]. That is the AutoGPT failure with better paperwork. The cure both projects needed and never got is the same one: **a bounded queue with an external acceptance test per item** — which HFO has *specified* (`task_queue.jsonl` carries `acceptance_test`) and never *run*. | [github.com/Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) · [github.com/yoheinakajima/babyagi](https://github.com/yoheinakajima/babyagi) |

---

## 3 · Durability, workflow, and the actual production pattern

| system | 1-line role | HFO verdict | integration cost | substitutes for | link |
|---|---|---|---|---|---|
| **Temporal** [W] | durable execution: event-history-backed workflows surviving process death, runs measured in days–years | ⏸️ **DEFER — right answer, wrong week.** Needs a server or Cloud account. Prior canon verdict stands [C]. ⭐ **BUT: it is the #1 candidate for the Oracle VM**, which is the one piece of infrastructure the operator has and has not onboarded. | high (server) / medium (Cloud free tier) | the hand-rolled JSONL chain + cron + PAUSED automations | [temporal.io](https://temporal.io) · [LangGraph plugin](https://temporal.io/blog/temporal-langgraph-plugin-durable-execution) |
| **DBOS** [K] | durable execution as a *library* — Postgres-backed, no separate server process | ⭐ **The under-considered row.** Its whole pitch is Temporal's guarantee without Temporal's server, which is precisely the §0-Fact-2 constraint that eliminated Temporal here. It still needs Postgres. | medium | same as Temporal, at lower ops cost | [github.com/dbos-inc/dbos-transact-py](https://github.com/dbos-inc/dbos-transact-py) |
| **Windows Task Scheduler / cron** [D] | the boring one | ✅ **ADOPT — it is the correct durability layer for a 3-loop fleet.** It survives process death, survives reboot, needs no server, and is already on both the laptop and the (unonboarded) Oracle VM. **Do not buy durability you can get from cron until cron has demonstrably failed.** | ~0 | Temporal, for now | built-in |

> **The honest architectural verdict:** the operator's fleet does not have a
> durability problem it can detect. Its loops are not dying mid-run — **they are
> `PAUSED`, or they are running and producing nothing** [D]. Adopting a durable
> execution engine solves a failure the system has never been observed to have,
> at the cost of the only week available to fix the failure it demonstrably has.

---

## 4 · Optimization, observability, and gates

| system | 1-line role | HFO verdict | integration cost | substitutes for | link |
|---|---|---|---|---|---|
| **DSPy + GEPA** [C/K] | programmatic prompt optimization against a metric; GEPA is gradient-free reflective optimization (ICLR 2026), reported ~35× fewer rollouts than GRPO | ✅ **ADOPT #2** — prior canon verdict, unchanged [C `swarm_pipeline_adoption_stack.v0_2.md` §3]. ⚠️ **but it is blocked on a prerequisite nobody flagged: DSPy optimizes against a metric, and HFO has zero executable metrics** (`tests/held_out/` is 18 markdown files, 0 `.py`) [D]. **DSPy before a metric exists is a no-op.** | low (`pip`) | "the prompt feels better" | [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) |
| **Langfuse** [C/K] | OSS LLM observability; auto-instruments many surfaces incl. DSPy; cloud free tier | ✅ **ADOPT #3, cloud tier only** — prior canon verdict, unchanged. Self-hosting is Docker; Docker is the measured blocker. | low (`pip` + cloud key) | guessing at token spend; `cost_tier_routing`'s *assumed* tiers | [langfuse.com](https://langfuse.com) |
| **LangSmith** [K] | LangChain's hosted tracing + eval | ⏸️ DEFER — overlaps Langfuse; picking both is churn. | low | Langfuse | [smith.langchain.com](https://smith.langchain.com) |
| **Braintrust** [K] | eval-first platform, strong on regression suites for LLM output | ⏸️ DEFER — same slot as Langfuse. Revisit if evals (not traces) become the bottleneck. | low | hand-rolled held-out tests | [braintrust.dev](https://braintrust.dev) |
| **W&B Weave** [K] | tracing/eval inside the W&B ecosystem | ⛔ REJECT for HFO — value is ecosystem lock-in the forge doesn't use. | low | Langfuse | [wandb.ai/site/weave](https://wandb.ai/site/weave) |
| **Instructor** [K] | structured output via Pydantic validation + retry on the LLM call | ✅ ⭐ **ADOPT — and it is the cheapest neurosymbolic gate on this list.** A Pydantic model for the chain row and the pheromone is a **deterministic, non-neural, external, fail-closed** validator — all four preconditions of `neurosymbolic_gates.contract.md` P1–P4 — for one `pip install`. Directly closes **G6 (pheromone schema, implementation: "none")**. | **very low** | 6 of 12 gates currently marked *no implementation anywhere* | [github.com/567-labs/instructor](https://github.com/567-labs/instructor) |
| **Guardrails AI** [K] | validation/correction framework around LLM I/O | ⏸️ DEFER — heavier than Instructor for the same first win. Adopt Instructor, measure, then consider. | medium | Instructor | [github.com/guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) |
| **LMQL** [K] | constrained decoding as a query language | ⛔ REJECT — constrains *generation*; HFO's gates need to constrain *effects*. Wrong layer. | high | nothing HFO needs | [lmql.ai](https://lmql.ai) |
| **OPA / Rego** [K] | general-purpose policy engine, deterministic decisions over JSON | ⏸️ **DEFER, high potential.** Exactly right for **G4 (effect-ceiling allowlist)** and **G11 (reason-first presence)**, both currently blocked as B2. But a policy DSL for one operator is overhead until a hand-written Python gate has proven insufficient. | medium | `pretooluse_gate.py` (gen-130, not ported) | [openpolicyagent.org](https://www.openpolicyagent.org) |
| **JSON Schema validation** [K] | the boring one | ✅ **ADOPT.** Same slot as Instructor for JSONL streams. Between them, G6 closes this week. | ~0 | G6 | [json-schema.org](https://json-schema.org) |

---

## 5 · Long-running cloud research agents

| system | 1-line role | relevance | HFO verdict | link |
|---|---|---|---|---|
| **OpenAI Deep Research** [K] | multi-minute–multi-hour autonomous research, browsing + synthesis, returns a cited report | ⭐ **The best existing proof that "launch it and come back later" works** — and note *why*: the task is **read-only**, so there is no effect to gate, and the deliverable is a document, which is verifiable by reading. | ✅ **USE AS-IS** for the operator's research lane. Do not rebuild. | [openai.com](https://openai.com) |
| **Google Deep Research (Gemini)** [K] | same category, Gemini family | ⭐ **This is HFO's cheapest path to a genuine second/third family opinion** — an existing subscription surface, no infrastructure. | ✅ **USE AS-IS** — the Gemini seat in the quorum, without solving Antigravity's consent gate first. | [gemini.google.com](https://gemini.google.com) |

> ⭐ **The generalizable lesson from this row, and it reframes the whole vision:**
> the two most reliably "autonomous" agents in production are both **read-only**.
> Autonomy is easy where effects are absent. Every hard problem in the operator's
> vision — gates, quorum, receipts, reputation — exists **only** because he wants
> agents that *change things*. That is the right ambition, but it means the
> Deep-Research experience is **not** evidence that his vision is close.
> Ratchet effects up one class at a time: `read → local file → git commit →
> deploy → send/spend`. HFO is stuck between *local file* and *git commit*, and
> `pheromone.contract.md` PH-2 already draws that line correctly.

---

## 6 · Scoreboard

| verdict | count | rows |
|---|---|---|
| ✅ **ADOPT this week** | **4** | Instructor · JSON Schema validation · Windows Task Scheduler/cron · (Deep Research surfaces, as-is) |
| ✅ carried from prior canon | 3 | Wrangler/CF Pages #1 · DSPy+GEPA #2 (⚠️ blocked on a metric) · Langfuse cloud #3 |
| ⏸️ DEFER | 6 | LangGraph · Temporal · DBOS · CrewAI · AutoGen · MetaGPT · OPA/Rego · Guardrails · LangSmith · Braintrust |
| ⛔ REJECT / STUDY-ONLY | 8 | OpenHands (Docker) · LMQL · W&B Weave · ChatDev · Devin · SWE-agent · AutoGPT/BabyAGI · IDE agents |

**Net new adoption recommended by this document: one `pip install instructor`
and a JSON-schema file.** Everything else is either already decided, already
present, or correctly deferred. That is the adopt-before-reinvent result and it
should be unsatisfying — an integration problem is not solved by acquiring more
things to integrate.

---

## 7 · Honest flaws

1. **Evidence grades are not uniform and the doc must not be read as if they
   are.** Only Devin's rates and the LangGraph/Temporal 2026 state were
   web-verified this session [W]. Everything marked [K] is model knowledge with a
   canonical URL attached, **not a receipt**. Anyone acting on a [K] row should
   fetch it first. The mission asked for a URL per system; a URL is a pointer,
   not a verification, and conflating them would be exactly the failure this
   capsule set is about.
2. **Devin's numbers come from review aggregators, not from Cognition or a peer
   -reviewed eval.** Reported figures ranged 13.86% → ">50% on SWE-Bench Pro"
   across sources with no consistent methodology. **Treat ~15% unattended /
   35–50% PR-acceptance as an order of magnitude, not a measurement.** The
   directional claim (unattended complex work is well under 50%) is robust
   across every source; the specific numbers are not.
3. **I did not evaluate cost for any row.** Every verdict is on fit and
   integration cost, not on spend. Given that `cost_tier_routing` is unenforced
   (G10: *"not ported"*), that is a real gap in this analysis.
4. **Confirmation-bias check:** this document reaches "adopt almost nothing,"
   which is conveniently consistent with the premise document's thesis. The
   strongest counter-argument is **DBOS** (§3) — it genuinely resolves the
   server-blocker that killed Temporal, and I deferred it partly because it does
   not fit the narrative. **If the operator wants one contrarian pick, it is
   DBOS, and the falsifier is whether Postgres installs on this host in under an
   hour.**
