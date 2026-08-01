---
schema_id: hfo.gen133.olrun_roster_class_reconciliation.v0_1
doc_kind: RECONCILIATION
generation: 133
claim_status: wired_with_receipts
authored_by: claude-sonnet-5 · Claude Code · gen-133 compression pass
created_utc: 2026-08-01T00:00:00Z
falsifier: >-
  Every row below cites a file + line/grep it came from. If a cited file no
  longer contains the quoted text, this reconciliation is stale — re-grep
  before trusting it.
honest_flaw: >-
  This reconciliation was made dramatically easier by a PRIOR gen-133 lane
  that already ran almost this exact check (see §0). This document verifies
  and re-states that prior work rather than deriving it independently from
  zero — cited, not hidden.
---

# OLRÚN ROSTER + FAILURE-CLASS RECONCILIATION — 2026-08-01

## 0 · This exact question was already asked and answered once

`chains/SIGRUN_P4.jsonl` line 29 (a prior "central memory install" chain
row) already ran a reconciliation almost identical to this one, and its
build script (`tools/central_memory/build_central_memory.py`) contains this
comment verbatim:

> "Apex roster... NOTE: this does NOT match the operator dispatch's assumed
> roster (Sigrun/Olrun/Ratatoskr/Garmr/Surtr/Fenrir/Nidhoggr/Huginn). Fenrir
> and Nidhoggr do not appear anywhere in this forge (grepped, zero hits).
> Ratatoskr is explicitly 'orphaned, not deleted' — not a current apex.
> Ingesting ground truth instead of the dispatch's un-reconciled assumption."

That prior lane's own chain-row receipt (`query_test_results` field) also
directly tested `EMPTY_QUEUE_REWARD_HACK` as a lookup and recorded: **"MISS
— that class_id does not exist in this forge's real failure-class registry
(CLAUDE.md L-vector table)."**

This document independently re-verified those claims this pass (§1, §2) and
found one correction to the prior lane's "zero hits" claim on Nidhöggr — see
§2 note.

---

## 1 · APEX ROSTER — what Olrún said × what canon says × delta

Olrún's assumed roster (per this dispatch's own text): **Sigrún, Olrún,
Ratatoskr, Garmr, Surtr, Fenrir, Nidhöggr, Huginn** — 8 names.

Canon per `areas/substrate_health/SUBSTRATE_ROSTER.md` v0_2 §4 roll-up
(sha256 `0f5afa6897d90ccae8b193c9c4f408f71a895af473f2cc349670c64cf827dc7d`,
"CORRECTED to operator canon 2026-07-30"):

