---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_READONLY_CONNECTOR_001
candidate: Google_Drive_read_only_search_fetch_and_metadata_connector
phase: 1
phase_name: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
result: PHASE1_BASELINE_ACCEPTED
expected_prior_version: 20
next_version: 21
campaign_wake: 1_of_4
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
wip_limit: 1
effect_ceiling: READ_ONLY_SYNTHETIC_METADATA_SEARCH_NO_FILE_CONTENT_FETCH_NO_DRIVE_WRITE_NO_PRIVATE_BODY_PERSISTENCE
valid_time_utc: 2026-08-01T17:46:55Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true

self_probe:
  tools_observed:
    - native_automations_list_read
    - github_fetch_search_create_update_readback
    - google_drive_search
    - web_official_primary_documentation
    - slack_post_after_git_readback
  expected_task_id: 6a55c1733708819185088bf334e33ea5
  observed_task_id: 6a55c1733708819185088bf334e33ea5
  task_enabled: true

official_contract:
  files_list:
    source: https://developers.google.com/workspace/drive/api/guides/search-files
    checked_utc: 2026-08-01T17:46:55Z
    supported_claims:
      - files.list supports q filtering and provider-owned page tokens
      - fields can constrain returned metadata
      - documented default files.list file fields are kind_id_name_mimeType_resourceKey
      - files.get uses fileId and alt_media returns file contents
    excluded_claims:
      - connector_search_is_proven_to_issue_exactly_one_files.list_call
      - connector_fetch_is_proven_to_map_one_to_one_to_files.get
      - connector_metadata_search_is_proven_least_privilege
  oauth_scopes:
    source: https://developers.google.com/workspace/drive/api/guides/api-specific-auth
    checked_utc: 2026-08-01T17:46:55Z
    supported_claims:
      - drive.file is documented as a narrower non_sensitive per_file scope
      - drive.metadata.readonly and drive.readonly are documented restricted scopes
      - applications should request the narrowest scope suitable for the task
    live_connector_scope: UNKNOWN
    live_connector_identity: UNKNOWN
    token_type: UNKNOWN
    credential_custody: UNKNOWN
  quota_and_cost:
    source: https://developers.google.com/workspace/drive/api/guides/limits
    checked_utc: 2026-08-01T17:46:55Z
    new_model_effective_date: 2026-05-01
    grandfathering_possible_for_projects_used_2025_11_through_2026_04: true
    documented_limits:
      per_minute_per_project_quota_units: 1000000
      per_minute_per_user_per_project_quota_units: 325000
      per_day_per_project_egress: 1_TB
      daily_billing_threshold_quota_units: 400000000
      files_list_quota_units: 100
      files_get_read_quota_units: 5
      files_download_quota_units: 200
    standard_use_additional_cost: NONE_DOCUMENTED_BELOW_THRESHOLD
    connector_actual_project_class: UNKNOWN
    connector_request_count: NOT_EXPOSED
    connector_quota_units_consumed: NOT_EXPOSED
    connector_quota_headers: NOT_EXPOSED
    exact_cost_usd_observed: 0_NO_CHARGE_SURFACED

direct_probe:
  action: Google_Drive.search
  connector_action_name: search
  connector_id: connector_5f3c8c41a1e54ad7a76272c89e2554fa
  controlled_input:
    query: HFO_X13_SYNTHETIC_NONEXISTENT_20260801T174623Z
    item_type: document
    topn: 3
    best_effort_fetch: false
    require_viewed_by_user: false
  connector_contract_basis:
    - explicit_item_type_document_requests_one_metadata_only_provider_page
    - explicit_item_type_never_fetches_file_contents_even_if_best_effort_fetch_true
  measured_result:
    status: SUCCESS_EMPTY
    result_count: 0
    error: null
    external_call_time_ms: 350
    content_returned: false
    file_or_folder_identity_returned: false
    next_page_token_exposed: false
    login_or_operator_relay_required: false
  permission_class: AUTHENTICATED_READ_SURFACE_SCOPE_AND_IDENTITY_HIDDEN
  operator_relay_minutes: 0
  operator_minutes_removed_estimate: 0_PHASE1_BASELINE_ONLY

measurements:
  custom_code_avoided_estimate:
    bounded_query_and_metadata_normalization: 40_to_120_LOC_UNVALIDATED
    provider_pagination_plumbing: 20_to_80_LOC_UNVALIDATED
    authentication_and_token_refresh: MATERIAL_BUT_UNQUANTIFIED
    content_privacy_policy: NOT_AVOIDED_REQUIRES_HFO_GATE
    retry_and_rate_limit_policy: NOT_AVOIDED_REQUIRES_HFO_GATE
    additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
  durability: GOOGLE_DRIVE_PROVIDER_STORAGE_ONLY_NO_WORKFLOW_REPLAY_RESUME_TRANSACTION_OR_EXACTLY_ONCE_CLAIM
  observability: SUCCESS_PATH_EXPOSED_ACTION_CONNECTOR_ID_EMPTY_NORMALIZED_RESULT_AND_EXTERNAL_CALL_TIME_BUT_NOT_RAW_REQUEST_METHOD_FIELDS_SCOPE_IDENTITY_HEADERS_REQUEST_COUNT_QUOTA_UNITS_RETRIES_OR_INTERNAL_CALL_SEQUENCE
  portability: MEDIUM_FOR_GENERIC_FILE_SEARCH_METADATA_AND_PAGINATION_LOW_FOR_CONNECTOR_ITEM_TYPE_SCHEMA_WRAPPER_ERRORS_AND_GOOGLE_NATIVE_EXPORT_BEHAVIOR
  failure_behavior: NOT_YET_PROBED_PHASE3
  credentials: CONNECTOR_AUTHENTICATED_LIVE_IDENTITY_SCOPE_TOKEN_TYPE_STORAGE_AND_CUSTODY_UNKNOWN
  direct_cost_or_quota_evidence: NO_CHARGE_SURFACED_AND_NO_QUOTA_TELEMETRY_EXPOSED_OFFICIAL_FILES_LIST_UNIT_COST_CANNOT_BE_BOUND_TO_THIS_WRAPPER_CALL

