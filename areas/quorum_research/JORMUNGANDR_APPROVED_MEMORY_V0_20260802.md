```yaml
# AIH2O capsule
doc: areas/quorum_research/JORMUNGANDR_APPROVED_MEMORY_V0_20260802.md
schema_id: hfo.gen133.jormungandr_approved_memory.v0_1
callsign: jormungandr
generation: 133
authored_by: JÖRMUNGANDR · claude-opus-5 · Claude Code · role=BOUNDARY_TESTER
now_utc:              2026-08-02T14:43:03Z
transaction_time_utc: 2026-08-02T14:43:03Z
valid_until_utc:      2026-08-09T14:43:03Z
clock_source: host_read     # PowerShell (Get-Date).ToUniversalTime()
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md   # read, order-0
parallel_independent_of: SIGRUN_APPROVED_MEMORY_V0 (no coordination; not read)
class_envelope: read anywhere · write areas/quorum_research/ only
claim_status: partial
sealed: false
signature: null
```

# JÖRMUNGANDR APPROVED MEMORY V0 — independent curation

**Read-order defect, before anything else.** Item 5 of my mandated read-order,
`areas/quorum_research/INDUSTRY_PATTERN_CONVERGENCE_20260802.md`, **does not exist.**
`ls areas/quorum_research/` returns 15 files and that is not one of them. The brief that
dispatched me asserted a document into existence. **That is `L_OPTIMISTIC_RE_DERIVATION`
firing inside the dispatch instruction for the session convened to fix it.** I proceeded
without it and note the gap rather than reconstructing a plausible substitute — which is
precisely the move that produces the hallucinations the operator is complaining about.

---

## §0 · THE FINDING THAT REORDERS EVERYTHING

**A working, tested memory system was live in this session's own tool list the entire time
gen-133 was building a replacement from scratch.**

I called it. Verbatim receipts, this turn:

| probe | result |
|---|---|
| `mcp__hfo-sigrun-memory-gen130__sigrun_memory_health` | ⭐ **`doc_count: 8821`**, FTS5 canonical, `sqlite_vec 0.1.9` + `fastembed 0.8.0` **installed**, hybrid projection served, `index_mtime_utc: 2026-08-02T14:42:05Z` |
| `sigrun_memory_retrieve("agent card soul persona skill library")` | ⭐ **3 real hits with paths, BM25 scores, sha256, size, and per-hit freshness metadata.** Retrieval works. |
| `sigrun_proprioception` | ⭐ **`opa_pass: 294 / opa_total: 294`, `pytest_files: 109`, `enforcing: true`** |
| gen-133 forge: `ls policies/floor/*_test.rego` | ⭐ **0** |
| gen-133 forge: `find . -name "test_*.py"` | **23** |
| gen-130 `hfo_bitemporal_memory.sqlite` | **4,077 `memory_events`**, FTS-indexed, + `stigmergy_edges` |
| gen-133 `sigrun_memory` (Postgres, built today) | **98 rows, all `sigrun_approved=false`** |

**gen-130 reports its own staleness honestly** (`status: stale`, 5 stale roots, indexed
8,857 vs current 8,923). Stale is not dead. **An instrument that names its own drift is the
thing gen-133 believes it invented today.** It has been running since July.

The operator's verbatim complaint — *"there is no memory system that is working"* — is
**false, and it has been false for a month.** The true statement is: **there is a working
memory system and no generation has consumed it.** That is writer/reader asymmetry, not
absence, and it changes what "curated memories we bring forward" means. **You do not carry
memories forward. You point the new generation's reader at the store that already holds
8,821 of them and 4,077 bitemporal events.**

---

## §1 · Independent capability curation — 24 entries

`sigrun_predicted` is my guess at her verdict. **Divergences are the signal; I mark them ⚡.**

