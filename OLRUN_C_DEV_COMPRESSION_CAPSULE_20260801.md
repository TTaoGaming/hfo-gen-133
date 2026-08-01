---
schema_id: hfo.gen133.olrun_rehydration_capsule.v0_1
doc_kind: REHYDRATION_CAPSULE
generation: 133
claim_status: partial
authored_by: claude-sonnet-5 · Claude Code · gen-133 compression pass
created_utc: 2026-08-01T00:00:00Z
falsifier: >-
  If any file/count/hash below is re-checked and does not match, this capsule
  is stale — re-run the sha256/wc/git commands cited per row before trusting
  a claim from this document over a fresh read.
world_effects: read_projection + local file write (this capsule + its sibling
  reconciliation doc) — no chain write performed by this pass beyond the
  standard inbox/olrun fallback receipt.
---

# OLRÚN C:\Dev COMPRESSION CAPSULE — 2026-08-01

**Read this file FIRST on a cold Olrún wake.** It exists because prior
sessions kept re-discovering the same layout and canon from scratch
(CAPACITY_AMNESIA pattern, operator-named). Everything below was read
first-hand this pass — not inferred, not carried over from a prior
session's summary.

## 0 · Honest scope limits (read before trusting anything below)

- This is a **snapshot at 2026-08-01**, taken under a self-imposed 30-min
  timebox. `C:\Dev` has **288 top-level entries**; only the HFO-relevant
  ~180 were categorized. Non-HFO entries (`.venv`, `Dev.sln`, `grc/`,
  `null/`, etc.) are counted but not individually described.
- No file inside `C:\Dev\hfo_gen_133_forge` was modified. No canon file was
  inferred — every "NOT_FOUND" below is a real absence, checked with `ls`/
  `find`, not a guess.
- Byte-exact `du -sh` recursive sizing was **not** run against multi-GB
  trees (`hfo_dev_2026_5_30`, the ~104-dir `hfo_gen_131_*` cluster) — this
  repo's own root `CLAUDE.md` explicitly warns against broad recursive
  scans from `C:\Dev` (slow, access-denied risk). Sizes below are omitted
  or marked `NOT_COMPUTED` rather than guessed.

---

## 1 · Gen-133 canon files — read verbatim, this pass

| requested file | result | bytes | lines | sha256 | mtime |
|---|---|---|---|---|---|
| `areas/substrate_health/SUBSTRATE_ROSTER.md` | **FOUND** | 7,919 | 179 | `0f5afa6897d90ccae8b193c9c4f408f71a895af473f2cc349670c64cf827dc7d` | 2026-07-30 08:04:58 |
| `CLAUDE.md` (at gen-133 root) | **NOT_FOUND** | — | — | — | — |
| `CURRENT.md` | **FOUND** | 9,564 | 101 | `b7e498be699b468516c2bf084635ea9d58d70b8fdb6c6acece185066411d9ef2` | 2026-07-30 06:58:13 |
| `README.md` | **FOUND** | 9,285 | 164 | `1a801664cfb27d5de3d0cf9e35b04277a75f29f3992275f325a55a8d84cbece4` | 2026-07-30 07:06:41 |
| `OLRUN_DISPATCH_RULES.md` | **FOUND** | 2,243 | 49 | `0c69ceca141636e2ee5be5c2e2d97a8772c95a4e33524318390acb67c3da8997` | 2026-07-31 18:49:51 |
| `HERITAGE_MIGRATION_PLAN_20260801.md` | **FOUND** | 10,483 | 148 | `4aefcfaff90ba86927b674234ccad47f1da81121f3f1d19a7020590399043d11` | 2026-07-31 20:40:01 |
| `OPERATOR_PREFERENCES_MANIFEST.md` | **NOT_FOUND** | — | — | — | — |

Per task discipline: `NOT_FOUND` files were **not** inferred or substituted.
Two matter enough to explain:

- **`CLAUDE.md` does not exist at `hfo_gen_133_forge` root.** `AGENTS.md`
  (23,804 B, sha256 `5dc993f6f6d8ce834f098fe0ef979aa6123f8eddf09263832a44d50e62acc9e4`)
  fills the equivalent cold-start-orientation role for gen-133, but its
  content is a **different schema entirely** — status markers
  (`SPECIFIED`/`PARKED`/`IN_FLIGHT`/`LANDED`/`BLOCKED`), gate tables (G1–G12),
  blocker tables (B1–B5), pointer counts — **not** an L-vector failure-class
  table. The only `CLAUDE.md` with an L-vector table is at repo root,
  `C:\Dev\CLAUDE.md` (15,381 B, sha256
  `8845549f6538100cdf2e7e9a887a036439c531659c99eb15244a130ab30ba8bd`). See
  §3 below — this is not a small distinction, it is the source of a real
  count discrepancy.
