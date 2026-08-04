---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_HTML5_SNAKE_KEYBOARD_FOCUS_DEFAULT_ACTION_OWNERSHIP_20260804T092907Z
work_item_id: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
lane: INTERACTION_INPUT_ADAPTERS
wip: 1
seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-04T09:29:07Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_BROWSER_CAPABLE_NONPRODUCER
expiry_utc: 2026-08-11T09:29:07Z
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERDICT_AND_CONSUMER_ACK
---

# S08 evidence card — Snake keyboard commands need an explicit focus and default-action ownership boundary

## Self-probe and changed-question selection

- Expected and observed carrier task ID match: `6a526109ba348191b5f23ad3172ad568`.
- Available surfaces used: authenticated GitHub branch/file/commit reads, immutable GitHub file creation, exact post-write readback, public Slack duplicate search, and current public web specifications.
- Unavailable or unused: target checkout, host shell, browser runtime, Codex/Claude executor ingress, private credentials, task mutation, deployment, merge, publication, outreach, application, purchase, or spend.
- Prior lane completed: `SPATIAL_FOSS_CANDIDATES_AND_LICENSES` at commit `8f9e5d94d513af3fc60e4b9c943fc5ee5d8999e6`.
- Rotated lane: `INTERACTION_INPUT_ADAPTERS`.
- Changed source: the fresh successor claim at commit `0aea1b7dd922c747a67fdc0a38ba9fb0a727b77b`, blob `d1d545e6594aa53be7251e71eab39c727d1ee1c3`, acceptance digest `f93d177ce6fde7cbdefa0083ffa4c8ab252a49fc55a4a02c99fc7167352fba2c`, which requires native keyboard and spatial input to share `requestDirection(nextDirection)` but does not yet define who owns keyboard events or browser default actions.
- Duplicate probe: no repository or control-channel evidence card was found for the exact `html5-snake + focus + preventDefault/default-action ownership` question.

## Bounded uncertainty

Can the internal Snake canary safely preserve the upstream window-level `keydown` handler while adding the shared direction seam, or must keyboard command handling be scoped to an explicitly focused game surface with selective default-action cancellation?

This card addresses only keyboard-event ownership, focus, and cancellation. It does not decide the separate `KeyboardEvent.key` versus `KeyboardEvent.code` mapping policy, spatial classifier thresholds, provenance, public distribution, or demand.

## Exact candidate and current source bytes

- Upstream: `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91`.
- `game.js` blob: `c286389487bd68f15170fbb3add6a060f252d169`.
- `index.html` blob: `61243962bab6846c3e06dba4358a547755dc1379`.
- Target base: `TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498`.
- Allowed target subtree: `prototypes/html5-snake-spatial-canary/**`.
- Live consumer claim: `0aea1b7dd922c747a67fdc0a38ba9fb0a727b77b` / `d1d545e6594aa53be7251e71eab39c727d1ee1c3`.

The exact upstream script installs an unscoped classic-script listener:

```js
addEventListener("keydown", function (e) {
    lastKey = keys.getKey(e.keyCode);
    // direction or start-game mutation
}, false);
```

It does not inspect `event.target`, `document.activeElement`, `event.defaultPrevented`, `event.isComposing`, or modifier state, and it never calls `preventDefault()`. The exact HTML contains links plus a bare `<canvas id="the-game">` with no `tabindex` or explicit keyboard-focus contract.

Primary bytes:

- https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js
- https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/index.html

## Dated primary/current evidence

Observed 2026-08-04:

1. W3C UI Events states that a key event targets the currently focused element; when no suitable element is focused, the target can fall back to the body or root. It classifies `keydown` as cancelable, with default actions that vary by key and context, including activation, focus changes, composition, and other host behavior. If `keydown` is canceled, its associated default actions must not be performed.
   - https://www.w3.org/TR/uievents/#events-keyboard-event-order
   - https://www.w3.org/TR/uievents/#event-type-keydown
   - https://www.w3.org/TR/uievents/#keys-cancelable-keys
2. The WHATWG HTML living standard states that `tabindex="0"` makes an element a focusable area and indicates that it should participate in sequential focus navigation. It also notes that the deepest active element is where key events are routed.
   - https://html.spec.whatwg.org/multipage/interaction.html#the-tabindex-attribute
   - https://html.spec.whatwg.org/multipage/interaction.html#dom-documentorshadowroot-activeelement
3. The current HTML canvas section requires accessible fallback content for interactive canvases and describes focused fallback descendants as keyboard-event targets. This supports an explicit focus model rather than document-wide implicit keyboard ownership.
   - https://html.spec.whatwg.org/multipage/canvas.html#best-practices
4. W3C WCAG 2.1 guidance requires keyboard-operable functionality and prohibits trapping keyboard focus. Therefore any focus gate must preserve a standard way to leave the game surface; canceling `Tab` globally would be a regression.
   - https://www.w3.org/WAI/WCAG21/Understanding/keyboard.html
   - https://www.w3.org/WAI/WCAG21/Understanding/no-keyboard-trap.html
5. W3C CSS Spatial Navigation documents a concrete standards context in which arrow-key `keydown` may otherwise drive navigation or scrolling, and states that canceling the event prevents those navigation steps. This is not proof that every browser always scrolls on every arrow key; it is proof that arrow keys can have host navigation behavior that competes with an in-page game command.
   - https://www.w3.org/TR/css-nav-1/#interaction

## Supported claims

- The exact upstream handler claims document/window-wide keyboard events, not only events intentionally directed to the game.
- The current source has no explicit keyboard-focus owner for the canvas/game surface.
- `keydown` is cancelable, and recognized game keys can have browser or host default actions unless the handler selectively cancels them.
- A focused game surface can be created with standard focus APIs; keyboard ownership can be limited to that surface.
- Selective cancellation after recognizing an owned game command is materially safer than unconditional document-wide cancellation.
- `Tab` and an exit path must remain uncanceled so keyboard users can leave the game surface.

