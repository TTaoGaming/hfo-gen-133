---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
event_id: X13_GITHUB_COMPARE_COMMITS_PHASE3_FAILURE_PROBE_20260804T074800Z
phase: 3_of_4
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 82
candidate: GitHub_compare_commits_bounded_readonly_diff_metadata_surface
effect_ceiling: CATALOG_ONLY_BOUNDED_READONLY_COMPARE
operation:
  surface: GitHub.compare_commits
  read_only: true
  base_full_sha: c7db220c2b578148be7c63e10ce085c84f802326
  head_synthetic_unknown_full_sha: "0000000000000000000000000000000000000000"
  retry_or_fallback: false
  hydration_or_followup_fetch: false
measured_facts:
  completed_success_response: false
  connector_visible_error: true
  error_message: Not Found
  error_status: "404"
  documentation_url: https://docs.github.com/rest/commits/commits#compare-two-commits
  is_error: true
  compare_status_returned: false
  commits_returned: 0
  files_returned: 0
  raw_http_headers_returned: false
  request_id_returned: false
  rate_limit_telemetry_returned: false
  connector_latency_ms: NOT_EXPOSED
  retries: 0
  fallbacks: 0
  candidate_mutations: 0
  surfaced_paid_cost_usd: 0_NO_CHARGE_SURFACED
  operator_minutes_removed_measured: 0
admitted_interpretation: CONNECTOR_FAILED_CLOSED_WITH_404_NOT_FOUND_FOR_ONE_KNOWN_BASE_AND_SYNTHETIC_UNKNOWN_FULL_SHA_PAIR_WITHOUT_RETURNING_COMPARE_CONTENT
not_admitted:
  - UNKNOWN_HEAD_SHA_WAS_THE_UNIQUE_CAUSE
  - REPOSITORY_OR_OBJECT_EXISTENCE
  - PERMISSION_STATE
  - RAW_PROVIDER_ERROR_PARITY
  - UPSTREAM_REQUEST_COUNT
  - ACTUAL_RATE_LIMIT_OR_QUOTA_CONSUMPTION
  - ZERO_HIDDEN_RETRIES
estimates:
  operator_minutes_removed: 1_to_3_UNVALIDATED
  custom_code_avoided: 15_to_50_LOC_UNVALIDATED
credentials:
  operator_supplied_this_call: 0
  principal: UNKNOWN
  effective_permission: UNKNOWN
  connector_managed: true
durability:
  input_binding: ONE_KNOWN_FULL_SHA_AND_ONE_SYNTHETIC_UNKNOWN_FULL_SHA
  result_persistence: GIT_EVENT_ONLY
observability:
  exposed: ERROR_MESSAGE_STATUS_DOCUMENTATION_URL_IS_ERROR
  missing: RAW_HTTP_HEADERS_REQUEST_ID_RATE_LIMIT_IDENTITY_UPSTREAM_ATTEMPTS_FIELD_OR_REF_SPECIFIC_REASON
portability:
  semantic_surface: GITHUB_SPECIFIC_COMPARE_API
  portable_abstraction: FAIL_CLOSED_NOT_FOUND_PARTIAL
failure_behavior_observed: OUTER_ERROR_404_WITHOUT_COMPARE_METADATA_OR_CONTENT
actual_upstream_request_count: UNKNOWN
actual_quota_consumed: UNKNOWN
consumer: HFO_COTS_CAPABILITY_INVENTORY
consumer_ack: NOT_OBSERVED
verifier: RAW_GITHUB_COMPARE_FOR_THE_SAME_INPUTS_UNDER_THE_SAME_PRINCIPAL_WITH_TRANSPORT_AND_RATE_LIMIT_HEADERS
strongest_falsifier: RAW_GITHUB_COMPARE_FOR_THE_SAME_INPUTS_RETURNS_NON_404_OR_VALID_COMPARE_METADATA
mandatory_gates:
  - TREAT_404_AS_AMBIGUOUS_BETWEEN_UNKNOWN_REF_INACCESSIBLE_OBJECT_OR_REPOSITORY_AND_WRAPPER_NORMALIZATION
  - DO_NOT_AUTOMATICALLY_RETRY_DETERMINISTIC_404_WITHOUT_CHANGED_INPUT_IDENTITY_OR_PERMISSION_EVIDENCE
  - FAIL_CLOSED_WHEN_COMPARE_METADATA_IS_ABSENT
  - REQUIRE_FULL_SHA_INPUTS_AND_VERIFY_RETURNED_BINDINGS_ON_SUCCESS
  - DO_NOT_CLAIM_RAW_PARITY_PERMISSION_STATE_QUOTA_USE_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_CREDIT
honest_flaw: ONE_SYNTHETIC_UNKNOWN_SHA_PROBE_ONLY_DOES_NOT_DISTINGUISH_MISSING_REF_FROM_INACCESSIBLE_OBJECT_REPOSITORY_PERMISSION_OR_WRAPPER_POLICY_AND_EXPOSES_NO_RAW_HEADERS_RATE_LIMITS_UPSTREAM_ATTEMPTS_CONSUMER_VALUE_OR_TIME_SAVINGS
phase_result:
  disposition: PHASE3_ACCEPTED_WITH_GATES
  adoption_credit: 0
  fitness_credit: 0
next_wake:
  phase: 4_of_4
  planned_probe: DECISION_ONLY_NO_ADDITIONAL_GITHUB_COMPARE_CALL
  provisional_disposition: ADOPT_WITH_GATES_CATALOG_ONLY_NONOPERATIONAL
valid_time_utc: 2026-08-04T07:48:00Z
recorded_time_utc: 2026-08-04T07:48:00Z
---

# X13 GitHub Compare Commits — Phase 3 Failure Probe

A single read-only comparison used one known full commit SHA and one non-secret synthetic unknown 40-hex SHA. The connector returned `404 Not Found` with no compare metadata, commits, or files. This is accepted only as fail-closed connector behavior; it does not identify whether the cause was the unknown ref, inaccessible repository or object, permission state, or wrapper normalization.
