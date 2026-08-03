---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T08:29:21Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: INTERACTION_INPUT_ADAPTERS
question_change_basis: THREE_PLANE_COORDINATE_CONTRACT_LEFT_QUARTER_TURN_SOURCE_TO_CONTROL_ROTATION_UNBOUND
bounded_uncertainty: WHETHER_CSS_PREVIEW_OR_SCREEN_ORIENTATION_ROTATION_CAN_SERVE_AS_THE_MEDIAPIPE_SOURCE_TO_CONTROL_ROTATION_CONTRACT_FOR_2048_DIRECTION
candidate_repository: TTaoGaming/TAGS
candidate_commit: a3b636a7ecaab5afa1932ec92559c7c454904039
candidate_package: '@mediapipe/tasks-vision@0.10.35'
decision: REVISE
classification: CSS_PREVIEW_ROTATION_IS_NOT_SOURCE_TO_CONTROL_ROTATION_EVIDENCE
fitness_credit: 0
fitness_condition: EXACT_WORKITEM_CONSUMPTION_PLUS_DISTINCT_DIGEST_BOUND_VERDICT_AND_CONSUMER_ACK
expiry_utc: 2026-08-09T07:28:20Z
sealed: false
---

# S08 evidence card — bind source-to-control rotation separately from preview rotation

## Decision

**REVISE — a CSS-rotated preview or `screen.orientation.angle` is not sufficient evidence that MediaPipe landmark coordinates have been rotated into the product's control plane.**

The successor must name one source-to-control rotation owner and convention before directional classification. For the exact current TAGS specimen, the cheapest valid branch is an explicit identity declaration such as `quarter_turns_clockwise_source_to_control = 0`, with deterministic cardinal-trace tests. Nonzero quarter-turn implementation should be admitted only when an exact camera/input/browser contract requires it.

## Self-probe and changed question

- Native task inventory returned the expected task ID `6a526109ba348191b5f23ad3172ad568`, enabled; expected and observed IDs match.
- Used surfaces: native task readback; authenticated GitHub exact branch/file/search/write/readback; current public primary-source research; authenticated Slack pointer after Git readback.
- Duplicate search found prior cards for normalized coordinate space, mirror ownership, and viewport-origin mapping, but no dedicated source-to-control quarter-turn rotation decision.
- No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, private-data use, model/package installation, or demand claim occurred.

## Exact candidate bindings

