---
schema_id: hfo.gen133.s08.evidence_card.v1
card_id: S08_HEXTRIS_SYNTHETIC_KEYBOARD_KEYCODE_BOUNDARY_20260803T133218Z
task_id: 6a526109ba348191b5f23ad3172ad568
seat: S08
wip: 1
lane: interaction_input_adapters
question: Can pinned Hextris accept a portable standards-based synthetic KeyboardEvent adapter without refactoring its existing keypress path?
decision: REVISE
candidate:
  repository: Hextris/hextris
  ref: 3f4847dc8fd7dab3d1c87e6324b9159d92fbd396
  input_source: js/input.js
  keyboard_dependency: vendor/keypress.min.js
  keyboard_dependency_version: 1.0.8
license_declared: GPL-3.0-or-later
valid_time_utc: 2026-08-03T13:32:18Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
consumer:
  - S09_PRODUCT_DECISION_QUEUE
  - SPATIAL_APP_FACTORY_BACKLOG_OWNER
proposed_workitem: SPATIAL_FACTORY_HEXTRIS_COMMAND_ADAPTER_GATE_001
verifier:
  - S04_STRUCTURAL_PREFLIGHT_SAME_PROVIDER_NONBINDING
  - DISTINCT_BROWSER_VERIFIER_CHROMIUM_FIREFOX
expiry_utc: 2026-08-10T13:32:18Z
fitness_credit: 0
privacy_class: PUBLIC_PRIMARY_SOURCES_ONLY
---

# S08 evidence card — Hextris synthetic keyboard boundary

## Bounded uncertainty

For exact candidate `Hextris/hextris@3f4847dc8fd7dab3d1c87e6324b9159d92fbd396`, can a spatial producer portably emit standards-based synthetic `KeyboardEvent` objects into the existing `keypress` library and obtain one left/right rotation without changing the game input code?

## Primary evidence checked on 2026-08-03

1. Exact game input source: <https://github.com/Hextris/hextris/blob/3f4847dc8fd7dab3d1c87e6324b9159d92fbd396/js/input.js> — registers `left`, `right`, `a`, and `d` combos; callbacks guard on `MainHex && gameState !== 0` and then call `MainHex.rotate(1)` or `MainHex.rotate(-1)`.
2. Exact vendored keyboard dependency: <https://github.com/Hextris/hextris/blob/3f4847dc8fd7dab3d1c87e6324b9159d92fbd396/vendor/keypress.min.js> — identifies itself as Keypress 1.0.8; attaches `keydown` and `keyup` listeners to `document.body`; resolves keys by passing `event.keyCode` through a static numeric map before invoking registered combos.
3. Current UI Events specification: <https://w3c.github.io/uievents/#interface-keyboardevent> and <https://w3c.github.io/uievents/#dictdef-keyboardeventinit> — `KeyboardEventInit` standardizes `key`, `code`, `location`, `repeat`, and `isComposing`; it does not provide a constructor member for legacy `keyCode`. The supplemental legacy model defines `keyCode` as readonly and system- and implementation-dependent.
4. Current DOM Living Standard, last updated 2026-07-18 when checked: <https://dom.spec.whatwg.org/#dom-event-istrusted> and <https://dom.spec.whatwg.org/#dom-eventtarget-dispatchevent> — script-created/dispatched events have `isTrusted == false`; `dispatchEvent()` delivers a synthetic event to listeners but does not convert it into a user-agent keyboard occurrence.

## Supported claims

- Hextris does not consume the standardized `KeyboardEvent.key` or `KeyboardEvent.code` fields in its vendored keyboard path. Keypress 1.0.8 gates recognition on numeric `event.keyCode`.
- A standards-only call such as `new KeyboardEvent('keydown', {key: 'ArrowLeft', code: 'ArrowLeft', bubbles: true})` has no specified constructor mechanism to initialize the legacy readonly `keyCode` value required by this dependency.
- Therefore a portable cross-browser claim that standards-based synthetic keyboard events will drive Hextris unchanged is unsupported.
- The lower-risk adapter strategy is to extract the existing guarded rotation callbacks into one explicit command function and have both native keyboard/touch handlers and the spatial producer call that function.
- Native keyboard and touch fallback can remain present; the revision changes the command seam, not the ordinary-input availability.