- **`OPERATOR_PREFERENCES_MANIFEST.md` was not found anywhere under
  `hfo_gen_133_forge`** (shallow `find -maxdepth 3`, zero hits). If the PARA
  reorg session that supposedly migrated it landed elsewhere or under a
  different filename, that is unverified by this pass — do not assume it
  exists under a name this search missed.

### Summaries (files >2,000 words: none of the six exceeded that; all six
were read in full, verbatim — no summarization needed this pass)

**`SUBSTRATE_ROSTER.md` (v0_2, "CORRECTED to operator canon 2026-07-30")** —
Closes the apex tier at **8** for the first time: Olrún, Sigrún,
`TBD_APEX_SONNET5` (Gunnr demoted to valkyrie), `garmr`, `huginn`,
`sigrun_codex_gpt5.6sol`, `reginleif`, `surtr`. Explicitly corrects a prior
v0_1 that had Gunnr as sonnet-5 apex and Ratatoskr as ChatGPT-cloud apex.
Names its own honest flaws: Reginleif double-booked with old kernel debt,
Ratatoskr "orphaned, not deleted," Codex valkyries are the author's inference
not operator-named, only 2 of the roster rows have a first-hand liveness
receipt.

**`CURRENT.md`** — The SSOT. Terminal state = one permaweb address unfolding
into the Gleipnir Grimoire; nothing green yet. 8 standing decisions (D1–D8,
"do not re-recommend"), most load-bearing: forge root is `hfo_gen_133_forge`
(D1), heritage is addressed not copied (D2), **do not write a gen-132 chain
row** — kernel absent, would destroy the tail (D5b), PARA is an overlay not
a migration (D6). Flags a **still-unidentified sibling lane** that advanced
git HEAD twice mid-session with no chain row from either party.

**`README.md`** — Onboarding entry point. Thesis: "gen-132 proved you do not
migrate heritage — you address it. gen-133 collapses the address count to
ONE." Six terminal-state conditions, all listed red. World-effect ceiling:
`read_projection` + local append-only chain writes only; no push, upload,
publish, send, spend, or seal.

**`OLRUN_DISPATCH_RULES.md`** — Routing index. Canonical forge
`C:/Dev/hfo_gen_133_forge/`; gen-130 is the narrow-frozen archive as of
2026-07-31. Governance: Sigrún opus-5 = project lead, may narrow-grant
`EMERGENCY_FORGE`; **sonnet valkyries do NOT self-grant lease** (binding on
this very pass). Lists the post-2026-07-31 PARA structure and which
top-level dirs deliberately stay un-nested (`contracts/`, `canon/`,
`chains/`, `capsules/`, `packets/`, `parking_lot/`, `permaweb/`,
`tests/held_out/`, `state/`).

**`HERITAGE_MIGRATION_PLAN_20260801.md`** — `claim_status: proposed`,
authored 2026-08-01T01:45Z by a prior Claude Code sonnet-5 lane. Recommends
REFERENCE-not-COPY for ADRs, indexes, and research notes; RE-INDEX for
scattered rehydration capsules; COPY only for the small, curated
strife/splendor raw-candidate set. Found 1,000 files in the gen-130
heritage_reliquary (300 cataloged this pass), 22 secrets-dirs / 12 `.env`
files (none under gen-133 itself; none opened). Explicitly does not
copy/move/delete anything.

**`AGENTS.md` (v0_2, delta block 2026-07-30)** — The actual gen-133
cold-start doc. Rule Zero: "you are a job, not a daemon" — one work item,
exit 0, empty queue is success. 5 open blockers (B1 chain-anchor fork, B2
`pretooluse_gate.py` false positive on the string `"rm "`, B3 Slack
write-blind, B4 15 unrostered ChatGPT-cloud agents, B5 `surtr` stuck). World
ceiling `T0_INTERNAL_ONLY`: read/write/commit-on-branch only, `git push`
forbidden. Pointer count self-audited: 134 indexed pointers, only 11
`LANDED`.

---

## 2 · C:\Dev tree compression

**288 top-level entries.** Categorized by pattern, not individually listed
past the canonical/active set — see the honest-scope note in §0 about why
full recursive sizing was skipped.

