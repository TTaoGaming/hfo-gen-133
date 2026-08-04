---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
event_id: X13_GITHUB_COMPARE_COMMITS_PHASE2_MICROUSE_20260804T064800Z
phase: 2_of_4
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 81
candidate: GitHub_compare_commits_bounded_readonly_diff_metadata_surface
effect_ceiling: CATALOG_ONLY_BOUNDED_READONLY_COMPARE
operation:
  surface: GitHub.compare_commits
  read_only: true
  base_full_sha: c7db220c2b578148be7c63e10ce085c84f802326
  head_full_sha: 8b8d3f3e2510159d81b866165b85ef706a559ee3
  hydration_or_followup_fetch: false
measured_facts:
  completed_response: true
  connector_visible_error: false
  status: ahead
  ahead_by: 1
  behind_by: 0
  total_commits: 1
  files_returned: 1
  file_1_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
  file_1_status: modified
  file_1_additions: 32
  file_1_deletions: 27
  file_1_changes: 59
  previous_filename_present: false
  base_sha_match: true
  merge_base_sha_match: true
  external_call_time_ms: 1540
  retries: 0
  fallbacks: 0
  candidate_mutations: 0
  surfaced_paid_cost_usd: 0_NO_CHARGE_SURFACED
  operator_minutes_removed_measured: 0
estimates:
  operator_minutes_removed: 1_to_3_UNVALIDATED
  custom_code_avoided: 15_to_50_LOC_UNVALIDATED
credentials:
  operator_supplied_this_call: 0
  principal: UNKNOWN
  effective_permission: UNKNOWN
  connector_managed: true
durability:
  input_binding: TWO_FULL_COMMIT_SHAS
  result_persistence: GIT_EVENT_ONLY
observability:
  exposed: STATUS_COUNTS_BASE_SHA_MERGE_BASE_SHA_PER_FILE_STATS_EXTERNAL_CALL_TIME
  missing: RAW_HTTP_STATUS_HEADERS_REQUEST_ID_RATE_LIMIT_UPSTREAM_ATTEMPTS_COMMIT_LIST_PATCHES_TRUNCATION_PROOF
portability:
  semantic_surface: GITHUB_SPECIFIC_COMPARE_API
  portable_abstraction: BASE_HEAD_STATUS_COUNTS_AND_FILE_STATS_PARTIAL
failure_behavior_observed: NOT_EXERCISED_THIS_PHASE
actual_upstream_request_count: UNKNOWN
actual_quota_consumed: UNKNOWN
consumer: HFO_COTS_CAPABILITY_INVENTORY
consumer_ack: NOT_OBSERVED
verifier: RAW_GITHUB_COMPARE_FOR_THE_SAME_FULL_SHA_PAIR_WITH_TRANSPORT_AND_RATE_LIMIT_HEADERS
strongest_falsifier: RAW_GITHUB_COMPARE_DISAGREES_ON_STATUS_COMMIT_COUNT_FILE_PATH_OR_FILE_STATS
mandatory_gates:
  - PREFER_FULL_COMMIT_SHAS_FOR_BINDING_DECISIONS
  - VERIFY_RETURNED_BASE_AND_MERGE_BASE_BINDINGS
  - BOUND_EXPECTED_COMMIT_AND_FILE_CARDINALITY
  - DO_NOT_ASSUME_COMPLETE_PATCH_OR_FILE_SET_NEAR_PROVIDER_LIMITS
  - DO_NOT_USE_BRANCH_OR_TAG_RESULTS_AS_IMMUTABLE EVIDENCE
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_RAW_PARITY_QUOTA_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_CREDIT
honest_flaw: ONE_SINGLE_FILE_ADJACENT_COMPARISON_ONLY_COMMIT_LIST_PATCH_CONTENT_RENAME_BINARY_LARGE_DIFF_PAGINATION_PERMISSION_FAILURE_QUOTA_HIDDEN_RETRIES_CONSUMER_VALUE_AND_TIME_SAVINGS_UNVERIFIED
phase_result:
  disposition: PHASE2_ACCEPTED_WITH_GATES
  admitted_interpretation: CONNECTOR_RETURNED_ONE_SMALL_NONZERO_FULL_SHA_COMPARISON_WITH_ONE_MODIFIED_FILE_AND_PER_FILE_COUNTS
  adoption_credit: 0
  fitness_credit: 0
next_wake:
  phase: 3_of_4
  planned_probe: ONE_NON_SECRET_INVALID_OR_UNKNOWN_FULL_SHA_COMPARE_TO_OBSERVE_FAILURE_NORMALIZATION_WITHOUT_RETRY
valid_time_utc: 2026-08-04T06:48:00Z
recorded_time_utc: 2026-08-04T06:48:00Z
---

# X13 GitHub Compare Commits — Phase 2 Micro-use

A single bounded comparison between two full commit SHAs returned `ahead`, one commit, and one modified file with per-file change counts. No file hydration, retry, fallback, or candidate mutation occurred. The result is accepted only as a small nonzero connector-visible compare receipt; completeness, raw-provider parity, quota use, and operational value remain unverified.
