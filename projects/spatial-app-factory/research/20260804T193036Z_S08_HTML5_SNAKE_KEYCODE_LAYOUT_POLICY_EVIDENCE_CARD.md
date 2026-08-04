---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: INTERACTION_INPUT_ADAPTERS
result: REVISE
valid_time_utc: 2026-08-04T19:30:36Z
expiry_utc: 2026-08-11T19:30:36Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# S08 evidence card — explicit keyboard-layout policy before Snake input parity

## Bounded changed uncertainty

The changed S06 packet now requires one focused native-keyboard path and one direct `requestDirection(nextDirection)` seam, but it does not bind the semantic contract for the upstream numeric aliases. Should the canary inherit `KeyboardEvent.keyCode` mappings for arrows plus W/A/S/D and H/J/K/L, or replace them with an explicit modern layout policy?

## Exact candidates

- Upstream application: `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91`
- Exact file: `game.js`
- Exact blob: `c286389487bd68f15170fbb3add6a060f252d169`
- Source: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js
- Current spatial adapter examined for boundary context only: `TTaoGaming/TAGS@a3b636a7ecaab5afa1932ec92559c7c454904039`, `prototypes/spatial-input-adapter.js`, blob `579c9551225f0974ed93564b6ad8bfb1abf72cf3`
- Adapter source: https://github.com/TTaoGaming/TAGS/blob/a3b636a7ecaab5afa1932ec92559c7c454904039/prototypes/spatial-input-adapter.js

The upstream file binds direction arrays to numeric `keyCode` values: arrows plus letter aliases (`WASD`, `HJKL`). It then mutates direction from `e.keyCode` in a global `keydown` listener.

## Primary current evidence

Sources retrieved 2026-08-04:

1. W3C UI Events states that conforming authors can use `key` and `code`; legacy `keyCode` is system- and implementation-dependent and its possible values are not normatively defined. https://www.w3.org/TR/uievents/
2. W3C defines `key` as the meaning of the pressed key after layout/IME mapping. Named navigation values include `ArrowUp`, `ArrowDown`, `ArrowLeft`, and `ArrowRight`. https://www.w3.org/TR/uievents-key/
3. W3C defines `code` as physical-key identity without keyboard-layout modification and gives game movement such as WASD as the motivating use case. https://www.w3.org/TR/uievents-code/

## Supported claims

- The exact upstream candidate uses legacy numeric `keyCode` for both semantic arrow keys and letter-based movement aliases.
- `keyCode` does not provide a current normative cross-layout contract for those letter aliases.
- `KeyboardEvent.key` is the correct field when the intended meaning is the named arrow command.
- `KeyboardEvent.code` is the correct field only when the product intentionally promises physical-position controls such as the keys occupying the US-QWERTY WASD positions.
- One undifferentiated fallback table mixing arrows, character meaning, and physical positions makes native/spatial parity ambiguous and difficult to verify.

## Excluded claims / unknowns

- No browser, OS keyboard-layout switch, IME, virtual keyboard, or accessibility device was executed in this pass.
- This card does not claim Chromium or Firefox currently fails the upstream numeric arrow codes.
- It does not prove whether existing users depend on the W/A/S/D or H/J/K/L aliases.
- It does not establish a public-product accessibility policy or require removal of all aliases forever.
- Safari, mobile virtual keyboards, alternate hardware, and assistive-input behavior remain `UNKNOWN`.

## Decision — `REVISE`

For the bounded canary:

1. Bind the required native direction path to `event.key` values `ArrowUp`, `ArrowDown`, `ArrowLeft`, and `ArrowRight` only.
2. Remove `keyCode` from the runnable derivative.
3. Do not silently preserve W/A/S/D or H/J/K/L through a mixed fallback table.
4. If a successor explicitly requires letter controls, declare one separately testable policy:
   - `PHYSICAL_POSITION`: use `event.code` values such as `KeyW`, `KeyA`, `KeyS`, `KeyD`; or
   - `LAYOUT_MEANING`: use normalized `event.key` character values and test the named layouts.
5. Never make spatial command semantics depend on either keyboard-layout policy; spatial input still calls the same direction command seam directly.
6. Record `key`, `code`, `keyCode`, layout, accepted command, and final action in browser evidence, while treating `keyCode` as observation only.

Required classification:

`ARROW_COMMANDS_USE_KEY; PHYSICAL_LETTER_CONTROLS_REQUIRE_EXPLICIT_CODE_POLICY; LEGACY_KEYCODE_IS_NONBINDING`

## Strongest objection

Dropping the inherited W/A/S/D and H/J/K/L aliases can regress familiar controls and reduce usability for users who do not prefer arrow keys. The answer is not to retain an ambiguous numeric table; it is to bind the desired alias behavior explicitly and test it as a separate acceptance surface.

## Falsifier

Revise this card if the exact WorkItem is amended to require backward-compatible letter aliases and a distinct verifier demonstrates, on the exact checkout, one documented `key` or `code` policy that preserves those aliases across the named keyboard layouts without duplicate commands, modifier leakage, composition leakage, focus escape, or native/spatial divergence.

## Verification contract

Verifier: `DISTINCT_BROWSER_CAPABLE_NONPRODUCER_KEYBOARD_LAYOUT_WITNESS`

Minimum evidence:

- Exact final checkout SHA and browser versions
- Chromium and Firefox
- US layout plus at least one non-US layout or OS-level layout switch
- Arrow commands under `event.key`
- Any admitted letter policy under the declared `event.key` or `event.code` contract
- Captured `key`, `code`, legacy `keyCode`, modifiers, `isComposing`, repeat, focus owner, `preventDefault` count, `requestDirection` count, and final-action count
- Zero synthetic keyboard events and zero second command before the movement tick

## License / terms uncertainty

The approved upstream README blob `bf29f270d27882138d6e50868a212b4780502ca8` contains a complete MIT notice: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/README.md . Prior Gen-133 evidence still classifies pre-existing file ancestry and public-distribution chain of title as not fully stood. This revision adds no dependency and copies no TAGS adapter bytes; the examined TAGS adapter remains license-unbound for reuse unless separately resolved.

## Cost and operator estimate

- Producer amendment: `20–40 minutes`
- Deterministic tests: `15–30 minutes`
- Chromium/Firefox plus one alternate-layout verification: `30–60 minutes`
- Surfaced paid cost: `$0`
- Operator minutes this research pass: `0`

## Consumer and credit gate

Consumer: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`, through the next authorized successor or acceptance amendment.

Research volume and candidate count earn zero credit. Fitness remains `0` until the exact WorkItem consumes this card, a distinct verifier binds evidence to the produced checkout, and a named ConsumerAck records the outcome.

## Effect record

No implementation, browser execution, keyboard-layout change, task mutation, account action, terms acceptance, private-data access, outreach, application, purchase, send, spend, deployment, merge, or publication occurred.
