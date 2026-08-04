---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
version: 84
prior_version: 83
candidate: GitHub_compare_commits_bounded_readonly_diff_metadata_surface
campaign_wake: 4_of_4
campaign_status: CLOSED
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: true
phase_4_decision: ADOPT_WITH_GATES
adoption_mode: CATALOG_ONLY_NONOPERATIONAL
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event:
  commit: f60cf20b42731307e8824794fbc32eded864f0cf
  path: state/coordination/experiments/cots_connector_x13/20260804T084800Z_GITHUB_COMPARE_COMMITS_PHASE4_ADOPT_WITH_GATES.md
  blob_sha: 32ac5ec1531adff9b9bbbb1035598e99ea484f56
  exact_readback_completed: true
prior_current_commit: cc9a74c34e7dab09d676eb56f7421a735ea36d81
prior_current_blob_sha: 50f62453eceb3fd154271742dca8114bc8aadac2
effect_ceiling: CATALOG_ONLY_BOUNDED_READONLY_COMPARE
adoption_credit: 0
fitness_credit: 0
consumer_ack: NOT_OBSERVED
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate: 1_to_3_UNVALIDATED
custom_code_avoided_estimate: 15_to_50_LOC_UNVALIDATED
credentials:
  principal: UNKNOWN
  effective_permission: UNKNOWN
  connector_managed: true
  least_privilege_proven: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_calls:
  compare_reads: 3
  completed_success_responses: 2
  connector_visible_errors: 1
  retries: 0
  fallbacks: 0
  mutations: 0
actual_upstream_request_count: UNKNOWN
actual_quota_consumed: UNKNOWN
campaign_measured_facts:
  phase_1: IDENTICAL_ZERO_DIFF_FOR_ONE_SAME_FULL_SHA_PAIR
  phase_2: AHEAD_BY_ONE_WITH_ONE_MODIFIED_FILE_AND_RETURNED_BASE_AND_MERGE_BASE_BINDINGS
  phase_3: FAIL_CLOSED_404_WITHOUT_COMPARE_METADATA_FOR_ONE_SYNTHETIC_UNKNOWN_SHA
  successful_call_external_time_ms_total: 2217
failure_behavior:
  connector_visible: OUTER_404_WITHOUT_COMPARE_CONTENT
  interpretation: AMBIGUOUS_UNKNOWN_REF_ACCESS_PERMISSION_OR_WRAPPER_NORMALIZATION
verifier:
  distinct_raw_provider_witness: NOT_COMPLETED
  advisory_reducer_result: REVISE_NONBINDING
  advisory_receipt_blob_sha: cbe14efaf7680cccc9bf09c185310403a5d93d8b
consumer:
  catalog: HFO_COTS_CAPABILITY_INVENTORY
  operational: NOT_NAMED
strongest_falsifier: SAME_PRINCIPAL_RAW_GITHUB_COMPARE_DISAGREES_ON_PHASE2_RESULT_OR_RETURNS_VALID_METADATA_OR_NON_404_FOR_PHASE3_INPUTS
mandatory_gates:
  - USE_FULL_COMMIT_SHAS_FOR_BINDING_DECISIONS
  - VERIFY_RETURNED_BASE_AND_MERGE_BASE_BINDINGS_ON_SUCCESS
  - TREAT_BRANCHES_AND_TAGS_AS_MUTABLE_OBSERVATIONS
  - BOUND_CARDINALITY_AND_INDEPENDENTLY_VERIFY_LARGE_OR_HIGH_ASSURANCE_COMPARISONS
  - FAIL_CLOSED_WHEN_COMPARE_METADATA_IS_ABSENT
  - TREAT_404_AS_AMBIGUOUS_AND_DO_NOT_AUTOMATICALLY_RETRY_WITHOUT_CHANGED_EVIDENCE
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_RAW_PARITY_QUOTA_USE_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_RAW_WITNESS_NAMED_OPERATIONAL_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_OR_FITNESS_CREDIT
adopted_boundary:
  allowed: BOUNDED_READONLY_CATALOG_DISCOVERY_AND_LOW_ASSURANCE_SMALL_FULL_SHA_RELATION_CHECKS
  prohibited: MERGE_RELEASE_OR_HIGH_ASSURANCE_GATING_WITHOUT_INDEPENDENT_VERIFICATION
honest_flaw: ONLY_SAME_SHA_ONE_ADJACENT_SINGLE_FILE_DIFF_AND_ONE_SYNTHETIC_404_WERE_EXERCISED; IDENTITY_SCOPE_RAW_PARITY_PAGINATION_TRUNCATION_RENAMES_BINARY_LARGE_DIFFS_RATE_LIMITS_HIDDEN_RETRIES_PERMISSION_VARIANCE_CONSUMER_VALUE_AND_TIME_SAVINGS_REMAIN_UNVERIFIED
next_campaign:
  candidate: Slack_bounded_readonly_message_search_metadata_surface
  next_phase: 1_of_4
  status: QUEUED_NOT_STARTED
review_expiry_utc: 2026-08-11T08:48:00Z
valid_time_utc: 2026-08-04T08:48:00Z
recorded_time_utc: 2026-08-04T08:48:00Z
---

# X13 CURRENT v84

GitHub compare-commits is closed as `ADOPT_WITH_GATES` for catalog-only, nonoperational use. Three bounded reads produced one identical result, one small one-file nonzero result, and one fail-closed `404`; no retries, fallbacks, or candidate mutations occurred. Operational and fitness credit remain zero because identity, raw-provider parity, quota use, completeness, named consumer acknowledgment, and measured operator relief are absent.