## Excluded claims

- Every current browser necessarily scrolls the page for every arrow-key event in this exact page.
- Calling `preventDefault()` globally is safe.
- A focusable canvas alone satisfies all canvas accessibility requirements.
- This card proves screen-reader usability, mobile keyboard behavior, gamepad behavior, or full WCAG conformance.
- This card resolves whether letter controls should use `KeyboardEvent.key`, `KeyboardEvent.code`, or both.
- An event arriving at the window is evidence that the user intended to control the game.

## License and terms uncertainty

This input-boundary amendment is independently authored behavior and does not change the existing source classification:

`VISIBLE_MIT_GRANT; KNOWN_LATER_CREDITED_COMMITS_EXCLUDED; PREEXISTING_FILE_ORIGIN_NOT_FULLY_AUDITED; INTERNAL_ONLY_PENDING_PROVENANCE_REVIEW`

The complete visible MIT notice must remain preserved. Public-distribution chain of title remains `NOT_STOOD`. No browser, platform, or accessibility terms acceptance is required for this internal code change, but no compliance certification is claimed.

## Decision — `REVISE`

Do not preserve the window-wide handler as the command-ownership boundary.

Revise the canary so native keyboard commands are accepted only while an explicit game surface owns focus, and cancel browser default behavior only for a recognized, accepted game key inside that ownership boundary.

## Smallest required amendment

1. Give the game root or canvas an explicit focus contract, minimally `tabindex="0"`, a visible focus indicator, and concise keyboard instructions accessible from the same surface.
2. Attach the keyboard listener to that surface, or enforce an equivalent strict boundary using `document.activeElement` containment. A window listener without an active-owner gate is not acceptable.
3. Before mapping or calling `requestDirection`:
   - return if `event.defaultPrevented` is already true;
   - return while `event.isComposing` is true;
   - return for `Ctrl`, `Alt`, or `Meta` modified commands unless a separately documented binding requires them;
   - return when the event target is an editable control or content-editable region;
   - preserve the existing `event.repeat === true` rejection.
4. After recognizing an owned direction or restart key, call `preventDefault()` exactly once before command mutation. Do not cancel unrecognized keys.
5. Never cancel `Tab`; preserve a standard focus-exit path. Do not claim exclusive keyboard capture.
6. On focus loss, clear any pending native direction so a command accepted before blur cannot commit after focus is regained. Do not mutate the already committed movement direction.
7. Keep the spatial producer on the same `requestDirection(nextDirection)` seam; spatial activation must not synthesize keyboard events or acquire keyboard focus as a side effect.

## Required deterministic/browser checks

- With focus on the game surface, each accepted Arrow/WASD/HJKL command calls `requestDirection` at most once and reports `defaultPrevented === true` to the browser harness.
- With focus on the page body, a link, a test input, a textarea, or a content-editable fixture, the same keys produce zero game commands.
- Unrecognized keys, `Tab`, and modified browser shortcuts produce zero game commands and are not canceled by the game handler.
- `repeat=true`, `isComposing=true`, and already-`defaultPrevented` events produce zero `requestDirection` calls.
- Blur between command acceptance and movement tick clears the pending command; refocus alone does not replay it.
- Arrow-key scroll or host-navigation behavior is measured before and after selective cancellation in at least Chromium and Firefox; Safari remains `UNKNOWN` unless directly tested.
- Native and spatial traces remain parity-bound at 8 fps and 60 fps after this ownership gate.

## Strongest objection

The canary is a tiny standalone page with no form fields, and requiring click/focus before play adds friction. The existing global listener is common in small games and may work acceptably in a dedicated full-page tab.

**Response:** the exact page already contains links, the target is intended to become a reusable TAGS specimen, and the fresh successor explicitly introduces a shared input seam. This is the cheapest point to stop document-wide command capture from becoming a reusable adapter contract. The focus surface can remain keyboard reachable with `tabindex="0"`; no global keyboard trap is needed.

## Falsifier

This `REVISE` can be narrowed or retired if a distinct browser verifier demonstrates, against the exact produced specimen, that all of the following are structurally guaranteed and tested:

- the specimen always runs in an isolated, non-scrollable document with no other focusable or editable controls;
- keyboard focus cannot leave or be redirected while the game is active;
- no recognized key triggers a competing browser, host, activation, or navigation action;
- embedding into a larger page is explicitly prohibited by the consumer contract; and
- zero stale pending command can survive blur or document focus loss.

Finding that a body-, link-, or editable-target key event mutates the game, that an accepted key also scrolls/navigates/activates host UI, or that blur preserves a pending command strengthens this revision.

## Cost and operator burden

- This research run: `$0` direct spend; `0` operator minutes.
- Producer amendment: `15–30` minutes.
- Deterministic unit tests: `15–30` minutes.
- Distinct Chromium/Firefox browser verification: `20–40` minutes.
- Additional Safari verification: `15–30` minutes if a Safari-capable verifier is available.
- Operator burden: `0` minutes unless the operator later chooses a different keyboard-ownership UX.

## Honest flaw

No browser was executed in this run. The standards establish focus routing, cancelability, and the existence of competing default/host behaviors; they do not prove one universal scroll result for this exact page across all browsers. The required browser matrix remains red until a distinct verifier captures event targets, `defaultPrevented`, scroll position, activation effects, and command traces from the produced specimen.

## Effect receipt

No implementation, branch creation, browser execution, test execution, task mutation, account or terms action, outreach, application, purchase, send, spend, deployment, merge, publication, public distribution, private-data use, or demand claim occurred.
