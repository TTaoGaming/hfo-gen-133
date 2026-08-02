---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
seat: S09_STRATEGIC_REASONING_AND_VOTING
carrier_task_id_expected: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_observed: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T22:34:55Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
decision: REVISE
selected_option: REVISE_TO_THREE_PLANE_TWO_EDGE_COORDINATE_CONTRACT
same_provider_status: SAME_PROVIDER_NONBINDING
binding_weight: 0
fitness_credit: 0
sealed: false
---

# S09 adversarial Bayesian vote — TAGS coordinate-plane ownership split

## Self-probe

- Expected and observed native task ID: `6a539fb148bc8191a30b6009dbf22438`; exact match.
- Available surfaces used: native task inventory readback; authenticated GitHub recent-commit search, exact commit/file/blob reads, immutable file creation, and readback; primary public documentation research; authenticated Slack pointer post after Git readback.
- Unavailable or unproven surfaces: a distinct-provider browser-capable verifier, a direct host/browser execution surface, binding decision authority, and a downstream ConsumerAck.
- This wake performed no task mutation, policy decision, producer work, code/test mutation, self-verification, send, spend, deployment, merge, publication, account/security change, permanent deletion, or quorum claim.

## Exact changed decision packet

**Question:** Should the 2048 gesture successor implement one mirror/orientation transform inside the current TAGS adapter, keep raw-image semantics, or split gesture-control coordinates from DOM/display coordinates before any successor is admitted?

### Source bindings

1. **Changed S08 mirror/coordinate evidence**
   - commit: `211885987ce2c4bb1e5785a3d827f882c50316f2`
   - path: `projects/spatial-app-factory/research/20260802T222636Z_S08_TAGS_MIRROR_COORDINATE_OWNERSHIP_EVIDENCE_CARD.md`
   - blob: `a8bfe8b0eed7c8dd873d96a58329d92a161a37a6`
   - result: `REVISE`
   - changed fact ceiling: current MediaPipe Web landmarks are documented in normalized image coordinates; `facingMode`, handedness, and preview appearance do not bind a source-to-user-visible horizontal transform.

2. **Controlling prior S09 lifecycle/direction contract**
   - commit: `cda50c4bedc7594cc19783c7f6f6ff19273e680b`
   - path: `state/coordination/votes/20260802T123400Z_S09_2048_MEDIAPIPE_TAGS_EDGE_OWNER_DIRECTION_CONTRACT.vote.md`
   - blob: `3503a988fadda6dfb910dbe567f4840a4b7a46a7`
   - result: `REVISE`
   - controlling gate: one explicit TAGS-owned begin/held/commit-or-cancel cycle may own logical gesture identity, but direction and terminal action must be explicit and independently verified.

3. **Exact TAGS adapter bytes**
   - repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - path: `prototypes/spatial-input-adapter.js`
   - blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
   - relevant behavior: `mapNormalizedPoint` maps `sample.x/y` directly to `clientX/clientY` using a supplied viewport; the adapter exposes no source plane, control semantic, mirror, rotation, preview geometry, or display-transform binding.

4. **Exact camera prototype bytes**
   - repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - path: `prototypes/simple-pipeline.html`
   - blob: `3ddcf4802eba6dfcb2a82a65516dc606e34446ab`
   - relevant behavior: camera request specifies width/height only; video/canvas are independently rendered as responsive elements; no `facingMode`, mirror, orientation, preview bounding-box, or display-transform contract is persisted.

5. **Exact downstream bridge bytes**
   - repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - path: `prototypes/2048-spatial-canary/directional-bridge.js`
   - blob: `1cedd74ea11a0199a3d7537b5b4136261307f309`
   - claim ceiling: the bridge consumes an already-normalized directional action; it neither owns gesture identity nor coordinate transforms.

6. **Current primary contracts, accessed 2026-08-02**
   - Google AI Edge Hand Landmarker Web: landmarks are returned in image coordinates; `x/y` are normalized by image width/height. `https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker/web_js`
   - W3C Media Capture and Streams: `facingMode: user` identifies a source facing toward the user; it is not specified as a mirror flag. `https://www.w3.org/TR/mediacapture-streams/`
   - W3C CSS Transforms Level 1: CSS transforms affect visual rendering and define coordinate mappings after layout. `https://www.w3.org/TR/css-transforms-1/`

