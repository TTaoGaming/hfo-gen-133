---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_CONTACTS_READONLY_CONNECTOR_001
version: 28
prior_version: 27
candidate: Google_Contacts_read_only_lookup_and_recipient_resolution_connector
candidate_contract_reference: official_Google_People_searchContacts_otherContacts_search_people_resource_scopes_cache_field_masks_plus_direct_connector_receipts
campaign_wake: 4_of_4
campaign_status: COMPLETE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: true
phase_4_decision: ADOPT_WITH_GATES
admitted_capability: BOUNDED_RECIPIENT_CANDIDATE_DISCOVERY_ONLY
binding_architecture_decision: false
last_event_commit: dff26eeef9989f0c9af9ee88c20c845df2388d49
last_event_path: state/coordination/experiments/cots_connector_x13/20260802T004800Z_GOOGLE_CONTACTS_READONLY_PHASE4_DECISION.md
last_event_blob_sha: c6cbb435c09953e7be5cdc545dcb066709025083
prior_current_commit: 89e611adf18a89fa4800afa58657aca355a3db26
prior_current_blob_sha: 798eaa1146414668fe2aad0a38c30b1c599c0247
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
effect_ceiling: READ_ONLY_BOUNDED_CONTACT_CANDIDATE_DISCOVERY_NO_AUTOMATIC_SELECTION_NO_SEND_NO_INVITE_NO_CONTACT_WRITE_NO_PERMISSION_ACCOUNT_OR_SECURITY_CHANGE
adoption_credit: 4
adoption_credit_basis:
  - OFFICIAL_PRIMARY_CONTRACT_PLUS_ONE_SYNTHETIC_EMPTY_DIRECT_CONNECTOR_TRACE
  - ONE_SOURCE_BOUND_MATCHED_DIRECT_TRACE_WITH_AMBIGUITY_CAUGHT_AND_NO_WORLD_EFFECT
  - ONE_SYNTHETIC_INVALID_ARGUMENT_TRACE_WITH_ERROR_URL_LEAK_OBSERVED
  - ONE_BOUNDED_PHASE4_ADOPT_WITH_GATES_DECISION_WITHOUT_NEW_CONTACT_CALL
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0_SELECTION_REMAINED_UNRESOLVED
operator_minutes_removed_estimate_per_CONFIRMED_bounded_lookup: 1_to_3_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_contact_query_and_result_normalization: 30_to_80_LOC_UNVALIDATED
  recipient_candidate_display: 20_to_60_LOC_UNVALIDATED
  authenticated_error_normalization: 20_to_60_LOC_UNVALIDATED
  authenticated_people_api_client_and_token_refresh: MATERIAL_BUT_UNQUANTIFIED
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
custom_policy_not_avoided:
  - AMBIGUITY_HANDLING
  - PRIVATE_DATA_MINIMIZATION
  - SOURCE_BOUND_IDENTITY_CONFIRMATION
  - OPERATOR_APPROVAL
  - CACHE_AND_SOURCE_ASSERTION_LIMITS
  - CONSUMER_ACK
  - ERROR_SANITIZATION
credentials:
  connector_authenticated_or_provider_reachable_in_all_three_calling_phases: true
  operator_supplied_credentials: 0
  live_identity: UNKNOWN
  live_oauth_scope: UNKNOWN
  token_type: UNKNOWN
  credential_custody: UNKNOWN
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_connector_wrapper_invocations: 3
phase_4_connector_invocations: 0
live_quota_headers_or_units: NOT_EXPOSED
actual_project_quota_class: UNKNOWN
billing_counters: NOT_EXPOSED
phase_1_receipt:
  action: Google_Contacts.search_contacts
  query_class: SYNTHETIC_HIGH_ENTROPY_NO_MATCH
  query_sha256: e72c906ca73ab85339ac2259a07643060c1dae8ce9244873cb3781f89388be3e
  max_results: 3
  result: SUCCESS_EMPTY
  result_count: 0
  external_call_time_ms: 972
  contact_body_returned: false
  identity_bearing_result_returned: false
