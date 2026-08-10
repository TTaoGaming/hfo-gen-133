---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_PR_CHANGED_FILENAMES_READONLY_030
event_id: X13_GITHUB_PR_CHANGED_FILENAMES_PHASE4_DECISION_ADOPT_WITH_GATES_20260810T004850Z
event_type: PHASE4_DECISION
phase: 4_of_4
phase_4_decision: ADOPT_WITH_GATES
disposition: ADOPT_WITH_GATES_BOUNDED_READONLY_ADVISORY_ONLY
campaign_status: CLOSED
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 219
candidate: GitHub.list_pr_changed_filenames
effect_ceiling: BOUNDED_READONLY_PR_FILENAME_DISCOVERY_ADVISORY_ONLY
phase_4_additional_candidate_calls: 0
source_events:
  phase_1:
    path: state/coordination/experiments/cots_connector_x13/20260809T214901Z_GITHUB_PR_CHANGED_FILENAMES_PHASE1_BASELINE.md
    blob_sha: b33efd0b06f2829cd93a993a2ee04a3638c9c670
  phase_2:
    path: state/coordination/experiments/cots_connector_x13/20260809T225004Z_GITHUB_PR_CHANGED_FILENAMES_PHASE2_REPLAY.md
    blob_sha: 0f9c5e522cebd890b46100ffa1abfdda4315aa00
  phase_3:
    path: state/coordination/experiments/cots_connector_x13/20260809T235200Z_GITHUB_PR_CHANGED_FILENAMES_PHASE3_FAILURE_PROBE.md
    blob_sha: 728b5db0d872a572090c171e7b9d0892bf2437e9
campaign_measurements:
  candidate_invocations_total: 3
  usable_candidate_results: 2
  expected_failure_probes_total: 1
  target_pr_number: 10
  phase1_filename_count: 26
  phase2_filename_count: 26
  phase1_phase2_count_match: true
  phase1_phase2_ordered_digest_match: true
  ordered_filename_digest_sha256: 503d2de2bca9c417c86d1de25d5527363d5e318f3cbf997cf7810258b9e12206
  phase1_external_call_time_ms: 486
  phase2_external_call_time_ms: 487
  phase3_failure_http_status: 404
  phase3_failure_classification: NONEXISTENT_OR_INACCESSIBLE
  phase3_permission_classification_proven: false
  connector_errors_total: 0
  retries_total: 0
  fallbacks_total: 0
  candidate_mutations_total: 0
  patch_diff_content_comment_hydration_observed: false
  raw_filename_persisted: false
  operator_minutes_removed_measured: 0
  custom_code_avoided_realized: 0
  custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
  direct_quota_evidence: NONE_FROM_CONNECTOR_RECEIPT
credentials:
  connector_managed: true
  authenticated_principal: UNKNOWN
  effective_permission: UNKNOWN
  least_privilege_proven: false
durability:
  candidate_results: EPHEMERAL_NORMALIZED_RESPONSES
  durable_receipts: PHASE1_PHASE2_PHASE3_PREFLIGHT_AND_RESULT_EVENTS_PLUS_PHASE4_DECISION_AND_CURRENT_POINTER
  git_coordination_write_conflicts_observed_total: 1
  conflict_note: PHASE3_RESULT_PERSISTENCE_HIT_ONE_UNRELATED_BRANCH_HEAD_409_THEN_SUCCEEDED_AFTER_REREAD_WITHOUT_ANOTHER_CANDIDATE_CALL
observability:
  exposed:
    - SUCCESS_FILENAME_COUNT
    - ORDERED_FILENAME_LIST_AVAILABLE_EPHEMERALLY
    - SUCCESS_EXTERNAL_CALL_TIME_MS_FOR_PHASE1_AND_PHASE2
    - STRUCTURED_404_NOT_FOUND_ON_SYNTHETIC_MISSING_PR
  not_exposed:
    - AUTHENTICATED_IDENTITY_AND_EFFECTIVE_PERMISSION
    - CALLER_CONTROLLED_PAGE_PER_PAGE_OR_MAX_FILES_BOUND
    - NATIVE_PAGE_COUNT_AND_UPSTREAM_REQUEST_COUNT
    - REQUEST_ID_AND_RATE_LIMIT_HEADERS
    - ACTUAL_QUOTA_DEBIT_OR_BILLING_RECEIPT
    - PHASE3_ERROR_LATENCY
    - PROOF_OF_MULTI_PAGE_COMPLETENESS
portability:
  github_rest_pull_files_semantics: HIGH_WITH_GITHUB_SPECIFIC_404_AUTHORIZATION_AMBIGUITY
  normalized_wrapper_shape: GITHUB_CONNECTOR_SPECIFIC
  auto_pagination_behavior: CLAIMED_BY_WRAPPER_NOT_DIRECTLY_VERIFIED_ON_MULTI_PAGE_PR
  cross_provider_parity: NOT_APPLICABLE_OR_NOT_TESTED
failure_behavior:
  observed: FAIL_CLOSED_WITH_STRUCTURED_404_NOT_FOUND_FOR_CLEARLY_SYNTHETIC_MISSING_PR
  classification: NONEXISTENT_OR_INACCESSIBLE_ONLY
  permission_or_existence_inference_from_404: FORBIDDEN
  automatic_retry_on_stable_404: FORBIDDEN_WITHOUT_CHANGED_INPUT_IDENTITY_PERMISSION_OR_NEW_EVIDENCE
