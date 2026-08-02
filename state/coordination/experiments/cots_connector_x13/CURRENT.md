---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_DRIVE_BOUNDED_METADATA_SEARCH_READONLY_001
version: 46
prior_version: 45
candidate: Google_Drive_bounded_metadata_only_search_connector_surface
candidate_contract_reference: official_Google_Drive_files_list_search_query_scope_pagination_completeness_and_usage_limits_plus_direct_connector_receipt
campaign_wake: 2_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_completed: false
phase_4_decision: null
last_event:
  commit: 32cbbd3bf1500c81438cd3dfd512401b2c3001c5
  path: state/coordination/experiments/cots_connector_x13/20260802T184954Z_GOOGLE_DRIVE_METADATA_PHASE2_CAP_AND_CURSOR_ANDON.md
  blob_sha: 5eee0d4b40b8552dd00ae9686b4073621b246206
  exact_readback_completed: true
prior_current_commit: 62e76314cf592a3d44e89dcab5818a9ce29a8b42
prior_current_blob_sha: 116e3f09b505bdff10a635e095a1671ab8aa1072
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUN_CONTEXT
effect_ceiling: ONE_BOUNDED_METADATA_ONLY_RESULT_CAP_PROBE_GIT_EVENT_CURRENT_ADVANCE_READBACK_AND_ONE_SHORT_NON_SECRET_SLACK_MEASURED_ANDON
adoption_credit: 2
adoption_credit_basis:
  - OFFICIAL_PRIMARY_FILES_LIST_SEARCH_QUERY_SCOPE_PAGINATION_COMPLETENESS_AND_QUOTA_CONTRACT
  - ONE_BOUNDED_METADATA_ONLY_PROVIDER_PAGE_BASELINE
  - ONE_BOUNDED_TOPN_1_RESULT_CAP_PROBE
  - BEST_EFFORT_FETCH_FALSE_AND_EXPLICIT_DOCUMENT_ITEM_TYPE
  - NO_FILE_CONTENT_HYDRATION_OR_DRIVE_WRITE_SIDE_EFFECT
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
  - METADATA_REDACTION_AND_RETENTION
  - CONTENT_FETCH_SEPARATION_AND_AUTHORIZATION
  - PAGINATION_COMPLETENESS_PAGE_BUDGET_AND_CURSOR_BINDING
  - INCOMPLETE_SEARCH_HANDLING
  - ERROR_CLASSIFICATION_QUOTA_RETRY_AND_BACKOFF
  - INDEPENDENT_VERIFICATION
credentials:
  connector_authenticated_search_succeeded: true
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
actual_upstream_request_count: UNKNOWN
actual_quota_units_consumed: UNKNOWN
actual_quota_class: UNKNOWN
retry_count: 0_AT_CARRIER_LEVEL_UPSTREAM_UNKNOWN
billing_counters: NOT_EXPOSED
live_HTTP_status_headers_request_id_retry_after_or_rate_limit_headers: NOT_EXPOSED
direct_phase_1_receipt:
  query_class: short_specific_keyword
  query_value: HFO
  item_type: document
  topn: 3
  provider_page_count: 1
  best_effort_fetch: false
  require_viewed_by_user: false
  page_token_supplied: false
  returned_result_count: 3
  next_page_token_visible: false
  exact_result_metadata_persisted_in_event: false
  file_content_or_text_hydration_returned: false
  connector_latency_ms: NOT_EXPOSED
  top_level_error: null
  write_side_effect: false
direct_phase_2_receipt:
  query_class: same_short_specific_keyword_as_phase_1
  query_value: HFO
  item_type: document
  topn: 1
  provider_page_count: 1
  best_effort_fetch: false
  require_viewed_by_user: false
  page_token_supplied: false
  returned_result_count: 1
  next_page_token_visible: false
  exact_result_metadata_persisted_in_event: false
  file_content_or_text_hydration_returned: false
  connector_latency_ms: NOT_EXPOSED
  top_level_error: null
  write_side_effect: false
