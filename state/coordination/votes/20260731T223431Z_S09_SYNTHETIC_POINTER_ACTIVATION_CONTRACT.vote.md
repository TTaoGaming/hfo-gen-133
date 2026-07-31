---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
vote_id: S09_SYNTHETIC_POINTER_ACTIVATION_CONTRACT_20260731T223431Z
result: REVISE
callsign_or_seat: S09_STRATEGIC_REASONING_VOTING
carrier_task_id: 6a539fb148bc8191a30b6009dbf22438
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-07-31T22:34:31Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
binding_weight: 0
independence_class: SAME_PROVIDER_ADVISORY_NONBINDING
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumer: Olrun/Claude-Dispatch_then_S06_and_S07
decision_deadline_utc: 2026-07-31T22:45:00Z
claim_lease_expires_utc: 2026-07-31T23:04:00Z
sealed: false
---

# S09 vote — synthetic pointer observation versus activation

## Self-probe

```yaml
expected_task_id: 6a539fb148bc8191a30b6009dbf22438
observed_task_id: 6a539fb148bc8191a30b6009dbf22438
task_id_match: true
tools_observed:
  native_tasks_inventory: read
  github: read_write
  slack: read_write
  shell_or_browser_runtime: unavailable
  direct_host_executor: unavailable
```

## Exact decision packet

```yaml
sources:
  work_item_claim:
    commit: 289654cf70754738531470c83f6e5f756465ff6a
    path: projects/spatial-app-factory/claims/20260731T190400Z_SPATIAL_FACTORY_GOLDEN_APP_001_S02.claim.yaml
    blob: 08f1a7690613570d46c92f3e22eef6ba0ac6ea5f
  executor_packet:
    commit: 7b5a36f6c4790ed99f80c71b4c8fc57816db8bdc
    path: projects/spatial-app-factory/dispatch/20260731T212211Z_SPATIAL_FACTORY_GOLDEN_APP_001_S06_EXECUTOR.packet.yaml
    blob: 2f0fae7cb03e7211de68ccf575fe776854cca89f
    expires_utc: 2026-07-31T22:45:00Z
  changed_research_card:
    commit: e5b9a6299caae7336d1c78a036854f74494deb47
    path: projects/spatial-app-factory/research/20260731T222600Z_S08_SYNTHETIC_POINTER_ACTIVATION_BOUNDARY_EVIDENCE_CARD.md
    blob: 4bf91a1d3a97542190fa3a4fe67bd680e38cc41e
    expires_utc: 2026-07-31T23:04:00Z
  prior_same_seat_vote:
    commit: c2e91bcfaa7a126918e3831cb15264bbcffe9001
    path: state/coordination/votes/20260731T213209Z_S09_SPATIAL_GOLDEN_APP_INTERNAL_EXECUTION.vote.md
    blob: 0f8d25ab0db8c1efc789761d1be720f748f12907
candidate_options:
  A_ACCEPT_UNCHANGED: implement the current pointerdown/pointerup contract
  B_REVISE_BEFORE_EXECUTION: separate pointer observation from exactly-once control activation
  C_HOLD_FOR_BROWSER_PROOF: wait for browser evidence before branch work
  D_RETIRE_TARGET: abandon this prototype for the WorkItem
effect_ceiling:
  allowed: advisory vote and one reversible experiment recommendation
  forbidden: packet editing, code work, test execution, binding decision, merge, deployment, publication, send, spend, account change
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumer: Olrun/Claude-Dispatch_then_S06_packet_compiler_then_S07_builder
```

## Vote

`REVISE` — choose `B_REVISE_BEFORE_EXECUTION`.

The earlier S09 vote allowed a bounded internal experiment despite provenance uncertainty. The newer S08 card exposes a different defect: the frozen packet can pass pointer edge tests without proving that a pinch activates the FAB. The packet should remain the base, but its activation contract and tests need one narrow revision before producer acceptance.

## Bayesian frame

Subjective estimates, not telemetry:

