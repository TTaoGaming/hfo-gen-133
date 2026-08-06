---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_SEARCH_PUBLIC_READONLY_010
event_type: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_BASELINE
phase: 1
phase_status: PHASE1_ACCEPTED_WITH_GATES
campaign_wake: 1_of_4
campaign_status: ACTIVE
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Slack_public_message_search_readonly_surface
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version: 136
expected_next_current_version: 137
prior_current_blob_sha: 3e792fe1d7805856dbb47d3c679e9fab9d065c90
effect_ceiling: ONE_BOUNDED_PUBLIC_READONLY_SEARCH_PLUS_GIT_FIRST_EVIDENCE_AND_CONDITIONAL_SLACK_FACT_POST
candidate_calls_this_phase: 1
candidate_mutations: 0
retries: 0
fallbacks: 0
query_contract:
  query_exact: '"X13_GITHUB_CODE_SEARCH_READONLY_009" in:<#C0BGNGPJFHU>'
  query_utf8_sha256: 66da0dfee3ecb6db34de06b77f7e86c08e88fb79d86675c98012ac3bcbd09208
  content_types: messages
  limit: 3
  include_bots: true
  sort: timestamp
  sort_dir: desc
  response_format: concise
  include_context: false
baseline_result:
  connector_error: null
  returned_result_count: 3
  pagination_cursor_present: true
  pagination_cursor_persisted: false
  result_channel_name: hfo-command-and-control
  result_channel_id_from_query_scope: C0BGNGPJFHU
  distinct_authors_observed: 1
  observed_author_label: TTao
  message_body_hydration: THREE_TRUNCATED_SEARCH_SNIPPETS
  exact_message_ids_or_ts_exposed: false
  exact_permalinks_exposed: false
  raw_query_echo_exposed: true
  provider_total_count_exposed: false
  provider_latency_exposed: false
normalized_result_contract:
  canonicalization: SORTED_KEY_WHITESPACE_FREE_UTF8_JSON_OVER_ORDERED_RANK_CHANNEL_AUTHOR_DISPLAY_TIMESTAMP_AND_LEADING_MARKER
  normalized_result_sha256: 5e1334ab9f209fd80ab1c737d8972a293672f925bc4ece98404ee56dff19c8e6
  ordered_descriptors:
    - rank: 1
      channel: hfo-command-and-control
      author: TTao
      display_timestamp: 2026-08-06_07:12:43_MDT
      leading_marker: S03_REVISE_X13_GITHUB_CODE_SEARCH_READONLY_009_PHASE4_DECISION_20260806T124836Z
    - rank: 2
      channel: hfo-command-and-control
      author: TTao
      display_timestamp: 2026-08-06_06:51:28_MDT
      leading_marker: X13_GITHUB_CODE_SEARCH_DEFER
    - rank: 3
      channel: hfo-command-and-control
      author: TTao
      display_timestamp: 2026-08-06_06:09:54_MDT
      leading_marker: S03_REVISE_X13_GITHUB_CODE_SEARCH_READONLY_009_PHASE3_20260806T114752Z
measured_fact: ONE_BOUNDED_PUBLIC_ONLY_SEARCH_RETURNED_THREE_TIMESTAMP_SORTED_MESSAGE_SNIPPETS_FROM_THE_SCOPED_CHANNEL_AND_EXPOSED_A_CONTINUATION_CURSOR
andon: SEARCH_RESULTS_ARE_ACCESS_AND_INDEX_DEPENDENT_TRUNCATED_DISCOVERY; LIMIT_THREE_IS_NOT_COMPLETENESS_AND_OPAQUE_CURSOR_IS_NOT_DURABLE_STATE
official_contract:
  primary_reference_search_messages: https://docs.slack.dev/reference/methods/search.messages/
  primary_reference_public_scope: https://docs.slack.dev/reference/scopes/search.read.public/
  primary_reference_realtime_search: https://docs.slack.dev/apis/web-api/real-time-search-api/
  nearest_documented_method_status: SEARCH_MESSAGES_IS_LEGACY_AND_SLACK_RECOMMENDS_REAL_TIME_SEARCH_API
  nearest_documented_legacy_scope: search:read_USER_TOKEN
  documented_public_scope: search:read.public
  documented_legacy_rate_tier: TIER_2_20_PLUS_PER_MINUTE
  mapping_of_connector_to_provider_method: UNKNOWN
  official_contract_notes:
    - SEARCH_RESULTS_CAN_BE_AFFECTED_BY_USER_SEARCH_FILTERS
    - CLOSE_PROXIMITY_MATCHES_CAN_BE_COLLAPSED_TO_ONE_MATCH
    - COUNT_OR_LIMIT_IS_A_PAGE_CAP_NOT_COMPLETENESS_EVIDENCE
    - PUBLIC_SEARCH_ACCESS_DEPENDS_ON_EFFECTIVE_PRINCIPAL_AND_SCOPE
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials:
  connector_managed: true
  effective_identity: UNKNOWN
  effective_scope: UNKNOWN
  token_type_storage_and_workspace_binding: UNKNOWN
durability:
  git_evidence: DURABLE_AFTER_READBACK
  slack_messages: MUTABLE_OR_DELETABLE_SOURCE_RECORDS
  search_index_and_order: MUTABLE
  pagination_cursor: OPAQUE_NOT_PERSISTED_NOT_DURABLE
observability:
  exposed:
    - bounded_result_count
    - result_channel_name
    - author_label
    - human_display_timestamp
    - truncated_message_snippet
    - pagination_cursor_presence
    - connector_error_state
  hidden:
    - raw_provider_method_request_and_response
    - stable_message_ts_or_id
    - result_permalink
    - provider_total_count_and_completeness
    - exact_effective_identity_and_scope
    - workspace_and_token_binding
    - http_headers_request_id_and_rate_limit_debit
    - internal_retry_or_fanout_audit
    - index_freshness
