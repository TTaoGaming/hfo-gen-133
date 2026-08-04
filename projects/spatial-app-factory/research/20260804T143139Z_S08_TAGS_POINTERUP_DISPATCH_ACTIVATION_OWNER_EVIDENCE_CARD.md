---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-04T14:31:39Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: interaction_input_adapters
question: Can the exact TAGS adapter safely treat a truthy pointerup dispatchEvent return as proof that no target listener already consumed the activation before activationCallback runs?
decision: REVISE
fitness_credit: 0
fitness_condition: exact WorkItem consumption and ConsumerAck only
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
sealed: false
---

# S08 evidence card — pointerup dispatch success is not activation ownership

## Decision

**REVISE — one spatial cycle needs one explicit activation owner. `dispatchEvent(pointerup) === true` means only that the cancelable event was not canceled; it does not show that target or ancestor listeners performed no action. Calling a separate `activationCallback` afterward can therefore create a second application action for one physical release.**

For the current Snake successor, the lower-risk contract is a direct named spatial producer that calls `requestDirection()` once at its selected edge and does not also route the same cycle through a generic target activation path.

## Self-probe and changed question

- Expected and observed carrier task ID: `6a526109ba348191b5f23ad3172ad568`; exact match.
- Authenticated GitHub identity: `TTaoGaming`; canonical repository default branch resolves to `agent/gen133-bootstrap-20260730`.
- Surfaces used: authenticated GitHub exact file, claim, recent-commit, duplicate-search, Git-first write/readback; current primary standards sources; authenticated Slack pointer after readback.
- Rotation lane: `interaction_input_adapters`, following the prior spatial-FOSS/license card.
- Changed queue edge: the current Snake successor requires one direct `requestDirection(nextDirection)` seam and a named spatial `BEGIN / HELD / COMMIT-or-CANCEL` producer. Prior S08 cards bounded repeat filtering and release-to-rearm but did not determine whether the reused TAGS adapter has a single owner for the terminal activation.
- Duplicate searches for `activationCallback`, `double activation`, `dispatchEvent pointerup`, and equivalent terms returned no prior Gen-133 evidence card.
- No task mutation, implementation, browser execution, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, or private-data use occurred.

## Exact candidate and bounded trace

### Candidate bytes

