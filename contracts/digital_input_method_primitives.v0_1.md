```yaml
# AIH2O capsule
doc: contracts/digital_input_method_primitives.v0_1.md
schema_id: hfo.gen133.contract.digital_input_method_primitives.v0_1
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — I author no scripts/)
valid_time_utc:       2026-08-01T04:54:47Z
transaction_time_utc: 2026-08-01T04:54:47Z
git_head: 60893a4
claim_status: proposed
sealed: false
supersedes: nothing
complements:
  - contracts/spatial_factory_framework.v0_1.md (the production line — this is the PRODUCT's internals)
  - contracts/spatial_input_ABI.v0_2.md (the wire format these primitives produce)
  - contracts/input_method_exemplars_adopt_before_reinvent.v0_1.md (what to adopt per primitive)
A_assumption: the operator's four demos are four skins on ONE machine — a noisy-landmark-to-trustworthy-intent refinery — and that machine is worth naming as primitives so it can be reused, tested, and sold rather than rebuilt per demo
I_input: hfopiano_v512 source read first-hand this session (signal_refinery.mjs, tracking_admission.mjs, refinery_presets.mjs, wrist_physics_guard.mjs, index.html PointRefinery §1820-1850) + 6 web-researched primitive families
H_hypothesis: the operator has already built 3 of the 4 axes to production quality and the 4th (lookahead / latency-perception) is COMPUTED BUT DISABLED in 100% of shipped presets — so the gap is not capability, it is one authority weight
H2_heldout: set lookahead authority > 0 on a golden MP4 trace and measure whether time-to-note-onset drops without raising false-trigger count. If false triggers rise faster than latency falls, the zero weight was CORRECT and this document's headline finding inverts.
O_output: 4 axes · 26 primitives · 1 measured pipeline · 1 falsified default · 8 falsifiers
```

# DIGITAL INPUT METHOD PRIMITIVES v0_1

*Decomposition of "noisy sensor → trustworthy intent" into atomic, swappable stages.*

---

## 0 · The headline finding, stated before the taxonomy

The operator asked to decompose the demo into primitives. Doing so surfaced a
fact that outranks the taxonomy itself, so it goes first.

**`hfopiano_v512` already implements all four axes.** The pipeline is named in
its own source comment (`signal_refinery.mjs:4`):

```
raw → [kinematic clamp] → [1-euro filter] → [lookahead] → [authority blend]
```

**But the lookahead stage's output weight is `0` in every shipped configuration.**

Verified first-hand this session, three independent places:

| Where | Evidence | Count |
|---|---|---|
| `refinery_presets.mjs` — `REFINERY_PRESETS` | `authority: {raw:0, filtered:1.0, lookahead:0}` | 3 of 3 presets |
| `refinery_presets.mjs` — `CURSOR_SMOOTHING_PRESETS` | same | 3 of 3 presets |
| `settings_profiles.v512.json` (49 KB, tallied by parse) | `{"filtered":1,"lookahead":0,"raw":0}` | **6 of 6 authority objects** |
| `index.html:899` — inline `CONFIG` default | `authority: { raw:0, filtered:1.0, lookahead:0 }` | 1 of 1 |

The app's own UI text concedes it. `index.html:626` labels raw and lookahead
**"diagnostic"**; `index.html:629` states the lookahead horizon
**"is not direct note authority in launch presets."**

So `lookaheadMs` (20 / 40 / 60 ms across presets) is computed every frame at
`index.html:1839-1840` and then multiplied by zero.

**Interpretation — and the honest fork.** There are two readings and this
document does not get to pick for free:

- **Reading A (gap):** the latency-perception axis is SPECIFIED-NOT-WIRED. One
  config change unlocks it. This is the reading that flatters the roadmap.
- **Reading B (earned default):** someone tried it, got false note-triggers from
  over-prediction, and set the weight to zero on purpose. The `known-limits.html`
  file and the ADR trail suggest this codebase does not ship untested defaults.

**H2_heldout above is the discriminator, and it has not been run.** Until it is,
§3 treats lookahead as *unproven-in-this-app*, not as *free latency*. See §3.5
for the research reason Reading B is more likely than it looks.

---

## 1 · The four axes and what they actually trade against each other

