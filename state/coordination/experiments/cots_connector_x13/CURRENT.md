---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_001
version: 85
prior_version: 84
candidate: Slack_public_message_search_bounded_readonly_surface
campaign_wake: 1_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
adoption_mode: NOT_ADOPTED_CATALOG_EXPERIMENT_ONLY
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event:
  commit: a511eac5510b814e4e12c0959dd2603a14554808
  path: state/coordination/experiments/cots_connector_x13/20260804T094822Z_SLACK_PUBLIC_MESSAGE_SEARCH_PHASE1_BASELINE.md
  blob_sha: d1302663e3880d6e641e7a6b23b621339ce94cd8
  exact_readback_completed: true
prior_current_commit: 1e9ad4fbca352bf4097446ed65aa5f30d99e2f79
prior_current_blob_sha: f343e001af7add813466ebc85e72ef5dd7fe062e
effect_ceiling: BOUNDED_PUBLIC_READONLY_SEARCH_BASELINE
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
  public_search_reads: 1
  completed_success_responses: 1
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
  connector_latency_ms: NOT_SURFACED
official_contract:
  search_messages: LEGACY_TIER_2_REQUIRES_SEARCH_READ_FOR_USER_TOKEN
  result_variance: USER_UI_FILTERS_AND_CLOSE_PROXIMITY_COLLAPSING_DOCUMENTED
  rate_limit_failure: HTTP_429_WITH_RETRY_AFTER_DOCUMENTED
  connector_to_official_method_binding: NOT_PROVEN
durability:
  connector_result: TRANSIENT
  git_receipt: IMMUTABLE_EVENT_READ_BACK
observability:
  rating: PARTIAL
  missing: TYPED_SCHEMA_RAW_HTTP_HEADERS_REQUEST_ID_RATE_LIMIT_TELEMETRY_UPSTREAM_ATTEMPT_COUNT
portability:
  rating: LOW_TO_MEDIUM
  reason: PROVIDER_SPECIFIC_QUERY_SYNTAX_AND_RENDERED_TEXT_RESPONSE
failure_behavior: NOT_PROBED
verifier:
  official_primary_docs_reviewed: true
  direct_connector_receipt_observed: true
  distinct_raw_provider_witness: NOT_COMPLETED
consumer:
  catalog: HFO_COTS_CAPABILITY_INVENTORY
  operational: NOT_NAMED
strongest_falsifier: SAME_PRINCIPAL_RAW_SLACK_SEARCH_OR_UI_WITH_IDENTICAL_BOUNDARY_DISAGREES_ON_MATCH_EXISTENCE_ORDER_OR_CURSOR_SEMANTICS
mandatory_gates:
  - PUBLIC_SEARCH_ONLY_UNLESS_PRIVATE_SCOPE_IS_EXPLICITLY_APPROVED
  - BOUND_CHANNEL_CONTENT_TYPE_RESULT_COUNT_AND_CONTEXT
  - TREAT_RESULTS_AS_NONAUTHORITATIVE_AND_POTENTIALLY_FILTERED_OR_DEDUPLICATED
  - DO_NOT_PERSIST_MATCHED_CONTENT_OR_IDENTIFIERS_WITHOUT_NAMED_RETENTION_NEED
  - CONCISE_NO_CONTEXT_IS_NOT_A_METADATA_ONLY_BOUNDARY
  - REQUIRE_TYPED_SCHEMA_FOR_OPERATIONAL_AUTOMATION
  - DO_NOT_CLAIM_UPSTREAM_METHOD_SCOPE_QUOTA_RAW_PARITY_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_NAMED_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_OR_FITNESS_CREDIT
honest_flaw: ONLY_ONE_KNOWN_PUBLIC_CHANNEL_POSITIVE_MATCH_WAS_EXERCISED; MATCHED_CONTENT_WAS_RETURNED_AS_RENDERED_TEXT_DESPITE_CONCISE_NO_CONTEXT, WHILE IDENTITY_SCOPE_COMPLETENESS_FILTERING_DEDUPLICATION_PAGINATION_RATE_LIMITS_FAILURES_HIDDEN_RETRIES_CONSUMER_VALUE_AND_TIME_SAVINGS_REMAIN_UNVERIFIED
next_phase:
  phase: 2_of_4
  action: ONE_BOUNDED_PUBLIC_SEARCH_MICRO_USE_WITH_A_SYNTHETIC_UNLIKELY_TOKEN_EXPECTED_TO_RETURN_ZERO_RESULTS
  constraints: NO_PRIVATE_SEARCH_NO_CONTEXT_NO_PAGINATION_NO_RETRY_NO_CONTENT_PERSISTENCE_NO_MUTATION
review_expiry_utc: 2026-08-11T09:48:22Z
valid_time_utc: 2026-08-04T09:48:22Z
recorded_time_utc: 2026-08-04T09:48:22Z
---

# X13 CURRENT v85

Slack public message search phase 1 completed with one bounded read-only call. One match and a continuation cursor were returned, but the connector emitted matched content and a permalink-like reference inside rendered text rather than typed message objects; concise/no-context is therefore not a metadata-only boundary. Operational and fitness credit remain zero.
