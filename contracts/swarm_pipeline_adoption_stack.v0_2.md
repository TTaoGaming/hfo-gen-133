```yaml
# AIH2O capsule
doc: contracts/swarm_pipeline_adoption_stack.v0_2.md
schema_id: hfo.gen133.contract.swarm_pipeline_adoption_stack.v0_2
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — I author no scripts/)
valid_time_utc:       2026-08-01T04:54:47Z
transaction_time_utc: 2026-08-01T04:54:47Z
git_head: 60893a4
claim_status: proposed
sealed: false
supersedes: nothing — no v0_1 of this document exists; numbered v0_2 per operator directive
complements:
  - contracts/loop_engineering_gap_analysis.v0_1.md (the measured failure this must not repeat)
  - contracts/software_factory_v0_1.md §0 "rule zero" (a line is not commissioned until it has produced 3 products)
  - contracts/bitemporal_central_memory.v0_1.md (the XTDB attempt, and why it is still blocked)
A_assumption: the operator wants the swarm pipeline OPERATIONAL, and "operational" means producing shippable output — not that more orchestration software is installed
I_input: web research on LangGraph/Temporal/DSPy-GEPA/Langfuse 2026 state · the forge's own measured install history (XTDB blocked on Docker; SQLite fallback live; LiteLLM present)
H_hypothesis: the forge's bottleneck is NOT missing orchestration software — it is that loops produce no product — so the correct adoption count this week is small, and biased toward tools that need ZERO new infrastructure
H2_heldout: install the top-3 and measure PRODUCTS SHIPPED over 7 days. If products-shipped is still zero while three new tools are running, the bottleneck was never tooling and every row in §3 is misdiagnosis.
O_output: 10 concerns surveyed · 3 ADOPT-THIS-WEEK · 4 DEFER · 3 REJECT · 1 install-history reality check
```

# SWARM PIPELINE ADOPTION STACK v0_2

---

## 0 · The reality check that reorders everything below

The operator asked for the top-3 to install this week. Before ranking, two
measured facts from this forge's own record constrain the answer:

**Fact 1 — the forge's diagnosed failure is production, not orchestration.**
`loop_engineering_gap_analysis` records that the most advanced loop in the fleet
**spent 40 commits building and maintaining itself, and its last work item was
recording that its mailbox was empty.** `software_factory_v0_1` §0 responds with
rule zero: *a line is not commissioned until it has produced 3 products that
passed QA. Building the line does not count as running the line.*

An adoption stack is, by construction, more line-building. **Every row below is
therefore under suspicion of being the exact failure mode this forge already
named.**

**Fact 2 — infrastructure-heavy adoption has a measured 0% success rate here,
this week.** The XTDB install (`bitemporal_central_memory.v0_1` §0 + chain rows
`a94eb777…`, `append_receipt_row.py`) is blocked: Docker Desktop's named pipe is
absent, `psql` is not installed on this host, and `psycopg` is missing from the
bundled Python. The result was a SQLite fallback, **43 rows, 0 chain rows
ingested.**

> **Therefore the ranking criterion is not "best tool." It is:
> _does this produce a shippable product this week WITHOUT requiring Docker, a
> server, or a new runtime?_**
>
> That single filter eliminates most of the survey list, including several tools
> that are genuinely better than the ones ranked above them.

---

## 1 · Survey — the ten concerns

Best-in-class per concern, stated so the ranking is a *choice* and not ignorance.

| Concern | Best-in-class 2026 | Note |
|---|---|---|
| Agent orchestration | **LangGraph 1.0** (Oct 2025) | most-deployed OSS agent framework; brought production checkpointing |
| Durable workflow | **Temporal** | event-history-backed durability, runs measured in days/years |
| Prompt compilation | **DSPy + GEPA** | GEPA (ICLR 2026) is gradient-free reflective optimization; reported to beat GRPO by up to 20% with **35× fewer rollouts** |
| Observability | **Langfuse** | OSS, auto-instruments 50+ AI surfaces incl. DSPy |
| LLM router | **LiteLLM** | ✅ already present in this workspace |
| Memory backend | mem0 · Letta · Zep · **XTDB** | XTDB chosen for bitemporality; ⛔ install blocked |
| Task queue | Celery · RQ · Kafka | — |
| Actor supervision | Dapr Actors · Orleans · OTP | — |
| Multi-objective evolutionary | **pyribs** (MAP-Elites) · QDax | strong fit for phenotype search; no current consumer |
| Content publishing | **Cloudflare Pages + Wrangler** | the demos already deploy this way |

