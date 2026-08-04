---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_001
version: 86
prior_version: 85
candidate: Slack_public_message_search_bounded_readonly_surface
campaign_wake: 2_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
adoption_mode: NOT_ADOPTED_CATALOG_EXPERIMENT_ONLY
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event:
  commit: 529ed1024b050b1ea6b1e3d65150fe54689b64a3
  path: state/coordination/experiments/cots_connector_x13/20260804T104944Z_SLACK_PUBLIC_MESSAGE_SEARCH_PHASE2_ZERO_RESULT_MICROUSE.md
  blob_sha: e77d66d3f28b3d61d0d573b1686094364fd1b2b7
  exact_readback_completed: true
prior_current_commit: 0dcf28c236e9b5b0f77a460a204da1025d3b9c96
prior_current_blob_sha: 34edf8a8d73fcd19f53fe1e9ffa263468932b4b3
effect_ceiling: BOUNDED_PUBLIC_READONLY_ZERO_RESULT_MICRO_USE
adoption_credit: 0
fitness_credit: 0
consumer_ack: NOT_OBSERVED
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate: 1_to_3_UNVALIDATED
custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
credentials:
  principal: UNKNOWN
  token_type: UNKNOWN
  effective_scope: UNKNOWN
  connector_managed: true
  least_privilege_proven: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_calls:
  public_search_reads: 2
  completed_success_responses: 2
  positive_result_responses: 1
  empty_result_responses: 1
  retries: 0
  fallbacks: 0
  mutations: 0
actual_upstream_request_count: UNKNOWN
actual_quota_consumed: UNKNOWN
phase_1_measured_facts:
  search_boundary: ONE_KNOWN_PUBLIC_CHANNEL_MESSAGES_ONLY_LIMIT_1_NO_CONTEXT
  result_count: 1
  continuation_cursor_exposed: true
  matched_text_returned: true
  permalink_like_reference_returned: true
  typed_message_objects_returned: false
  response_shape: JSON_WRAPPER_CONTAINING_RENDERED_TEXT
phase_2_measured_facts:
  search_boundary: ONE_KNOWN_PUBLIC_CHANNEL_MESSAGES_ONLY_LIMIT_1_NO_CONTEXT_SYNTHETIC_UNLIKELY_TOKEN
  result_count: 0
  terminal_pagination_marker_exposed: true
  continuation_cursor_exposed: false
  matched_text_returned: false
  permalink_like_reference_returned: false
  query_text_echoed_in_rendered_response: true
  typed_message_objects_returned: false
  response_shape: JSON_WRAPPER_CONTAINING_RENDERED_TEXT
  connector_latency_ms: NOT_SURFACED
official_contract:
  search_messages: LEGACY_TIER_2_REQUIRES_SEARCH_READ_FOR_USER_TOKEN
  result_variance: USER_UI_FILTERS_AND_CLOSE_PROXIMITY_COLLAPSING_DOCUMENTED
  rate_limit_failure: HTTP_429_WITH_RETRY_AFTER_DOCUMENTED
  connector_to_official_method_binding: NOT_PROVEN
durability:
  connector_result: TRANSIENT
  git_receipts: TWO_IMMUTABLE_EVENTS_READ_BACK
observability:
  rating: PARTIAL
  present: RESULT_STATE_TERMINAL_PAGINATION_MARKER_QUERY_ECHO_IN_RENDERED_TEXT
  missing: TYPED_SCHEMA_RAW_HTTP_HEADERS_REQUEST_ID_RATE_LIMIT_TELEMETRY_UPSTREAM_ATTEMPT_COUNT
portability:
  rating: LOW_TO_MEDIUM
  reason: PROVIDER_SPECIFIC_QUERY_SYNTAX_AND_RENDERED_TEXT_RESPONSE
failure_behavior:
  empty_result: NORMAL_COMPLETED_RESPONSE
  explicit_failure_path: NOT_PROBED
verifier:
  official_primary_docs_reviewed: true
  direct_connector_receipts_observed: true
  distinct_raw_provider_witness: NOT_COMPLETED
consumer:
  catalog: HFO_COTS_CAPABILITY_INVENTORY
  operational: NOT_NAMED
strongest_falsifier: SAME_PRINCIPAL_RAW_SLACK_SEARCH_AT_THE_SAME_OBSERVATION_WINDOW_DISAGREES_ON_MATCH_EXISTENCE_OR_TERMINAL_PAGINATION_STATE_FOR_THE_IDENTICAL_BOUNDARY
mandatory_gates:
  - PUBLIC_SEARCH_ONLY_UNLESS_PRIVATE_SCOPE_IS_EXPLICITLY_APPROVED
  - BOUND_CHANNEL_CONTENT_TYPE_RESULT_COUNT_AND_CONTEXT
  - TREAT_POSITIVE_AND_ZERO_RESULTS_AS_NONAUTHORITATIVE_AND_POTENTIALLY_FILTERED_OR_DEDUPLICATED
  - DO_NOT_PERSIST_MATCHED_CONTENT_IDENTIFIERS_CURSORS_OR_EXACT_QUERY_TEXT_WITHOUT_NAMED_RETENTION_NEED
  - CONCISE_NO_CONTEXT_IS_NOT_A_METADATA_ONLY_BOUNDARY
  - ASSUME_QUERY_TEXT_MAY_BE_ECHOED_IN_CONNECTOR_OUTPUT
  - REQUIRE_TYPED_SCHEMA_FOR_OPERATIONAL_AUTOMATION
  - DO_NOT_CLAIM_UPSTREAM_METHOD_SCOPE_QUOTA_RAW_PARITY_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_NAMED_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_OR_FITNESS_CREDIT
honest_flaw: ONLY_ONE_POSITIVE_AND_ONE_SYNTHETIC_ZERO_RESULT_PUBLIC_SEARCH_HAVE_BEEN_EXERCISED; THE CONNECTOR RETURNS_RENDERED_TEXT_AND_ECHOES_QUERY_TEXT, WHILE IDENTITY_SCOPE_COMPLETENESS_FILTERING_DEDUPLICATION_PAGINATION_FAILURES_RATE_LIMITS_HIDDEN_RETRIES_CONSUMER_VALUE_AND_TIME_SAVINGS_REMAIN_UNVERIFIED
next_phase:
  phase: 3_of_4
  action: ONE_BOUNDED_PUBLIC_SEARCH_FAILURE_PROBE_USING_A_SYNTHETIC_INVALID_PAGINATION_CURSOR
  constraints: NO_PRIVATE_SEARCH_NO_CONTEXT_NO_RETRY_NO_FALLBACK_NO_CONTENT_PERSISTENCE_NO_MUTATION
review_expiry_utc: 2026-08-11T10:49:44Z
valid_time_utc: 2026-08-04T10:49:44Z
recorded_time_utc: 2026-08-04T10:49:44Z
---

# X13 CURRENT v86

Slack public message search phase 2 completed with one bounded read-only zero-result micro-use. The connector returned a terminal no-more-pages state and no matched content, but echoed the exact query text inside rendered output. Zero results remain nonauthoritative, operational and fitness credit remain zero, and phase 3 is limited to one synthetic invalid-cursor failure probe.
