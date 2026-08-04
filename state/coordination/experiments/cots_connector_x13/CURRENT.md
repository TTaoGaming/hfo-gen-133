---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
version: 82
prior_version: 81
candidate: GitHub_compare_commits_bounded_readonly_diff_metadata_surface
campaign_wake: 2_of_4
campaign_status: OPEN
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
adoption_mode: NOT_ADOPTED
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event:
  commit: 761929b130ccfd3dfa892848a70fa7181efad990
  path: state/coordination/experiments/cots_connector_x13/20260804T064800Z_GITHUB_COMPARE_COMMITS_PHASE2_MICROUSE.md
  blob_sha: 18745f32e2a2fb5efe8549e650e0aa1fdc7ee3cc
  exact_readback_completed: true
prior_current_commit: c3f75a1569b2306c130ea567cf8bb2b12a9db7df
prior_current_blob_sha: c3bd23150aed4d93034f4cd37f41f7ed63d8fb2f
effect_ceiling: CATALOG_ONLY_BOUNDED_READONLY_COMPARE
adoption_credit: 0
fitness_credit: 0
consumer_ack: NOT_OBSERVED
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate: 1_to_3_UNVALIDATED
custom_code_avoided_estimate: 15_to_50_LOC_UNVALIDATED
credentials:
  operator_supplied_this_campaign: 0
  principal: UNKNOWN
  effective_permission: UNKNOWN
  connector_managed: true
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_calls:
  compare_reads: 2
  completed_responses: 2
  errors: 0
  retries: 0
  fallbacks: 0
  mutations: 0
actual_upstream_request_count: UNKNOWN
actual_quota_consumed: UNKNOWN
observability:
  exposed: STATUS_COUNTS_BASE_SHA_MERGE_BASE_SHA_PER_FILE_STATS_EXTERNAL_CALL_TIME
  missing: RAW_HTTP_STATUS_HEADERS_REQUEST_ID_RATE_LIMIT_IDENTITY_UPSTREAM_ATTEMPTS_COMMIT_LIST_PATCHES_TRUNCATION_PROOF
measured_facts:
  phase_1_same_full_sha_compare:
    status: identical
    ahead_by: 0
    behind_by: 0
    total_commits: 0
    files_returned: 0
    external_call_time_ms: 677
  phase_2_adjacent_full_sha_compare:
    base_sha: c7db220c2b578148be7c63e10ce085c84f802326
    head_sha: 8b8d3f3e2510159d81b866165b85ef706a559ee3
    status: ahead
    ahead_by: 1
    behind_by: 0
    total_commits: 1
    files_returned: 1
    returned_file: state/coordination/experiments/cots_connector_x13/CURRENT.md
    file_status: modified
    additions: 32
    deletions: 27
    changes: 59
    base_sha_match: true
    merge_base_sha_match: true
    external_call_time_ms: 1540
    hydration_retry_fallback_or_candidate_mutation: false
mandatory_gates:
  - PREFER_FULL_COMMIT_SHAS_FOR_BINDING_DECISIONS
  - VERIFY_RETURNED_BASE_AND_MERGE_BASE_BINDINGS
  - TREAT_BRANCHES_AND_TAGS_AS_MUTABLE
  - BOUND_EXPECTED_COMMIT_AND_FILE_CARDINALITY
  - DO_NOT_ASSUME_COMPLETE_PATCH_OR_FILE_SET_NEAR_PROVIDER_LIMITS
  - VERIFY_LARGE_OR_HIGH_ASSURANCE_COMPARISONS_INDEPENDENTLY
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_RAW_PARITY_QUOTA_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_CREDIT
verifier: RAW_GITHUB_COMPARE_FOR_THE_SAME_FULL_SHA_PAIR_WITH_TRANSPORT_AND_RATE_LIMIT_HEADERS
consumer: HFO_COTS_CAPABILITY_INVENTORY
strongest_falsifier: RAW_GITHUB_COMPARE_DISAGREES_ON_STATUS_COMMIT_COUNT_FILE_PATH_OR_FILE_STATS
honest_flaw: TWO_EASY_FULL_SHA_PATHS_ONLY_COMMIT_LIST_PATCH_CONTENT_RENAME_BINARY_LARGE_DIFF_PAGINATION_PERMISSION_FAILURE_QUOTA_HIDDEN_RETRIES_CONSUMER_VALUE_AND_TIME_SAVINGS_UNVERIFIED
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_GATES
  admitted_interpretation: CONNECTOR_RETURNED_IDENTICAL_ZERO_DIFF_FOR_ONE_FULL_SHA_PAIR
phase_2_result:
  disposition: PHASE2_ACCEPTED_WITH_GATES
  admitted_interpretation: CONNECTOR_RETURNED_ONE_SMALL_NONZERO_FULL_SHA_COMPARISON_WITH_ONE_MODIFIED_FILE_AND_PER_FILE_COUNTS
next_wake:
  phase: 3_of_4
  planned_probe: ONE_NON_SECRET_INVALID_OR_UNKNOWN_FULL_SHA_COMPARE_TO_OBSERVE_FAILURE_NORMALIZATION_WITHOUT_RETRY
review_expiry_utc: 2026-08-11T06:48:00Z
valid_time_utc: 2026-08-04T06:48:00Z
recorded_time_utc: 2026-08-04T06:48:00Z
---

# X13 CURRENT v82

GitHub compare-commits phase 2 is accepted with gates. One adjacent full-SHA comparison returned `ahead`, one commit, and one modified file with per-file change counts; base and merge-base bindings matched. Adoption and fitness credit remain zero.
