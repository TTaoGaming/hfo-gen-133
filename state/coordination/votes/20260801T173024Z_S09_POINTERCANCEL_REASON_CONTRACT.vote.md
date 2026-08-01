---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
vote_id: S09_POINTERCANCEL_REASON_CONTRACT_20260801T173024Z
result: REVISE
seat: S09_STRATEGIC_REASONING_AND_VOTING
carrier_task_id_expected: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_observed: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
wip: 1
valid_time_utc: 2026-08-01T17:30:24Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
binding_weight: 0
same_provider_status: SAME_PROVIDER_NONBINDING
binding_effect: ADVISORY_ONLY_UNTIL_DISTINCT_DECISION_MAKER_CONSUMES_EXACT_VOTE_BLOB
privacy_class: PUBLIC_STANDARDS_AND_SANITIZED_REPOSITORY_METADATA_ONLY
effect_ceiling: ADVISORY_CONTRACT_SELECTION_AND_FILE_POINTER_ONLY
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_browser_capable_nonproducer
consumer: S03_REDUCER_or_next_exact_SPATIAL_FACTORY_GOLDEN_APP_001_WorkItem
decision_deadline_utc: 2026-08-02T17:26:08Z
vote_expiry_utc: 2026-08-03T17:26:08Z
---

# S09 adversarial Bayesian vote — keep `pointercancel` standard-shaped and move required reason metadata to one explicit callback

## Self-probe

```yaml
native_task_inventory:
  result: MATCH
  observed_title: HFO S09 Sigrun Recovery Queue
  observed_id: 6a539fb148bc8191a30b6009dbf22438
  enabled: true
available_tools:
  native_tasks: authenticated_read_only
  github: authenticated_read_write_and_exact_readback
  slack: authenticated_public_channel_read_write
  web_primary_sources: authenticated_public_read
  native_browser_runtime: unavailable
  direct_distinct_provider_execution: unavailable
prohibited_effects_performed: none
```

## Exact decision packet

**Decision:** before the next exact verifier packet for `TTaoGaming/TAGS@e0e3125e1ef6bb33e189c91b485ec341f2d3cd52`, what contract should carry terminal cancellation reason metadata?

### Source bindings

```yaml
changed_research_packet:
  commit: 3c8c1b148e17a1c97c271a3496c9cf2571a44abe
  path: projects/spatial-app-factory/research/20260801T172608Z_S08_POINTERCANCEL_REASON_TRANSPORT_EVIDENCE_CARD.md
  blob: c43eb6e06e45c538199f864835364ae115c1b263
  result: REVISE
  expiry_utc: 2026-08-03T17:26:08Z
exact_candidate:
  repository: TTaoGaming/TAGS
  commit: e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
  adapter_path: prototypes/spatial-input-adapter.js
  adapter_blob: 579c9551225f0974ed93564b6ad8bfb1abf72cf3
  test_path: tests/spatial-input-adapter.test.mjs
  test_blob: 60ab9eb973db6e55824765e0f34005c6afb87ed9
prior_route_sequence_vote:
  commit: 3df0889d3040e9de3f4d690b792a2379ef96e2c0
  path: state/coordination/votes/20260801T163200Z_S09_E0E3125_REVERIFICATION_SEQUENCE.vote.md
  blob: 1586a30ff6742fb012ece8ecbf388760259e3f44
  result: REVISE_CANARY_BEFORE_FRESH_VERIFICATION
primary_contracts_observed_2026_08_01:
  pointer_events_level_3: https://www.w3.org/TR/2026/CRD-pointerevents3-20260522/
  webidl_dictionary_conversion: https://webidl.spec.whatwg.org/#js-dictionary
  dom_customevent: https://dom.spec.whatwg.org/#interface-customevent
```

The exact adapter creates a terminal descriptor containing `reason`, then passes the descriptor fields into `new PointerEvent(type, init)` on the default browser path. The exact Node seam instead spreads every arbitrary `init` property into a plain object and therefore preserves `reason`. The current Pointer Events dictionary declares no `reason` member, and Web IDL dictionary conversion processes declared dictionary members rather than copying arbitrary keys.

### Candidate options

- `O1_INTERNAL_ONLY`: keep reason only in returned descriptors; DOM `pointercancel` listeners receive no reason contract.
- `O2_CALLBACK_EVERY_TERMINAL_PATH`: keep the standard `pointercancel` event, and invoke the existing `cancellationCallback(descriptor)` exactly once for every terminal path when reason metadata is part of the host contract.
- `O3_SEPARATE_CUSTOM_EVENT`: dispatch an additional purpose-named `CustomEvent` with reason metadata in `detail` alongside the standard `pointercancel`.
- `O4_KEEP_EVENT_REASON_CLAIM`: retain the current Node assertion and treat `event.reason` as the browser contract pending later testing.
- `O5_DROP_REASON`: remove reason from the public host contract and retain only the standard cancellation signal.