**The crucial architectural finding from research** (and it resolves a false
choice the operator's list implies): **LangGraph and Temporal are not
competitors.** The converged 2026 pattern is *LangGraph for reasoning, Temporal
for orchestration* — Temporal owns the durable multi-hour lifecycle, a Temporal
activity spins up a LangGraph agent for the reasoning-intensive subtask.
Temporal now ships an official LangGraph plugin. A LangGraph run lives in a
single process: **checkpoints are not durable execution — if the process dies,
the run dies with it.**

That matters for HFO specifically, whose whole doctrine is durable loops
surviving process death. It means **LangGraph alone cannot deliver HFO's stated
durability requirement**, and Temporal is the component that would — which is
also the component that needs a server the host cannot currently run.

---

## 2 · Filtering by the §0 criterion

| Candidate | Needs Docker/server/new runtime? | Produces a product this week? | Verdict |
|---|---|---|---|
| Temporal | ✅ **yes** (server or Cloud) | no | ⏸️ **DEFER** — right answer, wrong week. Same class as XTDB. |
| LangGraph | no (pip) | indirectly | ⏸️ **DEFER** — see §2.1 |
| DSPy + GEPA | no (pip) | **yes** | ✅ **ADOPT #2** |
| Langfuse | self-host = Docker; **cloud = no** | yes (visibility) | ✅ **ADOPT #3**, cloud tier only |
| Wrangler / CF Pages | no (npm) | **yes — an actual URL** | ✅ **ADOPT #1** |
| LiteLLM | already present | — | ✅ keep |
| pyribs | no (pip) | no consumer | ⏸️ DEFER |
| mem0 / Letta / Zep | varies | no | ⏸️ DEFER — memory lane is already mid-flight on XTDB/SQLite; adding a fourth store is churn |
| Celery / RQ / Kafka | ✅ yes (broker) | no | ❌ REJECT — a single-operator forge has no queue-depth problem |
| Dapr / Orleans / OTP | ✅ yes | no | ❌ REJECT — actor supervision for a swarm that has not shipped 3 products is premature |

### 2.1 Why LangGraph is deferred despite being the obvious pick

It is the highest-profile tool on the list and the one most likely to be
expected here. Deferring it needs a reason, not a shrug:

1. Its durability story is **exactly the thing HFO already has** — the JSONL
   chain with `prev_sha256` links, `claim_status`, and receipts is a durable
   append-only log. Adopting LangGraph checkpointing means running two
   persistence models with different truth semantics.
2. Its checkpoints **do not survive process death** (§1), which is the specific
   guarantee HFO's doctrine demands. So it does not close the gap it appears to.
3. The forge's agents are **heterogeneous substrates** (Claude Code, Codex,
   cloud ChatGPT) coordinated through files and contracts. LangGraph orchestrates
   *in-process Python*. Most of the fleet is not in that process.

> **Adopt LangGraph when a single Python-hosted agent needs an internal reasoning
> graph. That is not the current bottleneck.** Adopt Temporal when durability
> across process death becomes the measured blocker *and* the host can run a
> server. Both are correct later; neither is correct this week.

---

## 3 · The three to install this week

### #1 · Wrangler / Cloudflare Pages — *ranked first because it is the only one that ships a product*

```bash
npm install -g wrangler
wrangler login
wrangler pages deploy ./dist/hfopiano_v512 --project-name=demo01
```

- **Integration point:** `spatial_factory_framework` station [8] PUBLISH. The
  demos already carry `_headers`, `404.html`, `sw.js` — Cloudflare Pages
  conventions. This is completing a path already 90% built, not opening a new one.