These are not four independent features. They are four points on **one**
trade-off surface, and naming the surface is most of the value:

```
                 jitter ◄──────────────────────────► lag
                        ▲                          ▲
        smoothing pulls │                          │ prediction pulls
        this way        │                          │ this way
                        │                          │
              safety ───┴── clamps BOTH ends ──────┘
                        (and pays in responsiveness)
```

**The invariant that makes the operator's design good:** noise is shaped by
*filtering and clamping*, never by *dropping*. Both `tracking_admission.mjs:30`
and `signal_refinery.mjs:10` state this independently as
**CLAMP-don't-drop** / **persist-once-detected**. That is a genuine design
insight and it is the thing most naive gesture pipelines get wrong — they gate
on classifier confidence, the hand changes gesture, confidence dips, tracking
falls off, and the user blames the camera.

**Stated as a rule for the ABI (§ carried into `spatial_input_ABI.v0_2`):**

> **P-0 · A classifier score must never gate the tracking of an established
> track.** Confidence gates *admission of new tracks* only. Kinematics gate
> *motion*. Conflating the two is the root cause of "tracking falls off when I
> change gesture."

---

## 2 · Axis 1 — SMOOTHING primitives

**Signature (all of them):** `(x_t, t) → x̂_t`, causal, streaming, O(1) state.

| # | Primitive | One sentence | Latency cost | Wins when | Fails when |
|---|---|---|---|---|---|
| S1 | **1-Euro filter** | Low-pass whose cutoff *rises with speed*: heavy smoothing when still, light when moving. | adaptive, ~1 frame at speed | interactive pointing — the canonical default | needs 2-param tuning; no noise model |
| S2 | **EMA / exponential** | `x̂ = αx + (1-α)x̂'`. One line, one param. | fixed, high for a given smoothness | prototypes, non-interactive | constant lag is felt at any useful α |
| S3 | **Double-exponential (Holt)** | EMA plus a tracked trend term. | lower lag than S2 at equal smoothness | signals with sustained velocity | overshoots on direction reversal |
| S4 | **Median filter (k-tap)** | Order statistic over a window. | (k-1)/2 frames | **spike/outlier rejection** — different job from S1 | destroys fine motion; cost grows with k |
| S5 | **Savitzky-Golay** | Least-squares polynomial fit over a window. | (k-1)/2 frames | preserving peaks/derivatives (velocity, onsets) | needs a window ⇒ inherently lagged |
| S6 | **Kalman (linear)** | Optimal estimator *given* a correct linear model + noise covariances. | model-dependent | you genuinely have a motion model and noise stats | hand motion is non-stationary; Q/R tuning is harder than 1-Euro's 2 params |
| S7 | **Extended Kalman** | S6 linearized about the current estimate. | higher | nonlinear observation (e.g. projection) | divergence risk; heavy for a web input path |
| S8 | **Complementary filter** | Blend a low-passed slow source with a high-passed fast one. | ~0 | genuine *sensor fusion* (IMU + vision) | needs two sources — N/A for camera-only |

**The measured comparison (research, not opinion).** The 1-Euro filter was
designed precisely against Kalman for this use case and reports the smaller
standard error (0.004 mm vs 0.015 mm) while cutting lag, with **two** tuning
parameters instead of a covariance matrix. Casiez, Roussel & Vogel, *1€ Filter*,
CHI 2012.

> **ADOPT-VERDICT · S1 is correct and already shipped.** `hfopiano_v512` uses
> 1-Euro. Do not replace it with Kalman. The literature and the app agree.

**What is genuinely missing from the operator's stack: S4.** The current spike
defense is `kinematicClamp` (a *clamp*, §4), which bends an outlier toward the
previous point but still lets it move the cursor. A 3-tap median would *reject*
a single-frame spike outright at a cost of 1 frame of lag. This is the one
smoothing primitive worth adding, and only if a golden trace shows single-frame
spikes surviving the clamp.

**FALSIFIER · S-F1:** run a golden MP4 through the refinery, log
`clamped == "teleport_clamp"` events. If they cluster as isolated single frames,
a median tap helps. If they come in runs of 2+, they are real fast motion and a
median filter would *destroy* it — do not add S4.

---

