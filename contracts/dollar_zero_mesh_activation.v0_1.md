# CONTRACT — $0 mesh ACTIVATION (not a new harness)

```yaml
contract: dollar_zero_mesh_activation
schema_id: hfo.gen133.contract.dollar_zero_mesh_activation.v0_1
valid_time_utc:       2026-07-31T18:45:00Z
transaction_time_utc: 2026-07-31T18:55:00Z
authored_by: SIGRUN_P4 · claude-opus-5 · gen-133
status: SPECIFIED — activation steps + smoke test. NOT RUN.
claim_status: partial
sealed: false
supersedes: nothing
complements:
  - contracts/free_mesh_harness.contract.md      (the job ABI + Gleipnir binding — NOT restated)
  - contracts/free_mesh_adapter.contract.md      (LiteLLM routing, 8 vendor families — NOT restated)
  - contracts/dollar_zero_mesh_harnesses.v0_1.md (the measured install inventory — NOT restated)
```

## 0 · Why this file is short

**I was asked to design a $0 mesh dispatch harness. One already exists.**

Three gen-133 contracts already specify the job ABI, the LiteLLM routing, the
8-family vendor roster, and the measured install inventory. LiteLLM 1.82.6,
LangGraph 1.1.3, `langgraph-checkpoint-sqlite`, DBOS, CrewAI, pydantic-ai and the
Ollama client are **all installed**. A durable LangGraph loop against local Ollama
**ran end to end this morning with 9 on-disk checkpoints**, verified by re-reading
state through a fresh connection.

Writing a fourth harness spec would be the **unindexed-capability failure** — the
pattern already recorded three times in this fleet (*"the kit was never lost, it
was unindexed"*; 78 of 81 scheduled tasks disabled-not-deleted; the harnesses
above). **This contract covers only the activation gap.**

## 1 · The blocker — one environment variable

```
OLLAMA_HOST = 0.0.0.0:11434     (User scope)
```

`0.0.0.0` is a valid **bind** address and an invalid **connect** address. The
server binds it correctly; the Python client reads the same variable and tries to
*connect* to it, and fails.

| probe | result |
|---|---|
| `curl http://127.0.0.1:11434/api/tags` | 200 |
| `ollama.Client(host=None)` (reads the env var) | ❌ ConnectionError |
| `ollama.Client(host="http://127.0.0.1:11434")` | ✅ 11 models |

**Failure class: `BIND_ADDRESS_AS_CONNECT_ADDRESS`.** One key serving two opposite
roles.

**Fix — operator, 30 seconds:**

```powershell
setx OLLAMA_HOST "http://127.0.0.1:11434"
```

If the variable exists so the server listens on all interfaces, set it in the
**service** environment only and leave the client default alone.

**Honest limit, carried forward:** andons A-005/006/007 recorded *partial*
successes, so some calls reached models by another path. This is decisively the
root cause for the **Python-client** path and at most contributory for the relay
path, which has not been reproduced.

## 2 · Activation steps — in order, each with an observable

| # | step | observable that it worked | who |
|---|---|---|---|
| A1 | `setx OLLAMA_HOST "http://127.0.0.1:11434"`, new shell | `ollama.Client()` lists 11 models | **operator** |
| A2 | Write `config/litellm_config.yaml` — Ollama models only, no vendor keys | `litellm --config … --test` returns a completion | sonnet valkyrie |
| A3 | **Smoke test (§3)** — 3 models × 3 structured calls, schema-validated | 9 validated rows in `state/ssot/dollar_zero_mesh_responses.jsonl` | sonnet valkyrie |
| A4 | Obtain free vendor keys — **only after A3 passes** | keys resolve, `litellm --test` per family | **operator** |
| A5 | Wrap in the LangGraph loop already proven this morning | loop resumes from disk after process kill | sonnet valkyrie |
| A6 | Wake apex **Surtr** (blocker B5 clears once A3 passes) | Surtr returns a non-blocked row | Olrún |

