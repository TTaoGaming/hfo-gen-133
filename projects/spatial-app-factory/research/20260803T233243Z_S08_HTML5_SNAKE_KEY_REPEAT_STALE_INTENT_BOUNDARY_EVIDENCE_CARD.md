---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T23:32:43Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: interaction_input_adapters
decision: REVISE
decision_scope: FILTER_NATIVE_KEY_REPEAT_BEFORE_SHARED_DIRECTION_COMMAND
fitness_credit: 0
sealed: false
---

# S08 evidence card — browser key repeat can carry stale intent across movement ticks

## Self-probe

- Exact carrier task ID observed: `6a526109ba348191b5f23ad3172ad568`; it matches the expected S08 task ID.
- Surfaces used: authenticated GitHub exact file/commit reads, branch-scoped immutable create and readback, the current primary W3C UI Events draft, and authenticated Slack pointer only after Git readback.
- Unavailable or unused: host checkout, browser execution, keyboard hardware, test runner, network capture, package installation, account action, task mutation, deployment, merge, publication, outreach, purchase, send beyond the required internal pointer, spend, or private-data access.

## Changed bounded question

The live WorkItem now binds the prior one-slot pending-direction card and the S15 shared-command-seam failure antibody. The contract prevents same-tick reversal and forbids synthetic keyboard dispatch, but the exact upstream native listener forwards every browser `keydown` and does not inspect `KeyboardEvent.repeat`.

**Bounded uncertainty:** Is a one-pending-direction-per-tick `requestDirection(nextDirection)` seam sufficient for discrete native/spatial parity if sustained native keys can emit repeated `keydown` events after movement state changes?

## Exact candidate and changed queue bindings

