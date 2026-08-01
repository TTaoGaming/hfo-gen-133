---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
vote_id: S09_GOLDEN_APP_TARGET_CONTINUITY_POLICY_20260801T063500Z
result: REVISE
recommended_option: REVISE_FIXED_TARGET_CYCLE_CONTINUITY
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
correlation_id: SPATIAL_FACTORY_GOLDEN_APP_001_TARGET_CONTINUITY_FEE50A7
callsign_or_seat: S09_STRATEGIC_REASONING_AND_VOTING_CELL
carrier_task_id_expected: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_evidence: RUNTIME_INSTRUCTION_CLAIM_NOT_NATIVE_TASK_READBACK
wip: 1
valid_time_utc: 2026-08-01T06:35:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
decision_deadline_utc: 2026-08-03T17:57:17Z
decision_deadline_basis: OPERATOR_PACKET_AUTHORITY_EXPIRY_EARLIER_THAN_RESEARCH_CARD_EXPIRY
effect_ceiling: INTERNAL_ADVISORY_PACKET_REVISION_AND_REVERSIBLE_BRANCH_TEST_RECOMMENDATION_ONLY_NO_PRODUCER_WORK_NO_BINDING_DECISION
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumer:
  - next_S02_admission_for_SPATIAL_FACTORY_GOLDEN_APP_001
  - Olrun/Claude-Dispatch
  - next_S06_executor_packet_compiler
  - S03_reducer_after_real_return
same_provider_status: SAME_PROVIDER_NONBINDING
binding_weight: 0
sealed: false
---

# S09 adversarial Bayesian vote — golden-app target continuity policy

## Self-probe

```yaml
expected_task_id: 6a539fb148bc8191a30b6009dbf22438
native_task_readback_exposed: false
task_identity_conclusion: expected_ID_present_in_runtime_instruction_but_not_independently_read_back
tools_observed:
  github_connector: authenticated_read_write_contents_commit_search_and_exact_blob_readback
  slack_public_channel: authenticated_read_write
  native_task_inventory: unavailable_to_this_carrier
  shell_or_browser_runtime: unavailable
  distinct_provider_ingress: unavailable
prohibited_effects_observed: none
```

## Exact changed decision packet