## 3 · Axis 2 — LOOKAHEAD / PREDICTION primitives

**Signature:** `(x̂_{≤t}, Δ) → x̃_{t+Δ}`. Every one trades *spatial error* for
*temporal lead*. There is no free lunch; the only question is the exchange rate.

| # | Primitive | One sentence | Horizon it survives | Fails when |
|---|---|---|---|---|
| P1 | **Constant-velocity dead reckoning** | `x̃ = x̂ + v·Δ`. | ~20–33 ms | any direction reversal — overshoots hard |
| P2 | **Constant-acceleration** | adds `½aΔ²`. | ~30–50 ms smooth motion | acceleration estimates are noise-amplified (2nd derivative) |
| P3 | **α-β / α-β-γ filter** | Fixed-gain radar tracker; Kalman's cheap cousin. | ~50 ms | needs steady-state assumption |
| P4 | **Kalman predict step** | Forward-project state before the measurement update. | model-dependent | inherits every S6 weakness, plus horizon error |
| P5 | **LSTM / GRU / TCN trajectory** | Learned motion prior over a history window. | 50–150 ms | needs training data, a runtime, and a latency budget of its own |
| P6 | **Task-structural prediction** | Predict the *event* (grasp/onset), not the position. | event-specific | needs a task model — but see §3.4, this is the sleeper |

### 3.1 What the operator's app actually implements

`index.html:1838-1840` — **P1, constant-velocity dead reckoning:**

```js
const la = c.lookaheadMs/1000;
const look = { x: rx.value + vel.x*la, ... };   // rx.value is the FILTERED value
```

Two properties worth naming:

1. **It extrapolates from the *filtered* signal, not the raw one.** `rx.value`
   is the 1-Euro output and `vel` is the 1-Euro's internal derivative. So the
   lookahead is trying to undo lag that the filter *just added*, using a velocity
   estimate that the same filter *just smoothed*. This is not wrong — it is the
   standard construction — but it means **lookaheadMs is not a latency budget,
   it is a lag-compensation term**, and calibrating it against end-to-end
   motion-to-photon latency would be a category error.
2. **It is P1, the weakest predictor**, at horizons up to 60 ms.

### 3.2 The research ceiling — and why the operator's 60 ms preset is suspect

Next-point prediction research on direct-touch input converges on a hard result:

- **Predicting ~33 ms ahead improves user performance.**
- **Predicting beyond ~33 ms does not** — subjective assessment *degrades*
  because prediction error produces visible spatial artifacts.
- Researchers went as far as defining metrics for **seven distinct spatial
  "side-effects"** of next-point prediction (overshoot, wrong-direction,
  jitter-amplification, lateness, …) precisely because over-prediction is
  visually offensive in a way that lag is not.

Cross-referenced against the shipped presets:

| Preset | `lookaheadMs` | vs ~33 ms research ceiling |
|---|---|---|
| Stable | 20 | ✅ within |
| ResponsivePlus (default) | 40 | ⚠️ marginal |
| Responsive | **60** | ❌ **~2× the ceiling, on the weakest predictor (P1)** |

> **This materially strengthens Reading B in §0.** A 60 ms constant-velocity
> extrapolation would produce exactly the overshoot-on-reversal artifact the
> literature describes. Setting `lookahead: 0` may not be an oversight — it may
> be the correct empirical response to a horizon that was set too long for the
> predictor being used. **The fix in that case is not "turn on lookahead," it is
> "lower the horizon to ≤33 ms, then turn it on."**

### 3.3 The perception numbers that bound the whole problem

Just-noticeable-difference thresholds for latency (direct-touch literature):

| Interaction | JND | Performance degrades above |
|---|---|---|
| **Dragging** (continuous) | **~11 ms** (some studies: 6 ms) | ~25 ms |
| **Tapping** (discrete) | **~69 ms** | much higher |

**This is the most decision-relevant pair of numbers in this document**, because
it says the two things the operator's app does are governed by *different budgets
that differ by 6×*:

- The **cursor** (continuous drag) is judged at ~11 ms — brutal, and no
  camera-based pipeline will hit it.
- The **note onset** (discrete tap) is judged at ~69 ms — **achievable**.

