---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_READONLY_CONNECTOR_001
phase: 4
phase_name: ADOPTION_DECISION
campaign_wake: 4_of_4
expected_prior_version: 15
next_version: 16
candidate: Gmail_read_only_search_and_message_metadata_connector
carrier: X13_COTS_AND_CONNECTOR_PDCA_LAB
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUNTIME_PROMPT
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_blob_sha: d5d79bd10fb405244b6293554cabd76e61e19d54
wip: 1
valid_time_utc: 2026-08-01T12:48:17Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
evidence_class:
  - DIRECT_GMAIL_CONNECTOR_RECEIPTS_PHASE1_PHASE2_PHASE3
  - OFFICIAL_GOOGLE_GMAIL_API_DOCUMENTATION_CHECKED_2026_08_01
  - SAME_PROVIDER_NONBINDING_ADVISORY
binding_weight: 0
effect_ceiling: PHASE4_DECISION_ONLY_NO_NEW_MAILBOX_READ_NO_WRITE
self_probe:
  exposed_tools:
    - GitHub_fetch_search_create_update
    - Slack_pointer_write
    - web_official_document_research
    - Gmail_connector_available_but_not_called_this_phase
  native_task_inventory_read: false
source_bindings:
  phase1:
    commit: 5e2b25a98206c2c17f58608bc7710f77996629d9
    path: state/coordination/experiments/cots_connector_x13/20260801T094705Z_GMAIL_ID_LIST_PHASE1_BASELINE.md
    blob_sha: 334026f4872fa38ffea5da03e8e784422c4cd680
  phase2:
    commit: 762e44e70865d2bd7368b73411ae3ad906bbac75
    path: state/coordination/experiments/cots_connector_x13/20260801T104849Z_GMAIL_LABEL_COUNTS_PHASE2_READ_ONLY_MICRO_USE.md
    blob_sha: 2fe987da24624d91a631a6948a7340027086f58d
  phase3:
    commit: 47a89124c7c2721c3dcdec6a191a50fdbc06cd4e
    path: state/coordination/experiments/cots_connector_x13/20260801T114940Z_GMAIL_ABSENT_LABEL_PHASE3_VARIANCE_PROBE.md
    blob_sha: 05704ca447df7eca42d9aad9374502280459f744
official_contract_sources:
  labels_list:
    url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels/list
    last_updated_utc: 2026-04-15
    finding: LISTS_ALL_LABELS_NO_NAME_FILTER_PARAMETER_AND_LIST_ITEMS_HAVE_ID_NAME_VISIBILITY_AND_TYPE_ONLY
  labels_resource:
    url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels
    last_updated_utc: 2026-04-15
    finding: LABEL_RESOURCE_DEFINES_MESSAGE_AND_THREAD_TOTAL_AND_UNREAD_AGGREGATES
  labels_get:
    url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels/get
    last_updated_utc: 2026-04-15
    finding: GETS_ONE_LABEL_AND_ACCEPTS_GMAIL_METADATA_AMONG_OTHER_SCOPES
  scopes:
    url: https://developers.google.com/workspace/gmail/api/auth/scopes
    last_updated_utc: 2026-06-03
    finding: GMAIL_METADATA_AND_GMAIL_READONLY_ARE_RESTRICTED_SCOPES_AND_NARROWEST_PRACTICAL_SCOPE_IS_PREFERRED
  quota:
    url: https://developers.google.com/workspace/gmail/api/reference/quota
    last_updated_utc: 2026-06-03
    finding: LABELS_LIST_1_LABELS_GET_1_MESSAGES_LIST_5_MESSAGES_GET_20_UNITS; STANDARD_USE_BELOW_DAILY_THRESHOLD_HAS_NO_ADDITIONAL_COST_BUT_LATER_2026_CHARGING_IS_PLANNED_WITH_NOTICE
  errors:
    url: https://developers.google.com/workspace/gmail/api/guides/handle-errors
    last_updated_utc: 2026-06-03
    finding: RAW_API_EXPOSES_HTTP_AND_JSON_ERROR_CLASSES_AND_RECOMMENDS_BOUNDED_EXPONENTIAL_BACKOFF_FOR_RETRYABLE_RATE_OR_SERVER_ERRORS
measured_campaign_summary:
  phase1_id_only_list:
    result: SUCCESS
    external_call_time_ms: 356
    message_id_count_returned_to_connector: 1
    private_identifiers_externalized: false
    body_or_header_returned: false
  phase2_known_label_aggregate:
    result: SUCCESS
    external_call_time_ms: 505
    returned_known_system_label_count: 1
    aggregate_fields_present: true
    exact_private_counts_externalized: false
    body_header_or_message_id_returned: false
  phase3_absent_label_name:
    result: SUCCESS_EMPTY_ARRAY
    external_call_time_ms: 279
    raw_http_or_provider_error_class_exposed: false
    interpretation: NOT_FOUND_OR_UNKNOWN_ONLY
