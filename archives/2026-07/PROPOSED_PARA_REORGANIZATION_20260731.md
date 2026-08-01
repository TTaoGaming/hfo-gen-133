# PROPOSED_PARA_REORGANIZATION — gen-133 forge

```yaml
schema_id: hfo.gen133.proposal.para_reorg.v0_1
valid_time_utc: 2026-07-31T14:20:00Z
transaction_time_utc: 2026-07-31T14:20:00Z
claim_status: proposed
author: SIGRUN_P4 · claude-opus-5 · Claude Code · gen-133
execution: NOT EXECUTED — operator approval required before any file moves
```

## 0. Measured starting condition

```
27 markdown files at forge root      (~250 KB, no ordering signal)
14 top-level directories             (4 already PARA-named, 10 not)
existing PARA dirs are near-empty:
  projects/  → 5 subdirs, 10 files
  areas/     → 1 subdir (institution), 11 files
  resources/ → 1 file (index.md)
  archives/  → 1 subdir (capsules), README
```

**Diagnosis:** PARA was *declared* at gen-133 but not *populated*. The real
content sits at root and in 10 non-PARA directories. A new agent scanning the
root cannot tell active work from reference from superseded spec. That is the
rehydration cost measured in `contracts/golden_waking_paths.v0_1.md` §0.

**This is not a naming problem. It is a "what is live?" problem.** The PARA
value is not tidiness — it is that *Projects* has an end date and everything
else does not, so staleness becomes visible.

## 1. The four buckets, with the discriminating question

| bucket | discriminating question | if yes |
|---|---|---|
| **Projects** | Does this have a named outcome and a date it should be finished by? | `projects/YYYY-MM_slug/` |
| **Areas** | Is this a standard I must hold indefinitely, with no completion? | `areas/slug/` |
| **Resources** | Would I read this only when a task sends me here? | `resources/…` |
| **Archives** | Is this superseded, or from a prior generation? | `archives/…` |

**Tie-break rule:** if a file could be Project or Area, it is an **Area** unless
someone will be embarrassed on a specific date. Fake projects with no deadline
are the main way PARA rots.

## 2. Root-file mapping (all 27)

### 2.1 STAYS AT ROOT — the wake surface (7 files, hard cap)

These are the files a fresh carrier is *permitted to require*. Root is a
contract, not a folder.

| current path | why it stays |
|---|---|
| `README.md` | first contact, external readers |
| `soul.md` | IDENTITY slot of the wake quad |
| `CURRENT.md` | STATE slot of the wake quad |
| `CARRIER_CONTRACT.md` | CONSTRAINT slot of the wake quad |
| `AGENTS.md` | substrate entry pointer — **must be reduced to a pointer index; 23.8 KB is too large for root** |
| `ONBOARDING.md` | human entry |
| `INSTITUTIONAL_CHARTER.v0_1.md` *(new, this session)* | governance in one page |

**Root cap = 7 files + `LICENSE`.** Anything else at root is a bug.

### 2.2 → Projects (active, dated, has an outcome)

