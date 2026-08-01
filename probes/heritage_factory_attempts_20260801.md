```yaml
# AIH2O capsule
doc: probes/heritage_factory_attempts_20260801.md
schema_id: hfo.gen133.probe.heritage_factory_attempts.v0_1
generation: 133
authored_by: HRIST valkyrie · sonnet-5 · silver-recovery/deep-dive
valid_time_utc:       2026-08-01T05:35:00Z
transaction_time_utc: 2026-08-01T05:35:00Z
timebox: 30min (hard)
feeds: Sigrún session local_b4579cd1
A_assumption: operator's factory/pipeline question is answerable by grepping for factory-class abstractions across C:/Dev, not by re-deriving strife/splendor
H_hypothesis: prior gens already built (not just specced) real MAP-Elites / adapter-registry / variant-multiplication machinery for spatial apps; the current 7-artifact gen-133 spec did not discover it
O_output: 6 chronological attempts, 1 reuse table (10 rows), 4 honest flaws
```

# HERITAGE PROBE — prior factory/pipeline attempts (2026-08-01)

## 0 · Answer up front

**Operator is closer than the 7 new specs imply.** Two prior gens (**gen-98**,
**gen-130**) already **shipped working code** for the exact primitives the
2026-08-01 spec pass (`spatial_factory_framework.v0_1.md` +
`logo_to_reskin_pipeline.v0_1.md` + `map_elites_portfolio_factory.v0_1.md` +
`adopt_before_reinvent_registry.v0_1.md` + `spatial_factory_evo_search.v0_1.md`
+ `plans/first_day_25_apps_pilot.md` + `plans/scale_25_to_100_per_day.md`)
proposes to build from scratch: a fitness-gated MAP-Elites archive, an
adapter-registry for input sources, a per-variant config schema (`brand.json`'s
direct ancestor), and 40 **real, on-disk, executed** reskin variants of one
game. **None of it ever reached a live deploy** — that gap (`deployed_url`
empty in all 50 gen-98 manifests) is the *same* gap the new spec names as
blocker **B1**. The registry pass that just ran (`adopt_before_reinvent_registry.v0_1.md`)
did not cite any of this — not because it doesn't exist, but (most likely)
because it sits outside the gen-133 forge root and the routing doctrine in
`C:\Dev\CLAUDE.md` does not surface it by default.

---

## 1 · Chronological attempts

### 1.1 · gen-98 `hfo_tile_factory` — the deepest prior attempt (2026-03)

