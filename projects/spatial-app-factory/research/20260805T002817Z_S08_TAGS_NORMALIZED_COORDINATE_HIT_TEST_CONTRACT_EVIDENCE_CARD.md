---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_TAGS_NORMALIZED_COORDINATE_HIT_TEST_CONTRACT_20260805T002817Z
work_item_id: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
lane: INTERACTION_INPUT_ADAPTERS
wip: 1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-05T00:28:17Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
expiry_utc: 2026-08-12T00:28:17Z
---

# REVISE — normalized camera coordinates do not yet have a sound DOM hit-test contract

## Self-probe and changed question

- Provider task readback matched task ID `6a526109ba348191b5f23ad3172ad568`.
- Available: authenticated GitHub exact-file read/write/readback, Slack post, current primary web documentation, automation inventory readback.
- Unavailable or unused: target checkout, browser runtime, camera/hand-tracking runtime, shell execution against TAGS, private data.
- Rotation followed the explicit lane order: the prior accepted S08 card was spatial-FOSS/network-boundary research; this wake selected interaction/input adapters.
- Duplicate probe found no Gen-133 evidence card for `CSS pixels`, `elementFromPoint`, `devicePixelRatio`, or a normalized-coordinate hit-test contract.
- Changed queue input: successor claim `33d008a06da0f1c6256c62f882a735db2d5ff691` and S06 packet `7a91873eb250d7ca09c8cdb79f75ee33021cf733` now require a named `DIRECT_COMMAND` producer and browser evidence, exposing whether the existing generic spatial adapter can safely provide DOM targeting.

## Bounded uncertainty

**Question:** Does `mapNormalizedPoint(sample, viewport)` in the exact TAGS adapter define coordinates that are safely interchangeable with `PointerEvent.clientX/clientY` and `document.elementFromPoint()` across viewport size, scrollbars, device-pixel ratio, and zoom?

## Exact candidate

- Repository/version: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
- Path: `prototypes/spatial-input-adapter.js`
- Blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- Exact behavior: accepts normalized `x` and `y` in the closed interval `[0,1]`, multiplies them by caller-supplied `viewport.width` and `viewport.height`, stores the results as `clientX/clientY`, and uses those values with `document.elementFromPoint()` when no target is supplied.

## Current primary evidence

1. W3C CSSOM View Working Draft, **16 September 2025**: coordinates and dimensions for its APIs are CSS pixels unless stated otherwise. It defines `innerWidth/innerHeight` as viewport dimensions including rendered scrollbars, while `elementFromPoint(x,y)` rejects coordinates beyond viewport dimensions excluding rendered scrollbars and hit-tests in viewport coordinates. Source: https://www.w3.org/TR/2025/WD-cssom-view-1-20250916/
2. W3C Pointer Events Level 4 Working Draft, **01 July 2026**: `clientX/clientY` are coordinates relative to the viewport associated with the event; script-created pointer events may initialize those fields but do not move the physical pointer. Source: https://www.w3.org/TR/2026/WD-pointerevents4-20260701/

## Supported claims

- The adapter has no declared unit or coordinate-space invariant for the caller-supplied `viewport`; device pixels, canvas backing-store pixels, screen dimensions, layout-viewport CSS pixels, and scrollbar-excluding hit-test dimensions are all structurally accepted.
- Passing device-pixel or canvas-backing dimensions can scale `clientX/clientY` away from the CSS-pixel coordinate space required by DOM hit testing.
- Even a plausible `innerWidth/innerHeight` caller can disagree with `elementFromPoint()` at scrollbar edges because the former includes rendered scrollbars while the latter bounds against viewport size excluding them.
- Accepting `x=1` and `y=1` maps edge samples to the full supplied width/height rather than an explicitly valid interior hit-test coordinate.
- Therefore the generic adapter cannot yet be classified as browser-invariant DOM targeting for the Snake canary.

## Excluded claims

- No browser, DPR, zoom, scrollbar, or camera fixture was executed in this pass.
- No current TAGS caller was inspected or proven to pass an incorrect viewport.
- This card does not establish that a shipped application currently mis-targets controls.
- It does not require DOM hit testing for the Snake canary; a target-independent direct command path remains preferable for that WorkItem.
- Safari, embedded webviews, cross-document iframe targeting, camera mirroring, and aspect-ratio crop policy remain `UNKNOWN`.

## Required revision

1. For `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`, keep `DIRECT_COMMAND` target-independent: map a classified gesture directly to `requestDirection(nextDirection)` and do not use `elementFromPoint()` or synthetic pointer dispatch in the command path.
2. For any future generic pointing adapter, define one explicit coordinate contract:
   - normalized camera coordinates and mirror/crop transform;
   - CSS-pixel viewport origin and dimensions used for hit testing;
   - scrollbar and visual-viewport policy;
   - edge handling using a half-open interior range rather than silently mapping `1` to an unqualified outer boundary;
   - typed rejection when the caller supplies backing-store, screen, or otherwise unbound dimensions.
3. Add deterministic unit tests for `x/y = 0`, interior values, and `1`, plus browser tests in Chromium and Firefox at DPR 1 and DPR 2, with scrollbars and page/visual zoom where supported.

## License and terms uncertainty

- The exact TAGS commit exposes no root `LICENSE` file at the probed path, and repository search returned no license binding for this adapter.
- Internal inspection is authorized by the current WorkItem; reuse or public distribution of this exact adapter remains `LICENSE_UNBOUND` until repository- or file-level rights are proven.
- W3C specifications are cited as documentation; no specification text is being vendored.

## Objection, falsifier, verifier, consumer

- **Strongest objection:** existing callers may already pass correct CSS-pixel dimensions, and the Snake direct-command path may never invoke DOM hit testing.
- **Response:** that can make the defect dormant, but it does not turn an undocumented generic API into a proven coordinate contract. The smallest safe action is to keep the current WorkItem target-independent and test the generic seam separately.
- **Falsifier:** exact caller and browser evidence demonstrates that every admitted runtime binds the supplied viewport to the same CSS-pixel hit-test coordinate space, handles normalized edge samples intentionally, and preserves target identity across DPR, scrollbars, and supported zoom conditions.
- **Verifier:** `DISTINCT_CHROMIUM_FIREFOX_COORDINATE_SPACE_VERIFIER`
- **Consumer:** next authorized successor or amendment for `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`; secondary consumer is a future `TAGS_SPATIAL_INPUT_ADAPTER_COORDINATE_CONTRACT` WorkItem.

## Cost and fitness

- Producer amendment for the Snake direct-command boundary: `5–15 minutes` if not already explicit.
- Generic adapter contract and unit-test revision: `20–45 minutes`.
- Chromium/Firefox DPR/scrollbar/zoom verification: `30–60 minutes` with existing tooling.
- Monetary cost: `$0`; operator minutes requested: `0`.
- Fitness credit: `0` until an exact WorkItem consumes this card and a distinct verifier binds results to exact bytes.

No task mutation, implementation, browser execution, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, private-data use, or demand invention occurred.
