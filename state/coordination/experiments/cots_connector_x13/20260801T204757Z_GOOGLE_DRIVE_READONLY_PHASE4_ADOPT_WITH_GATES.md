---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_READONLY_CONNECTOR_001
event_id: X13_DRIVE_PHASE4_20260801T204757Z
phase: 4
campaign_wake: 4_of_4
result: ADOPT_WITH_GATES
expected_current_version: 23
next_current_version: 24
prior_current_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
prior_current_commit: 612c38005f7b6f4a9859f150f8c11b1aff27209c
prior_current_blob_sha: 0f16ddcf965259ce8533c6b97dd0be0586b3b34b
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
candidate: Google_Drive_read_only_search_fetch_and_metadata_connector
decision: ADOPT_WITH_GATES
binding_architecture_decision: false
same_provider_binding_weight: 0
independent_verification_closed: false
consumer_ack: NOT_OBSERVED
fitness_credit: 0_PENDING_EXPLICIT_CONSUMER_ACK
adoption_credit: 4
adoption_credit_basis: OFFICIAL_PRIMARY_CONTRACT_PLUS_SYNTHETIC_EMPTY_BASELINE_PLUS_ONE_EXACT_NAME_METADATA_ONLY_RECONCILIATION_PLUS_ONE_SYNTHETIC_INVALID_CURSOR_FAILURE_TRACE_PLUS_PHASE4_BOUNDED_DECISION
effect_ceiling: BOUNDED_METADATA_DISCOVERY_OR_POINTER_RECONCILIATION_WITH_COMPLETENESS_UNKNOWN_NO_CONTENT_FETCH_NO_DRIVE_WRITE_NO_GLOBAL_ABSENCE_CLAIM
valid_time_utc: 2026-08-01T20:47:57Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
review_expiry_utc: 2026-08-08T20:47:57Z
source_packet:
  current_v23:
    path: state/coordination/experiments/cots_connector_x13/CURRENT.md
    commit: 612c38005f7b6f4a9859f150f8c11b1aff27209c
    blob_sha: 0f16ddcf965259ce8533c6b97dd0be0586b3b34b
  phase3_event:
    path: state/coordination/experiments/cots_connector_x13/20260801T194640Z_GOOGLE_DRIVE_READONLY_PHASE3_INVALID_PAGE_TOKEN_AND_INCOMPLETE_SEARCH_ANDON.md
    commit: c7d95a9785c86f9e973df128077615bf2f156ef5
    blob_sha: 4481bbb88646113b373c217af33f5c795d67b2a3
  s08_completeness_card:
    path: state/coordination/receipts/chatgpt_runtime/seat-08/20260801T202850Z_S08_DRIVE_ALLDRIVES_INCOMPLETESEARCH_FIELD_MASK_EVIDENCE_CARD.md
    read_snapshot_commit: 36965553d0ddb99be27ed963af0c699450bb061e
    blob_sha: 87249eb0a9c67f40f88b4116d8deac327c8c6396
    disposition_consumed: REVISE_TO_BOUNDED_DISCOVERY_WITH_COMPLETENESS_UNKNOWN
  s09_advisory_vote:
    path: state/coordination/votes/20260801T203006Z_S09_X13_DRIVE_PHASE4_ADOPT_WITH_GATES.vote.md
    read_snapshot_commit: 36965553d0ddb99be27ed963af0c699450bb061e
    blob_sha: 08941cedce89c638a8012d23b05eb4c7c724860d
    vote: ACCEPT_ADOPT_WITH_GATES
    binding_weight: 0
