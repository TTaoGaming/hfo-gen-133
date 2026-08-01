---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_READONLY_CONNECTOR_001
event_id: X13_DRIVE_PHASE3_20260801T194640Z
phase: 3
campaign_wake: 3_of_4
result: PHASE3_ACCEPTED_WITH_PAGINATION_RESET_GATE_AND_INCOMPLETE_SEARCH_ANDON
expected_current_version: 22
next_current_version: 23
prior_current_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
prior_current_blob_sha: 148d35924bbd734040a12d5896acc2537eb9dc2a
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
candidate: Google_Drive_read_only_search_fetch_and_metadata_connector
probe: SYNTHETIC_INVALID_PAGE_TOKEN_ON_BOUNDED_METADATA_ONLY_DOCUMENT_SEARCH
effect_ceiling: READ_ONLY_SYNTHETIC_FAILURE_PROBE_NO_CONTENT_FETCH_NO_DRIVE_WRITE_NO_PRIVATE_BODY_PERSISTENCE
valid_time_utc: 2026-08-01T19:46:40Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
review_expiry_utc: 2026-08-08T19:46:40Z
direct_connector_probe:
  action: Google_Drive.search
  query_class: SYNTHETIC_NONEXISTENT_NON_SENSITIVE
  query: hfo-x13-synthetic-nonexistent-20260801
  item_type: document
  topn: 1
  best_effort_fetch: false
  require_viewed_by_user: false
  page_token_class: SYNTHETIC_INVALID
  page_token_sha256: b8373b700b3dc879a7596415adf45beb8d9b943c37afc79004a3418a1a176138
  result: TOOL_ERROR_INVALID_ARGUMENT
  normalized_error_code: INVALID_ARGUMENT
  upstream_http_status: 400
  upstream_error_domain: global
  upstream_error_reason: invalid
  upstream_error_location: pageToken
  upstream_error_location_type: parameter
  upstream_message: Invalid_Value
  result_count: 0
  file_content_returned: false
  identity_bearing_result_returned: false
  retry_observed: false
  latency_ms: NOT_EXPOSED
  quota_headers_or_units: NOT_EXPOSED
provider_request_facts_exposed_by_error_surface:
  provider_api: GOOGLE_DRIVE_V3
  provider_method: GET_FILES_LIST
  endpoint: https://www.googleapis.com/drive/v3/files
  query_translation: NAME_CONTAINS_OR_FULLTEXT_CONTAINS_PLUS_DOCUMENT_MIME_ALLOWLIST_PLUS_TRASHED_FALSE
  page_size: 1
  corpora: allDrives
  include_items_from_all_drives: true
  supports_all_drives: true
  fields_mask:
    - nextPageToken
    - files.id
    - files.name
    - files.mimeType
    - files.size
    - files.createdTime
    - files.modifiedTime
    - files.viewedByMeTime
    - files.sharedWithMeTime
    - files.capabilities
    - files.webViewLink
    - files.parents
    - files.shared
    - files.driveId
  incompleteSearch_requested: false
  raw_request_url_echoed_by_connector_error: true
  raw_request_url_persisted_to_git_or_slack: false
  request_url_sha256: 95bcc15a390869513ac8a3b1175993ee16089aa2467dd8a98d4389ae51b471cd
privacy_externalization: SYNTHETIC_QUERY_ONLY_NO_RAW_DRIVE_FILE_FOLDER_OWNER_SHARING_OR_PRIVATE_BODY_DATA_WRITTEN_TO_GIT_OR_SLACK
measured_facts:
  - INVALID_PAGE_TOKEN_FAILS_CLOSED_WITH_HTTP_400_AND_NO_RESULTS_OR_CONTENT
  - CONNECTOR_ERROR_SURFACE_ECHOES_THE_RAW_PROVIDER_REQUEST_URL_AND_QUERY_PARAMETERS
  - EXPLICIT_DOCUMENT_MODE_MAPS_TO_ONE_FILES_LIST_REQUEST_WITH_CORPORA_ALLDRIVES_AND_A_BROAD_DOCUMENT_MIME_ALLOWLIST_IN_THIS_FAILURE_TRACE
  - RESPONSE_FIELDS_MASK_OMITS_INCOMPLETESEARCH_WHILE_CORPORA_IS_ALLDRIVES