adoption_decision: ADOPT_WITH_GATES
adopted_scope:
  - BOUNDED_EXACT_KNOWN_LABEL_STATUS_AGGREGATES_FOR_OPERATOR_RELIEF
  - BOUNDED_ID_ONLY_MESSAGE_DISCOVERY_WHEN_AGGREGATES_CANNOT_ANSWER_THE_QUESTION
excluded_or_deferred_scope:
  - MESSAGE_METADATA_FETCH_UNTIL_EXPLICIT_FORMAT_METADATA_AND_HEADER_CONTROLS_ARE_EXPOSED_AND_PROVEN
  - MESSAGE_BODY_OR_ATTACHMENT_READ_BY_DEFAULT
  - ARBITRARY_QUERY_SEARCH_UNDER_AN_ASSUMED_GMAIL_METADATA_SCOPE
  - HIGH_RATE_POLLING_OR_BULK_MAILBOX_MINING
  - RAW_PROVIDER_PERMISSION_ERROR_OR_QUOTA_BEHAVIOR_CLAIMS_FROM_WRAPPER_EMPTY_RESULTS
  - DURABLE_WORKFLOW_REPLAY_RESUME_OR_EXACTLY_ONCE_CLAIMS
adoption_order:
  first: LABEL_AGGREGATES
  second: ID_ONLY_DISCOVERY
  not_admitted: BODY_BEARING_READ_ACTIONS_WITHOUT_EXPLICIT_OPERATOR_OR_WORKITEM_NEED
mandatory_gates:
  - PRIVATE_BODIES_HEADERS_IDS_TOKENS_ATTACHMENTS_AND_EXACT_COUNTS_STAY_IN_SOURCE_SYSTEMS_UNLESS_AN_EXPLICIT_WORKITEM_REQUIRES_THEM
  - PREFER_LABEL_AGGREGATES_OVER_MESSAGE_LISTING_FOR_STATUS_QUESTIONS
  - USE_EXACT_KNOWN_LABEL_NAMES_AND_TREAT_EMPTY_RESULTS_AS_NOT_FOUND_OR_UNKNOWN
  - DO_NOT_INFER_GLOBAL_ABSENCE_PERMISSION_STATE_OR_RAW_GMAIL_FAILURE_CLASS_FROM_EMPTY_SUCCESS
  - LIVE_OAUTH_IDENTITY_SCOPE_TOKEN_TYPE_STORAGE_AND_LEAST_PRIVILEGE_REMAIN_UNKNOWN
  - DO_NOT_DESCRIBE_THE_LIVE_CONNECTOR_AS_GMAIL_METADATA_SCOPED_OR_LEAST_PRIVILEGE
  - CONNECTOR_NAME_FILTER_ENRICHMENT_CALL_SEQUENCE_AND_ACTUAL_QUOTA_COST_REMAIN_HIDDEN
  - LOW_RATE_BOUNDED_CALLS_ONLY_WHILE_PROJECT_QUOTA_BILLING_AND_RETRY_TELEMETRY_ARE_HIDDEN
  - NO_UNBOUNDED_AUTOMATIC_RETRY; RETRYABLE_FAILURES_REQUIRE_BOUNDED_BACKOFF_AND_STOP_CONDITIONS
  - NO_DURABILITY_EXACTLY_ONCE_OR_INDEPENDENT_VERIFICATION_CLAIM
  - DISTINCT_NONPRODUCER_REVIEW_BEFORE_ANY_HIGHER_EFFECT_PRIVACY_PERMISSION_OR_INTERNAL_CALL_SEQUENCE_CLAIM
credentials:
  required_observed: ONE_PREEXISTING_AUTHENTICATED_GMAIL_CONNECTOR
  new_login_or_secret_handling_this_campaign: false
  live_identity: UNKNOWN
  live_scope: UNKNOWN
  token_storage: CONNECTOR_MANAGED_UNINSPECTED
durability: GMAIL_PROVIDER_MAILBOX_DURABILITY_ONLY_NO_WORKFLOW_DURABILITY
observability:
  exposed: ACTION_SUCCESS_OUTPUT_SHAPE_EXTERNAL_CALL_LATENCY_CONNECTOR_AND_ACTION_IDS
  hidden: RAW_HTTP_STATUS_ON_SUCCESS_REQUEST_ID_OAUTH_SCOPE_QUOTA_HEADERS_RETRY_AUDIT_INTERNAL_CALL_SEQUENCE