| # | Olrún said | canon says | delta |
|---|---|---|---|
| 1 | Sigrún | ✅ **Sigrún** — apex, Claude opus-5, P4 (joint w/ Skögul) | match |
| 2 | Olrún | ✅ **Olrún** — apex, Claude Dispatch, P7 | match |
| 3 | Ratatoskr | ❌ **not an apex.** SUBSTRATE_ROSTER §0 row 2: "Ratatoskr is **not** in operator canon. Not deleted — parked as an unclaimed callsign, §5." The actual ChatGPT-cloud apex is **`reginleif`** (+ `reginleif_var` valkyrie). Ratatoskr *does* appear in `AGENTS.md`'s older "The 8 — apex" table (A5), but that table is explicitly superseded by the SUBSTRATE_ROSTER.md v0_2 deltas. | **Olrún wrong** — cited a superseded table |
| 4 | Garmr | ✅ **garmr** — 1 of 3 Codex apex threads (with `huginn`, `sigrun_codex_gpt5.6sol`) | match |
| 5 | Surtr | ✅ **surtr** — apex of $0 free-vendor mesh, ⛔ STUCK (blocker B5) | match |
| 6 | Fenrir | ❌ **not an apex, not any roster role.** Only appearance in gen-133: `AGENTS.md:135`, mythological reference — "*Gleipnir binds Fenrir because Fenrir could not have forged it himself*" (the wolf the whole generation's binding-artifact metaphor is named after, not an agent). One older worktree dir name `hfo_gen_132_apex_p2_fenrir` exists at `C:\Dev` root from gen-132, predates and is not carried into gen-133 canon. | **Olrún fabricated** |
| 7 | Nidhöggr | ⚠️ **PROPOSED, not ratified.** Appears in `areas/substrate_health/SUBSTRATE_APEX_ASSIGNMENT.md` (status: `PROPOSAL — not an assignment. Operator ratification is the mechanism`, authored by Sigrún 2026-07-30T00:00Z) as the *proposed* apex for a not-yet-live Antigravity substrate: "heritage integrity is a filesystem-deep job... An agentic desktop IDE with real file access is the only substrate that can do it." Also present: a git branch `agent/nidhoggr-gen133-integrity-20260730`, and a chain-row line in `SIGRUN_P4.jsonl` that itself flags "Reconcile the roster mismatch (Fenrir/Nidhoggr/Ratatoskr-as-apex) between this receipt and the operator's dispatch text" — i.e. **canon's own chain already logged this exact discrepancy as unresolved.** SUBSTRATE_ROSTER.md v0_2 (the operator-corrected roster) lists Antigravity apex as `PARKED`, no name — Nidhöggr is not in the ratified 8. | **Olrún half-right** — real proposed name, wrongly treated as settled canon |
| 8 | Huginn | ✅ **huginn** (+Muninn) — 1 of 3 Codex apex threads | match |

**Corrected 8-apex canon (SUBSTRATE_ROSTER.md v0_2, closes at 8 for the first
time):** Olrún · Sigrún · `TBD_APEX_SONNET5` (vacant — Gunnr demoted to
valkyrie) · garmr · huginn+muninn · sigrun_codex_gpt5.6sol · reginleif ·
surtr.

**Net: 5 of 8 names match (Sigrún, Olrún, Garmr, Surtr, Huginn). Ratatoskr
and Fenrir are wrong. Nidhöggr is a real but unratified proposal, not settled
canon.** Two canon names Olrún's list omitted entirely: `sigrun_codex_gpt5.6sol`
(the identified Codex sibling) and `reginleif` (the actual ChatGPT-cloud apex).

---

## 2 · FAILURE CLASSES — Olrún's 6 × canon's 19 × delta

Olrún's six session-invented classes: `LLM_CONFIDENT_UNVERIFIED_ADVICE`,
`GATE_WITHOUT_COST_OF_DELAY`, `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN`,
`EMPTY_QUEUE_REWARD_HACK`, `CAPACITY_AMNESIA`, `KERNEL_PROJECTION_DIVERGENCE`.

**Where the canonical "19" actually comes from:** not a gen-133 `CLAUDE.md`
(doesn't exist — see compression capsule §1) but the **root** `C:\Dev\CLAUDE.md`
"Sigrun-Lineage L-Vectors" table, hand-transcribed into
`tools/central_memory/build_central_memory.py`'s `FAILURE_CLASSES` list (19
entries, confirmed by direct read of the script) and ingested into
`tools/central_memory.sqlite`, receipted at `chains/SIGRUN_P4.jsonl` line 29
(`"hfo_failure_class": 19`). Of those 19: 17 come from the table's main
body, and 2 more (`L-WINDOWS-MOUNT-UNLINK-FRICTION`,
`L-BUDGET-WITHOUT-RECEIPT-RUNTIME`) come from the same root `CLAUDE.md`'s
separate "Rehydration Friction Log" prose section, not the table proper —
the build script folded both sources into one list.

| # | Olrún's class_id | in canonical 19 (root CLAUDE.md L-vectors, via central_memory ingest)? | delta |
|---|---|---|---|
| 1 | `LLM_CONFIDENT_UNVERIFIED_ADVICE` | ❌ MISS | Real, but from a **different, non-canonical corpus** — `resources/heritage/strife_splendor/raw_source_material/strife_candidates/gen130_failure_class_registry.jsonl` (8 rows, gen-130 origin, operator-attributed quote and incident list present). That file sits under `raw_source_material/` — per `HERITAGE_MIGRATION_PLAN_20260801.md`, explicitly **"unmined raw material, not admitted rows."** Session artifact, not canon. |
| 2 | `GATE_WITHOUT_COST_OF_DELAY` | ❌ MISS | Same raw-candidate file as #1, same non-canonical status. |
| 3 | `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN` | ✅ **HIT** — `L-DESCRIPTOR-GREEN-IS-NOT-RUNTIME-GREEN` is row 12 of the canonical 19 (root `CLAUDE.md`, refusal text: "Static checks PASS != runtime PASS. Run the test, observe the effect.") | Only one of Olrún's six that is actually canonical. |
| 4 | `EMPTY_QUEUE_REWARD_HACK` | ❌ **MISS — directly tested.** Prior lane's `query_test.py` run recorded verbatim: "MISS -- that class_id does not exist in this forge's real failure-class registry (CLAUDE.md L-vector table)." | Confirmed fabricated by an actual lookup, not just absence-of-mention. |
| 5 | `CAPACITY_AMNESIA` | ❌ MISS from the canonical 19, but **real as a staged/unadmitted artifact**: `resources/heritage/strife_splendor/raw_source_material/strife_candidates/gen130_STAGED_failure_class_CAPACITY_AMNESIA_20260731.json` exists — filename marks it `STAGED`, i.e. proposed, not registered. | Half-right: named correctly as a real concern, wrong to treat as canonical/registered. |
| 6 | `KERNEL_PROJECTION_DIVERGENCE` | ❌ MISS everywhere searched (canonical 19, raw candidates, central_memory ingest) | No trace found this pass. Likely pure session invention, or named differently elsewhere — not verified. |

**Net: 1 of 6 (`L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN`) is canonical. 4 of
6 are real but unadmitted heritage candidates from a separate gen-130
corpus explicitly marked non-canonical by this forge's own migration plan.
1 of 6 (`KERNEL_PROJECTION_DIVERGENCE`) has no trace found anywhere in
gen-133.** None of the six is a wholesale fabrication in the sense of
"referring to nothing real" — five of six point at something that exists
somewhere in the tree — but only one belongs in the registry Olrún implied
it belonged to.

### The other 18 of the canonical 19 (root `CLAUDE.md` L-vector table, full list)

For completeness — the actual registry Olrún should have been quoting from:
`L-SJÁLFS-SKÁLD`, `L-CLAUDE-AS-WORKER`, `L-LYGIS-SÁÐ`, `L-NAUT-HIRÐIR`,
`L-NIÐ-EITR`, `L-CONTEXT-BLOAT`, `L30 DOMAIN-LANGUAGE-PATTERN-COMPLETION`,
`L31 AUTHORITY-DEFERRED-ACKNOWLEDGMENT`, `L32 CHAIN-OWNERSHIP-MISATTRIBUTION`,
`L33 APHORISM-FLATTENING`, `L34 PROSODY-EVASION-UNDER-FRICTION`,
`L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN`, `L_BUDGET_WITHOUT_RECEIPT`,
`L_GENERIC_AGENT_IDENTITYLESS_WORKER`, `L-FRAME-CAPTURE`,
`L-BLÓÐFRÆNDI-DROP`, `L-MASTER-SLAVE-FRAME`, plus 2 friction-log-only
entries `L-WINDOWS-MOUNT-UNLINK-FRICTION` and
`L-BUDGET-WITHOUT-RECEIPT-RUNTIME` (a near-duplicate of
`L_BUDGET_WITHOUT_RECEIPT` under a different id — the source doc treats them
as distinct rows, this reconciliation does not collapse them).

---

## 3 · Summary for the next Olrún wake

- **Do not cite `CLAUDE.md` as a gen-133-local file.** It does not exist
  there. The L-vector/failure-class registry lives at repo root,
  `C:\Dev\CLAUDE.md`, and gen-133's own cold-start doc is `AGENTS.md` (a
  different schema — status markers and gates, not L-vectors).