direct_cost_and_quota_evidence:
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
  actual_quota_consumed: UNKNOWN
  rate_limit_headers_exposed: false
  provider_billing_or_quota_receipt: ABSENT
verifier:
  completed: PARTIAL_GIT_DURABLE_READBACK_PLUS_DIRECT_CONNECTOR_RECEIPTS_PLUS_PHASE1_PHASE2_DIGEST_COMPARISON
  strongest_missing_witness: KNOWN_MULTI_PAGE_PR_WITH_INDEPENDENT_RAW_GITHUB_REST_FILES_LIST_COUNT_AND_SAFE_DIGEST_UNDER_THE_SAME_PRINCIPAL_CLASS
consumer:
  named_consumer: HFO_PR_BLAST_RADIUS_AND_TARGETED_PATCH_SELECTION_GATES
  operational_ack: NOT_OBSERVED
  adoption_credit: 1
  fitness_credit: 0
strongest_falsifier: A_KNOWN_MULTI_PAGE_PR_IS_SILENTLY_TRUNCATED_OR_THE_WRAPPER_AUTO_PAGINATION_EXCEEDS_OPERATOR_BOUNDEDNESS_REQUIREMENTS_WITHOUT_EXPOSING_REQUEST_COUNT_OR_LIMIT_CONTROL
mandatory_gates:
  - READ_ONLY_ONLY
  - USE_ONLY_ON_KNOWN_SMALL_PRS_WHERE_FILENAME_CARDINALITY_IS_EXPECTED_TO_BE_WELL_BELOW_NATIVE_MULTI_PAGE_BOUNDARIES
  - TREAT_404_AS_NONEXISTENT_OR_INACCESSIBLE_AND_NEVER_AS_PERMISSION_OR_EXISTENCE_PROOF
  - NO_AUTOMATIC_RETRY_ON_STABLE_404_WITHOUT_CHANGED_EVIDENCE
  - DO_NOT_FETCH_PATCH_DIFF_CONTENT_OR_COMMENTS_AS_PART_OF_THIS_CAPABILITY
  - DO_NOT_PERSIST_RAW_FILENAMES_UNLESS_MINIMUM_NECESSARY_FOR_A_NAMED_CONSUMER
  - DO_NOT_CLAIM_AUTHORITATIVE_COMPLETENESS_ON_MULTI_PAGE_OR_LARGE_PRS
  - DO_NOT_CLAIM_RATE_LIMIT_QUOTA_COST_EFFECTIVE_PRINCIPAL_OR_LEAST_PRIVILEGE_PROPERTIES_WITHOUT_DIRECT_RECEIPTS
  - REQUIRE_INDEPENDENT_RAW_PROVIDER_WITNESS_BEFORE_USING_FOR_HIGH_ASSURANCE_MERGE_RELEASE_OR_SECURITY_GATES
adopted_boundary:
  allowed:
    - BOUNDED_READONLY_PR_BLAST_RADIUS_DISCOVERY_ON_KNOWN_SMALL_PRS
    - ADVISORY_TARGET_SELECTION_FOR_SUBSEQUENT_EXPLICITLY_GATED_PATCH_FETCHES
  forbidden:
    - LARGE_OR_UNBOUNDED_PR_COMPLETENESS_CLAIMS
    - MERGE_RELEASE_OR_SECURITY_GATING_WITHOUT_INDEPENDENT_VERIFICATION
    - PERMISSION_OR_EXISTENCE_INFERENCE_FROM_404
    - MUTATION_PUBLICATION_OR_IMPLICIT_PATCH_CONTENT_COMMENT_HYDRATION
    - FITNESS_CREDIT_WITHOUT_MEASURED_OPERATOR_OUTCOME
honest_flaw: THE_CAMPAIGN EXERCISED ONLY ONE KNOWN_SMALL_26_FILE_PR_TWICE_AND_ONE_SYNTHETIC_404; MULTI_PAGE_AUTO_PAGINATION_TRUNCATION_NATIVE_REQUEST_COUNT_RATE_LIMITS_HIDDEN_RETRIES_EFFECTIVE_PERMISSION_LARGE_PR_BEHAVIOR_CONSUMER_VALUE_AND_ACTUAL_OPERATOR_TIME_SAVINGS_REMAIN_UNVERIFIED
next_campaign:
  candidate: GitHub.get_pr_info_bounded_readonly_metadata_surface
  next_phase: 1_of_4
  action_this_wake: NONE
valid_time_utc: 2026-08-10T00:48:50Z
recorded_time_utc: 2026-08-10T00:48:50Z
---

# X13 GitHub PR changed-filenames phase 4 decision

Decision: `ADOPT_WITH_GATES` for bounded, read-only, advisory use on known-small pull requests. Two direct reads of PR #10 returned the same 26-filename count and identical ordered digest in 486 ms and 487 ms, while one synthetic missing-PR probe failed closed with structured `404 Not Found`. No candidate mutation, retry, fallback, patch/diff/content/comment hydration, direct quota debit, effective principal, or rate-limit telemetry was observed.

The connector avoids custom filename-list pagination and normalization code in principle, but realized code avoidance and measured operator-time savings remain zero. The unresolved boundedness flaw is material: the wrapper exposes no caller-controlled page, per-page, or maximum-file limit while multi-page auto-pagination has not been independently verified. Adopt only inside the mandatory gates above; do not use it as authoritative evidence for large-PR completeness, permissions, merge/release/security decisions, cost, or quota claims.
