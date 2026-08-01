```yaml
# AIH2O
schema_id: hfo.gen130.industry_pattern_exemplars.v0_1
unifying_phrase: "Producer, Verifier, Consumer -- all three or none"
doc: SIGRUN_INDUSTRY_PATTERN_EXEMPLARS_20260731.md
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5
valid_time_utc: 2026-08-01T06:10:00Z
git_head: b857c16
claim_status: partial — install inventory is MEASURED; integration costs are estimates
A_assumption: HFO needs to adopt exemplars it does not have
I_input: pip list on the main interpreter + 3 venv site-packages scans, run this session
H_hypothesis: FALSIFIED — 12 of the named exemplars are ALREADY INSTALLED; only one gap is real
H2_heldout: name an exemplar in the operator's list that is both absent and load-bearing. Exactly one qualifies (pyribs).
O_output: measured inventory · the "lost them" mechanism · top-5 · adopt/don't table
```

# INDUSTRY PATTERN NAMES + EXEMPLARS

## 0 · The measured answer, before any recommendation

The operator wrote: *"we already tried most of these already and then lost them."*
**That is correct, and I found the mechanism.**

### ✅ FALSIFIER RUN AND PASSED (2026-08-01T06:20Z)

I ran my own falsifier against `tools/hfo-python.cmd`'s interpreter — the one
agents actually use:

```
OK   langgraph
OK   langgraph.checkpoint.sqlite
OK   opentelemetry.sdk
OK   litellm
```

**All four import cleanly.** Recommendations #1, #2, #3 and #5 below are not
"probably installed" — they are **verified reachable from the agent runtime.**
The only thing standing between them and use is that nobody has called them.

`work/.venv_cots` last modified **2026-06-27** (34 days ago). It *is* referenced
— in `canon/adr/g130-0104-cots-assimilation-acl-vacuole.md`,
`contracts/evo_search_harness.v0_1.md`, and three other **documents**. Referenced
by prose, executed by nothing. That is the orphaning, precisely: **documented
adoption without runtime adoption.**

### Already installed in the MAIN interpreter — usable today, unused

| exemplar | version | pattern | HFO status |
|---|---|---|---|
| **LiteLLM** | 1.90.2 | OpenAI-compatible proxy / model router | proven hand-run; not wired |
| **LangGraph** | 1.2.6 | supervisor + **`interrupt()`** HITL | **unused — this is the class-approval primitive** |
| **langgraph-checkpoint-sqlite** | 3.1.0 | durable workflow checkpointing | **unused — this is most of Ratatoskr's "missing organ"** |
| **LangChain** | 1.3.11 (+anthropic 1.4.8, openai 1.3.3) | LLM app framework | partial |
| **MCP** | 1.28.1 | tool orchestration protocol | **in use** ✓ |
| **OpenTelemetry** | api+sdk 1.43.0 | traces | **unused** |
| **ollama** | 0.6.2 | local model client | proven this session ✓ |
| **anthropic / openai** | 0.112.0 / 2.44.0 | provider SDKs | in use ✓ |

### Orphaned in `work/.venv_cots` — installed, invisible, unreachable

| exemplar | version | pattern |
|---|---|---|
| **temporalio** | **1.29.0** | durable workflow execution |
| **DBOS** | **2.24.0** | durable execution on Postgres/SQLite |
| **DSPy** | **3.2.1** | declarative LLM pipeline programming |
| **prometheus_client** | **0.25.0** | metrics |

> ### 🔍 THE "LOST THEM" MECHANISM — measured, not theorised
>
> **They were installed into an isolated venv that no runtime path points at.**
> Not deleted. Not broken. **Orphaned.** `tools/hfo-python.cmd` runs the main
> interpreter; `work/.venv_cots` is a sealed pocket. Four mature exemplars have
> been sitting one directory away, fully installed, for weeks.
>
> This is `CAPACITY_AMNESIA` in its tooling form, and the cure is **not**
> `pip install`. It is: **point one runtime at what already exists.**
>
> **What makes re-adoption stick this time:** a `capacity_manifest.jsonl` row per
> exemplar whose `acceptance_test` is an *import + one real call from the
> interpreter agents actually use.* An exemplar with no such test is not adopted,
> it is merely downloaded — which is precisely the state all four are in now.

### Genuinely missing, and only one matters

| exemplar | status | verdict |
|---|---|---|
| **pyribs** (MAP-Elites) | **ABSENT** | **the one real install.** MIT, Berkeley/Caltech, `pip install ribs` |
| QDax / evosax / EvoJAX | absent | JAX-heavy; overkill at 2 occupied grid cells |
| CrewAI / AutoGen | absent here | **do not adopt** — LangGraph already installed and strictly better for HITL |
| Langfuse / Phoenix / Helicone | absent | month-3; OTel is already installed and unused |
| TrueSkill / EigenTrust | absent | the reputation math is ~50 lines; not worth a dependency yet |
| Celery / RQ | absent | **do not adopt** — `task_queue.jsonl` works and is kernel-adjacent |
| Temporal *server* | absent (client only) | the client is orphaned; the server is a month-scale lift |

