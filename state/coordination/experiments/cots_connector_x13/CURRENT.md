---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GOOGLE_CONTACTS_READONLY_CONNECTOR_001
version: 26
prior_version: 25
candidate: Google_Contacts_read_only_lookup_and_recipient_resolution_connector
candidate_contract_reference: official_Google_People_searchContacts_people_get_Person_scopes_cache_and_field_masks_plus_direct_connector_receipts
campaign_wake: 2_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_completed: false
phase_4_decision: PENDING
binding_architecture_decision: false
last_event_commit: f59fd296b5ef8a1f37fed1072877645de6273f78
last_event_path: state/coordination/experiments/cots_connector_x13/20260801T224921Z_GOOGLE_CONTACTS_READONLY_PHASE2_SOURCE_BOUND_LOOKUP.md
last_event_blob_sha: 3c5aee0c2f67b9fcdb39da17636035c538a3897a
prior_current_commit: 3bdf9a24cd71e9139bb37c973b395ef75d169588
prior_current_blob_sha: 2df63b31b9cb2dbd6df33fcd8dbfaf7485f65625
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
effect_ceiling: ONE_SOURCE_BOUND_READ_ONLY_CONTACT_SEARCH_LOW_RESULT_CAP_NO_CONTACT_BODY_READ_NO_RECIPIENT_SELECTION_NO_SEND_NO_CONTACT_WRITE_NO_PRIVATE_IDENTITY_EXTERNALIZATION
adoption_credit: 2
adoption_credit_basis:
  - OFFICIAL_PRIMARY_CONTRACT_PLUS_ONE_SYNTHETIC_EMPTY_DIRECT_CONNECTOR_TRACE
  - ONE_SOURCE_BOUND_MATCHED_DIRECT_TRACE_WITH_AMBIGUITY_CAUGHT_AND_NO_WORLD_EFFECT
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
independent_verification_closed: false
operator_relay_minutes: 0
operator_minutes_removed_measured: 0_SELECTION_REMAINS_UNRESOLVED
operator_minutes_removed_estimate_per_CONFIRMED_bounded_lookup: 1_to_3_UNVALIDATED
custom_code_avoided_estimate:
  authenticated_contact_query_and_result_normalization: 30_to_80_LOC_UNVALIDATED
  recipient_candidate_display: 20_to_60_LOC_UNVALIDATED
  ambiguity_privacy_source_binding_and_approval_policy: NOT_AVOIDED_REQUIRES_HFO_GATES
  authenticated_people_api_client_and_token_refresh: MATERIAL_BUT_UNQUANTIFIED
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
credentials:
  connector_authenticated_in_phase1_and_phase2: true
  operator_supplied_credentials: 0
  live_identity: UNKNOWN
  live_oauth_scope: UNKNOWN
  token_type: UNKNOWN
  credential_custody: UNKNOWN
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_connector_request_count: NOT_PROVEN
live_quota_headers_or_units: NOT_EXPOSED
actual_project_quota_class: UNKNOWN
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
official_contract_checked_2026_08_01:
  search_endpoint: people.searchContacts
  source_contract: AUTHENTICATED_USERS_GROUPED_CONTACTS_FROM_CONTACT_SOURCE
  match_semantics: PREFIX_PHRASE_OVER_NAMES_NICKNAMES_EMAILS_PHONES_AND_ORGANIZATIONS
  maximum_page_size: 30
  read_mask_required: true
  cache_warmup_required: EMPTY_QUERY_THEN_WAIT_SEVERAL_SECONDS
  accepted_search_scopes:
    - contacts
    - contacts.readonly
  people_get_field_mask_required: true
  merged_person_sources_possible: true
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
  hidden_or_unattested:
    - readMask
    - source_selection
    - empty_query_cache_warmup
    - warmup_to_search_delay
    - upstream_method_and_request_url
    - oauth_scope_and_authenticated_identity
    - saved_contact_vs_otherContacts_vs_directory_ranking_policy
    - request_count_quota_class_retries_headers_and_wrapper_fanout
failure_semantics:
  empty_success: NO_MATCH_RETURNED_BY_ONE_WRAPPER_CALL_NOT_ABSENCE_DIRECTORY_PROOF_CACHE_FRESHNESS_OR_COMPLETENESS
  matched_multi_candidate: HOLD_SELECTION_AND_RETURN_ONLY_SANITIZED_COUNTS_FIELD_CLASSES_SOURCE_PREFIX_AND_DIGESTS
  context_coherent_candidate: NOT_IDENTITY_PROOF
  otherContacts_result: NOT_A_CURATED_SAVED_CONTACT_ASSERTION
  permission_401_403_404: NOT_TESTED
  rate_limit_429_and_5xx: NOT_TESTED
durability: GOOGLE_CONTACTS_PROVIDER_STORAGE_ONLY_NO_WORKFLOW_REPLAY_RESUME_TRANSACTION_IDEMPOTENCY_OR_EXACTLY_ONCE_CLAIM
observability: MEDIUM_FOR_WRAPPER_ACTION_RESULT_COUNT_FIELD_CLASSES_SOURCE_PREFIX_NORMALIZED_ERROR_CONNECTOR_ID_AND_LATENCY_BUT_LOW_FOR_UPSTREAM_REQUEST_FIELD_MASK_WARMUP_SCOPE_QUOTA_RETRIES_CACHE_AGE_AND_RANKING
portability: MEDIUM_FOR_PROVIDER_NEUTRAL_RECIPIENT_LOOKUP_INTENT_LOW_TO_MEDIUM_FOR_GOOGLE_PREFIX_MATCHING_OTHERCONTACTS_MERGED_PERSON_SEMANTICS_OPAQUE_RESOURCE_NAMES_AND_WRAPPER_RESULT_NORMALIZATION
provisional_scope:
  - ONE_NAMED_OPERATOR_OBLIGATION
  - ONE_BOUNDED_RECIPIENT_CANDIDATE_LOOKUP
  - LOW_RESULT_CAP
  - SEARCH_FIRST
  - NO_SEND_NO_INVITE_NO_CONTACT_WRITE
  - READ_CONTACT_ONLY_IF_NAMED_CONSUMER_REQUIRES_ONE_SPECIFIC_MISSING_FIELD
