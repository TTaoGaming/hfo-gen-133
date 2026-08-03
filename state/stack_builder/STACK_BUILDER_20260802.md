```yaml
# AIH2O capsule
doc: state/stack_builder/STACK_BUILDER_20260802.md
schema_id: hfo.gen133.stack_builder_v0.v0_1
callsign: STACK-BUILDER-V0
generation: 133
authored_by: sonnet-5 · Claude Code
now_utc: 2026-08-02T05:10:00Z
clock_source: host_read              # bash `date -u -Iseconds`, this session
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md, areas/quorum_research/SIGRUN_ROOT_CAUSE_LEAK_20260802.md
claim_status: wired_with_receipts    # every capability below is a runtime probe result, executed this session
ships_running_code: tools/stack_builder/*.py, state/ssot/capability_registry.json (5 new entries + 1 fixed probe arg)
```

# STACK BUILDER v0 — Postgres/pgvector/LiteLLM/DBOS/CrewAI, runtime-verified

Operator directive: stand up litellm + crewai + dbos + postgres + pgvector,
"anything else we can verify working," ship a real Olrun-writes /
Sigrun-reads memory demo, register capabilities, run the census. Boring
engineering, execute not document.

**Headline: the core memory-gap flow works, end to end, verified by
runtime probe, not prose.** Docker Desktop's WSL2 engine would not come up
(twice now, across two separate sessions) — pivoted to installing Postgres
16 + pgvector directly inside the operator's own WSL Ubuntu-24.04 distro,
which has passwordless sudo. sentence-transformers is DEAD (torch hangs);
the memory demo uses Ollama's local nomic-embed-text instead, which was
already running on this machine.

---

## 1. Install log

| piece | command | exit | notes |
|---|---|---|---|
| litellm, dbos, crewai, sentence-transformers, psycopg2-binary, pgvector, langfuse | `python -m pip install --user litellm dbos crewai sentence-transformers psycopg2-binary pgvector langfuse` | **0** | ~50 dependency-version warnings against other already-installed projects in the same shared user site-packages (aider-chat, openhands-ai, garak, guardrails-ai, dspy, gpt-researcher, smolagents, pydantic-ai-slim, etc.) — none fatal to the installs actually exercised below |
| Docker Desktop engine (attempt 1) | launched `Docker Desktop.exe`, polled `docker ps` for ~100s | **FAILED** | `npipe:////./pipe/dockerDesktopLinuxEngine` never accepted a connection in time |
| Docker Desktop engine (attempt 2, diagnostic) | confirmed `dockerDesktopLinuxEngine` pipe exists, WSL `docker-desktop` distro boots instantly (`wsl -d docker-desktop -- echo` returns immediately) | **FAILED** | pipe exists but `docker version`/`docker ps` both hang past 30s — the backend behind the pipe is not answering. Matches `tools/xtdb/INSTALL_ATTEMPT.md`'s prior-session finding exactly (15 min, never came up) |
| Postgres 16 + pgvector (pivot: WSL Ubuntu-24.04, not Docker) | `wsl -d Ubuntu-24.04 -- sudo apt-get install -y postgresql postgresql-contrib postgresql-16-pgvector` | **0** | clean install, no admin needed — passwordless sudo already configured in the operator's own WSL distro |
| Postgres network config | `listen_addresses='*'` + `pg_hba.conf` host rule + `ALTER USER postgres PASSWORD` + `CREATE DATABASE hfo_stack` + `CREATE EXTENSION vector` | **0** | reachable from Windows at `127.0.0.1:5432/hfo_stack` via WSL2's default localhost forwarding |
| sentence-transformers runtime | `import torch` | **HUNG** | tested to 180s with no exception and no output — dead on this machine's shared site-packages, not merely slow. Not chased further; see honest_flaw |

---

## 2. Runtime probe log