**Do not do A4 before A3.** Adding six vendor families to a path that has not
completed one validated local call multiplies unknowns instead of resolving them.

### Free vendor signup — A4 only

| vendor | signup | note |
|---|---|---|
| Groq | `console.groq.com` | free tier, fast |
| Cerebras | `cloud.cerebras.ai` | **already in the 401 rotation per gen-132 — may only need re-issue, not signup** |
| OpenRouter | `openrouter.ai/keys` | `:free` suffix only. gen-132: credits present ⇒ 1000 `:free` req/day vs 50 |

⚠️ gen-132 recorded default `OPENROUTER_API_KEY` **revoked (401)** with
`HFO_OPENROUTER_*` alternates alive. **Verify which key is live before assuming a
vendor is dead** — that exact false-red already cost this fleet a diagnosis cycle.

## 3 · Smoke test — the acceptance gate, red-first

**Three models × three structured calls, schema-validated.** Not "did it
respond" — **"did it respond in schema, three times running."**

```
models:   qwen3.5:9b · granite3.3:8b · gemma4:e4b        (≥8B ONLY — see the 3B rule)
prompt:   return ONLY {"verdict":"STOOD"|"FELL","reason":"<=12 words"}
repeat:   3 per model
validate: pydantic-ai / instructor. UNPARSEABLE = FAIL, not retry.
control:  llama3.2:3b MUST be run too and MUST FAIL. A smoke test where the known-
          bad case passes is not measuring anything.
PASS:     9/9 validated on the ≥8B tier AND the 3B control fails.
```

**That control line is the whole point.** A green with no red is a fake green.

## 4 · Wrapper + writer discipline

```
dispatch_to_dollar_zero_mesh.py <model> <prompt_file> <out_jsonl>
  → LiteLLM completion
  → validate against contracts/schemas/dollar_zero_response.v0_1.json
  → INVALID: write a row with status="schema_fail" and the raw text. Never silently retry.
  → VALID:   append one row
```

**Single writer.** One process appends to
`state/ssot/dollar_zero_mesh_responses.jsonl`. Concurrent appenders is how the
kernel/projection divergence already recorded at gen-130 (1144 orphaned rows, 31%)
happens again.

**Rows carry `prev_sha256` + `row_sha256` under an explicitly declared
`hash_rule`.** Non-negotiable: 7 of 9 rows in `chains/SIGRUN_P4.jsonl` carry **no**
hash fields at all, because a carrier silently dropped the discipline and nothing
detected it (`L_CHAIN_HASH_ABANDONED_SILENTLY`).

## 5 · Invocation paths — ranked by what is proven

| path | status |
|---|---|
| **Bash from a Claude scheduled task** | ✅ **recommended.** Scheduled sessions cannot dispatch child sessions but **can** run bash |
| Codex scheduled goal | ✅ viable — 6 ACTIVE automations prove the Codex scheduler fires |
| WSL cron | ✅ viable, installed, **never exercised** |
| DBOS durable queue | ✅ installed; heaviest; correct end state, wrong first step |

## 6 · Falsifiers

| # | falsifier | cost of delay |
|---|---|---|
| F1 | A1 lands and the client still fails → `BIND_ADDRESS_AS_CONNECT_ADDRESS` was contributory, not causal; A-005/006/007 need re-diagnosis | **30 seconds to test, days of blocked mesh work if untested** |
| F2 | ≥8B models fail the 3×3 schema test → the $0 tier cannot produce rows and §13's cheap tier is void | every downstream $0 plan collapses; **better to know in 20 minutes** |
| F3 | The 3B control **passes** → the 3B rule is wrong and the tier threshold is too conservative | over-spending on mid tier indefinitely |
| F4 | LiteLLM's Ollama provider needs config this contract omits | I did not read LiteLLM's docs this session and **did not fabricate its behavior**; A2 is spec, not verified |

**Nothing here is run. Every row above is `proposed` until A3 emits its 9+1.**