mandatory_gates:
  - TREAT_MATCHED_RESULTS_AS_PRIVATE_IDENTITY_DATA
  - PERSIST_ONLY_SANITIZED_COUNTS_FIELD_CLASSES_SOURCE_PREFIX_AND_DIGESTS_UNLESS_THE_CONSUMER_EXPLICITLY_REQUIRES_THE_ADDRESS_IN_THE_PRIVATE_SOURCE_SYSTEM
  - NEVER_AUTO_SELECT_OR_SEND_FROM_FUZZY_PREFIX_DUPLICATE_SPELLING_CONTEXTUAL_DOMAIN_UNKNOWN_DISPLAY_NAME_OR_MULTI_SOURCE_RESULTS
  - REQUIRE_SOURCE_BOUND_IDENTITY_CONFIRMATION_OR_OPERATOR_APPROVAL_BEFORE_EMAIL_SEND_INVITE_OR_EXTERNAL_ACTION
  - DO_NOT_TREAT_OTHERCONTACTS_AS_A_CURATED_SAVED_ADDRESS_BOOK
  - TREAT_EMPTY_RESULT_AS_NO_MATCH_RETURNED_BY_ONE_WRAPPER_CALL_ONLY
  - DO_NOT_CLAIM_CURRENT_CACHE_COMPLETENESS_UNTIL_WARMUP_BEHAVIOR_IS_EXPOSED_OR_INDEPENDENTLY_MEASURED
  - DO_NOT_CLAIM_LEAST_PRIVILEGE_WHILE_SCOPE_AND_FIELD_MASK_ARE_HIDDEN
  - DO_NOT_READ_FULL_CONTACT_BODY_UNLESS_A_NAMED_CONSUMER_REQUIRES_ONE_SPECIFIC_MISSING_FIELD
  - FITNESS_REMAINS_ZERO_UNTIL_A_NAMED_DOWNSTREAM_WORKITEM_RECORDS_SOURCE_BOUND_CONSUMERACK_AND_MEASURED_OPERATOR_OUTCOME
excluded_or_deferred_scope:
  - GENERAL_CONTACT_EXPORT_OR_INVENTORY
  - DIRECTORY_MINING_OR_GMAIL_HISTORY_INFERENCE
  - CONTACT_BODY_PERSISTENCE_TO_GIT_OR_SLACK
  - AUTOMATIC_RECIPIENT_SELECTION
  - SEND_INVITE_CONTACT_WRITE_ACCOUNT_OR_SECURITY_CHANGE
  - PROVIDER_STORAGE_AS_WORKFLOW_DURABILITY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NON_CHATGPT_CONTACT_CONNECTOR_OR_SOURCE_OWNER_REVIEW
consumer:
  - S05_OPERATOR_RELIEF_CELL
  - X11_CARRIER_SURFACE_PDCA_LAB
reversible_next_experiment: ONE_SYNTHETIC_INVALID_OR_PERMISSION_VARIANCE_PROBE_WITH_NO_REAL_IDENTITY_QUERY_NO_CONTACT_BODY_READ_AND_SANITIZED_ERROR_CAPTURE
strongest_falsifier: A_SOURCE_BOUND_TRACE_PROVES_THE_CONNECTOR_CAN_REQUEST_MINIMAL_FIELDS_SELECT_ONLY_CURATED_SAVED_CONTACTS_AND_RETURN_ONE_UNAMBIGUOUS_CURRENT_RECIPIENT_WITHOUT_OPERATOR_CONFIRMATION_OR_PRIVATE_BODY_OVERREAD
honest_flaw: PHASE2_USED_A_REAL_PRIVATE_NAME_AND_THE_CONNECTOR_EXPOSED_THREE_PRIVATE_EMAIL_CANDIDATES_TO_THIS_RUNTIME; RAW_VALUES_WERE_NOT_PERSISTED_BUT_NO_INDEPENDENT_SOURCE_CONFIRMED_THE_CORRECT_RECIPIENT_AND_THE_LOOKUP_DID_NOT_REMOVE_OPERATOR_WORK
review_expiry_utc: 2026-08-08T22:49:21Z
valid_time_utc: 2026-08-01T22:49:21Z
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

Google Contacts read-only recipient resolution is active at phase **2/4**.

A source-bound lookup for one existing property-safety follow-up returned three private identity candidates in 2.410 seconds. All three were `otherContacts` resources. The connector exposed resource IDs, names, email addresses, and mail pointers while still exposing no field-mask, source-selection, cache-warmup, OAuth-scope, ranking, quota, retry, or request-count controls.

The micro-use proved candidate retrieval but did not resolve the recipient. One candidate was context-coherent with the obligation, but contextual coherence is not identity proof. No candidate was selected, no full contact body was read, and no send, invitation, or contact write occurred. Operator minutes removed remain zero.

Next: one synthetic, privacy-safe invalid-input or permission-variance probe. Error output must be sanitized before Git or Slack persistence.