| capability | probe | output | verdict | industry_convergence | named_winners_using_it | external_fitness_verdict |
|---|---|---|---|---|---|---|
| `cap-litellm-completion` | `python tools/stack_builder/probe_litellm.py` | `RAW_RESPONSE: '4'` for "what is 2+2" against `ollama/llama3.2:3b` | **ALIVE** | HIGH | Netflix, Lemonade, Rocket Money | **INDUSTRY_PROVEN** |
| `cap-postgres-durable-scratchpad` (Postgres+pgvector) | `python tools/stack_builder/check_scratchpad_alive.py` | `scratchpad_rows_last_24h=1` | **ALIVE** (conditional — see honest_flaw on WSL idle-shutdown) | HIGH | OpenAI, Supabase, Neon | **INDUSTRY_PROVEN** |
| `cap-dbos-workflow-execution` | `python tools/stack_builder/check_dbos_alive.py` | `dbos_success_rows_last_hour=1`; `dbos.workflow_status` row: `workflow_uuid=5e625ec7-8fb3-4d27-b955-b8c00be17e43, status=SUCCESS, name=olrun_write_workflow` | **ALIVE** | MEDIUM | Dosu, Yutori, Supabase | **EMERGING_PATTERN** |
| `cap-pgvector-semantic-recall` | `python tools/stack_builder/probe_pgvector_recall.py` | query *"what did Olrun observe last night about the factory pipeline?"* → top match `cosine_sim=0.7677` (threshold 0.7) | **ALIVE** | HIGH (inherits Postgres+pgvector's) | OpenAI, Supabase, Neon | **INDUSTRY_PROVEN** |
| `cap-crewai-runtime` | `python tools/stack_builder/crewai_demo.py` | `CREW_OUTPUT='...The researcher cannot provide information about durable execution engines.'` (non-empty, real, unmocked `kickoff()`) | **ALIVE** — flips Sigrún's pre-registered `DEAD` falsifier (`repo_grep: from crewai`) because both the import AND a real `kickoff()` fired | MEDIUM, vendor-stat-heavy | DocuSign (real case study); "60% Fortune 500" is unaudited vendor marketing | **EMERGING_PATTERN — adopt with caveat** |
| `cap-sentence-transformers-embed` | `python tools/stack_builder/probe_embed.py` | no output after 180s+ | **DEAD** | n/a | n/a | n/a — dead in this environment, not an industry-fitness question |
| Aider (pre-existing) | not re-probed this session; `cap-aider-code-lane` already ALIVE in the registry | — | unchanged | not evaluated this session | — | — |
| Langfuse | not attempted — needs a cloud account signup, which is an "explicit permission" action outside this session's install/run/query pre-authorization | — | **DEFERRED** | not evaluated this session | — | — |
| GitHub Actions census workflow | not touched this session — `cap-supervision-tree` stays whatever the last census recorded | — | unchanged | not evaluated this session | — | — |

**Full external-fitness detail, alternatives comparison (LangGraph / OpenAI
Agents SDK / Claude Agent SDK / Vercel AI SDK), and the honest tension
between industry convergence and HFO's own adoption history: see §8.5,
added mid-session per the operator's reframe.**

**Honest note on the CrewAI content:** `llama3.2:3b` answered the research
task with a refusal-shaped non-answer rather than a fact, and the writer
agent faithfully compressed the refusal. That is a **model-quality**
observation about a 3B local model under a terse prompt, not a wiring
failure — the falsifier only requires real, non-mocked `kickoff()` output,
which this is.

---

## 3. Memory demo transcript — Olrun writes, Sigrun reads

**Step 1 — Olrun writes (DBOS workflow, actual command + output):**

```
$ python tools/stack_builder/dbos_demo.py
...
22:52:42 [INFO] (dbos:_dbos.py:680) DBOS launched!
WORKFLOW_ID=5e625ec7-8fb3-4d27-b955-b8c00be17e43
SCRATCHPAD_ROW_ID=1
```

**Postgres receipt, queried directly (separate command, after the workflow exited):**

```
SELECT workflow_uuid, status, name, created_at FROM dbos.workflow_status;
('5e625ec7-8fb3-4d27-b955-b8c00be17e43', 'SUCCESS', 'olrun_write_workflow', 1785646362783)

SELECT id, author, left(body,60), written_utc, workflow_id FROM olrun_scratchpad;
(1, 'olrun', 'Olrun observed the factory pipeline stalling overnight -- th', 2026-08-01 22:52:42.878602-06:00, '5e625ec7-8fb3-4d27-b955-b8c00be17e43')
```

**Step 2 — Sigrun reads, fresh process, semantic query only (actual command + output):**

```
$ python tools/stack_builder/probe_pgvector_recall.py
QUERY='what did Olrun observe last night about the factory pipeline?'
  id=1 author=olrun sim=0.7677 written=2026-08-01 22:52:42.878602-06:00 body='Olrun observed the factory pipeline stalling overnight -- the outreach queue dra'
TOP_MATCH_SIM=0.7677
PROBE_PASS=True
```

Sigrun's query process never read `dbos_demo.py`'s source, never shared a
Python object with it, and never touched a markdown file. It rehydrated the
fact by cosine similarity over an embedding computed independently, in a
separate process invocation, against a row written by a DBOS-checkpointed
workflow. **This is the shape Sigrún's root-cause row 77 asked for**: a
queryable execution record that exists independently of prose.

---

## 4. Updated capability_registry.json

6 new entries added to `state/ssot/capability_registry.json`:
`cap-litellm-completion`, `cap-postgres-durable-scratchpad`,
`cap-dbos-workflow-execution`, `cap-pgvector-semantic-recall`,
`cap-sentence-transformers-embed` (registered DEAD, per row 77's own
discipline — a registry entry at claim-time even for a failure).
`cap-crewai-runtime` already existed (Sigrún pre-registered it DEAD as a
falsifier) and is expected to flip ALIVE from this session's `crewai_demo.py`
now that `from crewai import` is real repo content, not a mention.

---

## 5. Capability census, before vs after

Baseline (row 77, 2026-08-02T04:16:28Z, 14 registered capabilities):
**ALIVE=6 DEAD=8 LEAKED=1**

**This session's actual run** (`state/ssot/capability_census/20260802T051954Z.json`,
20 registered capabilities — 6 more were added between row 77 and now by
other work this generation, not only by this session):

