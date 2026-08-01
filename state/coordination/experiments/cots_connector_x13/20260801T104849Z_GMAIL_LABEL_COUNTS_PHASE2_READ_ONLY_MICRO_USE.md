---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_READONLY_CONNECTOR_001
phase: 2
phase_name: SMALLEST_HARMLESS_READ_ONLY_MICRO_USE
campaign_wake: 2_of_4
expected_prior_version: 13
next_version: 14
candidate: Gmail_read_only_search_and_message_metadata_connector
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUNTIME_PROMPT
native_task_inventory_read_this_wake: false
wip: 1
valid_time_utc: 2026-08-01T10:48:49Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
evidence_class:
  - DIRECT_GMAIL_CONNECTOR_RECEIPT
  - OFFICIAL_GOOGLE_GMAIL_API_DOCUMENTATION
  - SAME_PROVIDER_NONBINDING_PREFLIGHT
binding_weight: 0
effect_ceiling: ONE_BOUNDED_READ_ONLY_INBOX_LABEL_AGGREGATE_CALL_NO_MESSAGE_READ_NO_WRITE
connector_action: Gmail.list_labels
connector_filter: INBOX_ONLY
connector_authenticated: true
external_call_time_ms: 505
call_succeeded: true
returned_label_count: 1
returned_label_identity: INBOX_SYSTEM_LABEL
aggregate_fields_present:
  - messagesTotal
  - messagesUnread
  - threadsTotal
  - threadsUnread
aggregate_values_externalized: false
aggregate_invariants_checked:
  messages_unread_lte_messages_total: true
  threads_unread_lte_threads_total: true
message_ids_returned: false
headers_returned: false
bodies_returned: false
attachments_returned: false
write_effect_observed: false
operator_relay_minutes: 0
operator_minutes_removed_estimate: 1_to_3_PER_STATUS_CHECK_UNVALIDATED
custom_code_avoided_estimate: 30_to_100_LOC_FOR_LABEL_DISCOVERY_FILTERING_DETAIL_FETCH_AND_COUNT_NORMALIZATION_UNVALIDATED
credentials_required_observed: ONE_PREEXISTING_AUTHENTICATED_GMAIL_CONNECTOR_NO_NEW_LOGIN_OR_SECRET_HANDLING
paid_cost_usd_observed: 0
direct_quota_units_observed: NOT_EXPOSED
official_labels_list_quota_units: 1
official_pricing_state_as_of_2026_06_03: STANDARD_USE_NO_ADDITIONAL_COST_BELOW_DAILY_THRESHOLD_FUTURE_CHARGING_PLANNED_LATER_2026
quota_caveat: CONNECTOR_RETURNS_COUNT_FIELDS_NOT_PROMISED_BY_RAW_LABELS_LIST_RESPONSE_SO_UNDERLYING_CALL_SEQUENCE_AND_ACTUAL_QUOTA_UNITS_ARE_HIDDEN
durability: GMAIL_PROVIDER_MAILBOX_STATE_ONLY_NO_WORKFLOW_REPLAY_RESUME_OR_EXACTLY_ONCE_CLAIM
observability: SUCCESS_AGGREGATE_FIELD_PRESENCE_LATENCY_CONNECTOR_AND_ACTION_IDS_EXPOSED_SCOPE_RAW_HTTP_QUOTA_RETRY_AUDIT_AND_INTERNAL_CALL_SEQUENCE_HIDDEN
portability: MEDIUM_TO_GMAIL_API_LOW_TO_OTHER_MAIL_PROVIDERS_UNTESTED
failure_behavior: NOT_PROBED_IN_PHASE2
privacy_result: AGGREGATE_STATUS_OBTAINED_WITHOUT_MESSAGE_IDS_HEADERS_BODIES_OR_EXACT_PRIVATE_COUNTS_WRITTEN_TO_GIT_OR_SLACK
official_contract_findings:
  - users_labels_list_accepts_gmail_metadata_gmail_readonly_gmail_labels_gmail_modify_or_full_mail_scope
  - raw_users_labels_list_documentation_says_list_items_only_include_id_name_visibility_and_type
  - detailed_count_fields_belong_to_the_Label_resource_and_may_require_labels_get
  - labels_list_official_quota_cost_is_1_UNIT_PER_REQUEST
  - live_connector_scope_and_actual_multi_call_quota_cost_are_not_exposed
