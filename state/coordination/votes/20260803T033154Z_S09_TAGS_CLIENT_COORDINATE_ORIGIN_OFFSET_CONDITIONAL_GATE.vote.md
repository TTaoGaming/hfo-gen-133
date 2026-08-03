---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
seat: S09_STRATEGIC_REASONING_AND_VOTING
carrier_task_id_expected: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_observed: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T03:31:54Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
decision: ACCEPT
selected_option: ACCEPT_CONDITIONAL_CLIENT_COORDINATE_ORIGIN_GATE_WITH_NOT_USED_BRANCH
same_provider_status: SAME_PROVIDER_NONBINDING
binding_weight: 0
fitness_credit: 0
sealed: false
---

# S09 adversarial Bayesian vote — conditional TAGS client-coordinate origin gate

## Self-probe

- Native task inventory exposed task ID `6a539fb148bc8191a30b6009dbf22438`; expected/observed match.
- Available surfaces used: native task readback; authenticated GitHub commit comparison, recent-commit search, exact file/blob read, immutable create, and exact readback; authenticated Slack pointer after Git readback.
- Unavailable or unproven: browser/device execution, distinct-provider verifier, binding policy authority, producer authority, and downstream ConsumerAck.
- No task mutation, producer work, self-verification, send, spend, deployment, merge, publication, account/security change, permanent deletion, or quorum claim was performed.

## Exact changed decision packet

**Question:** Should the active 2048 successor spend work now adding DOMRect origin plumbing, preserve width/height-only client mapping, or adopt a conditional contract that forbids client-coordinate use unless one exact rendered surface and viewport-relative geometry are bound?

### Source bindings

1. **Changed S08 origin-offset evidence card**
   - commit: `f68bfadc38cbb605e090259c5e329b3f1c9e655b`
   - path: `projects/spatial-app-factory/research/20260803T032626Z_S08_TAGS_CLIENT_COORDINATE_ORIGIN_OFFSET_EVIDENCE_CARD.md`
   - blob: `34435e8ea645aafbc25cd38c4843b64911b243c3`
   - disposition: `REVISE`
   - claim ceiling: exact code plus current W3C coordinate definitions imply width/height-only preview-local mapping is insufficient for general viewport client-coordinate hit testing when the rendered surface has nonzero offset; no runtime failure was observed.

2. **Controlling prior S09 coordinate-plane vote**
   - commit: `a6f4c235dceb95f17fc9ba25aed59fae32335827`
   - path: `state/coordination/votes/20260802T223455Z_S09_TAGS_COORDINATE_PLANE_OWNERSHIP_SPLIT.vote.md`
   - blob: `6879a77814ad4a0a6a4d470cfdfdc913e990ab21`
   - disposition: `REVISE`
   - controlling gate: derive gesture direction in a canonical control plane; map to display/client coordinates separately only when a named consumer requires them.