phase_2_receipt:
  source_system: GOOGLE_CALENDAR_PRIMARY_PRIVATE
  source_obligation_class: PROPERTY_SAFETY_CONTACT_FOLLOWUP
  matching_source_event_count: 2
  action: Google_Contacts.search_contacts
  query_sha256: 4256e512fcfb03cad0ee741589ec9ea9d525dc2af0ebb1d5db1ffa9eb4cc3f49
  max_results: 3
  result: SUCCESS_MATCHED_AMBIGUOUS
  result_count: 3
  external_call_time_ms: 2410
  source_prefix_observed: otherContacts
  source_prefix_count: 3
  returned_field_classes:
    - resource_id
    - display_name
    - email_address
    - mailto_pointer
  raw_identity_fields_persisted: false
  contact_body_read: false
  automatic_selection: false
  send_invite_or_write: false
phase_3_receipt:
  action: Google_Contacts.search_contacts
  query_class: SYNTHETIC_INVALID_NEGATIVE_PAGE_SIZE
  synthetic_query_sha256: 8711c38123fc2df1c3fd1878187b24c6360b50fe9fb71e4e23b4054aa69a6d56
  max_results: -1
  result: INVALID_ARGUMENT
  upstream_http_status: 400
  upstream_status: INVALID_ARGUMENT
  identity_bearing_result_returned: false
  contact_body_returned: false
  upstream_endpoint_observed_in_error: people.googleapis.com/v1/people:searchContacts
  upstream_method_inferred_from_url: GET
  upstream_read_mask_observed:
    - names
    - emailAddresses
    - photos
  raw_request_url_exposed_in_error: true
  raw_request_url_persisted: false
  automatic_retry_observed: false
  permission_or_consent_transition: false
phase_4_receipt:
  new_contacts_call: false
  decision: ADOPT_WITH_GATES
  admitted_scope: BOUNDED_RECIPIENT_CANDIDATE_DISCOVERY_ONLY
  event_commit: dff26eeef9989f0c9af9ee88c20c845df2388d49
  event_blob_sha: c6cbb435c09953e7be5cdc545dcb066709025083
official_contract_checked_2026_08_02:
  people_searchContacts_endpoint: GET_https://people.googleapis.com/v1/people:searchContacts
  people_searchContacts_source_contract: AUTHENTICATED_USERS_GROUPED_CONTACTS_FROM_CONTACT_SOURCE
  match_semantics: PREFIX_PHRASE_OVER_NAMES_NICKNAMES_EMAILS_PHONES_AND_ORGANIZATIONS
  page_size: DEFAULT_10_IF_OMITTED_OR_ZERO_VALUES_OVER_30_CAPPED_TO_30
  read_mask_required: true
  cache_warmup_required: EMPTY_QUERY_THEN_WAIT_SEVERAL_SECONDS
  accepted_search_scopes:
    - contacts
    - contacts.readonly
  otherContacts_search_endpoint: GET_https://people.googleapis.com/v1/otherContacts:search
  otherContacts_search_source_contract: OTHER_CONTACT_SOURCE
  otherContacts_search_scope: contacts.other.readonly
  person_resources_can_merge_multiple_sources: true
  otherContacts_typically_auto_created_from_interactions: true
  numeric_connected_project_quota_ceiling: NOT_ESTABLISHED_BY_INSPECTED_PUBLIC_SEARCH_CONTRACT_OR_LIVE_WRAPPER
