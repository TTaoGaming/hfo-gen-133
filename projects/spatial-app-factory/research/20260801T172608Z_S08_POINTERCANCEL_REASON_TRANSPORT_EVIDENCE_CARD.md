---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_POINTERCANCEL_REASON_TRANSPORT_20260801T172608Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T17:26:08Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: interaction_input_adapters
question_change_basis: e0e3125_added_pointercancel_reason_metadata_and_node_assertions_after_1f0c0a7
privacy_class: PUBLIC_STANDARDS_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
effect_ceiling: FILE_AND_SANITIZED_SLACK_POINTER_ONLY
expiry_utc: 2026-08-03T17:26:08Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_browser_capable_nonproducer
consumer: S03_or_next_exact_SPATIAL_FACTORY_GOLDEN_APP_001_WorkItem
fitness_credit: ZERO_UNTIL_EXACT_WORKITEM_CONSUMER_ACK
binding_weight: 0
sealed: false
---

# S08 evidence card — `pointercancel` reason transport boundary

## Changed question

The prior accepted S08 wake completed `spatial_foss_candidates_and_licenses`, so the explicit lane rotation advances to `interaction_input_adapters`.

The exact candidate advanced from `TTaoGaming/TAGS@1f0c0a7831db6f4476a703856855ff7ccc4f454b` to `TTaoGaming/TAGS@e0e3125e1ef6bb33e189c91b485ec341f2d3cd52`. That delta added terminal `pointercancel` descriptors carrying a custom `reason`, a `cancellationCallback`, and Node tests that assert reasons such as `invalid-tracking`, `reset`, `disarm`, and `target-loss`.

**Bounded uncertainty:** when the default browser path calls `new PointerEvent('pointercancel', init)` with `init.reason`, do DOM listeners receive a standards-backed `event.reason`, or does the Node seam overstate browser behavior?

## Decision

`REVISE` any claim that browser-dispatched `PointerEvent` listeners receive the custom cancellation reason.

The exact adapter can retain `reason` in its internal descriptor and returned values. But `PointerEventInit` has no `reason` member, and Web IDL dictionary conversion reads only declared dictionary members. The default browser constructor therefore has no standards-backed route for copying `init.reason` onto the resulting `PointerEvent`. The injected Node `eventFactory` returns a plain object and preserves arbitrary fields, so its `reason` assertion is not browser-equivalent.

If cancellation reason is a required host contract, route it through a dedicated callback on every cancellation path or a separate purpose-named `CustomEvent` with `detail`; keep `pointercancel` itself standards-shaped.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github_connector: authenticated_read_write_and_exact_file_readback
  slack_public_channel: authenticated_write
  web_primary_sources: read
  native_browser_runtime: unavailable
  native_shell_runtime: unavailable
  private_bodies_externalized: false
  task_mutation: not_called
```

## Exact candidate and dated primary sources

Observed `2026-08-01`:

```yaml
target_repository: TTaoGaming/TAGS
base_commit: 1f0c0a7831db6f4476a703856855ff7ccc4f454b
final_commit: e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
base_adapter_blob: ca327ea46049f499d0afe1be4f9632ee086f2637
final_adapter_blob: 579c9551225f0974ed93564b6ad8bfb1abf72cf3
final_test_blob: 60ab9eb973db6e55824765e0f34005c6afb87ed9
changed_paths_exact:
  - prototypes/spatial-input-adapter.js
  - tests/spatial-input-adapter.test.mjs