> **P-1 · Split the budget by event class.** Continuous-position latency and
> discrete-event latency are different products with different acceptance bars.
> Optimizing them with one `lookaheadMs` knob is why one knob cannot win.

### 3.4 The sleeper primitive: P6, predict the *event*, not the position

This is where the recent literature has moved, and it fits the operator's app
better than P1 ever will. **Grasp Prediction based on Local Finger Motion
Dynamics** (arXiv 2506.10818, 2025) reports an LSTM predicting **the time point
of a grasp to better than 21 ms**, and distance-to-object to better than 1 cm,
explicitly framed for "adaptive and fine-grained interactive user interfaces."

Why this matters for a *piano*: a piano key press is a discrete onset event, not
a cursor position. Predicting *"a key-down is coming in ~20 ms"* lets you start
the audio envelope early — which attacks felt latency **where the 69 ms budget
lives** — without moving the cursor a single pixel and therefore **without any
of the seven spatial side-effects.**

> **This is the highest-value unbuilt primitive in the stack.** P1 fights for
> milliseconds against an 11 ms bar it cannot win. P6 fights inside a 69 ms bar
> it can. Ranked #1 in §7.

### 3.5 FALSIFIERS

- **P-F1 (the §0 discriminator):** set `lookahead: 0.5` at `lookaheadMs: 33` on a
  golden MP4. Measure note-onset time AND false-trigger count. **If false
  triggers rise at all, Reading B is confirmed and §0's headline is downgraded
  from "gap" to "correct default."**
- **P-F2:** the 60 ms Responsive preset should show *more* overshoot artifacts
  than the 20 ms Stable preset when lookahead is enabled. If it does not, the
  §3.2 research ceiling does not transfer to camera-based hand input and the
  whole of §3.2 is wrong.
- **P-F3 (kills P6 if it fails):** on recorded traces, can *any* model call a
  key-down ≥20 ms before it happens, better than chance? If not, §3.4 is a paper
  result that does not transfer and P6 drops to rank 5.

---

## 4 · Axis 3 — SAFETY primitives

**Signature:** `(candidate, state) → (accepted | modified | refused, reason)`.
The `reason` is not optional — a safety stage that cannot say *why* it fired is
unfalsifiable and cannot be tuned.

| # | Primitive | One sentence | Shipped in v512? |
|---|---|---|---|
| F1 | **Kinematic step clamp** | Bound per-frame displacement; bend outliers toward previous. | ✅ `signal_refinery.kinematicClamp` — fixed thresholds |
| F2 | **Adaptive outlier clamp** | Same, but the threshold is `median + k·MAD` of the hand's *own* rolling history. | ✅ `wrist_physics_guard.mjs` — Planck.js (MIT), `teleport_k_mad: 6.0`, 60-frame buffer |
| F3 | **NaN / non-finite freeze** | Non-finite input freezes to last good value rather than propagating NaN. | ✅ `kinematicClamp` → `"nan_freeze"` |
| F4 | **Range clamp** | Hard-bound output to `[0,1]`. | ✅ `clamp01` |
| F5 | **Admission gate** | Confidence threshold for **new** tracks only. | ✅ `tracking_admission.admitHand` |
| F6 | **Persistence / coasting** | Keep a track alive across brief dropouts (`coastMs` 80–300). | ✅ `persistence.mjs` |
| F7 | **Dead-man / staleness release** | Release a track when motion falls *below* the hand's own micro-jitter floor — a real hand always tremors; a frozen cursor does not. | ✅ `wrist_physics_guard` |
| F8 | **Dead zone** | Ignore input inside a region/threshold. | ⚠️ partial (`stickiness`) |
| F9 | **Rate limit** | Bound *events/sec*, distinct from bounding motion. | ❌ **not found** |
| F10 | **Fallback modality** | Degrade to mouse/keyboard when the primary modality fails. | ⚠️ seams exist (`injectCursorDTO`), policy does not |
| F11 | **Jidoka / halt-on-defect** | Stop the line on a detected defect rather than emitting degraded output. | ✅ `lifecycle_panic.mjs` |
| F12 | **State-machine verification** | Prove unsafe states are unreachable. | ❌ not attempted |

