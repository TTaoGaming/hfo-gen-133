---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
version: 81
prior_version: 80
candidate: GitHub_compare_commits_bounded_readonly_diff_metadata_surface
campaign_wake: 1_of_4
campaign_status: OPEN
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
adoption_mode: NOT_ADOPTED
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event:
  commit: 06f785961bf3adb91287ae55acd9a498f3c4237f
  path: state/coordination/experiments/cots_connector_x13/20260804T054800Z_GITHUB_COMPARE_COMMITS_PHASE1_BASELINE.md
  blob_sha: 8df5caaac7e6adf684efb3439d4a1bf5a8fcaf78
  exact_readback_completed: true
prior_current_commit: 8b8d3f3e2510159d81b866165b85ef706a559ee3
prior_current_blob_sha: bd6bd8f70d5144c98297150b76bc57333a9086fb
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
  compare_reads: 1
  completed_responses: 1
  errors: 0
  retries: 0
  fallbacks: 0
  mutations: 0
actual_upstream_request_count: UNKNOWN
actual_quota_consumed: UNKNOWN
observability:
  exposed: STATUS_COUNTS_BASE_SHA_MERGE_BASE_SHA_FILES_EXTERNAL_CALL_TIME
  missing: RAW_HTTP_HEADERS_REQUEST_ID_RATE_LIMIT_IDENTITY_UPSTREAM_ATTEMPTS
measured_facts:
  same_full_sha_compare_completed: true
  requested_sha: 8b8d3f3e2510159d81b866165b85ef706a559ee3
  status: identical
  ahead_by: 0
  behind_by: 0
  total_commits: 0
  files_returned: 0
  base_sha_match: true
  merge_base_sha_match: true
  external_call_time_ms: 677
  mutation_retry_fallback_or_file_fetch: false
mandatory_gates:
  - PREFER_FULL_COMMIT_SHAS_FOR_BINDING_DECISIONS
  - TREAT_BRANCHES_AND_TAGS_AS_MUTABLE
  - BOUND_COMMIT_AND_FILE_CARDINALITY
  - VERIFY_LARGE_COMPARISONS_INDEPENDENTLY
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_RAW_PARITY_QUOTA_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_CREDIT
verifier: RAW_GITHUB_COMPARE_WITH_SAME_SHA_PAIR_AND_TRANSPORT_TELEMETRY
consumer: HFO_COTS_CAPABILITY_INVENTORY
strongest_falsifier: RAW_SAME_SHA_COMPARE_RETURNS_NONIDENTICAL_OR_DIFFERENT_COMMIT_BINDING
honest_flaw: SAME_SHA_ZERO_DIFF_ONLY_CHANGED_DIFF_PAGINATION_PERMISSION_FAILURE_QUOTA_RETRY_CONSUMER_VALUE_AND_TIME_SAVINGS_UNVERIFIED
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_GATES
  admitted_interpretation: CONNECTOR_RETURNED_IDENTICAL_ZERO_DIFF_FOR_ONE_FULL_SHA_PAIR
next_wake:
  phase: 2_of_4
  planned_probe: BOUNDED_ADJACENT_FULL_SHA_COMPARISON_WITH_SMALL_NONZERO_FILE_SET
  planned_base_sha: c7db220c2b578148be7c63e10ce085c84f802326
  planned_head_sha: 8b8d3f3e2510159d81b866165b85ef706a559ee3
review_expiry_utc: 2026-08-11T05:48:00Z
valid_time_utc: 2026-08-04T05:48:00Z
recorded_time_utc: 2026-08-04T05:48:00Z
---

# X13 CURRENT v81

GitHub compare-commits phase 1 is accepted with gates. One same-full-SHA comparison returned `identical`, zero ahead/behind counts, zero commits, zero files, matching base and merge-base SHAs, and 677 ms connector time. Adoption and fitness credit remain zero.