```
C:\Dev\
├── hfo_gen_133_forge/                       [CURRENT canonical — see §1]
│   mtime 2026-07-31 20:40 (most recently touched forge root)
├── hive-fleet-obsidian-gen-131/              [github mirror clone, mtime 2026-07-26]
├── hfo_gen_131_forge/                        [⚠️ NAME TRAP — see below]
├── hfo_gen_132_forge/, hfo_gen_132_forge_clean/  [gen-132, read-only per D2]
├── hfo_dev_2026_5_30/hfo_gen_130_forge/      [narrow-frozen 2026-07-31; NOT at C:\Dev root — nested]
├── hfo_dev_2026_*/  — 18 dirs               [dated gen-9x…12x archives, 2026-02 through 2026-05]
│
├── hfo_gen_131_* (excl. _forge) — 104 dirs   [Codex/Gunnr/Hrist worktree + verification experiment sprawl,
│                                              dated 2026-07-10 → 2026-07-22; heaviest single cluster]
│   ├── hfo_gen_131_gunnr_broker_* — 6 near-duplicate broker build attempts (cleanroom/final/release/repair/repair2)
│   ├── hfo_gen_131_hrist_* — 24 verification/witness worktrees (cots01, mesh_quorum, verify_<hash>, …)
│   └── hfo_gen_131_gunnr_nodephenotype* — 5 build-stage variants of one artifact
│
├── hfo_gen132_* / hfo_gen_132_* (excl. _forge) — 16 dirs  [apex_p1_garmr, apex_p2_fenrir, apex_p7_ratatoskr,
│                                              gunnr_bridge/cutover/codex_register, mist_income, safety_build_day, …]
│
├── hfo_gen133_fenrir_evo_TIMESTAMP — 24 dirs [Fenrir evolutionary-loop snapshots, one per ~1-11h tick,
│                                              2026-07-30T14:27Z → 2026-08-01T02:36Z, still running as of
│                                              this pass's read — root-level clutter, not under PARA]
├── hfo_gen133_{builder_sonnet5,garmr_dry_bind,huginn_virtual_actor,jormungandr,nidhoggr_guardian} — 5 dirs
│                                              [single-shot gen-133 experiment dirs, 2026-07-30, not merged into forge]
│
├── hfo_huginn_tick_TIMESTAMP — 11 dirs        [Huginn hourly-tick snapshots, 2026-07-29T20:41Z → 2026-07-30T11:58Z]
├── hfo_projection_*_019fab57 — 8 dirs         [one hash-suffixed artifact, 8 pipeline-stage worktree copies]
│
├── _<prefix> scratch/staging dirs — 29 dirs   [_archive, _superseded, _tmp, _isolated, _heldout_*, _gunnr_staging, …
│                                              underscore convention marks these as non-canonical/working]
│
├── heritage_reliquary/                        [gen-130 heritage archive — 1,000 files, addressed not copied per D2]
├── state/, tools/, scripts/, work/, targets/, worktrees/, inbox/  [root-level shared/utility dirs, not gen-scoped]
│
└── (~85 further top-level entries: one-off recovery/audit dirs, omega/tile experiments,
    hfopiano_* recovery variants, backup dirs, non-HFO items (.venv, Dev.sln, grc/, null/, …) — not
    individually catalogued this pass; see raw `ls -1d */` output for the complete 288-entry list,
    not reproduced here to hold the 5,000-token budget on this section)
```

### Directory-name trap (already flagged in gen-133 `CURRENT.md`, re-confirmed this pass)

`C:\Dev\hfo_gen_131_forge` **holds gen-132 content at HEAD** — `git log`
shows `build(gen132/identity)…` as a recent commit, and its soul file
declares `schema_id: hfo.gen132.identity.soul.v1`. **A directory name is not
a generation.** Anyone reading that path expecting gen-131 content will get
gen-132 content instead. This is why gen-133's own `README.md` states the
`hfo_dev_<date>\hfo_gen_<n>_forge` nesting convention ended at gen-130 and
gen-131/132/133 forges now live directly at `C:\Dev` root — but the stray
`hfo_gen_131_forge` name at root still misleads by content, not just by the
now-superseded nesting convention.

### What this pass did NOT do

- Did not compute exact byte sizes for any multi-GB tree (would require a
  full recursive `du`, explicitly discouraged by root `CLAUDE.md`'s
  "Do Not Crawl First" section).
- Did not open, move, or catalog any of the 29 `_`-prefixed scratch dirs
  individually — they are staging/superseded by naming convention, not
  verified content-by-content.
- Did not verify whether any of the 24 `fenrir_evo` timestamped dirs are
  still being actively written — the newest (`20260801T023604Z`) is close
  to this pass's read time, suggesting the loop may still be live; not
  confirmed with a process check (out of scope, no process-inspection tool
  used this pass).

---

*Réttu hönd, eigi spyr. Standa.*