- Candidate: `JDStraughan/html5-snake@4e3049553b316c05c53befab6a51ada88d14d41e`
- Exact implementation: `game.js`
- Live WorkItem: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`
- Claim: commit `bb99518b7815afcc1fa5d48cc8c8a9e614b3d815`, blob `515a1a8af19b8ae4e1c523c1b85241522a1ed9e6`
- Prior S08 tick-buffer card: commit `97228589cbee180a6a68296b699b7d10a77680fc`, blob `f89b0134414c611af49563dc777a36807b890aa3`
- Changed S15 shared-seam receipt: commit `85851442778388df329e001cefa795fe1c65162a`, blob `805ebda2074fb565b7115ecc30aeecb73113ee85`
- Current downstream state: S06 and S07 remain `HOLD`; no implementation or browser trace exists.

## Dated primary sources

Checked `2026-08-03`:

1. Exact pinned source: <https://github.com/JDStraughan/html5-snake/blob/4e3049553b316c05c53befab6a51ada88d14d41e/game.js>
2. W3C UI Events Working Draft, `21 February 2026`: <https://www.w3.org/TR/2026/WD-uievents-20260221/>
3. Exact live claim at commit `bb99518b7815afcc1fa5d48cc8c8a9e614b3d815`.
4. Exact S15 shared-command-seam receipt at commit `85851442778388df329e001cefa795fe1c65162a`.

## Direct finding

The pinned source registers one global `keydown` listener, maps legacy `e.keyCode`, and processes every matching event. It has no `e.repeat` check and no native activation-edge filter.

The current W3C draft defines `KeyboardEvent.repeat` as `true` for a sustained press. It states that holding a key causes repeating `keydown` events at a system-configured rate, with the initial delay and repeat cadence configuration-dependent. It also describes repeated `keydown` events with `repeat=true` at an environment-dependent rate.

Therefore the one-slot queue alone does not establish that one physical native activation produces one direction command. A held key can continue generating browser events after one or more movement ticks. The exact cross-key repeat policy is environment-dependent, so this card does **not** claim every platform will reproduce the same stale-intent trace. It does establish that the current contract cannot safely assume auto-repeat stops at a tick boundary or after another direction becomes committed.

One adversarial trace permitted by the current unfiltered adapter boundary is:

1. the committed direction is `left`;
2. a sustained `right` press produces an initial inverse command and is rejected;
3. a fresh perpendicular `up` command is accepted and a movement tick commits `up`;
4. a later repeated `right` `keydown` from the still-sustained native key reaches the same command seam;
5. `right` is now perpendicular to committed `up`, so it can be accepted without a fresh right-key activation.

That is stale held-key intent crossing a state transition. Spatial frame classification should not be required to emulate browser auto-repeat merely to satisfy native/spatial parity.

## Supported claims

- The exact upstream listener forwards all matching `keydown` events and does not distinguish initial activation from browser auto-repeat.
- Browser key-repeat timing is external, configurable, and not synchronized to the game’s `8–60 fps` movement loop.
- The pending-direction seam solves mutable same-tick reversal, but by itself does not prove activation-edge equivalence between native and spatial producers.
- Minimum revision for this specimen:
  1. the native keyboard adapter must reject `KeyboardEvent.repeat === true` before mapping or calling `requestDirection`;
  2. only the initial nonrepeat keydown may offer a direction command;
  3. the shared command must still reject same-as-committed, same-as-pending, inverse, and second-valid-before-tick commands under the existing contract;
  4. the spatial producer must be verified as one command per activation edge, not one command per camera/classifier frame;
  5. no producer may synthesize keyboard events.
- This filter is additive, dependency-free, and preserves the native keyboard path required by S15.

## Required acceptance trace amendment

Add one digest-bound browser trace at both source speed floor `8 fps` and ceiling `60 fps`:

- log sanitized event fields `{mappedDirection, repeat}` and command outcomes only;
- begin committed `left`;
- hold native `right` long enough to observe at least one `repeat=true` event;
- issue one fresh native `up` activation while `right` remains physically held where the environment permits;
- after `up` commits, every `repeat=true` event must be rejected at the adapter boundary and must produce no `requestDirection` call;
- direction must remain `up` until a new nonrepeat activation is observed;
- replay the equivalent spatial activation-edge sequence and prove the same command-level trace without per-frame duplicates.

If a target environment does not continue the first key’s repeat after a second key is pressed, record that measured limitation rather than fabricating the trace. Independently prove the simpler invariant that **all observed `repeat=true` direction events are filtered before the command seam**.

## Excluded claims

- No browser, operating system, keyboard, assistive technology, or device was executed.
- No claim is made that all platforms repeat multiple held keys in the same way.
- This card does not select `key` versus `code`, repair legacy `keyCode`, define IME/composition handling, prevent default scrolling, manage focus, or specify accessibility behavior.
- It does not prove spatial activation-edge detection, classifier hysteresis, latency, usability, collision behavior, or game feel.
- It does not authorize implementation, routing, merge, deployment, publication, account action, task mutation, purchase, outreach, send, spend, or private-data use.
- It supports no buyer, demand, revenue, conversion, or product-market-fit claim.

## License and terms uncertainty

- The candidate remains under the visible MIT notice, which must be preserved in any internal specimen and later permitted distribution.
- This recommendation adds no dependency or external asset.
- The separate 2013 contributor-license/public-distribution chain-of-title boundary remains unresolved; this card does not cure or worsen it.
- W3C UI Events is a Working Draft and may change; the verifier must use observed target-browser behavior as the operational receipt.

## Strongest objection

Filtering all auto-repeat may reduce responsiveness for a user who intentionally expects held-key repetition. That objection is not measured here. For this Snake specimen, direction changes are discrete commands, the existing spatial contract is activation-edge based, and hidden operating-system repeat semantics would create producer asymmetry. A deliberate hold-to-repeat feature should be a separate WorkItem with an explicit repeat cadence and equivalent spatial hold-state semantics, not an accidental property of the browser adapter.

## Cost and operator-minute estimate

- This research pass: `$0` external spend; `0` operator minutes; no runtime execution.
- Producer amendment: `5–15 minutes` to filter `e.repeat` before the shared command and add the trace hook to the existing bounded specimen packet.
- Distinct browser verification: `15–30 minutes` across `8` and `60 fps`, including a platform that emits observable repeat events.
- Expected operator relay: `0 minutes` for the internal unmerged specimen.

## Falsifier

Revise this recommendation if a distinct browser-capable verifier proves, with exact event and command traces, that the supported target set cannot produce stale repeated direction events and that retaining repeat materially improves measured control without breaking native/spatial parity.

Retire the candidate if activation-edge parity cannot be demonstrated inside `15 producer + 30 verifier minutes`, if repeat filtering requires broad keyboard-state machinery, or if the candidate fails the already-bound license, zero-network, browser, or shared-command gates.

## Verifier

- Structural: S04 may verify exact task, source, changed-binding, expiry, and internal-consistency fields; same-provider binding weight remains `0`.
- Technical: a distinct browser-capable nonproducer must inspect the exact branch SHA and return event/command traces bound to the acceptance digest.
- This S08 card is research evidence, not a technical verdict, quorum, or ConsumerAck.

## Consumer

- Exact consumer WorkItem: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`.
- Immediate consumers: S06 packet compiler, S07 bounded builder after exact S04 PASS, distinct browser verifier, and S09 decision queue.
- Required consumption: amend the native/spatial parity matrix with repeat filtering or reject this exact card with measured evidence.
- Fitness remains `0` until exact WorkItem consumption, distinct `STOOD | FELL`, and named ConsumerAck.

## Expiry

- Evidence expiry: `2026-08-10T23:32:43Z`.
- Immediate invalidation on change to the candidate commit, keyboard adapter, shared-command contract, target-browser set, WorkItem, or W3C repeat semantics.

## Disposition

**REVISE — FILTER_NATIVE_KEY_REPEAT_BEFORE_SHARED_DIRECTION_COMMAND.**

Do not let environment-controlled browser auto-repeat cross the shared discrete direction seam. Filter `repeat=true` in the native adapter, preserve the direct command path, and prove activation-edge parity with the spatial producer before this WorkItem can stand.