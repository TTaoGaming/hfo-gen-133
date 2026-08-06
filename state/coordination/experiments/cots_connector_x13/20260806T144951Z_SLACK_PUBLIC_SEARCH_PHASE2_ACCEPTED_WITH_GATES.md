---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_SEARCH_PUBLIC_READONLY_010
event_type: PHASE2_SMALLEST_HARMLESS_READONLY_MICRO_USE
phase: 2
phase_status: PHASE2_ACCEPTED_WITH_GATES
campaign_wake: 2_of_4
campaign_status: ACTIVE
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Slack_public_message_search_readonly_surface
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version: 137
expected_next_current_version: 138
prior_current_blob_sha: 1cb30ecc15aa0934f29b7bd26e98e8765d49df16
effect_ceiling: ONE_IDENTICAL_BOUNDED_PUBLIC_SEARCH_PLUS_BOUNDED_DIRECT_PUBLIC_CHANNEL_EXISTENCE_WITNESS_AND_GIT_FIRST_EVIDENCE
candidate_calls_this_phase: 3
candidate_search_calls_this_phase: 1
candidate_direct_channel_read_calls_this_phase: 2
candidate_mutations: 0
retries: 0
bounded_query_adjustments: 1
fallbacks: 1
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
search_replay_result:
  connector_error: null
  returned_result_count: 3
  pagination_cursor_present: true
  pagination_cursor_persisted: false
  result_channel_name: hfo-command-and-control
  result_channel_id_from_query_scope: C0BGNGPJFHU
  distinct_authors_observed: 1
  observed_author_label: TTao
  exact_message_ids_or_ts_exposed: false
  exact_permalinks_exposed: false
  provider_total_count_exposed: false
  provider_latency_exposed: false
  normalized_result_sha256: 5e1334ab9f209fd80ab1c737d8972a293672f925bc4ece98404ee56dff19c8e6
  phase_1_normalized_result_sha256: 5e1334ab9f209fd80ab1c737d8972a293672f925bc4ece98404ee56dff19c8e6
  normalized_result_digest_match: true
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
direct_channel_witness:
  channel_id: C0BGNGPJFHU
  known_write_receipt_message_ts: '1786020688.154669'
  exact_equality_bound_probe:
    oldest: '1786020688.154669'
    latest: '1786020688.154669'
    limit: 5
    returned_messages: 0
    connector_error: null
  widened_bounded_probe:
    oldest: '1786020600.000000'
    latest: '1786020800.000000'
    bounded_window_seconds: 200
    limit: 20
    returned_messages: 1
    connector_error: null
    witness_channel: hfo-command-and-control
    witness_display_timestamp: 2026-08-06_06:51:28_MDT
    witness_leading_marker: X13_GITHUB_CODE_SEARCH_DEFER
    campaign_token_present: true
    prior_event_commit_present: 09647078b4cb4c4670396a146c357235f8f6dc6f
    prior_current_version_present: 136
    normalized_witness_sha256: c905bed4d0fd9eadc0797f3c96a32182ac1dc9bf08bfb22bf79506487bbbf464
    author_email_observed_but_not_persisted: true
    stable_message_ts_or_permalink_exposed_by_read: false
measured_fact: IDENTICAL_BOUNDED_PUBLIC_SEARCH_REPLAY_RETURNED_THE_SAME_ORDERED_THREE_RESULT_DIGEST_AND_A_BOUNDED_DIRECT_CHANNEL_READ_CONFIRMED_ONE_KNOWN_PUBLIC_MESSAGE
andon: EXACT_EQUALITY_OLDEST_AND_LATEST_BOUNDS_RETURNED_EMPTY_WHILE_A_WIDENED_200_SECOND_WINDOW_RETURNED_THE_KNOWN_MESSAGE; DO_NOT_ASSUME_EQUALITY_BOUNDARY_SEMANTICS_OR_USE_EXACT_BOUND_EMPTY_AS_ABSENCE
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
  direct_read_bounds: REQUEST_PARAMETERS_DURABLE_IN_EVENT_BUT_PROVIDER_BOUNDARY_SEMANTICS_UNVERIFIED
observability:
  exposed:
    - bounded_search_result_count
    - result_channel_name
    - author_label
    - human_display_timestamp
    - truncated_search_snippet
    - pagination_cursor_presence
    - direct_channel_message_body_for_one_public_witness
    - connector_empty_success_separate_from_error
  hidden:
    - raw_provider_method_request_and_response
    - stable_message_ts_or_id_in_read_output
    - result_permalink
    - provider_total_count_and_completeness
    - exact_effective_identity_and_scope
    - workspace_and_token_binding
    - http_headers_request_id_and_rate_limit_debit
    - internal_retry_or_fanout_audit
    - index_freshness
    - oldest_latest_inclusivity_or_precision_contract
portability:
  rating: LOW_TO_MEDIUM
  reason: SLACK_SEARCH_GRAMMAR_CHANNEL_IDENTIFIERS_RESULT_SHAPE_OPAQUE_CURSOR_AND_TIME_BOUNDARY_BEHAVIOR_ARE_PROVIDER_AND_WRAPPER_SPECIFIC
