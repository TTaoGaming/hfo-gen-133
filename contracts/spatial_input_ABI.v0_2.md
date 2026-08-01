```yaml
# AIH2O capsule
doc: contracts/spatial_input_ABI.v0_2.md
schema_id: hfo.gen133.contract.spatial_input_abi.v0_2
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — I author no scripts/)
valid_time_utc:       2026-08-01T04:54:47Z
transaction_time_utc: 2026-08-01T04:54:47Z
git_head: 60893a4
claim_status: proposed
sealed: false
supersedes: nothing — v0_1 of THIS document does not exist; the predecessor artifacts are shipped code, named below
predecessors_in_code:
  - CanonicalHandFrame/1        (hfopiano_v512 index.html:1854 — SHIPPED, read first-hand)
  - CursorPrimitiveOutput.v0_1  (grc ADR-0015 / ADR-0002 — SHIPPED, referenced by spatial_factory_framework)
complements:
  - contracts/digital_input_method_primitives.v0_1.md (the stages this ABI sequences)
  - contracts/spatial_factory_framework.v0_1.md §A (uses this DTO stream as the metamorphic oracle)
A_assumption: the operator wants ONE input contract that four demos and every future spatial app consume, so smoothing/prediction/safety are written once and configured per-app
I_input: CanonicalHandFrame/1 as shipped · 4 injection seams · OpenXR semantic actions · WebXR targeting/action split · the 11ms-drag / 69ms-tap JND split
H_hypothesis: the shipped DTO is already 80% right, and v0_2's job is three additions — a modality discriminator, a SPLIT authority (visual vs commit), and a mandatory degraded-mode signal — not a redesign
H2_heldout: replay a fixed landmark trace through the pipeline twice; the emitted DTO stream must be BYTE-IDENTICAL. If it is not, determinism is a claim not a property, and golden-master testing in spatial_factory_framework §A rests on sand.
O_output: 1 wire schema · 2 contracts (producer/consumer) · 5 pipeline stages · 4 fallback states · 6 falsifiers
```

# SPATIAL INPUT ABI v0_2

*One contract: any input driver → any spatial app, with smoothing, prediction and
safety applied once, in the middle, by configuration.*

---

## 0 · Why v0_2 and not v0_1

There is no `spatial_input_ABI.v0_1.md`. The predecessor is **not a document —
it is shipped code**: `CanonicalHandFrame/1` in `hfopiano_v512`, plus
`CursorPrimitiveOutput.v0_1` from the `grc` ADR line. Numbering this v0_2
records that this spec *follows working code*, and does not pretend to originate
the contract.

Preserved from the shipped DTO without change:

```js
{ schema:"CanonicalHandFrame/1", timestamp, source, hands, cursors:[] }
```

**Three additions, each traceable to a measured finding:**

| # | Addition | Driven by |
|---|---|---|
| A1 | `modality` discriminator + semantic actions | OpenXR/WebXR prior art; the app is hand-only today and hard-binds it |
| A2 | **Split authority** — `visual` vs `commit` | the 11 ms-drag / 69 ms-tap JND split (primitives §3.3, §5) |
| A3 | Mandatory `tracking_state` degraded-mode signal | F10 gap (primitives §4) — the only gap that fails the *user* |

---

## 1 · The wire schema

```jsonc
{
  "schema": "SpatialInputFrame/2",
  "frame_id": 40217,                 // monotonic, per-session; determinism anchor
  "timestamp_ms": 1234567.891,       // producer clock, monotonic
  "source": {
    "modality": "hands",             // hands|pose|face|voice|cursor|keyboard|gamepad|synthetic
    "driver": "mediapipe.hand_landmarker",
    "driver_version": "0.10.x",
    "injected": false,               // true when entering via a test seam
    "source_frame_id": 40217         // the ORIGINATING sensor frame (see §5)
  },

  "tracking_state": "tracked",       // acquiring|tracked|coasting|degraded|lost   ← A3
  "confidence": 0.83,                // producer's own score. NEVER gates an established track.

  "tracks": [{
    "track_id": "slot_0",            // stable across frames; the liveness authority
    "handedness": "right",           // modality-specific; absent for non-hand modalities
    "age_frames": 812,

    // ---- A2: the split. Two points, not one. ----
    "point": {
      "commit":  { "x":0.412, "y":0.688, "z":-0.02 },   // authoritative for EVENTS. Conservative.
      "visual":  { "x":0.418, "y":0.681, "z":-0.02 },   // authoritative for RENDER. May lead.
      "raw":     { "x":0.406, "y":0.694, "z":-0.02 },   // diagnostic
      "velocity":{ "x":0.15,  "y":-0.22, "z":0.0 },     // normalized units/sec
      "speed": 0.267
    },

    "landmarks": [ /* modality-specific array; absent for cursor/keyboard */ ],

    "actions": [                     // ---- A1: semantic, not hardware ----
      { "id":"note_press", "phase":"begin", "value":0.91, "target":"key_C4" }
    ],

    "safety": {                      // every stage that fired, and why
      "clamped": "none",             // none|step_clamp|teleport_clamp|nan_freeze|nan_noprev
      "gates_fired": [],             // e.g. ["deadman_release","rate_limit"]
      "admitted_by": "persistence"   // persistence|confidence_gate|injected
    }
  }],

  "pipeline": {                      // what produced this frame — the repro key
    "config_hash": "sha256:9f2c…",   // hash of the full refinery config
    "stages": ["admit","clamp","smooth","predict","blend"],
    "lookahead_ms": 33,
    "authority": { "commit":"filtered", "visual":"lookahead" }
  }
}
```

