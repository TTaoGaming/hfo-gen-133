---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T22:26:36Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: interaction_input_adapters
question: Can the 2048 gesture successor infer user-relative left/right from MediaPipe normalized image coordinates, front-camera facingMode, or handedness without an explicit mirror-transform owner?
decision: REVISE
classification: TAGS_HORIZONTAL_DIRECTION_REQUIRES_EXPLICIT_MIRROR_COORDINATE_OWNER
fitness_credit: 0
fitness_condition: exact successor WorkItem ConsumerAck plus distinct digest-bound browser verdict
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
sealed: false
---

# S08 evidence card — TAGS mirror and coordinate ownership

## Decision

**REVISE — bind one explicit source-to-control coordinate transform before deriving horizontal direction. Do not infer mirroring from `facingMode: "user"`, a handedness label, or the appearance of the camera preview.**

The current MediaPipe Hand Landmarker Web guide defines landmark `x` and `y` as normalized **image coordinates**. The media-capture specification defines `facingMode: "user"` as a source facing the user; it does not define whether application-visible frames or a rendered preview are mirrored. CSS transforms can separately modify visual rendering after layout. The exact TAGS adapter maps `sample.x` directly to `clientX` and exposes no mirror/orientation field. Therefore a visually mirrored preview can disagree with the raw control plane: a user-visible movement to screen-right can have a negative raw-image `dx`, and an overlay can appear on the opposite side unless one component owns the transform.

## Self-probe and changed edge

- Native task inventory exposed enabled task `6a526109ba348191b5f23ad3172ad568`; expected and observed IDs match.
- Available surfaces used: native task readback, authenticated GitHub search/fetch/create/readback, primary public web research, authenticated Slack pointer post.
- Changed uncertainty: the prior normalized-coordinate card required mirroring/orientation ownership but did not resolve whether camera-facing or handedness metadata could safely supply it. Current primary contracts do not provide that binding.
- No task mutation, account creation, terms acceptance, outreach, application, purchase, spend, deployment, merge, publication, private-data use, model download, or code/test mutation occurred.

## Exact candidate bindings

1. **TAGS adapter under review**
   - Repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - Path: `prototypes/spatial-input-adapter.js`
   - Git blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
   - Exact behavior: `clientX = sample.x * viewport.width`; `clientY = sample.y * viewport.height`
   - Missing binding: no `mirrorX`, source orientation, preview transform, or declared control-coordinate semantic.

2. **Current camera prototype inspected for integration context**
   - Repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - Path: `prototypes/simple-pipeline.html`
   - Git blob: `3ddcf4802eba6dfcb2a82a65516dc606e34446ab`
   - Exact behavior: requests video width/height only; no `facingMode` or explicit mirror contract is bound.

3. **Upstream task family inherited from the active successor packet**
   - Package candidate: `@mediapipe/tasks-vision@0.10.35`
   - Task surface: Hand Landmarker / normalized image landmarks
   - Model asset: still unbound; no model asset is admitted by this card.

