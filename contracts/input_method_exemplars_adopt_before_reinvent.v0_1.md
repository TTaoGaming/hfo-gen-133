```yaml
# AIH2O capsule
doc: contracts/input_method_exemplars_adopt_before_reinvent.v0_1.md
schema_id: hfo.gen133.contract.input_method_exemplars.v0_1
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — I author no scripts/)
valid_time_utc:       2026-08-01T04:54:47Z
transaction_time_utc: 2026-08-01T04:54:47Z
git_head: 60893a4
claim_status: proposed
sealed: false
supersedes: nothing
complements:
  - contracts/digital_input_method_primitives.v0_1.md (the primitives these implement)
A_assumption: every primitive in the companion document has an off-the-shelf implementation, and HFO's default failure is rebuilding one badly
I_input: 4 web research passes (smoothing libs, prediction papers, XR input abstractions, latency perception) + first-hand read of what hfopiano_v512 already vendors
H_hypothesis: the correct adopt count for the INPUT stack is near zero new dependencies — the operator has already adopted the two that matter (1-Euro, Planck.js) and the remaining gaps are design changes, not packages
H2_heldout: if a reviewer can name one npm package that would remove ≥100 lines from signal_refinery.mjs + wrist_physics_guard.mjs without changing behavior on the golden trace, this document's core recommendation is wrong
O_output: 14 candidate exemplars · 2 ADOPT · 3 STUDY-DON'T-INSTALL · 6 REJECT · 1 already-vendored audit
```

# INPUT-METHOD EXEMPLARS — adopt before reinvent v0_1

---

## 0 · The uncomfortable finding

The adopt-before-reinvent instinct is correct in general and **mostly wrong for
this specific stack**, because the operator already ran it.

`hfopiano_v512` vendors exactly the right two things:

| Already adopted | License | Used for | Verdict |
|---|---|---|---|
| **MediaPipe HandLandmarker** (Google AI Edge) | Apache-2.0 | landmark detection, in a worker | ✅ correct, no viable alternative at this quality/cost |
| **Planck.js** (Box2D 2.4 port) | MIT | wrist-level physics guard | ✅ correct, and honestly labeled |
| 1-Euro filter | (implemented inline) | smoothing | ✅ correct algorithm, see §1 on whether to swap to a package |

`wrist_physics_guard.mjs:4-9` even documents the *reasoning* for its adoption —
that the prior guard "is hand-rolled clamp/freeze math, NOT a COTS engine, and
was never wired live," and that this module is the COTS replacement. That is
adopt-before-reinvent already practiced, with provenance, unprompted.

> **So the honest recommendation for the input stack is: adopt almost nothing
> new.** The gaps identified in the primitives document (split authority,
> lookahead horizon, fallback modality, event prediction) are **design and
> config changes**, not missing libraries. Recommending a package for each would
> be adoption theatre.

What follows is therefore ranked by *whether to install at all*, and most rows
say no.

---

## 1 · Smoothing — 1-Euro implementations

