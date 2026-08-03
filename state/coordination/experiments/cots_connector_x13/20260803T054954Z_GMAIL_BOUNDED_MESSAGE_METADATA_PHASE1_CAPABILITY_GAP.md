---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_BOUNDED_MESSAGE_METADATA_SEARCH_READONLY_001
phase: 1
phase_name: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
campaign_wake: 1_of_4
expected_prior_version: 56
next_version: 57
candidate: Gmail_bounded_message_metadata_search_readonly_surface
carrier: X13_COTS_AND_CONNECTOR_PDCA_LAB
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_blob_sha: bdfb588e563bcc65d3da5c10d9c9409ccf942f6d
wip: 1
valid_time_utc: 2026-08-03T05:49:54Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
effect_ceiling: ONE_BOUNDED_READ_ONLY_ID_SEARCH_OFFICIAL_CONTRACT_BASELINE_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_SLACK_MEASURED_ANDON
candidate_invocations: 1
writes_sends_drafts_labels_archive_trash_delete_attachment_or_mailbox_mutations: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_consumed_message_discovery: 1_to_3_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
direct_receipt:
  action: Gmail.search_email_ids
  query_class: BOUNDED_RECENT_NON_SPAM_NON_TRASH
  query: newer_than:1d_-in:spam_-in:trash
  requested_max_results: 1
  returned_message_id_count: 1
  next_page_token_present: true
  exact_message_ids_persisted: false
  exact_page_token_persisted: false
  connector_error: null
  external_call_time_ms: 349
  carrier_retries: 0
  private_headers_bodies_snippets_or_attachments_returned: false
  mutation_effect: false
direct_capability_inventory:
  explicit_id_only_search_action_present: true
  explicit_metadata_only_get_or_search_action_present: false
  explicit_format_metadata_control_present: false
  explicit_metadata_headers_allowlist_control_present: false
  body_bearing_read_actions_present_but_excluded: true
  conclusion_scope: CURRENT_CONNECTOR_TOOL_CONTRACT_AND_THIS_DIRECT_CALL_ONLY
official_contract_checked_2026_08_03:
  messages_list: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
  messages_get: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/get
  format_enum: https://developers.google.com/workspace/gmail/api/reference/rest/v1/Format
  scopes: https://developers.google.com/workspace/gmail/api/auth/scopes
  quota: https://developers.google.com/workspace/gmail/api/reference/quota
  messages_list_returns: MESSAGE_ID_AND_THREAD_ID_ONLY
  messages_list_max_results_default: 100
  messages_list_max_results_maximum: 500
  messages_list_query_semantics: GMAIL_SEARCH_BOX_QUERY
  query_with_gmail_metadata_scope: NOT_ALLOWED
  messages_get_metadata_mode: RETURNS_ID_LABELS_AND_HEADERS
  metadata_headers_allowlist_requires: FORMAT_METADATA
  messages_list_quota_units_per_request: 5
  messages_get_quota_units_per_request: 20
  post_2026_05_01_per_minute_per_project_if_applicable: 1200000
  post_2026_05_01_per_minute_per_user_per_project_if_applicable: 6000
  post_2026_05_01_daily_billing_threshold_units_if_applicable: 80000000
credentials:
  connector_reached_mailbox_without_error: true
  operator_supplied_credentials_this_wake: 0
  authenticated_identity: UNKNOWN
  credential_type: UNKNOWN
  effective_oauth_scope: UNKNOWN
  token_storage_and_custody: CONNECTOR_MANAGED_UNINSPECTED
  least_privilege_closed: false
