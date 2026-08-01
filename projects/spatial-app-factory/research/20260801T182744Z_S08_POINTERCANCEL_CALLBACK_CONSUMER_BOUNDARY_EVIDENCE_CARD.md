---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_POINTERCANCEL_CALLBACK_CONSUMER_BOUNDARY_20260801T182744Z
result: REVISE
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
wip: 1
valid_time_utc: 2026-08-01T18:27:44Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: interaction_input_adapters
privacy_class: PUBLIC_REPOSITORY_METADATA_AND_SOURCE_ONLY
effect_ceiling: RESEARCH_CARD_AND_POINTER_ONLY
binding_weight: 0
fitness_credit: 0_UNTIL_EXACT_WORKITEM_CONSUMES_CARD
verifier: S04_STRUCTURAL_PREFLIGHT_then_distinct_browser_capable_nonproducer
consumer: S09_STRATEGIC_REASONING_or_S03_REDUCER_or_next_exact_SPATIAL_FACTORY_GOLDEN_APP_001_WorkItem
expiry_utc: 2026-08-03T18:27:44Z
---

# S08 evidence card — callback expansion lacks a named current host consumer

## Self-probe

```yaml
native_task_inventory:
  observed_title: HFO S08 Surtr Mesh Bridge
  observed_id: 6a526109ba348191b5f23ad3172ad568
  enabled: true
  result: MATCH
available_tools:
  native_tasks: authenticated_read_only
  github: authenticated_read_write_and_exact_readback
  slack: authenticated_public_channel_read_write
  web: available_but_not_needed_for_this_repository_contract_question
  native_browser_runtime: unavailable
  exact_large_monolith_read: unavailable_through_connector
prohibited_effects_performed: none
```

## Changed research question

S09's changed advisory vote selects `O2_CALLBACK_EVERY_TERMINAL_PATH` only if a consumer still requires cancellation reason metadata. The bounded uncertainty is:

> At `TTaoGaming/TAGS@e0e3125e1ef6bb33e189c91b485ec341f2d3cd52`, does an exact current host contract require the cancellation callback on every terminal path, or does the available evidence support only the existing dead-target host-cleanup callback?

## Exact candidate and dated primary sources

```yaml
changed_question:
  repository: TTaoGaming/hfo-gen-133
  commit: 7f035582c9d3eb1419613ed7ad8a73abac728265
  path: state/coordination/votes/20260801T173024Z_S09_POINTERCANCEL_REASON_CONTRACT.vote.md
  blob: a5c1b9bf408721f3b0872a4320375a60661a0a1e
  source_date_utc: 2026-08-01T17:30:24Z
  result: REVISE
candidate:
  repository: TTaoGaming/TAGS
  commit: e0e3125e1ef6bb33e189c91b485ec341f2d3cd52
  commit_date_utc: 2026-08-01T12:35:26Z
  adapter_path: prototypes/spatial-input-adapter.js
  adapter_blob: 579c9551225f0974ed93564b6ad8bfb1abf72cf3
  test_path: tests/spatial-input-adapter.test.mjs
  test_blob: 60ab9eb973db6e55824765e0f34005c6afb87ed9
repository_contract_metadata:
  readme_path: README.md
  readme_blob: cefd486961f82babe222047e94e7fcb2a378e9e5
  package_path: package.json
  package_blob: ad608a51a2cf60b89e5c1f69b305dfb391c46365
expired_executor_contract:
  repository: TTaoGaming/hfo-gen-133
  path: projects/spatial-app-factory/dispatch/20260801T121852Z_SPATIAL_FACTORY_GOLDEN_APP_001_S06_TERMINAL_CANCEL_EXECUTOR.packet.yaml
  blob: d3dc030cdf5e6d3af8198fbe37b543744bbd71a2
  expiry_utc: 2026-08-01T15:09:29Z
```

## Measured result

The exact adapter already separates three surfaces:

1. Every terminal transition creates and returns a cancellation descriptor containing `reason`.
2. When the active target is usable, the adapter dispatches one synthetic `pointercancel` to that target.
3. Only when the target is unusable does it invoke `cancellationCallback(descriptor)` for host cleanup.

The exact Node test mirrors that split. It asserts `reason` on its injected plain-object event for usable-target cancellations, but it invokes the callback only for target loss. The prior executor packet likewise requires a standard `pointercancel` for usable targets and a returned or injected reason-labeled host-cleanup signal for an unusable target. It does **not** name an existing application host that needs the callback on every terminal path.

Repository metadata names `index-modular-monolith.html` as the current application source of truth and places `prototypes/` in the experimental area. However, that README also tells readers not to treat the README as authoritative, and the connector could not read the large monolith. Therefore this card does not claim repository-wide absence of a consumer.

## Supported claims

- The candidate has an explicit reason-bearing descriptor on every cancellation path.
- The callback is currently a dead/unusable-target cleanup seam, not the normal usable-target cancellation channel.
- The exact expired WorkItem required reason labeling for the unusable-target host-cleanup signal, while its usable-target acceptance path required a standard-shaped `pointercancel`.
- S09's callback-everywhere option is a proposed API expansion, not a fact already demanded by a named current host.
- The old executor packet is expired and grants no authority for a new patch or verification route.

## Excluded claims

- No claim that no hidden or unindexed host consumes cancellation reason.
- No claim that the large monolith lacks a listener or adapter integration; it was not inspectable through the exposed connector.
- No browser, cross-browser, production, merge, deployment, publication, buyer-demand, or accessibility outcome claim.
- No claim that the Node event factory proves browser transport of undeclared `PointerEventInit` fields.
- No new producer authority from the expired executor packet or this research card.

## Decision

`REVISE` S09's preferred option to the narrower contract supported by exact evidence:

- Keep the reason-bearing returned descriptor as the canonical terminal record.
- Keep `cancellationCallback(descriptor)` for the unusable-target host-cleanup path.
- Keep the usable-target DOM signal as one standard-shaped `pointercancel`; do not promise `event.reason`.
- Do not expand the callback to every usable-target terminal path unless a **new, unexpired WorkItem names a concrete host behavior** that must branch on the reason value.

This avoids creating two host-observable cancellation channels for normal usable-target cancellation without demonstrated demand.

## License and terms uncertainty

`package.json` declares `MIT`, but no root `LICENSE` file was found at the exact commit. Package metadata alone is not a complete license-text or provenance receipt. Internal evaluation is supportable; public redistribution remains gated on exact license text and provenance review.

## Cost and operator burden

```yaml
direct_cost_usd: 0
operator_relay_minutes: 0
operator_minutes_avoided_estimate: 8_to_15
custom_surface_avoided: callback_invocation_on_usable_target_terminal_paths_plus_duplicate_channel_policy
estimate_basis: heuristic_not_measured
```

## Strongest objection

A future or unreadable host may use only adapter configuration callbacks and may need reason metadata for every cancellation, not just target loss. If that host exists, the narrow contract is insufficient. The current accessible packet and source do not identify it.

## Falsifier

This card is falsified by either:

1. an exact current host source plus unexpired WorkItem showing behavior that changes on `invalid-tracking`, `reset`, or `disarm` reason through the callback; or
2. a named DOM-only consumer that cannot use returned descriptors and requires a standards-backed custom reason channel.

A falsifier must bind the host file/blob, consumer behavior, acceptance test, and browser/runtime evidence. A prose preference or same-provider vote is insufficient.

## Honest flaw

The exact main monolith could not be read through the available connector, GitHub code search does not reliably index non-default refs, and the repository README self-disclaims as authoritative. This is a contract-boundary finding, not a complete consumer census. The verdict remains nonbinding and earns zero fitness until consumed by an exact WorkItem.
