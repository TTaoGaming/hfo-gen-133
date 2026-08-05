---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_SEARCH_READONLY_002
event_id: X13_GOOGLE_DRIVE_SEARCH_METADATA_PHASE4_ADOPT_WITH_GATES_20260805T084801Z
event_type: PHASE4_DECISION
phase: 4_of_4
phase_4_decision: ADOPT_WITH_GATES
disposition: ADOPT_WITH_GATES_BOUNDED_READONLY_HUMAN_REVIEWED_NONOPERATIONAL
campaign_status: CLOSED
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 107
candidate: Google_Drive_search_metadata_only_document_surface
effect_ceiling: BOUNDED_READONLY_HUMAN_REVIEWED_METADATA_DISCOVERY
phase_4_additional_candidate_calls: 0
source_events:
  phase_1:
    path: state/coordination/experiments/cots_connector_x13/20260805T054953Z_GOOGLE_DRIVE_SEARCH_METADATA_PHASE1_ACCEPTED_WITH_GATES.md
    blob_sha: 36450fa813aa57205df11c65011ec9cbbfa03e30
  phase_2:
    path: state/coordination/experiments/cots_connector_x13/20260805T064903Z_GOOGLE_DRIVE_SEARCH_METADATA_PHASE2_EMPTY_RESULT_MICROUSE.md
    blob_sha: 9a0cd3f04a64345b55aee9c7e45be5cc277f91d5
  phase_3:
    path: state/coordination/experiments/cots_connector_x13/20260805T074708Z_GOOGLE_DRIVE_SEARCH_METADATA_PHASE3_INVALID_PAGE_TOKEN_FAILURE_PROBE.md
    blob_sha: 7e79d6b6e78b20f3ac3974c931e8be6ba7c927ea
campaign_measurements:
  readonly_calls: 3
  connector_level_successes: 2
  expected_permanent_client_failures: 1
  positive_metadata_results: 1
  normal_empty_results: 1
  invalid_page_token_failures: 1
  content_hydrations: 0
  caller_retries: 0
  caller_fallbacks: 0
  secondary_reads: 0
  candidate_mutations: 0
  phase_2_external_call_time_ms: 1219
  phase_1_and_phase_3_latency: NOT_EXPOSED
  operator_minutes_removed_measured: 0
  operator_minutes_removed_estimate: NOT_CLAIMED
  custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
credentials:
  operator_supplied_across_campaign: 0
  authenticated_principal: UNKNOWN
  effective_oauth_scope: UNKNOWN
  connector_managed: true
  least_privilege_proven: false
durability:
  provider_metadata: PROVIDER_STORED
  workflow_replay_resume_transaction_exactly_once: NOT_PROVIDED
  durable_receipts: FOUR_IMMUTABLE_GIT_EVENTS_PLUS_VERSIONED_CURRENT
observability:
  exposed:
    - TRANSFORMED_POINTER_METADATA_URL_TITLE_STABLE_ITEM_ID_PARENT_IDS
    - NORMAL_EMPTY_RESULT_ARRAY
    - PROVIDER_HTTP_400_AND_STRUCTURED_INVALID_PAGE_TOKEN_ERROR
    - FULL_PROVIDER_REQUEST_URL_ON_ERROR
    - PHASE_2_EXTERNAL_CALL_TIME
  not_exposed:
    - AUTHENTICATED_IDENTITY_AND_EFFECTIVE_SCOPE
    - RAW_CORPUS_FIELD_MASK_AND_INCOMPLETE_SEARCH
    - HTTP_HEADERS_AND_PROVIDER_REQUEST_ID
    - QUOTA_DEBIT_AND_REMAINING_LIMITS
    - HIDDEN_PAGINATION_RETRY_AND_ATTEMPT_GRAPH
    - CONNECTOR_TO_RAW_PROVIDER_PARITY
    - PHASE_1_AND_PHASE_3_LATENCY