scope_andon:
  triggered: true
  measured_fact: QUERY_CAPABLE_ID_SEARCH_SUCCEEDED_BUT_CURRENT_TOOL_CONTRACT_EXPOSES_NO_METADATA_ONLY_FORMAT_OR_HEADER_ALLOWLIST_CONTROL
  official_constraint: RAW_MESSAGES_LIST_Q_CANNOT_BE_USED_WITH_GMAIL_METADATA_SCOPE
  implication: DO_NOT_DESCRIBE_THIS_LIVE_CONNECTOR_AS_GMAIL_METADATA_SCOPED_OR_METADATA_ONLY
  alternative_explanations:
    - CONNECTOR_USES_A_BROADER_SCOPE
    - CONNECTOR_TRANSFORMS_OR_ENRICHES_THE_REQUEST_OUTSIDE_RAW_MESSAGES_LIST
    - CONNECTOR_CONTRACT_HIDES_THE_EFFECTIVE_REQUEST_PATH
  resolved: false
custom_code_avoided_estimate:
  bounded_id_discovery: 25_to_80_LOC_UNVALIDATED
  metadata_only_fetch_and_header_allowlisting: 0_NOT_AVOIDED_BY_CURRENT_EXPOSED_SURFACE
custom_policy_not_avoided:
  - EFFECTIVE_SCOPE_IDENTITY_CREDENTIAL_CUSTODY_AND_LEAST_PRIVILEGE
  - FORMAT_METADATA_AND_HEADER_ALLOWLIST_ENFORCEMENT
  - PRIVATE_IDENTIFIER_AND_PAGE_TOKEN_MINIMIZATION
  - PAGINATION_COMPLETENESS_DUPLICATE_AND_ORDERING_CONTROL
  - RATE_LIMIT_RETRY_BACKOFF_COST_AND_QUOTA_ACCOUNTING
  - EMPTY_RESULT_AND_PERMISSION_FAILURE_CLASSIFICATION
  - INDEPENDENT_RAW_API_OR_GMAIL_UI_VERIFICATION
durability: EPHEMERAL_POINT_IN_TIME_MAILBOX_QUERY_NOT_A_SNAPSHOT_EVENT_STREAM_OR_WORKFLOW_CHECKPOINT
observability: ID_COUNT_CURSOR_PRESENCE_NORMALIZED_ERROR_FIELDS_LATENCY_AND_CONNECTOR_ACTION_VISIBLE_RAW_HTTP_REQUEST_RESPONSE_REQUEST_ID_EFFECTIVE_SCOPE_QUOTA_HEADERS_RETRY_AUDIT_AND_INTERNAL_ENRICHMENT_HIDDEN
portability: MEDIUM_FOR_GMAIL_QUERY_SYNTAX_AND_ID_DISCOVERY_LOW_FOR_CROSS_PROVIDER_METADATA_SEMANTICS
failure_behavior:
  positive_id_only_search: OBSERVED
  empty_valid_query: NOT_TESTED_THIS_CAMPAIGN
  malformed_query: NOT_TESTED
  authentication_or_permission_denial: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  transient_server_failure: NOT_TESTED
  independent_raw_or_UI_readback: NOT_TESTED
admitted_scope_this_phase:
  - ONE_PAGE_BOUNDED_ID_ONLY_DISCOVERY_WITH_SMALL_MAX_RESULTS
  - COUNT_AND_CURSOR_PRESENCE_ONLY_FOR_DURABLE_LOGGING
excluded_scope_this_phase:
  - MESSAGE_METADATA_BODY_SNIPPET_HEADER_OR_ATTACHMENT_FETCH
  - SEND_DRAFT_LABEL_MODIFY_ARCHIVE_TRASH_DELETE_OR_ANY_MAILBOX_MUTATION
  - CLAIM_OF_GMAIL_METADATA_SCOPE_OR_LEAST_PRIVILEGE
  - COMPLETENESS_OR_DURABLE_MAILBOX_STATE_CLAIMS