failure_interpretation:
  invalid_page_token: CLIENT_SIDE_CURSOR_FAILURE_NOT_PERMISSION_DENIAL_NOT_GLOBAL_ABSENCE
  permission_state: NOT_TESTED
  content_state: NO_CONTENT_RETURNED
  safe_recovery: DISCARD_REJECTED_TOKEN_AND_RESTART_FROM_FIRST_PAGE_AT_MOST_ONCE_FOR_THE_SAME_BOUNDED_QUERY_WITH_ID_DEDUPLICATION
  unsafe_recovery:
    - BLIND_OR_UNBOUNDED_RETRY
    - PRESERVING_A_REJECTED_TOKEN
    - CALLING_EMPTY_RESULTS_AFTER_RESTART_GLOBAL_ABSENCE
    - CLAIMING_COMPLETE_ALLDRIVES_SEARCH_WHILE_INCOMPLETESEARCH_IS_NOT_EXPOSED
official_contract_facts_checked_2026_08_01:
  drive_400_means_client_request_error: true
  files_list_rejected_page_token_should_be_discarded_and_pagination_restarted_from_first_page: true
  files_list_page_tokens_are_typically_valid_FOR_SEVERAL_HOURS: true
  files_list_results_may_change_when_items_are_added_or_removed: true
  allDrives_search_can_return_incompleteSearch_true_when_not_all_corpora_were_searched: true
  official_files_list_reference: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
  official_search_guide: https://developers.google.com/workspace/drive/api/guides/search-files
  official_error_guide: https://developers.google.com/workspace/drive/api/guides/handle-errors
new_or_tightened_gates:
  - TREAT_INVALID_PAGE_TOKEN_AS_A_TYPED_CURSOR_FAILURE_NOT_PERMISSION_DENIAL_OR ABSENCE
  - DISCARD_A_REJECTED_PAGE_TOKEN_AND_RESTART_FROM_PAGE_ONE_AT_MOST_ONCE_FOR_THE_SAME_BOUNDED_QUERY
  - DEDUPLICATE_RESTARTED_RESULTS_BY_STABLE_FILE_ID_WITHOUT_PERSISTING_RAW_IDS_OUTSIDE_THE_PRIVATE_SOURCE_BOUNDARY
  - DO_NOT_BLINDLY_RETRY_HTTP_400_INVALID_ARGUMENT
  - SANITIZE_CONNECTOR_ERRORS_BECAUSE_THE_RAW_PROVIDER_REQUEST_URL_CAN_ECHO_QUERY_TERMS_AND_FILTERS
  - DO_NOT_CLAIM_COMPLETE_OR_GLOBAL_DRIVE_SEARCH_WHILE_USING_ALLDRIVES_IF_INCOMPLETESEARCH_IS_NOT_EXPOSED
  - PREFER_USER_OR_ONE_NAMED_DRIVE_CORPUS_WHEN_THE_CONTRACT_ALLOWS_IT_AND_COMPLETE_SEARCH MATTERS
  - KEEP_BEST_EFFORT_FETCH_FALSE_FOR_FAILURE_AND_PAGINATION_PROBES
accepted_scope_delta:
  - TYPED_INVALID_CURSOR_FAILURE_CAN_BE_HANDLED_WITHOUT_CONTENT_FETCH_OR_OPERATOR LOGIN
  - ERROR_TRACE_CAN_VERIFY_PROVIDER_METHOD_QUERY_TRANSLATION_FIELDS_MASK_AND_CORPUS FOR_A_SYNTHETIC_PROBE
excluded_claims:
  - NATURALLY_EXPIRED_TOKEN_BEHAVIOR
  - VALID_SECOND_PAGE_BEHAVIOR_OR_RESULT_DEDUPLICATION
  - PERMISSION_401_403_OR_404_BEHAVIOR
  - RATE_LIMIT_429_OR_SERVER_RETRY_BEHAVIOR
  - COMPLETE_ALLDRIVES_SEARCH
  - ONE_WRAPPER_CALL_ALWAYS_EQUALS_ONE_PROVIDER_REQUEST
  - LEAST_PRIVILEGE_SCOPE_OR_CREDENTIAL_CUSTODY
  - PROVIDER_DURABILITY_AS_WORKFLOW_DURABILITY
operator_relay_minutes: 0
operator_minutes_removed_estimate: 1_to_3_UNVALIDATED
custom_code_avoided_estimate:
  provider_error_parsing_and_normalization: 20_to_60_LOC_UNVALIDATED
  page_token_plumbing: 20_to_60_LOC_UNVALIDATED
  safe_restart_deduplication_and_privacy_redaction: NOT_AVOIDED_REQUIRES_HFO_GATE
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
credentials:
  connector_authenticated: true
  operator_supplied_credentials_this_wake: 0
  live_identity: UNKNOWN
  live_oauth_scope: UNKNOWN
  token_type: UNKNOWN
  credential_custody: UNKNOWN
