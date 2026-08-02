---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_DRIVE_BOUNDED_METADATA_SEARCH_READONLY_001
version: 48
prior_version: 47
candidate: Google_Drive_bounded_metadata_only_search_connector_surface
candidate_contract_reference: official_Google_Drive_files_list_pagination_error_scope_completeness_and_usage_limits_plus_direct_connector_receipts
campaign_wake: 4_of_4
campaign_status: COMPLETE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: true
phase_4_decision: ADOPT_WITH_GATES
last_event:
  commit: d05b443edf1a8ca6b508c69f1259d1b40456ed2d
  path: state/coordination/experiments/cots_connector_x13/20260802T204848Z_GOOGLE_DRIVE_METADATA_PHASE4_ADOPT_WITH_GATES.md
  blob_sha: 2abb8db4fd5294115d9715f5d81344f62c89f442
  exact_readback_completed: true
prior_current_commit: e16b2fe1746427514e310d8ef57a6c0c07478f52
prior_current_blob_sha: 345b3d091a64cccde0739126891499f2c61a661f
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: PHASE4_DECISION_ONLY_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_REDACTED_SLACK_DECISION
adoption_credit: 4
adoption_credit_basis:
  - OFFICIAL_PRIMARY_FILES_LIST_PAGINATION_ERROR_SCOPE_AND_QUOTA_CONTRACT
  - BOUNDED_METADATA_ONLY_PROVIDER_PAGE_BASELINE
  - BOUNDED_TOPN_1_RESULT_CAP_PROBE
  - SYNTHETIC_INVALID_PAGE_TOKEN_FAILED_CLOSED_WITH_PARAMETER_LEVEL_ERROR
  - DIRECT_RAW_REQUEST_MAPPING_FOR_CORPUS_PAGE_SIZE_FIELDS_AND_MIME_FILTER
  - PHASE4_DECISION_WITH_EXPLICIT_ADMITTED_SCOPE_AND_GATES
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_bounded_discovery: 1_to_5_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_list_query_and_metadata_normalization: 30_to_100_LOC_UNVALIDATED
  page_token_corpus_and_error_handling: 20_to_70_LOC_UNVALIDATED_NON_ADDITIVE
custom_policy_not_avoided:
  - ACCOUNT_IDENTITY_AND_AUTHORITY
  - LIVE_OAUTH_SCOPE_AND_LEAST_PRIVILEGE_VERIFICATION
  - QUERY_SCOPE_CORPUS_AND_SHARED_DRIVE_POLICY
  - METADATA_TOKEN_URL_REDACTION_AND_RETENTION
  - CONTENT_FETCH_SEPARATION_AND_AUTHORIZATION
  - PAGINATION_COMPLETENESS_PAGE_BUDGET_AND_CURSOR_BINDING
  - INCOMPLETE_SEARCH_HANDLING
  - ERROR_CLASSIFICATION_QUOTA_RETRY_AND_BACKOFF
  - INDEPENDENT_VERIFICATION
credentials:
  connector_authenticated_search_path_reached_provider: true
  operator_supplied_credentials: 0
  authenticated_user_identity: UNKNOWN
  live_oauth_scope: UNKNOWN
  oauth_client_or_project: UNKNOWN
  delegated_or_direct_drive_authority: UNKNOWN
  credential_custody: UNKNOWN
  least_privilege_closed: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
campaign_candidate_invocations:
  phase_1_bounded_metadata_search: 1
  phase_2_topn_1_result_cap_probe: 1
  phase_3_invalid_page_token_probe: 1
  phase_4_decision_only: 0
actual_upstream_request_count: UNKNOWN_AT_LEAST_ONE_PROVIDER_REQUEST_VISIBLE_IN_PHASE3
actual_quota_units_consumed: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
billing_counters: NOT_EXPOSED
live_request_id_retry_after_rate_limit_or_quota_headers: NOT_EXPOSED
direct_phase_1_receipt:
  query_value: HFO
  item_type: document
  topn: 3
  best_effort_fetch: false
  returned_result_count: 3
  next_page_token_visible: false
  content_hydration: false
  write_side_effect: false
