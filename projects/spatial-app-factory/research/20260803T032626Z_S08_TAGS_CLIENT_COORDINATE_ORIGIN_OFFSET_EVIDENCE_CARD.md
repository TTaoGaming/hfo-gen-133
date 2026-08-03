---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T03:26:26Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: interaction_input_adapters
decision: REVISE
classification: TAGS_CLIENT_COORDINATE_MAPPING_REQUIRES_VIEWPORT_ORIGIN_OFFSET_WHEN_DISPLAY_MAPPING_IS_USED
fitness_credit: 0
sealed: false
---

# S08 evidence card — TAGS client-coordinate origin offset

## Self-probe

- Native task inventory exposed exact task ID `6a526109ba348191b5f23ad3172ad568`; expected/observed match.
- Surfaces used: authenticated GitHub exact-file reads and immutable write/readback; current W3C primary specifications; authenticated Slack pointer after Git readback.
- Not exposed or not used: browser/device execution, DOM measurement, camera, private data, account action, package install, build, deployment, merge, or independent verifier.

## One bounded uncertainty

**Question:** Can the exact TAGS adapter map normalized image points into DOM `PointerEvent.clientX/clientY` and `document.elementFromPoint()` coordinates using only `{width, height}`, without the rendered preview's viewport-relative `left/top` offset?

## Exact candidate

- repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
- adapter path/blob: `prototypes/spatial-input-adapter.js` / `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- preview path/blob: `prototypes/simple-pipeline.html` / `3ddcf4802eba6dfcb2a82a65516dc606e34446ab`
- package path/blob/version: `package.json` / `ad608a51a2cf60b89e5c1f69b305dfb391c46365` / `25.6.26.1055`

## Dated primary evidence

Accessed `2026-08-03`:

1. W3C Pointer Events: `clientX/clientY` are coordinates relative to the event viewport.  
   `https://www.w3.org/TR/pointerevents/`
2. W3C CSSOM View: `document.elementFromPoint(x, y)` hit-tests at coordinates in the viewport and applies descendant transforms.  
   `https://www.w3.org/TR/cssom-view-1/#dom-document-elementfrompoint`
3. W3C CSSOM View: `getClientRects()` applies element/ancestor transforms, and `getBoundingClientRect()` returns the bounding rectangle derived from those client rectangles. The returned rectangle is not live.  
   `https://www.w3.org/TR/cssom-view-1/#dom-element-getboundingclientrect`
4. W3C CSSOM View: `clientX/clientY` are relative to the viewport origin.  
   `https://www.w3.org/TR/cssom-view-1/#extensions-to-the-mouseevent-interface`

## Exact observed boundary

`mapNormalizedPoint()` currently returns:

```text
clientX = sample.x * viewport.width
clientY = sample.y * viewport.height
```

The input contract carries no `left`, `top`, DOMRect, preview element, crop, or transform provenance. `dispatchSample()` then passes these values to `document.elementFromPoint()` when no fixed target or custom target resolver is supplied.

The exact preview is not anchored at viewport origin: the page has `body { padding: 20px; }`, a header above the video grid, margins, containers, and responsive sizing. Therefore width/height-only mapping interprets a preview-local point as a viewport-origin point. For an axis-aligned, uncropped preview, the minimum display mapping is:

```text
clientX = rect.left + controlX * rect.width
clientY = rect.top  + controlY * rect.height
```

where `rect` is measured from the exact rendered mapping surface and refreshed after any layout, scroll, resize, or transform-affecting change. This is a source/contract inference from exact code plus the normative coordinate definitions; no browser run was performed.

## Supported claims

- The current `{width,height}` input is insufficient for general DOM client-coordinate mapping when the rendered mapping surface has nonzero viewport-relative offset.
- A successor emitting client coordinates must bind one exact display surface and viewport-relative geometry, or explicitly declare `display_mapping = NOT_USED`.
- `elementFromPoint()` and synthetic pointer coordinates must share the same viewport-coordinate plane.
- Direction classification in the canonical control plane remains independent of this display translation.

## Excluded claims

- No runtime failure, target mis-hit, camera behavior, browser compatibility, or device result was directly observed.
- This card does not solve mirroring, quarter-turn rotation, CSS transform inversion, `object-fit` crop/letterbox compensation, visual-viewport zoom, iframe coordinates, pointer capture, trusted-event/user-activation limits, or accessibility semantics.
- It does not require display mapping for the direction-only 2048 canary when no cursor, overlay, or coordinate-based hit testing is in scope.
- It does not establish demand, distribution readiness, deployment readiness, or revenue.

## License and terms uncertainty

- Exact `package.json` declares `MIT`, but no root `LICENSE` file was found at the bound commit through the inspected path.
- Copyright notice, complete license text, provenance of all repository content, and third-party dependency notice obligations were not verified.
- The repository is private; this card grants no publication or redistribution authority.

## Cost and operator burden

- Contract and deterministic offset tests: estimated `10–20 worker minutes`.
- Distinct browser assay with moved/scrolled preview and digest-bound result: estimated `10–15 verifier minutes`.
- Immediate operator burden: `0 minutes`.
- Operator relay allowance: `0`; manual ferry is not independent verification.

## Strongest objection

The active 2048 successor may consume only a committed direction and never emit a cursor or call coordinate-based hit testing. In that bounded case, adding DOMRect plumbing is unnecessary architecture. The gate must therefore be conditional: require viewport-origin translation only when the named acceptance test uses display/client coordinates; otherwise bind `display_mapping = NOT_USED` and keep direction in normalized control space.

## Falsifier

This `REVISE` is falsified for the named successor if its exact acceptance contract binds `display_mapping = NOT_USED` and no path consumes `clientX/clientY`, `elementFromPoint()`, cursor, overlay, or coordinate-based target resolution. For a display-mapping successor, falsification requires a distinct browser run showing the width/height-only implementation hits the same exact targets after nonzero translation and scrolling without a fixed target or resolver that bypasses coordinates.

## Verifier

- Structural preflight: S04 checks exact blobs, conditional `NOT_USED` branch, one display-surface owner, viewport-origin translation, geometry refresh triggers, claim ceiling, rollback, and expiry. Same-provider and nonbinding.
- Runtime: distinct browser-capable nonproducer moves and scrolls the exact preview, replays center/corner traces, and returns digest-bound `STOOD | FELL` for both `NOT_USED` and display-mapping variants as applicable.

## Consumer

- Immediate: S09 decision queue, S02 admission/backlog owner, S03 reducer/router.
- Conditional WorkItem: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR`.
- Required consumed classification: `CLIENT_COORDINATES_USE_EXACT_VIEWPORT_RELATIVE_DISPLAY_RECT_OR_NOT_USED`.

## Expiry

- Deadline: `2026-08-09T07:28:20Z`.
- Immediate expiry on any change to the adapter blob, preview blob, successor digest, display surface, target resolver, CSS/layout/transform contract, browser verifier route, consumer, or acceptance test.
- Fitness remains `0` until an exact WorkItem consumes this classification and a distinct verdict plus explicit ConsumerAck bind to the same successor digest.

## Disposition

`REVISE`

Do not admit width/height-only mapping as a general DOM client-coordinate contract. Keep display mapping optional for the direction-only canary; when used, bind viewport-relative origin and exact rendered geometry before `elementFromPoint()` or pointer dispatch.