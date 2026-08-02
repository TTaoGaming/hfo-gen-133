```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_APPROVED_MEMORY_V0_20260802.md
schema_id: hfo.gen133.sigrun_approved_memory_v0.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T14:45:12Z
clock_source: host_read              # `date -u`, this turn
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md
extends: chain rows 75 (canon V1) · 76 (V2 lattice) · 77 (root cause §0)
mode: INTEGRATION — no fresh research dispatched
probes_this_turn: capability_census · heritage find across C:/Dev · agent_card_verifier verify · pytest (165 passed)
claim_status: wired_with_receipts    # §1 verdicts are probe results; §2-§4 are proposed
```

# SIGRÚN APPROVED-MEMORY V0 — curated from 133 generations

Two measurements reframe everything the operator asked.

**(1) The forge repaired itself.** Census at row 77 read **ALIVE=6 / DEAD=8**.
Census this turn: ⭐ **ALIVE=21 / DEAD=9.** `cap-langgraph-runtime` and
`cap-crewai-runtime` are both ALIVE — real imports, and `runtime_probe.py`
builds a 2-node `StateGraph`, `compile()`s it, `invoke()`s it and asserts on
returned output. I read that file independently; it is an execution probe, not
an import probe. **The row-77 prescription worked.**

**(2) All four pillars already exist, tested, stranded.**
`C:/Dev/.gunnr_tmp_node1_pr95_20260719/work/valkyrie_prey_harness/` —
⭐ **14,329 lines of Python, and `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest
tools/` → 165 passed, 1 skipped, 8.69s.** Alongside it: **40 agent cards that
pass their own verifier** (`agent_card_verifier.py verify` →
`{"ok": true, "n_cards": 40}`, exit 0) and **34 `SKILL.md` files, 26,505 words**.

⛔ **gen-133 has ported none of it.** `.agents/skills/` = **0**.
`state/identity/agent_cards/` = **0**. `tools/tests/` = **0**.

> ⭐ **This is the root cause with a face on it. The capability did not fail to
> exist. It was built, tested green, and then lost across a generation boundary
> because nothing but prose carried it forward — and prose is re-interpreted,
> not executed.** The operator is not missing four pillars. He is missing a
> **port**, and a dated temp directory is holding his best engineering hostage.

---

## §1 · Curated approved-memory (32 entries)

`GOLD` = probe fired this turn or a cited receipt exists · `HALLUCINATION` =
claimed without receipt · `PARTIAL` = real but needs port/repair.