portability:
  within_gmail_connector: MEDIUM_FOR_THE_MEASURED_ACTIONS
  direct_gmail_api: MEDIUM_WITH_REIMPLEMENTATION_OF_WRAPPER_FILTER_AND_ENRICHMENT
  other_mail_providers: LOW_AND_UNTESTED
failure_behavior:
  measured: ABSENT_EXACT_LABEL_NAME_NORMALIZES_TO_SUCCESS_EMPTY_ARRAY
  unmeasured: AUTH_FAILURE_PERMISSION_FAILURE_RATE_LIMIT_SERVER_ERROR_RETRY_AND_PARTIAL_RESPONSE
custom_code_avoided_estimate:
  label_status: 30_to_100_LOC_UNVALIDATED
  id_discovery: 25_to_80_LOC_UNVALIDATED
  additive_total: NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP
operator_relay_minutes: 0
operator_minutes_removed_estimate: 1_to_3_PER_CONSUMED_STATUS_CHECK_UNVALIDATED
paid_cost_usd_observed: 0
direct_cost_and_quota_limit:
  official_method_units_known: true
  actual_connector_units: NOT_EXPOSED
  actual_project_daily_usage: NOT_EXPOSED
  actual_project_grandfathering_or_new_quota_class: UNKNOWN
  future_pricing_change_risk: MATERIAL_RECHECK_BEFORE_SCALE
strongest_falsifier: A_DISTINCT_REVIEW_OR_DIRECT_CONNECTOR_INSPECTION_SHOWS_THAT_LABEL_AGGREGATES_REQUIRE_BODY_BEARING_READS_OR_EXCESS_HIDDEN_CALLS_OR_A_REPEAT_KNOWN_LABEL_PROBE_RETURNS_EMPTY_WITHOUT_MAILBOX_CHANGE_OR_THE_CONNECTOR_EXPOSES_A_PROVEN_METADATA_ONLY_GET_THAT_CHANGES_THE_ADOPTION_BOUNDARY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_FOR_SCOPE_PRIVACY_PERMISSION_COST_OR_INTERNAL_CALL_SEQUENCE_CLAIMS
consumer: S05_OPERATOR_RELIEF_CELL_AND_RATATOSKR
consumer_ack: NOT_OBSERVED
fitness_credit: 0_UNTIL_CONSUMED_BY_A_WORKITEM
review_expiry_utc: 2026-08-08T12:48:17Z
honest_flaw: THE_DECISION_RESTS_ON_THREE_SMALL_SAME_PROVIDER_PROBES_AND_OFFICIAL_RAW_API_DOCUMENTATION; IT_DOES_NOT_INSPECT_THE_CONNECTOR_IMPLEMENTATION_LIVE_OAUTH_SCOPE_TRUE_CALL_COUNT_PROJECT_QUOTA_CLASS_OR_REAL_AUTH_RATE_LIMIT_AND_SERVER_FAILURES
campaign_result: ADOPT_WITH_GATES
campaign_status: COMPLETE
next_campaign:
  experiment_id: X13_GOOGLE_CALENDAR_READONLY_CONNECTOR_001
  candidate: Calendar_read_only_event_search_and_free_busy_connector
  next_phase: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
sealed: true
---

# X13 Gmail connector phase 4 — adopt with gates

Adopt only the measured low-effect surfaces: exact known-label aggregate status first, and bounded
message-ID discovery only when aggregates cannot answer the question. These two paths can remove a
small mailbox-opening or pagination step without custom Gmail code, but their estimated savings have
not yet been validated by a consumed WorkItem.

Do not treat the connector as a general message-metadata surface. The exposed message-read action
lacks explicit Gmail `format=METADATA` and selected-header controls, while the live OAuth identity,
scope, token storage, raw HTTP responses, quota telemetry, enrichment call sequence, and retry audit
remain hidden. Body-bearing reads, attachments, bulk mining, and high-rate polling are not admitted.

The absent-label probe is a connector-boundary behavior only: an empty success means `not found or
unknown`. It does not establish permission state, global absence, raw Gmail error behavior, or exact
provider cost. Official Gmail pricing and quota documentation now includes a daily billing threshold
and says charging above request limits is planned later in 2026, so cost assumptions must be rechecked
before scale.

This decision is same-provider advisory evidence with binding weight zero. Fitness credit remains zero
until S05 or another WorkItem consumes the capability and records measured operator relief.