- **First PDCA loop:** *Plan* deploy reskin #1 → *Do* `wrangler pages deploy` →
  *Check* a stranger loads the URL and sees a different brand → *Act* record the
  deploy command in the factory runbook so reskin #2 costs one command.
- **Why #1:** it is the only item in this entire document that converts existing
  work into a **stranger-visible artifact**. Per the strife/splendor corpus,
  every splendor miss is an internal capability and the one hit is the one thing
  deployed. **The deficit is deployment, not capability.**
- **It also clears blocker B2** (deploy mechanism for handpiano.com is currently
  *inferred* from `_headers`/`sw.js`, not verified).

**FALSIFIER · W-F1:** if `wrangler pages deploy` fails because handpiano.com is
on Netlify rather than Cloudflare, B2 is resolved in the *other* direction and
#1 becomes `netlify-cli`. **The inference has not been verified** — this is the
same source-vs-target confusion recorded as strife candidate S-008, and it is
called out here rather than repeated.

### #2 · DSPy + GEPA

```bash
pip install dspy gepa
```

- **Integration point:** the `quality_gate` in `hfo_universal_genotype` §7 and
  the held-out test specs. GEPA optimizes *textual components against a metric* —
  and HFO's held-out tests **are** metrics. This is a rare structural fit.
- **First PDCA loop:** take ONE narrow, already-specified classification —
  strife/splendor admissibility (whose bar is written down in
  `strife_splendor_rehydration.v0_1`, and whose §6.3 mining pass was explicitly
  deferred as "a judgment call a mechanical pass should not fake") → hand-label
  20 examples → GEPA-optimize a classifier prompt → measure against held-out
  labels.
- **Why #2:** it directly attacks the RBR doctrine's root cause. GEPA is
  *reflective optimization against a measured metric* — a machine-verified
  propose/dispose split, which is defense-in-depth rank 3 and 6 in the
  Reflex-Before-Reasoning ladder. It replaces "the prompt feels better" with a
  number.
- **Cost warning honored:** 35× fewer rollouts than GRPO is still rollouts.
  Pin a rollout budget before the first run; this is `cost_tier_routing`'s
  problem and it should be routed through the already-present LiteLLM.

**FALSIFIER · D-F1:** if GEPA cannot beat a hand-written prompt on 20 held-out
strife/splendor labels, it is not earning its rollout spend on this corpus size,
and #2 drops behind Langfuse.

### #3 · Langfuse — **cloud tier only**

```bash
pip install langfuse
# cloud.langfuse.com — free tier. DO NOT self-host this week.
```

- **Integration point:** wrap LiteLLM calls; auto-instruments DSPy, so #2 becomes
  observable for free.
- **First PDCA loop:** instrument one valkyrie lane for 7 days → read actual
  token spend and latency per lane → compare against `cost_tier_routing`'s
  *assumed* tiers.
- **Why #3, and why explicitly not self-hosted:** self-hosting is Docker, and
  Docker is the measured blocker (§0 Fact 2). Choosing the cloud tier is
  choosing the version that can actually run on this host this week.
- **Why it matters:** `cost_tier_routing.v0_1` assigns cost tiers on estimate.
  This is the direct cure for **L_BUDGET_WITHOUT_RECEIPT** — probe first,
  validate empirically, then scale.

**FALSIFIER · L-F2:** if measured per-lane spend matches `cost_tier_routing`'s
estimates within ±20%, the estimates were fine and the instrumentation is
overhead — keep it only on the most expensive lane.

---

## 4 · The ordering claim, stated so it can be attacked

The three are ranked **publish → optimize → observe**, deliberately inverting the
conventional order (observe → optimize → publish).

The conventional order is correct for a system that is shipping and wants to ship
better. **This forge is not shipping.** Instrumenting and optimizing a pipeline
that has produced zero stranger-visible products this generation would produce
excellent telemetry about a machine that makes nothing — which is a more precise
restatement of the exact failure `loop_engineering_gap_analysis` measured.