| # | name | gen source | receipt | verdict | pillar | bring-forward |
|---|---|---|---|---|---|---|
| 1 | **valkyrie_prey_harness tools** | gen-131 PR95 worktree | ⭐ **165 passed / 1 skipped, 8.69s**, 14,329 LOC | **GOLD** | P4 | ⭐ **PORT FIRST** |
| 2 | **agent_card_verifier + 40 cards** | gen-131 | `verify` → `ok:true, n_cards:40`, exit 0 | **GOLD** | P1 | port verifier + cards |
| 3 | **34 SKILL.md library** | gen-130 | 26,505 words, sourced (Rother, TPS, LEI) | **GOLD** | P3 | port — ⚠️ see §2-P3 |
| 4 | `mint_agent_cards.py` (274 LOC) | gen-131 | ships with #2 | **GOLD** | P1 | port |
| 5 | `quorum_fanout.py` 1,036 LOC | gen-131 | 507 LOC of passing tests | **GOLD** | P4 | port |
| 6 | `reputation_ledger.py` 924 LOC | gen-131 | 458 LOC passing tests | **GOLD** | P4 | port |
| 7 | `mesh_circuit_breaker.py` 400 LOC | gen-131 | 213 LOC passing tests | **GOLD** | P4 | port |
| 8 | `sigrun_secrets_env.py` 636 LOC | gen-131 | 270 LOC passing tests | **GOLD** | P4 | port |
| 9 | `valkyrie_mesh_drainer.py` 1,203 LOC | gen-131 | 808 LOC passing tests | **GOLD** | P4 | port |
| 10 | **capability_census + registry** | gen-133 row 77 | 30 claims probed, self-tested both directions | **GOLD** | P2 | keep — the spine |
| 11 | `cap-runtime-probe-executes` | gen-133 | real `StateGraph→compile→invoke` + assert | **GOLD** | P4 | keep |
| 12 | `cap-pgvector-semantic-recall` | gen-133 | cosine **0.7677** > 0.7 threshold | **GOLD** | P2 | keep |
| 13 | `cap-dbos-workflow-execution` | gen-133 | `workflow_status` row SUCCESS, uuid `5e625ec7…` | **GOLD** | P4 | keep |
| 14 | `cap-bitemporal-memory` | gen-133 | probe exit 0 | **GOLD** | P2 | keep |
| 15 | `cap-litellm-completion` | gen-133 | `'4'` from `ollama/llama3.2:3b`, unmocked | **GOLD** | P4 | keep |
| 16 | `cap-genotype-instantiable` | gen-133 | Abstract Factory returns all 4 products | **GOLD** | P4 | keep |
| 17 | `cap-games/leads-phenotype` | gen-133 | both probes exit 0 | **GOLD** | P4 | keep |
| 18 | `lineage_lease.py` + live lease | gen-133 | `leases.jsonl` 8 rows, one live in TTL | **GOLD** | P4 | keep |
| 19 | `demo01-handpiano.pages.dev` | gen-133 | HTTP **200**, 315,930 B | **GOLD** | — | the portfolio artifact |
| 20 | cross-vendor quorum votes | gen-133 | 18 dated rows, RAM-failures logged honestly | **GOLD** | P4 | keep |
| 21 | ⛔ **LangGraph "adopted"** | gen-133 pre-row-77 | **0 imports** at row 77 | **HALLUCINATION** *(since repaired — #11)* | P4 | archive as failure pattern |
| 22 | ⛔ **central_memory chain mirror** | gen-133 | `hfo_chain_row=0` under **10 contracts** describing it | **HALLUCINATION** | P2 | archive; DBOS/pgvector supersedes |
| 23 | ⛔ **XTDB install** | gen-133 | `tools/xtdb/` holds only `INSTALL_ATTEMPT.md` | **HALLUCINATION** | P2 | archive |
| 24 | ⛔ **Zep warm memory** | gen-124 | reports + manifests; **no live receipt found** | **HALLUCINATION** | P2 | archive |
| 25 | ⛔ **Slack bridge** | gen-133 | 0-byte stub; self-reported dead | **HALLUCINATION** | P4 | archive until OAuth |
| 26 | ⛔ **`demo01.handpiano.com`** | gen-133 | curl code **000** | **HALLUCINATION** | — | fix DNS or drop the claim |
| 27 | ⛔ **stigmergic composition** | gen-133 | **zero named revenue adopters** (industry scan) | **HALLUCINATION-by-design** | P4 | ⭐ honestly pre-registered DEAD — the model to copy |
| 28 | **OPA policy floor** | gen-133 | 1,209 lines across 10 `.rego`, **0 test files** | **PARTIAL** | P4 | write tests or drop |
| 29 | **SIGRUN_P4 chain** | gen-133 | 89 rows; verifier says **hash-broken at lines 1–10** | **PARTIAL** | P2 | repair root or accept as legacy |
| 30 | **Postgres/pgvector on WSL** | gen-133 | ALIVE **only while a keep-alive holds the distro** | **PARTIAL** | P2 | ⭐ hardest blocker (§2-P2) |
| 31 | **sentence-transformers** | gen-133 | `import torch` hangs >180s | **PARTIAL** | P2 | worked around via nomic-embed-text |
| 32 | **MCP servers** (`hfo_gemini`, `hfo_prey8`) | gen-89/90 | files exist, never probed | **PARTIAL** | P4 | probe before porting |
| 33 | **Codex automations** | gen-133 | 65 files, **7 ACTIVE (11%)** | **PARTIAL** | P4 | arm or archive |
| 34 | **task_queue / task_results** | gen-133 | 2 deposits, **0 pickups** | **PARTIAL→DEAD** | P4 | still the oldest open andon |

**Pattern across the HALLUCINATION rows:** every one was *described in prose and
never probed*. Every GOLD row has a program that exits 0. **There is no third
category.** That is the approved-memory rule in one line.

---

## §2 · Per-pillar Bayesian

| pillar | P(shippable this month) | P(external effect this quarter \| shipped) | blocking chain |
|---|---|---|---|
| **P1 agent-cards** | ⭐ **0.95** | ⛔ **0.05** | none — it is a file copy + a verifier that already exits 0 |
| **P2 memory** | **0.80** | **0.10** | ⭐ Postgres survives reboot without a hand-held keep-alive → bitemporal writes → recall probe |
| **P3 skills** | **0.90** | ⛔ **0.03** | none — copy 34 files |
| **P4 tools facade** | **0.70** | ⭐ **0.25** | port harness → resolve shared-site-packages conflicts → wire probes into registry |

**Adversarial counter-arguments — where Jörmungandr would be right:**

- **P1:** *"Forty personas for a solo operator with zero external effects is
  org-chart cosplay."* ⭐ **Largely correct.** One operator running one apex plus
  a few dispatches needs perhaps 5 cards, not 40. **Port the verifier and ~5
  cards; leave 35 in heritage.** The verifier is the asset; the roster is
  inventory.
- **P2:** *"cosine 0.7677 on one query/row pair is n=1, and memory only pays if
  sessions are long-lived — yours die in an hour."* Correct on both. The recall
  demo needs ≥20 pairs with a held-out negative set before it is evidence.
- **P3:** ⭐ ***"SKILL.md is prose. It is the exact substrate row 77 indicts.
  Adding 26,505 words of skills adds 26,505 more words to re-interpret
  optimistically."*** ⭐ **This is the strongest counter in the document and I
  concede it.** Skills only escape the indictment if each one carries an
  executable check. **Port skills only with a registry probe per skill, or the
  pillar is a regression.**
- **P4:** *"You are porting a 14k-line harness whose tests only pass with plugin
  autoload disabled — that is an environment on borrowed time."* Correct; the
  logfire/opentelemetry clash is real and shared across ~15 installed projects.

⭐ **Read the second column, not the first.** All four pillars are *easy to ship*
and *nearly irrelevant to income*. Summed P(external effect) is dominated by P4
at 0.25, and P4 matters only because tools are what touch Upwork, itch.io and
GitHub. **The pillars are infrastructure for a factory whose output still has no
buyer** — V2's lattice is unchanged by any of this.

---

## §3 · MAPE-K + PDCA, concretely

| loop stage | mechanism (existing file, not a plan) |
|---|---|
| **Monitor** | `tools/capability_census.py` — one activation probe per claim; a virtual actor registers its probe at claim-time or it does not exist |
| **Analyze** | census diff vs prior census → `ALIVE→DEAD` = leak, exit 1. Curated memory (§1) supplies the prior: GOLD rows are trusted, HALLUCINATION rows are never re-derived from |
| **Plan** | the **agent card** (P1) defines the actor's goal and ceiling; the **skills** (P3) define its legal toolbox |
| **Execute** | tools facade (P4) — `quorum_fanout`, `mesh_circuit_breaker`, `lineage_lease`, LiteLLM, DBOS workflows |
| **Knowledge** | bitemporal Postgres/pgvector (P2) — valid-time + transaction-time, corrections as new rows, never in-place `UPDATE` |
| **PDCA** | **Check** = the daily census; **Act** = the GitHub Actions andon Issue. **Weekly:** any capability DEAD 7 days is archived to heritage. **Quarterly:** any pillar with 0 external effects is demoted |

⛔ **The loop closes only if the census runs on a clock.**
`cap-supervision-tree` still reads **DEAD** — the workflow YAML is staged and
unpushed. **Until the operator pushes it, MAPE-K has a Monitor and no clock,
which is PDCA with the Check step performed by whoever remembers.**

---

## §4 · Build specs for Olrún

| # | spec | tier | timebox | deliverable + acceptance | registry probe |
|---|---|---|---|---|---|
| **B1** ⭐ | **PORT-THE-HARNESS** — copy `valkyrie_prey_harness/tools/` into `tools/harness/`, pin `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` | sonnet-5 | 90 min | `pytest tools/harness/ -q` → **165 passed** *in gen-133* | `cap-harness-tests-green` |
| **B2** | **PORT-CARDS-THIN** — verifier + **5** cards (Sigrún, Olrún, Jörmungandr, +2), not 40 | sonnet-5 | 45 min | `agent_card_verifier.py verify` exits 0 in gen-133 | `cap-agent-cards-verified` |
| **B3** | **SKILLS-WITH-TEETH** — port **5** highest-value SKILL.md, each with an executable check | sonnet-5 | 60 min | 5 skills, 5 probes, all exit 0; ⛔ **a skill without a probe is rejected** | `cap-skills-probed` |
| **B4** | **MEMORY-DURABILITY** — Postgres survives a reboot without a hand-held keep-alive; recall on **≥20 pairs + held-out negatives** | sonnet-5 | 90 min | recall probe exits 0 **after** a WSL restart | `cap-memory-survives-restart` |
| **B5** ⭐ | **PUSH-THE-CLOCK** — operator taps ENV-B; workflow runs once | operator | 5 min | `gh run list` returns ≥1 run | `cap-supervision-tree` flips ALIVE |

**External-fitness gate:** B1–B4 are *internal* capability work and produce **no
external effect by construction**. Per V2 §4 they do **not** count against the
`N=3` external experiment cap — and they do not substitute for it either.

---

## §5 · Where I was wrong

1. ⛔ ⭐ **V1 §1 — "freeze the stack, $0/mo, drop everything" — was WRONG, and
   expensively.** The stack-builder session added Postgres, pgvector, DBOS and
   CrewAI and the census went **6 → 21 ALIVE**. My freeze would have prevented
   the largest capability gain of the generation. **The error:** I generalized
   *"tool churn is the wound"* into *"no new tools."* The real distinction is
   **probed adoption vs prose adoption**. Churn without probes is the wound;
   adoption with a pre-registered probe is safe and was the whole point of row
   77. **V1 §1 is RETRACTED and replaced by: adopt freely, probe at claim-time.**
2. ⛔ **My decline-discipline was over-tight.** I declined seats across V1/V2/§0
   on "supply against a demand constraint" grounds. The seats that ran produced
   15 new ALIVE capabilities. **That heuristic is correct for outbound and
   document work and wrong for internal capability work.** Corrected here: B1–B4
   dispatched without hesitation.
3. ⚠️ **Row 77's root cause SURVIVES and is now better evidenced** — the stranded
   worktree is the cleanest instance of it yet. But P3 partially *contradicts*
   the prescription: porting 26,505 words of prose skills adds re-interpretation
   surface. **Resolved by B3's rule — no skill without a probe.**
4. **Unchanged:** V2's market lattice, `N=3`, the M1×G1 complementarity, and the
   2026-08-16 global falsifier. **None of the four pillars moves a buyer**, and
   nothing this turn touched income.

---

## Honest flaws

1. ⭐ **`claim_status: wired_with_receipts` covers §1's verdicts only.** §2's
   probabilities are calibrated judgment; §3 and §4 are `proposed`.
2. **The 165-test suite passes only with `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`.**
   With autoload on it does not even collect. **I am grading GOLD on a suite that
   needs a flag to run** — real, but fragile, and B1 must carry the flag or the
   port is a false green.
3. **I did not read the 34 SKILL.md files or the 40 agent cards for content
   quality.** I verified they exist, are substantial, and pass a verifier.
   **Verified-shaped is not verified-good.**
4. **`INDUSTRY_PATTERN_CONVERGENCE` lives at `state/industry_patterns/`, not the
   path in the brief.** I read its verdicts secondhand via `DURABLE_SUBSTRATE`
   and the registry notes — ⚠️ **the "LangGraph stronger fitness than CrewAI"
   claim is inherited, not independently checked by me.**
5. **32 curated entries is what I found in one pass across `C:/Dev`.** 133
   generations certainly hold more GOLD; **absence here is not absence.**
6. ⭐ **Every pillar is easy and none of them pays.** If this document causes a
   week of pillar-building instead of B5 plus the §4 external experiments, it
   will have been the most productive-looking mistake of the generation.

*Réttu hönd, eigi spyr. Standa.*