portability:
  metadata_search_and_opaque_ids: MEDIUM
  empty_result_and_invalid_cursor_semantics: MEDIUM
  query_translation_mime_filters_corpus_parent_ids_url_token_and_error_shape: GOOGLE_AND_CONNECTOR_SPECIFIC
failure_behavior:
  observed:
    - POSITIVE_SUCCESS
    - NORMAL_EMPTY_SUCCESS
    - FAIL_CLOSED_HTTP_400_INVALID_PAGE_TOKEN_WITH_NO_RESULTS
  material_hazard: ERROR_SURFACE_ECHOED_QUERY_AND_PAGE_TOKEN_IN_FULL_PROVIDER_REQUEST_URL
  not_observed:
    - VALID_EXPIRED_OR_QUERY_MISMATCHED_PAGE_TOKEN
    - AUTHENTICATION_OR_PERMISSION_DENIAL
    - RATE_LIMIT_OR_TRANSIENT_FAILURE
    - HIDDEN_RETRY_OR_FALLBACK
direct_cost_and_quota_evidence:
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
  actual_quota_consumed: UNKNOWN
  provider_billing_or_quota_receipt: ABSENT
  official_contract_url: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
  official_search_guide_url: https://developers.google.com/workspace/drive/api/guides/search-files
  official_error_url: https://developers.google.com/workspace/drive/api/guides/handle-errors
  official_quota_url: https://developers.google.com/workspace/drive/api/guides/limits
  inherited_documented_files_list_cost: 100_QUOTA_UNITS_UNDER_POST_2026_05_01_MODEL_WITH_GRANDFATHERING_POSSIBLE
verifier:
  required: DISTINCT_AUTHORIZED_SAME_PRINCIPAL_RAW_DRIVE_FILES_LIST_WITNESS_FOR_EQUIVALENT_QUERY_AND_VALID_PAGINATION_WITH_SAFE_REQUEST_RESPONSE_DIGEST_HTTP_STATUS_REQUEST_ID_SCOPE_CORPUS_INCOMPLETE_SEARCH_AND_QUOTA_FIELDS
  assigned: false
  completed: false
  result: NOT_RUN
consumer:
  named_catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
  operational_consumer: NOT_ASSIGNED
  consumer_ack: NOT_OBSERVED
  adoption_credit: 0
  fitness_credit: 0
strongest_falsifier: SAME_PRINCIPAL_RAW_FILES_LIST_DISAGREES_ON_RESULT_SET_EMPTY_RESULT_OR_INVALID_TOKEN_BEHAVIOR_OR_SHOWS_INCOMPLETE_SEARCH_TRUE_CONTENT_FETCH_HIDDEN_PAGINATION_UNBOUNDED_RETRIES_OR_CONNECTOR_SCOPE_BROADER_THAN_REQUIRED
mandatory_gates:
  - USE_SHORT_SPECIFIC_QUERIES_LOW_TOPN_EXPLICIT_ITEM_TYPE_AND_BEST_EFFORT_FETCH_FALSE
  - TREAT_FILE_METADATA_SEARCH_QUERIES_URLS_IDS_PARENT_IDS_TITLES_AND_PAGE_TOKENS_AS_SENSITIVE
  - DO_NOT_PERSIST_RAW_POINTER_METADATA_WITHOUT_A_NAMED_CONSUMER_AND_MINIMUM_NECESSARY_NEED
  - NEVER_TREAT_EMPTY_RESULTS_AS_AUTHORITATIVE_ABSENCE_WITHOUT_CORPUS_INCOMPLETE_SEARCH_VALID_PAGINATION_IDENTITY_SCOPE_AND_RAW_PARITY_EVIDENCE
  - USE_ONLY_NEXT_PAGE_TOKEN_FROM_THE_IMMEDIATELY_PRECEDING_COMPATIBLE_REQUEST
  - NEVER_RETRY_A_REJECTED_PAGE_TOKEN_UNCHANGED
  - FAIL_CLOSED_ON_CONNECTOR_ERRORS_AND_NEVER_INTERPRET_ZERO_RESULTS_DURING_ERROR_AS_ABSENCE
  - SANITIZE_QUERY_STRINGS_PAGE_TOKENS_AND_PROVIDER_REQUEST_URLS_FROM_LOGS_GIT_SLACK_AND_EXCEPTION_AGGREGATION
  - DO_NOT_INFER_CONTENT_IDENTITY_FRESHNESS_UNIQUENESS_CANONICALITY_ORDER_COMPLETENESS_OR_LEAST_PRIVILEGE
  - KEEP_USE_BOUNDED_READONLY_HUMAN_REVIEWED_AND_NONOPERATIONAL
  - REQUIRE_SAME_PRINCIPAL_RAW_PARITY_VALID_PAGINATION_IDENTITY_SCOPE_CORPUS_INCOMPLETE_SEARCH_QUOTA_CONSUMER_ACK_AND_MEASURED_OPERATOR_VALUE_BEFORE_UNATTENDED_USE_OR_OPERATIONAL_CREDIT
