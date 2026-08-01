# CONTRACT — $0 mesh loop harnesses: measured inventory

```yaml
contract: dollar_zero_mesh_harnesses
schema_id: hfo.gen133.contract.dollar_zero_mesh_harnesses.v0_1
valid_time_utc: 2026-07-31T06:45:00Z
transaction_time_utc: 2026-07-31T07:00:00Z
authored_by: SIGRÚN P4 · claude-opus-5
status: MEASURED on host — pip list + live loop execution, not recalled
claim_status: partial
sealed: false
complements: contracts/free_mesh_harness.contract.md (the ABI + Gleipnir threads — NOT restated here)
scope: which harnesses are INSTALLABLE/INSTALLED and which actually RAN on this host
```

## 0 · Headline

> **Install nothing tonight. Six of the operator's named harnesses are already
> installed, and a durable loop against local Ollama ran end to end during this
> session.**

The operator asked: *"we can download harnesses for the $0 mesh."* Measured
answer: the download already happened. The gap is **activation and indexing**, not
acquisition — the third instance of that pattern in this session, after
B.10 *"the kit was never lost, it was unindexed"* and the 78 disabled scheduled
tasks.

## 1 · Measured inventory — `pip list`, this host, 2026-07-31T06:45Z

| harness | version | installed | license | Ollama-compat | best-fit HFO use |
|---|---|---|---|---|---|
| **LangGraph** | **1.1.3** | ✅ | MIT | ✅ via `ollama` / `langchain-community` | **the strange-loop substrate.** Cyclic graphs = the wake loop |
| **`langgraph-checkpoint-sqlite`** | **3.0.3** | ✅ | MIT | n/a | **durability on disk.** Resume after process death |
| `langgraph-checkpoint` | 4.0.1 | ✅ | MIT | n/a | checkpoint ABI |
| **DBOS** | **2.17.0** | ✅ | MIT | n/a (orchestration) | **durable execution.** Survives *host* reboot, exactly-once |
| **CrewAI** | **1.11.1** (+tools 1.11.0) | ✅ | MIT | ✅ | multi-agent teams — maps to valkyrie squads |
| **LiteLLM** | **1.82.6** | ✅ | MIT | ✅ | **the vendor router `free_mesh_harness` specifies as "unverified"** |
| `langchain` / `-core` / `-community` | 1.2.12 / 1.2.22 / 0.4.1 | ✅ | MIT | ✅ | tool/model adapters |
| `langchain-mcp-adapters` | 0.2.2 | ✅ | MIT | n/a | MCP ↔ LangGraph bridge |
| `smolagents` | 1.24.0 | ✅ | Apache-2.0 | ✅ | minimal code-agent loops |
| `pydantic-ai` | 1.70.0 | ✅ | MIT | ✅ | **typed/validated agent output** — schema-enforced rows |
| `instructor` | 1.14.5 | ✅ | MIT | ✅ | structured extraction |
| `swarm` (OpenAI) | 0.1.0 | ✅ | MIT | partial | experimental//educational; superseded upstream |
| `ollama` (client) | 0.6.1 | ✅ | MIT | ✅ | ⚠️ **see §3 — default host is broken on this box** |
| **Letta** (MemGPT) | — | ❌ | Apache-2.0 | ✅ | durable agent memory — **the one real gap**; overlaps existing memory MCP |
| AutoGen / AG2 | — | ❌ | MIT/CC-BY | ✅ | multi-agent; overlaps CrewAI |
| Aider | — | ❌ | Apache-2.0 | ✅ | git-native pair programmer — good Codex-lane complement |
| OpenHands | — | ❌ | MIT | ✅ | full SWE agent; **heavy — Docker required** |
| Semantic Kernel | — | ❌ | MIT | partial | .NET-first; poor fit |
| MetaGPT / GPT-Engineer | — | ❌ | MIT | partial | scaffold-generators; **contra D3 minimalism** |

