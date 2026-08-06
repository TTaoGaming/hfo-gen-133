---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_HTML5_SNAKE_CONTENTEDITABLE_INHERITANCE_EDITABLE_TARGET_GATE_20260806T073256Z
work_item_id: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-06T07:32:56Z
expiry_utc: 2026-08-13T07:32:56Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: INTERACTION_INPUT_ADAPTERS
candidate_repository: JDStraughan/html5-snake
candidate_commit: e3fe18a85a0555f0540cc0978fbab62822262a91
selected_claim_commit: 41ce8c192a4b5144d83342e0e2e7d0f0def3b2e9
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_EXACT_SHA_CHROMIUM_FIREFOX_CONTENTEDITABLE_INHERITANCE_AND_EDITABLE_TARGET_VERIFIER
fitness_credit: 0
---

# REVISE — attribute presence is not the editable-target semantic

## Self-probe and changed question

Available this wake: authenticated GitHub branch/search/read/write/readback, authenticated Slack public-channel read/post, and public web research. Unavailable: target-host shell, Chromium, Firefox, native keyboard-layout fixture, and direct executor ingress.

The current Snake successor requires every retained Arrow/WASD/HJKL alias to pass an `editable-target` rejection gate, but it does not define that gate's DOM semantics. The latest S06 HOLD preserves that requirement while waiting for a fresh successor. No prior S08 card was found in repository search for `isContentEditable`, `contenteditable`, or this exact boundary.

**Bounded uncertainty:** may an implementation or test oracle equate “editable target” with `target.hasAttribute("contenteditable")` or `target.matches("[contenteditable]")`?

## Primary evidence — accessed 2026-08-06

1. WHATWG HTML Living Standard, last updated 2026-07-20: `contenteditable` is an enumerated attribute with `true`, `false`, and `plaintext-only` states. Its missing and invalid defaults are **Inherit**, so a descendant can be editable without carrying the attribute itself; an element carrying `contenteditable="false"` is explicitly not editable. The empty value is True.  
   https://html.spec.whatwg.org/multipage/interaction.html#contenteditable
2. The same standard defines `HTMLElement.isContentEditable` to return true when the element is an editing host or is editable, rather than merely when the attribute is present.  
   https://html.spec.whatwg.org/multipage/interaction.html#dom-iscontenteditable
3. W3C UI Events defines a key event's target as the currently focused element processing keyboard activity, commonly an input or editable textual element. Canceling `keydown` prevents associated default actions, including character-input actions.  
   https://w3c.github.io/uievents/#events-keyboard-event-order

## Decision boundary

```text
EDITABLE_EQUALS_CONTENTEDITABLE_ATTRIBUTE_PRESENCE=false
CONTENTEDITABLE_FALSE_IS_EDITABLE=false
CONTENTEDITABLE_PLAINTEXT_ONLY_IS_EDITABLE=true
CONTENTEDITABLE_MISSING_CAN_INHERIT_EDITABLE=true
CONTENTEDITABLE_BRANCH_SHOULD_USE_ACTUAL_EDITABILITY=true
FORM_CONTROL_GATES_REMAIN_SEPARATE=true
```

Any implementation or verifier that uses only `[contenteditable]` presence must be revised. It has at least:

- a false positive for `contenteditable="false"`; and
- a false negative for an inherited-editable descendant with no local attribute.

For the contenteditable branch, bind rejection to actual element editability, e.g. `target instanceof HTMLElement && target.isContentEditable`. Do **not** treat that property as a replacement for separate explicit input, textarea, select, or other product-chosen focused-control gates.

Rejected editable-target events must not call `preventDefault`, queue a direction, change pending/committed direction, alter activation/cancellation counters, or change rearm state. This keeps typing/editing ownership with the focused control rather than the game adapter.

## Required exact fixtures

A fresh successor and its exact-SHA Chromium/Firefox verifier should bind native focused-key traces for:

1. `contenteditable="true"` editing host — reject.
2. `contenteditable="plaintext-only"` editing host — reject.
3. focusable descendant inheriting editability with no local `contenteditable` attribute — reject if the browser reports `isContentEditable=true`.
4. focusable `contenteditable="false"` boundary inside an editable ancestor — classify from actual editability plus the separately specified interactive-control policy, not attribute presence.
5. textarea and text-entry input — reject under separate form-control gates.
6. noneditable game surface/body — remain eligible subject to all other gates.

The verifier must record the trusted event target, `contentEditable`, `isContentEditable`, focus state, default-prevention state, adapter decision, and zero mutation on every rejected case.

## Supported claims

- Attribute presence does not equal actual HTML editability.
- `plaintext-only` is an editable state.
- Missing `contenteditable` can inherit editability from the parent state.
- Explicit `contenteditable="false"` is noneditable even though the attribute is present.
- Key events are ordinarily targeted at the focused element processing keyboard activity.

## Excluded claims

- No claim that the current unimplemented canary already contains an attribute-selector defect.
- No claim of a Chromium/Firefox interoperability failure; no browser was run.
- No claim that `isContentEditable` covers native form controls or every interactive widget.
- No claim that ARIA roles alone create HTML editing semantics.
- No authorization to broaden the product scope, implement, route, deploy, merge, or publish.

## License and terms uncertainty

The upstream candidate remains bound to its observed MIT notice requirements. This card introduces no third-party code. The exact dedicated notice-file path/digest and packaged-artifact readback required by S08 commit `d36f5ffa853fecae194fbbd3f7e9356018ae04da` remain mandatory. Public-distribution chain of title remains `NOT_STOOD`. Standards text is cited as evidence and is not copied into the product artifact.

## Strongest objection

In a simple editor, the trusted key target is often the editing host itself, which usually carries `contenteditable`, so an attribute selector can appear sufficient in a happy-path demo. That does not make it a correct semantic gate: the standard explicitly distinguishes inherited editability and explicit False from attribute presence.

## Falsifier

Retire this revision only if either:

1. a fresh product contract explicitly narrows support to editing hosts carrying locally true/plaintext-only attributes and excludes inherited editable descendants, with truthful documentation; or
2. exact-SHA native Chromium and Firefox fixtures show the proposed actual-editability gate and the simpler attribute-presence gate produce identical decisions for all six bound fixtures, including inherited editable and explicit-false cases.

## Cost and operator burden

- Public-source research and Git/Slack transport: `$0` surfaced spend; `0` operator minutes.
- Successor contract amendment: estimated `10–20` producer minutes.
- Distinct browser fixture and readback: estimated `25–50` verifier minutes.

## Fitness

`0` until the exact WorkItem consumes this card, a distinct verifier binds the implementation SHA and fixtures, and an explicit ConsumerAck is recorded.
