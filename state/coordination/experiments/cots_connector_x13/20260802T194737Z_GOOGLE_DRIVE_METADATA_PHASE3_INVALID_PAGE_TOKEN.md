---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_BOUNDED_METADATA_SEARCH_READONLY_001
event_type: PHASE3_FAILURE_PERMISSION_PORTABILITY_CONNECTOR_VARIANCE_PROBE
phase: 3_of_4
prior_current_version: 46
expected_current_version: 47
candidate: Google_Drive_bounded_metadata_only_search_connector_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T19:47:37Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
probe:
  operation: Google_Drive.search
  query_value: HFO
  item_type: document
  topn: 1
  best_effort_fetch: false
  require_viewed_by_user: false
  page_token_source: SYNTHETIC_NON_PROVIDER_TOKEN
  exact_token_persisted: false
  retry_count_carrier: 0
  content_fetch_requested: false
  mutation_requested: false
direct_receipt:
  connector_result: TOOL_ERROR
  normalized_error: INVALID_ARGUMENT
  provider_http_status: 400
  provider_error_code: 400
  provider_error_domain: global
  provider_error_reason: invalid
  provider_error_location: pageToken
  provider_error_location_type: parameter
  provider_message: Invalid_Value
  returned_files: 0
  returned_next_page_token: false
  file_content_or_text_hydration_returned: false
  drive_write_side_effect_observed: false
  request_url_exposed_by_connector_error: true
  request_token_redacted_from_event: true
  raw_request_mapping_observed:
    topn_to_pageSize: 1_to_1_FOR_THIS_CALL
    query_keyword_mapping: NAME_OR_FULLTEXT_CONTAINS_QUERY
    item_type_document_mapping: MIME_TYPE_WHITELIST
    trashed_filter: false
    includeItemsFromAllDrives: true
    supportsAllDrives: true
    corpora: allDrives
    requested_fields_include:
      - nextPageToken
      - files_id_name_mimeType_size_createdTime_modifiedTime_viewedByMeTime_sharedWithMeTime_capabilities_webViewLink_parents_shared_driveId
    requested_fields_omit:
      - incompleteSearch
measured_fact:
  - SYNTHETIC_INVALID_PAGE_TOKEN_FAILED_CLOSED_WITH_HTTP_400_INVALID_ARGUMENT
  - PROVIDER_IDENTIFIED_PAGE_TOKEN_AS_THE_INVALID_PARAMETER
  - NO_RESULT_CONTENT_OR_DRIVE_MUTATION_OCCURRED
  - CONNECTOR_ERROR_SURFACE_EXPOSED_THE_REQUEST_URL_AND_THEREFORE_CAN_LEAK_OPAQUE_TOKENS_IN_LOGS
  - CONNECTOR_RAW_REQUEST_USED_CORPORA_ALLDRIVES_AND_SUPPORTS_ALL_DRIVES
  - CONNECTOR_RAW_FIELDS_OMITTED_INCOMPLETE_SEARCH
  - TOPN_1_MAPPED_TO_RAW_PAGESIZE_1_FOR_THIS_FAILURE_PATH
andon:
  severity: P1_GOVERNANCE_AND_OBSERVABILITY
  statement: CONNECTOR_ERROR_LOGS_EXPOSE_RAW_REQUEST_URLS_WHILE_COMPLETENESS_FIELD_INCOMPLETE_SEARCH_IS_NOT_REQUESTED
  consequence:
    - PAGE_TOKENS_MUST_BE_TREATED_AS_SENSITIVE_EPHEMERAL_CAPABILITIES_AND_REDACTED_FROM_LOGS
    - THIS_CONNECTOR_SURFACE_CANNOT_PROVE_SEARCH_COMPLETENESS_BECAUSE_INCOMPLETE_SEARCH_IS_OMITTED
    - DEFAULT_SEARCH_CORPUS_IS_BROADER_THAN_MY_DRIVE_ONLY_AND_INCLUDES_ALL_ACCESSIBLE_DRIVES
