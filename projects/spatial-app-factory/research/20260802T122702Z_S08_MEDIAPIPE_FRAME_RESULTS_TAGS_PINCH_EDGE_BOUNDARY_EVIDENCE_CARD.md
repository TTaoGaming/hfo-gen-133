---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T12:27:02Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: interaction_input_adapters
question: Does MediaPipe Gesture Recognizer for Web provide a once-per-physical-gesture event, or must the bound producer add an explicit edge/lifecycle contract before calling the 2048 directional bridge?
decision: REVISE
fitness_credit: 0
fitness_condition: exact successor WorkItem ConsumerAck only
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
sealed: false
---

# S08 evidence card — MediaPipe frame results versus TAGS pinch edge contract

## Decision

**REVISE — treat MediaPipe Gesture Recognizer output as frame/run classification, not a documented once-per-gesture event. Admit the existing TAGS pinch lifecycle only as a candidate producer-owned edge gate; it is not yet bound to the 2048 directional action schema.**

The official Web API processes a supplied video frame on each `recognizeForVideo(...)` call and returns a `GestureRecognizerResult` for that recognition run. The official guide loops over changed video frames and calls `processResult(...)` each time. No stable `gestureId`, begin/commit/release event, duplicate key, or once-per-physical-gesture guarantee is documented for this API surface.

The exact TAGS `spatial-input-adapter.js` does contain explicit lifecycle state: `pinchHeld`, separate down/up thresholds, one `pointerdown` transition when the pinch crosses down, one `pointerup` transition when it crosses up, and `activationCallback(...)` only after the terminal `pointerup` dispatch succeeds. Repeated held samples produce pointer moves but do not produce another down or activation. That makes the adapter a plausible edge-source primitive for one pinch cycle, but no exact binding currently converts that completed pinch cycle into the directional bridge action object.

## Self-probe and changed edge

- Expected and observed carrier task ID: `6a526109ba348191b5f23ad3172ad568`; exact match.
- Available surfaces: authenticated GitHub search/fetch/create/readback, public web research, authenticated Slack pointer post.
- Changed question source: S09 held the 2048 successor until an exact gesture producer and ownership model are bound. The current uncertainty is whether the likely MediaPipe Web source already supplies logical gesture edges. It does not document such a contract.
- No task mutation, code/test mutation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, or private-data use occurred.

## Exact candidates

1. **Frame classifier candidate**
   - Package: `@mediapipe/tasks-vision@0.10.35` (stable `latest` observed 2026-08-02)
   - Repository: `google-ai-edge/mediapipe`
   - Task: `GestureRecognizer`
   - Mode/API: `runningMode: "video"`; `recognizeForVideo(videoFrame, timestamp, ...)`
   - Model example: `gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task`
   - Package/repository license: Apache-2.0

2. **Candidate edge gate already present in TAGS**
   - Repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - Path: `prototypes/spatial-input-adapter.js`
   - Git blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
   - Relevant state: `pinchHeld`, `activeTarget`, `lastPoint`, `cancellationPending`, `armed`
   - Relevant boundary: down-threshold -> held lifecycle -> up-threshold -> one activation callback

3. **Downstream call-level consumer, not yet bound**
   - Repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - Path: `prototypes/2048-spatial-canary/directional-bridge.js`
   - Git blob: `1cedd74ea11a0199a3d7537b5b4136261307f309`
   - Current admitted ceiling: `ONE_ACCEPTED_SUBMIT_CALL -> ONE_MOVE`

## Dated primary sources — accessed 2026-08-02

1. Google AI Edge, Gesture recognition guide for Web:  
   https://developers.google.com/edge/mediapipe/solutions/vision/gesture_recognizer/web_js
2. Google AI Edge, JavaScript `GestureRecognizer` API reference:  
   https://developers.google.com/edge/api/mediapipe/js/tasks-vision.gesturerecognizer
3. Official npm package metadata and versions for `@mediapipe/tasks-vision`:  
   https://www.npmjs.com/package/@mediapipe/tasks-vision?activeTab=versions
4. Official MediaPipe repository and Apache-2.0 project license:  
   https://github.com/google-ai-edge/mediapipe
5. Exact TAGS pointer/pinch adapter bytes:  
   https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/spatial-input-adapter.js
6. Prior exact repeat-suppression boundary card consumed by S09:  
   https://github.com/TTaoGaming/hfo-gen-133/blob/5cf31404669117aceae24454ee8502140f321680/projects/spatial-app-factory/research/20260802T072820Z_S08_2048_DIRECTIONAL_BRIDGE_REPEAT_SUPPRESSION_BOUNDARY_EVIDENCE_CARD.md
7. S09 successor admission HOLD requiring an exact producer ownership contract:  
   https://github.com/TTaoGaming/hfo-gen-133/blob/fc0caa0981101f357297894e4e4d12b507cabca2/state/coordination/votes/20260802T073224Z_S09_2048_REPEAT_SUPPRESSION_SUCCESSOR_ADMISSION_HOLD.vote.md

## Supported claims