adopted_boundary:
  allowed:
    - BOUNDED_READONLY_HUMAN_REVIEWED_METADATA_DISCOVERY
    - LOW_ASSURANCE_CATALOG_AND_OPERATOR_ASSISTANCE
  forbidden:
    - AUTHORITATIVE_ABSENCE_OR_COMPLETENESS_CLAIMS
    - UNATTENDED_FILE_SELECTION_ROUTING_OR_DELETION
    - CONTENT_HYDRATION_WITHOUT_SEPARATE_CAMPAIGN_AND_NAMED_CONSUMER
    - DURABLE_STORAGE_OF_RAW_POINTERS_QUERIES_OR_TOKENS_WITHOUT_MINIMUM_NECESSARY_NEED
    - AUTOMATIC_RETRY_OR_PAGINATION_WITHOUT_COMPATIBLE_CURSOR_PROVENANCE_AND_BOUNDED_POLICY
    - OPERATIONAL_ADOPTION_OR_FITNESS_CREDIT
honest_flaw: THE_CAMPAIGN USED_ONE_POSITIVE_TOPN_ONE_QUERY_ONE_UNREPRODUCIBLE_SYNTHETIC_EMPTY_QUERY_AND_ONE_SYNTHETIC_PERMANENT_CLIENT_ERROR; IDENTITY_SCOPE_RAW_PROVIDER_PARITY_VALID_PAGINATION_INCOMPLETE_SEARCH_REAL_PERMISSION_DENIAL_RATE_LIMIT_TRANSIENT_FAILURE_HIDDEN_CALLS_ACTUAL_QUOTA_OPERATOR_TIME_SAVED_AND_CONSUMER_VALUE_REMAIN_UNVERIFIED
next_campaign:
  candidate: GitHub_fetch_file_readonly_contents_surface
  experiment_id: X13_GITHUB_FETCH_FILE_READONLY_003
  next_phase: 1_of_4
  action_this_wake: NONE
review_expiry_utc: 2026-08-12T08:48:01Z
valid_time_utc: 2026-08-05T08:48:01Z
recorded_time_utc: 2026-08-05T08:48:01Z
---

# X13 Google Drive metadata search phase 4 decision

Decision: `ADOPT_WITH_GATES` for bounded, read-only, human-reviewed metadata discovery only. Across three calls, the connector returned one positive metadata result, one normal empty result, and one fail-closed invalid-page-token error without hydrating file content. The material hazard is that the provider request URL surfaced in the error and echoed both the query and page token, so queries, tokens, and provider URLs must be sanitized before any durable logging or messaging.

The connector avoided direct OAuth handling, request construction, metadata mapping, and basic pagination plumbing, estimated at 40-120 lines of custom code, but that estimate is unvalidated. It removed zero measured operator minutes and has no raw-provider witness, principal or scope proof, valid-pagination evidence, `incompleteSearch` visibility, quota receipt, operational consumer acknowledgment, or measured value. No operational adoption or fitness credit is awarded.