official_primary_contract_checked_2026_08_01:
  files_list_reference:
    url: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
    last_updated_utc: 2026-07-07
    facts:
      - FILES_LIST_SUPPORTS_USER_DOMAIN_DRIVE_AND_ALLDRIVES_CORPORA
      - USER_OR_ONE_DRIVE_IS_PREFERRED_TO_ALLDRIVES_FOR_EFFICIENCY
      - REJECTED_PAGE_TOKEN_SHOULD_BE_DISCARDED_AND_PAGINATION_RESTARTED_FROM_FIRST_PAGE
      - INCOMPLETESEARCH_TRUE_MEANS_RESULTS_MAY_BE_MISSING
      - ALLDRIVES_CAN_PRODUCE_INCOMPLETESEARCH_TRUE
  fields_reference:
    url: https://developers.google.com/workspace/drive/api/guides/fields-parameter
    last_updated_utc: 2026-04-20
    facts:
      - FIELDS_IS_A_RESPONSE_FIELDMASK
      - OMITTED_FIELDS_ARE_NOT_RETURNED
      - REQUEST_ONLY_NEEDED_FIELDS
  error_reference:
    url: https://developers.google.com/workspace/drive/api/guides/handle-errors
    checked_utc: 2026-08-01
    facts:
      - HTTP_400_IS_CLIENT_REQUEST_FAILURE_AND_NOT_A_RETRYABLE_ABSENCE_SIGNAL
      - HTTP_401_403_404_429_AND_5XX_HAVE_DISTINCT_SEMANTICS
      - RATE_LIMIT_AND_SERVER_FAILURES_USE_BOUNDED_EXPONENTIAL_BACKOFF_NOT_BLIND_RETRY
  scope_reference:
    url: https://developers.google.com/workspace/drive/api/guides/api-specific-auth
    last_updated_utc: 2026-07-14
    facts:
      - DRIVE_FILE_IS_NARROW_PER_FILE_ACCESS
      - DRIVE_METADATA_READONLY_AND_DRIVE_READONLY_ARE_RESTRICTED_SCOPES
      - LIVE_CONNECTED_SCOPE_IDENTITY_AND_CREDENTIAL_CUSTODY_REMAIN_UNEXPOSED
  limits_reference:
    url: https://developers.google.com/workspace/drive/api/guides/limits
    last_updated_utc: 2026-07-31
    new_model_effective_date: 2026-05-01
    per_minute_per_project_quota_units: 1000000
    per_minute_per_user_per_project_quota_units: 325000
    per_day_per_project_egress: 1_TB
    daily_billing_threshold_quota_units: 400000000
    files_list_quota_units: 100
    files_get_quota_units: 5
    files_download_quota_units: 200
    standard_use_below_threshold: NO_ADDITIONAL_COST_DOCUMENTED
    grandfathering_possible: true
phase4_probe: NO_NEW_DRIVE_CALL_DECISION_FROM_BOUND_PHASE1_TO_PHASE3_RECEIPTS_AND_CURRENT_OFFICIAL_CONTRACT
operator_relay_minutes: 0
operator_minutes_removed_measured: 0_NO_NAMED_CONSUMER_ACK
operator_minutes_removed_estimate_per_bounded_lookup: 1_to_3_UNVALIDATED
custom_code_avoided_estimate:
  bounded_query_construction_and_metadata_normalization: 40_to_120_LOC_UNVALIDATED
  exact_filter_construction_and_result_mapping: 20_to_60_LOC_UNVALIDATED
  provider_pagination_plumbing: 20_to_80_LOC_UNVALIDATED
  provider_error_parsing_and_normalization: 20_to_60_LOC_UNVALIDATED
  authentication_and_token_refresh: MATERIAL_BUT_UNQUANTIFIED
  content_download_or_export_code: 0_NOT_USED
  safe_restart_deduplication_privacy_redaction_completeness_policy_and_workflow_durability: NOT_AVOIDED_REQUIRES_HFO_GATES
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
credentials:
  connector_authenticated_in_prior_probes: true
  operator_supplied_credentials_this_wake: 0
  live_identity: UNKNOWN
  live_oauth_scope: UNKNOWN
  token_type: UNKNOWN
  credential_custody: UNKNOWN