privacy_externalization:
  drive_item_names_written_to_git_or_slack: false
  drive_item_ids_written_to_git_or_slack: false
  drive_urls_written_to_git_or_slack: false
  drive_file_bodies_written_to_git_or_slack: false
  owner_or_sharing_identity_written_to_git_or_slack: false
  synthetic_probe_contains_sensitive_data: false

provisional_gates:
  - DEFAULT_TO_EXPLICIT_ITEM_TYPE_METADATA_ONLY_SEARCH_FOR_DISCOVERY
  - SET_BEST_EFFORT_FETCH_FALSE_UNLESS_A_NAMED_CONSUMER_REQUIRES_CONTENT
  - REQUIRE_SHORT_SPECIFIC_QUERY_LOW_TOPN_AND_NAMED_OBLIGATION_OR_ARTIFACT
  - KEEP_FILE_NAMES_IDS_URLS_OWNERS_SHARING_IDENTITIES_AND_BODIES_IN_SOURCE_SYSTEMS_UNLESS_EXPLICITLY_REQUIRED
  - TREAT_FETCH_EXPORT_REVISION_AND_RAW_DOWNLOAD_AS_PRIVATE_BODY_SURFACES
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_WHILE_LIVE_SCOPE_IDENTITY_AND_CREDENTIAL_CUSTODY_ARE_HIDDEN
  - DO_NOT_CLAIM_ONE_WRAPPER_CALL_EQUALS_ONE_FILES_LIST_CALL_OR_100_QUOTA_UNITS
  - HANDLE_PROVIDER_PAGE_TOKENS_OPAQUELY_AND_BOUND_PAGINATION
  - NO_PROVIDER_DURABILITY_AS_WORKFLOW_DURABILITY_OR_EXACTLY_ONCE

strongest_falsifier: A_DISTINCT_TRACE_SHOWS_EXPLICIT_METADATA_ONLY_SEARCH_FETCHES_OR_HYDRATES_FILE_CONTENT_EXPOSES_PRIVATE_FIELDS_IGNORES_TOPN_OR_FANS_OUT_TO_MULTIPLE_UNBOUNDED_PROVIDER_CALLS_OR_THE_LIVE_CONNECTOR_USES_BROADER_SCOPE_THAN_NEEDED_WITHOUT_A_CONTAINMENT_GATE
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_FOR_PRIVACY_SCOPE_REQUEST_COUNT_AND_CONTENT_ISOLATION
consumer: S05_OPERATOR_RELIEF_CELL_AND_X11_CARRIER_SURFACE_LAB
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
fitness_credit: 0_PENDING_EXPLICIT_CONSUMER_ACK
honest_flaw: SYNTHETIC_EMPTY_SEARCH_PROVES_ONLY_THAT_ONE_BOUNDED_METADATA_MODE_CALL_RETURNED_EMPTY_WITHOUT_CONTENT_IT_DOES_NOT_VALIDATE_MATCHED_RESULT_FIELDS_PAGINATION_FETCH_EXPORT_SHARED_DRIVE_BEHAVIOR_PERMISSION_FAILURE_ACTUAL_OAUTH_SCOPE_OR_ONE_TO_ONE_API_MAPPING
review_expiry_utc: 2026-08-08T17:46:55Z
next_phase: PHASE2_SMALLEST_HARMLESS_READ_ONLY_MICRO_USE_ON_ONE_ALREADY_EXTERNALIZED_NAMED_ARTIFACT_METADATA_ONLY_FIRST_AND_FETCH_ONLY_IF_REQUIRED
---

# X13 Google Drive read-only connector — phase 1

The official Drive contract and one direct connector baseline were admitted. A synthetic, metadata-only document search returned an empty success in 350 ms without file content or identity-bearing results. This is evidence for a bounded discovery surface, not evidence of least privilege, exact provider-call count, content isolation on matched results, or workflow durability.

The live OAuth identity, scope, token type, credential custody, request count, quota-unit consumption, retry behavior, headers, and internal call sequence remain hidden. The official Drive quota model is recorded for scale planning, but it cannot be assigned directly to this wrapper call without lower-level telemetry.

Phase 2 should use one already-externalized named artifact, search metadata first, and fetch content only when a named consumer needs a specific field that metadata cannot provide.