```
CAPABILITY CENSUS 20260802T051954Z   (vs 20260802T045219Z.json)
ALIVE=12  DEAD=11  LEAKED=0
EXIT=0
```

**This session's own net contribution: +5 ALIVE, 0 leaked** —
`cap-litellm-completion`, `cap-postgres-durable-scratchpad`,
`cap-dbos-workflow-execution`, `cap-pgvector-semantic-recall` (all new
this session), and `cap-crewai-runtime` (pre-existing entry, flipped from
Sigrún's pre-registered DEAD falsifier to ALIVE by tonight's
`crewai_demo.py`). `cap-sentence-transformers-embed` was added and
correctly reports DEAD. `LEAKED=0` — nothing that was previously ALIVE
regressed.

**A genuine supervision-tree bug was found and fixed while getting this
number**, worth reporting on its own merits: the census's `cli` probe type
uses `subprocess.run(shell=True, capture_output=True, timeout=60)`. When
the child process itself hangs (as `import torch` does on this machine —
see §7), a grandchild process inherits the stdout/stderr pipe handles, and
even after the 60s timeout fires and the immediate child is killed, the
still-running grandchild keeps the pipe open — so `subprocess.run` never
sees EOF and blocks **forever**, not for 60 seconds. Three consecutive
census runs (300s, 480s, and one direct in-process debug run) all
hung indefinitely on exactly this one probe, silently orphaning **5
separate stuck `probe_embed.py` processes** across attempts before the
cause was isolated by probing each registry entry one at a time with
timestamps. Fixed by rewriting that one probe's `arg` to use PowerShell's
`Start-Process` + `WaitForExit` + `taskkill /T` (which does not share
inherited pipe handles and kills the whole process tree on timeout) instead
of a plain `python ...` shell command. **This is itself a supervision-tree
finding in the spirit of row 77**: an instrument meant to catch dead
capabilities can itself be taken down by one badly-behaved probe, silently,
with no error — exactly the kind of failure that only a runtime
observation (not reading the script's prose) would catch.

---

## 6. Heritage memory mining report

Dispatched as a background Explore agent over gen-130 through gen-133.
**The operator's claim checks out — a working memory system already
existed and was lost, not never built:**

| system | verdict | evidence |
|---|---|---|
| gen-130 hybrid memory MCP (FTS5 + sqlite-vec) | **WORKING-WITH-RECEIPTS** | 8821 docs, 934-row vector table, wired into `.mcp.json`, live tool calls documented |
| gen-130 bitemporal memory events | **WORKING-WITH-RECEIPTS** | 4077 rows, valid/transaction-time columns already shaped like a real bitemporal design |
| gen-130 single-writer kernel | **WORKING-WITH-RECEIPTS** | 20336 inbox/event rows, 674 jobs, fresh as of Jul 31 |
| gen-133 `central_memory.sqlite` | **WORKING-WITH-RECEIPTS (small)** | seeded this week, `hfo_chain_row` still 0 — this is exactly the gap this session's Postgres/DBOS work is meant to close |
| gen-133 XTDB attempt | **ABANDONED** | Docker never came up (15 min prior session) — same failure this session hit again, independently confirming it's a real environment issue, not a one-off |
| gen-131 carryover of gen-130's memory | **DEGRADED** | 36 of 8821 docs survived migration (99.6% loss), `.malformed.bak` files are the failure's own receipt |
| gen-132 | **ABANDONED** | no `state/memory/` directory exists at all — memory was dropped entirely between generations |
| vendored mem0/letta/sqlite-vec bakeoff | **SCAFFOLDED-BUT-UNUSED** | full upstream repos copied for evaluation, never wired into a running `.mcp.json` |

**Salvage plan:** port gen-130's `docs`/`docs_fts` schema and 8821 rows
into a Postgres table with a `tsvector` column; port `memory_events`
(already bitemporal-shaped, 4077 rows) directly; reuse
`work/scripts/sigrun_memory_{core,ingest,retrieve,health}.py` as the
hybrid-search logic reference. **Do not** carry forward gen-131's copy —
it is the corrupted version, not a source of truth.

---

## 7. External Fitness Gate — industry convergence (operator mid-session reframe)

**Mid-execution reframe, operator verbatim:** *"emergency forge. we have
done this many times. let's formalize it and let's base this run off
industry patterns and proven what works... I have many ideas but what
I've been doing is internal fitness and we need external fitness now."*
Added in place, per the operator's own instruction not to restart. Every
row below cites a WebSearch fetched this session (August 2026 results).

**Internal fitness** = does it pass the runtime probe in §2. **External
fitness** = do named 2024-2026 production winners run it. A capability can
score high on one and low on the other — that gap is the point of this
section.

| capability | industry_convergence | named_winners_using_it | verdict |
|---|---|---|---|
| **Postgres + pgvector** | **HIGH** | OpenAI, Supabase, Neon — pgvector is described as the pragmatic default for production RAG up to 50-100M vectors ([devstarsj.github.io](https://devstarsj.github.io/2026/06/22/pgvector-postgres-vector-database-production-2026/), [Medium: Top 15 vector databases 2026](https://medium.com/@pratik-rupareliya/top-15-vector-databases-in-2026-a-production-decision-guide-from-100-enterprise-deployments-dd58a04f51a5)) | **INDUSTRY_PROVEN** |
| **LiteLLM** | **HIGH** | Netflix, Lemonade, Rocket Money named as production users; 20k+ GitHub stars; described as the most mature of the open-source LLM gateways ([compsmag.com](https://www.compsmag.com/reviews/litellm-review/)) | **INDUSTRY_PROVEN** |
| **DBOS** | **MEDIUM** | Dosu (Celery→DBOS migration, 20k workflows/hour, 50k+ projects served — [dosu.dev](https://dosu.dev/blog/migrate-celery-to-dbos-dosu)), Yutori (named production customer quote — [dbos.dev](https://www.dbos.dev/blog/dbos-new-features-march-2026)), Supabase ("Running Durable Workflows in Postgres" published case study — cited in this session's earlier `DURABLE_SUBSTRATE_PRIOR_ART_20260802.md`) | **EMERGING_PATTERN** — 3 named references is real but far smaller-scale convergence than Temporal/Restate at the substrate-runtime tier |
| **CrewAI** | **MEDIUM, vendor-stat-heavy** | DocuSign (published case study, "14x less code than equivalent LangGraph" — [47billion.com](https://47billion.com/blog/ai-agents-in-production-frameworks-protocols-and-what-actually-works-in-2026/)); one unnamed "global insurance company" sales-trainer deployment. Vendor claims "450M agents/month, 60% of Fortune 500" ([getpanto.ai](https://www.getpanto.ai/blog/crewai-platform-statistics)) — **this exact stat was already flagged skeptically in this session's own prior research** (`SIGRUN_ROOT_CAUSE_LEAK_20260802.md`, cross-referencing it against CrewAI's reported ~$3.2M ARR) | **EMERGING_PATTERN — adopt with caveat.** One real named case (DocuSign), thin beyond that; the vendor's own usage-scale marketing is the weakest kind of evidence in this table |

**Alternatives with stronger or different external fitness, per operator's ask:**

| framework | industry_convergence | named_winners_using_it | verdict |
|---|---|---|---|
| **LangGraph** | **HIGH — highest of any orchestration layer checked** | Klarna (85M users), Uber, LinkedIn; called "the most battle-tested for production" with a claimed 47% lower token cost than CrewAI ([requesty.ai](https://www.requesty.ai/blog/best-ai-agent-sdks-compared-2026-langchain-crewai-openai-anthropic-google), [turion.ai](https://turion.ai/blog/langgraph-vs-openai-claude-agent-sdk-2026/)) | **INDUSTRY_PROVEN** |
| **Claude Agent SDK** | MEDIUM, but directly dogfooded | Duotach (10 agents in production: support/finance/marketing/SEO — [duotach.com](https://duotach.com/en/blog/agentes-ia-claude-code)); Anthropic's own Claude Code runs on it | **EMERGING_PATTERN**, with the strongest internal/external alignment of anything in this table — **this session itself is running on it** |
| **OpenAI Agents SDK** | MEDIUM | Described broadly as "production-grade" alongside Claude Agent SDK; no single distinctly-named 2026 production case surfaced in this search round | **EMERGING_PATTERN, weakly evidenced** |
| **Vercel AI SDK** | HIGH, different layer | Perplexity, Otter, Jasper, Thomson Reuters CoCounsel; Stripe/Shopify/Notion also named ([leadcognition.io](https://leadcognition.io/who-uses/vercel-ai-sdk/), [humanxai.events](https://humanxai.events/vercel-in-2026-the-93-billion-bet-on-ai-native-infrastructure)) | **INDUSTRY_PROVEN — not a substitute.** This is the streaming/frontend-integration layer, not an orchestration or durable-execution competitor to DBOS/CrewAI |

**The honest tension this surfaces, stated plainly:** external fitness
ranks **LangGraph above CrewAI** — stronger named winners, a bigger claimed
efficiency edge, and Anthropic-adjacent industry consensus calling it the
safest production pick. But `SIGRUN_ROOT_CAUSE_LEAK_20260802.md` (this
generation's own row 77) measured LangGraph adoption inside HFO at **zero
imports, twice** — the framework was never actually wired in despite being
named in prose repeatedly. CrewAI, by contrast, ran a real `kickoff()` on
the first attempt this session, with zero prior HFO history either way.
**External fitness and internal fitness point in opposite directions here,
and this document does not resolve that tension for the operator** — it
states it. A `cap-langgraph-runtime` probe already exists in the registry
(`repo_grep: from langgraph`, currently DEAD); the honest next step is one
scoped attempt at wiring LangGraph against the same Postgres+Ollama
substrate this session just stood up, now that "no infra" is no longer a
valid excuse — see `next_safe_action`.

**External-fitness synthesis — which pieces are winner-backed vs internal preference:**

- **Winner-backed, high confidence:** Postgres+pgvector, LiteLLM. Keep
  without reservation.
- **Winner-backed, but thinner than marketing suggests:** DBOS (real but
  small-scale references), CrewAI (one real named case, rest is vendor
  usage-volume marketing that this generation's own prior research already
  distrusted). Keep both — they are runtime-verified in §2 — but do not
  cite the vendor scale-numbers as adoption justification going forward.
- **Not in this stack, but more winner-backed than what's in it:**
  LangGraph. This is the honest gap — the operator's reframe is correct
  that internal-fitness-only reasoning was steering this build, and
  LangGraph is the clearest example of a more externally-validated
  alternative that was skipped, for internal-history reasons (twice-failed
  adoption) rather than external-evidence reasons.
- **Already adopted, not re-evaluated tonight, strongest internal/external
  alignment available:** Claude Agent SDK — this whole session runs on it.

---

## 8. Honest_flaw

1. **Postgres is durable only while a keep-alive `wsl` process holds the
   VM open.** WSL2 auto-stops an idle distro ~8 seconds after the last
   `wsl.exe` invocation exits, which silently drops the localhost port
   forward — `psycopg2` then reports `ECONNREFUSED`, indistinguishable
   from "Postgres crashed." This session ran `nohup wsl -d Ubuntu-24.04 --
   sleep 14400 &` as a workaround; **that process dies with this session**.
   Without a durable fix (a scheduled task, a `.wslconfig`
   `vmIdleTimeout=-1` setting, or converting to a real Windows service /
   Docker container once Docker's engine is diagnosed), tomorrow's census
   run will report `cap-postgres-durable-scratchpad` and
   `cap-dbos-workflow-execution` as DEAD not because the capability
   regressed but because the keep-alive process is gone. **This is exactly
   the false-DEAD mirror of the false-ALIVE pattern row 77 caught itself
   committing** — flagging it explicitly so it isn't read as a regression.
2. **Docker Desktop's WSL2 engine is confirmed broken across two separate
   sessions**, not a one-off cold-boot fluke. `dockerDesktopLinuxEngine`
   named pipe exists but nothing answers behind it. Not diagnosed further
   (Docker Desktop logs / a repair-install were out of scope for a 4-hour
   build session) — flagging as a known blocker for whoever next wants
   Docker-based infra on this machine.
3. **sentence-transformers is DEAD**, specifically `import torch` hangs
   indefinitely with no exception in this shared, ~50-package user
   site-packages environment. The memory demo does not depend on it
   (Ollama's `nomic-embed-text` covers the embedding need), but the
   registered capability itself is not fixed, only routed around.
4. **CrewAI's answer content was a refusal, not a fact** — `llama3.2:3b`
   is a weak model for even a two-sentence factual task under a terse
   prompt. The wiring is real; the output quality is not proof the crew
   *reasoned* correctly, only that it *ran* for real.
5. **Langfuse was not attempted.** It requires a cloud account, which
   falls under this session's own explicit-permission boundary
   (creating accounts) rather than the BUILD/INSTALL/RUN/QUERY
   pre-authorization the mission granted. Deferred, not failed.
6. **The census itself was down for most of this session, silently.**
   §5 has the full account: a hung `torch` import inside
   `cap-sentence-transformers-embed` combined with a Windows-specific
   `subprocess.run(shell=True, capture_output=True)` pipe-inheritance bug
   to make the census hang forever, not for its intended 60s cap — three
   separate multi-minute runs died this way before the cause was isolated,
   orphaning 5 stuck processes. Fixed and confirmed: final clean run
   reports **ALIVE=12 DEAD=11 LEAKED=0**, pasted verbatim in §5, not
   "expected." Flagging the time cost honestly: this single bug consumed
   roughly a third of the session's wall-clock budget.
7. **The External Fitness Gate (§7) is WebSearch-sourced, one layer removed
   from primary sources** — same caveat this generation's other research
   documents already carry. Vendor-published case studies (DocuSign, Dosu,
   Yutori) are real but self-selected positive examples; no attempt was
   made to find named production *failures* or *abandonments* of any of
   these tools, which would be the more informative external-fitness signal
   and was out of scope for this session's time budget.

---

## 9. next_safe_action

**For the operator, tomorrow morning:**

1. Decide whether to fix Docker Desktop (repair install / check WSL2
   kernel version) or commit to the WSL-Postgres path long-term. If WSL
   long-term: set `vmIdleTimeout=-1` (or a large value) in
   `%USERPROFILE%\.wslconfig` so Postgres survives without a manual
   keep-alive process, then re-run
   `python tools/stack_builder/check_scratchpad_alive.py` cold (no prior
   `wsl` command run first) to confirm it survives an idle gap.
2. Run `python tools/capability_census.py` fresh each morning — that is
   now the only trustworthy signal for whether any of tonight's 5 new
   ALIVE capabilities are still alive, not this document.
3. If the WSL-Postgres path is kept: port gen-130's 8821-row hybrid memory
   corpus into it per §6's salvage plan — that closes the actual
   Olrun/Sigrun memory gap at full scale, not just the one-row demo shipped
   tonight.
4. Do not re-attempt sentence-transformers/torch in this same
   user-site-packages environment without first isolating a clean venv —
   the hang is very likely a dependency clash among the ~50 already-installed
   projects sharing this site-packages, not a sentence-transformers defect
   per se.
5. **Decide the LangGraph question §7 surfaced explicitly** — external
   fitness ranks it above CrewAI (Klarna/Uber/LinkedIn vs one DocuSign case
   study), but HFO has twice failed to wire it in at all (0 imports). Now
   that a working Postgres+Ollama substrate exists, that excuse is gone.
   Either timebox one real LangGraph attempt against this same substrate, or
   explicitly accept CrewAI on internal-fitness grounds and say so — don't
   let the tension sit unresolved by default.

*Réttu hönd, eigi spyr. Standa.*