```yaml
decision_question: >-
  After the exact TAGS fee50a7 adapter and tests introduced descriptor-by-descriptor target resolution,
  what target-continuity policy should the next exact S02/S06 packet bind before re-admitting the expired
  golden-app claim for one target-specific pinch activation?
decision_deadline_utc: 2026-08-03T17:57:17Z
packet_effect_ceiling:
  allowed:
    - advisory vote
    - recommendation for one new immutable claim and executor packet
    - one reversible branch-file-test experiment on the existing four-path allowlist
  forbidden:
    - task mutation
    - producer implementation by S09
    - binding policy decision
    - self-verification
    - merge
    - deployment
    - publication
    - send
    - spend
    - account or security change
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumer:
  - next_S02_admission_for_SPATIAL_FACTORY_GOLDEN_APP_001
  - Olrun/Claude-Dispatch
  - next_S06_executor_packet_compiler
  - S03_reducer_after_real_return
candidate_options:
  ACCEPT_CURRENT_DYNAMIC_RESOLUTION: >-
    requeue the expired packet and fee50a7 implementation without changing the target-continuity contract;
    permit each synthetic descriptor to resolve independently through elementFromPoint
  REVISE_FIXED_TARGET_CYCLE_CONTINUITY: >-
    for this one-FAB golden app, bind mainFab as the exact injected target at cycle start, preserve it through
    held and release transitions, invoke one explicit programmatic activation callback on valid release,
    and exclude the dynamic resolver path from the A3 target-activation PASS claim
  REVISE_GENERAL_PRESS_TARGET_CONTINUITY: >-
    implement a reusable dynamic policy that captures the press target on pinch-down and routes held plus release
    to that target with explicit cancellation and target-loss semantics
  HOLD_FOR_BROWSER_PROOF: >-
    perform no new branch work until a clean browser matrix proves the required target and activation behavior
  RETIRE_TARGET: >-
    stop using the current TAGS FAB prototype for this WorkItem
  ABSTAIN: >-
    record insufficient evidence to choose a policy
source_bindings:
  changed_S08_card:
    commit: da51463c590a337f060eea881d83ccbd84175da9
    path: projects/spatial-app-factory/research/20260801T062903Z_S08_SYNTHETIC_POINTER_TARGET_CONTINUITY_EVIDENCE_CARD.md
    blob: 4310036928da223d611ca9f4ee5eb93eddfb3d13
    result: REVISE
    expires_utc: 2026-08-08T06:29:03Z
  exact_target_head:
    repository: TTaoGaming/TAGS
    commit: fee50a70188b510695e8e5fad2ebadc6cba0535a
    adapter_path: prototypes/spatial-input-adapter.js
    adapter_blob: c90a715c72735f0c04d60c91cd9c9afb0f2ddec4
    test_path: tests/spatial-input-adapter.test.mjs
    test_blob: 9416a2e34c331ab46dd2f04c8d8664dbc0088405
  expired_renewed_claim:
    commit: 47cd1e8bfb7cf78651e8978f4dec1f5e2a76bad4
    path: projects/spatial-app-factory/claims/20260801T000607Z_SPATIAL_FACTORY_GOLDEN_APP_001_S02_RENEWED.claim.yaml
    blob: f90e3797b4e5aa398aa386e555e26b53ae27cfc5
    acceptance_contract_sha256: ffaa1a6fa0637039abd6ab9e43b1b978d1505edd0575ab020ca7256e3a45a8cb
    lease_expired_utc: 2026-08-01T04:06:07Z
  expired_revised_executor_packet:
    commit: 44bcfd69ecf90afd95b52c7917e65376ba49163f
    path: projects/spatial-app-factory/dispatch/20260801T001933Z_SPATIAL_FACTORY_GOLDEN_APP_001_S06_REVISED_EXECUTOR.packet.yaml
    blob: 94b2da15f48657dcfa41bb0020693f44b756ca4e
    packet_expired_utc: 2026-08-01T03:00:00Z
  operator_authority:
    commit: b9d0f66cb64feeccef8472b1830fbcb5e1796551
    path: projects/spatial-app-factory/packets/20260731T175717Z_REGINLEIF_SCHEDULED_LOOPS_PDCA_OPERATOR_DIRECTIVE.packet.md
    blob: 04e3fc472c65f58fb2e189f546371eb9a2899330
    authority_expires_utc: 2026-08-03T17:57:17Z
  prior_S09_activation_vote:
    commit: 76c88d7e7595c0f879120ea7d330152d8d570c23
    path: state/coordination/votes/20260731T223431Z_S09_SYNTHETIC_POINTER_ACTIVATION_CONTRACT.vote.md
    blob: d8bac6c114da5d32a6ccf7641dc95ce37dd0ef64
    result: REVISE
```

The changed S08 card is newer than the prior S09 vote. The expired S06 packet already requires activation against the same resolved target bound to a cycle, but its phrase “exact target or target resolver” leaves the dynamic resolver path insufficiently constrained. The current fee50a7 code resolves every descriptor separately unless `config.target` is supplied, and the current Node test uses one constant target without an A-at-down/B-at-up negative control. No newer exact producer digest, browser run, distinct verdict, or ConsumerAck was found on the connected Git branch or public control channel. Absence on those surfaces does not prove absence elsewhere.

## Vote

`REVISE` — select `REVISE_FIXED_TARGET_CYCLE_CONTINUITY` for this bounded golden app.

The next S02/S06 packet should not renew the expired claim unchanged. It should explicitly bind the existing native `mainFab` control as the fixed target for the accepted golden-app path, retain that target as cycle state from valid pinch-down through release, and require exactly one injected programmatic activation after a matched valid release. The default `elementFromPoint()` resolver may remain as nonaccepted exploratory behavior, but it must not satisfy A3, native-capture, trusted-input, or general target-continuity claims.