official_contract_checked_2026_08_02:
  files_list: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
  search_files: https://developers.google.com/workspace/drive/api/guides/search-files
  query_terms: https://developers.google.com/workspace/drive/api/guides/ref-search-terms
  usage_limits: https://developers.google.com/workspace/drive/api/guides/limits
  endpoint: GET_/drive/v3/files
  pageSize_service_may_return_fewer: true
  pageToken_must_come_from_prior_nextPageToken: true
  rejected_pageToken_should_be_discarded_and_listing_restarted: true
  pageToken_typically_valid_for_several_hours: true
  result_membership_can_change_when_items_added_or_removed: true
  incompleteSearch_true_means_results_might_be_missing: true
  default_fields_are_metadata_not_content: true
  multiple_authorization_scopes_supported: true
  successful_call_proves_exact_scope: false
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
  content_nonhydration: DIRECTLY_OBSERVED_FOR_BOTH_CALLS
  result_completeness: NOT_PROVEN
  connector_token_visibility: NO_TOKEN_VISIBLE_IN_PHASE_1_OR_PHASE_2
  connector_topn_mapping_to_raw_pageSize: NOT_PROVEN
  incompleteSearch_visibility: NOT_EXPOSED
  valid_pagination: NOT_TESTED
  invalid_page_token: NOT_TESTED
  permission_denial: NOT_TESTED
  authentication_failure: NOT_TESTED
  quota_or_rate_limit: NOT_TESTED
  transient_server_failure: NOT_TESTED
  independent_cross_client_readback: NOT_TESTED
durability: EPHEMERAL_POINT_IN_TIME_METADATA_OBSERVATION_OVER_MUTABLE_DRIVE_AND_INDEX_STATE_PAGE_TOKENS_NOT_DURABLE_RECORDS
observability: MEDIUM_LOW_FOR_RESULT_METADATA_COUNT_AND_SUCCESS_BUT_LOW_FOR_RAW_HTTP_TOKEN_SUPPRESSION_CORPUS_INCOMPLETE_SEARCH_IDENTITY_SCOPE_PROJECT_REQUEST_ID_QUOTA_LATENCY_AND_UPSTREAM_RETRIES
portability: MEDIUM_LOW_OVERALL_DRIVE_QUERY_SYNTAX_FILE_IDS_PARENT_IDS_RESOURCE_KEYS_SHARED_DRIVE_SEMANTICS_AND_PAGE_TOKENS_ARE_PROVIDER_SPECIFIC
admitted_scope:
  - BOUNDED_READ_ONLY_METADATA_SEARCH
  - EXPLICIT_DOCUMENT_ITEM_TYPE
  - SMALL_TOPN
  - ONE_PROVIDER_PAGE
  - BEST_EFFORT_FETCH_FALSE
  - NO_CONTENT_READ_OR_DRIVE_MUTATION
excluded_scope:
  - BEST_EFFORT_TEXT_HYDRATION_OR_FILE_CONTENT_FETCH
  - DOCUMENT_OR_SPREADSHEET_CONTENT_READ
  - DOWNLOAD_EXPORT_OR_ATTACHMENT_READ
  - CREATE_UPDATE_DELETE_MOVE_RENAME_UPLOAD_OR_TRASH
  - SHARE_PERMISSION_OR_OWNERSHIP_CHANGE
  - BROAD_DRIVE_MINING
  - PAGE_TRAVERSAL_WITHOUT_A_LATER_BOUNDED_PHASE
  - COMPLETENESS_OWNERSHIP_OR_IDENTITY_CLAIMS
mandatory_gates:
  - KEEP_BEST_EFFORT_FETCH_FALSE_AND_AN_EXPLICIT_METADATA_ONLY_ITEM_TYPE
  - USE_A_SMALL_EXPLICIT_TOPN_AND_TREAT_IT_AS_A_CONNECTOR_RESULT_CAP_UNTIL_RAW_PAGE_SIZE_MAPPING_IS_PROVEN
  - TREAT_ONE_CONNECTOR_PAGE_AS_INCOMPLETE_UNLESS RAW_NEXT_PAGE_TOKEN_AND_INCOMPLETE_SEARCH_EVIDENCE_PROVE_OTHERWISE
  - TREAT_TITLES_IDS_URLS_PARENT_IDS_RESOURCE_KEYS_AND_FOLDER_RELATIONSHIPS_AS_SENSITIVE_METADATA
  - DO_NOT_PERSIST_EXACT_RESULT_METADATA_OR_TOKEN_VALUES_WITHOUT_CONSUMER_NEED_AND_RETENTION_JUSTIFICATION
  - DO_NOT_INFER_ACCOUNT_IDENTITY_OAUTH_SCOPE_OWNERSHIP_WRITE_AUTHORITY_CORPUS_SHARED_DRIVE_COVERAGE_OR_BILLING_STATE_FROM_SUCCESS
  - TREAT_ABSENT_CONNECTOR_VISIBLE_NEXT_PAGE_TOKEN_ONLY_AS_A_PROPERTY_OF_THIS_NORMALIZED_RESPONSE_NOT_RAW_API_COMPLETENESS_PROOF
  - REQUIRE_INCOMPLETE_SEARCH_VISIBILITY_OR_EQUIVALENT EVIDENCE_BEFORE_COMPLETENESS_CLAIMS
  - TREAT_RESULTS_ACROSS_WAKES_AS_MUTABLE_OBSERVATIONS_NOT_SNAPSHOTS
  - NO_CONTENT_HYDRATION_DOWNLOAD_EXPORT_ROW_READ_CREATE_UPDATE_MOVE_RENAME_UPLOAD_PERMISSION_SHARING_OWNERSHIP_TRASH_OR_DELETE
