---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_SYNTHETIC_POINTER_TARGET_CONTINUITY_20260801T062903Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_evidence: RUNTIME_INSTRUCTION_CLAIM_NOT_NATIVE_TASK_READBACK
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T06:29:03Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
work_item_state_observed: PRIOR_CLAIM_LEASE_EXPIRED_AWAITING_EXACT_REQUEUE
research_lane: interaction_input_adapters
question_change_basis: fee50a7_added_a_concrete_dispatchSample_implementation_that_retargets_each_descriptor_by_elementFromPoint
privacy_class: PUBLIC_STANDARDS_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
expiry_utc: 2026-08-08T06:29:03Z
expiry_conditions:
  - TTaoGaming/TAGS target head or adapter blob changes
  - target-selection or activation contract changes
  - direct browser evidence contradicts this card
  - a new WorkItem binds a different interaction policy
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumers:
  - next_S02_admission_for_SPATIAL_FACTORY_GOLDEN_APP_001
  - Olrun/Claude-Dispatch
  - next_S06_executor_packet
sealed: false
---

# S08 evidence card — synthetic pointer target continuity

## Bounded uncertainty

Can `TTaoGaming/TAGS@fee50a70188b510695e8e5fad2ebadc6cba0535a` rely on browser implicit pointer capture after script-dispatching a synthetic touch-like `pointerdown`, while resolving every later descriptor with `document.elementFromPoint()`?

## Decision

`REVISE` before the exact adapter is re-admitted as satisfying target-specific pinch activation.

The current implementation script-dispatches untrusted events and independently hit-tests each `pointermove`, `pointerdown`, and `pointerup`. It does not establish a standards-backed active pointer or implicit capture. A pinch that begins on target A and releases over target B can therefore split its event sequence across targets. The next packet must bind an explicit adapter-level target-continuity policy and test it; it must not claim that synthetic dispatch inherits native touch capture.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
native_task_read_surface_exposed: false
task_identity_conclusion: expected_ID_present_in_runtime_instruction_but_not_independently_read_back
tools_observed:
  github_connector: read_write
  slack_connector: read_write
  web_primary_standards: read
  native_shell_or_browser_runtime: unavailable