**F7 deserves special note** because it is genuinely clever and I have not seen
it in the published literature: *inverting* the liveness test. Most systems ask
"is this moving enough to be real?" — which punishes deliberate stillness. The
operator's guard asks "is this *impossibly* still?" using the hand's own tremor
floor as the reference. Merely-slow passes; frozen does not. The stated principle
in `wrist_physics_guard.mjs:13` — **"gate the IMPOSSIBLE, never the merely-fast
or merely-slow"** — is the correct general form of a safety primitive and should
be lifted into the ABI as a rule.

> **P-2 · Safety stages gate the impossible, not the unusual.** Any threshold
> expressed as a fixed absolute (pixels, m/s) is a latent bug; express it
> relative to the signal's own recent statistics or to body scale.

**The real gap: F9 + F10 are the two that protect *the user*, and both are
weakest.** F1–F8 protect the *signal*. If the camera is occluded mid-performance,
nothing in the shipped stack routes the user to a working input path.

**FALSIFIER · F-F1:** occlude the camera mid-gesture on a golden trace. Does the
app emit a *distinguishable* degraded-mode signal, or does it silently coast then
release? If the user cannot tell "the system lost me" from "I stopped moving,"
F10 is required, not optional.

---

## 5 · Axis 4 — LATENCY PERCEPTION primitives

Distinct from §3: these reduce *felt* latency **without** predicting position.
They are cheaper, safer, and mostly unbuilt in the operator's stack.

| # | Primitive | Mechanism | Cost |
|---|---|---|---|
| L1 | **Anticipation feedback** | Visual/haptic response begins on *approach*, before commit (key glows as the finger descends). | trivial — pure render |
| L2 | **Decouple visual from authority** | Render the *predicted* point, act on the *filtered* point. Eye sees no lag; audio never false-fires. | small |
| L3 | **Client-side prediction + rollback** | Act immediately, reconcile on truth (GGPO/netcode). | needs reversible effects |
| L4 | **Audio-first commit** | Fire the sound at detection and let the visual catch up — the ear is stricter than the eye. | small |
| L5 | **Perceptual masking** | A transient (click, flash) at commit masks a following delay. | trivial |
| L6 | **Pipeline shortening** | Just make it faster: worker offload, lower resolution, `requestVideoFrameCallback`. | ✅ partly shipped |

**L2 is the single most valuable unbuilt item on this axis, and it is nearly
free.** The operator's architecture *already separates the streams* — `refine()`
returns `{raw, filtered, lookahead, velocity, speed}` and the DTO carries
"full raw/filtered/lookahead/velocity per point" (`index.html:4364`). The
authority blend then collapses them to one point.

> **The insight §0's finding actually points at:** the app has **one** authority
> knob where it needs **two**. Note authority should stay `filtered` (protecting
> the 69 ms discrete budget from false triggers). *Visual* authority should be
> allowed `lookahead` (attacking the 11 ms continuous budget, where a few px of
> overshoot is invisible but lag is not).
>
> **A wrong pixel is forgivable. A wrong note is not.** One knob cannot express
> that; two can. This is a strictly better change than turning the existing knob
> up, and it makes P-F1's risk go to zero on the audio path.

**FALSIFIER · L-F1:** ship L2 (visual=lookahead@33ms, note=filtered) and A/B it
blind against the current build. If testers cannot pick the L2 build above
chance, felt latency is not dominated by the cursor and L4/L6 should be ranked
above it.

---

## 6 · The composed pipeline, as measured

```
camera / MP4 / injected trace
  │
  ├─ SEAM 1  setVideoSource(urlOrStream)
  ▼
MediaPipe HandLandmarker  (worker thread — mediapipe_hand_landmarker.worker.mjs)
  │  detectionConf / presenceConf / trackingConf     ← F5, tunable per preset
  ├─ SEAM 2  injectRawLandmarks(hands, ts)
  ├─ SEAM 3  injectNoisyLandmarks(hands, ts)
  ▼
persistence.mjs        → slotId, coasting            ← F6
  ▼
tracking_admission.mjs → admitHand()                 ← F5, persist-once-detected
  ▼
wrist_physics_guard.mjs → Planck.js body, adaptive MAD ← F2, F7
  ▼
PointRefinery.refine()  (index.html:1820-1850)
  ├─ kinematicClamp()   ← F1, F3, F4
  ├─ OneEuro.filter()   ← S1        → filtered, velocity
  └─ lookahead          ← P1        → filtered + v·Δ
  ▼
blendAuthority({raw, filtered, lookahead}, authority)   ← ⚠️ lookahead weight = 0
  ▼
CanonicalHandFrame/1  { schema, timestamp, source, hands, cursors[] }
  │
  ├─ SEAM 4  injectCursorDTO(dto)   ← bypasses the refinery entirely
  ▼
consumers: note engine · renderer · telemetry
```