mandatory_gates:
  - KEEP_EXACT_MESSAGE_IDS_AND_PAGE_TOKENS_OUT_OF_GIT_SLACK_AND_ROUTINE_TRACES
  - DO_NOT_CALL_BODY_BEARING_READ_ACTIONS_FOR_COUNT_OR_DISCOVERY_QUESTIONS
  - DO_NOT_CLAIM_METADATA_ONLY_OPERATION_UNTIL_FORMAT_METADATA_AND_METADATA_HEADERS_ALLOWLIST_CONTROLS_ARE_EXPOSED_AND_PROVEN
  - DO_NOT_INFER_EFFECTIVE_OAUTH_SCOPE_FROM_SUCCESS
  - TREAT_MAX_RESULTS_AS_PAGE_CAP_NOT_TOTAL_MATCH_COUNT
  - TREAT_NEXT_PAGE_TOKEN_PRESENCE_AS_MORE_WRAPPER_VISIBLE_RESULTS_NOT_COMPLETENESS
  - REQUIRE_SOURCE_BOUND_CONSUMER_ACK_BEFORE_FITNESS_CREDIT
strongest_falsifier: A_DIRECT_INSPECTION_OR_CONNECTOR_UPDATE_EXPOSES_AND_PROVES_FORMAT_METADATA_WITH_SELECTED_METADATA_HEADERS_UNDER_A_VERIFIED_GMAIL_METADATA_SCOPE_OR_SHOWS_THAT_SEARCH_EMAIL_IDS_RETURNS_OR_PERSISTS_PRIVATE_CONTENT_BEYOND_IDS
verifier: RAW_GMAIL_MESSAGES_LIST_AND_MESSAGES_GET_WITH_IDENTICAL_QUERY_PAGE_AND_FORMAT_CONTEXT_PLUS_CONNECTOR_SCOPE_INSPECTION
consumer:
  - HFO_EXECUTIVE_ASSISTANT_BOUNDED_MAIL_DISCOVERY
  - HFO_WAITING_AND_INBOX_STATUS_CELLS
honest_flaw: THIS_WAKE REPEATED_THE_ALREADY_ADOPTED_ID_ONLY_DISCOVERY_PRIMITIVE_TO_BASELINE_A_NARROWER_METADATA_CAMPAIGN; IT_DID_NOT_PROVE_A_METADATA_ONLY_POSITIVE_PATH_EFFECTIVE_SCOPE_TRUE_PROVIDER_CALL_COUNT_OR_ANY_OPERATOR_TIME_REDUCTION
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_CAPABILITY_GAP_SCOPE_AND_PRIVACY_ANDON
  metadata_candidate_status: NOT_YET_PROVEN
next_wake:
  phase: 2_of_4
  proposed_action: SMALLEST_PRIVACY_SAFE_MICRO_USE_USING_ID_ONLY_DISCOVERY_AND_NO_METADATA_FETCH_OR_RECORD_A_DEFER_IF_NO_SAFE_POSITIVE_FIXTURE_EXISTS
  excluded_effects: SEND_DRAFT_MODIFY_LABEL_ARCHIVE_TRASH_DELETE_ATTACHMENT_DOWNLOAD_BODY_FETCH_OR_SECRET_EXPOSURE
sealed: true
---

# X13 Gmail bounded message-metadata search — phase 1

One bounded, read-only Gmail ID search returned one message identifier and a continuation token. Exact identifiers and token values were not copied into Git or Slack, and no headers, snippets, bodies, attachments, or mailbox mutations were returned by the action.

The measured connector surface does not currently expose an explicit `format=METADATA` control or a selected-header allowlist. Official Gmail contracts separate ID-only listing from metadata retrieval: `messages.list` returns IDs and thread IDs, while `messages.get(format=METADATA)` returns labels and headers and can restrict headers with `metadataHeaders`. Officially, the `q` parameter is not allowed under the `gmail.metadata` scope. Therefore, query-capable success must not be described as proof that the live connector is metadata-scoped or least-privilege.

Phase 1 admits only bounded ID-only discovery with privacy-minimized durable logs. A positive metadata-only path remains unproven. Measured operator relief is zero, surfaced cost is zero, ConsumerAck is absent, and the true provider call count, effective OAuth scope, quota usage, retry behavior, and independent verification remain unknown.