direct_phase_2_receipt:
  query_value: HFO
  item_type: document
  topn: 1
  best_effort_fetch: false
  returned_result_count: 1
  next_page_token_visible: false
  content_hydration: false
  write_side_effect: false
direct_phase_3_receipt:
  query_value: HFO
  item_type: document
  topn: 1
  best_effort_fetch: false
  page_token_source: SYNTHETIC_NON_PROVIDER_TOKEN
  exact_token_persisted: false
  connector_result: INVALID_ARGUMENT
  provider_http_status: 400
  provider_error_reason: invalid
  provider_error_location: pageToken
  provider_error_location_type: parameter
  returned_result_count: 0
  returned_next_page_token: false
  content_hydration: false
  write_side_effect: false
  request_url_exposed_in_error: true
  observed_raw_request_mapping:
    topn_to_pageSize: 1_to_1_FOR_THIS_CALL
    query: NAME_OR_FULLTEXT_CONTAINS_HFO
    item_type_document: MIME_TYPE_WHITELIST
    trashed: false
    includeItemsFromAllDrives: true
    supportsAllDrives: true
    corpora: allDrives
    incompleteSearch_requested_in_fields: false
official_contract_checked_2026_08_02:
  files_list: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
  handle_errors: https://developers.google.com/workspace/drive/api/guides/handle-errors
  usage_limits: https://developers.google.com/workspace/drive/api/guides/limits
  endpoint: GET_/drive/v3/files
  pageSize_is_maximum_not_completeness_proof: true
  pageToken_must_come_from_prior_nextPageToken: true
  rejected_pageToken_should_be_discarded_and_listing_restarted: true
  pageToken_typically_valid_for_several_hours: true
  result_membership_can_change_when_items_added_or_removed: true
  incompleteSearch_true_means_results_might_be_missing: true
  http_400_is_client_request_error: true
  files_list_quota_units_new_model: 100
  published_new_model_per_minute_per_project_units: 1000000
  published_new_model_per_minute_per_user_per_project_units: 325000
  published_new_model_daily_billing_threshold_units: 400000000
  pre_May_1_2026_active_projects_may_retain_prior_quotas: true
  live_project_quota_model_and_billing_state: UNKNOWN
fresh_web_contract_retrieval_this_wake: SUCCESS_OFFICIAL_GOOGLE_PRIMARY_DOCS
failure_semantics:
  bounded_metadata_search: DIRECTLY_OBSERVED_SUCCESS
  topn_1_result_cap: DIRECTLY_OBSERVED_ONE_RESULT
  invalid_page_token: DIRECTLY_OBSERVED_HTTP_400_INVALID_ARGUMENT_LOCATION_PAGETOKEN
  invalid_page_token_retry: NOT_PERFORMED
  content_nonhydration: DIRECTLY_OBSERVED_FOR_ALL_THREE_CALLS
  result_completeness: NOT_PROVEN_AND_CONNECTOR_FIELDS_OMIT_INCOMPLETE_SEARCH
  connector_topn_mapping_to_raw_pageSize: OBSERVED_1_TO_1_FOR_PHASE3_FAILURE_PATH_ONLY
  connector_default_corpus: DIRECTLY_OBSERVED_ALLDRIVES_FOR_PHASE3_REQUEST
  valid_pagination: NOT_TESTED
  permission_denial: NOT_TESTED
  authentication_failure: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  transient_server_failure: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: EPHEMERAL_POINT_IN_TIME_METADATA_OBSERVATION_OVER_MUTABLE_DRIVE_AND_INDEX_STATE_PAGE_TOKENS_NOT_DURABLE_RECORDS