### 1.1 Why `commit` and `visual` are separate fields, not one point plus a flag

This is the load-bearing design decision in v0_2 and it comes straight from
measurement, not taste.

Continuous dragging is judged against a **~11 ms** JND. Discrete tapping is
judged against **~69 ms**. Those budgets differ by ~6×, so one authority setting
must lose one of them. Worse, they fail *asymmetrically*:

> **A wrong pixel is forgivable. A wrong note is not.**

Prediction error on the visual stream costs a few pixels of overshoot that the
literature says users largely do not notice below ~33 ms. The identical error on
the commit stream costs a **false note trigger** — an unrecoverable, audible
defect.

So the ABI makes them *different fields* rather than one field with a policy,
because a policy can be misconfigured into a false trigger and a field cannot.
`commit` is allowed to be conservative forever; `visual` is allowed to lead.

**This directly repairs the finding in `digital_input_method_primitives` §0** —
that lookahead has weight `0` in 100% of shipped profiles — without taking on the
false-trigger risk that (per §3.2 of that document) probably caused the zero in
the first place.

---

## 2 · Producer contract

Any driver claiming `SpatialInputFrame/2` MUST:

| # | Requirement |
|---|---|
| PR-1 | Emit `timestamp_ms` from a **monotonic** clock. Never wall-clock. |
| PR-2 | Emit a stable `track_id` for the lifetime of a track; never reuse an id within a session. |
| PR-3 | Emit `confidence` as its **own** score, and never use it to drop an established track (**P-0**). |
| PR-4 | Emit `point.raw` unmodified. Producers do not smooth — that is the middleware's job. |
| PR-5 | Emit `tracking_state`, including `lost`. Silence is not a valid way to say "lost". |
| PR-6 | Be **replaceable**: emitting this frame is the whole contract. A mouse driver and MediaPipe are peers. |

**PR-5 is the F10 repair.** The shipped app coasts and then releases; a consumer
cannot currently distinguish "the user stopped moving" from "we lost the hand."
Making `lost` an explicit emitted state — rather than the absence of frames — is
what lets a consumer offer a fallback instead of appearing frozen.

---

## 3 · Consumer contract

| # | Requirement |
|---|---|
| CO-1 | Use `point.commit` for anything **irreversible** (note-on, click, submit, purchase). |
| CO-2 | Use `point.visual` for rendering. Never render `commit` — that is where felt lag comes from. |
| CO-3 | Handle all five `tracking_state` values. `degraded` and `lost` MUST have defined UI. |
| CO-4 | Bind to `actions[].id` (semantic), never to `landmarks[i]` (hardware). Landmark access is a debug affordance. |
| CO-5 | Never re-smooth. Double-smoothing is double lag. |
| CO-6 | Tolerate unknown `modality` values — degrade, do not throw. |

**CO-4 is the OpenXR lesson.** Apps bind to `menu_select`, not to "the A button."
That indirection is what makes rebinding, accessibility, and multi-modality
possible without touching app code — and it is what turns the operator's four
demos into four *configs* rather than four codebases.

---

## 4 · Middleware — the pluggable pipeline

```
producer frame (raw, unsmoothed)
   ↓
[1] ADMIT     confidence gate — NEW tracks only          (F5)
   ↓
[2] CLAMP     kinematic/adaptive outlier bound            (F1,F2,F3,F4,F7)
   ↓
[3] SMOOTH    1-Euro (minCutoff, beta)                    (S1)
   ↓
[4] PREDICT   horizon ≤33ms → produces `visual` only      (P1/P6)
   ↓
[5] BLEND     authority weights → commit + visual         (A2)
   ↓
SpatialInputFrame/2
```

Each stage: `(frame, config, state) → (frame', state')`. Pure w.r.t. its declared
state; **must** record what it did into `safety.gates_fired`.

**Stage ordering is not arbitrary and must not be reordered:**
- CLAMP before SMOOTH — otherwise the filter ingests the spike and rings.
- PREDICT after SMOOTH — extrapolating raw noise amplifies it.
- ADMIT first — never spend compute on an inadmissible track.

**Config is data.** The entire pipeline is described by the `pipeline` block in
§1, and `config_hash` makes any emitted frame reproducible. This is what lets
`spatial_factory_framework` treat a reskin as a config swap with a byte-stable
DTO oracle.

---

## 5 · Determinism

