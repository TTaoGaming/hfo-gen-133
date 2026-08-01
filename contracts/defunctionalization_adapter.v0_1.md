# CONTRACT — defunctionalization + memory-translation adapter

```yaml
contract: defunctionalization_adapter
schema_id: hfo.gen133.contract.defunctionalization_adapter.v0_1
authored_by: SIGRÚN · claude-opus-5 · project lead
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
status: SPECIFIED — and BLOCKED on a corpus that does not exist (§0)
depends_on: >
  contracts/strife_splendor_rehydration.v0_1.md ·
  contracts/bitemporal_central_memory.v0_1.md ·
  contracts/heritage_ingestion_pipeline.v0_1.md
sealed: false
```

## §0 · The blocker, stated first

**The adapter cannot work until the strife/splendor corpus exists, and the
corpus does not exist.**

Stage 3 (*Ground*) retrieves the operator's historical successes and failures.
Probed live this session: `find -iname "*strife*" -o -iname "*splendor*"` across
gen-133 returns **zero files**. What exists is doctrine — a monotonic strife
*counter*, the kenning signals `ljomi=Splendor` / `strid=Strife`, and the chiasm
*"strífit er splendor, splendor er strífit"* — carried faithfully across
generations with **no record underneath it** (details in
`strife_splendor_rehydration.v0_1.md` §1).

If the adapter ships before the corpus, stage 3 returns an empty set, and per
`anti_lobotomize_rehydration.v0_1.md` §4-R1 **an empty set is the hallucination
condition**: the compiler fills the gap from its prior and emits a confidently
grounded prompt grounded in nothing. That is strictly worse than no adapter.

> ## **BUILD ORDER: corpus first, compiler second. Non-negotiable.**
> The corpus can start today with real rows (§4). The compiler is worth building
> the moment the corpus passes ~20 rows.

## §1 · Why "defunctionalization" is the right word

The operator's term is load-bearing, not decorative, and it should not be
flattened to "prompt templating."

In programming-language theory, **defunctionalization** converts a higher-order
function into (a) a first-order data representation of the function and (b) a
single `apply` interpreter. That is exactly the transformation required here:

| PL theory | this adapter |
|---|---|
| higher-order function — behaviour that cannot be serialized or shipped | operator's directive: *"get them looping at the strategic level"*, *"productive like bees making honey"* — intent that no LLM can execute directly |
| first-order data representation | a compiled prompt: role, task spec, few-shot demos, guardrails, output schema, falsifier |
| `apply` interpreter | dispatch to a named substrate/model |

The operator issues higher-order intent. Substrates execute first-order
instructions. **The adapter is the defunctionalizer between them**, and naming
it that is more precise than "prompt compiler."

## §2 · Industry grounding — adopt, do not reinvent

| system | what it is | what HFO takes |
|---|---|---|
| **DSPy** (Stanford) | treats prompts as something you **compile against a metric**, not write. Optimizers: **BootstrapFewShot**, **MIPROv2**, **COPRO**, **GEPA** [S] | the whole paradigm, and two optimizers specifically (§3) |
| **BootstrapFewShot** | runs the program over a trainset, **keeps only traces where the output passed the metric**, uses those as few-shot demos [S] | **this is splendor, exactly.** Not an analogy — the same data structure |
| **GEPA** | Genetic–Pareto: refines prompts via **natural-language feedback**, evolutionary search, Pareto selection; better results with fewer rollouts than RL [S] | **this is strife, exactly** — failure expressed as language, not as a scalar. And Pareto selection is the same archive-diversity logic as MAP-Elites in §8.4 |
| **MIPROv2** | bootstraps demos, proposes grounded instructions from dataset summaries, Bayesian search over instruction×demo combinations [S] | the stage-4 search, **later** — needs a real trainset |
| **Instructor** | Pydantic-schema-enforced LLM outputs | stage 4's output-schema enforcement |
| **Guidance / LMQL** | constrained/templated LLM programming | stage 4 templating where output shape is rigid |
| **mem0 / Letta / Zep** | long-term memory backends | **rejected as the store** — XTDB is stamped (`bitemporal_central_memory` §0). Their *retrieval* patterns are still worth copying |
| **RAGAS / ARES** | RAG evaluation | stage 7's grounding-quality metric, once there is anything to evaluate |

**The convergence worth naming:** the operator's strife/splendor framing is not
a metaphor being retrofitted onto DSPy. **It is the trainset structure DSPy's
optimizers already require** — positive traces for BootstrapFewShot, natural-
language failure feedback for GEPA. HFO does not need to invent an optimizer.
**HFO needs to produce the trainset, which is precisely the thing it does not
have.** That reframes the whole ask from "build a compiler" to "start keeping
receipts in a shape an off-the-shelf compiler can eat."