## Excluded claims

- No browser execution, DevTools inspection, automated test, mobile test, or spatial producer integration occurred in this pass.
- This card does not claim synthetic keyboard delivery is impossible in every browser. Engine-specific `keyCode` behavior, deprecated constructors, property overrides, test-driver APIs, or automation frameworks may make particular demonstrations work.
- A one-browser demonstration using a `keyCode` hack would not prove a standards-based portable adapter.
- Directly calling `MainHex.rotate()` without preserving the current `gameState` guard is not admitted.
- The optional speed-up path is excluded from this card because it has stateful `keydown`/`keyup` balance and multiplicative `window.rush` behavior requiring a separate cancellation/idempotency review.
- No demand, buyer, revenue, distribution, accessibility, production-readiness, or current-browser compatibility claim is supported.

## License and terms uncertainty

The repository declares `GPL-3.0-or-later`. Refactoring `js/input.js` or adding a command adapter to a conveyed browser bundle remains inside the prior GPL-preserving boundary: notices, corresponding source, modification marking, and applicable copyleft duties must be maintained. Asset, vendored-dependency, branding, and trademark provenance remain unresolved from the prior candidate card. This adapter finding neither clears nor worsens those uncertainties.

## Smallest admissible next experiment

Create one WorkItem against the exact SHA with no publication:

1. add a tiny command boundary such as `rotateCommand(direction)` that preserves the existing `MainHex` and `gameState` guard;
2. route existing left/right keyboard callbacks and `handleClickTap()` through that same command boundary;
3. let the spatial producer invoke only the command boundary, not synthesize keyboard events;
4. add deterministic traces proving native left, native right, spatial left, and spatial right each produce exactly one matching rotation;
5. include negative traces for paused or unavailable `MainHex`, duplicate producer emissions, and accidental double routing through both synthetic and direct paths;
6. separately probe the standards-only synthetic `KeyboardEvent` constructor in current Chromium and Firefox and record observed `keyCode`, callback invocation, and rotation count as evidence, not as the admitted production path.

## Cost and operator load

- This research pass: surfaced spend `$0`; operator minutes `0`.
- Proposed command-seam refactor and deterministic traces: `20–40` producer minutes.
- Distinct two-browser verification: `15–30` verifier minutes.
- Operator action: `0` unless later publication, branding, or proprietary licensing is requested.

## Strongest objection

A direct command seam modifies upstream code and can drift from native behavior, while a synthetic event appears cheaper. The answer is to make native handlers consume the same extracted command function; otherwise the system maintains two behavioral paths and creates duplicate-rotation risk. The standards contract does not justify depending on a readonly legacy `keyCode` field that the exact dependency requires.

## Falsifier

Revise this card toward `ADMIT_SYNTHETIC_KEYBOARD` only if a distinct verifier demonstrates, in clean current Chromium and Firefox at the exact SHA, that a standards-only `KeyboardEvent` constructor using documented fields—without deprecated constructors, `keyCode` mutation, property overrides, browser automation privilege, or source modification—reliably invokes the Keypress 1.0.8 left/right combos exactly once. Return `RETIRE` for the command-seam proposal if extracting the guarded function changes native behavior or deterministic traces cannot prevent duplicate or reversed rotations.

## Decision

`REVISE` — retire the unchanged synthetic-keyboard injection strategy from the default adapter path. Preserve native fallback, but consume Hextris through one explicit guarded rotation command shared by native and spatial producers. Research volume and candidate count earn no credit. Fitness remains `0` until a named WorkItem consumes this exact card, a distinct verifier binds a verdict to the resulting digest, and the consumer acknowledges it.

## Honest flaw

This is a source-and-specification boundary review, not runtime proof. Browser-specific legacy behavior may differ, and the exact refactor cost remains an estimate until a clean checkout is executed.