The metamorphic test in `spatial_factory_framework.v0_1` §A ("`reskin(app)`
produces a byte-identical DTO stream") depends entirely on this section holding.

**Requirements:**

| # | Requirement |
|---|---|
| D-1 | Replaying an identical input trace with an identical `config_hash` MUST produce a byte-identical frame stream. |
| D-2 | No stage may read wall-clock time. `dt` comes from `timestamp_ms` deltas **in the trace**, never from `performance.now()` at replay time. |
| D-3 | No stage may consume unseeded randomness. |
| D-4 | Float ops must be order-stable — no parallel reduction over tracks. |
| D-5 | `source_frame_id` must be carried through unchanged, so any output frame is attributable to its originating sensor frame. |

**D-2 is the one most likely to be already violated.** The shipped
`PointRefinery.refine()` computes `dt` from a timestamp, but the surrounding
loop is driven by rAF/`performance.now()`. If any `dt` on the replay path comes
from real elapsed time rather than trace timestamps, replays will differ run to
run and D-1 fails.

> **⚠️ UNVERIFIED.** I read `refine()` (`index.html:1820-1850`) but did **not**
> trace every caller's `dt` source, and I did not run a double-replay. **D-1 is
> a requirement in this spec, not an observed property of the shipped app.**
> H2_heldout is exactly this test and it is unrun.

The four shipped seams are what make the test cheap: `injectRawLandmarks` feeds
a fixed trace in at stage 0 with no camera and no human.

---

## 6 · Fallback semantics

| `tracking_state` | Meaning | Producer | Consumer MUST |
|---|---|---|---|
| `acquiring` | no track yet; confidence gate active | emit frames, empty `tracks` | show "looking for your hand" |
| `tracked` | committed; slot id stable | full frames | normal operation |
| `coasting` | brief dropout; extrapolating within `coastMs` | last-known + `coasting` | keep rendering; **suppress new commits** |
| `degraded` | tracking alive but quality low (occlusion, dark) | frames + lowered `confidence` | visible quality indicator; **offer fallback modality** |
| `lost` | released; track id retired | emit `lost` **once**, then `acquiring` | release held state; **activate fallback** |

**The rule that matters:** `coasting` **suppresses new commits but keeps
rendering.** Continuity of the visual (which the eye tracks) is preserved while
the irreversible path (which the ear judges) refuses to fire on extrapolated
data. This is the same asymmetry as §1.1, applied to dropout instead of
prediction — and it is why the two-field split pays for itself twice.

---

## 7 · Falsifiers

| ID | Kills | Test |
|---|---|---|
| **A-F1** | §5 determinism, and with it the factory's metamorphic oracle | replay one trace twice → byte-compare. **Highest priority; unrun.** |
| A-F2 | §1.1 split-authority design | ship split authority; if testers cannot distinguish it from `filtered`-everywhere above chance, the split is unjustified complexity |
| A-F3 | §3 CO-4 semantic binding | if no second modality ever ships, the action indirection is pure overhead |
| A-F4 | §6 fallback model | occlude camera; if no `degraded`/`lost` is emitted, PR-5 is unimplementable as specified |
| A-F5 | the whole ABI | if a second app cannot consume `SpatialInputFrame/2` without modification, this is a description of one app, not an ABI |
| A-F6 | §4 stage order | reorder CLAMP/SMOOTH on a spiky trace; if output is unchanged, the ordering claim is decoration |

**A-F5 is the real test.** An ABI with one consumer is a data structure. The
operator has (at least) `hfopiano_v512` and `pinchpiano`; the cheapest proof is
making the second one consume this contract unmodified.

---

## 8 · Honest flaw

This document specifies a contract that **nothing currently implements.** The
shipped `CanonicalHandFrame/1` is close but does not carry `tracking_state`,
split authority, semantic actions, or `config_hash`. Every requirement here is
`proposed`, and the migration cost — touching the DTO factory, the blend stage,
and every consumer — is real and unestimated.

Two specific weaknesses I am not papering over:

1. **D-1 is asserted, not measured** (§5). The factory framework's blocking
   metamorphic gate depends on it. If A-F1 fails, that gate needs redesign, and
   this document will have contributed a false floor to a document that is
   already treating it as load-bearing.
2. **The `commit`/`visual` split doubles the point payload** on every track,
   every frame. For 21 landmarks × 2 hands at 60 fps that is not free, and I
   have not measured it. If profiling shows it matters, the fix is to emit
   `visual` as a *delta* from `commit` — but that is a v0_3 concern and I am
   recording it rather than pre-optimizing.

---

*Sources:* [OpenXR input chapter](https://github.com/KhronosGroup/OpenXR-Docs/blob/main/specification/sources/chapters/input.adoc) ·
[WebXR input explainer](https://immersive-web.github.io/webxr/input-explainer.html) ·
[MDN WebXR inputs](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API/Inputs) ·
[Latency perception thresholds](https://link.springer.com/chapter/10.1007/978-3-319-58475-1_4) ·
[Next-Point Prediction Metrics](https://www.researchgate.net/publication/310823575_Next-Point_Prediction_Metrics_for_Perceived_Spatial_Errors) ·
[Godot XR action map proposal](https://github.com/godotengine/godot-proposals/issues/6548)