---

## §17.1 · TOP 5 TO ADOPT THIS WEEK

Ranked by runtime-per-hour, given the runtime-not-architecture push. **Four of
five are wiring, not installing.**

### 1 · LangGraph `interrupt()` — the class-approval primitive
- **Pattern:** durable human-in-the-loop / propose-dispose split
- **Install:** *already installed* (`langgraph 1.2.6`). Zero commands.
- **Integration point:** wrap the outreach send step. Graph runs autonomously
  through enrich → draft → queue, then `interrupt()` before send; operator
  approves the **class** once; graph resumes and Instantly executes.
- **Runtime benefit:** this is literally §11.8 / §15's "approve the class not the
  instance," and it is the pattern every 2026 platform converged on.
- **Cost:** ~4h. $0. Low risk (reversible steps only before the interrupt).
- **Falsifier:** if `interrupt()` cannot survive a process restart with the
  sqlite checkpointer, it is not durable and Temporal becomes necessary.

### 2 · langgraph-checkpoint-sqlite — durable execution without Temporal
- **Pattern:** event-sourced workflow / checkpoint-replay
- **Install:** *already installed* (3.1.0).
- **Integration point:** the pull-loop. Replaces the claim-TTL machinery I
  specced in `mape_k_schedule_adapter.v0_1.md` §2 with a maintained implementation.
- **Runtime benefit:** kills the "wrapper dies with the session" failure that has
  blocked Day 1 all session.
- **Cost:** ~4h. $0.
- **Falsifier:** if it cannot express claim/TTL/revert semantics, keep the JSONL
  queue and use it only for checkpointing.
- **Why not Temporal/DBOS:** both are orphaned in `.venv_cots`, both need a
  server or Postgres, and **LangGraph's checkpointer is already in the
  interpreter agents actually run.** Adopt the nearer one.

### 3 · LiteLLM as a running proxy — the feeding proboscis
- **Pattern:** OpenAI-compatible gateway / model router with fallback ladder
- **Install:** *already installed* (1.90.2); `litellm --config <cfg>` to run.
- **Integration point:** every valkyrie calls one endpoint; the §16 adapter
  becomes a config file rather than code.
- **Runtime benefit:** the $0 mesh (measured working this session) becomes
  addressable by any agent without per-provider code, and cost tracking comes free.
- **Cost:** ~2h. $0.
- **Falsifier:** if the proxy adds >2s overhead to a 26s local call, call Ollama direct.

### 4 · pyribs — the only genuine install
- **Pattern:** **MAP-Elites / Quality-Diversity** (Mouret & Clune 2015; Cully et
  al., *Nature* 2015)
- **Install:** `pip install ribs` — MIT, maintained (Berkeley/Caltech, ICAROS lab)
- **Integration point:** the §16.2 archive. Do **not** hand-roll grid + elite
  bookkeeping; that is exactly the reinvention the operator is warning against.
- **Runtime benefit:** deferred — **the grid has 2 occupied cells and n=1 each.**
- **Cost:** ~30 min install, ~3h integration.
- **⚠️ Honest ranking note:** this is #4, not #1, *because MAP-Elites over 2 data
  points is theatre.* Adopt the library now so the archive is standard, but the
  real work is filling cells, which needs no library at all.
- **Falsifier:** if after 30 days the grid has <20 occupied cells, pyribs is
  premature and a dict would have done.

