---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13-GCAL-RO-001-P4-20260801T164756Z
experiment_id: X13_GOOGLE_CALENDAR_READONLY_CONNECTOR_001
phase: 4
phase_name: ADOPTION_DECISION
campaign_wake: 4_of_4
expected_prior_version: 19
next_version: 20
candidate: Calendar_read_only_event_search_and_free_busy_connector
carrier: X13_COTS_AND_CONNECTOR_PDCA_LAB
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_blob_sha: a1a9ccc3ee5deaf139977470d4aa181abb271f84
wip: 1
valid_time_utc: 2026-08-01T16:47:56Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
evidence_class:
  - DIRECT_GOOGLE_CALENDAR_CONNECTOR_RECEIPTS_PHASE1_PHASE2_PHASE3
  - OFFICIAL_GOOGLE_CALENDAR_API_DOCUMENTATION_CHECKED_2026_08_01
  - SAME_PROVIDER_NONBINDING_ADVISORY
binding_weight: 0
binding_architecture_decision: false
effect_ceiling: PHASE4_DECISION_ONLY_NO_NEW_CALENDAR_READ_NO_CALENDAR_WRITE
self_probe:
  exposed_tools:
    - native_automations_inventory_read
    - GitHub_fetch_search_create_update
    - Slack_read_write_surface_available
    - web_official_document_research
    - Google_Calendar_connector_available_but_not_called_in_phase4
  expected_task_id_match: true
source_bindings:
  phase1:
    commit: d9d13734a133c06258bb324118ac6e2b66a7b224
    path: state/coordination/experiments/cots_connector_x13/20260801T134733Z_GOOGLE_CALENDAR_READONLY_PHASE1_BASELINE.md
    blob_sha: fc4fdb3484e9b931d561886f7dd984cdf3a63e3a
    commit_path_verified: true
  phase2:
    commit: c19740bcef8f8453ce9bd3f746b5e3e5be3927fe
    path: state/coordination/experiments/cots_connector_x13/20260801T145120Z_GOOGLE_CALENDAR_READONLY_PHASE2_REED_RECONCILIATION.md
    blob_sha: d9ef5c8804b31c50466dfa890f4b340574ca8044
    commit_path_verified: true
  phase3:
    commit: 836afef4db0523ca917e54f93f0a554a4060e9e1
    path: state/coordination/experiments/cots_connector_x13/20260801T154924Z_GOOGLE_CALENDAR_READONLY_PHASE3_INACCESSIBLE_CALENDAR_404_VARIANCE.md
    blob_sha: 311daaa0b6bcfafd13c4defdeae6eba3287656a4
    commit_path_verified: true
official_contract_sources:
  scopes:
    url: "https://developers.google.com/workspace/calendar/api/auth"
    checked_utc: 2026-08-01
    finding: GOOGLE_RECOMMENDS_THE_NARROWEST_PRACTICAL_SCOPE_AND_DOCUMENTS_DISTINCT_CALENDAR_FREEBUSY_EVENTS_FREEBUSY_EVENTS_READONLY_AND_CALENDAR_READONLY_SCOPES
  freebusy_query:
    url: "https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query"
    checked_utc: 2026-08-01
    finding: FREEBUSY_RETURNS_BUSY_INTERVALS_AND_PER_CALENDAR_ERRORS_WITH_CALENDAR_EXPANSION_MAX_50_AND_SUPPORTS_NARROW_FREEBUSY_SCOPES
  events_list:
    url: "https://developers.google.com/workspace/calendar/api/v3/reference/events/list"
    checked_utc: 2026-08-01
    finding: EVENTS_LIST_RETURNS_EVENT_RESOURCES_AND_PAGINATION_TOKENS_SO_EVENT_SEARCH_IS_A_PRIVATE_BODY_CAPABLE_SURFACE_NOT_METADATA_ONLY
  errors:
    url: "https://developers.google.com/workspace/calendar/api/guides/errors"
    checked_utc: 2026-08-01
    last_updated_utc: 2026-07-16
    finding: RATE_LIMIT_ERRORS_CAN_APPEAR_AS_403_OR_429_AND_RETRYABLE_RATE_OR_SERVER_ERRORS_REQUIRE_EXPONENTIAL_BACKOFF; PHASE3_CONFIRMED_CONNECTOR_404_NORMALIZATION_ONLY
  quota:
    url: "https://developers.google.com/workspace/calendar/api/guides/quota"
    checked_utc: 2026-08-01
    finding: NEW_MODEL_DOCUMENTS_10000_REQUESTS_PER_MINUTE_PER_PROJECT_600_PER_MINUTE_PER_USER_PER_PROJECT_AND_1000000_DAILY_BILLING_THRESHOLD_BUT_PRE_MAY_2026_PROJECTS_MAY_RETAIN_PREVIOUS_QUOTAS