portability:
  rating: LOW_TO_MEDIUM
  reason: SLACK_SEARCH_GRAMMAR_CHANNEL_IDENTIFIERS_RESULT_SHAPE_AND_OPAQUE_CURSOR_ARE_PROVIDER_AND_WRAPPER_SPECIFIC
failure_behavior:
  measured:
    - BOUNDED_NONEMPTY_SUCCESS
    - PAGINATION_CURSOR_PRESENT
  unmeasured:
    - EMPTY_SUCCESS
    - INVALID_QUERY
    - AUTHENTICATION_OR_PERMISSION_DENIAL
    - PRIVATE_DATA_EXCLUSION_VARIANCE
    - RATE_LIMIT
    - TRANSIENT_TRANSPORT_OR_SERVER_FAILURE
    - INDEX_LAG_OR_UNAVAILABLE
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_or_quota_evidence: NONE
nominal_rate_contract_evidence: LEGACY_SEARCH_MESSAGES_TIER_2_ONLY_IF_CONNECTOR_MAPS_TO_THAT_METHOD_MAPPING_UNKNOWN
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DISTINCT_RAW_SLACK_PROVIDER_SEARCH_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EXACT_QUERY_PLUS_DIRECT_CHANNEL_READ_FOR_KNOWN_MESSAGE_EXISTENCE
verifier_result: NOT_RUN
strongest_falsifier: MATCHED_RAW_PROVIDER_SEARCH_OR_DIRECT_CHANNEL_WITNESS_RETURNS_MATERIALLY_DIFFERENT_PUBLIC_RESULTS_OR_SHOWS_THE_WRAPPER_INCLUDED_NONPUBLIC_DATA_MISSCOPED_THE_CHANNEL_OR_OMITTED_A_KNOWN_MATCH_WITHIN_THE_SAME_ACCESS_AND_TIME_CONTEXT
mandatory_gates:
  - PUBLIC_CHANNEL_SEARCH_ONLY_UNLESS_OPERATOR_EXPLICITLY_AUTHORIZES_PRIVATE_SEARCH
  - TREAT_LIMIT_AS_OUTPUT_CAP_NOT_COMPLETENESS
  - HANDLE_CONTINUATION_EXPLICITLY_BUT_DO_NOT_TREAT_OPAQUE_CURSOR_AS_DURABLE_STATE
  - RETAIN_STABLE_MESSAGE_TS_OR_PERMALINK_WHEN_AVAILABLE; THIS_WRAPPER_DID_NOT_EXPOSE_THEM_IN_CONCISE_OUTPUT
  - TREAT_RESULTS_AS_ACCESS_AND_INDEX_DEPENDENT_DISCOVERY_NOT_AUTHORITATIVE_SLACK_HISTORY
  - REQUIRE_DIRECT_CHANNEL_OR_RAW_PROVIDER_WITNESS_FOR_CONSEQUENTIAL_NEGATIVE_OR_COMPLETENESS_CLAIMS
  - DO_NOT_INFER_EFFECTIVE_IDENTITY_SCOPE_PROVIDER_METHOD_INDEX_FRESHNESS_OR_QUOTA_FROM_SUCCESS
  - NO_UNBOUNDED_RETRY_OR_HIGH_RATE_POLLING
adoption_credit: 0
fitness_credit: 0
honest_flaw: THE_BASELINE_USED_A_SELF_REFERENTIAL_KNOWN_TOKEN_IN_ONE_PUBLIC_CHANNEL_AND RETURNED_TRUNCATED_SNIPPETS_WITHOUT_STABLE_MESSAGE_IDS_OR_PERMALINKS; IT_DOES_NOT_TEST_GENERAL_RELEVANCE_COMPLETENESS_EMPTY_RESULTS_PERMISSION_BOUNDARIES_INDEX_LAG_FAILURES_OPERATOR_SAVINGS_OR_OPERATIONAL_CONSUMER_VALUE
next_phase: PHASE2_IDENTICAL_BOUNDED_QUERY_REPEATABILITY_AND_DIRECT_CHANNEL_WITNESS_PENDING
review_expiry_utc: 2026-08-13T13:48:04Z
valid_time_utc: 2026-08-06T13:48:04Z
recorded_time_utc: 2026-08-06T13:48:04Z
sealed: true
---

# X13 Slack public search phase 1 — accepted with gates

One bounded public-only Slack message search returned three timestamp-sorted snippets from the explicitly scoped `#hfo-command-and-control` channel and exposed a continuation cursor. The call made no Slack mutation, used no retry or fallback, and surfaced no charge. The exact query bytes and a deterministic normalized-result digest are recorded for a later bounded replay.

This is discovery evidence, not completeness or durable state. The wrapper returned truncated snippets but no stable message timestamp, message ID, permalink, provider total count, request ID, effective identity, OAuth scope, raw provider method, rate-limit debit, or index-freshness receipt. The returned cursor is opaque and was intentionally not persisted.

Slack's official documentation identifies `search.messages` as a legacy method and recommends the Real-time Search API. The legacy contract is Tier 2 and requires a user token with `search:read`; Slack also documents `search:read.public` for public-channel search. The connector's actual provider mapping and effective scope are unknown, so those values are contract references rather than direct connector receipts. Search can also be affected by user search filters and may collapse nearby matching messages.

Retain this surface provisionally only for bounded, human-reviewed public catalog discovery. Treat result limits as caps, treat results as access- and index-dependent, and require a direct channel or raw-provider witness before making consequential completeness or negative claims.
