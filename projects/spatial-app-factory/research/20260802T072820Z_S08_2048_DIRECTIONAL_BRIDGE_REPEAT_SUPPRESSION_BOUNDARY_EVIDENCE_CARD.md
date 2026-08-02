---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T07:28:20Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
lane: interaction_input_adapters
question: Does the exact TAGS 2048 directional bridge suppress repeated accepted samples so one physical gesture cannot cause multiple 2048 moves?
decision: REVISE
fitness_credit: 0
fitness_condition: exact WorkItem ConsumerAck only
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
sealed: false
---

# S08 evidence card — 2048 directional bridge repeat-suppression boundary

## Decision

**REVISE — admit only `ONE_ACCEPTED_SUBMIT_CALL -> ONE_MOVE`; exclude `ONE_PHYSICAL_GESTURE -> ONE_MOVE`.**

The exact bridge has one `inputManager.emit('move', direction)` call in each successful `submit(action)` invocation, but it stores no gesture/action identity, prior direction, edge state, cooldown, duplicate key, or release state. Therefore repeated accepted calls are not suppressed by the bridge. The present tests establish call-level behavior only; they do not establish gesture-level idempotency under repeated camera frames or repeated producer delivery.

This finding does not invalidate the producer's five passing unit tests. It narrows the claim ceiling and identifies the next contract that must be owned either by the gesture producer or by an explicit bridge protocol.

## Self-probe and changed edge

- Native carrier inventory matched expected S08 task ID `6a526109ba348191b5f23ad3172ad568` and showed the task enabled.
- Tools observed: native task readback; authenticated GitHub search/fetch/write/readback; authenticated public Slack read/write; web research; ephemeral local execution surface.
- No task mutation, account action, terms acceptance, private-data use, merge, deployment, publication, send, or spend occurred.
- Changed edge: S07 returned an exact bridge implementation after the earlier compatibility card, then S03 recorded that the verifier and ConsumerAck deadlines expired without a distinct `STOOD | FELL`. This card evaluates one previously unbounded behavior in the now-existing exact implementation; it does not renew the expired claim.

## Exact candidate and consumer

- Repository/final commit: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`
- Producer branch: `agent/spatial-2048-directional-bridge-repair-20260802T0424Z`
- Bridge: `prototypes/2048-spatial-canary/directional-bridge.js`
  - Git blob: `1cedd74ea11a0199a3d7537b5b4136261307f309`
  - SHA-256 from producer return: `28f3794567edc7f21461b0cd9d6440f1341eb7b2c6cba3036f440e825c3201a6`
- Tests: `prototypes/2048-spatial-canary/directional-bridge.test.js`
  - Git blob: `92eaed8f2680f332e7bd62ca59724bb89b291bf0`
  - SHA-256 from producer return: `b10352b35ca4b902053741acc06acb05b49c80110ea99963945f3d53852c36cc`
- Existing pointer adapter, unchanged: `prototypes/spatial-input-adapter.js@579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- Upstream app seam: `gabrielecirulli/2048@478b6ec346e3787f589e4af751378d06ded4cbbc`
- Expired WorkItem: `SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_001`
- Immediate consumers: S09 scope decision and any S03-routed nonretroactive successor claim for the same immutable producer digest.

## Dated primary evidence — accessed 2026-08-02

1. Exact final bridge implementation:  
   https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/2048-spatial-canary/directional-bridge.js
2. Exact final unit tests:  
   https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/2048-spatial-canary/directional-bridge.test.js
3. Exact unchanged TAGS pointer adapter:  
   https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/spatial-input-adapter.js
4. Exact S07 producer return, including red-first and `5/5` green unit evidence:  
   https://github.com/TTaoGaming/hfo-gen-133/blob/ffdf23e91d37a47c7a3b8605910fe1a9e49a680d/state/coordination/receipts/chatgpt_runtime/seat-07/20260802T042745Z_SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_PATCH_RETURNED.yaml
5. Exact S03 expiry HOLD, preserving producer evidence but recording no distinct verdict or ConsumerAck:  
   https://github.com/TTaoGaming/hfo-gen-133/blob/67271e33ea26292af7e707bd4dbc6220c600aaec/state/coordination/receipts/chatgpt_runtime/seat-03/20260802T070745Z_SPATIAL_FACTORY_GOLDEN_APP_001_2048_DIRECTIONAL_BRIDGE_VERIFIER_AND_CLAIM_EXPIRED_HOLD.yaml

## Supported claims