observability: MEDIUM_FOR_PHASE3_ERROR_PATH_RAW_STATUS_PARAMETER_LOCATION_REQUEST_URL_AND_PROVIDER_JSON_BUT_LOW_FOR_SUCCESS_PATH_COMPLETENESS_IDENTITY_SCOPE_PROJECT_REQUEST_ID_QUOTA_LATENCY_AND_UPSTREAM_RETRIES
portability: MEDIUM_LOW_OVERALL_DRIVE_QUERY_MIME_CORPUS_FILE_ID_PARENT_RESOURCE_KEY_AND_PAGE_TOKEN_SEMANTICS_ARE_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_METADATA_SEARCH
  - EXPLICIT_METADATA_ONLY_ITEM_TYPE
  - SMALL_EXPLICIT_TOPN
  - ONE_PROVIDER_PAGE
  - BEST_EFFORT_FETCH_FALSE
  - TIMESTAMPED_DISCOVERY_OBSERVATION_ONLY
  - SEPARATE_CONTENT_AUTHORIZATION_REQUIRED
excluded_scope:
  - BEST_EFFORT_TEXT_HYDRATION_OR_FILE_CONTENT_FETCH
  - DOCUMENT_OR_SPREADSHEET_CONTENT_READ
  - DOWNLOAD_EXPORT_OR_ATTACHMENT_READ
  - CREATE_UPDATE_DELETE_MOVE_RENAME_UPLOAD_OR_TRASH
  - SHARE_PERMISSION_OR_OWNERSHIP_CHANGE
  - BROAD_DRIVE_MINING
  - PAGE_TRAVERSAL_WITHOUT_A_LATER_BOUNDED_AND_TOKEN_BOUND_OPERATION
  - COMPLETENESS_OWNERSHIP_IDENTITY_SCOPE_OR_AUTHORITY_CLAIMS
mandatory_gates:
  - KEEP_BEST_EFFORT_FETCH_FALSE_AND_AN_EXPLICIT_METADATA_ONLY_ITEM_TYPE
  - USE_A_SMALL_EXPLICIT_TOPN_AND_TREAT_IT_AS_A_CONNECTOR_RESULT_CAP
  - ACCEPT_PAGE_TOKEN_ONLY_FROM_THE_IMMEDIATELY_PRECEDING_ADMITTED_RESPONSE_FOR_THE_EXACT_ACCOUNT_QUERY_ITEM_TYPE_CORPUS_FIELDS_AND_PAGE_CONTEXT
  - NEVER_SYNTHESIZE_PARSE_RECONSTRUCT_PERSIST_BY_DEFAULT_OR_REUSE_A_REJECTED_PAGE_TOKEN
  - ON_REJECTED_TOKEN_DISCARD_IT_AND_RESTART_FROM_FIRST_PAGE_OR_ABORT_DO_NOT_RETRY_UNCHANGED
  - REDACT_PAGE_TOKEN_AND_FULL_REQUEST_URL_FROM_GIT_SLACK_TRACES_AND_ROUTINE_LOGS
  - TREAT_DEFAULT_CONNECTOR_SEARCH_AS_ALL_ACCESSIBLE_DRIVES_BECAUSE_RAW_REQUEST_USED_CORPORA_ALLDRIVES
  - DO_NOT_CLAIM_COMPLETENESS_BECAUSE_CONNECTOR_REQUEST_FIELDS_OMIT_INCOMPLETE_SEARCH
  - TREAT_TOPN_TO_RAW_PAGESIZE_MAPPING_AS_OBSERVED_FOR_ONE_CALL_NOT_A_GLOBAL_ABI_GUARANTEE
  - TREAT_TITLES_IDS_URLS_PARENT_IDS_RESOURCE_KEYS_AND_FOLDER_RELATIONSHIPS_AS_SENSITIVE_METADATA
  - DO_NOT_INFER_ACCOUNT_IDENTITY_OAUTH_SCOPE_OWNERSHIP_WRITE_AUTHORITY_PROJECT_QUOTA_CLASS_BILLING_STATE_OR_CREDENTIAL_CUSTODY_FROM_SUCCESS
  - TREAT_RESULTS_ACROSS_WAKES_AS_MUTABLE_OBSERVATIONS_NOT_SNAPSHOTS
  - SEPARATE_CLIENT_INPUT_AUTHENTICATION_AUTHORIZATION_QUOTA_RATE_LIMIT_AND_TRANSIENT_SERVER_FAILURES
  - NO_CONTENT_HYDRATION_DOWNLOAD_EXPORT_ROW_READ_CREATE_UPDATE_MOVE_RENAME_UPLOAD_PERMISSION_SHARING_OWNERSHIP_TRASH_OR_DELETE