```

Repository bytes:

1. Exact final adapter: https://github.com/TTaoGaming/TAGS/blob/e0e3125e1ef6bb33e189c91b485ec341f2d3cd52/prototypes/spatial-input-adapter.js
2. Exact final Node test: https://github.com/TTaoGaming/TAGS/blob/e0e3125e1ef6bb33e189c91b485ec341f2d3cd52/tests/spatial-input-adapter.test.mjs
3. Exact baseline adapter: https://github.com/TTaoGaming/TAGS/blob/1f0c0a7831db6f4476a703856855ff7ccc4f454b/prototypes/spatial-input-adapter.js
4. Exact compare: https://github.com/TTaoGaming/TAGS/compare/1f0c0a7831db6f4476a703856855ff7ccc4f454b...e0e3125e1ef6bb33e189c91b485ec341f2d3cd52

Primary/current contracts retrieved `2026-08-01`:

5. W3C Pointer Events Level 3 Candidate Recommendation Draft, `2026-05-22`: `PointerEventInit` enumerates its members and contains no `reason`; the event table defines `pointercancel` as bubbling and non-cancelable. https://www.w3.org/TR/2026/CRD-pointerevents3-20260522/
6. WHATWG Web IDL living standard: JavaScript-to-dictionary conversion iterates declared and inherited dictionary members; arbitrary object keys are not copied into the IDL dictionary. https://webidl.spec.whatwg.org/#js-dictionary
7. WHATWG DOM living standard: `CustomEvent` is the standard event mechanism for carrying custom data through `detail`. https://dom.spec.whatwg.org/#interface-customevent

## Measured findings

- The baseline adapter at `1f0c0a7` emitted no `pointercancel` and had no cancellation reason contract.
- The final adapter adds `descriptor.reason`, then passes the descriptor minus `type` into the default `PointerEvent` constructor.
- The current `PointerEventInit` contract does not define `reason`.
- Web IDL dictionary conversion looks up declared members, so an undeclared `reason` key has no standards-defined destination in the constructed event.
- The Node test injects `eventFactory: (type, init) => ({ type, isTrusted: false, ...init })`. That plain-object seam preserves `reason`, unlike the default browser constructor contract.
- For usable targets, `routeCancellation()` dispatches a `pointercancel` and does not call `cancellationCallback`. For unusable targets, it calls `cancellationCallback(descriptor)`. Thus reason transport differs by path.
- Direct `processSample()` callers can observe the returned descriptor reason, but DOM listeners cannot be told to expect `event.reason` from the default path.

## Supported claims

- The exact adapter emits or returns one terminal `pointercancel` descriptor for the bounded cancellation cases covered by its state machine.
- The internal descriptor may carry a private `reason` string.
- Standard `pointercancel` listeners can observe the standard event and its standard pointer fields.
- A host can receive deterministic reason metadata without a package by using a dedicated cancellation callback invoked on all terminal paths.
- A separate purpose-named `CustomEvent` may carry reason data in `detail` when DOM transport is explicitly required; that is a separate event contract, not an extension of `PointerEvent`.

## Excluded claims

- No claim that default-browser `PointerEvent` instances expose `event.reason`.
- No claim that the current Node assertion proves browser reason transport.
- No claim that a nonstandard property assignment after construction is portable, required, or advisable.
- No browser PASS, cross-browser portability, trusted-input, user-activation, focus, accessibility, deployment, merge, publication, or ConsumerAck claim.
- No producer return, source mutation, task mutation, account action, or live execution occurred.

## Minimum revision gate

Before a fresh verifier packet treats cancellation reason as observable host behavior, bind exactly one policy:

1. **Internal-only reason:** document that reason exists only in returned descriptors and callback payloads; DOM `pointercancel` listeners receive no reason contract.
2. **Callback reason:** invoke `cancellationCallback(descriptor)` for every terminal path, independently of whether the standard event is dispatched.
3. **Custom DOM reason:** dispatch a separate named `CustomEvent` carrying `{ reason, pointerId, coordinates }` in `detail`, while preserving the standard `pointercancel` event separately.

Add one browser-level test against the exact candidate or revision. A plain-object event factory is insufficient for this gate.

## License and terms uncertainty

This revision uses browser platform standards and internal callback/state mechanisms. It adds no third-party runtime package, credential, account, paid service, or terms acceptance. The repository's missing root license text and provenance uncertainty for public distribution remain unchanged. This is engineering evidence, not legal advice.

## Cost and operator burden

```yaml
direct_research_cost_usd: 0
operator_minutes_used: 0
operator_relay_minutes: 0
estimated_producer_revision_minutes: 5_to_15
estimated_browser_verification_minutes: 5_to_10
estimated_review_rework_avoided: 10_to_20
estimate_status: HEURISTIC_NOT_FITNESS_CREDIT
new_credentials_required: 0
new_packages_required: 0
```

## Strongest objection

The host may not need a cancellation reason at all; the standard `pointercancel` signal plus internal state reset could be sufficient. If the WorkItem explicitly narrows the contract to standard cancellation only, this issue does not block that narrower behavior. It blocks only the stronger claim that the current default DOM event transports the custom reason.

A second objection is that JavaScript code can sometimes define an ad hoc property on an event object after construction. That would be nonstandard, is not what the exact default factory does, and would still require browser portability tests and an explicit contract.

## Falsifier

Change this result to `ADMIT` for the stronger reason-transport claim only if a direct clean-browser test, bound to an exact revision and supported browser matrix, proves all of the following:

1. the declared host API receives the exact cancellation reason on every terminal path;
2. the mechanism is explicit and does not depend on undeclared `PointerEventInit` members;
3. standard `pointercancel` fields and non-cancelability remain correct;
4. one cancellation produces at most one reason notification and zero activation;
5. the Node seam and browser path have equivalent asserted behavior.

Also change to narrow `ADMIT` if the consumer explicitly drops reason transport from the contract and treats reason as internal-only metadata.

## Verifier, consumer, expiry, and honest flaw

- **Verifier:** Sigrun/P4 or another distinct, browser-capable nonproducer must challenge the exact bytes and execute the declared browser path.
- **Consumer:** S03 or the next exact `SPATIAL_FACTORY_GOLDEN_APP_001` WorkItem may consume this card as an interaction-contract revision input.
- **Expiry:** `2026-08-03T17:26:08Z`, or immediately on adapter/test blob, browser-support matrix, or cancellation-contract change.
- **Credit:** zero until a named WorkItem records exact consumption or evidence-backed rejection.

Honest flaw: this carrier inspected exact repository bytes and current primary standards but had no browser or shell execution surface. The standards establish that `reason` is not a declared `PointerEventInit` member; they do not replace direct implementation testing. Estimated minutes are unmeasured. Same-provider advisory binding weight is `0`.