Node 24.13.1 / npm 11.8.0 present. Python 3.12.10. Six venvs already exist
(`.venv`, `work/.venv_cots`, `work/.venv_mesh_cots_20260616`,
`work/.venv_openai_agents_sdk`, …).

## 2 · PROOF OF RUN — a durable loop actually executed

Not a claim. Executed this session, local Ollama, $0:

```
FINAL:              {"n": 3, "log": ["Nothing.", "Silence", "Present"]}
RESUMED_FROM_DISK:  {"n": 3, "log": ["Nothing.", "Silence", "Present"]}
CHECKPOINT_COUNT:   9
```

Method: LangGraph `StateGraph` with a conditional self-edge (`tick → tick` until
`n ≥ 3`), `SqliteSaver` over `probe_ckpt.sqlite`, model `llama3.2:3b` via local
Ollama. State was then **re-read through a new `sqlite3` connection and a new
`SqliteSaver` object** — proving persistence is on disk, not in memory. 9
checkpoints recorded.

**This is the strange-loop substrate the operator is asking for, and it works
today.**

**Second finding from the same run — it constrains every loop design.** The log
*should* read `["STOOD","STOOD","STOOD"]`. `llama3.2:3b` returned *"Nothing." /
"Silence" / "Present"* — it could not follow a one-word protocol three consecutive
times.

> **3B models cannot hold a protocol.** A loop depending on structured output from
> the 3B tier emits well-formed rows containing noise — **worse than failing**,
> because it looks like it worked. Use `pydantic-ai`/`instructor` to *validate and
> reject*, or put ≥8B on any structured step.

## 3 · ⛔ THE BLOCKER — one environment variable

```
OLLAMA_HOST = 0.0.0.0:11434     (User-scope, verified first-hand)
```

`0.0.0.0` is a valid **bind** address for a server and an **invalid connect**
address for a client. The Ollama *server* binds it correctly. The Ollama *Python
client reads the same variable* and tries to **connect** to it — and fails.

| probe | result |
|---|---|
| `curl http://127.0.0.1:11434/api/tags` | **200** |
| `curl http://[::1]:11434/api/tags` | **200** |
| `ollama.Client(host=None)` → reads `OLLAMA_HOST` | ❌ `ConnectionError` |
| `ollama.Client(host="http://127.0.0.1:11434")` | ✅ **OK, 11 models** |

**Fix (operator, 30 seconds):**

```powershell
setx OLLAMA_HOST "http://127.0.0.1:11434"     # or remove the User-scope variable
```

If the variable exists to make the server listen on all interfaces, set the
**server-side** variable in the service environment only, and leave the client
default alone. **One key must not serve two opposite roles.**

New failure class: **`BIND_ADDRESS_AS_CONNECT_ADDRESS`.**

**Honest limit:** andons A-005/006/007 recorded *partial* successes (llama 3/4,
phi4 2/4), so those calls reached the model by some other path. This is decisively
the root cause **for the Python-client loop path** and at most contributory for the
relay path, which I did not reproduce.

## 4 · Host capacity — the real meter is RAM

31.5 GB total · Intel Core Ultra 7 258V · Arc 140V iGPU (shared memory).

| free RAM | when |
|---|---|
| 6.1 GB | 2026-07-30T15:20Z (recorded) |
| **3.2 GB** | 2026-07-31T06:33Z (measured) |

| model | size | verdict |
|---|---|---|
| `llama3.2:3b` | 2.0 GB | ✅ runs · ❌ cannot hold a protocol |
| `phi4-mini:3.8b` | 2.5 GB | ✅ fits |
| `granite3.3:8b` | 4.9 GB | ✅ **answered `STOOD` correctly in 40 s** — falsifies A-007's *"totally non-functional"* |
| `qwen3.5:9b` | 6.6 GB | ❌ **empty response after 134 s** |
| `gemma4:e4b` | 9.6 GB | ⚠️ recorded `quality_reject` (incoherent on trivial arithmetic) |
| `llama4:scout` | **67.4 GB** | ⛔ **impossible — 2.1× total RAM.** Correctly never attempted |

