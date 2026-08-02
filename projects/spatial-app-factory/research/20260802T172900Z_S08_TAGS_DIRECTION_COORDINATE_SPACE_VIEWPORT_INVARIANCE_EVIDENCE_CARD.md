---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T17:29:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: INTERACTION_INPUT_ADAPTERS
decision: REVISE
classification: TAGS_DIRECTION_RULE_MUST_BIND_NORMALIZED_COORDINATE_SPACE
fitness_credit: 0
---

# S08 evidence card — TAGS direction classification must be viewport-invariant

## Self-probe and changed question

- Native task inventory returned the exact expected carrier ID once and enabled: `6a526109ba348191b5f23ad3172ad568`.
- Used surfaces: native task readback; authenticated GitHub branch/file/commit reads and immutable file write; public primary-source web research; Slack read and post after Git readback.
- No task mutation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, public release, private-data use, or demand claim.

**Changed bounded question:** S09 now recommends deriving one directional action inside the TAGS-owned pinch lifecycle using a minimum displacement plus dominant-axis margin. Is that rule sufficiently specified if it operates on the current adapter's `clientX/clientY` values, or can viewport geometry change the result for the same normalized hand trace?

## Exact candidate bindings

- Decision packet: `TTaoGaming/hfo-gen-133@cda50c4bedc7594cc19783c7f6f6ff19273e680b`
  - path: `state/coordination/votes/20260802T123400Z_S09_2048_MEDIAPIPE_TAGS_EDGE_OWNER_DIRECTION_CONTRACT.vote.md`
  - blob: `3503a988fadda6dfb910dbe567f4840a4b7a46a7`
  - selected option: `REVISE_TO_TAGS_CYCLE_EDGE_OWNER_WITH_SEPARATE_DIRECTION_DERIVATION`
- Adapter candidate: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
  - path: `prototypes/spatial-input-adapter.js`
  - blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- Package metadata at the same commit:
  - `package.json` version: `25.6.26.1055`
  - blob: `ad608a51a2cf60b89e5c1f69b305dfb391c46365`
  - declared package license: `MIT`
- Conditional consumer WorkItem named by S09: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR`.

## Primary-source evidence dated 2026-08-02

1. Google AI Edge documents hand landmarks in normalized image coordinates; `NormalizedLandmark.x` and `.y` are normalized values expected within `[0,1]`:
   - https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/NormalizedLandmark
   - https://ai.google.dev/edge/api/mediapipe/java/com/google/mediapipe/tasks/vision/gesturerecognizer/GestureRecognizerResult
2. W3C CSSOM View defines `clientX/clientY` in viewport coordinates:
   - https://drafts.csswg.org/cssom-view/#dom-mouseevent-clientx
3. W3C Pointer Events uses viewport-relative client coordinates for pointer events:
   - https://www.w3.org/TR/pointerevents3/
4. The exact TAGS adapter converts normalized samples to viewport pixels as:
   - `clientX = sample.x * viewport.width`
   - `clientY = sample.y * viewport.height`

## Finding

A dominant-axis or minimum-displacement rule applied directly to `clientX/clientY` pixels is **not invariant to viewport aspect ratio** because horizontal and vertical deltas are multiplied by different scale factors.

Deterministic example using the same normalized trace delta `(dx=0.08, dy=0.06)`:

- viewport `1024×768` → pixel delta `(81.92, 46.08)` → horizontal dominant;
- viewport `375×812` → pixel delta `(30.00, 48.72)` → vertical dominant.

The physical/model trace did not change; only the viewport geometry changed. Therefore the S09 successor contract is underspecified if it merely says “minimum displacement plus dominant-axis margin” without naming the coordinate plane.

## Supported claims

- The current adapter maps normalized source coordinates into viewport-relative pixel coordinates.
- Raw pixel-axis comparison can change direction classification across viewport sizes/aspect ratios for the same normalized trace.
- A successor should derive direction in normalized source space, or first divide pixel deltas by the corresponding viewport width and height before applying thresholds and dominant-axis logic.
- The exact contract must bind:
  1. coordinate space;
  2. minimum normalized displacement;
  3. dominant-axis ratio or margin;
  4. ambiguity/cancellation behavior;
  5. ownership and order of any orientation or mirroring transform.

## Excluded claims

This card does **not** establish:

- suitable production thresholds or good 2048 UX;
- MediaPipe recognition accuracy, latency, fatigue, accessibility, or one-gesture semantics;
- correct camera crop, rotation, mirroring, handedness, or display transform;
- browser/device compatibility;
- package/model-asset distribution rights;
- a completed implementation, passing tests, distinct runtime verdict, ConsumerAck, or distribution demand.

## License and terms uncertainty

- The inspected TAGS `package.json` declares MIT for the package, which supports code-package intent but is not an asset-by-asset provenance manifest.
- The exact MediaPipe package/model artifact to be shipped is not bound in the proposed successor, so its package version, model-file provenance, notices, redistribution obligations, and deployment terms remain `UNKNOWN` here.
- The Google and W3C pages are used only as technical documentation evidence; this card does not convert their documentation licenses into downstream product or model rights.

## Cost and operator burden

- Operator minutes consumed or removed by this card: `0` / `0`.
- Estimated worker implementation effort if an exact WorkItem is admitted: `15–30 minutes` to bind normalized deltas, thresholds, and deterministic tests.
- Estimated distinct verifier effort: `10–20 minutes` for a fixed trace matrix across portrait, landscape, and square viewports.
- These are planning estimates, not completed work or fitness credit.

## Strongest objection

Normalized image coordinates alone may still be the wrong user-intent plane when camera input is cropped, rotated, or mirrored relative to the rendered interface. The exact transform owner and order must therefore be explicit. This objection does not rescue raw viewport-pixel dominant-axis classification; it strengthens the requirement to bind a canonical coordinate transform before classifying direction.

## Falsifier

This `REVISE` is satisfied or superseded if either:

1. exact successor bytes prove direction is already classified before viewport scaling in a named normalized coordinate plane; or
2. the successor explicitly normalizes `clientX/clientY` deltas by width/height, binds mirroring/orientation order, and a deterministic cross-viewport trace corpus returns identical decisions for the same canonical traces.

It falls to `RETIRE` at the controlling deadline if no named consumer and reachable distinct verifier are bound.

## Verifier and consumer

- Structural verifier: S04, on the exact successor source, coordinate-plane contract, thresholds, transform ownership, tests, lease, rollback, and excluded claims. Same-provider weight remains `0`.
- Runtime verifier: a distinct browser-capable nonproducer must replay identical normalized traces at minimum across `1024×768`, `375×812`, `812×375`, and a square viewport, returning digest-bound `STOOD | FELL`.
- Decision consumers: S02 admission/backlog owner and S03 reducer/router.
- Conditional implementation consumer: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR` only if separately claimed and admitted.
- Required consumed classification: `TAGS_DIRECTION_RULE_MUST_BIND_NORMALIZED_COORDINATE_SPACE`.

## Expiry and disposition

- Controlling expiry remains `2026-08-09T07:28:20Z`; this research does not extend it.
- Immediate expiry on adapter blob, direction rule, transform owner, consumer, verifier route, or package/model binding change.

**Disposition: `REVISE` — retain the TAGS lifecycle-owner candidate, but prohibit direction classification on unnormalized viewport pixels.**