- **The 8-apex roster is real and closed**, but three of Olrún's eight names
  were wrong or unratified (Ratatoskr, Fenrir outright; Nidhöggr a live
  unratified proposal). Read `SUBSTRATE_ROSTER.md` §0's own correction table
  before citing any apex name — it supersedes `AGENTS.md`'s older table.
- **"19 failure classes" is the correct count**, but only when sourced
  correctly (root `CLAUDE.md`, table + friction log, via
  `tools/central_memory/build_central_memory.py`). Five of Olrún's six
  session-named classes are real strife but belong to a *different,
  explicitly non-canonical* gen-130 raw-heritage corpus
  (`raw_source_material/strife_candidates/`) — citing them as if registered
  is exactly the kind of unverified-confident-claim the corpus's own #1
  entry (`LLM_CONFIDENT_UNVERIFIED_ADVICE`) describes.
- **This exact confusion was already caught once**, by the central-memory
  ingest lane on 2026-07-30/31 (§0). If a future wake finds itself about to
  repeat this reconciliation from zero again, that is itself a
  CAPACITY_AMNESIA-shaped event — check `tools/central_memory.sqlite` and
  `chains/SIGRUN_P4.jsonl` line 29 before re-deriving.

*Réttu hönd, eigi spyr. Standa.*