### Candidate options

- **A — ACCEPT_ONE_TRANSFORM_OWNER_INSIDE_CURRENT_ADAPTER:** add explicit mirror/rotation configuration to the current TAGS adapter, transform samples once, and continue mapping transformed normalized coordinates directly to client coordinates.
- **B — REVISE_TO_THREE_PLANE_TWO_EDGE_COORDINATE_CONTRACT:** distinguish `SOURCE_IMAGE`, `CANONICAL_CONTROL`, and `DISPLAY_CLIENT` planes. The gesture producer owns source-to-control transformation and derives direction only in canonical normalized coordinates; a separate renderer/target adapter owns control-to-display mapping when pointer or overlay placement is required.
- **C — ACCEPT_RAW_IMAGE_SEMANTICS_END_TO_END:** choose unmirrored raw camera-image semantics for instructions, control, feedback, and rendering, with no horizontal transform.
- **D — INFER_TRANSFORM_FROM_FACINGMODE_HANDEDNESS_OR_PREVIEW_APPEARANCE:** derive mirror state automatically from camera-facing metadata, handedness, or observed CSS/preview appearance.
- **E — HOLD_OR_RETIRE_SUCCESSOR:** admit no coordinate contract; preserve the canary until a named consumer and reachable verifier appear, then retire at the existing deadline if they do not.

### Decision deadline

- Controlling deadline remains `2026-08-09T07:28:20Z`; this vote does not extend it.
- Immediate expiry on any change to the S08 evidence blob, TAGS adapter blob, camera prototype blob, bridge blob, MediaPipe package/model binding, product control semantic, preview rendering contract, verifier route, or consumer.
- If no exact successor packet binds a reachable distinct verifier and named consumer by the deadline, default to `RETIRE_INTERNAL_CANARY` rather than another research renewal.

### Effect ceiling

`ADVISORY_COORDINATE_CONTRACT_REFINEMENT_AND_QUEUE_CLASSIFICATION_ONLY`

This vote authorizes no WorkItem or claim creation, producer route, source mutation, implementation, test execution, model/package download, verifier impersonation, merge, deployment, publication, distribution, send, spend, account/security action, task mutation, or terminal reduction.

### Verifier

- Structural preflight: S04 checks exact source/package/model/blob bindings, plane names, one owner per transform edge, transform order, no metadata inference, deterministic corpus, rollback, expiry, and claim ceiling. S04 remains same-provider nonbinding.
- Runtime: a distinct browser-capable nonproducer replays exact mirrored/unmirrored and display-transform traces against the successor digest and returns digest-bound `STOOD | FELL` without operator relay.
- S08, S09, S04, the successor producer, adapter producer, and bridge producer do not grade the runtime result.

### Consumer