4. **Conditional implementation consumer**
   - WorkItem: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR`
   - Current controlling application seam: `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc`

## Dated primary sources — accessed 2026-08-02

1. Google AI Edge, **Hand landmarks detection guide for Web**, last updated 2026-05-28 UTC. It states that output landmarks are in image coordinates and that `x`/`y` are normalized by image width/height.  
   https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker/web_js
2. W3C, **Media Capture and Streams**, current Candidate Recommendation Draft. `facingMode` describes the direction a camera faces; `user` means facing toward the user.  
   https://www.w3.org/TR/mediacapture-streams/
3. W3C, **CSS Transforms Module Level 1**. CSS transforms affect visual rendering and establish transformed coordinate systems after sizing/positioning.  
   https://www.w3.org/TR/css-transforms-1/
4. Google MediaPipe legacy Hands documentation/source, explicitly marked as superseded by the newer Solutions task. It historically assumed mirrored input for handedness and instructed applications to swap handedness when input was not mirrored. This is a warning against treating handedness as a current universal mirror contract, not a claim about current Tasks Web behavior.  
   https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/hands.md
5. Exact TAGS adapter bytes.  
   https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/spatial-input-adapter.js

## Supported claims

- Current Hand Landmarker Web output uses normalized image coordinates; the documented coordinate owner is the input image, not the user's perceived mirrored preview.
- `facingMode` identifies camera direction relative to the user. The inspected standard does not make it a horizontal-mirroring flag.
- CSS can transform the rendered preview independently of the raw sample values passed into the TAGS adapter.
- The exact TAGS adapter performs a direct normalized-image-to-viewport mapping and has no explicit mirror/orientation configuration.
- **Inference:** if a preview is horizontally mirrored while the control samples remain in raw image coordinates, user-relative horizontal direction and overlay placement can invert unless the source-to-control transform is applied exactly once.
- Handedness is semantic classification, not a safe substitute for a coordinate transform. Legacy MediaPipe documentation itself made handedness dependent on an input-mirroring assumption.

## Excluded claims

- No claim that all browsers mirror front-camera previews, or that any browser must do so.
- No claim that current MediaPipe Tasks Web inherits the legacy Hands mirrored-handedness assumption; the current guide inspected here does not state that contract.
- No claim that `facingMode: "user"` is currently present in TAGS; the inspected prototype does not request it.
- No claim that the existing TAGS candidate has demonstrated a runtime left/right failure on a named browser/device.
- No claim that raw camera-image left/right is intrinsically wrong. It is valid if the product explicitly chooses camera-image semantics and renders feedback in the same plane.
- No performance, accuracy, accessibility, compatibility, demand, distribution, revenue, deployment, or publication claim.
- No distinct verifier verdict and no ConsumerAck.

## Required successor gate

One exact producer must own and persist the coordinate contract:

- `input_plane`: normalized source-image coordinates;
- `control_semantics`: `USER_VISIBLE_PREVIEW` or `RAW_CAMERA_IMAGE`;
- `mirror_x`: explicit boolean or equivalent matrix, never inferred from handedness;
- `rotation`: explicit source-to-control rotation/orientation rule;
- transform order and ownership: apply exactly once before displacement/direction classification;
- direction derivation: use start and terminal samples in the same transformed normalized plane;
- ambiguous/sub-threshold motion: cancel, with zero bridge submits.

Minimum deterministic corpus: identical physical traces represented as unmirrored and mirrored input pairs must yield the declared user-relative direction; applying the transform twice must fail a negative control; changing handedness while preserving coordinates must not flip direction.

## License / terms uncertainty

- Google MediaPipe SDK/repository metadata identifies Apache-2.0; Google documentation content is CC BY 4.0 and code samples Apache-2.0.
- The selected model asset remains separately uninspected for exact version, provenance, redistribution terms, and third-party notices.
- The TAGS repository/root license remains unresolved in the current research lane. This card analyzes exact bytes but grants no copying, redistribution, or publication clearance.
- W3C specifications were used as reference contracts only; no specification text or code is imported into a product artifact.

## Cost and operator-minute estimate

- Research spend: `$0`.
- Operator minutes consumed: `0`.
- Estimated successor implementation: `10–20 worker engineering minutes` for one explicit transform field/matrix and deterministic mirrored/unmirrored tests, unmeasured.
- Estimated distinct browser verification: `10–15 verifier minutes`, unmeasured.
- Operator relay allowance: `0`; manual ferry is not a valid verifier route.

## Strongest objection

A horizontal mirror multiplies every `dx` by `-1`, but the bridge only needs a consistent direction, so the team could simply choose raw-image semantics and avoid extra configuration. That objection is correct **only if** the preview, cursor feedback, instructions, and expected game direction all use the same raw-image plane. The current candidate does not state that product choice, and camera UIs commonly render a self-view transform independently. The missing artifact is not necessarily a mirror operation; it is an explicit owner and declared semantic so the transform cannot be omitted, guessed, or applied twice.

## Falsifier

This `REVISE` is falsified or superseded if either:

1. current exact-version official MediaPipe/Web contracts expose a stable source-to-user-visible coordinate/mirroring flag that the exact adapter consumes without another transform; or
2. an exact successor digest declares raw-image semantics and a distinct browser-capable nonproducer returns `STOOD` on mirrored/unmirrored, front/rear, double-transform negative-control, handedness-invariance, cancellation, and unchanged keyboard/touch regressions, followed by named ConsumerAck.

It falls to `RETIRE` if no admissible successor and reachable distinct verifier exist by the controlling deadline.

## Verifier

- Structural: S04 confirms exact adapter/package/model/source bindings, one transform owner, transform order, claim ceiling, test corpus, rollback, expiry, and no handedness/facingMode inference.
- Runtime: a distinct browser-capable nonproducer replays deterministic mirrored/unmirrored traces against the exact successor digest and returns digest-bound `STOOD | FELL`.
- S08, S09, the successor producer, and the bridge producer do not grade the runtime result.

## Consumer

- Immediate decision consumers: S02 admission/backlog owner and S03 reducer/router.
- Conditional implementation consumer: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR`.
- Required consumed classification: `TAGS_HORIZONTAL_DIRECTION_REQUIRES_EXPLICIT_MIRROR_COORDINATE_OWNER`.
- Fitness remains `0` until the exact WorkItem records ConsumerAck after a distinct verdict on the same successor digest.

## Expiry

`2026-08-09T07:28:20Z` — the existing controlling successor deadline, not extended by this card — or immediately upon adapter blob, package/model, camera-source binding, preview transform, control semantic, verifier route, or consumer change.
