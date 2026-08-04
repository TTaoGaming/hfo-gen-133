---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_001_PHASE1
experiment_id: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
prior_current_version: 84
candidate: Slack_public_message_search_bounded_readonly_surface
phase: 1_of_4
phase_result: PHASE1_ACCEPTED_WITH_GATES
wip: 1
effect_ceiling: BOUNDED_PUBLIC_READONLY_SEARCH_BASELINE
candidate_invocations: 1
retries: 0
fallbacks: 0
candidate_mutations: 0
query_boundary:
  scope: ONE_KNOWN_PUBLIC_CHANNEL
  content_types: MESSAGES_ONLY
  result_limit: 1
  context_requested: false
  bot_messages_included: true
  sort: TIMESTAMP_DESC
  query_text_persisted: false
measured_result:
  connector_completed: true
  returned_result_count: 1
  pagination_cursor_exposed: true
  surrounding_context_returned: false
  matched_message_text_returned: true
  permalink_like_reference_returned: true
  typed_message_objects_returned: false
  response_shape: JSON_WRAPPER_CONTAINING_RENDERED_TEXT
  raw_http_status_exposed: false
  raw_headers_exposed: false
  request_id_exposed: false
  rate_limit_headers_exposed: false
  connector_latency_ms: NOT_SURFACED
admitted_interpretation: CONNECTOR_RETURNED_ONE_MATCH_FROM_ONE_BOUNDED_PUBLIC_CHANNEL_SEARCH_AND_EXPOSED_A_CONTINUATION_CURSOR
non_admitted_interpretations:
  - COMPLETE_OR_STABLE_SEARCH_RESULT
  - EXACT_QUERY_FORWARDING
  - EXACT_UPSTREAM_METHOD
  - LEAST_PRIVILEGE_OR_EFFECTIVE_SCOPE
  - RAW_SLACK_API_PARITY
  - ACTUAL_RATE_LIMIT_OR_QUOTA_CONSUMPTION
  - ZERO_HIDDEN_RETRIES
  - METADATA_ONLY_RESPONSE
credentials:
  principal: UNKNOWN
  token_type: UNKNOWN
  effective_scope: UNKNOWN
  connector_managed: true
  least_privilege_proven: false
durability:
  connector_result: TRANSIENT
  durable_receipt: THIS_GIT_EVENT
observability:
  present:
    - ONE_RESULT_COUNT
    - CHANNEL_LABEL_IN_RENDERED_RESULT
    - RESULT_TIMESTAMP_IN_RENDERED_RESULT
    - CONTINUATION_CURSOR
  absent:
    - TYPED_RESULT_SCHEMA
    - RAW_HTTP_STATUS
    - RAW_HEADERS
    - REQUEST_ID
    - RATE_LIMIT_REMAINING
    - UPSTREAM_ATTEMPT_COUNT
portability:
  rating: LOW_TO_MEDIUM
  reason: SLACK_QUERY_MODIFIERS_AND_RESULT_FIELDS_ARE_PROVIDER_SPECIFIC_AND_CONNECTOR_RETURNS_RENDERED_TEXT_INSTEAD_OF_A_TYPED_API_ENVELOPE
failure_behavior: NOT_PROBED_IN_PHASE1
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_upstream_request_count: UNKNOWN
actual_quota_consumed: UNKNOWN
official_contract:
  slack_search_messages_url: https://docs.slack.dev/reference/methods/search.messages/
  slack_rate_limits_url: https://docs.slack.dev/apis/web-api/rate-limits/
  facts:
    - OFFICIAL_SEARCH_MESSAGES_REQUIRES_SEARCH_READ_FOR_USER_TOKENS
    - OFFICIAL_SEARCH_MESSAGES_IS_TIER_2_AND_DOCUMENTED_AS_LEGACY
    - OFFICIAL_SEARCH_MESSAGES_RESULTS_CAN_BE_AFFECTED_BY_USER_UI_SEARCH_FILTERS
    - OFFICIAL_SEARCH_MESSAGES_CAN_COLLAPSE_CLOSE_PROXIMITY_MATCHES
    - OFFICIAL_RATE_LIMIT_RESPONSE_USES_HTTP_429_AND_RETRY_AFTER
  connector_to_official_method_binding: NOT_PROVEN
custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate: 1_to_3_UNVALIDATED
verifier:
  official_primary_docs_reviewed: true
  direct_connector_receipt_observed: true
  distinct_raw_provider_witness: NOT_COMPLETED
consumer:
  catalog: HFO_COTS_CAPABILITY_INVENTORY
  operational: NOT_NAMED
  consumer_ack: NOT_OBSERVED
strongest_falsifier: SAME_PRINCIPAL_RAW_SLACK_SEARCH_OR_SLACK_UI_WITH_IDENTICAL_QUERY_BOUNDARY_DISAGREES_ON_MATCH_EXISTENCE_ORDER_OR_CURSOR_SEMANTICS
mandatory_gates:
  - USE_PUBLIC_SEARCH_ONLY_UNLESS_PRIVATE_SCOPE_IS_EXPLICITLY_APPROVED
  - BOUND_CHANNEL_CONTENT_TYPE_RESULT_COUNT_AND_CONTEXT
  - TREAT_RESULTS_AS_NONAUTHORITATIVE_AND_POTENTIALLY_FILTERED_OR_DEDUPLICATED
  - DO_NOT_PERSIST_MATCHED_TEXT_PERMALINK_MESSAGE_TIMESTAMP_AUTHOR_OR_CURSOR_WITHOUT_A_NAMED_RETENTION_NEED
  - DO_NOT_TREAT_CONCISE_OR_NO_CONTEXT_AS_METADATA_ONLY_BECAUSE_MATCHED_TEXT_WAS_RETURNED
  - PARSE_RENDERED_TEXT_ONLY_FOR CATALOG_EXPERIMENTS; REQUIRE_TYPED_SCHEMA_FOR_OPERATIONAL_AUTOMATION
  - DO_NOT_CLAIM_EXACT_UPSTREAM_METHOD_SCOPE_QUOTA_RAW_PARITY_OR_ZERO_HIDDEN_RETRIES
  - REQUIRE_NAMED_CONSUMER_ACK_AND_MEASURED_OUTCOME_BEFORE_OPERATIONAL_OR_FITNESS_CREDIT
honest_flaw: ONE_KNOWN_PUBLIC_CHANNEL_POSITIVE_MATCH_ONLY; THE_WRAPPER_RETURNED_MATCHED_CONTENT_AS_RENDERED_TEXT_DESPITE_A_CONCISE_NO_CONTEXT_REQUEST, AND IDENTITY_SCOPE_COMPLETENESS_FILTERING_DEDUPLICATION_PAGINATION_RATE_LIMITS_HIDDEN_RETRIES_FAILURES_CONSUMER_VALUE_AND_TIME_SAVINGS_REMAIN_UNVERIFIED
valid_time_utc: 2026-08-04T09:48:22Z
recorded_time_utc: 2026-08-04T09:48:22Z
---

# X13 Slack public message search — phase 1 baseline

One bounded read-only search of one known public channel returned one match and a continuation cursor. The connector also returned matched message text and a permalink-like reference inside a rendered text payload, so the requested concise/no-context mode is not a metadata-only boundary.

Official Slack documentation describes `search.messages` as a legacy Tier-2 method requiring `search:read` for user tokens, with results affected by user search filters and possible close-proximity collapsing. The connector's upstream method, principal, scope, quota consumption, and raw parity are not exposed or proven.

No Slack content, author, message timestamp, permalink, cursor, or exact query was persisted in this event. Adoption and fitness credit remain zero.