`C:\Dev\hfo_dev_2026_3\hfo_gen_98_forge\archived_root\hfo_tile_factory\`

- **`registry.py`** — a real SQLite-backed MAP-Elites archive: `register_tile()`,
  `query_tiles()`, `TileFitnessError`, `FITNESS_GATE = 0.72` (hard-coded reject
  below gate, not advisory). Header quine claims "134/134 tiles above gate."
- **`adapters/`** — `mediapipe_adapter.ts`, `mediapipe_gesture_adapter.ts`,
  `spatial_os_adapter.ts`, `synthetic_adapter.ts`, `w3c_pointer_adapter.ts` —
  exactly the "one thin wrapper per input source" pattern the new spec asks for
  (framework §5 asks for it per *deploy host*; this is the same shape per
  *input source*).
- **`pipeline/`** — `signal_refinery_tile.ts`, `mediapipe_pipeline.ts`,
  `w3c_pointer_bridge_tile.ts` — a real, tested refinery
  (`tests/test_signal_refinery.py`, 187 lines: One-Euro + EMA + Passthrough,
  asserts `'hfo.gen98.omega.signal_refinery.v1'` schema ID, asserts
  `createMediaPipeRefinery` factory-adapter pattern exists in source, asserts
  no DOM access — pure-function discipline enforced by test).
- **`apps/manifests/`** — **50 real JSON files**, one per game
  (`game_2048.json`, `game_snake.json`, `game_tetris.json`, …), schema
  `hfo.gen98.app.<name>.v1`, fields: `source_url`, `license`,
  `input_primitive`, `wrapper_tier`, `wrangler_project`, `deployed_url`,
  `ssot_tile_id`, `pointer_adapter`. **This is `brand.json`'s direct ancestor.**
- **`apps/avalanche/`** — **40 real HTML files**, hand-built reskin/variant
  multiplications of one game across archetype-pair codenames
  (`a2r2_avalanche.html`, `a2s2_avalanche.html`, `a2w2_ammit_avalanche.html`,
  `b2r2_avalanche.html`, `d2s2_avalanche.html`, `d2s2_signal_forge.html`,
  `d2s2_spatial_os.html`) plus purpose variants
  (`brand_avalanche_onepager.html`, `c2p2_logo_physics_avalanche.html`,
  `avalanche_tradeshow.html`, `analytics_dashboard.html`). **This is the
  reskin-multiplication claim already proven technically possible, by hand,
  40 times over.**

**What shipped:** static files on disk, all 50 manifests, all 40 variant HTML
apps, a tested refinery tile, an adapter registry, a SQLite fitness-gated
archive.

**What killed it:** `grep deployed_url` across all 50 manifests → **every one
is empty**, `deployed_at: null` in the sampled file. **Zero of the 50 wrapped
games ever reached a live `wrangler_project` URL.** The factory built the
product line and never crossed the deploy gate — same failure mode the new
spec calls B1.

### 1.2 · gen-115 `HFO_Omega_Spatial_Input_Factory_Sigrun_Analysis_v0_2.md` — design doc, never shipped (~2026-05)

`C:\Dev\hfo_dev_2026_high_signal_silver_gold\hfo_gen_115_notes-...\hfo_gen_115\`

- Explicitly named **adopt-before-reinvent doctrine before the term existed**:
  *"custom tracker / custom smoothing algorithm if package works —
  explicitly flagged NOT-recommended (prefer COTS 1eurofilter over adhoc)"*
  (line 190) and shows a COTS-wrapping adapter pattern
  (`src/adapters/one-euro-adapter.ts`, line 511).
- Also specs inertial coasting (`createCoaster(maxMs)`, line 533) as "glue,
  not a physics engine" — same register as the new spec's restraint language.
- **This is the direct doctrinal ancestor of `adopt_before_reinvent_registry.v0_1.md`**,
  and the new registry does not cite it.
- **Never shipped as running code** — it is titled "Analysis," not a build
  receipt.

### 1.3 · gen-107 gesture-pointer-bridge — shipped smoothing code (~2026-05)

`C:\Dev\hfo_dev_2026_4_2\hfo_gen_107_forge\spatial_os_push\active\gesture-pointer-bridge\src\mosa\tiles\k2-filter-chain.ts`

- `N1EuroAutoTune` (line 105) — auto-tuning 1-Euro filter, real TypeScript,
  shipped. Feeds the same smoothing lineage `adopt_before_reinvent_registry.v0_1.md`
  row 13 credits to `signal_refinery.mjs` — correct call, third independent
  confirmation that 1-Euro is the right adopt.

### 1.4 · gen-130 `run_piano_mapelites.mjs` — a REAL MAP-Elites driver for THIS product line (2026-05-31)

`C:\Dev\gseed_20260610T0110Z\payload\hfo_tiles\tools\run_piano_mapelites.mjs`
(557 lines; identical/mirrored copy almost certainly also lives in the
gen-130 forge proper under `hfo_tiles/tools/`, per its own path-resolution
code expecting `FORGE_DIR = resolve(HFO_TILES_DIR, '..')`).

- Deterministic `mulberry32` RNG, seed `0x9e3779b9` — reproducible runs.
- Cell key = `authority_mode × filter_preset` (5 modes × 2 presets) — a real
  BC-tuple archive over **composition genomes** (not detectors/filters/physics
  — explicitly out of scope per its own header comment).
- Scores each genome by **replaying captured detector rows through the real
  refinery tile** (`finger_cursor_stream_pipeline_tile`) against an **operator
  fingertip oracle** — i.e. Oracle-A-shaped semantic scoring already existed
  for the piano product, 2 months before `spatial_factory_framework.v0_1.md`
  invented "Oracle A" as new.
- Honest guards in the header: fabricated fitness is refused; a missing golden
  fixture falls back to a clearly-named `SYNTHETIC_STUB`, flagged as not-real.
- Companion receipt `EMERGENCY_FORGE_TEST_SUITE_HARDENING_RECEIPT_20260603.md`
  records an actual run of the **v0.11 microkernel pipeline** over 201
  index-tip hand-frames: `rows_checked=201, green=true, red_first=true,
  shippable=false`. **`shippable=false` is load-bearing** — this is likely the
  same suite `SIGRUN_STAMP_LOGO_100APPS_20260801.md` GATE 0.2 asks to be run
  again (`run_hfopiano_v511x_golden_master_suite.mjs`), and its last known
  status was explicitly not-shippable.

**What shipped:** a working, deterministic QD driver against a real product
oracle. **What's unclear:** whether it was ever run past the founder-seeding
stage — no `work/breeding/piano_mapelites_v0_1/runs/` output was located in
this session's budget (see honest flaws).

### 1.5 · garmr_outreach_control (2026-07-09 receipts, folded 2026-07-28) — MAP-Elites *vocabulary*, wrong domain

`C:\Dev\garmr_outreach_control_20260728\work\valkyrie_prey_harness\receipts\goll_map_elites_rainbow_*.md`
and `work\scripts\kata_map_elites_registry.py`.

- "Goll's MAP-Elites Rainbow+" is an **LLM model-evaluation leaderboard**
  (28 models, 85 probes, HON/RWH/ADV/INS/GATE composite scores) — MAP-Elites
  terminology borrowed for **model tiering**, not product/app variant search.
- `kata_map_elites_registry.py` is a **selection-support tool for KATA.md
  learning packets** — groups by north-star × niche, promotes only on explicit
  packet flags. Its own docstring: *"This is selection support, not an
  optimizer."*
- **Neither is reusable code for a spatial-app factory** — different domain
  entirely. The **pattern** (archive + niche key + fitness-vector fields) is
  the only transferable part, and gen-98/gen-130 already have that pattern in
  the correct domain (§1.1, §1.4).

### 1.6 · gen-133 itself, 2026-08-01 ~04:48–05:08Z — the 7 factory-spec artifacts

`spatial_factory_framework.v0_1.md`, `logo_to_reskin_pipeline.v0_1.md`,
`map_elites_portfolio_factory.v0_1.md`, `adopt_before_reinvent_registry.v0_1.md`,
`spatial_factory_evo_search.v0_1.md`, `plans/first_day_25_apps_pilot.md`,
`plans/scale_25_to_100_per_day.md` (stamped together in
`inbox/olrun/SIGRUN_STAMP_LOGO_100APPS_20260801.md`).

- All authored by SIGRÚN P4 / opus-5, `ceiling=strategic`, **zero scripts/
  authored** (`code_authoring` gate denied 4× — blocker B3 in every document).
- `adopt_before_reinvent_registry.v0_1.md` ran its own adopt-before-reinvent
  pass and found **independent convergence** with a parallel lane
  (`swarm_pipeline_adoption_stack.v0_2.md`,
  `input_method_exemplars_adopt_before_reinvent.v0_1.md`, `local_a3fcb3a7`) on
  Cloudflare Pages, DSPy+GEPA, and the 1-Euro adopt — **but neither lane's
  registry mentions gen-98's `hfo_tile_factory`, gen-130's
  `run_piano_mapelites.mjs`, or gen-115's Omega analysis doc.**
- The registry's own row 1 proposes **pyribs** for MAP-Elites, with the caveat
  it "only earns its place once MU5 (continuous refine_config) unlocks" and
  "until then a dict keyed by BC-tuple is equivalent." **A dict keyed by
  BC-tuple, with a deterministic RNG and a real oracle, is exactly what
  gen-130 already built** (§1.4).

---

## 2 · Reuse table — what's proven code vs. build-from-scratch

| # | Component (named in the 2026-08-01 spec) | Prior-gen status | Verdict | Evidence (path:line) |
|---|---|---|---|---|
| 1 | MAP-Elites archive over skin genes | **Working driver exists** for this exact product (piano) — deterministic RNG, real BC-tuple cells, real oracle replay | **REUSE the pattern now; defer pyribs to MU5 as the registry itself already says** | `gseed_20260610T0110Z/payload/hfo_tiles/tools/run_piano_mapelites.mjs:1-80` |
| 2 | Fitness-gated archive storage | SQLite `registry.py`, hard `FITNESS_GATE=0.72`, `register_tile`/`query_tiles`/`TileFitnessError` | **REUSE** — schema and gate logic is directly portable to a `brand_id` archive | `hfo_gen_98_forge/archived_root/hfo_tile_factory/registry.py:1-60` |
| 3 | `brand.json` per-variant config schema | 50 real manifests: `wrapper_tier`, `pointer_adapter`, `wrangler_project`, `deployed_url`, `ssot_tile_id` | **REUSE as ancestor** — extend this schema, don't design from zero | `hfo_tile_factory/apps/manifests/game_2048.json:1-20` |
| 4 | Adapter registry (one wrapper per source/host) | `adapters/{mediapipe,w3c_pointer,spatial_os,synthetic}_adapter.ts` + factory-fn test | **REUSE pattern** — same shape the framework wants for deploy adapters (§5), already proven for input adapters | `tests/test_signal_refinery.py:179` (`createMediaPipeRefinery` factory-adapter assertion) |
| 5 | Reskin/variant multiplication (1 app → N brands) | 40 **real** HTML variants of one game, hand-built | **PARTIAL REUSE** — proves the multiplication is technically achievable; done by hand, not a byte-anchored patcher; **none shipped live** | `hfo_tile_factory/apps/avalanche/` (40 files, `ls` count) |
| 6 | Deploy pipeline (dist → live URL) | `wrangler_project` field present in all 50 manifests; `deployed_url` **empty in all 50** | **NOT REUSABLE — this is the still-open gap**, identical to the new spec's blocker B1 | grep `deployed_url` across `apps/manifests/*.json`, 50/50 empty |
| 7 | Golden-master / regression harness (Oracle A precursor) | Real replay-against-oracle scoring already built for hfopiano; a real 201-frame run recorded `shippable=false` | **REUSE candidate — but re-verify before trusting**; last known status was explicitly not-shippable | `EMERGENCY_FORGE_TEST_SUITE_HARDENING_RECEIPT_20260603.md:19` |
| 8 | 1-Euro / smoothing adapter | Three independent shipped implementations (gen-98 tested, gen-107 auto-tune, gen-115 COTS-wrap doc) | **REUSE — already triple-confirmed correct**, registry row 13 got this right | `k2-filter-chain.ts:105`; `test_signal_refinery.py:6` |
| 9 | Adopt-before-reinvent doctrine itself | gen-115 stated the identical principle 3 months earlier ("prefer COTS 1eurofilter over adhoc") | **REUSE — this doc is the uncited doctrinal parent** of `adopt_before_reinvent_registry.v0_1.md` | `HFO_Omega_Spatial_Input_Factory_Sigrun_Analysis_v0_2.md:190` |
| 10 | MAP-Elites vocabulary for non-product selection (model eval, kata packets) | `goll_map_elites_rainbow_*` (LLM leaderboard), `kata_map_elites_registry.py` (packet selection) | **DO NOT REUSE code** — wrong domain; only the archive+niche+fitness-vector *shape* transfers, and rows 1–2 above already have that shape in the right domain | `kata_map_elites_registry.py:26-38` |

---

## 3 · Honest flaw

1. **Time-boxed at 30 minutes; did not open** `apps/spatial_os/`,
   `apps/wrappers/`, or the broader `omega_games` 50-title library separately
   from `hfo_tile_factory/apps/manifests` — they may overlap or be the same
   corpus under two names; not confirmed either way.
2. **Never executed anything.** Every claim above is static-file / grep
   evidence (`[D]` disk-probe grade in the forge's own evidence key), not a
   runtime observation. `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN` applies to
   this whole probe as much as to the specs it's evaluating.
3. **"The current spec pass didn't discover this" is stated as fact but the
   cause is unconfirmed.** gen-98 and gen-130 live outside
   `C:\Dev\hfo_gen_133_forge`, and per `C:\Dev\CLAUDE.md` routing doctrine,
   cross-gen heritage mining is a deliberate, separate pass — not something
   the spec-authoring session would do by default. This may be an
   access-boundary/routing gap, not a diligence failure by SIGRÚN P4.
4. **Did not confirm whether `run_piano_mapelites.mjs` was ever run past
   founder-seeding** — no `work/breeding/piano_mapelites_v0_1/runs/` output was
   located under the `gseed_20260610T0110Z` mirror within budget; the gen-130
   forge proper (`hfo_dev_2026_5_30/hfo_gen_130_forge/work/breeding/`) was not
   separately checked.

*Réttu hönd, eigi spyr. Standa.*