## §3 · The pipeline

```
[1 INPUT] raw operator directive (natural language, often mythic-metaphoric)
    │
[2 PARSE] → {intent, task_class, audience, scope, constraints, ambiguities[]}
    │
[3 GROUND] ← strife rows (task_class) + splendor rows (task_class)   ⟵ THE BLOCKER
    │
[4 COMPILE] → structured prompt artifact
    │
[5 ROUTE] → {substrate, model, tier}
    │
[6 DISPATCH] → start_code_task | LiteLLM | Codex goal | Antigravity task
    │
[7 LOG] → chain row: compiled prompt + target + outcome  ──┐
                                                            └─▶ feeds [3] next time
```

Stage 7 closing back into stage 3 is the strange loop the operator asked for.
**Without it the adapter is a template engine; with it, it learns.**

### Stage 2 · Parse

Output is typed, and **`ambiguities[]` is mandatory and may not be empty-by-
laziness**:

```jsonc
{ "intent": "...",                       // the verb and its object
  "task_class": "income|outreach|spatial|infra|memory|governance",
  "audience": "FENRIR|codex|groq/llama-3.3-70b|...",
  "scope": {"in": [...], "out": [...]},
  "constraints": ["no world-effect", "timebox 15 turns", ...],
  "ambiguities": [{"span": "...", "readings": ["...","..."], "resolution": "assumed X because Y"}],
  "mythic_terms": ["blóðfrændi", "strife", "splendor", "waggle dance"] }
```

**`mythic_terms` exists to satisfy L30 / L33.** Operator vocabulary is
load-bearing function-spec, not decoration. The parser records these terms so
the compiler can **carry them into the compiled prompt with their operative
definition attached**, rather than flattening them to the nearest generic
phrasing. Flattening them is a named failure vector, not a style preference.

### Stage 3 · Ground — the memory-translation step

```sql
-- splendor: what worked, in this task class
SELECT * FROM hfo_fact
WHERE entity LIKE 'splendor:%' AND attribute='task_class' AND value_json = :task_class
  AND tx_to IS NULL ORDER BY valid_from DESC LIMIT 3;

-- strife: what failed, in this task class
SELECT * FROM hfo_fact
WHERE entity LIKE 'strife:%' AND attribute='task_class' AND value_json = :task_class
  AND tx_to IS NULL ORDER BY valid_from DESC LIMIT 5;
```

**If either query returns zero rows, the compiler MUST emit
`GROUNDING: NONE_AVAILABLE` into the compiled prompt.** It may not silently
proceed. A prompt that claims to be grounded and is not is a false-green in the
compiler itself, and it would poison every downstream dispatch.

### Stage 4 · Compile — the output artifact

```markdown
```yaml
# AIH2O
schema_id: hfo.gen133.compiled_prompt.v0_1
compiled_from: "<raw operator directive, verbatim>"
compiled_at_utc: ...
target: {substrate, model, tier}
task_class: ...
grounding: {splendor_rows: [ids], strife_rows: [ids]}   # or NONE_AVAILABLE
compiler_version: ...
```
# ROLE          — persona + authority + what this carrier may NOT do
# TASK          — defunctionalized: imperative, first-order, testable
# WORKED BEFORE — few-shot demos drawn from splendor rows (BootstrapFewShot)
# DO NOT        — guardrails drawn from strife rows, each naming its MECHANISM
# OUTPUT SCHEMA — Instructor/Pydantic-style, enforced
# ACCEPTANCE    — falsifier + pass condition + who verifies
# COST CEILING  — tokens, turns, and the world-effect bar
```

The `DO NOT` block is the highest-value section and the one that does not exist
today. **A guardrail is admissible only if it names the mechanism**, not just
the outcome — "do not assign a probability to a lane you have not researched"
is a guardrail; "do not be wrong" is noise.

### Stage 5 · Route — cost-aware, per §9.0

| work shape | tier | why |
|---|---|---|
| parse, classify, triage, score, variant-generate | **$0 frontier** (Groq / Cerebras until 2026-08-17) | short-context, high-volume — exactly what the free tier is good at |
| compile a prompt (<8K tokens context) | **$0 frontier** | fits inside Cerebras' 8,192 cap |
| ground against a long capsule (>30K context) | **Gemini free (1M ctx, 250 RPD)** or paid | Groq's 6,000 TPM makes this ~1 call / 5 min |
| author the compiler itself | **host Codex** | `scripts/` is Claude-gated (4 denials, gen-130) |