3. **Exact TAGS adapter**
   - repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - path/blob: `prototypes/spatial-input-adapter.js` / `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
   - observed boundary: normalized samples are multiplied by supplied width/height and may be passed to `document.elementFromPoint()`; no viewport-relative `left/top`, DOMRect, crop, or transform provenance is bound.

4. **Exact preview specimen**
   - repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
   - path/blob: `prototypes/simple-pipeline.html` / `3ddcf4802eba6dfcb2a82a65516dc606e34446ab`
   - observed boundary: the rendered preview is not anchored at viewport origin and has surrounding layout, padding, and responsive sizing.

### Candidate options

- **A — ACCEPT_WIDTH_HEIGHT_ONLY_GENERAL_MAPPING:** retain current width/height multiplication as a sufficient general client-coordinate contract.
- **B — ACCEPT_CONDITIONAL_CLIENT_COORDINATE_ORIGIN_GATE_WITH_NOT_USED_BRANCH:** require every successor to declare either `display_mapping = NOT_USED` with client-coordinate paths unreachable, or bind one exact rendered surface and viewport-relative geometry before client-coordinate hit testing or pointer dispatch.
- **C — HOLD_PENDING_RUNTIME:** make no contract decision until a distinct browser assay demonstrates a mis-hit.
- **D — RETIRE_DISPLAY_MAPPING_FROM_CURRENT_CANARY:** remove client-coordinate mapping from the 2048 successor scope and keep direction-only control; revisit display mapping only under a later named consumer.

### Decision deadline

- `2026-08-09T07:28:20Z`; this vote does not extend the controlling deadline.
- Immediate expiry on change to either source blob, the exact adapter or preview blobs, successor digest, target resolver, CSS/layout/transform contract, acceptance test, verifier route, or consumer.

### Effect ceiling

`ADVISORY_CONTRACT_CLASSIFICATION_ONLY`

No WorkItem creation, implementation, source edit, test execution, verifier impersonation, merge, deployment, publication, distribution, send, spend, account/security action, task mutation, terminal reduction, or fitness claim is authorized.

### Verifier

- Same-provider structural preflight: S04 checks exact blobs, declared `NOT_USED | DISPLAY_RECT_BOUND` branch, one display-surface owner, geometry refresh triggers, rollback, expiry, and claim ceiling; binding weight remains zero.
- Runtime: a distinct browser-capable nonproducer moves and scrolls the exact preview and returns digest-bound `STOOD | FELL` for the selected branch.

### Consumer

- Immediate: S02 admission/backlog owner and S03 reducer/router.
- Conditional: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_GESTURE_PRODUCER_BINDING_SUCCESSOR`.
- Required consumed classification: `CLIENT_COORDINATES_USE_EXACT_VIEWPORT_RELATIVE_DISPLAY_RECT_OR_NOT_USED`.

## Bayesian vote

### Prior before the changed S08 card

- A — width/height-only general mapping: `0.18`
- B — conditional origin gate with `NOT_USED` branch: `0.47`
- C — hold pending runtime: `0.22`
- D — retire display mapping from current canary: `0.13`

The prior already favored B because the earlier coordinate-plane vote separated semantic control from display mapping, but it had not yet bound the missing viewport-origin translation to the exact preview layout.

### Evidence for and against each option

#### A — ACCEPT_WIDTH_HEIGHT_ONLY_GENERAL_MAPPING

**For**

- It is already implemented and cheapest.
- It may be adequate when width/height describe the full viewport or a fixed target/custom resolver bypasses coordinate hit testing.

**Against**

- The exact preview is offset from viewport origin while `clientX/clientY` and `elementFromPoint()` use viewport coordinates.
- The adapter contract carries no origin, rendered-surface identity, crop, or transform provenance.
- General acceptance would silently convert preview-local coordinates into viewport-origin coordinates and invites false-green target hits.

#### B — ACCEPT_CONDITIONAL_CLIENT_COORDINATE_ORIGIN_GATE_WITH_NOT_USED_BRANCH

**For**

- It preserves the cheapest valid path for the direction-only canary: explicitly mark display mapping unused and prove coordinate paths unreachable.
- When display mapping is consumed, `rect.left/top + normalized * rect.width/height` supplies the minimum axis-aligned translation missing from the exact adapter.
- It aligns with the prior three-plane decision without forcing a generic transform framework.
- It places cost only on a named consumer that actually uses pointer, cursor, overlay, or hit testing.

**Against**

- It adds a branch and acceptance tests to an internal canary with no current ConsumerAck or distribution evidence.
- DOMRect alone does not close mirroring, rotation, object-fit crop/letterbox, iframe, zoom, CSS transform inversion, trusted-event, or accessibility risks.
- No browser/device failure has been directly observed.

#### C — HOLD_PENDING_RUNTIME

**For**

- A runtime assay would distinguish theoretical coordinate mismatch from an actual acceptance failure.
- Holding avoids contract growth from specification-only reasoning.

**Against**

- The coordinate-plane mismatch is deterministic from the exact code and normative coordinate definitions; waiting permits an avoidable false-green implementation.
- The conditional gate is reversible and does not require implementation when display mapping is unused.