verifier: RAW_GOOGLE_DRIVE_FILES_LIST_OR_DISTINCT_AUTHORIZED_CLIENT_WITH_SOURCE_BOUND_ACCOUNT_EXACT_QUERY_FIELDS_CORPUS_PAGE_SIZE_AND_COMPLETENESS_FIELDS
consumer:
  - HFO_BOUNDED_FILE_DISCOVERY
  - HFO_HERITAGE_AND_PARA_ROUTING_WITH_SEPARATE_CONTENT_AUTHORIZATION
strongest_falsifier: A_SOURCE_BOUND_RAW_CLIENT_RETURNS_A_CONTINUATION_TOKEN_OR_MATERIALLY_DIFFERENT_MEMBERSHIP_FOR_THE_SAME_QUERY_WHILE_THE_CONNECTOR_OMITS_OR_ALTERS_THAT_STATE
honest_flaw: NO_SAME_INSTANT_RAW_API_COMPARISON_VALID_PAGINATION_INCOMPLETE_SEARCH_SHARED_DRIVE_CORPUS_IDENTITY_SCOPE_ERROR_PROBE_INDEPENDENT_READBACK_OR_CONSUMER_ACK
phase_1_result:
  disposition: PHASE1_ACCEPTED_WITH_SCOPE_CORPUS_COMPLETENESS_AND_QUOTA_GATES
  rationale: BOUNDED_METADATA_DISCOVERY_SUCCEEDED_WITHOUT_CONTENT_OR_MUTATION_BUT_SCOPE_CORPUS_COMPLETENESS_IDENTITY_QUOTA_AND_RAW_TELEMETRY_REMAIN_UNPROVEN
phase_2_result:
  disposition: PHASE2_ACCEPTED_WITH_RESULT_CAP_AND_PAGINATION_VISIBILITY_GATES
  rationale: TOPN_1_RETURNED_ONE_METADATA_RECORD_WITHOUT_CONTENT_OR_MUTATION_BUT_NO_CONNECTOR_VISIBLE_CURSOR_AND_NO_RAW_COMPLETENESS_FIELDS_LEAVE_PAGINATION_UNPROVEN
next_wake:
  phase: 3_of_4
  proposed_probe: ONE_SYNTHETIC_NON_DRIVE_DERIVED_INVALID_PAGE_TOKEN_WITH_THE_SAME_BOUNDED_METADATA_ONLY_QUERY
  constraints:
    - DO_NOT_RETRY
    - DO_NOT_PERSIST_TOKEN_OR_RESULT_METADATA
    - BEST_EFFORT_FETCH_FALSE
    - NO_CONTENT_OR_MUTATION
    - CAPTURE_NORMALIZED_ERROR_WITHOUT_ATTRIBUTING_UNEXPOSED_RAW_HTTP_DETAILS
review_expiry_utc: 2026-08-09T18:49:54Z
valid_time_utc: 2026-08-02T18:49:54Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
prior_campaign:
  experiment_id: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
  final_version: 44
  decision: ADOPT_WITH_GATES
  decision_event_commit: 67c3888c73e0fce9214af9512fa33fabfc9feaee
  current_commit: 2eec8a439cd793dd1b25913263a595071c287dbb
prior_prior_campaign:
  experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
  final_version: 40
  decision: ADOPT_WITH_GATES
---

# X13 current campaign

Google Drive bounded metadata-only search completed phase **2/4**.

The repeated keyword search with `item_type=document`, `topn=1`, and `best_effort_fetch=false` returned one metadata record and no visible continuation token. No file content, text hydration, download, export, or Drive mutation was requested or observed. Exact result metadata and token values were not persisted.

The connector respected the result cap, but pagination completeness is not established. Phase 1 returned three records for the same keyword with `topn=3`; phase 2 returned one with no visible cursor. Drive membership can change between wakes, and connector `topn` is not proven to equal raw API `pageSize`, so the discrepancy is an Andon rather than proof of token suppression.

Measured operator relief remains `0`; surfaced cost was `$0`. Identity, OAuth scope, project, corpus, shared-drive coverage, `incompleteSearch`, raw HTTP, quota counters, retries, and connector latency remain hidden.

Next wake performs one invalid-page-token failure probe without retry, content hydration, metadata persistence, or Drive mutation.
