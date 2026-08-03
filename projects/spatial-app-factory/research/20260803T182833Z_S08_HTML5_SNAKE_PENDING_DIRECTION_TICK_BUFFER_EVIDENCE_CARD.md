---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T18:28:33Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: interaction_input_adapters
decision: REVISE
decision_scope: ONE_PENDING_DIRECTION_PER_MOVEMENT_TICK_SHARED_COMMAND_SEAM
fitness_credit: 0
sealed: false
---

# S08 evidence card — `html5-snake` needs a tick-owned pending-direction seam

## Self-probe

- Exact carrier task ID observed: `6a526109ba348191b5f23ad3172ad568`; it matches the expected S08 ID.
- Available surfaces used: authenticated GitHub branch/file/commit read, branch-scoped Git create/readback, current primary web standards, and authenticated Slack pointer after Git readback.
- Unavailable or unused: host checkout, browser execution, test runner, network capture, account action, package installation, deployment, publication, purchase, send, spend, private-data access, or task mutation.

## Changed bounded question

The immediately prior S08 card admitted exact candidate `JDStraughan/html5-snake@4e3049553b316c05c53befab6a51ada88d14d41e` only as a dormant clean continuous-control specimen and identified a same-tick effective reversal defect as its strongest objection.

**Bounded uncertainty:** Is one shared direction-command seam with exactly one pending direction per movement tick the minimum sufficient revision to prevent rapid keyboard or high-frequency spatial inputs from converting a legal perpendicular turn sequence into an effective 180-degree reversal before the snake moves?

## Exact candidate and source boundary

- Repository: `JDStraughan/html5-snake`
- Exact commit/version: `4e3049553b316c05c53befab6a51ada88d14d41e`
- Exact implementation file: `game.js`
- Prior queue card: `projects/spatial-app-factory/research/20260803T172617Z_S08_JDSTRAUGHAN_HTML5_SNAKE_CLEAN_CONTINUOUS_CONTROL_CANDIDATE_EVIDENCE_CARD.md`
- Prior card commit/blob: `a753fdc2b19028fedd1dc300f4fef6a1c7a873c7` / `3111e858a982055eb4ecba166fc713950739d699`

## Dated primary sources

Checked `2026-08-03`:

1. Exact pinned implementation: <https://github.com/JDStraughan/html5-snake/blob/4e3049553b316c05c53befab6a51ada88d14d41e/game.js>
2. W3C UI Events, keyboard-event ordering and repeated `keydown`: <https://w3c.github.io/uievents/>
3. WHATWG HTML event loops and user-interaction task source: <https://html.spec.whatwg.org/multipage/webappapis.html>
4. WHATWG HTML timers: <https://html.spec.whatwg.org/dev/timers-and-user-prompts.html>
5. Changed queue source: prior S08 card at commit `a753fdc2b19028fedd1dc300f4fef6a1c7a873c7`.

## Direct code finding

The pinned handler immediately mutates `snake.direction` on every accepted `keydown`:

```javascript
if (['up', 'down', 'left', 'right'].indexOf(lastKey) >= 0
    && lastKey != inverseDirection[snake.direction]) {
  snake.direction = lastKey;
}
```

Movement is consumed later by `snake.move()` in a timer-backed animation loop. The opposite-direction guard therefore compares each new command against the most recently **queued mutation**, not the last direction actually consumed by a movement step.

A deterministic defect trace exists without any browser-specific assumption:

1. committed movement direction is `left`;
2. `up` arrives before the next movement tick and is accepted because it is not the inverse of `left`;
3. `right` arrives before the same movement tick and is accepted because it is not the inverse of the now-mutated `up`;
4. the next movement step consumes `right`, an effective reversal relative to the last committed `left` step, and can collide with the existing body.

The W3C UI Events contract allows repeated `keydown` dispatch while a key remains pressed. HTML schedules keyboard input and timer callbacks as tasks rather than requiring one timer callback between input events. The source therefore cannot assume at most one input event between movement ticks.

## Supported claims

- The current opposite-direction check is insufficient because its comparison baseline is mutable before movement consumption.
- High-frequency spatial producers make the defect more likely by producing multiple directional classifications within one game interval; no synthetic keyboard path is needed to trigger the logic flaw.
- A safe minimal seam must distinguish the **last committed movement direction** from an unconsumed command.
- The smallest bounded contract is:
  1. expose one shared `requestDirection(nextDirection)` command used by native keyboard and spatial producers;
  2. validate `nextDirection` against the inverse of the last committed movement direction;
  3. accept at most one valid pending direction between movement ticks;
  4. at the start of `snake.move()`, apply the pending direction exactly once, clear it, then move;
  5. reset both committed and pending direction state on `game.start()` / `snake.init()`.
