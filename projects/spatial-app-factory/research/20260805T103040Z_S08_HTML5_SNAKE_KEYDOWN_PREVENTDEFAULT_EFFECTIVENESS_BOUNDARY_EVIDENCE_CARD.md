---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-05T10:30:40Z
expiry_utc: 2026-08-12T10:30:40Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: INTERACTION_INPUT_ADAPTERS
bounded_uncertainty: >-
  Is the current Snake acceptance clause "accepted focused commands call preventDefault exactly once"
  sufficient to prove that the native Arrow-key default action was actually canceled, and is an explicit
  addEventListener({passive:false}) option required for keydown?
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_CHROMIUM_FIREFOX_KEYDOWN_CANCELATION_FIXTURE_VERIFIER
fitness: 0_PENDING_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# S08 evidence card — keydown `preventDefault()` effectiveness boundary

## Exact candidate and changed question

- WorkItem: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`.
- Fresh successor claim: `TTaoGaming/hfo-gen-133@8d8ede0222511e3543223cceab1440e6bf2f21ab`,
  `projects/spatial-app-factory/claims/20260805T100853Z_SPATIAL_FACTORY_HTML5_SNAKE_POINTER_IDENTITY_ARCHIVE_MAINTENANCE_SUCCESSOR.claim.yaml`,
  blob `981b7bd21c4e1409e6c9b2fb0ed391d9ac9849dc`, acceptance digest
  `64a3be61b13d8780dac9de4b7c526fd961209c60386247b0a858b0eb05304975`.
- Target base: `TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498`.
- Upstream source remains `JDStraughan/html5-snake@e3fe18a85a0555f0540cc0978fbab62822262a91`.
- Changed acceptance surface: accepted focused native Arrow commands must call `preventDefault()` exactly once.

## Primary evidence, accessed 2026-08-05

1. WHATWG DOM defines successful cancellation as requiring both `event.cancelable=true` and execution outside a passive listener; otherwise `preventDefault()` does not set the canceled flag and `defaultPrevented` remains false.
   https://dom.spec.whatwg.org/#dom-event-preventdefault
2. WHATWG DOM's default-passive algorithm returns true only for `touchstart`, `touchmove`, `wheel`, and `mousewheel` on specified root targets; `keydown` therefore defaults to non-passive when the option is omitted.
   https://dom.spec.whatwg.org/#default-passive-value
3. W3C UI Events defines trusted `keydown` as synchronous, bubbling, composed, and cancelable. Canceling it prevents its associated default actions.
   https://www.w3.org/TR/uievents/#event-type-keydown

## Finding

`addEventListener("keydown", handler)` does **not** need an explicit `{passive:false}` option under the current DOM standard: `keydown` is outside the event types that default to passive. A trusted native `keydown` is also specified as cancelable.

However, a call-count assertion alone does not prove effective cancellation. A test harness can construct a synthetic `KeyboardEvent` with the default `cancelable=false`; `preventDefault()` may then be called exactly once while `defaultPrevented` remains false. Likewise, any wrapper that explicitly registers the handler with `passive:true` defeats cancellation.

## Required revision

Classify the contract as:

```text
NATIVE_KEYDOWN_DEFAULT_PASSIVE=false
TRUSTED_KEYDOWN_CANCELABLE=true
EXPLICIT_PASSIVE_FALSE_OPTION=OPTIONAL_HARDENING
PREVENTDEFAULT_CALL_COUNT_ALONE=INSUFFICIENT_VERIFICATION
ACCEPTED_COMMAND_MUST_END_WITH_DEFAULT_PREVENTED_TRUE
PASSIVE_TRUE_KEYDOWN_REGISTRATION=FORBIDDEN
```

Amend the acceptance test, not the direct-command architecture:

- Retain exactly one `preventDefault()` call only after all rejection gates pass.
- Assert `event.defaultPrevented === true` for every accepted native Arrow command.
- Synthetic test fixtures must set `cancelable:true`; a fixture with omitted or false `cancelable` is a negative control, not proof of default-action suppression.
- Reject or statically flag `passive:true` on the keydown registration path.
- Explicit `{passive:false}` may be used for audit clarity, but is not required by the standard for `keydown`.
- Rejected commands must not call `preventDefault()` and must leave `defaultPrevented` unchanged.

## Supported claims

- Omitted passive options do not make `keydown` passive by default under the current DOM Standard.
- Trusted `keydown` is specified as cancelable.
- `defaultPrevented=true` is stronger evidence of effective cancellation than method-call count alone.

## Excluded claims

- No claim that every browser build is conformant without exact Chromium and Firefox traces.
- No claim that framework or helper wrappers preserve omitted/non-passive listener options.
- No claim that a synthetic event proves trusted-user input semantics.
- No claim that canceling one keydown suppresses every host-OS or browser-reserved shortcut.
- No implementation, browser execution, target checkout, or test run occurred.

## License and terms uncertainty

- No code or substantial specification text is copied; the standards are used as reference evidence only.
- WHATWG and W3C document-license terms were not audited for derivative redistribution because no derivative specification content is being shipped.
- Upstream Snake MIT packaging and public-distribution chain-of-title remain governed by the existing exact-pin evidence; this card changes neither.

## Cost and operator-minute estimate

- This research pass: `$0`, `0 operator minutes`.
- Acceptance/test amendment: `5–10 producer minutes`.
- Deterministic cancelable/noncancelable fixtures: `10–20 minutes`.
- Distinct Chromium and Firefox verification: `20–40 minutes`.

## Strongest objection

The WorkItem already limits the runnable path to trusted native keydown and forbids synthetic keyboard dispatch, so the standards imply cancellation will work without more contract text. Response: runnable semantics may be correct, but the existing verifier could still pass a noncancelable synthetic fixture by observing only one method call. The revision closes a verification false-green without adding a new runtime dependency.

## Falsifier

Retire this revision if an exact-sha implementation and distinct Chromium/Firefox verifier demonstrate all of the following without the added assertion: accepted native Arrow events always finish with `defaultPrevented=true`; rejected events never become canceled; the listener is never passive; synthetic fixture cancelability is explicitly bound; and no false-green can pass by counting `preventDefault()` calls alone.

## Decision

`REVISE`

The command seam remains valid. Tighten the acceptance oracle from "called once" to "called once and cancellation took effect."