This is an app-specific choice, not an architecture decision for every spatial control. A general press-target policy can be evaluated later when a multi-target WorkItem exists.

## Bayesian assessment

Weights are advisory action allocations, not calibrated probabilities.

```yaml
prior_action_weights:
  ACCEPT_CURRENT_DYNAMIC_RESOLUTION: 0.12
  REVISE_FIXED_TARGET_CYCLE_CONTINUITY: 0.38
  REVISE_GENERAL_PRESS_TARGET_CONTINUITY: 0.24
  HOLD_FOR_BROWSER_PROOF: 0.16
  RETIRE_TARGET: 0.05
  ABSTAIN: 0.05
posterior_action_weights:
  ACCEPT_CURRENT_DYNAMIC_RESOLUTION: 0.03
  REVISE_FIXED_TARGET_CYCLE_CONTINUITY: 0.62
  REVISE_GENERAL_PRESS_TARGET_CONTINUITY: 0.18
  HOLD_FOR_BROWSER_PROOF: 0.11
  RETIRE_TARGET: 0.03
  ABSTAIN: 0.03
```

### ACCEPT_CURRENT_DYNAMIC_RESOLUTION

Evidence for:

- `dispatchSample()` exists and the deterministic descriptor tests cover mapping, one down edge, one up edge, and invalid samples.
- The branch is already bounded to four files and no dependency is required.
- A narrow consumer that never crosses targets may appear to work.

Evidence against:

- The exact code independently calls `resolveTarget()` for each descriptor and uses `document.elementFromPoint()` when no fixed target is injected.
- No press target, capture state, cancellation policy, or target-loss policy is retained.
- The current test uses one constant injected target and therefore cannot falsify cross-target splitting.
- Synthetic `dispatchEvent()` does not establish a native active pointer, implicit capture, trusted input, or click.
- Reusing expired claim and packet bytes without changed acceptance would launder stale authority and stale test coverage.

Conclusion: strongest false-green path; reject.

### REVISE_FIXED_TARGET_CYCLE_CONTINUITY

Evidence for:

- The golden app has one named native control, `mainFab`; a fixed target matches the WorkItem rather than inventing a general framework.
- The current adapter already supports `config.target`, so this option uses an existing seam and should require the least code.
- The expired acceptance contract already requires target-specific injected activation, native fallback preservation, no dependency, and exact branch/test evidence.
- Retaining the target as explicit cycle state makes reset, disarm, target loss, repeated release, and exactly-once activation testable without claiming browser capture.
- An A-at-down/B-at-up test can prove that B receives zero activation even when release coordinates hit B.
- The change is reversible on an unmerged branch and keeps the effect ceiling narrow.

Evidence against:

- It does not solve general multi-target, drag, canvas, hover, or release-inside semantics.
- Fixed-target tests can hide defects in the default dynamic resolver if downstream summaries describe the whole adapter as verified.
- Programmatic `target.click()` remains weaker than trusted user activation and still needs browser/accessibility testing before stronger claims.
- A new claim and packet are required because the prior lease and executor packet expired.

Conclusion: best fit for one bounded golden-app proof, provided the accepted scope explicitly excludes the dynamic resolver.

### REVISE_GENERAL_PRESS_TARGET_CONTINUITY

Evidence for:

- Capturing the press target on pinch-down is reusable for multiple controls and directly addresses cross-target splitting.
- It can define held routing, release ownership, target removal, cancellation, and reset semantics in one adapter policy.
- It reduces the chance that future consumers accidentally use the unsafe per-descriptor resolver.

Evidence against:

- It adds state and policy surface before a multi-target WorkItem exists.
- Release-inside, cancel-on-leave, drag, hover, and activation ownership are product choices, not purely technical defaults.
- More branches and edge cases increase producer and verifier burden and make the first golden-app loop slower.
- The user’s current objective is a verified outcome and operator relief, not a generalized input framework.

Conclusion: valid next campaign, but over-scoped for this WorkItem.

### HOLD_FOR_BROWSER_PROOF

Evidence for:

- Only browser execution can close claims about DOM hit testing, focus, native fallback, accessibility, and cross-browser behavior.
- Same-provider Git/Slack artifacts share prompt and connector blind spots.
- A fixed-target Node test alone cannot establish user activation or real pointer semantics.

Evidence against:

- The branch experiment is reversible and explicitly forbidden from claiming trusted input or browser completion.
- A stricter deterministic contract is the artifact needed before browser verification is useful.
- No browser runtime or distinct verifier is exposed to this carrier, so HOLD would delay a cheap internal patch without resolving the gap.

Conclusion: strongest dissent if downstream consumers cannot preserve the static-versus-browser evidence boundary.

### RETIRE_TARGET

Evidence for:

- Provenance and public-distribution uncertainty remain unresolved.
- Repeated expiry and ingress failures show workflow friction beyond this one code defect.

Evidence against:

- The target already has bounded code and tests, and the continuity defect has a small reversible correction.
- Retirement would discard a nearly complete internal proof without a verified cheaper replacement.
- This vote does not authorize public distribution.

Conclusion: premature.

### ABSTAIN

Evidence for:

- No direct browser run, final producer digest, distinct verdict, or explicit consumer acknowledgement exists.
- The renewed claim and executor packet are expired.

Evidence against:

- The decision is only whether to issue a narrower internal packet, not whether the app is complete.
- Exact immutable code, tests, card, claim, packet, and authority bytes are available for a weight-zero advisory choice.

Conclusion: unnecessary under the narrow ceiling.

## Correlated-evidence risk

S02, S06, S08, prior S09, Slack routing, and this vote are ChatGPT-carried and mostly share the same GitHub/Slack connector family. The exact code and blob readbacks improve traceability but do not create provider independence. The S08 and S09 agreement must not be counted as a majority or a quorum. `SAME_PROVIDER_NONBINDING`; binding weight `0`.

## Disagreement without majority laundering

- The expired S06 packet says the activation callback must use the same resolved target bound to the cycle, which supports continuity in principle.
- The fee50a7 implementation does not yet implement that cycle-bound target or activation seam; it resolves descriptors independently unless a fixed target is injected.
- The changed S08 card says the next packet must choose fixed-target, press-target continuity, release-inside, or cancel-on-leave rather than rely on implicit capture.
- The prior S09 vote favored an injected target-specific activation seam but predated the exact descriptor-by-descriptor target-resolution evidence.

These artifacts do not vote independently. The material disagreement is whether the existing packet is already precise enough and whether the first implementation should be app-specific or general.

## Strongest dissent

`HOLD_FOR_BROWSER_PROOF` is the strongest dissent. A fixed target plus Node tests may create another attractive green artifact while leaving real DOM focus, pointer event ordering, native fallback, and accessibility untested. That dissent wins if any consumer intends to call the result a browser-ready, native-input, accessibility, or production PASS; if no distinct verifier can inspect the final code; or if the accepted scope cannot exclude the default dynamic resolver.

A secondary dissent favors `REVISE_GENERAL_PRESS_TARGET_CONTINUITY`: fixing only the FAB path leaves an unsafe default API that future consumers may misuse. That dissent wins when a named multi-target consumer appears or when the adapter is promoted as a reusable general input layer.

## Opportunity cost and operator-minute burden

```yaml
ACCEPT_CURRENT_DYNAMIC_RESOLUTION:
  immediate_producer_minutes: 0_to_5
  likely_false_green_rework_minutes: 20_to_60
  operator_minutes: 0_to_5
REVISE_FIXED_TARGET_CYCLE_CONTINUITY:
  packet_revision_minutes: 5_to_10
  producer_patch_and_tests_minutes: 10_to_25
  distinct_review_minutes: 5_to_15
  operator_relay_minutes_expected: 0
  direct_cost_usd_observed: 0
REVISE_GENERAL_PRESS_TARGET_CONTINUITY:
  packet_revision_minutes: 10_to_20
  producer_patch_and_edge_tests_minutes: 25_to_50
  distinct_review_minutes: 10_to_25
  opportunity_cost: delays_first_closed_golden_app_loop
HOLD_FOR_BROWSER_PROOF:
  immediate_minutes: 0_to_3
  browser_ingress_or_operator_relay_minutes_unvalidated: 10_to_30
  delay_cost: no_new_verified_branch_artifact
RETIRE_TARGET:
  closeout_minutes: 2_to_5
  lost_asset: existing_bounded_branch_and_tests
ABSTAIN:
  minutes: 0
  consequence: same_ambiguity_recurs_on_next_requeue
```

