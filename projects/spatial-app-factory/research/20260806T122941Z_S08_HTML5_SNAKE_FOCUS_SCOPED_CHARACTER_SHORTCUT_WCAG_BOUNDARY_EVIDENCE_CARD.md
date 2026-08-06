---
schema_id: hfo.gen133.s08_evidence_card.v1
result: ADMIT
card_id: S08_HTML5_SNAKE_FOCUS_SCOPED_CHARACTER_SHORTCUT_WCAG_BOUNDARY_20260806T122941Z
work_item_id: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
wip: 1
lane: INTERACTION_INPUT_ADAPTERS
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-06T12:29:41Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
expiry_utc: 2026-08-13T12:29:41Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_EXACT_SHA_CHROMIUM_FIREFOX_FOCUS_SCOPED_CHARACTER_SHORTCUT_VERIFIER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERDICT_AND_CONSUMER_ACK
sealed: false
---

# S08 evidence card — focus-scoped WASD/HJKL aliases satisfy the narrow WCAG character-shortcut exception

## Self-probe and changed-question selection

- Expected and observed task ID match: `6a526109ba348191b5f23ad3172ad568`.
- Surfaces used: native task inventory readback, authenticated GitHub search/fetch/create/readback, and current public W3C sources.
- Unavailable or unused: target checkout, shell, Chromium, Firefox, assistive-technology runtime, direct executor ingress, private data, task mutation, deployment, merge, publication, send, spend, purchase, account action, terms acceptance, outreach, or application.
- Rotated lane: `INTERACTION_INPUT_ADAPTERS`.
- Duplicate probe: no Gen-133 card was found for the exact `html5-snake + WCAG 2.1.4 character shortcuts + active-only-on-focus exception` question.

## Bounded changed uncertainty

The current successor requires preservation of the upstream Arrow, WASD, and HJKL instructions while retaining the predecessor focus-ownership gate. Does preserving the character aliases require a separate disable/remap setting, or can the canary rely on the WCAG 2.1.4 exception for shortcuts that are active only when their user-interface component has focus?

## Exact candidate and changed contract

- Upstream: `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91`.
- `game.js` blob: `c286389487bd68f15170fbb3add6a060f252d169`.
- `index.html` blob: `61243962bab6846c3e06dba4358a547755dc1379`.
- Current successor claim: `TTaoGaming/hfo-gen-133@01ee0d85928b9dd0c916373c4d1862e693bca072`.
- Claim path: `projects/spatial-app-factory/claims/20260806T121000Z_SPATIAL_FACTORY_HTML5_SNAKE_PAGE_CSS_PROVENANCE_SUCCESSOR.claim.yaml`.
- Claim acceptance digest observed before this card: `39c0c79b49fdcf4a189ca27f2aa0b8452d1d5fd923287633e625493235fae233`.

The frozen upstream runtime installs a document/window-level `keydown` listener and maps the letter families W/A/S/D and H/J/K/L to direction commands. The frozen HTML advertises all three keyboard families and gives the canvas no explicit `tabindex` or focus owner.

Primary candidate bytes, observed 2026-08-06:

- https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js
- https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/index.html
- https://github.com/TTaoGaming/hfo-gen-133/blob/01ee0d85928b9dd0c916373c4d1862e693bca072/projects/spatial-app-factory/claims/20260806T121000Z_SPATIAL_FACTORY_HTML5_SNAKE_PAGE_CSS_PROVENANCE_SUCCESSOR.claim.yaml

## Dated primary/current evidence

Sources observed 2026-08-06:

1. WCAG 2.1 Success Criterion 2.1.4 states that a shortcut implemented using only letter, punctuation, number, or symbol characters must be turn-off-able, remappable to include a non-printable key, **or active only when its user-interface component has focus**.
   - https://www.w3.org/TR/WCAG21/#character-key-shortcuts
2. W3C's current Understanding document explains that the focus-only exception avoids the need for a separate override when the character shortcut operates only while the relevant component has focus. It also identifies accidental speech-input activation as the primary risk of global character shortcuts.
   - https://www.w3.org/WAI/WCAG21/Understanding/character-key-shortcuts.html
3. W3C Technique G217 describes turn-off/remap as a sufficient technique when shortcuts are not focus-scoped, and separately states that a shortcut limited to a particular focused component does not need that override mechanism.
   - https://www.w3.org/WAI/WCAG21/Techniques/general/G217
4. W3C APG recommends avoiding or mitigating conflicts with browser, operating-system, and assistive-technology key assignments and making shortcut scope explicit.
   - https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/

## Decision — `ADMIT`

Admit the preserved WASD/HJKL aliases **without adding a disable/remap setting only under the already-required strict focus-owner contract**.

Required classification:

`CHARACTER_ALIASES_ADMITTED_ONLY_WHILE_EXPLICIT_GAME_COMPONENT_OWNS_FOCUS; GLOBAL_OR_BODY_SCOPED_ALIASES_NOT_ADMITTED`

## Supported claims