mandatory_gates:
  - PREFER_LABEL_AGGREGATES_OVER_MESSAGE_LISTING_FOR_COUNT_OR_STATUS_QUESTIONS
  - NO_EXACT_PRIVATE_COUNTS_MESSAGE_IDS_HEADERS_OR_BODIES_EXTERNALIZATION
  - LIVE_SCOPE_UNKNOWN_MUST_NOT_BE_DESCRIBED_AS_LEAST_PRIVILEGE
  - CONNECTOR_ENRICHMENT_CALL_SEQUENCE_AND_ACTUAL_QUOTA_COST_UNKNOWN
  - LOW_RATE_BOUNDED_CALLS_WHILE_LIVE_QUOTA_AND_BILLING_CLASS_ARE_HIDDEN
  - NO_DURABILITY_OR_EXACTLY_ONCE_CLAIM
  - DISTINCT_NONPRODUCER_BEFORE_HIGHER_EFFECT_OR_PRIVACY_CLAIM
strongest_falsifier: A_REPEAT_INBOX_LABEL_STATUS_CALL_WITHOUT_MAILBOX_CHANGE_RETURNS_STRUCTURALLY_INCONSISTENT_AGGREGATES_OR_DIRECT_INSPECTION_SHOWS_THE_CONNECTOR_READS_MESSAGE_BODIES_TO_COMPUTE_COUNTS
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_FOR_SCOPE_PRIVACY_OR_UNDERLYING_CALL_SEQUENCE_CLAIMS
consumer: X13_PHASE3_AND_RATATOSKR
consumer_ack: NOT_OBSERVED
review_expiry_utc: 2026-08-08T10:48:49Z
honest_flaw: THE_OUTPUT_PROVES_A_PRIVACY_PRESERVING_AGGREGATE_RESULT_AT_THE_CONNECTOR_BOUNDARY_BUT_NOT_THE_CONNECTORS_INTERNAL_DATA_MINIMIZATION_OAUTH_SCOPE_CALL_SEQUENCE_OR_TRUE_QUOTA_COST
phase_result: ACCEPT_PHASE2
next_phase: PHASE3_FAILURE_PERMISSION_PORTABILITY_AND_CONNECTOR_VARIANCE_PROBE
sealed: true
---

# X13 Gmail connector phase 2 — aggregate status micro-use

One bounded `Gmail.list_labels` call filtered to the system `INBOX` label succeeded in 505 ms.
The connector returned the label plus four aggregate status fields. The exact private counts remain
inside the connector receipt and were not copied to Git or Slack. No message ID, header, body,
attachment, or mailbox write was returned or performed.

This is a smaller and more privacy-preserving COTS path for inbox-status questions than paging
through message IDs. It can remove a small manual Gmail-opening step without custom mailbox code.
The estimate is not yet validated by a consumed WorkItem.

## Contract and variance finding

Google documents `users.labels.list` as a read-only label listing method and permits the
`gmail.metadata` scope among others. However, the raw `labels.list` response is documented as
containing only label identity and visibility fields; detailed aggregate counts are fields on the
Label resource and can be obtained through `labels.get`. The connector exposes the counts in one
action but does not reveal whether it performs enrichment calls, what live OAuth scope it holds,
or the actual quota units consumed.

Official sources checked on 2026-08-01:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels/list
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels
- https://developers.google.com/workspace/gmail/api/reference/quota

Phase 2 is accepted only at the connector-output boundary. It is not evidence of least privilege,
internal data minimization, exact one-unit cost, workflow durability, or independent verification.