### 5 · OpenTelemetry — turn on the traces you already have
- **Pattern:** distributed tracing (the observability triad's middle leg)
- **Install:** *already installed* (api+sdk 1.43.0).
- **Integration point:** span per queue task: claim → execute → result. Export to
  a local file first; no collector needed on day one.
- **Runtime benefit:** answers "which loop is decoration" with **measurement**
  rather than the rubric the audit sonnet is currently guessing with.
- **Cost:** ~3h. $0.
- **Falsifier:** if spans do not distinguish real-work loops from heartbeat loops,
  the instrumentation is at the wrong boundary.

**Total: ~16 hours, $0, one `pip install`.** Nothing else in the operator's list
should be adopted this week.

---

## §17.2 · Pattern → exemplar table (condensed to decisions)

| HFO concept | pattern name | exemplar | license | verdict |
|---|---|---|---|---|
| adapter / proboscis | OpenAI-compatible gateway | **LiteLLM 1.90.2** | MIT | **adopt-tomorrow (installed)** |
| model routing by cost | LLM router | RouteLLM / OpenRouter / Portkey | mixed | **defer** — LiteLLM covers it |
| class approval | HITL interrupt / propose-dispose | **LangGraph 1.2.6** | MIT | **adopt-tomorrow (installed)** |
| durable workflow | event-sourced checkpoint-replay | **langgraph-checkpoint-sqlite 3.1.0** | MIT | **adopt-this-week (installed)** |
| durable workflow (heavy) | durable execution | Temporal 1.29.0 / DBOS 2.24.0 | MIT / MIT | **defer — orphaned in `.venv_cots`; needs server/PG** |
| reputation grid | MAP-Elites / Quality-Diversity | **pyribs** | MIT | **adopt-this-week (install)** |
| QD at scale | QD on JAX | QDax / evosax / EvoJAX | Apache-2/MIT | **do-not-adopt** — overkill |
| declarative prompting | programmatic LLM pipelines | **DSPy 3.2.1** | MIT | **adopt-this-month** — orphaned; strong fit for §16 prompt-tuning |
| tool protocol | MCP | **mcp 1.28.1** | MIT | **in use** ✓ |
| agent teams | multi-agent orchestration | CrewAI / AutoGen / OpenAI Swarm | mixed | **do-not-adopt** — duplicates LangGraph, weaker HITL |
| traces | OpenTelemetry | **otel 1.43.0** | Apache-2 | **adopt-this-week (installed)** |
| metrics | Prometheus | **prometheus_client 0.25.0** | Apache-2 | **adopt-this-month** — orphaned |
| LLM observability | LLM tracing | Langfuse / Phoenix / Helicone | MIT / Elastic | **defer** — use OTel first |
| task queue | pull-based work queue | `task_queue.jsonl` (own) | — | **keep** — Celery/RQ add a broker for no gain |
| pull-based work | Toyota Production System / kanban | — | — | **already the doctrine** |
| reputation math | EigenTrust / TrueSkill / Thompson sampling | — | — | **hand-roll** — ~50 lines, no dep |
| agent eval | LLM-as-judge harness | PromptFoo / Braintrust / RAGAS | mixed | **adopt-this-month** — needed for MAP-Elites `quality` |
| cold email | cold email at scale | **Instantly** | SaaS | **in use, paid** ✓ |
| enrichment | waterfall enrichment | Clay / Apollo / Hunter | SaaS | **adopt-this-month** — ~$50–150, fixes B2 |
| list validation | email verification | NeverBounce / MillionVerifier | SaaS | **adopt with enrichment** — the bounce-test gate |
| LinkedIn | LinkedIn automation | HeyReach (native Instantly integration) | SaaS | **defer** — no LinkedIn account exists |
| deploy | static site / edge | **Cloudflare Pages** (`cf-wrangler` in node_modules) | — | **adopt-tomorrow (installed)** |
| fork-and-reskin | template repository | GitHub template repos + worktrees | — | **adopt-this-week** — free, replaces the reskin script |
| governance | commons governance | **Ostrom's 8 principles** | — | **already mapped** (§7.2) |
| stigmergy | response-threshold task allocation | Bonabeau FRT | — | **adopt** — one field change (§11.9) |

---

## §17.3 · What would make re-adoption stick

The four orphaned packages are the proof that installing is not adopting.

**Rule, stated as a gate:** an exemplar is `adopted` only when a
`capacity_manifest.jsonl` row exists whose `acceptance_test` is a command that
**imports it from `tools/hfo-python.cmd`'s interpreter and makes one real call**,
verified by an agent that did not install it. Anything less is `unverified`.

Applied today, that rule scores: LiteLLM `verified` (proven hand-run), ollama
`verified` (2 inferences this session), MCP `verified` (in use), and **LangGraph,
OTel, Temporal, DBOS, DSPy, Prometheus all `unverified`** despite being installed.
That is the honest state.

## Honest flaws

- The inventory is **measured**; every integration-hour estimate is a guess.
- I scanned `pip list` on the main interpreter plus three venv `site-packages`
  directories. Other environments (conda, node, global npm, other worktrees) were
  **not** scanned — more may be orphaned elsewhere.
- I did not verify pyribs' current version or that `pip install ribs` succeeds on
  this host; the license and provenance are from prior knowledge, not fetched.
- I recommend LangGraph over Temporal/DBOS partly because it is in the reachable
  interpreter. That is a proximity argument, not a technical one. If durable
  execution later needs multi-day workflows or cross-host recovery, Temporal is
  the better tool and this call should be revisited.
- **Frame-capture check:** "you already have everything, just wire it" is the
  fourth time today I have produced that shape of finding. It is either a genuine
  dominant pattern in this codebase or a lens I have fallen in love with. The
  defence is that every row above names a version string you can check in ten
  seconds.

---
*FALSIFIER:* run `tools/hfo-python.cmd -c "import langgraph, opentelemetry"` — if it fails, my top-2 recommendations are wrong and those are orphaned too ·
*cost_of_delay:* LOW on installs; **HIGH on LangGraph `interrupt()`** — it is the class-approval mechanism blocking the outreach lane, installed and unused for weeks ·
*leverage_level_meadows:* L6 information flows · *domain_cynefin:* Complicated