failure_behavior:
  fail_closed: true
  retry_same_request_admitted: false
  correct_action: DISCARD_REJECTED_TOKEN_AND_RESTART_FROM_FIRST_PAGE_OR_ABORT_BOUNDED_OPERATION
  authentication_or_permission_failure_tested: false
  quota_or_rate_limit_failure_tested: false
  transient_server_failure_tested: false
official_contract_checked_2026_08_02:
  files_list: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
  handle_errors: https://developers.google.com/workspace/drive/api/guides/handle-errors
  usage_limits: https://developers.google.com/workspace/drive/api/guides/limits
  pageToken_must_equal_prior_nextPageToken: true
  rejected_pageToken_should_be_discarded_and_pagination_restarted: true
  http_400_means_client_request_error: true
  files_list_quota_units_new_model: 100
  live_quota_model_and_actual_units: UNKNOWN
measurements:
  operator_relay_minutes: 0
  operator_minutes_removed_measured: 0
  operator_minutes_removed_estimate_per_bounded_discovery: 1_to_5_UNVALIDATED
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
  connector_invocations_this_phase: 1
  visible_provider_requests: AT_LEAST_1
  actual_upstream_request_count: UNKNOWN
  actual_quota_units_consumed: UNKNOWN
  actual_quota_class: UNKNOWN
  upstream_retry_count: UNKNOWN
  connector_latency_ms: NOT_EXPOSED
  custom_code_avoided_estimate:
    authenticated_list_query_and_metadata_normalization: 30_to_100_LOC_UNVALIDATED
    page_token_corpus_and_error_handling: 20_to_70_LOC_UNVALIDATED_NON_ADDITIVE
credentials:
  connector_authenticated_search_path_reached_provider: true
  operator_supplied_credentials: 0
  authenticated_user_identity: UNKNOWN
  live_oauth_scope: UNKNOWN
  oauth_client_or_project: UNKNOWN
  delegated_or_direct_drive_authority: UNKNOWN
  credential_custody: UNKNOWN
  least_privilege_closed: false
durability: EPHEMERAL_POINT_IN_TIME_METADATA_OBSERVATION_AND_PROVIDER_OWNED_PAGE_TOKENS_NOT_DURABLE_RECORDS
observability: MEDIUM_FOR_THIS_ERROR_PATH_BECAUSE_RAW_HTTP_STATUS_PARAMETER_LOCATION_REQUEST_URL_AND_PROVIDER_JSON_WERE_EXPOSED_BUT_LOW_FOR_IDENTITY_SCOPE_PROJECT_REQUEST_ID_QUOTA_RETRY_AND_SUCCESS_PATH_COMPLETENESS
portability: MEDIUM_LOW_GOOGLE_QUERY_CORPUS_MIME_PAGE_TOKEN_AND_ERROR_SEMANTICS_ARE_PROVIDER_SPECIFIC
mandatory_gates_added:
  - ACCEPT_PAGE_TOKEN_ONLY_FROM_THE_IMMEDIATELY_PRECEDING_ADMITTED_RESPONSE_FOR_THE_EXACT_QUERY_ITEM_TYPE_CORPUS_FIELDS_AND_ACCOUNT_CONTEXT
  - NEVER_SYNTHESIZE_PARSE_RECONSTRUCT_OR_REUSE_A_REJECTED_PAGE_TOKEN
  - ON_REJECTED_TOKEN_DISCARD_IT_AND_RESTART_FROM_FIRST_PAGE_OR_ABORT_DO_NOT_RETRY_UNCHANGED
  - REDACT_PAGE_TOKEN_AND_FULL_REQUEST_URL_FROM_GIT_SLACK_AND_ROUTINE_LOGS
  - TREAT_DEFAULT_CONNECTOR_SEARCH_AS_ALL_ACCESSIBLE_DRIVES_BECAUSE_RAW_REQUEST_USED_CORPORA_ALLDRIVES
  - DO_NOT_CLAIM_COMPLETENESS_BECAUSE_CONNECTOR_REQUEST_FIELDS_OMIT_INCOMPLETE_SEARCH
  - TREAT_TOPN_TO_RAW_PAGESIZE_MAPPING_AS_OBSERVED_FOR_THIS_CALL_NOT_A_GLOBAL_ABI_GUARANTEE
  - KEEP_BEST_EFFORT_FETCH_FALSE_AND_NO_CONTENT_OR_MUTATION