> **#1 alone satisfies the operator's actual ask.** "Make the swarm pipeline
> operational" is satisfied by a URL a stranger can load, and by nothing else.
> #2 and #3 are improvements to a line that #1 proves exists.

**FALSIFIER · O-F1 (against this whole document):** if after 7 days all three are
installed and **products shipped is still zero**, then tooling was never the
bottleneck, §3 is misdiagnosis, and the correct next move is the one that has
been ranked #1 across four consecutive canon documents without execution —
*operator sends messages to prior paying clients.* That non-execution remains the
most decision-relevant fact in the forge, and no adoption stack changes it.

---

## 5 · Adoption ledger

| # | Tool | Decision | Infra needed | Gate |
|---|---|---|---|---|
| 1 | Wrangler / CF Pages | ✅ **THIS WEEK** | npm only | W-F1 |
| 2 | DSPy + GEPA | ✅ **THIS WEEK** | pip only | D-F1 |
| 3 | Langfuse (cloud) | ✅ **THIS WEEK** | pip + free account | L-F2 |
| 4 | LiteLLM | ✅ keep (present) | — | — |
| 5 | Temporal | ⏸️ DEFER | server | when durability-across-process-death is *measured* as blocking |
| 6 | LangGraph | ⏸️ DEFER | pip | when one Python agent needs an internal graph |
| 7 | XTDB | ⏸️ BLOCKED | Docker | operator starts Docker Desktop |
| 8 | pyribs | ⏸️ DEFER | pip | when a phenotype search has a fitness function with a consumer |
| 9 | mem0 / Letta / Zep | ⏸️ DEFER | varies | not until the XTDB/SQLite lane resolves |
| 10 | Celery / RQ / Kafka | ❌ REJECT | broker | single-operator forge has no queue-depth problem |
| 11 | Dapr / Orleans / OTP | ❌ REJECT | runtime | premature before rule-zero's 3 products |

---

## 6 · Honest flaw

This document recommends installing three things, and its own §0 argues that
installing things is this forge's characteristic failure mode. That tension is
real and I have not fully resolved it — I have only biased the list toward
zero-infrastructure tools and put the one that ships a product first.

A stricter reading of `software_factory_v0_1` rule zero says the correct
recommendation is **#1 only, and nothing else until three products have
shipped.** I did not make that recommendation because the operator explicitly
asked for a top-3, and narrowing a requested scope to one item is the operator's
call to make, not mine. **I am flagging it here so the call is available:** if
you want the strictest version consistent with your own doctrine, take #1 this
week and hold #2 and #3 until reskin #1 is live at a URL.

Second flaw: every 2026 claim about LangGraph, Temporal, GEPA and Langfuse comes
from **search-result summaries and vendor/marketing-adjacent blog posts**, not
from running the tools or reading primary docs first-hand. The GEPA numbers
(20% over GRPO, 35× fewer rollouts) are **the project's own reported figures**,
carried here as claims-with-attribution, not as verified results. Per S-008: I
have provenance on what the sources *say*, not on what this host can *run*.

---

*Sources:* [LangGraph vs Temporal (LangChain)](https://www.langchain.com/resources/langgraph-vs-temporal) ·
[Temporal LangGraph plugin](https://temporal.io/blog/temporal-langgraph-plugin-durable-execution) ·
[Temporal vs LangGraph 2026 (Cordum)](https://cordum.io/blog/temporal-vs-langgraph) ·
[Durable Agent Execution in Production 2026](https://agentmarketcap.ai/blog/2026/04/10/durable-agent-execution-production-temporal-modal-event-sourced) ·
[GEPA (GitHub)](https://github.com/gepa-ai/gepa) ·
[DSPy GEPA overview](https://dspy.ai/api/optimizers/GEPA/overview/) ·
[Optimizing GEPA for production (Decagon)](https://decagon.ai/blog/optimizing-gepa-for-production) ·
[Langfuse DSPy integration](https://langfuse.com/integrations/frameworks/dspy)