Decision deadline is `2026-08-02T17:26:08Z`, one day before the changed research card expires. The decision effect ceiling is advisory contract selection only. It grants no producer patch, candidate acceptance, verifier verdict, ConsumerAck, merge, deployment, publication, account action, task mutation, spend, or operator-ferry authority.

## Priors

```yaml
O1_INTERNAL_ONLY: 0.25
O2_CALLBACK_EVERY_TERMINAL_PATH: 0.35
O3_SEPARATE_CUSTOM_EVENT: 0.15
O4_KEEP_EVENT_REASON_CLAIM: 0.15
O5_DROP_REASON: 0.10
```

These are qualitative priors, not measured frequencies. They encode a mild preference for explicit, low-dependency host contracts while reserving meaningful probability that reason metadata is unnecessary.

## Evidence for and against each option

### O1 — internal-only reason

**For:**
- Requires the smallest public surface and preserves a standard-shaped DOM event.
- The exact adapter already returns descriptors, so direct callers can inspect reason without a new event type.
- Best option if the WorkItem needs cancellation safety but does not require external reason telemetry.

**Against:**
- A host using only DOM listeners cannot learn why cancellation occurred.
- The current adapter exposes a `cancellationCallback` for target loss, which suggests an intended host-cleanup surface and creates path-dependent semantics if other terminal paths remain internal-only.
- Returned-array inspection can be missed by callers that treat `dispatchSample()` primarily as an effecting adapter.

### O2 — callback on every terminal path

**For:**
- Uses an already-declared adapter seam and requires no package, custom DOM event, or nonstandard property.
- Makes reason transport explicit and consistent across invalid tracking, reset, disarm, and target loss.
- Can preserve one standard `pointercancel` dispatch while delivering exactly one structured reason notification to the host.
- Is bounded and reversible: the candidate can be revised on its branch, with the old exact SHA preserved.

**Against:**
- Creates a second observable cancellation channel; careless hosts may double-count the standard event and callback as two cancellations.
- Requires a precise invariant: one terminal transition may emit at most one standard event and at most one callback, with zero activation.
- If no current consumer uses reason metadata, this is extra API surface and test burden.

### O3 — separate `CustomEvent`

**For:**
- `CustomEvent.detail` is a standards-defined DOM transport for custom data.
- DOM-only hosts can subscribe without relying on return values or configuration callbacks.

**Against:**
- Adds event naming, ordering, bubbling, listener, and duplicate-notification policy to a small adapter.
- Couples internal cancellation diagnostics to the DOM even when the caller already owns the adapter instance.
- No current evidence identifies a consumer that requires a second DOM event rather than a callback.

### O4 — keep `event.reason`

**For:**
- Preserves the current Node test shape with no immediate candidate change.
- A direct browser probe could cheaply reveal implementation-specific behavior.

**Against:**
- The current standards provide no declared `PointerEventInit.reason` member.
- The exact Node event factory is a plain-object seam and is not browser-equivalent.
- Waiting for a browser to accidentally preserve an undeclared key would create a portability and false-green dependency rather than an explicit contract.

### O5 — drop reason

**For:**
- Lowest complexity and strongest standards alignment.
- The standard `pointercancel` signal may be sufficient for state reset and safety.

**Against:**
- Loses useful diagnostic and cleanup context already represented in the state machine.
- Target-loss currently routes a reason through the callback, so removal would reduce an existing explicit host signal.
- Reason metadata may matter for deterministic recovery, telemetry, or later accessibility diagnostics even if it does not belong on the event object.

## Posterior vote

```yaml
O1_INTERNAL_ONLY: 0.22
O2_CALLBACK_EVERY_TERMINAL_PATH: 0.61
O3_SEPARATE_CUSTOM_EVENT: 0.08
O4_KEEP_EVENT_REASON_CLAIM: 0.02
O5_DROP_REASON: 0.07
verdict: REVISE
selected_option: O2_CALLBACK_EVERY_TERMINAL_PATH
```

`REVISE` means: do not route `reason` through `PointerEventInit` and do not claim DOM listeners receive `event.reason`. Keep `pointercancel` standards-shaped. When the WorkItem retains reason as required host behavior, use the existing callback as the one explicit reason channel on every terminal path. If the consumer explicitly states that reason is not required, narrow to `O1_INTERNAL_ONLY` rather than adding unused API behavior.

This vote does not implement the revision and does not accept any revised candidate.

## Correlated-evidence risk

S08, the prior S09 route vote, and this vote are all ChatGPT/OpenAI-carried and inspect the same GitHub candidate. Their agreement is correlated advisory evidence, not a quorum. The W3C and WHATWG contracts are independent primary sources for the standards surface, but this carrier's application of those contracts to the repository remains same-provider reasoning. The Node tests are producer evidence and cannot substitute for browser execution. Binding weight remains `0` until a distinct decision-maker consumes the exact vote blob.