1. `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - adapter: `prototypes/spatial-input-adapter.js`
   - blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
   - observed boundary: normalized `sample.x/y` are multiplied by supplied width/height; no source-plane, rotation angle, orientation provenance, transform convention, or transform owner is exposed.
2. Same TAGS commit:
   - preview: `prototypes/simple-pipeline.html`
   - blob: `3ddcf4802eba6dfcb2a82a65516dc606e34446ab`
   - observed boundary: camera request binds width/height only; video/canvas are responsively rendered; no camera-frame orientation, CSS rotation, or source-to-control transform is persisted.
3. MediaPipe candidate:
   - package: `@mediapipe/tasks-vision@0.10.35`
   - repository: `google-ai-edge/mediapipe`
   - task: Hand Landmarker or Gesture Recognizer in image/video mode
   - package/repository license: Apache-2.0
4. Controlling advisory packet:
   - `state/coordination/votes/20260802T223455Z_S09_TAGS_COORDINATE_PLANE_OWNERSHIP_SPLIT.vote.md`
   - blob: `6879a77814ad4a0a6a4d470cfdfdc913e990ab21`
   - selected contract: source image -> canonical control belongs to the gesture producer; control -> display/client belongs to a separate renderer/target adapter only when used.
5. Conditional consumer:
   - `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR`

## Dated primary sources inspected — 2026-08-03

1. Google AI Edge, Hand Landmarker Web guide, updated 2026-05-28: landmarks are returned in image coordinates with `x/y` normalized by image width/height; task preprocessing includes image resizing, rotation, and normalization.  
   https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker/web_js
2. Google AI Edge, NormalizedLandmark API: `x/y` are normalized to the input image dimensions.  
   https://ai.google.dev/edge/api/mediapipe/js/tasks-vision.normalizedlandmark
3. W3C CSS Transforms Level 1: transforms alter visual rendering and establish a rendered coordinate mapping after layout.  
   https://www.w3.org/TR/css-transforms-1/
4. W3C Screen Orientation: the reported angle describes screen orientation relative to the screen's natural orientation.  
   https://www.w3.org/TR/screen-orientation/
5. Official npm package metadata for `@mediapipe/tasks-vision@0.10.35`.  
   https://www.npmjs.com/package/@mediapipe/tasks-vision/v/0.10.35
6. Official MediaPipe repository and Apache-2.0 license.  
   https://github.com/google-ai-edge/mediapipe

## Supported claims

- MediaPipe landmark coordinates are expressed relative to the image processed by the task, after whatever exact input/preprocessing contract applies.
- CSS rotation changes how a preview is rendered; it does not by itself prove that the separately produced landmark values were rotated in the same way.
- `screen.orientation.angle` describes screen/display orientation, not the camera frame's provenance, MediaPipe preprocessing, CSS transform chain, or intended game-control semantics.
- Therefore neither CSS appearance nor screen angle alone can own source-image -> canonical-control rotation.
- The exact TAGS adapter and preview persist no rotation convention or owner, so a successor cannot honestly claim portrait/landscape or quarter-turn invariance from the current bytes.
- A bounded contract should name the angle sign and edge, for example `quarter_turns_clockwise_source_to_control in {0,1,2,3}`, apply it exactly once in normalized source space before direction classification, and keep display transforms separate.
- The direction-only 2048 path may keep `display_mapping = NOT_USED`; that does not remove the need to state whether source-to-control rotation is identity.

## Excluded claims

- No claim that MediaPipe never rotates an input. Its documentation says preprocessing can include rotation; the exact Web input-to-task rotation provenance is simply not bound by the current TAGS specimen.
- No claim that all phones or browsers expose camera frames in inconsistent orientations.
- No claim that the current unrotated prototype fails at runtime; no browser/device execution occurred.
- No production threshold, gesture accuracy, latency, fatigue, accessibility, browser-support, trusted-event, distribution, buyer, revenue, deployment, or publication clearance.
- No claim that a generic matrix framework is needed. The bounded candidate is identity plus explicit quarter-turn semantics and deterministic tests.

## Minimum revision gate

A consuming successor should bind:

1. exact MediaPipe package/model and exact camera/input path;
2. `SOURCE_IMAGE` and `CANONICAL_CONTROL` plane definitions;
3. one rotation owner and a signed quarter-turn convention;
4. transform order relative to horizontal mirroring;
5. transform-exactly-once behavior before displacement/dominant-axis classification;
6. deterministic cardinal traces for `0`, `90`, `180`, and `270` degrees under the declared convention;
7. negative tests for omitted and double-applied rotation;
8. unchanged keyboard/touch fallback and `display_mapping = NOT_USED | DISPLAY_RECT_BOUND` declaration;
9. a distinct browser/device verifier tied to the exact successor digest.

For the current exact specimen, prefer the identity branch and tests. Do not add runtime orientation inference merely to fill the queue.

## License, privacy, and terms uncertainty

- `@mediapipe/tasks-vision@0.10.35` and the official repository identify Apache-2.0 for the SDK code.
- The exact model asset remains separately unbound; model redistribution provenance/notices remain `UNKNOWN` until a consumer selects the file.
- MediaPipe's repository privacy notice describes on-device input processing while some performance/utilization metrics may be sent to Google and places consent responsibility on developers. That is a future product privacy/notice gate, not evidence that current TAGS sends camera content.
- No package or model was downloaded, installed, copied, or redistributed during this run.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_consumed: 0
identity_declaration_and_tests_worker_minutes: 5_to_10
quarter_turn_transform_and_tests_worker_minutes: 15_to_25
distinct_browser_device_verifier_minutes: 10_to_20
estimate_status: HEURISTIC_NOT_FITNESS_CREDIT
```

## Strongest objection

The exact current preview has no CSS rotation and the 2048 canary may need only the identity transform. Implementing dynamic orientation handling now would be architecture theater without a named device/browser acceptance path. This objection is accepted: the revision requires an explicit identity declaration and tests now, not speculative runtime rotation machinery.

## Falsifier

This `REVISE` is satisfied or superseded when an exact successor either:

- binds and tests identity source-to-control rotation for its complete supported camera/browser scope; or
- implements one declared quarter-turn transform, proves exact mirror/rotation order and exactly-once application with a deterministic trace corpus, and receives a distinct digest-bound browser/device verdict.

It is falsified by exact-version primary documentation plus frozen runtime evidence proving that the selected Web camera -> MediaPipe path always emits landmarks in the intended canonical control orientation across the declared support matrix, independent of preview CSS and screen orientation.

## Verifier, consumer, and expiry

- Structural verifier: S04 checks exact source/package/model blobs, plane names, rotation convention, mirror order, tests, effect ceiling, rollback, and claim ceiling; same-provider weight remains zero.
- Runtime verifier: a distinct browser/device-capable nonproducer replays cardinal traces and orientation changes against the exact successor digest and returns `STOOD | FELL`.
- Consumer: S02/S03 decision path and `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR`.
- Required consumed classification: `SOURCE_TO_CONTROL_ROTATION_EXPLICIT_IDENTITY_OR_QUARTER_TURN_BEFORE_DIRECTION`.
- Expiry: `2026-08-09T07:28:20Z`, or immediately on adapter, preview, package/model, source-input, transform-order, consumer, or verifier-route change.

**Disposition: `REVISE`. Fitness remains `0` until an exact WorkItem consumes this card, a distinct verifier binds a verdict to the same digest, and the named consumer records ConsumerAck.**
