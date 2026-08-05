---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-05T05:31:12Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: interaction_input_adapters
question: Can the exact TAGS generic adapter safely present a fixed pointerId=1, pointerType=touch, isPrimary=true synthetic stream as a drop-in native Pointer Events lifecycle when native input and pointer-capture consumers may coexist?
decision: REVISE
fitness_credit: 0
fitness_condition: exact WorkItem consumption and ConsumerAck only
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
sealed: false
---

# S08 evidence card — synthetic pointer identity is not a native active-pointer lease

## Decision

**REVISE — the exact TAGS stream is an untrusted application protocol, not a native Pointer Events lifecycle. Hard-coding `pointerId=1`, `pointerType='touch'`, and `isPrimary=true` does not register an active user-agent pointer, cannot guarantee pointer-capture compatibility, and can collide semantically with concurrent native input or consumer maps keyed only by `pointerId`.**

For the current Snake WorkItem, retain the already selected `DIRECT_COMMAND -> requestDirection(nextDirection)` path and dispatch no synthetic `PointerEvent` for that command cycle.

Required classification:

```text
SYNTHETIC_POINTER_STREAM_IS_UNTRUSTED_APP_PROTOCOL
NOT_A_USER_AGENT_ACTIVE_POINTER_LEASE
POINTER_CAPTURE_COMPATIBILITY_NOT_PROVEN
FIXED_POINTER_ID_1_NOT_SAFE_AS_GENERIC_COEXISTENCE_CONTRACT
SNAKE_DIRECT_COMMAND_EXCLUDES_THIS_SURFACE
```

## Self-probe and changed queue edge

- Expected and observed task ID: `6a526109ba348191b5f23ad3172ad568`; exact match.
- Available surfaces used: authenticated GitHub exact-file and changed-queue reads; current primary standards research; Git-first write/readback; one Slack pointer after readback.
- Rotation lane: `interaction_input_adapters`, following the prior spatial-FOSS/license card.
- Changed queue edge: commit `2a25ec954b33a2925629ecf6a58b759e50fe27f8` admitted a fresh successor for `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`. Its acceptance contract now makes `DIRECT_COMMAND` the sole spatial activation owner and forbids synthetic pointer dispatch in the Snake command path. The exact generic adapter still exposes an unresolved pointer-identity and capture contract material to that exclusion and to any future DOM-control consumer.
- Duplicate searches for fixed synthetic `pointerId`, pointer-capture compatibility, native/synthetic ID collision, and equivalent terms found no prior S08 evidence card. Prior cards addressed cancellation, coordinate space, target continuity, release-to-rearm, and duplicate activation ownership, not active-pointer identity.

No task mutation, implementation, browser execution, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, public release, or private-data use occurred.

## Exact candidate

- Repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
- Path: `prototypes/spatial-input-adapter.js`
- Blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- Exact defaults:
  - `pointerId: 1`
  - `pointerType: 'touch'`
  - every descriptor sets `isPrimary: true`
- Exact behavior: `defaultEventFactory()` constructs `new PointerEvent(type, init)`, and `dispatchSample()` sends those script-created events with `dispatchEvent()`.
- Current consumer claim: `TTaoGaming/hfo-gen-133@2a25ec954b33a2925629ecf6a58b759e50fe27f8`, path `projects/spatial-app-factory/claims/20260805T050801Z_SPATIAL_FACTORY_HTML5_SNAKE_EXTERNAL_NAVIGATION_LICENSE_PACKAGING_SUCCESSOR.claim.yaml`.

## Primary-source findings

Sources accessed 2026-08-05:

1. Exact TAGS candidate: https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/spatial-input-adapter.js
2. W3C Pointer Events Level 4, latest published Working Draft dated 2026-05-22: https://www.w3.org/TR/pointerevents/
3. WHATWG DOM Living Standard, current page accessed 2026-08-05: https://dom.spec.whatwg.org/

Supported standards facts:

- DOM defines an event created and dispatched by application script as untrusted; `isTrusted` is false unless the user agent dispatched it.
- Pointer Events defines `pointerId` as the identifier for a pointer and allows user agents to reserve `0` or `1` for the primary mouse pointer. Active user-agent pointers in a top-level browsing context must have unique IDs.
- Pointer Events defines `isPrimary` as a relationship among active pointers of the same pointer type: at most one primary pointer per type, ordinarily the first active pointer for that type.
- `Element.setPointerCapture(pointerId)` must throw `NotFoundError` when the supplied ID does not match an active pointer. Constructing and dispatching a `PointerEvent` object does not itself prove that the user agent has created that active-pointer record.

The bounded inference is therefore: the adapter can deliver event-shaped data to listeners, but its fixed identity fields do not acquire the browser-managed active-pointer, primary-pointer, compatibility-mouse, or capture semantics that native consumers may infer from those fields.

## Failure specimens

### A. Pointer-capture consumer

1. A target's `pointerdown` handler calls `setPointerCapture(event.pointerId)`, a normal native-pointer pattern.
2. TAGS dispatches an untrusted event carrying `pointerId=1`.
3. No matching browser-managed active pointer is established by the adapter contract.
4. The capture call can throw `NotFoundError` or otherwise fail to produce the intended capture lifecycle.
5. The adapter's own `activeTarget` pinning may continue, but the target's declared Pointer Events contract has already diverged.

### B. Concurrent native pointer bookkeeping

1. Application code stores pointer state in a map keyed only by `pointerId` and accepts native plus synthetic events on the same surface.
2. The user agent uses or reserves ID `1` for the primary mouse while TAGS also emits ID `1` labelled as touch and primary.
3. The map can overwrite, merge, or terminate the wrong logical stream unless it separately namespaces trust/source/type and serializes ownership.
4. No exact adapter field or mode enforces that separation.

These specimens do not claim a browser internally merges the synthetic event into native pointer state. The defect is the opposite: application-visible identity can look native enough to collide while lacking native lifecycle guarantees.

## Required revision

For the current Snake successor:

1. Keep spatial direction input target-independent and call `requestDirection(nextDirection)` directly.
2. Emit zero synthetic `PointerEvent`, `MouseEvent`, `dispatchEvent`, `elementFromPoint`, pointer-capture, or generic activation traffic for the same command cycle.
3. Preserve native keyboard and spatial command parity at the command seam, not at the DOM-event-shape layer.

For any future generic DOM-control adapter:

1. Type the surface explicitly as `UNTRUSTED_APPLICATION_POINTER_PROTOCOL`; do not claim native Pointer Events substitutability.
2. State whether native input may coexist. If yes, namespace stream identity by at least source/trust plus logical pointer ID; never key shared state only by the fixed numeric ID.
3. Do not default to user-agent-conventional `pointerId` values `0` or `1`. Allocate a per-session logical ID or require the caller to provide one, while stating that this still does not create a browser active pointer.
4. Do not promise `setPointerCapture`, implicit capture, compatibility mouse events, trusted activation, or browser active-pointer behavior. Return typed `UNSUPPORTED_SYNTHETIC_CAPTURE` when a consumer requires them.
5. Derive or declare `isPrimary` under an adapter-owned multi-pointer policy; never set every concurrent synthetic pointer primary.
6. Add deterministic mixed-input tests with native mouse/touch fixtures and synthetic cycles, plus separate counters for source, trust, pointer type, logical ID, capture call, thrown exception, terminal edge, and final action.
7. Require distinct Chromium and Firefox browser capture before any broader compatibility claim. Safari and untested assistive/device paths remain `UNKNOWN`.

## Supported claims

- The exact adapter hard-codes ID `1`, type `touch`, and primary status for its synthetic descriptors.
- Events created with the constructor and sent through `dispatchEvent()` are untrusted.
- A script-supplied ID does not by itself prove a matching browser-managed active pointer.
- Pointer capture requires a matching active pointer and can reject an arbitrary synthetic ID.
- ID `1` is not a safe generic coexistence namespace because the Pointer Events specification permits user agents to reserve it for the primary mouse.
- The current Snake WorkItem's direct-command exclusion is the smaller contract and avoids this class of ambiguity.

## Excluded claims