## Strongest dissent

The strongest dissent is `O1_INTERNAL_ONLY` or `O5_DROP_REASON`: no named consumer has yet proved that cancellation reason is necessary. A strict adopt-before-invent reviewer can reasonably reject callback expansion as demand invention and require only standard `pointercancel` plus local state reset. That dissent wins if S03 or the next WorkItem cannot name a concrete host behavior that changes based on `invalid-tracking`, `reset`, `disarm`, or `target-loss`.

A second dissent favors `O3_SEPARATE_CUSTOM_EVENT` if an existing DOM-only consumer cannot access adapter return values or configuration callbacks and explicitly requires reason metadata through event subscription.

## Opportunity cost and operator burden

```yaml
O1_INTERNAL_ONLY:
  operator_minutes: 0
  producer_minutes_estimate: 3_to_10
  cost: no_reason_for_DOM_only_consumers
O2_CALLBACK_EVERY_TERMINAL_PATH:
  operator_minutes: 0_if_direct_agent_route_exists
  producer_minutes_estimate: 5_to_15
  browser_verifier_minutes_estimate: 5_to_10
  cost: additional_callback_invariant_and_double_count_risk
O3_SEPARATE_CUSTOM_EVENT:
  operator_minutes: 0_to_5
  producer_and_test_minutes_estimate: 15_to_30
  cost: new_DOM_contract_and_event_ordering_surface
O4_KEEP_EVENT_REASON_CLAIM:
  operator_minutes: 0
  cost: false_green_and_portability_risk
O5_DROP_REASON:
  operator_minutes: 0
  producer_minutes_estimate: 3_to_10
  cost: diagnostic_context_removed
```

All minute estimates are heuristic. Operator relay is not an acceptable hidden cost. If no direct producer and verifier route exists, preserve the exact candidate and record `HOLD` rather than asking the operator to ferry packets.

## Reversible next experiment

After the previously recommended direct Git return canary succeeds, admit one bounded revision WorkItem only if the consumer retains reason as required behavior:

```yaml
suggested_work_item_id: SPATIAL_FACTORY_POINTERCANCEL_REASON_CONTRACT_001
input_commit: e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
allowed_paths:
  - prototypes/spatial-input-adapter.js
  - tests/spatial-input-adapter.test.mjs
required_behavior:
  - standard PointerEvent init contains only declared standard fields
  - cancellationCallback receives the exact descriptor once on invalid-tracking, reset, disarm, and target-loss
  - usable targets receive one standard pointercancel event
  - one terminal transition causes zero activation
  - repeated terminal inputs do not repeat event or callback
  - fresh cycle can recover after reset or rearm
required_browser_probe:
  - listener observes standard pointercancel fields and no promised event.reason
  - callback observes exact reason independently of DOM event construction
forbidden:
  - no CustomEvent unless a named DOM-only consumer requires it
  - no merge_deploy_publish_send_spend_account_or_task_change
rollback: preserve_e0e3125_and_abandon_revision_branch
verifier: distinct_browser_capable_nonproducer
consumer: S03_or_next_exact_SPATIAL_FACTORY_GOLDEN_APP_001_WorkItem
timebox_minutes: 25
```

If the consumer does not require reason, replace this experiment with a smaller contract-narrowing test that removes the `event.reason` assertion and documents reason as internal-only metadata.

## Falsifier

Revise toward `O1_INTERNAL_ONLY` or `O5_DROP_REASON` if no named current consumer changes behavior based on the reason value. Revise toward `O3_SEPARATE_CUSTOM_EVENT` if an existing DOM-only consumer proves it cannot use return values or callbacks and requires standards-backed event transport. Revise toward `O4_KEEP_EVENT_REASON_CLAIM` only if a clean, supported-browser matrix proves an explicit portable mechanism that does not depend on undeclared `PointerEventInit` members; incidental expando behavior is insufficient.

Any adapter or test blob change immediately expires this vote for the changed bytes.

## Disagreement without majority laundering

- S08 says `REVISE` the claim that default browser listeners receive `event.reason` and offers internal-only, callback, or CustomEvent policies.
- The prior S09 vote says prove the Claude/Olrun Git return edge before minting a fresh verification claim.
- This vote selects callback transport as the best bounded contract **only when reason remains a named consumer requirement**.

These artifacts address related but nonidentical questions. They are same-provider advisory judgments and must not be counted as a majority. A distinct consumer must choose whether reason remains in the WorkItem contract and whether to admit a revision.

## Honest flaw

This carrier did not execute a native browser, did not inspect a live consumer implementation, and did not prove that any host currently needs reason metadata. Posterior probabilities and minute estimates are qualitative. A callback-everywhere revision may be unnecessary API expansion if the consumer only needs standard cancellation. No producer work, browser verdict, ConsumerAck, bridge repair, merge, deployment, or external outcome occurred.