# CONTRACT — cost-tier routing

```yaml
contract: cost_tier_routing
schema_id: hfo.gen133.contract.cost_tier_routing.v0_1
valid_time_utc:       2026-07-31T18:40:00Z
transaction_time_utc: 2026-07-31T18:55:00Z
authored_by: SIGRUN_P4 · claude-opus-5 · gen-133
status: SPECIFIED — routing table + decision tree. NOT ENFORCED (no router reads this yet)
claim_status: partial
sealed: false
companions: contracts/free_mesh_adapter.contract.md (LiteLLM routing) · contracts/dollar_zero_mesh_activation.v0_1.md
```

## 0 · The rule in one line

> **Frontier decides. Mid executes. Cheap counts.**
> A task routed one tier too high wastes money. A task routed one tier too low
> produces well-formed noise, which is worse — it *looks* like it worked.

## 1 · Measured substrate inventory — this host, 2026-07-31

| tier | substrate | status | cost |
|---|---|---|---|
| **frontier** | Claude opus-5 (Code + Dispatch) | ✅ live | metered |
| **frontier (cross-family)** | Codex GPT-5.6 Sol (ChatGPT app) | ✅ live, 6 ACTIVE automations | subscription |
| **mid** | Claude sonnet-5 (valkyries) | ✅ live | metered, ~10–20% of opus |
| **mid** | Antigravity + Antigravity IDE | ⚠️ **installed, never exercised by HFO** | unknown |
| **cheap** | Ollama local — 11 models, incl. `llama4:scout` 67 GB, `qwen3.5:9b`, `gemma4:e4b`, `granite3.3:8b` | ⚠️ **installed, blocked by one env var** | **$0** |
| **cheap** | Cerebras / Groq / OpenRouter free tiers | ⚠️ keys absent or rotating | **$0** |
| **router** | LiteLLM **1.82.6** | ✅ **already installed** (`Python312/Scripts/litellm`) | — |
| **orchestration** | LangGraph 1.1.3 + `langgraph-checkpoint-sqlite` 3.0.3, DBOS 2.17.0, CrewAI 1.11.1, pydantic-ai 1.70.0 | ✅ installed; **durable loop PROVEN this morning, 9 disk checkpoints** | — |
| **unknown** | Kiro | ⛔ **installed, unidentified — Olrún to classify** | unknown |

## 2 · Routing table — TASK CLASS × TIER × SUBSTRATE

| task class | tier | substrate | why |
|---|---|---|---|
| Strategic reasoning, spec design, offer/pricing design | **frontier** | opus-5 (Sigrún) | a wrong decision here costs weeks; token cost is noise against that |
| Red-team / adversarial vote / safety veto | **frontier, cross-family** | Codex GPT-5.6 Sol | judgment-critical **and** must not share the proposer's blind spot |
| Quorum ratification vote | **frontier ≥2 families** | opus-5 apex + ≥1 Codex | §10.3 damping: a same-family-only quorum is `advisory` |
| Code write, refactor, test authoring | **mid** | sonnet-5 · Codex | good enough, 10× cheaper. **Never opus for code** |
| Dispatch coordination, scheduling, host control | **mid** | sonnet-5 (Olrún) | one round-trip per decision |
| Copy drafting (email, proposal, post) | **mid** | sonnet-5 | voice matters; 8B tier flattens it |
| Copy *linting* (opt-out present? jargon? one CTA?) | **deterministic** | **plain Python, no model** | it is a string check. **A model here is pure waste and adds a failure mode** |
| Reply classification (5 classes) | **cheap** | Ollama ≥8B, schema-validated | high volume, low judgment |
| Contact/company enrichment normalization | **cheap** | Ollama ≥8B | bulk, verifiable downstream |
| Bulk summarization / triage of long docs | **cheap** | `llama4:scout` (long context) | volume play |
| Family-diversity voting (non-Anthropic) | **cheap** | Ollama ≥8B, **never 3B** | free family diversity for the §10.3 formula |
| Embeddings | **cheap** | `nomic-embed-text` local | $0, already installed |
| Anything touching SEND/SPEND/PUBLISH/PUSH/SEAL | **none — symbolic gate** | deterministic program + operator | **no tier of model is authorized here.** §1 envelope |

## 3 · The 3B rule — measured, not assumed

> **No model below 8B parameters may produce a row, a vote, or a classification.**

Proof, this host, 2026-07-31: a LangGraph loop asked `llama3.2:3b` for the single
word `STOOD` three times. It returned `"Nothing." / "Silence" / "Present"`. It
could not hold a one-word protocol three times running.

**A 3B model in a structured pipeline emits well-formed rows containing noise.**
That is worse than failure, because the schema passes and the receipt looks clean.
3B tier is permitted only for: embeddings, and non-structured throwaway text a
human reads directly.

**Falsifier:** `qwen3.5:9b` or `granite3.3:8b` fails the same 3-round protocol
test. Then the threshold is above 8B and this rule is too permissive. **Run the
test before trusting the tier.**

## 4 · Dispatch decision tree

```
work item arrives
│
├─ Does it cause SEND / SPEND / PUBLISH / PUSH / SEAL / DELETE?
│    └─ YES → symbolic gate + operator. NO MODEL DECIDES THIS. stop.
│
├─ Is it a pure string/schema/exit-code check?
│    └─ YES → deterministic Python. NO MODEL. stop.
│
├─ Does a wrong answer cost > 1 week of capacity, or set a price/offer?
│    └─ YES → frontier. If I am both proposer and grader → +1 cross-family voter.
│
├─ Does it write code, run tests, or coordinate a dispatch?
│    └─ YES → mid (sonnet-5 / Codex).
│
├─ Is it high-volume, low-judgment, and downstream-verifiable?
│    └─ YES → cheap ($0 mesh, ≥8B, output schema-validated by pydantic-ai
│              BEFORE it becomes a row — an unvalidated mesh output is not evidence)
│
└─ else → mid. Unclassified defaults UP, never down.
```

**Escalation is monotonic.** Downgrading a task's tier after seeing a result you
dislike is reward hacking with extra steps.

## 5 · Falsifiers

| # | falsifier | cost of delay |
|---|---|---|
| F1 | 30 days of routing produces no measurable spend reduction → the tiering was theatre; **nobody is measuring per-tier spend today, so this is currently unfalsifiable** | the routing cannot be improved because it is not instrumented |
| F2 | `≥8B` outputs fail schema validation > 10% of the time → the cheap tier is not usable for rows and the table is wrong | every $0 row landed before this is measured is suspect |
| F3 | Antigravity turns out to be frontier-class and free → the mid tier is mis-specified and Antigravity should absorb sonnet work | unknown-sized; **Antigravity has never been exercised by HFO** |
| F4 | Kiro is a substrate and is already running loops nobody indexed → the roster is incomplete, 4th instance of the unindexed-capability pattern | unknown |

**Not enforced.** No router reads this file. It is a decision aid until a
dispatcher consults it programmatically.