measured_campaign_summary:
  phase1_synthetic_event_search:
    result: SUCCESS_EMPTY
    external_call_time_ms: 191
    max_results: 5
    private_event_body_returned: false
  phase1_primary_freebusy:
    result: SUCCESS
    external_call_time_ms: 155
    exact_busy_intervals_externalized: false
    calendar_error: null
  phase2_known_obligation_search:
    result: SUCCESS_ONE_MATCH
    external_call_time_ms: 364
    event_id_digest_matched_prior_receipt: true
    privacy_behavior: FULL_DESCRIPTION_AND_IDENTITY_BEARING_FIELDS_RETURNED_WHEN_ONLY_METADATA_WAS_NEEDED
    private_body_persisted_to_git_or_slack: false
  phase2_exact_event_readback:
    result: SUCCESS
    event_id_digest_matched_prior_receipt: true
    external_call_time_ms: NOT_EXPOSED
  phase3_invalid_calendar_selector:
    result: EXPECTED_ERROR_NO_EVENT_DATA
    wrapper_error_class: NOT_FOUND
    upstream_http_status: 404
    upstream_reason: global_notFound
    interpretation: UNKNOWN_NOT_FOUND_OR_INACCESSIBLE
    latency_ms: NOT_EXPOSED
    connector_id_on_error: NOT_EXPOSED
adoption_decision: ADOPT_WITH_GATES
campaign_result: ADOPT_WITH_GATES
campaign_status: COMPLETE
adopted_scope:
  - BOUNDED_FREEBUSY_FOR_AVAILABILITY_WITH_EXPLICIT_TIME_WINDOW_AND_NO_EVENT_DETAIL_READ
  - BOUNDED_EVENT_SEARCH_ONLY_FOR_A_KNOWN_OPERATOR_OBLIGATION_WITH_EXPLICIT_TIME_WINDOW_LOW_RESULT_CAP_AND_PRIVATE_BODY_HANDLING
  - EXACT_EVENT_READBACK_ONLY_WHEN_DIGEST_BINDING_OR_AN_OMITTED_REQUIRED_FIELD_JUSTIFIES_THE_EXTRA_READ
excluded_or_deferred_scope:
  - GENERAL_CALENDAR_MINING_OR_UNBOUNDED_EVENT_SEARCH
  - METADATA_ONLY_EVENT_SEARCH_CLAIM_BECAUSE_THE_CONNECTOR_RETURNED_PRIVATE_BODY_AND_IDENTITY_FIELDS
  - AUTOMATIC_ACCESS_REQUEST_LOGIN_OR_PERMISSION_REPAIR_FROM_404
  - SECONDARY_OR_SHARED_CALENDAR_PERMISSION_CLAIMS_NOT_DIRECTLY_PROBED
  - HIGH_RATE_POLLING_BULK_PAGINATION_OR_BLIND_RETRY
  - CALENDAR_WRITE_SEND_INVITE_OR_ACCOUNT_CHANGE
  - PROVIDER_DURABILITY_AS_WORKFLOW_REPLAY_RESUME_TRANSACTION_OR_EXACTLY_ONCE