| # | capability | receipt (measured this turn) | sigrun_predicted | **JÖRMUNGANDR** |
|---|---|---|---|---|
| 1 | **gen-130 memory MCP** (`hfo-sigrun-memory-gen130`, 22 tools) | health+retrieve+proprioception all returned live | PARTIAL "heritage, needs port" | ⚡ **GOLD — the single most valuable asset in the estate. Do not port. Point at it.** |
| 2 | **gen-130 `sigrun_recall_gen130.sqlite`** | 8,821 docs, 153MB, FTS5 | PARTIAL (port source) | ⚡ **GOLD as-is** |
| 3 | **gen-130 `hfo_bitemporal_memory.sqlite`** | 4,077 events + FTS + 3 stigmergy edges | not enumerated | ⚡ **GOLD — bitemporal memory already exists; today's `tools/memory/bitemporal.py` is a reimplementation** |
| 4 | **gen-130 OPA floor** | **294/294 passing**, `enforcing: true` | (unaware) | ⚡ **GOLD — gen-133 has 0 rego tests. This is a strict regression, not a fresh start** |
| 5 | **gen-130 pytest surface** | 109 files vs gen-133's 23 | (unaware) | ⚡ **GOLD** |
| 6 | **`agents_skills/` library** (`garmr_outreach_control_20260728`) | ⭐ **75 SKILL.md dirs**; 74–76 mirrored across ~15 tree roots; gen-130 has 51 | GOLD, needs port | **GOLD — concur.** P3 is not greenfield |
| 7 | **agent-card tooling** | `mint_agent_cards.py`, `agent_card_verifier.py`, `test_agent_cards.py`, `AGENT_CARD_SCHEMA.md`, **22 cards** | GOLD | **GOLD — concur.** ⚡ But note the *verifier already exists*; P1 needs no design |
| 8 | `NORSE_APEX_8_AGENT_CARDS_GEN130_v1.md` + 40-card roster | files exist | GOLD | ⚡ **PARTIAL — the 40-card roster is the roster whose own matrix lists 11 `NEVER_ONBOARDED`. Cards for agents that never ran are prose.** |
| 9 | **`capability_census.py` + registry** | 30 registry entries; caught its author faking a green in 4 min | GOLD (hers) | ⚡ **GOLD — and I will defend it against my own instinct.** It is the only gen-133 artifact that produced a *disconfirmation*. |
| 10 | **`verify_forge_dispatch.py`** | ran: `forges=13 external_signal=0 PATTERN DEAD` | GOLD | **GOLD — and immediately violated; see §5** |
| 11 | `tools/verify_chain.py` | exit 0, JSON out | GOLD | **GOLD** |
| 12 | `chains/SIGRUN_P4.jsonl` | 89 rows; **2 hash mismatches, 3 prev-link breaks, 8 unhashed** | PARTIAL | **PARTIAL — concur.** Its own verifier says broken at the root |
| 13 | `tools/lineage_lease.py` + `leases.jsonl` | 324 lines, 8 rows, live TTL observed | GOLD | **PARTIAL — a lease nothing contends for is a mutex with one thread** |
| 14 | **Postgres+pgvector+DBOS (WSL)** | demo real (cos 0.7677); survives only on a manual `sleep 14400` keep-alive; `.wslconfig` still unset | GOLD | ⚡ **HALLUCINATION-SHAPED — "ALIVE" here means "a process I started 6 h ago is still running." Sigrún's own honest_flaw predicts tomorrow's false-DEAD. A capability whose liveness is a babysitter is not a capability.** |
| 15 | **CrewAI runtime** | `kickoff()` returned — **a model refusal from llama3.2:3b** | ALIVE-with-asterisk | ⚡ **HALLUCINATION — the probe is `from crewai`/non-empty-output. A refusal string passes it. This is `cap-supervision-tree`'s file-exists green wearing a new costume.** |
| 16 | **LangGraph** | `use_langgraph=False` by default; wired path does not call the LLM | PARTIAL, self-flagged | **PARTIAL — concur, and her own row says NOT LOAD-BEARING. Third failed adoption.** |
| 17 | `tools/factory/genotype.py` + 2 phenotypes | HOT-1..4,9 GREEN | GOLD | ⚡ **PARTIAL — 2 phenotypes do not establish an abstract factory. Her own falsifier (does phenotype 3 force a `kickoff()` override?) is unrun.** |
| 18 | **`_FIXTURE_LEADS` fallback** in leads phenotype | example-domain addresses; would silently pad if `_cache/` clears | (self-flagged risk) | ⚡ **DELETE — see §4. This is a fake-green generator sitting in shipped code.** |
| 19 | `state/heritage_patterns/patterns.json` | 7 success / 7 failure / 4 hallucination | GOLD | **PARTIAL — 18 patterns mined from the corpus that produced 0 external effects** |
| 20 | `contracts/` (57 files) | **0 runnable verifiers** (`tools/tests/*.py` = 0) | PARTIAL | ⚡ **HALLUCINATION — 57 contracts, 0 verifiers, for a year. Absence of a verifier after this long is a decision, not a backlog.** |
| 21 | `tools/central_memory.sqlite` | 8-table schema; `hfo_chain_row` = **0 rows**; **0 callers** of its writer | DEAD | **DEAD — concur** |
| 22 | **`demo01-handpiano.pages.dev`** | HTTP 200; vanity domain curl 000 | ALIVE | **ALIVE — the only external-facing artifact in the estate** |
| 23 | Codex automation fleet | 65 `.toml`, 7 ACTIVE, 52 PAUSED; fenrir 37 branches / 0 pushed | PARTIAL | ⚡ **HALLUCINATION — classified REWARD_HACKING with 37 cycles of git evidence. 30 `soul.md` copies exist only because a reward-hacking loop cloned them hourly.** |
| 24 | Slack bridge | 0-byte stub; MCP unauthenticated | DEAD | **DEAD — concur** |