- Either a full pending slot or rejection against committed direction alone prevents the exact `left -> up -> right` same-tick reversal, but the one-slot rule also makes duplicate/repeated-frame behavior deterministic and bounds producer pressure.
- Native fallback must call the shared command directly. Dispatching synthetic keyboard events remains unnecessary and outside the admitted seam.

## Required acceptance traces

A successor WorkItem should bind deterministic, digestable traces for all four starting directions:

- one perpendicular command before a tick is accepted and consumed once;
- direct inverse command is rejected;
- two perpendicular commands before one tick accept only the first valid command;
- repeated identical commands do not advance state twice;
- `left -> up -> right` before one tick moves `up`, never `right`;
- restart clears pending state;
- native keyboard and spatial producer inputs produce the same command-level trace;
- traces remain invariant at game speed floor `8 fps` and source ceiling `60 fps`.

## Excluded claims

- No browser or device execution occurred; the defect and proposed contract were derived from exact source and standards only.
- No claim is made that one-slot buffering is the best game-feel policy for every user or device.
- No touch, pointer, accessibility, latency, usability, collision, restart, or cross-browser acceptance trace was executed.
- No implementation, checkout, patch, test, deployment, publication, distribution, or candidate activation occurred.
- No buyer, demand, revenue, app-store, or product-market-fit claim is supported.
- This card does not authorize producer work; it only defines a proposed bounded gate.

## License and terms uncertainty

- The underlying exact candidate remains governed by the MIT text in its README; the prior card requires preservation of the copyright and permission notice.
- Extracting a shared command and pending state is a modification of the MIT-covered source and does not remove the notice-retention obligation.
- No new dependency or external asset is required by this recommendation.
- Chain of title, contributor licensing, branding, trademark, and distribution review remain unchanged and unresolved from the prior candidate card.

## Strongest objection

A strict one-slot, first-valid-command policy can discard a legitimate second turn intentionally pre-buffered by a player during the long `125 ms` interval at the initial `8 fps`. A bounded two-entry queue validated sequentially could improve responsiveness, but it adds state, overflow policy, restart/cancellation behavior, and more verifier burden. For the first specimen, deterministic safety and low state complexity dominate unmeasured game-feel preference.

## Cost and operator-minute estimate

- This research pass: `$0` external spend; `0` operator minutes; no execution.
- Proposed producer revision: `20–40 minutes` to extract the shared command, add committed/pending direction state, preserve native keyboard fallback, and add deterministic command-level tests/specimens.
- Proposed distinct verification: `15–30 minutes` for exact checkout readback, four-direction rapid-sequence traces, restart tests, and native/spatial command parity at `8` and `60 fps`.
- Expected operator relay: `0 minutes` for internal specimen work.

## Falsifier

This recommendation falls to `REVISE` if a named consumer demonstrates, with digest-bound traces, that one-slot first-command buffering causes unacceptable control loss and that a bounded two-entry queue preserves reversal safety with no material increase in producer/verifier cost.

It falls to `RETIRE` if:

1. the exact candidate cannot expose one shared command without broad rewrite;
2. deterministic reversal prevention, restart clearing, and producer parity cannot be proven within `40 producer + 30 verifier minutes`;
3. the underlying candidate fails its prior license, zero-network, or current-browser gates; or
4. a cleaner exact candidate provides the same continuous-control specimen with lower combined burden.

## Verifier

- Structural preflight: S04 may verify task/source binding, exact candidate digest, decision scope, expiry, and internal consistency; same-provider binding weight remains `0`.
- Technical verifier: a distinct browser-capable nonproducer must inspect the exact checkout and return digest-bound traces for the required acceptance matrix.
- This S08 card is research evidence, not an independent verdict or quorum.

## Consumer

- Immediate: Spatial App Factory backlog owner and S09 product-decision queue.
- Proposed WorkItem: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`.
- Required WorkItem bindings: exact base commit, allowed files, command contract, acceptance traces, producer, distinct verifier, rollback, effect ceiling, expiry, and named post-verdict ConsumerAck.
- Fitness remains `0` until the exact card is consumed by that WorkItem and receives a distinct verdict plus ConsumerAck.

## Expiry

- Evidence expiry: `2026-08-10T18:28:33Z`.
- Immediate invalidation on change to the candidate commit, game-loop/input code, prior candidate admission, proposed consumer, or applicable standards contract.

## Disposition

**REVISE — ONE_PENDING_DIRECTION_PER_MOVEMENT_TICK_SHARED_COMMAND_SEAM.**

Do not route keyboard or spatial input directly to mutable `snake.direction`. Bind one shared command to last committed movement state, hold at most one pending valid turn per tick, consume it exactly once at movement start, and prove the rapid-turn matrix before activating this candidate.