verifier: SOURCE_BOUND_RAW_GOOGLE_DRIVE_FILES_LIST_OR_DISTINCT_AUTHORIZED_CLIENT_WITH_IDENTICAL_ACCOUNT_QUERY_CORPUS_FIELDS_PAGE_SIZE_AND_COMPLETENESS_FIELDS
consumer:
  - HFO_BOUNDED_FILE_DISCOVERY
  - HFO_HERITAGE_AND_PARA_ROUTING_WITH_SEPARATE_CONTENT_AUTHORIZATION
strongest_falsifier: A_SOURCE_BOUND_RAW_OR_DISTINCT_CLIENT_SHOWS_MATERIAL_QUERY_MEMBERSHIP_CORPUS_PAGINATION_COMPLETENESS_OR_ERROR_SEMANTICS_DIFFERENT_FROM_THE_CONNECTOR_FOR_THE_SAME_ACCOUNT_AND_REQUEST
honest_flaw: NO_VALID_NEXT_PAGE_TRAVERSAL_REAL_EXPIRED_TOKEN_QUERY_TOKEN_MISMATCH_401_403_429_5XX_IDENTITY_SCOPE_INDEPENDENT_READBACK_OR_CONSUMER_ACK_SUCCESS_PATH_LATENCY_AND_LIVE_QUOTA_HIDDEN
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_SCOPE_CORPUS_COMPLETENESS_AND_QUOTA_GATES
phase_2_result:
  disposition: PHASE2_ACCEPTED_WITH_RESULT_CAP_AND_PAGINATION_VISIBILITY_GATES
phase_3_result:
  disposition: PHASE3_ACCEPTED_WITH_TOKEN_REDACTION_CORPUS_COMPLETENESS_AND_CLIENT_ERROR_GATES
phase_4_result:
  disposition: ADOPT_WITH_GATES
  rationale: THE_CONNECTOR_AVOIDS_CUSTOM_AUTHENTICATED_LISTING_AND_NORMALIZATION_FOR_NARROW_DISCOVERY_BUT_COMPLETENESS_IDENTITY_SCOPE_CONTENT_AUTHORIZATION_TOKEN_BINDING_REDACTION_AND_FAILURE_POLICY_REMAIN_EXTERNAL_GATES
next_wake:
  phase: 1_of_4
  experiment_id: X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001
  candidate: GitHub_Actions_bounded_workflow_run_status_readonly_surface
  proposed_action: OFFICIAL_CONTRACT_AND_ONE_BOUNDED_LATEST_RUN_METADATA_BASELINE
  exclusions:
    - WORKFLOW_DISPATCH
    - RERUN
    - CANCEL
    - ARTIFACT_DOWNLOAD
    - SECRET_READ
    - WORKFLOW_OR_BRANCH_MUTATION
review_expiry_utc: 2026-08-09T20:48:48Z
valid_time_utc: 2026-08-02T20:48:48Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
prior_campaign:
  experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
  final_version: 44
  decision: ADOPT_WITH_GATES
prior_prior_campaign:
  experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
  final_version: 40
  decision: ADOPT_WITH_GATES
---

# X13 current campaign

Google Drive bounded metadata-only search completed phase **4/4** with decision **`ADOPT_WITH_GATES`**.

Admitted use is narrow, bounded, read-only metadata discovery with `best_effort_fetch=false`, an explicit metadata item type, a small result cap, one provider page, and separate authorization before any content read.

The connector is not evidence of completeness, stable inventory, account identity, OAuth scope, ownership, write authority, quota class, or billing state. Direct evidence showed `corpora=allDrives`, omitted `incompleteSearch`, and exposed a raw provider request URL on the invalid-token error path; token and URL redaction are mandatory.

Measured operator relief remains `0`; surfaced cost was `$0`; fitness credit remains `0` pending source-bound ConsumerAck and measured operator outcome.

Next wake begins phase 1 for bounded read-only GitHub Actions workflow-run status metadata. No workflow mutation or execution control is admitted.