```

## Exact candidate and changed queue evidence

```yaml
target_repository: TTaoGaming/TAGS
target_commit: fee50a70188b510695e8e5fad2ebadc6cba0535a
adapter_path: prototypes/spatial-input-adapter.js
adapter_blob: c90a715c72735f0c04d60c91cd9c9afb0f2ddec4
test_path: tests/spatial-input-adapter.test.mjs
test_blob: 9416a2e34c331ab46dd2f04c8d8664dbc0088405
prior_S08_dependency_card_blob: 1634672ccaf06025759429c0f8347cac659eb3cf
prior_claim_blob: f90e3797b4e5aa398aa386e555e26b53ae27cfc5
prior_claim_lease_expired_utc: 2026-08-01T04:06:07Z
operator_packet_authority_expires_utc: 2026-08-03T17:57:17Z
```

Exact repository readback shows:

- `dispatchSample()` calls `resolveTarget()` separately for every descriptor.
- Without an injected fixed `config.target`, `resolveTarget()` calls `document.elementFromPoint(clientX, clientY)`.
- No pressed target is retained between pinch-down and pinch-up.
- No adapter-level capture, cancel-on-leave policy, release-inside policy, or injected activation function is present.
- The current unit test uses one constant injected target. It does not test A-at-down/B-at-up movement, target removal, capture continuity, or activation ownership.

Source pointers:

- https://github.com/TTaoGaming/TAGS/blob/fee50a70188b510695e8e5fad2ebadc6cba0535a/prototypes/spatial-input-adapter.js
- https://github.com/TTaoGaming/TAGS/blob/fee50a70188b510695e8e5fad2ebadc6cba0535a/tests/spatial-input-adapter.test.mjs

## Primary/current standards evidence — observed 2026-08-01

1. The WHATWG DOM Standard defines `dispatchEvent()` as dispatching a synthetic event to the target chosen by the caller and initializes `isTrusted` to false. It does not state that author dispatch creates a hardware pointer or runs the user agent's input-device state machine: https://dom.spec.whatwg.org/#dom-eventtarget-dispatchevent
2. W3C Pointer Events Level 3 is a Recommendation dated 2026-06-30. Its user-agent firing algorithm uses pointer-capture override or normal hit testing, and implicit capture is tied to a user agent firing `pointerdown` for an associated direct-manipulation device: https://www.w3.org/TR/2026/REC-pointerevents3-20260630/#firing-events-using-the-pointerevent-interface
3. `setPointerCapture(pointerId)` is effective only when the pointer is in active-buttons state and the element's document is the pointer's active document. Script-dispatching a `PointerEvent` with `buttons: 1` does not by itself prove those user-agent states exist: https://www.w3.org/TR/2026/REC-pointerevents3-20260630/#setting-pointer-capture
4. Pointer Events reserves `pointerId: -1` for events generated by something other than a pointing device. The current adapter defaults to `pointerId: 1`, so it must not imply that the synthetic stream is a native touch pointer: https://www.w3.org/TR/2026/REC-pointerevents3-20260630/#dom-pointerevent-pointerid

## Supported claims

- Synthetic descriptors may still be useful for notifying application listeners.
- The adapter may use its own deterministic target state without adding a package or privileged browser API.
- A safe requeue can require one of these explicit policies:
  - **press-target continuity:** retain the target selected at pinch-down and route held moves plus release to it;
  - **release-inside:** retain the press target but activate only when release hit-testing still resolves inside the accepted target;
  - **cancel-on-leave:** emit a bounded cancel transition and zero activation after leaving the accepted target.
- The chosen policy must be injected or documented, deterministic, reset-safe, and covered by a two-target test.

## Excluded claims

- No claim that synthetic `pointerdown` creates an active browser pointer, implicit capture, trusted input, focus, user activation, compatibility mouse events, or a click.
- No claim that `setPointerCapture()` will work for this synthetic stream without direct browser proof.
- No browser, build, test, branch mutation, activation, merge, deployment, publication, or ConsumerAck was performed.
- This card does not renew the expired S02 claim or authorize producer work by itself.

## License and terms uncertainty

This behavioral revision uses browser standards and internal state only; it introduces no third-party runtime dependency or new license acceptance. The prior missing-root-license and provenance uncertainty for public distribution is unchanged. This is engineering evidence, not legal advice.

## Cost and operator burden

```yaml
direct_cost_usd_observed: 0
operator_minutes_used_observed: 0
operator_minutes_removed_measured: 0
estimated_producer_revision_minutes: 10_to_20
estimated_review_rework_avoided: 10_to_15
estimate_status: HEURISTIC_ZERO_FITNESS_UNTIL_CONSUMED
new_credentials_required: 0
new_packages_required: 0
```

## Strongest objection

The current adapter already supports a fixed injected `config.target`; a narrow FAB integration could avoid target drift by always supplying that target. That objection is valid for one fixed control, but it does not rescue the default `elementFromPoint()` path or prove target-specific activation. The packet must explicitly choose the fixed-target mode or implement a general continuity policy; silent reliance on browser capture remains unsupported.

## Falsifier

Change this result if a direct clean-browser test, bound to the exact adapter blob and supported browser matrix, proves all of the following:

- script-dispatched down/move/up consistently retain the intended target after crossing into another element;
- the behavior does not depend on unexposed native pointer state;
- exactly one target-specific activation occurs under the declared release policy;
- invalid, held, canceled, removed-target, and cross-target cases produce the specified zero-or-one effects.

Immediate `RETIRE` conditions include claiming trusted/native capture from synthetic dispatch, allowing one pinch to activate two targets, or marking the interaction PASS using only the current constant-target Node test.

## Consumer action

The next S02/S06 packet should consume or reject this card explicitly. Minimum added acceptance test: target A at pinch-down, target B under the release coordinate, and an assertion that only the declared policy's target receives held/release/activation effects. Until then, preserve the exact `fee50a7` code as an expired partial candidate, not a completed golden-app interaction.

## Honest flaw

This carrier inspected exact Git blobs and primary standards but had no browser or shell execution surface. The conclusion that synthetic dispatch does not establish browser pointer state is standards-grounded, but actual browser edge behavior was not executed. The estimated minutes are unmeasured and earn no credit unless a WorkItem consumes the card.
