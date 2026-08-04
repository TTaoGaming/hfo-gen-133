---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
version: 83
prior_version: 82
candidate: GitHub_compare_commits_bounded_readonly_diff_metadata_surface
campaign_wake: 3_of_4
campaign_status: OPEN
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: false
phase_4_decision: PENDING
adoption_mode: NOT_ADOPTED
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event:
  commit: 8bc7c4266e2e83f2453221d497cdbff9fad3a5ce
  path: state/coordination/experiments/cots_connector_x13/20260804T074800Z_GITHUB_COMPARE_COMMITS_PHASE3_FAILURE_PROBE.md
  blob_sha: aae94e611c6511baa2fa82f2a607ae50f775f2b7
  exact_readback_completed: true
prior_current_commit: 17235637e3a60db39f62dc4f3345d7ab64ee7ffa
prior_current_blob_sha: fd66e92e90947a95dc6dfaf5e694bf7965cff315
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
phase_3_measured_fact:
  input: ONE_KNOWN_BASE_FULL_SHA_PLUS_ONE_SYNTHETIC_UNKNOWN_FULL_SHA
  connector_error: 404_NOT_FOUND
  compare_metadata_returned: false
  commits_returned: 0
  files_returned: 0
  raw_headers_or_request_id: NOT_EXPOSED
  connector_latency: NOT_EXPOSED
mandatory_gates:
  - FAIL_CLOSED_WHEN_COMPARE_METADATA_IS_ABSENT
  - TREAT_404_AS_AMBIGUOUS_NOT_AS_PROOF_OF_REF_ABSENCE_OR_PERMISSION_STATE
  - DO_NOT_AUTOMATICALLY_RETRY_404_WITHOUT_CHANGED_EVIDENCE
  - USE_FULL_COMMIT_SHAS_AND_VERIFY_RETURNED_BINDINGS_ON_SUCCESS
  - BOUND_CARDINALITY_AND_VERIFY_LARGE_COMPARISONS_INDEPENDENTLY
  - DO_NOT_CLAIM_RAW_PARITY_QUOTA_USE_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_CREDIT
verifier: RAW_GITHUB_COMPARE_SAME_INPUTS_SAME_PRINCIPAL_WITH_TRANSPORT_AND_RATE_LIMIT_HEADERS
consumer: HFO_COTS_CAPABILITY_INVENTORY
strongest_falsifier: RAW_GITHUB_COMPARE_RETURNS_NON_404_OR_VALID_COMPARE_METADATA_FOR_THE_SAME_INPUTS
honest_flaw: ONE_SYNTHETIC_FAILURE_PROBE_CANNOT_DISTINGUISH_UNKNOWN_REF_FROM_INACCESSIBLE_OBJECT_REPOSITORY_PERMISSION_OR_WRAPPER_NORMALIZATION_AND_OPERATIONAL_VALUE_REMAINS_UNMEASURED
phase_3_result:
  disposition: PHASE3_ACCEPTED_WITH_GATES
  admitted_interpretation: CONNECTOR_FAILED_CLOSED_WITH_404_AND_RETURNED_NO_COMPARE_CONTENT
next_wake:
  phase: 4_of_4
  planned_probe: DECISION_ONLY_NO_ADDITIONAL_COMPARE_CALL
  provisional_disposition: ADOPT_WITH_GATES_CATALOG_ONLY_NONOPERATIONAL
review_expiry_utc: 2026-08-11T07:48:00Z
valid_time_utc: 2026-08-04T07:48:00Z
recorded_time_utc: 2026-08-04T07:48:00Z
---

# X13 CURRENT v83

GitHub compare-commits phase 3 is accepted with gates. A known-base versus synthetic-unknown full-SHA comparison failed closed as connector-visible `404 Not Found` and returned no compare content. The result does not identify whether the cause was the unknown ref, an inaccessible object, repository permission, or wrapper normalization. Adoption and fitness credit remain zero.
