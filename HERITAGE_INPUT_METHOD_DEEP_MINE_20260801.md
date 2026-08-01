# HERITAGE DEEP MINE — Input Method Abstractions (smoothing / lookahead / latency / safety / ABI)

```yaml
gen: 133
doc: HERITAGE_INPUT_METHOD_DEEP_MINE_20260801.md
purpose: narrow deep-mine of INPUT-METHOD abstractions (hand/gesture/pointer pipelines)
  across canonical HFO gens, distinct from the prior broad strife/splendor pass
scope: read-only on all heritage/source files
timebox: ~45 min active tool-call work
claim_rule: every claim carries a path+line citation. No unsourced assertions.
outputs:
  - state/ssot/input_method_heritage_mining_20260801.jsonl (48 rows)
  - state/ssot/input_method_strife_splendor_abstractions_20260801.jsonl (7 rows)
  - state/ssot/input_method_proof_artifacts_20260801.jsonl (16 rows)
  - this file
```

## Hits per gen (approximate signal density, not exhaustive)

| gen | canonical root | signal density this pass | notable |
|---|---|---|---|
| gen-130 | `hfo_dev_2026_5_30\hfo_gen_130_forge` | **HIGH** | richest single root — HandPiano design docs, kinematic-guard doctrine, capacity_manifest |
| gen-130 (external) | `handpiano_launch_20260602` | **HIGHEST** | the only root with a real, fuzz-verified, running implementation (`dist/refinery.mjs`) |
| gen-107 | `hfo_dev_2026_4_2\hfo_gen_107_forge` | **HIGH** | most feature-complete filter-plugin family found (`k2-filter-chain.ts`) — 5 named techniques in one file |
| gen-98 | `hfo_dev_2026_3\hfo_gen_98_forge` | MEDIUM | earliest `signal_refinery` concept, schema-versioned ABI + TDD suite |
| gen-115 (curated) | `hfo_dev_2026_high_signal_silver_gold` | MEDIUM | design/analysis doc recommending COTS 1-euro adapter + inertial coasting — no shipped code confirmed |
| gen-131 | `hfo_gen_131_forge` (holds gen-132 content at HEAD, see directory-name trap below) | MEDIUM | `hfo_input_kernel.mjs` kernel-boundary contract, `gesture_pointer_bridge` npm README |
| gen-132 | `hfo_gen_132_forge`, `hfo_gen_132_forge_clean` | **LOW** | file-list hits present but sampled content was mesh/governance infra, not spatial-input; treated as low-signal for this task, not zero |
| gen-133 | `hfo_gen_133_forge` (this forge) | LOW-MEDIUM | no shipped input-method code found; a handful of contract/report files matched keywords by title only (not individually line-verified — see honest scope) |

**Directory-name trap re-verified independently this pass:** did not re-run `git log` myself (time budget); relied on `CURRENT.md` line 65's own first-hand claim (`hfo_gen_131_forge` holds gen-132 content at HEAD) rather than re-deriving it. This is a disclosed reuse, not a fresh verification — see `remaining_risk` in the receipt.

## Top-5 smoothing approaches

