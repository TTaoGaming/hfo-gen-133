---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-04T04:33:12Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: interaction_input_adapters
question: After a held pinch is cancelled by tracking loss or another terminal fault, can the exact TAGS adapter treat reacquisition of the still-pinched hand as a second activation without observing a release?
decision: REVISE
fitness_credit: 0
fitness_condition: exact WorkItem consumption and ConsumerAck only
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
sealed: false
---

# S08 evidence card — tracking-loss cancellation requires release-to-rearm

## Decision

**REVISE — a cancelled held cycle must enter `REQUIRE_RELEASE` (or an equivalent neutral-wait state). The exact adapter currently clears `pinchHeld`; a reacquired sample that remains below the down threshold can therefore create a second `pointerdown` without any observed physical release.**

This is a state-machine boundary, not evidence that real hardware frequently exhibits the trace. The safe default for the one-activation-edge contract is: cancel the old cycle, emit no command, suppress every new begin while the signal remains pinched, and re-arm only after a valid neutral/released sample.

## Self-probe and changed question

- Expected and observed carrier task ID: `6a526109ba348191b5f23ad3172ad568`; exact match.
- Authenticated GitHub identity: `TTaoGaming`; canonical repository default branch and requested branch both resolve to `agent/gen133-bootstrap-20260730`.
- Surfaces used: authenticated GitHub exact source/claim/recent-state reads and Git-first write/readback; current primary web documentation; authenticated Slack channel read and one pointer after Git readback.
- Changed queue edge: the newest consumed interaction invariant now requires one explicit `BEGIN / HELD / COMMIT-or-CANCEL` owner and zero per-frame commands. The prior S08 MediaPipe card established that need but did not inspect whether cancellation safely prevents a false second `BEGIN` during still-pinched reacquisition.
- No task mutation, source implementation, test execution, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, or private-data use occurred.

## Exact candidate and bounded trace

### Adapter bytes

- Repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
- Path: `prototypes/spatial-input-adapter.js`
- Blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- Thresholds: `pinchDownThreshold=0.35`; `pinchUpThreshold=0.55`
- Relevant state: `pinchHeld`, `activeTarget`, `lastPoint`, `cancellationPending`, `armed`

### Exact state path

1. A valid sample with `pinch <= 0.35` while `pinchHeld=false` sets `pinchHeld=true` and emits `pointerdown`.
2. Invalid tracking while held creates `pointercancel`; the terminal path calls `clearCycle()`.
3. `clearCycle()` sets `pinchHeld=false` and does not retain a release-required state.
4. The next valid sample, if the physical hand is still pinched and remains `<= 0.35`, satisfies the begin condition again and emits another `pointerdown`.

The same premature re-arm shape applies when a held cycle is cleared through target loss, reset, or disarm/re-arm. The code does not need to emit an activation callback on the cancelled cycle for this to matter: two begins for one uninterrupted physical hold violate the declared edge-owner model and can leak into a future directional producer if begin/terminal ownership is reused carelessly.

## Current external contract

- Candidate classifier package: `@mediapipe/tasks-vision@0.10.35`, stable `latest` observed 2026-08-04; repository/tag family `google-ai-edge/mediapipe`.
- Google's current Web guide documents frame-by-frame video recognition. It states that hand-presence or tracking-confidence failure can trigger palm detection again; it does not bind reacquired results to a persistent physical-activation identity.
- W3C Pointer Events Level 4 defines `pointercancel` as termination/suppression of a pointer stream and `pointerdown` as transition into the active-buttons/contact state. Cancellation is therefore not evidence that the hand became physically neutral before a synthetic producer emits a new down.

Primary sources accessed 2026-08-04:

1. Exact TAGS adapter: https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/spatial-input-adapter.js
2. Google AI Edge Gesture Recognizer Web guide, updated 2026-05-28: https://developers.google.com/edge/mediapipe/solutions/vision/gesture_recognizer/web_js
3. Google AI Edge Gesture Recognizer options/API: https://developers.google.com/edge/api/mediapipe/python/mp/tasks/vision/GestureRecognizerOptions
4. Google AI Edge Gesture Recognizer result API: https://developers.google.com/edge/api/mediapipe/js/tasks-vision.gesturerecognizerresult
5. W3C Pointer Events Level 4 Working Draft, 2026-05-22: https://www.w3.org/TR/2026/WD-pointerevents4-20260522/
6. Official npm package metadata: https://www.npmjs.com/package/@mediapipe/tasks-vision
7. Prior S08 frame-result/edge-owner card: https://github.com/TTaoGaming/hfo-gen-133/blob/15a6f0ada99d73ac2aae07d05c8e9977d5f50c64/projects/spatial-app-factory/research/20260802T122702Z_S08_MEDIAPIPE_FRAME_RESULTS_TAGS_PINCH_EDGE_BOUNDARY_EVIDENCE_CARD.md
8. Current Snake successor claim, acceptance item 8: https://github.com/TTaoGaming/hfo-gen-133/blob/c72a290566711418e566f9c81af3bf32836e05db/projects/spatial-app-factory/claims/20260804T020604Z_SPATIAL_FACTORY_HTML5_SNAKE_REPEAT_FILTER_SUCCESSOR.claim.yaml

## Required revision

For any successor that reuses this lifecycle:

1. Add explicit state `REQUIRE_RELEASE` / `CANCELLED_WAIT_NEUTRAL` when a cycle that had begun is cancelled by invalid tracking, target loss, reset, or disarm.
2. In that state, valid still-pinched samples emit zero `pointerdown`, zero activation, and zero `requestDirection` calls.
3. Re-arm only after at least one valid sample with `pinch >= pinchUpThreshold`; a stricter multi-sample neutral rule may be evaluated but is not established by this card.
4. After re-arm, a later down-threshold crossing may create exactly one fresh `BEGIN`.
5. Preserve the distinction between dropout before any begin and cancellation after a held begin; this card does not require neutral lockout when no cycle existed.
6. Deterministically test at 8 and 60 fps:
   - `DOWN -> invalid -> still DOWN` = one begin, one cancel, zero commit, zero second begin;
   - `DOWN -> invalid -> still DOWN -> UP -> DOWN` = two begins total, with the second only after neutral re-arm;
   - equivalent target-loss, reset, and disarm/re-arm traces;
   - cancellation creates zero latent direction command.

A bounded grace-window resume could replace release-to-rearm only if one exact producer proves continuity without emitting a second begin. The currently bound MediaPipe result surface exposes no stable logical activation ID, so that alternative is not admitted here.

## Supported claims

- The exact TAGS bytes clear held state after terminal cancellation.
- The exact next-sample condition can emit a new `pointerdown` while the physical input is still below the down threshold.
- MediaPipe documents tracking/detection fallback and per-run results, not a persistent logical activation identity across reacquisition.
- `pointercancel` terminates a pointer stream but is not synonymous with an observed physical release.
- A release-to-rearm state closes this specific false-second-edge trace without requiring timeout deduplication.

## Excluded claims

- No claim about the real-world frequency of tracking loss, reacquisition timing, browser behavior, camera quality, or model accuracy.
- No claim that one neutral sample is ergonomically optimal; multi-sample hysteresis remains a measurement question.
- No claim that pinch is the correct Snake or 2048 product gesture.
- No runtime, accessibility, latency, compatibility, user-demand, buyer, revenue, deployment, publication, or production-readiness claim.
- No implementation authorization, S04 pass, distinct verifier verdict, ConsumerAck, or completion claim.
- The current Snake claim is separately blocked by its newer source-pin contradiction; this card does not edit or revive that claim.

## License / terms uncertainty

- `@mediapipe/tasks-vision@0.10.35` and the official MediaPipe repository identify Apache-2.0 for SDK code.
- A top-level `LICENSE` was not found at the exact TAGS commit through the available repository path read, and the inspected README excerpt did not supply a repository-wide license grant. Reuse/distribution of TAGS bytes therefore remains `LICENSE_UNBOUND` unless another exact license/provenance artifact is supplied.
- The MediaPipe model asset remains a separate provenance/license gate; this run did not download, install, package, or redistribute it.
- Google's repository privacy notice describes on-device input processing plus performance/utilization metrics and developer consent responsibility. This card authorizes no telemetry, camera access, or user-data processing.

## Cost and operator minutes

- Research spend: `$0`.
- Operator minutes consumed: `0`.
- Estimated producer amendment: `10–25 engineering minutes`, unmeasured.
- Estimated deterministic test work: `15–25 verifier minutes`, unmeasured.
- Estimated distinct browser verification: `10–20 minutes`, unmeasured.

## Strongest objection

A hard release-to-rearm gate can make the interaction feel stuck after a brief false cancellation, especially if the user keeps pinching. A short continuity grace period might provide better UX. That objection is valid, but immediate re-begin is not a safe substitute: a grace strategy must retain the original cycle identity and emit zero second begin. Without a stable identity in the bound classifier surface, release-to-rearm is the lower-risk default.

## Falsifier

This card falls or is superseded if:

- exact successor bytes already retain a post-cancel state that makes the stated trace incapable of producing a second begin/command;
- an exact producer with a documented stable activation identity safely resumes the same cycle across reacquisition and passes the complete deterministic corpus; or
- the consumer selects a different input producer that does not reuse the TAGS lifecycle.

It expires immediately on adapter blob change, producer-state binding change, package/model major-version change, or WorkItem retirement.

## Verifier

- Structural: `S04_STRUCTURAL_PREFLIGHT_VERIFIER` checks the exact state transitions, blob bindings, license ceiling, and test oracle; same-provider weight remains zero.
- Runtime: a distinct browser-capable nonproducer replays synthetic dropout/reacquisition traces at 8 and 60 fps against an exact successor SHA and returns digest-bound `STOOD | FELL`.
- S08, the adapter producer, packet compiler, and successor producer do not grade the runtime result.

## Consumer

- Immediate consumer: the next authorized S02/S06 successor for `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`; the current immutable claim remains blocked and is not modified.
- Required consumed classification: `CANCELLED_HELD_CYCLE_MUST_REARM_ONLY_AFTER_VALID_NEUTRAL`.
- Decision consumer: `S09_STRATEGIC_REASONING_AND_VOTING` after distinct verification.
- Fitness remains `0` until an exact WorkItem cites these exact bytes and records ConsumerAck.

## Expiry

`2026-08-11T04:33:12Z`, or immediate supersession under the falsifier/change conditions above.