connector_variance:
  exposed_inputs:
    - query
    - max_results
  exposed_outputs_observed:
    - resource_id
    - display_name
    - email_address
    - mailto_pointer
    - source_resource_prefix
  error_path_telemetry_observed:
    endpoint: people_searchContacts
    readMask: names_emailAddresses_photos
    full_provider_request_url_echoed: true
  hidden_or_unattested:
    - success_path_endpoint_and_source_selection
    - public_field_mask_control
    - empty_query_cache_warmup
    - warmup_to_search_delay
    - oauth_scope_and_authenticated_identity
    - saved_contact_vs_otherContacts_vs_directory_ranking_policy
    - request_count_quota_class_retries_headers_and_wrapper_fanout
source_class_attribution:
  phase2_success_payload_resource_prefix: otherContacts
  phase3_invalid_error_endpoint: people_searchContacts
  status: UNRESOLVED
  claim_ceiling: DO_NOT_INFER_SUCCESS_PATH_ENDPOINT_SOURCE_SCOPE_OR_RANKING_FROM_ERROR_PATH_OR_RESOURCE_PREFIX_ALONE
failure_semantics:
  empty_success: NO_MATCH_RETURNED_BY_ONE_WRAPPER_CALL_NOT_ABSENCE_DIRECTORY_PROOF_CACHE_FRESHNESS_OR_COMPLETENESS
  matched_multi_candidate: HOLD_SELECTION_AND_RETURN_ONLY_SANITIZED_COUNTS_FIELD_CLASSES_SOURCE_PREFIX_AND_DIGESTS
  context_coherent_candidate: NOT_IDENTITY_PROOF
  otherContacts_result: NOT_A_CURATED_SAVED_CONTACT_ASSERTION
  invalid_negative_page_size: HTTP_400_INVALID_ARGUMENT_NO_IDENTITY_RESULT
  invalid_argument_retry: DO_NOT_BLIND_RETRY_WITHOUT_CORRECTING_REQUEST
  error_privacy: FULL_PROVIDER_URL_MAY_ECHO_QUERY_AND_FIELDS_SANITIZE_BEFORE_PERSISTENCE
  permission_401_403_404: NOT_TESTED_AND_MUST_NOT_BE_FORCED
  rate_limit_429_and_5xx: NOT_TESTED
durability: GOOGLE_CONTACTS_PROVIDER_STORAGE_ONLY_NO_WORKFLOW_REPLAY_RESUME_TRANSACTION_IDEMPOTENCY_OR_EXACTLY_ONCE_CLAIM
observability: MEDIUM_FOR_WRAPPER_ACTION_RESULT_COUNT_FIELD_CLASSES_SOURCE_PREFIX_NORMALIZED_ERROR_ENDPOINT_CLASS_READMASK_AND_RESPONSE_STATUS_BUT_LOW_FOR_SUCCESS_PATH_ENDPOINT_SOURCE_CACHE_SCOPE_IDENTITY_QUOTA_RETRIES_AND_RANKING
portability: MEDIUM_FOR_PROVIDER_NEUTRAL_RECIPIENT_CANDIDATE_LOOKUP_AND_INVALID_ARGUMENT_INTENT_LOW_TO_MEDIUM_FOR_GOOGLE_PREFIX_MATCHING_OTHERCONTACTS_RESOURCE_NAMES_ENDPOINTS_FIELDMASKS_CACHE_AND_WRAPPER_NORMALIZATION
admitted_scope:
  - ONE_NAMED_OPERATOR_OBLIGATION
  - ONE_SOURCE_BOUND_IDENTITY_HINT
  - ONE_BOUNDED_RECIPIENT_CANDIDATE_LOOKUP
  - LOW_RESULT_CAP
  - SEARCH_FIRST
  - CANDIDATE_DISCOVERY_ONLY
  - NO_SEND_NO_INVITE_NO_CONTACT_WRITE
  - READ_CONTACT_ONLY_IF_NAMED_CONSUMER_REQUIRES_ONE_SPECIFIC_MISSING_FIELD