**I tested "use the bigger unused models" and the test refuted me.** Recorded
because recommending it unverified would have been
`LLM_CONFIDENT_UNVERIFIED_ADVICE` from the seat that registered that class.

**Operating rule:** the local mesh is metered by **wall-clock and RAM, not
dollars**, on a machine the operator is actively using. Cap concurrency at **one
local model at a time**, prefer **≤5 GB** footprints, and treat host
responsiveness as a real cost.

## 5 · Ranked — top 3, all zero-install

| # | harness | why | first action |
|---|---|---|---|
| **1** | **LangGraph + `SqliteSaver`** | Proven above. Durable, resumable, cyclic. Directly implements the wake loop and mutual-watch cure for `WATCHDOG_FATE_SHARING`. | Fix §3, then port the probe into a real wake loop that writes a chain row per tick |
| **2** | **DBOS 2.17.0** | Exactly-once durable execution — survives host reboot, not just process exit. The outer rung under LangGraph. | Wrap the LangGraph loop in a DBOS workflow |
| **3** | **LiteLLM 1.82.6** | The vendor router `free_mesh_harness.contract.md` records as *"operator-side, unverified by this lane."* **It is installed.** Unblocks cross-family routing for the free tiers. | Verify against one free vendor; re-point the 3 valkyries wired to the absent Together `-Turbo-Free` models |

**Deferred, deliberately:** Letta (real gap, but overlaps the existing memory MCP —
verify the overlap before installing); Aider (good Codex complement, no loop role);
OpenHands (Docker-heavy, contra D3); MetaGPT/GPT-Engineer (scaffold generators —
the hoarding failure mode in package form).

## 6 · FALSIFIERS

| # | claim | falsifier |
|---|---|---|
| F1 | "Harnesses already installed" | A fresh shell in the venv these loops will actually run under fails to `import langgraph`. **My `pip list` was the global 3.12.10 interpreter — six venvs exist and I did not check inside them.** |
| F2 | "Durable loop works" | Kill the process mid-loop and restart; if it replays from `n=0` instead of resuming, `SqliteSaver` is not durable across process death. My test resumed within one process lifetime — **weaker than a true crash test.** |
| F3 | "`OLLAMA_HOST` is the root cause" | Unset it and re-run A-005/006/007's original workload. If the 3 models still crash 4/4, the env var was incidental. |
| F4 | "3B can't hold a protocol" | Run 20 trials with a strict system prompt + `instructor` validation. If ≥18 return `STOOD`, my n=3 was prompt-design failure, not capability. |
| F5 | "Install nothing" | If any top-3 harness needs a version bump or a missing extra to do real work, "already installed" was over-stated — presence ≠ sufficiency. |
| F6 | "granite works" | One 3-token generation at `num_ctx=8192` is not a workload. Under a real 8K-context diff review it may still fail — which is what A-007 actually tested. **My probe falsifies "totally non-functional", not "unreliable under load."** |

**F1 and F6 are the two most likely to fire.** Check both before acting on §5.

## 7 · Honest flaw

Measurements are single-instant, on a host under active memory pressure, taken by
the substrate reporting them. `pip list` was read from the **global** interpreter —
if the loops run inside `work/.venv_cots` or another venv, the inventory may not
hold there (F1). The durable-loop proof resumed state **within one process
lifetime**; I did not kill and restart the process, so "survives process death" is
inferred from the SQLite file being re-read through a fresh connection, not
demonstrated by a crash (F2). No free *cloud* vendor was called at all — Cerebras
remains blocked by HFO's own PreToolUse secret-read gate, and the Together
`-Turbo-Free` models remain absent from the vendor catalog. **The entire cloud half
of the $0 mesh is still unverified by me.**

*Take what is given ≠ believe what is claimed.*
*No receipt = no state.*