- W/A/S/D and H/J/K/L are character-key shortcuts within WCAG 2.1.4's scope.
- Arrow keys are non-character navigation keys and are not the bounded subject of this card.
- WCAG 2.1.4 provides three alternative compliance paths; the focus-only path does not additionally require a turn-off or remap control.
- The current WorkItem can therefore preserve the upstream letter aliases if the game is an explicit focusable component and the shortcuts produce zero commands when focus is outside that component.
- The inherited focus gate and preserved-alias contract are compatible; a separate settings UI is not required for this narrow internal canary if the focus boundary is real and browser-verified.

## Excluded claims and uncertainty

- The frozen upstream window-level listener is not admitted by this card.
- Focus on `body`, the document root, or an arbitrary page descendant is not treated as proof that a specific game component owns focus.
- This card does not certify WCAG conformance, accessibility, screen-reader behavior, speech-recognition behavior, browser-shortcut safety, or public-product readiness.
- It does not prove the produced canary already has a focusable game root, visible focus indicator, or correct focus containment.
- It does not decide `event.key` versus `event.code`; the current character-value policy remains separately bound.
- Modifier, composition, repeat, editable-target, visibility, blur/rearm, and selective `preventDefault()` gates remain mandatory predecessor requirements.

## Exact admission boundary

The producer and verifier must preserve all of the following:

1. One dedicated game component is sequentially focusable, has a visible focus indicator, and exposes concise keyboard instructions.
2. The letter aliases are accepted only when that exact component, or a deliberately bounded descendant, owns focus.
3. Focus on body/root, links, controls, editable fixtures, or any element outside the game component yields zero `requestDirection` calls and zero game-owned cancellation.
4. `Tab` and `Shift+Tab` move into and out of the component without being canceled or trapped.
5. The handler is attached to the game component or enforces equivalent exact `activeElement` containment; mere event bubbling to `window` is not ownership.
6. No global fallback silently re-enables W/A/S/D or H/J/K/L when the game is unfocused.

## Strongest objection

The specimen is a small full-page game, so adding a dedicated focus boundary can feel like unnecessary click/focus friction; the entire page might be argued to be the game component.

That objection does not clear the frozen candidate: the page already contains links, the upstream handler is window-scoped, and the target is a reusable TAGS specimen that may be embedded. The WCAG exception is strongest when the component boundary is explicit and testable, not when `body` or `window` is treated as implicit ownership.

## Falsifier

This `ADMIT` falls to `REVISE` if the exact produced artifact retains a window/document/body shortcut path without strict focus containment, if a letter alias mutates the game while focus is on any outside fixture, if focus cannot leave with standard keyboard navigation, or if the packaged instructions claim focus-scoped controls while browser traces show global activation.

It stands narrowly if a distinct verifier binds the exact implementation SHA and proves the focus matrix below in Chromium and Firefox.

## Verification contract

Verifier: `DISTINCT_EXACT_SHA_CHROMIUM_FIREFOX_FOCUS_SCOPED_CHARACTER_SHORTCUT_VERIFIER`

Minimum evidence:

- exact implementation SHA, browser versions, and packaged instruction bytes;
- visible focus state and `document.activeElement`/containment trace;
- W/A/S/D and H/J/K/L accepted exactly once while the game component owns focus;
- the same keys yield zero commands and zero game cancellation while focus is on body/root, a link, input, textarea, contenteditable fixture, and an outside focusable control;
- `Tab` and `Shift+Tab` enter and leave without trap;
- no global fallback, duplicate command, modifier leakage, composition leakage, repeat leakage, or blur replay;
- explicit `STOOD | FELL` bound to the canonical producer-return digest.

## License and terms uncertainty

- The pinned upstream README contains a visible MIT-form grant permitting modification subject to notice preservation.
- This accessibility/input boundary adds no dependency and copies no external implementation.
- The canonical MIT notice path/digest and packaged-byte readback from the current successor remain mandatory.
- Public-distribution chain of title remains `NOT_STOOD`.
- W3C documents are cited as standards/guidance; no claim of W3C endorsement or certification is made.

## Cost and operator estimate

- External spend: `$0`.
- Operator minutes this research pass: `0`.
- Contract amendment if needed: `5–10 minutes`.
- Focus-scoping implementation if missing: `10–25 minutes`.
- Chromium/Firefox focus-matrix verification: `25–50 minutes`.
- Separate assistive-technology or speech-input validation: `UNKNOWN / outside this card`.

## Consumer, expiry, and credit

- Consumer: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001` through the next exact authorized successor/acceptance amendment.
- Expiry: `2026-08-13T12:29:41Z`.
- Fitness remains `0` until exact WorkItem consumption, distinct verification, and explicit ConsumerAck.

## Honest flaw and effect record

This is a standards-and-static-bytes boundary decision. No browser, speech input, assistive technology, implementation, package, or verifier run was observed. The card admits one contract shape; it does not prove the current artifact meets it.

No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, private-data use, or demand invention occurred.