mandatory_gates:
  - PREFER_FREEBUSY_FOR_AVAILABILITY_AND_USE_EVENT_SEARCH_ONLY_WHEN_EVENT_LEVEL_FACTS_ARE_REQUIRED
  - TREAT_SEARCH_EVENTS_AND_READ_EVENT_AS_PRIVATE_BODY_READ_SURFACES_NOT_METADATA_ONLY
  - REQUIRE_EXPLICIT_TIME_WINDOW_LOW_RESULT_CAP_NAMED_OBLIGATION_PRIVACY_CEILING_AND_CONSUMER
  - EVENT_DESCRIPTIONS_ATTENDEES_EMAIL_IDENTITIES_CONTACT_DETAILS_RAW_EVENT_IDS_URLS_LOCATIONS_EXACT_PRIVATE_BUSY_INTERVALS_AND_CALENDAR_IDS_STAY_IN_SOURCE_SYSTEMS_UNLESS_EXPLICITLY_REQUIRED
  - DO_NOT_PERSIST_PRIVATE_RESPONSE_BODIES_TO_GIT_OR_SLACK; PERSIST_ONLY_SANITIZED_FACTS_DIGESTS_AND_SOURCE_POINTERS
  - AVOID_READ_EVENT_WHEN_SEARCH_ALREADY_RETURNS_THE_REQUIRED_FACTS_EXCEPT_FOR_DIGEST_BINDING_OR_MISSING_FIELDS
  - EMPTY_SUCCESS_MEANS_NOT_FOUND_OR_UNKNOWN_NOT_GLOBAL_ABSENCE_OR_PERMISSION_PROOF
  - MAP_404_TO_UNKNOWN_NOT_FOUND_OR_INACCESSIBLE_NOT_GLOBAL_ABSENCE_AND_NOT_CONFIRMED_PERMISSION_DENIAL
  - DO_NOT_AUTO_REQUEST_ACCESS_OR_TRIGGER_LOGIN_FROM_404
  - RETRY_ONLY_FOR_DOCUMENTED_RETRYABLE_RATE_OR_SERVER_FAILURES_WITH_BOUNDED_EXPONENTIAL_BACKOFF_JITTER_AND_STOP_CONDITIONS
  - LIVE_OAUTH_IDENTITY_SCOPE_TOKEN_TYPE_STORAGE_AND_CREDENTIAL_CUSTODY_REMAIN_UNKNOWN
  - DO_NOT_DESCRIBE_THE_LIVE_CONNECTOR_AS_LEAST_PRIVILEGE
  - LOW_RATE_BOUNDED_CALLS_ONLY_WHILE_RAW_REQUEST_COUNT_QUOTA_HEADERS_RETRY_AUDIT_BILLING_CLASS_AND_INTERNAL_CALL_SEQUENCE_ARE_HIDDEN
  - RECHECK_QUOTA_AND_BILLING_BEFORE_SCALE_BECAUSE_ACTUAL_PROJECT_GRANDFATHERING_OR_NEW_QUOTA_CLASS_IS_UNKNOWN
  - NO_PROVIDER_DURABILITY_WORKFLOW_DURABILITY_EXACTLY_ONCE_OR_INDEPENDENT_VERIFICATION_CLAIM
credentials:
  required_observed: ONE_PREEXISTING_AUTHENTICATED_GOOGLE_CALENDAR_CONNECTOR
  new_login_account_creation_terms_or_secret_handling_this_campaign: false
  live_identity: UNKNOWN
  live_scope: UNKNOWN
  token_type: UNKNOWN
  token_storage: CONNECTOR_MANAGED_UNINSPECTED
  credential_custody: UNKNOWN
durability: GOOGLE_CALENDAR_PROVIDER_DURABILITY_ONLY_NO_HFO_WORKFLOW_REPLAY_RESUME_TRANSACTION_OR_EXACTLY_ONCE_SEMANTICS
observability:
  exposed_success_path: ACTION_CONNECTOR_ID_NORMALIZED_RESULT_SEARCH_LATENCY_PAGINATION_AND_ERROR_ENVELOPE
  exposed_error_path: WRAPPER_CLASS_UPSTREAM_HTTP_STATUS_REASON_AND_MESSAGE
  hidden: ERROR_LATENCY_CONNECTOR_ID_ON_ERROR_RAW_HEADERS_REQUEST_ID_OAUTH_IDENTITY_SCOPE_QUOTA_USAGE_RETRY_COUNT_BILLING_CLASS_AND_INTERNAL_CALL_SEQUENCE
portability:
  within_current_connector: MEDIUM_FOR_MEASURED_FREEBUSY_EVENT_SEARCH_AND_READBACK_ACTIONS
  direct_google_calendar_api: MEDIUM_WITH_REIMPLEMENTATION_OF_WRAPPER_FILTER_NORMALIZATION_AND_PRIVACY_GATES
  other_calendar_providers: LOW_AND_UNTESTED
failure_behavior:
  measured: SYNTHETIC_INVALID_CALENDAR_SELECTOR_FAILS_CLOSED_WITH_NOT_FOUND_404_AND_NO_EVENT_DATA
  ambiguous_semantics: THE_SAME_404_CLASS_CAN_MEAN_NONEXISTENT_OR_INACCESSIBLE
  unmeasured: REAL_SHARED_CALENDAR_PERMISSION_DENIAL_AUTH_FAILURE_401_RATE_LIMIT_403_OR_429_SERVER_5XX_RETRY_AND_PARTIAL_RESPONSE