This vote itself removes no measured operator minutes. The recommended path is designed for zero operator relay if S02, S06, the producer, verifier, and reducer consume Git directly.

## Smallest reversible next experiment

The next authorized S02/S06 carriers should issue one new exact claim and executor packet, not edit or silently renew the expired artifacts. Minimum experiment:

1. Bind target repository `TTaoGaming/TAGS`, starting head `fee50a70188b510695e8e5fad2ebadc6cba0535a`, adapter blob `c90a715c...`, and test blob `9416a2e3...`.
2. Keep the existing four-path allowlist, no-dependency rule, native `mainFab` control, and programmatic-activation evidence ceiling.
3. Declare the accepted golden-app policy as `fixed_target_cycle_continuity`:
   - resolve or inject `mainFab` once for a new valid armed pinch cycle;
   - retain that exact target through held and release transitions;
   - clear target and held state on reset, disarm, invalid cycle termination, or target loss;
   - invoke the injected activation callback exactly once after one matched valid release;
   - never imply browser pointer capture, trusted input, focus, or accessibility PASS.
4. Add an exact two-target test: target A is bound at down; release coordinates or a fake `elementFromPoint()` resolve B; only A may receive held/release effects and exactly one activation; B receives zero activation.
5. Add target-removal, reset, disarm, invalid, held, and repeated-release negatives with zero extra activation.
6. Run the frozen Node tests, diff check, allowed-path check, static-server readbacks, and exact final-SHA readback with real exit codes.
7. Route the exact producer return to a distinct nonproducer for `STOOD | FELL`; S04 same-provider preflight remains weight `0`.
8. Require explicit Olrun ConsumerAck only after distinct `STOOD`; no Slack pointer or repository presence is acknowledgement.

Rollback is an unmerged branch discard or ordinary forward revert. No merge, deployment, publication, send, spend, or account effect is authorized.

## Falsifiers

Revise this recommendation to `REVISE_GENERAL_PRESS_TARGET_CONTINUITY`, `HOLD`, or `RETIRE` if any of the following occurs:

- a named current consumer requires multiple independently hit-tested controls, drag, canvas, release-inside, or cancel-on-leave semantics;
- the fixed-target path cannot preserve the existing native `mainFab` mouse, touch, keyboard, `onclick`, and ordinary click fallback;
- the two-target test shows target B receiving release or activation, target A receiving duplicate activation, or stale target state surviving reset/disarm;
- implementation changes paths outside the four-file allowlist or adds a dependency, workflow, credential, deployment, or account effect;
- the producer cannot start from exact head `fee50a7` or cannot return exact commands, exit codes, blobs, and final SHA;
- a clean browser test bound to the exact final SHA proves that the current dynamic path safely provides the declared continuity and exactly-once activation across the supported matrix without hidden native pointer state;
- the next packet describes the fixed-target Node result as general adapter, native-pointer, browser, accessibility, production, or independent-verification PASS;
- no distinct verifier or named consumer is available before the operator authority expires;
- the operator authority or target head changes before a new exact claim is admitted.

## Honest flaw

This vote inspected exact Git files and public Slack telemetry but did not execute a shell, browser, build, or test and did not inspect private coordination. The recommended fixed-target policy is a scope judgment: it minimizes the first golden-app patch but may be too narrow for later multi-target spatial applications. Time estimates are heuristic and earn no fitness until a real producer return and consumer acknowledgement exist. The source artifacts and this vote are same-provider advisory evidence; binding weight remains `0`.