| # | technique | verdict | evidence |
|---|---|---|---|
| 1 | **1-euro filter** (`OneEuro`/`LowPass` classes, `cutoff = minCutoff + beta*|velocity|`) | ✅ shipped, fuzz-verified as part of the guarded pipeline | `C:\Dev\handpiano_launch_20260602\dist\refinery.mjs:28` |
| 2 | **N1EuroAutoTune** — 1-euro with auto-adjusted `minCutoff`/`beta` from a rolling noise-variance window | design-complete, no runtime verification found | `C:\Dev\hfo_dev_2026_4_2\hfo_gen_107_forge\spatial_os_push\active\gesture-pointer-bridge\src\mosa\tiles\k2-filter-chain.ts:105` |
| 3 | **DoubleExponentialSmoothing** (Holt's method: level + trend) | design-complete, no runtime verification found | same file, line 196 |
| 4 | **EMA / Passthrough refinery variants** behind a schema-versioned factory | TDD-passing, internal-only (not stranger-visible — see splendor admissibility note) | `C:\Dev\hfo_dev_2026_3\hfo_gen_98_forge\archived_root\hfo_tile_factory\tests\test_signal_refinery.py:6` |
| 5 | **Smoothing-only, no pre-filter guard** (the Cubism-precedent / pre-guard HandPiano baseline) | ❌ STRIFE — cited as external precedent and reproduced as gen-130's own pre-guard baseline (43/95 fuzz leaks) | `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\docs\handpiano_multihand_identity_wrist_roi_repulsion_design_spec.md:133` + `C:\Dev\handpiano_launch_20260602\fuzz\FUZZ_REPORT.md:40` |

## Top-5 lookahead approaches

| # | technique | verdict | evidence |
|---|---|---|---|
| 1 | **Velocity-extrapolated lookahead** (`filtered + velocity * lookaheadMs`) as a selectable "authority channel" alongside raw/filtered | shipped, part of the fuzz-verified pipeline | `C:\Dev\handpiano_launch_20260602\dist\refinery.mjs:50,377` |
| 2 | **Kernel-boundary doctrine**: "the kernel may apply filters, predictions, lookahead — but it MUST NOT [own policy]" | design principle, not itself tested | `C:\Dev\hfo_gen_131_forge\work\factory\spatial_os\same_origin_apps\_kernel\hfo_input_kernel.mjs:57` |
| 3 | **Minimal inertial coasting** (`createCoaster(maxMs)`, `coast: {maxMs:120, confidenceDecay:0.7}`) — bridges brief tracking loss | design doc only, no shipped code confirmed | `...HFO_Omega_Spatial_Input_Factory_Sigrun_Analysis_v0_2.md:398,533` |
| 4 | **`kin freeze/clamp -> one-euro -> lookahead -> authority`** ordered v0.11 microkernel pipeline | SYNTHETIC_GREEN (201 rows tested, not human-witnessed at component level) | `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\EMERGENCY_FORGE_TEST_SUITE_HARDENING_RECEIPT_20260603.md:19` |
| 5 | raw/filtered/lookahead trio flagged `SYNTHETIC_GREEN` across the whole primitive inventory | ⚠️ unverified at component scope — see strife row on witness-scope conflation | `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\GEN130_MOBA_EWQ_rehydration_capsule.md:20` |

## Top-5 latency-perception approaches

| # | technique | verdict | evidence |
|---|---|---|---|
| 1 | **Edge/local inference, no cloud round-trip** (accuracy traded for responsiveness, recovered via smoothing/confidence-gating) | doctrine, HandPiano-cited | `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\CAREER_KIT_v1.md:102` |
| 2 | **`confidenceDecay: 0.7`** on coasting — latency-hiding degrades gracefully rather than freezing/dropping | design doc, unshipped | `...HFO_Omega_Spatial_Input_Factory_Sigrun_Analysis_v0_2.md:398` |
| 3 | **`maxDtMs: 2000`** stale-gap detection (reset velocity baseline rather than clamp on a big time gap) | shipped, fuzz-covered | `C:\Dev\handpiano_launch_20260602\dist\refinery.mjs:81` |
| 4 | **`minDtMs: 0.5`** duplicate/zero-dt frame detection (hold-if-static / drop-if-moved) | shipped, fuzz-covered | same file, line 80 |
| 5 | No dedicated JND (just-noticeable-difference) or perceptual-threshold technique was found this pass | — gap, not a finding | n/a |

## Top-5 safety approaches

| # | technique | verdict | evidence |
|---|---|---|---|
| 1 | **KinematicPhysicsGuard** (teleport/velocity/accel/NaN/OOB/geometry/hand-count/frame-time, pre-filter) | ✅ SPLENDOR — 86/95 fuzz-SOUND, 0 false-rejects, browser-verified | `C:\Dev\handpiano_launch_20260602\dist\refinery.mjs:211` + `fuzz\FUZZ_REPORT.md:58` |
| 2 | **Confidence gate** (`minConfidence: 0.30`, rejects NaN/<0) | shipped, part of guard | `refinery.mjs:74` |
| 3 | **Bounds clamp-or-drop** (`boundsClampTolerance: 0.06`) | shipped, part of guard | `refinery.mjs:78` |
| 4 | **VelocityClamp / ConfidenceHysteresis / DualLeakyBucket** — MOSA-composable safety plugins | design-complete, no runtime verification found | `k2-filter-chain.ts:12,253,327` |
| 5 | **"Safety-before-smoothing" ordering doctrine** (KinematicClampTile named explicitly to run before smoothing, "prevents reacquire jumps") | design principle, matches the gen-130 shipped ordering (guard wired BEFORE the 1-euro filter) | `hfo_input_kernel.mjs:165` + `GEN130_MOBA_E_BEACON_canonical_handpiano_20260603T2322Z.md:43` |

## Primitives ready to adopt from own history (working implementation exists)

- **KinematicPhysicsGuard + PointRefinery (1-euro + lookahead)** — `C:\Dev\handpiano_launch_20260602\dist\refinery.mjs`. This is the single strongest candidate: it is the only input-method artifact in the entire mining pass with (a) a shipped implementation, (b) an adversarial fuzz test suite with numeric pass/fail thresholds, and (c) browser-level verification through a real app seam. Port it directly rather than re-deriving.
- **CanonicalHandFrame DTO shape** (`{schema, timestamp, source, hands, cursors}`) — same file, `makeHandFrame()` at line 59 — gives gen-133 a ready-made ABI envelope.

## Primitives that need fresh build or external adoption

- **JND / perceptual-latency threshold modeling** — no implementation or design doc found anywhere in this pass. If gen-133 wants a principled "how much latency can a user actually feel" budget, this needs either fresh research or an external exemplar (e.g. published game-networking JND literature); nothing in-house was found.
- **Chirality / cross-frame hand-identity model** — explicitly named as a gap in the fuzz report's own roadmap allowlist (`geo-inverted-finger-order`, `geo-identity-chirality-mismatch`, `geo-identity-flip-handedness` — `handpiano_launch_20260602\fuzz\FUZZ_REPORT.md:67-71`). The existing guard correctly declines to handle these; gen-133 should treat this as a known, disclosed gap rather than an oversight.
- **Auto-tuning smoothing** (`N1EuroAutoTune`, gen-107) — designed but never verified running against real MediaPipe input as far as this pass found. Worth a fresh verification pass before trusting it, not a fresh build.

## Honest scope note

**Covered with real content reads (not just file-list hits):** gen-130 forge (deep), `handpiano_launch_20260602` (deep — this is where the only fully-verified artifact lives), gen-107 `k2-filter-chain.ts` (sampled, single file, ~30 lines read), gen-98 `test_signal_refinery.py` (sampled, ~40 lines read), gen-131 `hfo_input_kernel.mjs` + `gesture_pointer_bridge/README.md` (sampled), gen-115 curated design doc (sampled, ~50 lines across a 800+ line file).

**Covered by file-list scan only, NOT individually line-verified:** gen-133 itself (18 files matched a keyword scan; only titles/paths recorded, not opened — see the two `input_method_heritage_mining` rows tagged `"file-list hit only"`), gen-132 / gen-132_forge_clean (30 and 8 files matched respectively; sampled content looked like mesh/governance infra rather than spatial-input, so not deep-mined further under the time budget).

**Not reached at all this pass:** `hfo_dev_2026_4_14`, `hfo_dev_2026_5`, `hfo_dev_2026_5_6`, `hfo_dev_2026_5_10`, `hfo_dev_2026_5_13`, `hfo_dev_2026_5_14`, `hfo_dev_2026_5_17`, `hfo_dev_2026_5_19`, `hfo_dev_2026_5_18`, `hfo_dev_2026_5_21`, `hfo_dev_2026_5_22`, `hfo_dev_2026_5_24`, `hfo_dev_2026_4`, `HFO_GEN99_VAULT_2026_03_19`, `archive\omega_gen7_unified_archive_2026_1_31`, `hfo_heritage`. All confirmed to exist in MOVE 1 (none were inaccessible/permission-denied) — they were simply not reached inside the 45-minute active-work timebox after the higher-priority roots (1-4, 9, plus gen-98/gen-107 for ancestry) consumed the budget. This is a disclosed gap, not a claim of "nothing there."

**`RECOVERY_TRIAGE_20260602.md`** and **`work/factory/spatial_os/hand_model_lab/`** (both cited in operator project memory as existing) were checked directly and **not found** at their expected paths — see `input_method_proof_artifacts_20260801.jsonl` for the `not_found` rows. Memory may be stale, or the artifacts moved/were pruned since the memory note was written; this pass did not search further for their new location under the time budget.

**`capacity_manifest.jsonl`** exists only at gen-130 (`state\ssot\capacity_manifest.jsonl`) among the priority roots checked; gen-131/132/133 have only schema/template files (`contracts\schemas\capacity_manifest.v0_1.json`, `manifest\capacity_manifest.schema.json`), no populated ledger — confirming the recon note in the task brief.

*Réttu hönd, eigi spyr. Standa.*