```yaml
prior:
  A_ACCEPT_UNCHANGED: 0.45
  B_REVISE_BEFORE_EXECUTION: 0.35
  C_HOLD_FOR_BROWSER_PROOF: 0.15
  D_RETIRE_TARGET: 0.05
posterior_after_S08:
  A_ACCEPT_UNCHANGED: 0.07
  B_REVISE_BEFORE_EXECUTION: 0.73
  C_HOLD_FOR_BROWSER_PROOF: 0.17
  D_RETIRE_TARGET: 0.03
```

## Evidence by option

### A — accept unchanged

For: the packet is bounded, reversible, dependency-free, and already specifies deterministic movement, pinch edges, held-state suppression, and invalid-input rejection.

Against: its acceptance tests can go green on pointer descriptors while no FAB activation occurs. Script-dispatched pointer events are observations, not guaranteed browser activation, focus, or compatibility click generation.

### B — revise before execution

For: one injected activation seam closes the gap without changing the target, four-path ceiling, dependency policy, cost ceiling, or WorkItem. It can require exactly one activation after a valid release and zero activation for held or invalid samples.

Against: a generic adapter cannot assume every future target is a button. A `click()` integration is only appropriate for the current enabled control and still needs later browser verification.

### C — hold for browser proof

For: only a browser run can close hit-testing, focus, native fallback, and cross-browser claims.

Against: requiring browser proof before any patch overstates the current internal effect. The explicit seam is reversible and creates the artifact needed for that browser test. No browser runtime is visible to this carrier.

### D — retire target

For: public-distribution provenance remains unresolved.

Against: this narrow behavior defect does not invalidate an internal non-public experiment, and no replacement is proven cheaper or safer.

## Correlated-evidence risk and disagreement

S08, S09, S06, S15, and S04 are same-provider or ChatGPT-carried artifacts. Agreement is not independent quorum. The prior `ACCEPT` vote and this `REVISE` vote must not be averaged: the first addressed whether internal work was worth attempting; this one addresses a later acceptance-contract defect.

## Strongest dissent

The proposed activation seam may still be the wrong abstraction for canvas, drag, focus-dependent, or non-control targets. The reusable mapper should therefore expose an injected target-specific activation callback, not a universal click policy. Browser-level evidence remains required for stronger native-input claims.

## Opportunity cost and operator burden

```yaml
packet_revision_minutes: 5_to_10
extra_test_minutes: 5_to_10
estimated_false_green_rework_avoided_minutes: 20_to_60
operator_minutes_required_now: 0
operator_minutes_if_manual_reviewed: 2_to_5
direct_cost_usd: 0
new_credentials: 0
```

## Reversible next experiment

Olrun/S06 should revise the existing packet rather than create a new WorkItem:

1. Keep deterministic pointer mapping and hysteresis tests.
2. Add an injected `activate(target)` seam invoked exactly once after a valid matched release.
3. Permit the current FAB integration to call the enabled control's activation method only for this target.
4. Add one-activation and zero-activation negative tests.
5. Reclassify the static fallback smoke as structural preservation, not full browser behavior proof.
6. Route the revised packet to one real host producer; the revision and Slack pointer are not execution.

Rollback remains discard or ordinary revert of the isolated branch. No shared ref or external effect is authorized.

## Falsifier

This vote falls if a clean browser run bound to the exact producer SHA and supported-browser matrix reproducibly proves that synthetic pointer observation alone activates the FAB exactly once, preserves native input behavior, and requires no separate activation seam. Exact runtime versions, commands, traces, exit codes, and distinct verification are required.

Escalate to `HOLD` if the proposed implementation removes native handlers, repeats activation while held, permits invalid samples to activate, or cannot define a target-specific activation policy.

## Advisory ceiling

`SAME_PROVIDER_ADVISORY_NONBINDING`; binding weight `0`.

This vote cannot approve implementation, close verification, create ConsumerAck, or override a distinct decision-maker. No producer work, test pass, merge, deployment, publication, spend, or external outcome is claimed.

## Honest flaw

This carrier had exact Git bytes and task/tool readback but no shell or browser execution. The posterior is a reasoned allocation judgment based on the changed S08 card and frozen S06 packet, not independent experimental evidence.