failure_behavior:
  measured:
    - IDENTICAL_QUERY_NONEMPTY_SUCCESS_WITH_MATCHED_NORMALIZED_DIGEST
    - PAGINATION_CURSOR_PRESENCE_REPEATED
    - EXACT_EQUALITY_TIME_BOUND_EMPTY_SUCCESS
    - WIDENED_BOUNDED_TIME_WINDOW_NONEMPTY_SUCCESS
  unmeasured:
    - SYNTHETIC_NONMATCH_EMPTY_SEARCH
    - INVALID_QUERY
    - AUTHENTICATION_OR_PERMISSION_DENIAL
    - PRIVATE_DATA_EXCLUSION_VARIANCE
    - RATE_LIMIT
    - TRANSIENT_TRANSPORT_OR_SERVER_FAILURE
    - INDEX_LAG_OR_UNAVAILABLE
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_or_quota_evidence: NONE
nominal_rate_contract_evidence: LEGACY_SEARCH_MESSAGES_TIER_2_ONLY_IF_CONNECTOR_MAPS_TO_THAT_METHOD_AND_DIRECT_CHANNEL_HISTORY_RATE_CONTRACT_UNKNOWN_MAPPING_UNKNOWN
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DISTINCT_RAW_SLACK_PROVIDER_SEARCH_AND_CHANNEL_HISTORY_READ_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_WITH_THE_EXACT_QUERY_AND_TIME_BOUNDS
verifier_result: NOT_RUN
strongest_falsifier: MATCHED_RAW_PROVIDER_CALLS_RETURN_MATERIALLY_DIFFERENT_ORDERED_SEARCH_RESULTS_OR_SHOW_THAT_EQUALITY_BOUNDS_SHOULD_INCLUDE_THE_KNOWN_MESSAGE_UNDER_THE_SAME_PRINCIPAL_AND_SOURCE_STATE
mandatory_gates:
  - PUBLIC_CHANNEL_SEARCH_ONLY_UNLESS_OPERATOR_EXPLICITLY_AUTHORIZES_PRIVATE_SEARCH
  - TREAT_LIMIT_AS_OUTPUT_CAP_NOT_COMPLETENESS
  - HANDLE_CONTINUATION_EXPLICITLY_BUT_DO_NOT_TREAT_OPAQUE_CURSOR_AS_DURABLE_STATE
  - TREAT_SEARCH_RESULTS_AS_ACCESS_AND_INDEX_DEPENDENT_DISCOVERY_NOT_AUTHORITATIVE_SLACK_HISTORY
  - USE_A_BOUNDED_DIRECT_CHANNEL_READ_OR_RAW_PROVIDER_WITNESS_FOR_CONSEQUENTIAL_EXISTENCE_COMPLETENESS_OR_NEGATIVE_CLAIMS
  - DO_NOT_TREAT_EXACT_EQUALITY_OLDEST_LATEST_EMPTY_AS_ABSENCE_WITHOUT_VERIFIED_BOUNDARY_SEMANTICS
  - DO_NOT_INFER_EFFECTIVE_IDENTITY_SCOPE_PROVIDER_METHOD_INDEX_FRESHNESS_OR_QUOTA_FROM_SUCCESS
  - NO_UNBOUNDED_RETRY_OR_HIGH_RATE_POLLING
adoption_credit: 0
fitness_credit: 0
honest_flaw: THE_REPLAY_USED_A_SELF_REFERENTIAL_KNOWN_TOKEN_IN_ONE_PUBLIC_CHANNEL_DURING_A_STABLE_SHORT_INTERVAL; THE_DIRECT_WITNESS_REQUIRED_FULL_TEXT_HYDRATION_AND_ONE_BOUNDED_WINDOW_ADJUSTMENT; NO_RAW_PROVIDER_PARITY_OPERATOR_SAVINGS_OPERATIONAL_CONSUMER_PERMISSION_FAILURE_RATE_LIMIT_OR_GENERAL_RELEVANCE_WAS_ESTABLISHED
next_phase: PHASE3_BOUNDED_SYNTHETIC_NONMATCH_PUBLIC_SEARCH_AND_CONNECTOR_VARIANCE_PROBE_PENDING
review_expiry_utc: 2026-08-13T14:49:51Z
valid_time_utc: 2026-08-06T14:49:51Z
recorded_time_utc: 2026-08-06T14:49:51Z
sealed: true
---

# X13 Slack public search phase 2 — accepted with gates

The identical bounded public-search query returned the same ordered three-result digest as phase 1 and again exposed a continuation cursor. This establishes narrow near-immediate repeatability for one known-token query against one public channel; it does not establish completeness, later replay stability, general search quality, or raw-provider parity.

A separate direct channel-history witness confirmed the known public message in a bounded 200-second window. An exact equality-bound read using the known write receipt timestamp returned an empty success, while the widened window returned the message. Therefore exact `oldest == latest` empty results cannot be interpreted as absence unless the connector's time-boundary and precision semantics are independently verified.

No Slack mutation occurred. One bounded query adjustment was used after the equality-bound empty result. The connector exposed no direct charge, quota debit, raw provider method, request ID, effective identity, OAuth scope, stable message timestamp or permalink in read output, or index-freshness receipt.

Retain this surface provisionally only for bounded, human-reviewed public discovery with explicit continuation handling and direct-read or raw-provider witnesses for consequential claims.