durability: GOOGLE_DRIVE_PROVIDER_STORAGE_AND_STABLE_FILE_ID_ONLY_NO_WORKFLOW_REPLAY_RESUME_TRANSACTION_OR_EXACTLY_ONCE_CLAIM
observability: FAILURE_TRACE_EXPOSED_PROVIDER_METHOD_FULL_QUERY_TRANSLATION_FIELDS_MASK_CORPUS_PAGE_SIZE_AND_ERROR_LOCATION_BUT_HID_SCOPE_IDENTITY_HEADERS_QUOTA_RETRIES_LATENCY_AND_INTERNAL_WRAPPER_CONTROL_FLOW
portability: MEDIUM_FOR_STANDARD_HTTP_400_AND_OPAQUE_PAGE_TOKEN_HANDLING_LOW_TO_MEDIUM_FOR_WRAPPER_ITEM_TYPE_QUERY_TRANSLATION_ALLDRIVES_DEFAULT_AND_ERROR_SHAPE
failure_behavior: FAIL_CLOSED_HTTP_400_INVALID_ARGUMENT_NO_RESULTS_NO_CONTENT_NO_OBSERVED_RETRY
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_connector_request_count: ONE_PROVIDER_REQUEST_VISIBLE_IN_THIS_ERROR_TRACE_BUT_WRAPPER_INTERNAL_PRE_OR_POST_CALLS_NOT_PROVEN_ABSENT
direct_connector_quota_units: NOT_EXPOSED
actual_project_quota_class: UNKNOWN
adoption_credit: 3
adoption_credit_basis: OFFICIAL_PRIMARY_CONTRACT_PLUS_EMPTY_BASELINE_PLUS_EXACT_NAME_METADATA_MICRO_USE_PLUS_ONE_SYNTHETIC_INVALID_CURSOR_FAILURE_TRACE
fitness_credit: 0_PENDING_EXPLICIT_CONSUMER_ACK
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_FOR_ERROR_REDACTION_RESTART_DEDUPLICATION_CORPUS_AND_INCOMPLETESEARCH_COVERAGE
consumer: S05_OPERATOR_RELIEF_CELL_AND_X11_CARRIER_SURFACE_LAB
strongest_falsifier: A_DISTINCT_VALID_PAGINATION_TRACE_SHOWS_THE_WRAPPER_EXPOSES_INCOMPLETESEARCH_OR_USES_A_BOUNDED_USER_OR_NAMED_DRIVE_CORPUS_OR_REDACTS_RAW_QUERY_TERMS_OR_SILENTLY_RETRIES_INVALID_TOKENS_WITHOUT_DUPLICATION_AND_WITH_REQUEST_COUNT_TELEMETRY
honest_flaw: THIS_WAS_AN_INTENTIONALLY_INVALID_SYNTHETIC_TOKEN_NOT_A_NATURALLY_EXPIRED_TOKEN_AND_IT_DID_NOT_TEST_VALID_PAGINATION_PERMISSION_FAILURE_RATE_LIMITS_RETRY_TIMING_DUPLICATE_SUPPRESSION_OR_AN_ACTUAL_INCOMPLETESEARCH_RESPONSE
next_phase: PHASE4_ADOPT_ADOPT_WITH_GATES_DEFER_REJECT_OR_UNKNOWN_DECISION
sealed: true
---

# X13 Google Drive read-only phase 3

A synthetic invalid page token produced a typed `INVALID_ARGUMENT` / HTTP 400 failure at the `pageToken` parameter. The call failed closed: no file result, identity-bearing metadata, or content was returned, and no retry was observed.

The error trace materially improved observability. It exposed that this wrapper invocation mapped to Drive v3 `files.list`, used `corpora=allDrives`, enabled shared-drive support, translated document mode into a broad MIME allowlist, and requested a metadata field mask. It also exposed two gates that were previously hidden.

First, the connector error echoed the full provider request URL. A private search term could therefore spill into logs or receipts unless error output is sanitized. This probe used only a synthetic term, and the raw URL was not persisted.

Second, the field mask omitted `incompleteSearch` while querying `allDrives`. Google documents that `allDrives` searches can be incomplete. Therefore an empty or partial wrapper result cannot support a global-absence or complete-search claim unless the connector exposes `incompleteSearch` or the query is narrowed to a corpus whose completeness can be evaluated.

Safe handling is to discard a rejected page token, restart the same bounded query from page one at most once, deduplicate privately by stable file ID, and never blindly retry a 400. This transition incurred no operator relay, Drive write, content fetch, send, spend, account change, task mutation, deployment, merge, publication, or secret use.