- MediaPipe Web `recognizeForVideo` accepts one video frame plus timestamp and returns a result for that recognition call.
- Google's reference loop invokes recognition on changed frames and processes each returned result; the documented unit is a frame/run result, not a logical physical-gesture event.
- The inspected Web documentation does not expose a stable gesture/action identifier or a begin/commit/release lifecycle for canned gesture classification.
- Therefore a consumer must not infer exactly-once physical-gesture delivery from the MediaPipe result object alone.
- The exact TAGS adapter suppresses repeated `pointerdown` transitions while `pinchHeld` remains true and emits its activation callback only on the successful `pointerup` terminal path.
- The adapter also has cancellation paths for disarm, invalid tracking, target loss, and reset, which can end a held cycle without activation.
- A successor can plausibly use this lifecycle as the producer-owned edge boundary, provided it binds direction derivation and one completed cycle to exactly one directional action submission.

## Excluded claims

- No claim that MediaPipe necessarily returns the same classification on every adjacent frame; only that the API contract is per recognition run and does not document logical-event deduplication.
- No claim that `pinchHeld` currently fixes the 2048 canary. No exact code path maps a completed pinch cycle to `{direction, confidence}` for the directional bridge.
- No claim that pinch is the correct product gesture for 2048; swipe displacement, dwell, or another explicit lifecycle may be better.
- No claim that `activationCallback` fires when the target rejects/cancels the pointer-up event; current bytes require successful dispatch.
- No runtime performance, accuracy, latency, accessibility, browser-compatibility, user-demand, revenue, deployment, or publication clearance.
- No distinct verifier verdict or ConsumerAck.

## Required successor contract

Admit a successor only if one exact packet binds:

1. `@mediapipe/tasks-vision` version and model asset version or another exact producer;
2. one lifecycle owner: TAGS pinch cycle, displacement-based swipe lifecycle, or stable action identity;
3. direction derivation from bounded samples;
4. one terminal commit -> one `directionalBridge.submit(...)` call;
5. repeated held/frame samples -> zero additional submit calls;
6. cancellation/reset/disarm -> zero latent submit calls;
7. a later distinct same-direction gesture -> one new submit call;
8. unchanged keyboard and touch fallback;
9. a reachable distinct browser-capable verifier and named consumer.

A timeout-only debounce remains insufficient because it can suppress legitimate rapid consecutive actions without proving logical identity.

## License / terms uncertainty

- `google-ai-edge/mediapipe` and the observed npm package metadata identify Apache-2.0 for the SDK package.
- The example gesture-recognizer model is a separate downloadable model asset. This run did not inspect or admit the model card/license terms for redistribution; any packaged model must receive its own exact asset-license/provenance gate.
- The Google repository privacy notice states that input processing occurs on device but performance/utilization metrics are sent to Google and that developers are responsible for consent where legally required. This is a future product privacy/notice gate, not a blocker for local internal testing.
- No package, model, or code was downloaded, copied, installed, or redistributed by this run.

## Cost / operator-minute estimate

- Research spend: `$0`.
- Operator minutes consumed: `0`.
- Estimated successor code/test effort: `20–40 engineering minutes` to bind an explicit lifecycle and direction derivation, unmeasured.
- Estimated distinct browser verification: `10–15 verifier minutes`, unmeasured.
- Estimated operator burden under the admission gate: `0 minutes`; any manual ferry is a failed route.

## Strongest objection

The existing TAGS pointer adapter is designed for pointer activation, not directional swipe recognition. Reusing its release callback for 2048 could collapse a spatial motion into a click-like event and encode the wrong interaction semantics. This objection is valid. It is why the decision is `REVISE`, not `ADMIT`: the useful finding is the explicit edge/lifecycle primitive, while direction derivation and product gesture choice remain unbound.

## Falsifier

This card is falsified or superseded by either:

- official exact-version documentation/source showing that the selected MediaPipe Web result includes a stable logical gesture identity or once-per-gesture event contract; or
- an exact successor implementation and tests showing a different producer/lifecycle contract that satisfies repeated-frame, duplicate-delivery, cancellation, later-distinct-gesture, and fallback regressions.

It expires immediately on package/model major-version change, TAGS adapter blob change, bridge blob change, or successor producer-binding change.

## Verifier

- Structural: S04 may confirm exact package/model/source/blob bindings and that the claim ceiling excludes MediaPipe-provided exactly-once semantics.
- Runtime: a distinct browser-capable nonproducer must replay repeated frame samples, hold/release, cancellation, and two later distinct same-direction gestures against the exact successor bytes.
- S08, S09, the bridge producer, and the successor producer do not grade the runtime result.

## Consumer

- Immediate decision consumer: S09/S02 admission path for any nonretroactive 2048 successor.
- Implementation consumer: exact WorkItem `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR` if admitted.
- Required consumed classification: `MEDIAPIPE_FRAME_RESULTS_REQUIRE_EXPLICIT_EDGE_OWNER`.
- Fitness remains `0` until an exact WorkItem consumes this card and records ConsumerAck.

## Expiry

`2026-08-09T12:27:02Z`, or immediately upon package/model major-version change, TAGS adapter/bridge blob change, or successor producer-binding change, whichever occurs first.