mandatory_gates:
  - TREAT_MATCHED_RESULTS_AS_PRIVATE_IDENTITY_DATA
  - PERSIST_ONLY_SANITIZED_COUNTS_FIELD_CLASSES_SOURCE_PREFIX_AND_DIGESTS_UNLESS_THE_CONSUMER_EXPLICITLY_REQUIRES_THE_ADDRESS_IN_THE_PRIVATE_SOURCE_SYSTEM
  - NEVER_AUTO_SELECT_OR_SEND_FROM_FUZZY_PREFIX_DUPLICATE_SPELLING_CONTEXTUAL_DOMAIN_UNKNOWN_DISPLAY_NAME_MERGED_SOURCE_OR_MULTI_CANDIDATE_RESULTS
  - REQUIRE_SOURCE_BOUND_IDENTITY_CONFIRMATION_OR_OPERATOR_APPROVAL_BEFORE_EMAIL_SEND_INVITE_SCHEDULING_OR_EXTERNAL_ACTION
  - DO_NOT_TREAT_OTHERCONTACTS_AS_A_CURATED_SAVED_ADDRESS_BOOK
  - TREAT_EMPTY_RESULT_AS_NO_MATCH_RETURNED_BY_ONE_WRAPPER_CALL_ONLY
  - DO_NOT_CLAIM_CURRENT_CACHE_COMPLETENESS_UNTIL_WARMUP_BEHAVIOR_IS_EXPOSED_OR_INDEPENDENTLY_MEASURED
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_WHILE_SCOPE_IDENTITY_SOURCE_SELECTION_AND_FIELD_MASK_CONTROL_ARE_HIDDEN
  - DO_NOT_READ_FULL_CONTACT_BODY_UNLESS_A_NAMED_CONSUMER_REQUIRES_ONE_SPECIFIC_MISSING_FIELD
  - TREAT_CONNECTOR_ERRORS_AS_POTENTIAL_PRIVATE_QUERY_LEAKS
  - SANITIZE_PROVIDER_REQUEST_URL_QUERY_FILTER_IDENTIFIERS_AND_FIELD_VALUES_BEFORE_GIT_OR_SLACK_PERSISTENCE
  - DO_NOT_USE_REAL_IDENTITIES_IN_MALFORMED_INPUT_PROBES
  - DO_NOT_BLIND_RETRY_HTTP_400_INVALID_ARGUMENT
  - DO_NOT_LAUNDER_ERROR_PATH_ENDPOINT_OR_RESOURCE_PREFIX_INTO_SUCCESS_PATH_SOURCE_SCOPE_OR_RANKING_PROOF
  - NO_SEND_INVITE_CONTACT_WRITE_ACCOUNT_SECURITY_CONSENT_OR_PERMISSION_REPAIR_WITHOUT_SEPARATE_AUTHORITY
  - FITNESS_REMAINS_ZERO_UNTIL_A_NAMED_DOWNSTREAM_WORKITEM_RECORDS_SOURCE_BOUND_CONSUMERACK_AND_MEASURED_OPERATOR_OUTCOME
excluded_or_deferred_scope:
  - GENERAL_CONTACT_EXPORT_OR_INVENTORY
  - DIRECTORY_MINING_OR_GMAIL_HISTORY_INFERENCE
  - CONTACT_BODY_PERSISTENCE_TO_GIT_OR_SLACK
  - AUTOMATIC_RECIPIENT_SELECTION
  - FORCED_PERMISSION_DENIAL_CONSENT_FLOW_OR_OAUTH_REFRESH
  - SEND_INVITE_CONTACT_WRITE_ACCOUNT_OR_SECURITY_CHANGE
  - PROVIDER_STORAGE_AS_WORKFLOW_DURABILITY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NON_CHATGPT_CONTACT_CONNECTOR_OWNER_OR_SUCCESS_PATH_TRACE_REVIEW
consumer:
  - S05_OPERATOR_RELIEF_CELL
  - X11_CARRIER_SURFACE_PDCA_LAB
  - X13_NEXT_CAMPAIGN