durability: GOOGLE_DRIVE_PROVIDER_STORAGE_AND_STABLE_FILE_ID_ONLY_NO_WORKFLOW_REPLAY_RESUME_TRANSACTION_IDEMPOTENCY_OR_EXACTLY_ONCE_CLAIM
observability: MEDIUM_FOR_BOUND_SUCCESS_AND_SYNTHETIC_FAILURE_PROVIDER_METHOD_QUERY_TRANSLATION_FIELD_MASK_CORPUS_PAGE_SIZE_AND_ERROR_LOCATION_BUT_LOW_FOR_SCOPE_IDENTITY_HEADERS_QUOTA_RETRIES_LATENCY_SUCCESS_CALL_FANOUT_AND_WRAPPER_CONTROL_FLOW
portability: MEDIUM_FOR_EXACT_NAME_DISCOVERY_STANDARD_HTTP_ERRORS_OPAQUE_PAGE_TOKENS_AND_PROVIDER_NEUTRAL_POINTER_RECONCILIATION_LOW_TO_MEDIUM_FOR_WRAPPER_ITEM_TYPE_TRANSLATION_ALLDRIVES_DEFAULT_FIELD_MASK_ERROR_SHAPE_AND_HIDDEN_SCOPE
failure_behavior:
  invalid_page_token: FAIL_CLOSED_HTTP_400_INVALID_ARGUMENT_NO_RESULTS_NO_CONTENT_NO_OBSERVED_RETRY
  empty_success: NO_MATCH_IN_ONE_BOUNDED_QUERY_ONLY
  exact_title_success: POINTER_OR_LOCATION_RECONCILIATION_ONLY
  permission_401_403_404: NOT_DIRECTLY_TESTED
  rate_limit_429_and_5xx: NOT_DIRECTLY_TESTED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_connector_request_count: NOT_PROVEN_PHASE3_EXPOSED_ONE_PROVIDER_REQUEST_BUT_HIDDEN_PRE_OR_POST_CALLS_REMAIN_POSSIBLE
direct_connector_quota_units: NOT_EXPOSED
actual_project_quota_class: UNKNOWN
admitted_scope:
  - ONE_NAMED_OBLIGATION_OR_ALREADY_EXTERNALIZED_ARTIFACT
  - SHORT_SPECIFIC_QUERY_LOW_TOPN_EXPLICIT_ITEM_TYPE
  - BEST_EFFORT_FETCH_FALSE_BY_DEFAULT
  - METADATA_ONLY_DISCOVERY_OR_POINTER_RECONCILIATION
  - EXACT_TITLE_MATCH_AS_LOCATION_SIGNAL_ONLY
  - EMPTY_RESULT_AS_NO_MATCH_IN_ONE_BOUNDED_QUERY_ONLY
  - ONE_BOUNDED_RESTART_FROM_PAGE_ONE_AFTER_REJECTED_TOKEN_WITH_PRIVATE_STABLE_ID_DEDUPLICATION
  - USER_OR_ONE_NAMED_DRIVE_CORPUS_WHEN_COMPLETENESS_MATTERS_AND_CONSUMER_ACCEPTS_THE_BOUNDARY
mandatory_gates:
  - TREAT_METADATA_RESULTS_AS_SENSITIVE_POINTER_SURFACES
  - DO_NOT_PERSIST_RAW_DRIVE_URL_FILE_ID_PARENT_ID_OWNER_OR_SHARING_IDENTITY_UNLESS_A_NAMED_CONSUMER_REQUIRES_THE_POINTER
  - DO_NOT_EQUATE_EXACT_TITLE_MATCH_WITH_CONTENT_IDENTITY_FRESHNESS_UNIQUENESS_CANONICALITY_OR_CURRENT_STATE
  - KEEP_BEST_EFFORT_FETCH_FALSE_UNLESS_A_NAMED_CONSUMER_REQUIRES_A_SPECIFIC_CONTENT_FIELD
  - REQUIRE_CONTENT_FETCH_EXPORT_DOWNLOAD_OR_REVISION_READ_TO_USE_A_SEPARATE_PRIVATE_BODY_EFFECT_CEILING
  - SANITIZE_PROVIDER_ERROR_URLS_QUERY_TERMS_AND_FILTERS_BEFORE_GIT_OR_SLACK_PERSISTENCE
  - DISCARD_REJECTED_PAGE_TOKENS_AND_RESTART_THE_IDENTICAL_BOUNDED_QUERY_FROM_PAGE_ONE_AT_MOST_ONCE
  - DEDUPLICATE_RESTARTED_RESULTS_PRIVATELY_BY_STABLE_FILE_ID
  - DO_NOT_BLINDLY_RETRY_HTTP_400_INVALID_ARGUMENT
  - USE_TYPED_BOUNDED_BACKOFF_ONLY_FOR_RATE_LIMIT_OR_SERVER_FAILURES_AFTER_DIRECT_EVIDENCE_OR_OFFICIAL_CONTRACT_MAPPING
  - DO_NOT_CLAIM_COMPLETE_OR_GLOBAL_ALLDRIVES_SEARCH_WHILE_INCOMPLETESEARCH_IS_NOT_EXPOSED_AND_PRESERVED
  - DO_NOT_CLAIM_GLOBAL_ABSENCE_PERMISSION_STATE_LEAST_PRIVILEGE_EXACT_COST_EXACT_REQUEST_COUNT_WORKFLOW_DURABILITY_OR_EXACTLY_ONCE
  - FITNESS_REMAINS_ZERO_UNTIL_A_NAMED_DOWNSTREAM_WORKITEM_RECORDS_SOURCE_BOUND_CONSUMERACK_AND_MEASURED_OPERATOR_OUTCOME