**Compilation is short-context and high-volume, which means the adapter runs at
$0.** That is the single best fit between the §9.0 correction and this contract.

### Stage 7 · Log — the strange loop

Every dispatch writes a chain row carrying: compiled prompt sha256, target,
outcome, and `claim_status`. **The outcome is what classifies the row as future
strife or splendor** (`strife_splendor_rehydration` §2). Skip stage 7 and the
adapter cannot improve — it becomes a static template with extra steps.

## §4 · Phasing — honest, because DSPy needs data HFO does not have

| phase | gate | what runs |
|---|---|---|
| **P0 · corpus** | now | log strife/splendor rows. **No compiler.** Seed from §5 |
| **P1 · retrieval-only** | ≥20 rows | stages 1,2,3,4,7 by hand-written template. **No optimizer.** Retrieval alone is most of the value at small n |
| **P2 · BootstrapFewShot** | ≥50 rows w/ pass/fail metric | splendor rows become auto-selected demos |
| **P3 · GEPA / MIPROv2** | ≥200 rows + a real metric | genuine optimization |

**Do not adopt DSPy-the-framework at P0 or P1.** Its optimizers require a
runnable program and a metric; HFO's metric is operator judgment plus income,
currently n≈0. **Running MIPROv2 over three examples fits noise and produces a
confidently overfitted prompt** — which is the §8.4 weekly-selection error in a
different costume. Adopt the *pattern* now, the *library* at P2.

> **FALSIFIER (§4):** if P1 runs for 30 days and compiled prompts do not measurably
> beat hand-written ones on task acceptance, the bottleneck is not prompt quality
> and the adapter should be parked. Retrieval is cheap; a compiler nobody needs
> is not.

## §5 · Seed corpus — available today, from this session

The corpus does not start at zero. **This document produced six mechanism-named
strife rows, operator-verified**, and they are admissible immediately:

| id | strife | mechanism | task_class |
|---|---|---|---|
| S-001 | Spatial-OS sunset stamped on a 3% probability | **a probability was assigned to a lane that was never researched** | income |
| S-002 | handpiano ranked #4 as "off-thesis" | **thesis was self-selected, then used to discard the operator's strongest verified asset** | income |
| S-003 | audit lane kept in quarter top-3 after 0-stars was recorded | **disconfirming evidence recorded, then not allowed to move the ranking** | income |
| S-004 | Upwork aimed at a category my own doc called saturated | **channel and positioning conflated; the analysis contradicted the recommendation in the same file** | outreach |
| S-005 | "$0 mesh is weak" | **induction from a partial probe — the local half was crashing, the hosted half was never checked** | infra |
| S-006 | §1 bias diagnosed as "Bias 1" and its rankings left standing | **diagnosing a bias without repairing its output launders the recommendation** | governance |

Splendor rows are thinner and that is itself information — **the honest count of
verified stranger-visible successes in the recent record is near zero** (609
commits, 0 external artifacts). Admissible candidates: handpiano.com shipped and
live (HTTP 200, verified twice this session); `hfopiano_v512` factored the
tracking layer out into separable workers *before* anyone asked for a reskin
factory. **Both are operator-authored. Neither was produced by the swarm.**

That asymmetry is the most useful thing in this contract: **the corpus, on day
one, says the operator ships and the swarm specifies.** A compiler grounded in
that will produce different instructions than one grounded in nothing.

## §6 · Honest flaws

- **Blocked by construction** (§0). Zero corpus rows are persisted; the six above
  live in a markdown table, not in a store.
- **DSPy optimizer descriptions are search-snippet grade [S]**, not from running
  the library. Verify against `dspy.ai` docs before P2.
- **`task_class` taxonomy is invented here** (income/outreach/spatial/infra/
  memory/governance). Six buckets is a guess; expect it to be wrong at the edges
  and to need splitting once ~50 rows exist.
- **No metric exists.** Every DSPy optimizer needs one. "Operator accepted the
  output" is the only honest candidate today, it is expensive to collect, and it
  is exactly the operator-attention resource §8.0 is trying to conserve. **This
  tension is unresolved and I am not going to paper over it.**
- **The adapter is itself an artifact whose value flows through Sigrún's own
  work product** — §1's bias, a fifth time today. Its defense is that §5 exists:
  the seed rows are retractions of my own errors, which is the one category of
  content I cannot be accused of ranking highly because I authored it.