custom_code_avoided_estimate:
  bounded_search_read_normalization_pagination: 60_to_160_LOC_UNVALIDATED
  freebusy_request_response_normalization: 30_to_80_LOC_UNVALIDATED
  request_auth_serialization_and_basic_error_unwrapping: 40_to_120_LOC_UNVALIDATED
  authentication_token_management: MATERIAL_BUT_UNQUANTIFIED
  retry_classification_policy: NOT_AVOIDED_REQUIRES_HFO_GATE
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
operator_relay_minutes: 0
operator_minutes_removed_estimate: 3_to_7_ACROSS_PHASES_2_AND_3_UNVALIDATED_UNTIL_CONSUMER_ACK
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_and_quota_limit:
  official_new_model_per_minute_per_project: 10000
  official_new_model_per_minute_per_user_per_project: 600
  official_daily_billing_threshold_requests: 1000000
  use_below_threshold_additional_cost: NONE_DOCUMENTED
  actual_connector_request_count: NOT_EXPOSED
  actual_project_quota_class: UNKNOWN_PRE_MAY_2026_PROJECTS_MAY_HAVE_PREVIOUS_QUOTAS
  actual_project_daily_usage: NOT_EXPOSED
  actual_billing_event: NOT_OBSERVED
  future_pricing_change_risk: MATERIAL_RECHECK_BEFORE_SCALE
strongest_falsifier: A_DISTINCT_REPRODUCTION_SHOWS_FREEBUSY_CAUSES_HIDDEN_EVENT_BODY_READS_OR_SEARCH_EVENT_PRIVACY_FIELDS_CANNOT_BE_CONTAINED_OR_THE_CONNECTOR_RETURNS_EVENT_DATA_OR_REAL_RESOURCE_METADATA_FOR_AN_UNAUTHORIZED_SELECTOR_OR_MAPS_THE_SAME_UPSTREAM_404_TO_SUCCESS_EMPTY_OR_HIDDEN_REQUEST_AMPLIFICATION_MAKES_BOUNDED_USE_UNSAFE
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_FOR_PRIVACY_PERMISSION_FAILURE_BEHAVIOR_REQUEST_EFFICIENCY_AND_SCOPE_CLAIMS
consumer: S05_OPERATOR_RELIEF_CELL_AND_X11_CARRIER_SURFACE_LAB
consumer_ack: NOT_OBSERVED
fitness_credit: 0_PENDING_EXPLICIT_CONSUMER_ACK
review_expiry_utc: 2026-08-08T16:47:56Z
honest_flaw: THE_DECISION_RESTS_ON_THREE_SMALL_SAME_PROVIDER_PROBES_AND_OFFICIAL_RAW_API_DOCUMENTATION; IT_DOES_NOT_INSPECT_THE_CONNECTOR_IMPLEMENTATION_LIVE_OAUTH_SCOPE_TRUE_UPSTREAM_CALL_COUNT_PROJECT_QUOTA_CLASS_OR_REAL_PERMISSION_AUTH_RATE_LIMIT_AND_SERVER_FAILURES
next_campaign:
  experiment_id: X13_GOOGLE_DRIVE_READONLY_CONNECTOR_001
  candidate: Google_Drive_read_only_search_fetch_and_metadata_connector
  next_phase: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
canonical_event: true
sealed: true
---

# X13 Google Calendar read-only connector phase 4 — adopt with gates

Adopt the measured read-only surfaces only. Use free/busy first for availability because it returns busy intervals rather than event bodies. Use event search only for a named obligation with a narrow time window, low result cap, private-body handling, and a named consumer. An exact event read is justified only when digest binding or a required omitted field needs it.

The connector removed a small manual Calendar lookup during the known Reed HVAC reconciliation and failed closed on a synthetic invalid-calendar selector. That supports bounded operator-relief use, but not a general Calendar mining service. Event search returned full description and identity-bearing fields when only metadata was needed, so it must be treated as a private-body read surface.

The live OAuth identity, scope, token type, credential custody, upstream request count, project quota class, quota headers, retry audit, and internal call sequence remain hidden. A 404 means only `unknown: not found or inaccessible`; it cannot trigger access requests, login, or a global-absence claim. Provider durability is not workflow durability.

This is same-provider advisory evidence with binding weight zero. Fitness credit remains zero until S05 or X11 explicitly consumes the capability and records measured operator relief. Next campaign: Google Drive read-only search, fetch, and metadata connector phase 1.