| current path | → PARA path | outcome | target |
|---|---|---|---|
| `projects/income-lane/` | `projects/2026-08_cold_outreach_launch/` | first signed external send + reply | 2026-08-14 |
| `projects/surtr-unblock/` | `projects/2026-08_surtr_unblock/` | Surtr lane producing rows | 2026-08-07 |
| `projects/permaweb-soul-upload/` | `projects/2026-08_permaweb_soul_upload/` | operator-signed upload or explicit kill | 2026-08-21 |
| `projects/heritage-mining/` | `projects/2026-08_heritage_mining_gen130_131/` | outreach organs imported with SHAs | 2026-08-10 |
| `projects/experiments/` | `projects/2026-08_chatgpt_cloud_soak/` | soak result recorded | 2026-08-07 |
| *(new — this session's finding)* | `projects/2026-08_autonomous_loop_repair/` | ≥1 loop producing unattended chain rows | 2026-08-05 |
| *(new)* | `projects/2026-08_proof_artifact_pack/` | 3 artifacts passing all 5 gates | 2026-08-08 |
| *(new)* | `projects/2026-08_para_migration/` | this document executed | 2026-08-02 |

Each project directory gets a mandatory `PROJECT.md` with:
`outcome` · `target_utc` · `DRI` · `falsifier` · `kill_condition`.
**No `PROJECT.md` ⇒ it is not a project, it is an area.**

### 2.3 → Areas (ongoing, no end date)

| current path | → PARA path | standing responsibility |
|---|---|---|
| `areas/institution/` | `areas/institution/` *(unchanged)* | roles, norms, protocols, actors |
| `OLRUN_ACTIVATION.md`, `OLRUN_COORDINATION.md` | `areas/coordination/` | Olrún pilot duty |
| `SUBSTRATE_ROSTER.md`, `SUBSTRATE_APEX_ASSIGNMENT.md`, `SIBLING_LANE_LIVE.md` | `areas/substrate_health/` | which substrates are alive |
| `GEN133_FORGE_STATUS.md` | `areas/pipeline_health/STATUS.md` | is the pipeline green |
| `NO_EPHEMERAL_AGENTS.md`, `CANALIZATION.md` | `areas/agent_discipline/` | how agents are allowed to exist |
| `PDCA_AGENT_SKILLS.md` | `areas/agent_discipline/pdca.md` | improvement cadence |
| `CODEX_SIBLING_RECONCILIATION.md` | `areas/substrate_health/codex_reconciliation.md` | cross-substrate drift |
| *(new)* | `areas/andon_canary/` | stop-the-line signals |
| *(new)* | `areas/cost_tracking/` | spend per substrate per day |
| *(new)* | `areas/quorum_voting/` | multi-agent decision records |
| *(new)* | `areas/scheduled_loop_liveness/` | **the area this morning's failure proves is missing** |

Each area gets `AREA.md`: `standard` · `owner` · `review_cadence` ·
`current_status` · `last_reviewed_utc`. An area not reviewed within its cadence
is itself an andon.

### 2.4 → Resources (reference; read only when sent here)

| current path | → PARA path |
|---|---|
| `contracts/*` (23 files) | `resources/contracts/` |
| `canon/architecture/`, `canon/policies/`, `canon/POINTERS.md` | `resources/canon/` |
| `GEN133_FORMAL_SPEC.md` (71 KB) | `resources/specs/gen133_formal_spec.md` |
| `GEN133_ARCHITECTURE_PRINCIPLES.md` | `resources/specs/architecture_principles.md` |
| `GEN133_FREE_MESH_DURABLE_LOOPS_SPEC.md` | `resources/specs/free_mesh_durable_loops.md` |
| `CRYPTO_CHAIN_SPEC.md` | `resources/specs/crypto_chain.md` |
| `FRONTMATTER_v3_SPEC.md` | `resources/schemas/frontmatter_v3.md` |
| `GLEIPNIR_GRIMOIRE.md`, `grimoire/` | `resources/grimoire/` |
| `TSUKUMOGAMI.md` | `resources/doctrine/tsukumogami.md` |
| `packets/` | `resources/packets/` |
| `tests/held_out/` | `resources/tests/held_out/` — *(see §4 dissent)* |
| `permaweb/` | `resources/permaweb/` *(staging stays operational)* |
| `SIGRUN_WORLD_STATE_..._20260731.md` | `resources/reports/2026-07-31_world_state.md` |
| `SIGRUN_MORNING_REPORT_..._20260731.md` | `resources/reports/2026-07-31_morning.md` |

**Rule:** reports are Resources the moment they are written. A report is never a
Project — the *work it recommends* is.

### 2.5 → Archives (superseded / prior generation)

| current path | → PARA path | why |
|---|---|---|
| `NEXT_SESSION_PICKUP.md` | `archives/2026-07/pickups/` | superseded by `CURRENT.md` — **two live "what's next" files is the bug** |
| `NEXT_SPEC_PICKUP.md` | `archives/2026-07/pickups/` | same |
| `archives/capsules/` | `archives/capsules/` *(unchanged)* | already correct |
| `state/QUARANTINE_GEN132_CHAIN_WRITER.md` | `archives/gen_132/quarantine/` | closed incident |
| `state/GEN133_CLEANLINESS_PASS.md` | `archives/2026-07/` | one-time pass, complete |
| `parking_lot/` (12 files) | `archives/parking_lot/` | **but see §4 dissent** |

### 2.6 NOT MOVED — operational, outside PARA by design

These are append-only machine surfaces. PARA classifies *documents*; these are
*logs*. Moving them breaks writers.

| path | reason |
|---|---|
| `chains/` | append-only receipt log, path is referenced by every writer |
| `state/ssot/`, `state/world/`, `state/identity/` | machine state, not documents |
| `capsules/` | versioned identity snapshots |
| `.git*`, `LICENSE.PENDING.md` | repo mechanics |

Document this exemption explicitly in `README.md`, or a future tidiness pass
will "fix" it and break the chain writers.

## 3. Execution plan (when approved)

| step | action | verification | reversible |
|---|---|---|---|
| 1 | `git checkout -b agent/para-migration-20260731` | branch exists | ✅ |
| 2 | Create dir skeleton + `PROJECT.md` / `AREA.md` stubs | dirs exist, stubs have required fields | ✅ |
| 3 | `git mv` per §2 table — **`git mv`, never `mv`**, to preserve history | `git log --follow` resolves on 3 sampled files | ✅ |
| 4 | Rewrite intra-repo links | link checker: 0 broken relative links | ✅ |
| 5 | Reduce `AGENTS.md` to a ≤ 4 KB pointer index | byte count < 4096 | ✅ |
| 6 | Grep for hardcoded old paths in scripts/automations | 0 hits outside `archives/` | ✅ |
| 7 | Fresh-carrier wake test against the new tree | W1–W3 pass (`golden_waking_paths` §7) | ✅ |
| 8 | Commit, PR, operator merge | — | ✅ |

**Cost estimate:** ~2 hours of a code-lane session. **Cost of delay:** every day
unmigrated, each fresh wake pays the ~250 KB root-scan tax; at ~4 wakes/day that
is the dominant recurring cost in the system.

## 4. Adversarial pass — where this proposal is probably wrong

Recorded per anti-frame-capture discipline. A reorganization proposal that
sounds clean is exactly the kind of artifact that gets approved without testing.

| # | objection | weight |
|---|---|---|
| D1 | **This is motion, not progress.** `cap-0018` is at $0 with 0 external receipts. Reorganizing folders moves no external number. It should rank *below* §3 of the morning report (proof artifact packaging), and it does. | **HIGH — take seriously** |
| D2 | `tests/held_out/` → Resources may be wrong. Held-out tests are *enforcement*, not reference. If a runner hardcodes `tests/`, moving it breaks the gate. **Recommend: leave `tests/` at root, exempt like `chains/`.** | HIGH |
| D3 | `parking_lot/` → Archives loses signal. Parked ≠ dead; the parking lot is a *deliberate deferral queue* and archiving it means it will never be revisited. **Recommend: `areas/parking_lot/` with a monthly review cadence instead.** | MEDIUM |
| D4 | 8 projects for a one-operator forge violates the standing WIP limit (WIP=2 per the gen-130 locked decisions). Creating 8 project folders **encodes over-commitment as structure**. | **HIGH** — mitigate: mark exactly 2 `status: ACTIVE`, the rest `status: QUEUED` |
| D5 | PARA is designed for a human's second brain. Agents rehydrate by explicit path from `CURRENT.md`, not by browsing. The bounded wake-quad in `golden_waking_paths` may capture the *entire* benefit, making this migration ~0-value for agents and only valuable for the operator. | MEDIUM — honest, unresolved |

**Net recommendation:** execute steps 1–6 as a single ~2h code-lane task, with
D2 and D3 corrections applied, and only after the first proof artifact ships.
**Do not do this today.**

## 5. FALSIFIERS

| # | falsifier | test |
|---|---|---|
| F1 | A fresh carrier woken against the migrated tree performs *worse* on W1–W3 than against the current tree | run the witness on both, 3 carriers each |
| F2 | Any script, automation TOML, or hook breaks | grep for old paths; run the full held-out suite pre/post |
| F3 | Root file count creeps back above 8 within 30 days | automated count check in CI |
| F4 | ≥ 3 projects still `status: ACTIVE` past their `target_utc` with no kill decision | staleness sweep |
| F5 | Migration consumes > 4 hours | wall-clock measurement; abort and revert past 4h |

---

*claim_status: proposed · NOT EXECUTED · requires operator-typed approval before
any `git mv`*