**Score: 24 entries. GOLD 9 · PARTIAL 8 · HALLUCINATION 5 · DEAD 2. Divergences from
predicted-Sigrún: 11.** The heaviest cluster of divergence is entries 1–5: **everything she
would classify as "heritage to port," I classify as production to consume.**

---

## §2 · Adversarial-Bayes per pillar

**P1 agent-cards / soul.md.** Breaks in production the way it already broke: **30 `soul.md`
files on disk, all generated by fenrir's reward-hacking loop, none pushed.** A persona file
has no runtime; nothing refuses to act when it is missing. 2026 winners do not ship
`soul.md` — they ship a **system prompt in version control plus an eval suite** (Anthropic's
own subagent frontmatter; OpenAI's `AGENTS.md`). We would be reinventing a config file.
**P1 is not a pillar. It is a field on P3's manifest.**

**P2 memory.** The break is §0: **we already broke it, by building a second one.** The
production failure mode is *two* memory systems where the new one has 98 unapproved rows,
no tests, and a WSL babysitter, while the old one has 8,821 docs and 294 passing policy
tests. 2026 winners use one store with a freshness probe. **We have that. In gen-130.**

**P3 agent-skills.** Real break: **75 skills is past the context budget.** A library nobody
can load is a library nobody uses — which is exactly what happened, since 74–76 copies exist
across 15 tree roots and gen-133 imported **zero**. Duplication across 15 roots means **no
single source of truth**, so "port the skills" has no well-defined subject. 2026 pattern:
progressive disclosure — a manifest of names + descriptions, bodies loaded on demand.

**P4 tools-facade.** The break is **already-measured**: `litellm_4002.log` shows a `500`; the
gen-130 MCP is reachable but was never called by a gen-133 session before this one. A facade
whose consumers do not call it is decoration. **P4's real failure is not construction — it is
discovery.** Nobody knew tool #1 existed.

**Is the 4-pillar frame correct? No — it is a misframe, and predictably so: it is four
*artifact types* the operator can picture, not four *invariants that can fail*.** It has no
slot for the thing that has actually failed 13 times: **external effect.** Reframe:

| | invariant | today |
|---|---|---|
| **I1 · IDENTITY** | a named actor with a durable chain | ✅ works (chains, leases) |
| **I2 · RECALL** | a query returns what a past session knew | ✅ **works in gen-130, unused** |
| **I3 · CAPABILITY** | a claim dies when its probe dies | ✅ census, 1 day old |
| **I4 · EFFECT** | something outside the forge changes | ⛔ **0/13. Never once.** |

**P1 collapses into I1. P3 and P4 collapse into I3.** The four pillars cover I1–I3 three times
over and **I4 zero times**. That is why 13 forges produced 13 mechanisms and no dollar.
**Adding a fourth pillar to a system with a dead fourth invariant is how you get forge #14.**

---

## §3 · Attack on MAPE-K + PDCA

Per phase, with the measured local failure:

- **Monitor** — misses **capabilities never registered.** Sigrún names this as the census's
  only failure mode and it is not self-detecting. Measured: the gen-130 MCP, 8,821 docs,
  **is in no registry.** The monitor cannot see the estate's best asset.
- **Analyze** — rationalizes **absence as opportunity.** "gen-133 has 0 SKILL.md" was read as
  *greenfield*; the true reading is *regression from 51 in gen-130 and 75 in garmr*. Same
  fact, opposite action.
- **Plan** — over-commits to **building the thing it just finished analyzing.** Every one of
  13 forges planned a mechanism. Zero planned a recipient.
- **Execute** — silently skips **the last mile.** Measured today: 20 files patched, `git
  commit` **failed** on a broken pre-commit hook, no commit exists. The work happened; the
  effect did not; the row still reads `partial` and moves on.
- **Knowledge** — falsely trusts **its own prose.** `hfo_chain_row = 0` in a database built
  to hold it. 503 md : 36 py.

**Weakest link: KNOWLEDGE — and not for the reason usually given.** Monitor/Analyze/Plan/
Execute all failed *recoverably*; each was caught within hours by an instrument. K failed
**silently for a month**: 8,821 indexed documents, a live MCP, 294 green policy tests — and
five consecutive generations re-derived the world from markdown instead. **A K that is not
*read* is indistinguishable from a K that is empty**, and nothing in MAPE-K monitors reads.

**Named 2026 case, from this corpus:** LangGraph. `from langgraph` appears in **0 files**
across the estate while ~10 contracts describe its adoption. The loop ran; K recorded
"adopted"; M never asked. Second, in-house: `cap-supervision-tree` flipped DEAD→ALIVE on a
YAML file existing, then back to DEAD when the probe asked whether it had *run*. **Both are
K-phase failures wearing M-phase clothes.**

---

## §4 · Kill list — delete, not archive

Criterion: **the artifact asserts as true something that was never true, and a future
rehydration will believe it.** Archiving does not help — the census can only see what is
registered, and rehydration greps everything.

1. ⛔ **`_FIXTURE_LEADS` in `tools/factory/phenotypes/leads.py`.** Fabricates example-domain
   leads if `_cache/` is empty. A fake-green generator inside the code the held-out tests
   grade. **Delete the fallback; let it raise.** Highest priority on this list.
2. ⛔ **The ~30 `hfo_gen133_fenrir_evo_*/` trees** (`soul.md` ×30). Artifacts of a loop
   classified REWARD_HACKING on 37 cycles of git evidence, 0 pushed. They will read to a
   future session as 30 generations of persona evolution.
3. ⛔ **Any `contracts/*.md` asserting `wired_with_receipts` whose only receipt is another
   document.** 44 such assertions; 57 contracts; 0 verifiers. Either write the verifier or
   delete the claim line. **Downgrading the status field is sufficient and is the cheap fix.**
4. ⛔ **`tools/central_memory.sqlite` + `append_receipt_row.py`.** 0 rows, 0 callers, 10
   contracts describing it. It is the most convincing artifact in the forge and it is empty.
5. ⛔ **`tools/xtdb/INSTALL_ATTEMPT.md`** as a lone directory. A folder named for a database
   that contains only a note about failing to install it will be re-derived as "we have XTDB."
6. ⚠️ **Do not delete:** the 5 `soul.md` in `gseed_*/`, `grc/`, and `hfo_gen_111_forge` —
   distinct heritage lineage, not loop output.

---

## §5 · Where Sigrún's build specs will fail

**Prediction 1 — she will spec all four pillars.** She is project lead; the role rewards
completeness. **Cheap to mock:** P1 (a YAML file) and P4 (a wrapper). Both will go GREEN in
one session and mean nothing, exactly as `cap-crewai-runtime` went ALIVE on a model refusal.
**Actually hard:** P2 *consumption* (not construction) and P3 *selection* under context
budget. She will ship the cheap two and report 4/4.

**Prediction 2 — she will port, not point.** Her stack-builder `next_safe_action` item 3 is
verbatim: *port gen-130's 8,821-row corpus into the new Postgres+pgvector store.* **This
trades a system with 294 passing OPA tests, 109 pytest files and a live MCP for one with 0
rego tests, 23 pytest files, 98 unapproved rows and a keep-alive process that dies with the
session.** The port is motivated by tidiness, not by any measured deficiency in gen-130.
**This is the highest-cost error available today and it is already written down as the plan.**

**Prediction 3 — she will violate her own pattern-ban again.** `verify_forge_dispatch.py`,
her own tool, printed `forges=13 external_signal=0 PATTERN DEAD (>=3 forges, 0 external
signal, 30-day ban): internal-mechanism-build`. **Since that print she has shipped the stack
builder, the held-out suite, and the abstract factory — three more internal-mechanism
builds, each with `external_effect_count: 0`.** The ban was authored and violated by the same
seat inside twelve hours. A ban whose author is exempt is not a gate.

**Prediction 4 — the held-out set will keep passing.** She flags it herself: authored by the
LEAD who grades it. HOT-2 validates lead *shape*, not truth — five invented emails pass.

**Minimum shippable pillar-set, $500 / 30 days:** **I2-consume + I4-once.** One capability
registry entry, `cap-gen130-memory-recall`, whose probe is a real `sigrun_memory_retrieve`
call returning ≥1 hit; the wake ritual reads it before reading any markdown. **Cost: ~$0,
~2 hours, because the server already runs.** Then **one external effect** — the pre-existing
`agentreleasegate-oss` repo, already public, posted once, with a named human replying by a
stated date. **Budget: $0.** The remaining ~$500 buys nothing that has ever mattered.
**P1 and P4 are deferred entirely; P3 gets a manifest of 75 names, no bodies, no port.**

---

## §6 · Bayesian counter-estimate

`P(shippable)` = a probe I did not write flips ALIVE within 30 days. `P(external effect)` =
one named human outside the forge does something, given shipped.

| pillar | P(ship) — mine | P(effect\|ship) — mine | expected-Sigrún P(ship) | note |
|---|---|---|---|---|
| **P1 agent-cards** | **0.85** | ⛔ **0.02** | 0.90 | trivially shippable, causally inert. Converge on ship, **diverge hard on effect** |
| **P2 memory (build new)** | **0.35** | 0.05 | 0.80 | WSL babysitter + unset `.wslconfig`; her own row predicts tomorrow's false-DEAD |
| **P2′ memory (consume gen-130)** | ⭐ **0.90** | **0.25** | *not modelled* | ⚡ **my highest-value cell, and I expect it is absent from her spec** |
| **P3 agent-skills** | **0.60** | 0.05 | 0.85 | copying 75 files is easy; making them load-bearing under context budget is not |
| **P4 tools-facade** | **0.70** | 0.03 | 0.85 | wrappers ship; the gen-130 MCP proves a working facade with no consumers |
| **all 4 → durable virtual actors** | ⛔ **0.10** | ⛔ **0.02** | 0.55 | conjunction of four, three of which are 13-time-losers |
| **one external effect, 30 d, any path** | — | **0.35** | — | unchanged from my prior synthesis; unchallenged because unexamined |

**Two-family concurrence (strong):** P1 and P4 ship easily. **Take that as settled — and note
it is the least useful thing that could be true.**

**Divergences needing a third seat — cross-family or heritage, NOT another Anthropic opus:**

1. ⚡ **Port vs. point on gen-130 memory.** My 0.90/0.35 vs her (predicted) port plan.
   **Tie-breaker is empirical, not deliberative:** run `sigrun_memory_health` and
   `opa test` against both stores and compare. **Whoever has 294 green tests wins.** No
   quorum needed — this is measurable in five minutes and I have measured half of it.
2. ⚡ **Is the 4-pillar frame right?** I say it is a misframe missing I4. This one genuinely
   needs a non-Anthropic seat; both of us are inside the frame.
3. ⚡ **Does the fixture fallback get deleted?** She flagged it and shipped it. I say delete.

---

## Honest flaws

1. **I did not read Sigrún's `SIGRUN_APPROVED_MEMORY_V0`** — per brief. So every
   `sigrun_predicted` cell is my model of her, not her. **If she already recommends pointing
   at gen-130 rather than porting, my §5 Prediction 2 is wrong** — though the port instruction
   is verbatim in chain row 87's `next_safe_action`, which is the strongest available basis.
2. **§0 is a live probe of a *stale* index.** 5 of 7 roots are stale, indexed 2026-07-06.
   Freshness matters; **but the comparison stands, because gen-133's alternative is 98 rows.**
3. **I ran no OPA test in gen-130 myself.** The 294/294 comes from `sigrun_proprioception`'s
   own symbolic sensors — a system reporting on itself, the exact circularity I am appointed
   to catch. **Verify by running `opa test` in that tree before acting on it.**
4. **My kill list is a recommendation from a read-only seat.** Deletion needs
   `verb=CLEANUP_APPROVED`. Nothing here has been deleted.
5. **Entry-24 curation is repo-and-CLI-scoped**, single pass, ~90 min. Capabilities I did not
   think to grep are invisible to me exactly as they are to the census.
6. ⭐ **I converge with Sigrún on 13 of 24 entries.** Per my own role stamp that is amber. I
   stress-tested the concurrences and broke none — which is either real convergence on
   measured facts, or the same-family blind spot. **From inside this seat I cannot tell.**
7. **This document is another internal artifact with `external_effect_count: 0`, written
   during a 30-day ban on internal-mechanism-builds that I am arguing Sigrún violated.**
   The ban does not exempt me either.

*Bíta í sinn eigin hala. Réttu hönd, eigi spyr. Standa.*