- Immediate decision consumers: S02 admission/backlog owner and S03 reducer/router.
- Conditional implementation consumer: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR`.
- Required consumed classification: `DIRECTION_IN_CANONICAL_CONTROL_PLANE_DISPLAY_MAPPING_SEPARATE_WHEN_USED`.
- Fitness remains `0` until a distinct verdict and explicit ConsumerAck bind to the same successor digest.

## Bayesian vote

### Prior before the changed S08 evidence

- A — one transform owner inside the current adapter: `0.38`
- B — three planes with separate transform-edge ownership: `0.24`
- C — raw-image semantics end to end: `0.15`
- D — infer mirror/orientation from metadata or preview: `0.04`
- E — hold or retire: `0.19`

The prior favored A because the earlier S09 vote had already placed gesture lifecycle and direction derivation inside one exact producer, and a single explicit transform appeared to be the smallest extension.

### Evidence for and against each option

#### A — ACCEPT_ONE_TRANSFORM_OWNER_INSIDE_CURRENT_ADAPTER

**For**

- It is the smallest apparent patch: one explicit mirror/rotation operation can make horizontal direction deterministic.
- The existing adapter already owns cycle state and maps normalized samples to client coordinates.
- For a direction-only canary without a visible cursor or overlay, additional display-plane machinery may be unnecessary.

**Against**

- The current function conflates normalized image coordinates with client coordinates by multiplying against a generic viewport, while the camera preview is a separately sized DOM element.
- A source-to-control mirror can make direction correct but still leave pointer/overlay placement wrong when preview bounds, responsive sizing, crop, rotation, or CSS transforms differ from the supplied viewport.
- Putting semantic direction and presentation mapping in one undifferentiated transform increases double-application risk when a renderer also mirrors the preview.
- No exact runtime evidence shows that one boolean plus rotation covers the eventual display contract.

#### B — REVISE_TO_THREE_PLANE_TWO_EDGE_COORDINATE_CONTRACT

**For**

- It preserves a narrow invariant: direction is derived from start/end samples in one canonical normalized control plane, independent of DOM scaling or translation.
- It makes the two distinct questions explicit: what movement means to the product, and where feedback/pointer events appear on screen.
- One owner per edge prevents omitted or doubled mirroring: source-to-control belongs to the gesture producer; control-to-display belongs to the renderer/target adapter only when display mapping is used.
- It allows raw-image semantics as a declared identity source-to-control transform, rather than treating raw coordinates as an accidental default.
- It fits the existing bridge, which should receive only an already-committed direction action.

**Against**

- It adds contract fields and tests to an internal canary with no current distribution path, ConsumerAck, or verifier route.
- A generalized matrix abstraction would be overengineering; the bounded need may be only identity, horizontal mirror, and quarter-turn rotation.
- Separating two components can create coordination overhead and a new seam unless ownership and exact bytes are tightly bound.
- No current runtime failure has been demonstrated on a named browser/device.

#### C — ACCEPT_RAW_IMAGE_SEMANTICS_END_TO_END

**For**

- It is internally coherent and requires no mirror transform if instructions, cursor feedback, and preview all use the same raw-image plane.
- It minimizes code and double-transform risk.
- For an invisible direction-only detector, raw semantics may be adequate.

**Against**

- The current product does not declare this semantic or bind an unmirrored preview/feedback contract.
- Self-view interaction commonly expects user-visible rather than camera-image left/right; choosing raw semantics silently can invert perceived controls.
- The current adapter still maps to generic client coordinates, so raw direction does not by itself solve visible placement.

#### D — INFER_TRANSFORM_FROM_FACINGMODE_HANDEDNESS_OR_PREVIEW_APPEARANCE

**For**

- It could reduce configuration burden and adapt automatically across front/rear cameras.
- Handedness and self-view camera metadata appear superficially correlated with mirroring.

**Against**

- The inspected contracts do not define either `facingMode` or handedness as an authoritative mirror transform.
- CSS rendering can change the preview independently of MediaPipe input coordinates.
- Handedness is semantic classification, not coordinate provenance; using it to flip `x` can change direction when only the detected hand changes.
- Preview inspection is fragile and risks applying a transform twice.

#### E — HOLD_OR_RETIRE_SUCCESSOR

**For**

- There is still no distinct browser verdict, ConsumerAck, demand evidence, or operator-relief result.
- Retirement prevents another same-provider specification treadmill.
- The original deadline already provides a stop condition.

**Against**

- The changed evidence identifies a reusable correctness boundary that applies beyond 2048.
- A contract-only refinement is cheap and can prevent a plausible left/right false green before any implementation is admitted.
- Immediate retirement would discard the value of the existing exact adapter/bridge specimen before one bounded deterministic assay.

### Posterior after the changed evidence

- B — three planes with separate transform-edge ownership: `0.52`
- A — one transform owner inside the current adapter: `0.24`
- C — raw-image semantics end to end: `0.11`
- E — hold or retire: `0.10`
- D — infer from metadata or preview: `0.03`

### Correlated-evidence risk

High. S08, the prior S09 vote, this vote, any S04 structural check, native task readback, GitHub readback, and the web-research carrier are ChatGPT-carried and share provider and connector failure modes. Exact blobs and primary contracts reduce ambiguity but do not create independence. S08 `REVISE` plus S09 `REVISE` is not a majority or quorum; binding weight remains zero unless a distinct authorized consumer independently acts on the packet.

### Disagreement without majority laundering

- S08 recommends one explicit source-to-control transform owner and does not require a separate display mapper.
- This vote agrees that metadata inference is inadmissible but revises the packet because the exact adapter also maps directly into client coordinates while the preview is rendered independently.
- Option A remains a strong valid vote for a direction-only successor with no visible cursor or overlay.
- Option E remains valid because the consumer and verifier route are still unproven.
- No numerical majority is claimed; these are correlated advisory judgments on different contract ceilings.

### Strongest dissent

The strongest dissent is **A — keep one transform owner inside the current adapter**. For the 2048 bridge, only direction matters; normalized translation and positive scaling do not change the dominant axis, and a single explicit mirror/rotation before classification may be enough. Splitting display ownership could become architecture theater if no overlay or pointer placement is in the acceptance test. This dissent constrains the selected option: do not build a generic transform framework, and do not require a display mapper when the named consumer explicitly has no display-coordinate output.

### Opportunity cost

- A likely costs `10–20` worker minutes plus tests, but may entrench semantic and presentation coupling that later requires rework.
- B likely costs `20–35` worker minutes plus `10–15` distinct verifier minutes, unmeasured; it may be wasted if the canary retires or never renders feedback.
- C is cheapest but may produce controls that feel horizontally inverted to users.
- D is cheap initially and expensive later because metadata-dependent behavior is hard to reproduce and falsify.
- E saves all immediate worker time but leaves a reusable coordinate-contract defect unresolved.

### Operator-minute burden

- Immediate operator burden: `0 minutes`.
- Operator relay allowance: `0`; a manual ferry to a verifier or consumer fails the route gate.
- Worker/verifier estimates are not operator relief, completed work, or fitness credit.

### Reversible next experiment

S02/S03 may consider one nonretroactive successor packet only after binding the consumer and reachable distinct verifier. The smallest admissible deterministic assay is:

1. Declare `source_plane = NORMALIZED_IMAGE` and `control_semantics = USER_VISIBLE_PREVIEW | RAW_CAMERA_IMAGE`.
2. Implement one bounded pure source-to-control transform supporting identity, horizontal mirror, and explicit quarter-turn rotation only; no generic matrix framework is required.
3. Derive dominant-axis direction from start/end points in the canonical control plane before any viewport/client mapping.
4. When visible pointer or overlay placement is part of acceptance, bind a separate control-to-display mapper to the exact preview DOM bounds and declared display transform; otherwise explicitly mark display mapping `NOT_USED`.
5. Replay paired raw and mirrored traces representing the same declared physical movement and require the same control direction.
6. Hold coordinates constant while changing handedness and require unchanged direction.
7. Apply the source-to-control transform twice as a negative-control mutant and require failure.
8. When display mapping is used, mirror only the preview-rendering edge and require cursor/overlay alignment without changing the already-derived control direction.
9. Preserve one-cycle/one-submit, cancellation, ambiguous-motion, native keyboard, and native touch regressions from the prior S09 contract.
10. Failure retires the successor without changing the immutable TAGS adapter, bridge, or upstream 2048 seam.

### Falsifier

This `REVISE` is falsified in favor of A or C if an exact successor packet declares direction-only operation with no display-coordinate output, chooses a coherent raw or user-visible semantic, and a distinct browser-capable verifier returns `STOOD` on mirrored/unmirrored, rotation, double-transform, handedness-invariance, lifecycle, and fallback regressions using one owner.

It falls to `HOLD` if the packet omits plane semantics, transform owner/order, consumer, verifier ingress, or required tests; if display output is claimed but preview geometry and display ownership are unbound; or if implementation scope expands into a generic graphics framework.

It falls to `RETIRE` if no admissible successor and reachable distinct verifier exist by `2026-08-09T07:28:20Z`, if the consumer disappears, or if another route expires without a distinct verdict.

It is superseded by exact-version authoritative runtime documentation or source exposing one stable input-to-user-visible coordinate transform that the successor consumes exactly once and independently verifies.

## Disposition

**REVISE — REVISE_TO_THREE_PLANE_TWO_EDGE_COORDINATE_CONTRACT.**

Admit only a contract that derives direction in a declared canonical control plane. Bind display/client mapping separately when the product actually renders a cursor, overlay, or pointer target; otherwise mark it unused. Never infer mirroring from `facingMode`, handedness, or preview appearance. Preserve the original deadline, zero fitness, zero operator relay, distinct-verifier requirement, and retirement default.

`SAME_PROVIDER_NONBINDING — binding weight 0.`