**The four injection seams are the most under-celebrated asset here.** They mean
this pipeline is **testable without a camera and without a human** — every claim
in this document is falsifiable by replaying a fixed trace. Seams 2 and 3 enter
*before* the refinery (so they test the refinery); seam 4 enters *after* (so it
tests consumers in isolation). That is a deliberate and correct test architecture,
and it is what makes the golden-master approach in `spatial_factory_framework`
possible at all.

---

## 7 · Ranked build order

Ranked by **(perceived gain) ÷ (risk × effort)**, given everything above.

| # | Item | Axis | Why here | Effort |
|---|---|---|---|---|
| **1** | **Split authority: visual vs note** (L2) | 4 | Unlocks lookahead's upside with zero false-note risk. Streams already exist; this is a config-shape change, not new math. | S |
| **2** | **Lower `lookaheadMs` to ≤33, then run P-F1** | 2 | Settles §0's fork with data. 60 ms on P1 is likely the actual bug. | S |
| **3** | **Anticipation feedback (L1) + audio-first (L4)** | 4 | Attacks felt latency with no prediction error at all. | S |
| **4** | **Fallback modality policy (F10)** | 3 | The only gap that fails the *user* rather than the signal. | M |
| **5** | **Event prediction / P6 grasp-onset** | 2 | Highest ceiling in the document; also the only one needing training data. | L |
| — | Median filter (S4) | 1 | **Only if S-F1 shows isolated single-frame spikes.** Do not add speculatively. | S |
| — | Kalman anywhere | 1 | **Explicitly do not.** Research and the shipped app both already chose 1-Euro. | — |

---

## 8 · Falsifier index

| ID | Kills | Test |
|---|---|---|
| S-F1 | median filter (S4) | clamp-event clustering on a golden trace |
| P-F1 | §0 headline finding | lookahead@33ms → false-trigger count |
| P-F2 | §3.2 research ceiling transfer | 60 ms vs 20 ms overshoot comparison |
| P-F3 | P6 event prediction | can any model call key-down ≥20 ms early, above chance? |
| F-F1 | F10 necessity | camera occlusion → is degraded mode distinguishable? |
| L-F1 | L2 ranking | blind A/B of split-authority build |

**Honest flaw of this document:** every primitive claim about `hfopiano_v512` was
read from source this session and is solid. **Every claim about what would
*improve* it is unrun.** The §0 headline is a real, verified, triple-confirmed
fact about the configuration — but its *interpretation* as a gap rather than an
earned default is exactly the kind of thing that looks obviously right and is
50/50 until P-F1 runs. §3.2 is the reason I now lean toward it being an earned
default with a mis-set horizon, which is a materially different repair than the
one this document would have recommended before the research pass.

---

*Sources:* [1€ Filter (Casiez et al., CHI 2012)](https://inria.hal.science/hal-00670496/document) ·
[1€ Filter, ACM DL](https://dl.acm.org/doi/10.1145/2207676.2208639) ·
[Are 100 ms Fast Enough? Latency Perception Thresholds](https://link.springer.com/chapter/10.1007/978-3-319-58475-1_4) ·
[Next-Point Prediction Metrics for Perceived Spatial Errors](https://www.researchgate.net/publication/310823575_Next-Point_Prediction_Metrics_for_Perceived_Spatial_Errors) ·
[User Perception of Touch Screen Latency](https://www.researchgate.net/publication/221100500_User_Perception_of_Touch_Screen_Latency) ·
[Grasp Prediction based on Local Finger Motion Dynamics (arXiv 2506.10818)](https://arxiv.org/abs/2506.10818) ·
[MediaPipe Hand Landmarker](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)