- For each accepted invocation, `submit` reaches exactly one explicit `inputManager.emit('move', direction)` statement and returns `true`.
- The bridge's mutable state is only its `enabled` flag. It has no state or key that can recognize two accepted calls as the same logical gesture/action.
- Calling `submit` again with another accepted action reaches the same emit path again; repeat suppression is not implemented by these exact bytes.
- The exact tests submit each accepted direction once and test rejection/disable cases. They do not submit the same accepted logical action twice, replay repeated frames, or prove a release/new-gesture boundary.
- The existing TAGS pointer adapter has pinch-cycle state, but it is unchanged and no exact binding from that pointer-cycle state to the directional action object is present in this three-file canary.
- The S07 return itself already excludes end-to-end gesture compatibility and states that the action-object schema is not bound to a real gesture producer.

## Excluded claims

- No claim that the bridge is universally defective. A correctly edge-triggered upstream producer could call it once per logical gesture.
- No claim that repeat suppression must reside inside this bridge. It may live in the producer, provided the ownership and behavior are exact, source-bound, and tested.
- No claim about real hand tracking, frame rate, browser behavior, latency, accessibility, player experience, or accidental double moves in an executed product.
- No merge, deployment, publication, distribution, demand, buyer, revenue, or product-fitness clearance.
- No renewal, retroactive verifier verdict, or ConsumerAck for the expired WorkItem.

## Required contract revision

A successor must make one of these boundaries explicit and testable:

1. **Producer-owned edge contract:** the bound producer proves it emits exactly one accepted `submit` call per logical gesture despite repeated input frames; or
2. **Identity-bound action:** the action carries a stable `gestureId` or `actionId`, and duplicate deliveries of that ID emit zero additional moves while a later distinct ID may emit the same direction once; or
3. **Explicit lifecycle:** begin/commit/release or equivalent edge state defines when another move is allowed.

A timeout-only debounce is not sufficient evidence by itself because it may also suppress legitimate rapid consecutive moves.

Minimum regression evidence:

- repeated samples from one logical gesture -> exactly one move;
- duplicate delivery of one committed action -> zero additional moves;
- a later distinct gesture in the same direction -> exactly one new move;
- cancellation/disarm/reset -> no latent move;
- keyboard and touch fallback remain unchanged.

## License / terms uncertainty

**No new license or terms uncertainty introduced.** This is a behavioral analysis of exact existing internal JavaScript and test bytes. The prior MIT notice and separate full-asset/Clear Sans provenance gate remain unchanged. No new code or third-party asset was copied into the canonical repository by this research run.

## Cost / operator-minute estimate

- Research spend: **$0**
- Operator minutes consumed: **0**
- Estimated successor implementation/test effort: **10–20 engineering minutes** for a minimal explicit edge/identity contract, not measured.
- Estimated distinct browser/gesture-source verification: **5–10 minutes**, not measured.

## Strongest objection

The bridge should stay deliberately stateless and should not guess physical gesture identity from `direction` and `confidence`; duplicate suppression belongs upstream. That objection is valid. It supports this `REVISE`, not `RETIRE`: keep the small call-level bridge, but stop describing its current unit evidence as one-gesture/one-move evidence until an exact producer contract owns and proves the edge boundary.

## Falsifier

This card is falsified by an exact successor or producer-binding artifact that:

- binds the relevant gesture producer and bridge bytes;
- demonstrates repeated-frame and duplicate-delivery behavior with the minimum regression cases above;
- allows a later distinct same-direction gesture;
- receives a clean distinct nonproducer/browser-capable verdict tied to the exact digest.

Any change to the bridge blob, test blob, producer contract, or upstream app seam immediately expires this card's exact-byte scope.

## Verifier

- Runtime: a distinct browser-capable nonproducer with access to the exact bridge and bound gesture producer.
- Structural: S04 may verify exact source/test bindings and that the claim ceiling says `CALL_LEVEL_ONLY` until runtime evidence exists.
- The bridge author/producer and S08 do not grade the successor.

## Consumer

- Immediate: S09 and S03 consume as `CURRENT_BRIDGE_CALL_LEVEL_ONLY` when deciding whether to admit a new nonretroactive verifier or repair WorkItem.
- Implementation consumer: the first exact successor that binds a real gesture producer to the 2048 bridge.
- Fitness remains `0` unless a named WorkItem explicitly consumes this card and records ConsumerAck.

## Expiry

`2026-08-09T07:28:20Z`, or immediately upon any bridge/test/producer-binding/upstream-seam change, whichever occurs first.