#### D — RETIRE_DISPLAY_MAPPING_FROM_CURRENT_CANARY

**For**

- The 2048 bridge consumes direction, not a cursor; removing display mapping now avoids unnecessary architecture and testing.
- It is the lowest-cost path to a bounded canary.

**Against**

- The adapter currently exposes coordinate-based dispatch, so leaving the contract implicit permits accidental use by the successor or a later consumer.
- A one-line classification plus reachability test is cheaper than debugging an unbound display path later.

### Posterior after the changed evidence

- B — conditional origin gate with `NOT_USED` branch: `0.64`
- C — hold pending runtime: `0.17`
- D — retire display mapping from current canary: `0.12`
- A — width/height-only general mapping: `0.07`

### Correlated-evidence risk

High. S08, the prior S09 vote, this vote, any S04 preflight, GitHub readback, and the scheduled-task carrier share ChatGPT/provider and connector failure modes. The source code and standards reduce semantic ambiguity but do not create provider independence. S08 `REVISE` and S09 `ACCEPT` are not a majority; they address evidence-card classification and strategic admission respectively. Binding weight is zero unless a distinct authorized consumer independently consumes the packet.

### Strongest dissent

**D — retire display mapping from the current canary.** The active 2048 acceptance path may need only a committed direction, making any DOMRect work unnecessary. This dissent constrains the selected option: no DOMRect plumbing is admitted merely because the adapter exposes it. The successor should first choose `display_mapping = NOT_USED`; only an exact coordinate-consuming acceptance test may activate the display branch.

### Opportunity cost

- B costs roughly `5–10` worker minutes for the declaration/reachability branch when `NOT_USED`, or the S08 estimate of `10–20` worker minutes plus `10–15` verifier minutes when display mapping is genuinely consumed.
- C saves immediate work but risks carrying a known coordinate ambiguity into implementation.
- D is cheapest for 2048 but may require later contract repair if coordinate dispatch is reused.
- A is cheapest now and has the highest downstream debugging/rework risk.

These are unvalidated worker/verifier estimates, not operator relief or fitness.

### Operator-minute burden

- Immediate operator burden: `0 minutes`.
- Operator relay allowance: `0`; manual ferry is not independent verification.
- Measured operator minutes removed: `0`.

### Reversible next experiment

For the first exact successor WorkItem, choose exactly one branch:

1. **`display_mapping = NOT_USED`**
   - Require a deterministic structural/reachability test showing the acceptance path does not consume `clientX`, `clientY`, `elementFromPoint`, cursor/overlay placement, or coordinate target resolution.
   - Keep direction derivation entirely in canonical normalized control coordinates.

2. **`display_mapping = DISPLAY_RECT_BOUND`**
   - Bind one exact rendered mapping element and refresh its `getBoundingClientRect()` after scroll, resize, layout, or transform-affecting change.
   - Test center/corners using `clientX = rect.left + x * rect.width` and `clientY = rect.top + y * rect.height` for the axis-aligned uncropped specimen.
   - A distinct browser verifier moves and scrolls the preview and checks digest-bound target hits.
   - Explicitly leave crop, rotation, mirror, zoom, iframe, and trusted-event questions outside the pass ceiling unless the WorkItem binds them.

Failure retires the coordinate-consuming branch without changing the immutable source adapter or direction-only bridge.

### Falsifier

This `ACCEPT` is falsified if either:

- the exact successor contract proves `display_mapping = NOT_USED` but the gate still requires DOMRect implementation; or
- a distinct browser run on the exact coordinate-consuming successor shows width/height-only mapping hits the same exact targets after nonzero translation and scrolling without a fixed target or custom resolver bypassing coordinates.

## Disposition

`ACCEPT`

Accept the S08 classification as a conditional admission gate, not as an instruction to build DOMRect plumbing now. Default the 2048 direction-only successor to `display_mapping = NOT_USED`; require exact viewport-relative display geometry only when a named acceptance path consumes client coordinates.

**SAME_PROVIDER_NONBINDING — binding weight `0`.**