- Repository/commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
- Path: `prototypes/spatial-input-adapter.js`
- Blob: `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- Relevant behavior:
  1. `dispatchSample()` dispatches an untrusted synthetic `pointerup` to `activeTarget`.
  2. It stores the boolean result as `dispatched`.
  3. After clearing cycle state, it calls `activationCallback(releasedTarget)` whenever `dispatched !== false`.

### Failure specimen

1. Target or ancestor registers a `pointerup` listener that performs the application action but does not call `preventDefault()`.
2. Adapter dispatches synthetic `pointerup`; the listener performs action A.
3. DOM dispatch completes and returns `true` because the event was not canceled.
4. Adapter calls `activationCallback`; callback performs action A again.
5. Observed result: two actions from one release, despite one terminal edge.

The inverse compatibility gap also exists: a target that activates only on high-level `click` receives no explicit `click` from this adapter. This card does not claim every browser will synthesize or suppress any additional event from these untrusted bytes; that requires browser capture. The proved defect is narrower: the dispatch return value cannot establish exclusive activation ownership.

## Current primary-source contract

Primary sources accessed 2026-08-04:

1. Exact TAGS adapter: https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/spatial-input-adapter.js
2. Current Snake successor claim: https://github.com/TTaoGaming/hfo-gen-133/blob/0aea1b7dd922c747a67fdc0a38ba9fb0a727b77b/projects/spatial-app-factory/claims/20260804T091631Z_SPATIAL_FACTORY_HTML5_SNAKE_PROVENANCE_CLASSIFICATION_FEASIBLE_CLOCK_SUCCESSOR.claim.yaml
3. WHATWG DOM Living Standard, updated 2026-07-18: https://dom.spec.whatwg.org/
4. W3C Pointer Events Level 4 Working Draft, 2026-07-01: https://www.w3.org/TR/2026/WD-pointerevents4-20260701/

The DOM Standard defines application-dispatched events as synthetic, sets `isTrusted=false`, and defines `dispatchEvent()` as a cancellation handshake: its boolean reports whether the event was canceled. It provides no consumed-action or listener-side-effect result.

Pointer Events Level 4 separately labels constructor-and-`dispatchEvent()` examples as untrusted pointer events. It encourages high-level `click` for device-independent activation and defines click/default activation behavior independently from low-level `pointerup` handling. Therefore, a generic adapter must not infer that an uncanceled `pointerup` reserves the application activation for a second callback.

## Required revision

For any successor that reuses this adapter lifecycle:

1. Declare exactly one activation owner per mode:
   - `DIRECT_COMMAND`: spatial terminal edge calls the app command seam; dispatch no generic activation sequence for that same cycle, or
   - `DOM_CONTROL`: route one documented high-level activation mechanism; call no parallel app callback.
2. Do not use the boolean return from `dispatchEvent(pointerup)` as `activation_not_consumed`, `action_not_taken`, or equivalent.
3. If low-level pointer events are retained for observation/visual state, their listeners must not also own the command, and the contract must state this explicitly.
4. For `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`, bind the spatial producer directly to `requestDirection(nextDirection)` and record whether command ownership is on `BEGIN` or `COMMIT`; zero target activation callback is permitted for that cycle.
5. Add deterministic counters for:
   - uncanceled `pointerup` listener with a side effect plus callback: expected one owner and one action, never two;
   - canceled `pointerup`: expected zero callback action;
   - target with only `click` activation: expected one explicitly selected high-level path or typed unsupported result;
   - cancellation, still-pinched reacquisition, and neutral re-arm: zero latent action.
6. Browser verification must record Chromium and Firefox event order, `isTrusted`, `defaultPrevented`, listener count, callback count, and final action count. Safari remains unknown unless separately captured.

## Supported claims

- The exact adapter dispatches `pointerup` before conditionally calling `activationCallback`.
- `dispatchEvent()` returning `true` establishes non-cancellation, not absence of listener side effects.
- A non-canceling `pointerup` listener and the callback can both perform an action in one synchronous call path.
- The current WorkItem already requires a direct command seam and exactly one terminal owner, so splitting command ownership is material to its acceptance traces.
- One explicit owner plus action-count assertions falsifies this bounded duplicate path.

## Excluded claims

- No claim that current Snake, 2048, or another target actually registers the duplicate listener.
- No claim that script-dispatched `pointerdown`/`pointerup` automatically produces a browser `click` in every or any named engine.
- No claim that activation should universally occur on pinch begin rather than release; that is a product-latency and error-rate measurement question.
- No browser, camera, classifier, accessibility, latency, user-demand, buyer, revenue, production-readiness, deployment, or publication claim.
- No implementation authorization, structural pass, producer return, distinct verifier verdict, ConsumerAck, or completion claim.

## License / terms uncertainty

- This card adds no package and copies no third-party implementation bytes.
- A repository-wide license grant for `TTaoGaming/TAGS` was not established at the exact candidate commit; reuse or distribution of the adapter bytes remains `LICENSE_UNBOUND` outside the existing internal evidence context.
- The Snake successor separately classifies its upstream as `VISIBLE_MIT_GRANT; PREEXISTING_FILE_ORIGIN_NOT_FULLY_AUDITED; INTERNAL_ONLY_PENDING_PROVENANCE_REVIEW`; public distribution chain of title remains `NOT_STOOD`.
- W3C and WHATWG standards are cited as documentation, not incorporated into product code.

## Cost and operator minutes

- Research spend: `$0`.
- Operator minutes consumed: `0`.
- Estimated producer revision: `15–30 engineering minutes`, unmeasured.
- Estimated deterministic unit tests: `15–30 verifier minutes`, unmeasured.
- Estimated distinct two-browser capture: `20–40 minutes`, unmeasured.

## Strongest objection

A generic adapter may intentionally expose both low-level pointer notifications and a separate app callback, leaving consumers responsible for not double-binding them. That can work, but the current API has no typed ownership mode and uses the dispatch boolean as its callback gate. Because `true` carries only cancellation state, consumer discipline is invisible and untestable at this boundary. An explicit mode or single command seam is the smaller zero-trust contract.

## Falsifier

This card falls or is superseded if exact successor bytes:

- remove one of the two activation-capable paths for a cycle;
- expose and enforce a typed ownership mode that makes the duplicate trace impossible;
- prove through exact-sha browser traces that every permitted target contract yields one action for the stated specimen; or
- replace this adapter with a producer that does not dispatch DOM pointer events.

It expires immediately on adapter blob change, ownership-mode change, WorkItem retirement, or a newer exact standards/browser finding that changes the bounded semantics.

## Verifier

- Structural: `S04_STRUCTURAL_PREFLIGHT_VERIFIER` checks exact blob binding, one-owner invariant, test oracle, license ceiling, and absence of dual command paths; same-provider weight remains zero.
- Runtime: a distinct browser-capable nonproducer uses instrumented targets whose `pointerup`, `click`, and callback paths increment separate counters, then returns digest-bound `STOOD | FELL` against the exact successor SHA.
- S08, the adapter author, packet compiler, and successor producer do not grade the runtime result.

## Consumer

- Immediate consumer: the next authorized successor or amendment for `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`.
- Required consumed classification: `ONE_SPATIAL_CYCLE_ONE_EXPLICIT_ACTIVATION_OWNER; DISPATCH_BOOLEAN_IS_CANCELLATION_ONLY`.
- Decision consumer: `S09_STRATEGIC_REASONING_AND_VOTING` after distinct verification.
- Fitness remains `0` until an exact WorkItem cites these exact bytes and records ConsumerAck.

## Expiry

`2026-08-11T14:31:39Z`, or immediate supersession under the falsifier/change conditions above.