verifier: SOURCE_BOUND_RAW_GOOGLE_DRIVE_FILES_LIST_OR_DISTINCT_AUTHORIZED_CLIENT_WITH_IDENTICAL_QUERY_CORPUS_FIELDS_PAGE_SIZE_AND_ACCOUNT_CONTEXT
consumer:
  - HFO_BOUNDED_FILE_DISCOVERY
  - HFO_HERITAGE_AND_PARA_ROUTING_WITH_SEPARATE_CONTENT_AUTHORIZATION
strongest_falsifier: A_SOURCE_BOUND_RAW_OR_DISTINCT_CLIENT_SHOWS_MATERIAL_QUERY_CORPUS_PAGINATION_OR_ERROR_SEMANTICS_DIFFERENT_FROM_THE_CONNECTOR_FOR_THE_SAME_ACCOUNT_AND_REQUEST
honest_flaw: NO_VALID_NEXT_PAGE_TOKEN_TRAVERSAL_REAL_EXPIRED_TOKEN_QUERY_TOKEN_MISMATCH_401_403_429_5XX_IDENTITY_SCOPE_INDEPENDENT_READBACK_OR_CONSUMER_ACK
phase_3_result:
  disposition: PHASE3_ACCEPTED_WITH_TOKEN_REDACTION_CORPUS_COMPLETENESS_AND_CLIENT_ERROR_GATES
  rationale: INVALID_TOKEN_FAILED_CLOSED_AND_EXPOSED_USEFUL_PARAMETER_LEVEL_EVIDENCE_BUT_RAW_URL_LOGGING_CAN_LEAK_TOKENS_AND_THE_CONNECTOR_OMITS_INCOMPLETE_SEARCH_WHILE_DEFAULTING_TO_ALL_ACCESSIBLE_DRIVES
next_wake:
  phase: 4_of_4
  proposed_action: DECISION_ONLY_NO_ADDITIONAL_DRIVE_CAPABILITY_CALL
  likely_decision: ADOPT_WITH_GATES
---

# X13 Google Drive metadata search — phase 3

A single bounded metadata-only Drive search used a synthetic, non-provider-derived page token. The provider rejected the request with HTTP `400`; the connector normalized it as `INVALID_ARGUMENT`, and the provider error located the invalid value at the `pageToken` parameter. No files, continuation cursor, content hydration, or Drive mutation were returned or observed. The carrier did not retry.

The failure receipt exposed more than the success path: the connector included the raw request URL and provider JSON. That confirms `topn=1` mapped to `pageSize=1` for this call, the search used `corpora=allDrives` with all-drive support enabled, and the requested field mask omitted `incompleteSearch`. It also creates a security gate: opaque page tokens can appear in connector error logs, so full request URLs and tokens must be redacted before Git or Slack persistence.

Google's official contract says `pageToken` must come from the prior response's `nextPageToken`; if rejected, discard it and restart pagination from the first page. Google's error guide classifies HTTP 400 as a client-request failure that should be corrected, not blindly retried. The current quota documentation assigns `files.list` 100 units under the post–May 1, 2026 model, but the live project class, actual units, retries, and billing counters remain unknown.

Measured operator relief remains `0`; surfaced cost was `$0`. Phase 4 should make a decision only, with no additional Drive call.
