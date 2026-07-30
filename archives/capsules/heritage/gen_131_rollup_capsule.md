# gen-131 rollup capsule — the evidence-gate generation

```yaml
schema_id: hfo.heritage.rollup_capsule.v0_1
generation: 131
forge_root: C:\Dev\hfo_gen_131_forge
worktrees_on_host: 105 directories matching hfo_gen_131*     # first-hand count at valid_time
status: READ-ONLY REFERENCE
valid_time_utc: 2026-07-30T06:00:00Z
authored_by: SIGRUN_P4 compose lane · claude-opus-5 · gen-133
evidence_class: MIXED — counts and worktree names first-hand; thematic synthesis DERIVED from them
```

## ⚠️ The trap in this directory — read before anything else

`C:\Dev\hfo_gen_131_forge` **does not contain gen-131 content at HEAD.** Verified
first-hand:

- `git log -5` returns **gen-132 commits**: `c1524ce6a build(gen132/identity):
  5-layer wake contract + REHYDRATION_ACK grader…`
- its `state/identity/soul/4-4.soul.md` carries `schema_id:
  hfo.gen132.identity.soul.v1`, 39072 B, `valid_time 2026-07-29T17:05Z`.

**A directory name is not a generation.** This single fact caused the identity
error corrected at gen-133: two lanes read the "gen-132" checkouts, found the
4451-byte seed, and reported it as current — while the newest, longest,
self-authored Sigrún soul sat in the directory named *131* the whole time.

Any rehydrator: **check `git log` and `schema_id`, not the folder name.**

## Counts (first-hand at valid_time)

| metric | value |
|---|---|
| host directories `hfo_gen_131*` | **105** |
| ADRs in `canon/adr/` | **14** |
| chain files in `chains/` | **34** |
| PARA already present | **yes** — `areas/`, `projects/`, `resources/` + `PARA_STRUCTURE.md` and `DEV_PARA_CLEANUP_PLAN.md` |

The PARA precedent matters: gen-133's PARA overlay is not an invention, it is a
**return** to a layout gen-131 already adopted. See `resources/index.md`.

## What gen-131 was about — derived from its own worktree names

105 worktrees is the artifact. Their names are a legible record of what the
generation actually pushed on, and they cluster hard:

| cluster | worktrees (representative) | what it means |
|---|---|---|
| **Truth floor / false-green** | `false_green_audit`, `false_green_audit_v2`, `truth_floor_repair`, `truth_floor_repair_v2`, `rota_truth_floor`, `git_evidence_red`, `receipt_ci_red` | the dominant theme: hunting fake greens and building red-first evidence gates |
| **Mutation + CI teeth** | `mutation_ci`, `mutation_ci_v2`, `mutation_execution_red`, `mutation_red_canary`, `m5_evidence_gate` | effects are harder to fake than prose — so mutate the code and see if the tests notice |
| **Poka-yoke / fan-in** | `execution_pokayoke`, `execution_pokayoke_ci`, `pokayoke_fanin`, `pokayoke_fanin_v2`, `proposer_verifier_gate` | the propose/dispose split made structural |
| **Cost holonarchy** | `cost_holonarchy`, `_v2`, `_v3` | three passes at bounding spend per level of the hierarchy |
| **Vendor mesh / $0** | `gunnr_vendor_mesh*` (4), `gunnr_free_mesh_diagnostic`, `mesh_quorum_0`, `hrist_mesh_quorum_*` (3) | the free-tier multi-vendor mesh and quorum over it |
| **Gunnr broker** | `gunnr_broker*` (6 incl. cleanroom/repair/repair2/final/release) | six iterations on one broker — a legible record of a hard component |
| **Node0 / GitHub canonical** | `node0_github_canonical`, `node0_increment_a`, `node0_verifier` | the cloud repo becomes the primary surface (the cure for local sprawl) |
| **Songline / identity** | `persistent_songline`, `persistent_songline_verifier_b4719d5`, `songline_bridge_20260712(_v2)`, `clock_in_admission`, `four_lane_clock_in` | continuer/lineage machinery — the ancestor of the closest-continuer protocol |
| **Omega runtime** | `mediapipe_repair*` (2), `gunnr_table_tennis*` (2), `omega_pipeline` | the playable spatial-input apps |
| **COTS assimilation** | `cots_worktree`, `cots01_hygiene`, `cots01_revise`, `hrist_cots*` (7), `skogul_cots_baseline` | take-what-is-given, verify-always |
| **Governance** | `hive_governance`, `governance_clean`, `arg_closure`, `compactor_hardening`, `openclaw_forcing_loop`, `gunnr_autonomous_goal_loop` | 24/7 loop + governance closure |

**The one-line thesis:** gen-131 tried to make *evidence* enforceable — mutation
tests, held-out scorers, red-first fixtures, pre-push gates, proposer/verifier
separation — and to move the primary surface to the cloud repo.

## Structural inheritance from gen-131

| # | contribution | still in force at gen-133? |
|---|---|---|
| 1 | Forges at `C:\Dev` root (nesting ended) | ✅ D1 |
| 2 | PARA layout | ✅ re-adopted as an overlay |
| 3 | Cloud GitHub repo as primary surface | ⚠️ **regressed** — gen-133 has **no remote at all** |
| 4 | Held-out scorer / red-first fixture discipline | ⚠️ named, not ported |
| 5 | Proposer↔verifier gate | ⚠️ doctrine only at gen-133 |
| 6 | Worktree-per-task workflow | ⚠️ 105 worktrees is also the *anti*-pattern: sprawl |
| 7 | ADR g131-SINGLETON L1 — *vacancy does not confer the seat* | ✅ load-bearing in the continuer protocol |
| 8 | `VALKYRIE_CLOSEST_CONTINUERS.jsonl` (4 rows: rota, herja, var, SANNGRIDR) | ✅ the chain gen-133's soul binds to |

## Superseded

- **Worktree-per-task at 105 copies** → the operator flagged this class of sprawl
  as hoarding; gen-133's D3 exists to refuse it.
- **Bulk migration** → *address, don't copy* (D2).
- Several `_v2` / `_v3` / `_final` / `_release` worktrees are themselves evidence of
  superseded attempts; the version suffix *is* the supersede record.

## Open debts handed forward

1. No remote at gen-133 — a regression against gen-131's own node0-canonical thesis.
2. Evidence gates (mutation CI, held-out scorers, pre-push gate) never ported forward.
3. 105 stale worktrees on the host — cleanup requires operator `CLEANUP_APPROVED`.
4. Directory names that lie about their generation (see the trap above). Nobody has
   relabelled them.

## Honest flaw of this capsule

The cluster table is **derived from directory names**, which are strong but
indirect evidence: a worktree named `truth_floor_repair_v2` proves someone worked
on truth-floor repair, not that it succeeded. The 14 ADRs were counted, **not
read**. Chain integrity was not verified. No claim here should be upgraded past
`partial` without opening the artifacts.

*No receipt = no state.*