strongest_falsifier: A_SUCCESS_PATH_TRACE_FOR_THIS_WRAPPER_VERSION_PROVES_THE_EXACT_ENDPOINT_SOURCE_SELECTION_READMASK_WARMUP_SCOPE_IDENTITY_RETRY_COUNT_UPSTREAM_REQUEST_COUNT_RANKING_AND_RESOURCE_MAPPING_OR_PROVES_ERRORS_SANITIZED_BEFORE_RUNTIME_EXPOSURE_PLUS_A_SOURCE_BOUND_CONSUMERACK_MEASURES_SAFE_OPERATOR_RELIEF
honest_flaw: PHASE2_USED_A_REAL_PRIVATE_NAME_AND_EXPOSED_THREE_PRIVATE_EMAIL_CANDIDATES_TO_THE_RUNTIME_PHASE3_ONLY_TESTED_AN_INVALID_ERROR_ROUTE_SUCCESS_PATH_SOURCE_SCOPE_CACHE_RANKING_AND_LEAST_PRIVILEGE_REMAIN_UNKNOWN_AND_ZERO_OPERATOR_MINUTES_WERE_MEASURED_REMOVED
next_campaign:
  experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
  candidate: GitHub_contents_API_branch_scoped_file_create_update_fetch_and_readback_connector
  next_phase: 1_of_4
  status: PLANNED
  effect_ceiling: HARMLESS_BRANCH_SCOPED_FILE_EVENT_AND_READBACK_ONLY_NO_MERGE_DELETE_FORCE_PUSH_OR_PRODUCTION_CHANGE
  first_probe: OFFICIAL_CONTRACT_PLUS_ONE_EXISTING_BRANCH_SCOPED_GIT_FIRST_EVENT_READBACK_BASELINE
  claim_limit: DO_NOT_CLAIM_DATABASE_ATOMICITY_WORKFLOW_DURABILITY_MERGE_SAFETY_OR_INDEPENDENT_VERIFICATION_FROM_GIT_STORAGE_ALONE
review_expiry_utc: 2026-08-09T00:48:00Z
valid_time_utc: 2026-08-02T00:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
prior_campaign:
  experiment_id: X13_GOOGLE_DRIVE_READONLY_CONNECTOR_001
  final_version: 24
  decision: ADOPT_WITH_GATES
  decision_commit: c0f93c82fbae71f4bc301f62929d0bd072ee052f
prior_prior_campaign:
  experiment_id: X13_GOOGLE_CALENDAR_READONLY_CONNECTOR_001
  final_version: 20
  decision: ADOPT_WITH_GATES
  decision_commit: 5e31a7b5f58cec5338e42f69d75a040626a6d062
prior_prior_prior_campaign:
  experiment_id: X13_GMAIL_READONLY_CONNECTOR_001
  final_version: 16
  decision: ADOPT_WITH_GATES
  decision_commit: 7a72ec06c8c4c94f6b88c4303066a3fac71ebd8c
---

# X13 current campaign

Google Contacts read-only recipient resolution is complete at phase **4/4** with `ADOPT_WITH_GATES`.

The admitted capability is one bounded recipient-candidate lookup for a named, source-bound operator obligation. Search results remain private identity data and nonbinding. No fuzzy, duplicate, contextual, merged-source, or `otherContacts` result may be auto-selected, and no email, invitation, scheduling, or other external action may occur without source-bound confirmation or operator approval.

The campaign measured zero operator minutes removed. It observed three connector invocations, no surfaced charge, one ambiguous three-candidate result, and one fail-closed HTTP 400 path that leaked the full provider request URL. Success-path endpoint, source, scope, field mask, cache state, ranking, retries, quota, fan-out, and credential custody remain unknown.

Next campaign: GitHub Contents API branch-scoped create/update/fetch/readback, phase 1. Git storage must not be laundered into database atomicity, workflow durability, merge safety, or independent-verification claims.