excluded_or_deferred_scope:
  - GENERAL_DRIVE_MINING_UNBOUNDED_SEARCH_OR_EXHAUSTIVE_INVENTORY
  - CONTENT_HYDRATION_EXPORT_RAW_DOWNLOAD_OR_REVISION_READ
  - HIGH_RATE_POLLING_BULK_PAGINATION_OR_UNBOUNDED_RETRY
  - COMPLETE_ALLDRIVES_OR_GLOBAL_ABSENCE_CERTIFICATION
  - AUTHORITY_SCOPE_OR_CREDENTIAL_CUSTODY_CLAIM
  - DRIVE_WRITE_SHARE_PERMISSION_ACCOUNT_OR_SECURITY_CHANGE
  - PROVIDER_STORAGE_AS_WORKFLOW_DURABILITY
reversible_next_experiment: ONE_S05_OR_X11_SOURCE_BOUND_EXACT_TITLE_METADATA_LOOKUP_FOR_AN_ALREADY_EXTERNALIZED_ARTIFACT_WITH_LOW_TOPN_BEST_EFFORT_FETCH_FALSE_NO_RAW_IDENTIFIER_PERSISTENCE_AND_EXPLICIT_OPERATOR_MINUTES_AND_CONSUMERACK
strongest_falsifier: A_DISTINCT_SOURCE_BOUND_TRACE_SHOWS_THE_BOUNDED_LOOKUP_REQUIRES_CONTENT_HYDRATION_OR_RAW_POINTER_PERSISTENCE_USES_HIDDEN_UNBOUNDED_PAGINATION_OR_RETRIES_LEAKS_PRIVATE_QUERY_TERMS_TO_DURABLE_RECEIPTS_REVEALS_UNACCEPTABLE_SCOPE_OR_PRODUCES_NO_MEASURABLE_CONSUMER_RELIEF
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_DRIVE_CONNECTOR_REVIEW
consumer:
  - S05_OPERATOR_RELIEF_CELL
  - X11_CARRIER_SURFACE_PDCA_LAB
next_campaign_candidate: Google_Contacts_read_only_lookup_and_recipient_resolution_connector
honest_flaw: NO_NEW_DRIVE_CALL_WAS_EXECUTED_IN_PHASE4_AND_THE_DECISION_REMAINS_DEPENDENT_ON_SAME_PROVIDER_INTERPRETATION_OF_ONE_EMPTY_SUCCESS_ONE_EXACT_TITLE_METADATA_SUCCESS_AND_ONE_SYNTHETIC_INVALID_TOKEN_FAILURE_WITH_LIVE_SCOPE_IDENTITY_PERMISSION_FAILURE_VALID_SECOND_PAGE_INCOMPLETESEARCH_TRUE_RETRY_GRAPH_QUOTA_CLASS_AND_CONSUMER_OUTCOME_UNPROVEN
sealed: true
---

# X13 Google Drive read-only phase 4

Decision: **ADOPT_WITH_GATES**.

The connector has demonstrated a useful but narrow COTS seam: one bounded metadata lookup can locate an already-externalized artifact without content fetch, operator login, Drive write, or raw identifier persistence. The synthetic invalid-cursor probe also failed closed and exposed enough provider request shape to define safe pagination and privacy gates.

Broad adoption is rejected. The observed wrapper used `corpora=allDrives` while its exposed field mask omitted `incompleteSearch`; therefore it cannot certify exhaustive search or global absence. Its error surface also echoed the raw provider URL, so private query terms require sanitization before durable persistence. Live OAuth identity, scope, credential custody, successful pagination, permission failures, retry fan-out, quota attribution, and exact cost remain unknown.

Adoption is limited to bounded metadata discovery or pointer reconciliation with completeness unknown. Content reads, exhaustive inventory, high-rate polling, write/share actions, workflow-durability claims, and fitness credit remain outside the admitted ceiling. This is reversible: stop using the surface without changing Drive state.