| Package | License | Verdict |
|---|---|---|
| [`@webarkit/oneeurofilter-ts`](https://www.jsdelivr.com/package/npm/@webarkit/oneeurofilter-ts) | **LGPL-3.0** | ❌ **REJECT on license.** LGPL in a bundled single-file web app is a genuine compliance hazard — the dynamic-linking carve-out does not cleanly survive bundling into `index.html`. Not worth it for ~40 lines. |
| [`1eurofilter`](https://www.npmjs.com/package/1eurofilter) | (unverified) | ⚠️ license not confirmed in research pass — **do not install without checking** |
| [`@david18284/one-euro-filter`](https://www.npmjs.com/package/@david18284/one-euro-filter) | (unverified) | ⚠️ same |
| **Casiez's own reference implementation** | — | ✅ **STUDY, DON'T INSTALL.** The [1€ filter paper](https://inria.hal.science/hal-00670496/document) publishes reference code in several languages. |

> **VERDICT · Keep the inline implementation.** The 1-Euro filter is ~40 lines.
> The operator's version is already integrated with the velocity channel that
> feeds lookahead. Swapping in a package would add a dependency, an LGPL risk,
> and a refactor, to delete 40 lines of correct code.
>
> **The one thing worth doing: verify the inline implementation against the
> paper's reference vectors.** That is a test, not a dependency.

**Kalman packages** ([`kalmanjs`](https://github.com/wouterbulten/kalmanjs),
[`kalman-filter`](https://www.npmjs.com/package/kalman-filter),
[`@bencevans/kalman-filter`](https://www.npmjs.com/package/@bencevans/kalman-filter))
— ❌ **REJECT all.** Not on quality; on *fit*. The primitives document establishes
that 1-Euro beats Kalman for interactive input on both lag and tuning burden, and
`kalmanjs` is 1-D only (you would need 63 instances for 21 landmarks × 3 axes).

**FALSIFIER · E-F1:** if the inline 1-Euro fails the paper's reference vectors,
this section inverts — take a package (a correct one) over correct-looking
inline code.

---

## 2 · The reference JS implementation worth reading

[**JDBar/jwc-mediapipe**](https://github.com/JDBar/jwc-mediapipe) — TypeScript +
React MediaPipe demo exposing `getLandmarkSmootherEWMA` and
`getLandmarkSmootherKalman`.

> ✅ **STUDY, DON'T INSTALL.** Value is the *interface shape* — a landmark
> smoother as a swappable factory function — which is exactly the pluggable
> middleware pattern the ABI needs. Not a production dependency (demo-grade, and
> its Kalman path is the one §1 rejects).

---

## 3 · Prediction — papers, not packages

There is **no off-the-shelf JS library** for hand-motion lookahead worth adopting.
This is a genuine "no exemplar exists" finding, so the adopt target is *method*.

| Source | What to take |
|---|---|
| [Grasp Prediction based on Local Finger Motion Dynamics](https://arxiv.org/abs/2506.10818) (2025) | **The method for P6.** LSTM on local finger dynamics → grasp time to <21 ms. Directly transferable to key-onset prediction. |
| [Next-Point Prediction Metrics for Perceived Spatial Errors](https://www.researchgate.net/publication/310823575_Next-Point_Prediction_Metrics_for_Perceived_Spatial_Errors) | **The evaluation harness.** Seven named spatial side-effects — adopt these as the *acceptance metrics* for any lookahead change. |
| [Evaluating Pose Forecasting for Compensating Network Latency](https://link.springer.com/chapter/10.1007/978-3-032-03805-0_3) (EuroXR 2025) | Encoding scheme for pose forecasting; relevant if prediction moves to full-body. |
| [Physics-Informed LSTM Delay Compensation (arXiv 2402.16587)](https://arxiv.org/pdf/2402.16587) | Pattern for constraining a learned predictor with physics — pairs naturally with the existing Planck.js guard. |

> **Highest-leverage adoption in this entire document is a metric, not a
> library:** the seven spatial side-effect metrics. Without them, any lookahead
> change is evaluated by vibes, which is precisely how a 60 ms P1 horizon ships.

---

## 4 · ABI design exemplars

| Exemplar | Adopt | Reject |
|---|---|---|
| [**OpenXR action system**](https://github.com/KhronosGroup/OpenXR-Docs/blob/main/specification/sources/chapters/input.adoc) | ✅ **The core idea:** apps bind to *semantic actions* (`note_press`), never to hardware (`landmark_8.y`). Enables rebinding, multi-modality, and a settings UI for free. | ❌ the C API, interaction profiles, suggested-binding machinery — vastly over-scoped for the web |
| [**WebXR input sources**](https://immersive-web.github.io/webxr/input-explainer.html) | ✅ **The targeting/action split** and the three targeting modes (`gaze`, `tracked-pointer`, `screen`) — a proven modality taxonomy | ❌ the XR session lifecycle |
| **MediaPipe result DTOs** | ✅ already the de-facto producer format | — |
| **MIDI 2.0 property exchange** | ✅ the idea that a device *describes its own capabilities* to the host | ❌ the wire protocol |
| **RxJS** | ✅ operator-pipeline *mental model* (`map`/`filter`/`scan` as stages) | ❌ **do not install** — 30 KB+ for a pattern expressible in ~20 lines |

> Godot's [XR action-map proposal](https://github.com/godotengine/godot-proposals/issues/6548) is
> worth reading as prior art for exactly this problem: generalizing OpenXR's
> action model to non-OpenXR backends. Same shape as HFO's need.

---

## 5 · Adoption ledger

| # | Exemplar | Decision | Install cost | Why |
|---|---|---|---|---|
| 1 | MediaPipe HandLandmarker | ✅ **KEEP** (adopted) | 0 — shipped | no viable alternative |
| 2 | Planck.js | ✅ **KEEP** (adopted) | 0 — shipped | MIT, honest provenance |
| 3 | Inline 1-Euro | ✅ **KEEP**, add reference-vector test | 0 | swapping is negative-value |
| 4 | 7 spatial side-effect metrics | ✅ **ADOPT (as tests)** | ~1 day to implement | the only way to evaluate §3 changes |
| 5 | OpenXR semantic-action model | ✅ **ADOPT (as design)** | design-only | drives ABI v0_2 |
| 6 | WebXR targeting/action split | ✅ **ADOPT (as design)** | design-only | drives ABI v0_2 modality enum |
| 7 | jwc-mediapipe smoother interface | 🔍 **STUDY** | 0 | interface shape only |
| 8 | Grasp-prediction LSTM method | 🔍 **STUDY** | research | P6, rank 5 in primitives doc |
| 9 | `@webarkit/oneeurofilter-ts` | ❌ **REJECT** | — | LGPL-3.0 in a bundled app |
| 10 | `kalmanjs` / `kalman-filter` | ❌ **REJECT** | — | wrong algorithm for the job |
| 11 | RxJS | ❌ **REJECT** | — | 30 KB for a 20-line pattern |
| 12 | Unity XR Interaction Toolkit | ❌ **REJECT** | — | wrong runtime; app is web |

**Net new npm dependencies recommended: ZERO.**

---

## 6 · Falsifiers

| ID | Kills | Test |
|---|---|---|
| E-F1 | §1 keep-inline verdict | inline 1-Euro vs paper reference vectors |
| E-F2 | §0 "adopt nothing" thesis | name one package removing ≥100 lines from the refinery with no golden-trace behavior change |
| E-F3 | §4 OpenXR adoption | if no second modality ever ships, the semantic-action indirection is pure overhead — revert to direct binding |

**Honest flaw:** licenses for `1eurofilter` and `@david18284/one-euro-filter`
were **not confirmed** — the research pass returned the package names without
license fields. They are marked ⚠️ rather than given a verdict. This is the
same failure class as S-008 in the chain (verifying the source, not the target),
and it is flagged here rather than papered over. It does not change the
recommendation, since §1 rejects installing any of them regardless.

Second flaw: this document argues *against* the operator's stated adopt-first
frame for this one stack. That could be motivated reasoning — it is easier to
recommend nothing than to integrate something. **E-F2 is the specific,
cheap test that would prove me wrong, and it is stated in a form a reviewer can
win.**

---

*Sources:* [MediaPipe Hand Landmarker](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) ·
[jwc-mediapipe](https://github.com/JDBar/jwc-mediapipe) ·
[@webarkit/oneeurofilter-ts](https://www.jsdelivr.com/package/npm/@webarkit/oneeurofilter-ts) ·
[kalmanjs](https://github.com/wouterbulten/kalmanjs) ·
[kalman-filter (npm)](https://www.npmjs.com/package/kalman-filter) ·
[OpenXR input chapter](https://github.com/KhronosGroup/OpenXR-Docs/blob/main/specification/sources/chapters/input.adoc) ·
[WebXR input explainer](https://immersive-web.github.io/webxr/input-explainer.html) ·
[MDN WebXR inputs](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API/Inputs) ·
[Godot XR action map proposal](https://github.com/godotengine/godot-proposals/issues/6548) ·
[Grasp Prediction (arXiv 2506.10818)](https://arxiv.org/abs/2506.10818) ·
[Physics-Informed LSTM (arXiv 2402.16587)](https://arxiv.org/pdf/2402.16587) ·
[Pose Forecasting for Network Latency (EuroXR 2025)](https://link.springer.com/chapter/10.1007/978-3-032-03805-0_3)