- No claim that Chromium or Firefox was executed in this pass.
- No claim that every browser throws for every synthetic capture attempt; exact runtime behavior remains verifier work.
- No claim that a browser internally merges synthetic and native pointer state.
- No claim that `pointerId=-1` is universally correct for camera-derived hand pointing; whether the source is modeled as a virtual pointing device must be explicit.
- No claim that generic synthetic pointer notification is always unusable. It can work under a narrow, typed, no-capture application protocol.
- No camera accuracy, classifier quality, accessibility, user-demand, buyer, revenue, deployment, publication, production-readiness, or completion claim.

## License and terms uncertainty

- No third-party implementation bytes were copied into this card.
- A repository-wide license grant for `TTaoGaming/TAGS` was not established at the exact candidate commit. Reuse or public distribution of `prototypes/spatial-input-adapter.js` remains `LICENSE_UNBOUND` outside existing internal evidence use.
- W3C and WHATWG standards are cited as documentation only. Their document licenses and any downstream incorporation requirements were not evaluated because no standards text is being shipped as product code.
- Browser telemetry, device permissions, and camera privacy terms are outside this bounded question and remain unevaluated.

## Cost and operator minutes

- Research spend: `$0`.
- Operator minutes consumed: `0`.
- Snake direct-command amendment: `5–15 engineering minutes`, unmeasured.
- Generic adapter identity-mode revision: `20–45 engineering minutes`, unmeasured.
- Deterministic mixed-input fixtures: `20–40 verifier minutes`, unmeasured.
- Distinct Chromium and Firefox capture: `30–60 minutes`, unmeasured.

## Strongest objection

A fully controlled application can reserve ID `1`, prohibit native coexistence, ignore pointer capture, and treat every synthetic field as application metadata. Under that closed-world contract the current bytes may function. The objection does not defeat this card: the adapter is presented as a generic pointer adapter, but the required exclusivity, no-capture rule, source namespace, and one-primary policy are not expressed or enforced. The safe fix is to type and gate that narrow protocol rather than imply native compatibility.

## Falsifier

This card falls or is superseded if exact successor bytes and digest-bound browser evidence show all of the following:

- a typed source namespace prevents native/synthetic map collision;
- logical pointer IDs are allocated per active synthetic stream rather than fixed globally;
- `isPrimary` is enforced under a declared one-primary-per-type policy;
- pointer-capture-required consumers are rejected before dispatch or supported through an independently proven mechanism;
- concurrent native mouse/touch and synthetic traces produce no merged, overwritten, duplicated, or orphaned stream in Chromium and Firefox; and
- the current Snake command path remains direct and contains no synthetic pointer dispatch.

Immediate expiry also occurs on adapter blob change, WorkItem retirement, or a newer exact standards result that changes the bounded contract.

## Verifier

- Structural verifier: `S04_STRUCTURAL_PREFLIGHT_VERIFIER` checks exact candidate/claim binding, direct-command exclusion, typed protocol labels, license ceiling, and deterministic oracle presence. Same-provider binding weight remains zero.
- Runtime verifier: `DISTINCT_CHROMIUM_FIREFOX_NATIVE_SYNTHETIC_POINTER_IDENTITY_AND_CAPTURE_VERIFIER` runs mixed native/synthetic fixtures and returns digest-bound `STOOD | FELL` with event trust, type, ID, primary flag, capture result/exception, action count, and terminal-state counters.
- S08, the adapter author, packet compiler, and producer do not grade the runtime result.

## Consumer

- Immediate consumer: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`, through the fresh successor admitted at commit `2a25ec954b33a2925629ecf6a58b759e50fe27f8`.
- Required consumed classification: `SNAKE_DIRECT_COMMAND_EXCLUDES_SYNTHETIC_POINTER_IDENTITY_AND_CAPTURE_SEMANTICS`.
- Future optional consumer: a separately authorized generic DOM-control adapter WorkItem; no such new WorkItem is invented by this card.
- Fitness remains `0` until an exact WorkItem cites these bytes and records ConsumerAck.

## Expiry

`2026-08-12T05:31:12Z`, or immediate supersession under the falsifier/change conditions above.
