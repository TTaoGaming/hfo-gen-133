---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_READONLY_CONNECTOR_001
campaign_wake: 1_of_4
phase: 1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
status: PHASE1_BASELINE_ACCEPTED_WITH_METADATA_GAP
candidate: Gmail_read_only_search_and_message_metadata_connector
carrier: X13_COTS_AND_CONNECTOR_PDCA_LAB
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUNTIME_PROMPT
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version: 12
next_current_version: 13
valid_time_utc: 2026-08-01T09:47:05Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
effect_ceiling: OFFICIAL_DOC_READ_PLUS_ONE_BOUNDED_GMAIL_ID_LIST_NO_BODY_NO_WRITE
self_probe:
  exposed_tools:
    - GitHub_fetch_search_create_update
    - Gmail_search_email_ids_and_body_read_actions
    - Slack_pointer_write
    - web_official_document_research
  native_task_inventory_read: false
official_contract:
  messages_list:
    reference: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
    last_updated_utc: 2026-04-15
    returns: MESSAGE_ID_AND_THREAD_ID_ONLY_PLUS_PAGE_TOKEN_AND_RESULT_SIZE_ESTIMATE
    q_with_gmail_metadata_scope: NOT_ALLOWED
    authorization_scopes_include:
      - gmail.metadata
      - gmail.readonly
      - gmail.modify
      - mail.google.com
  messages_get:
    reference: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/get
    last_updated_utc: 2026-04-15
    metadata_contract: FORMAT_METADATA_WITH_OPTIONAL_METADATA_HEADERS
  scopes:
    reference: https://developers.google.com/workspace/gmail/api/auth/scopes
    last_updated_utc: 2026-06-03
    gmail_metadata_class: RESTRICTED
    gmail_readonly_class: RESTRICTED
  quota:
    reference: https://developers.google.com/workspace/gmail/api/reference/quota
    observed_document_state_date: 2026-08-01
    messages_list_quota_units_per_request: 5
    live_connector_quota_counter: NOT_EXPOSED
    live_connector_billing_class: NOT_EXPOSED
exact_probe:
  action: Gmail.search_email_ids
  arguments:
    query: EMPTY_STRING
    label_ids:
      - INBOX
    max_results: 1
  privacy_rule: DO_NOT_EXTERNALIZE_RETURNED_MESSAGE_ID_OR_PAGE_TOKEN
measured_result:
  authenticated_call_succeeded: true
  returned_message_id_count: 1
  next_page_token_present: true
  message_body_returned: false
  message_headers_returned: false
  external_call_time_ms: 356
  connector_id_exposed: true
  connector_action_name_exposed: true
  raw_http_status_exposed_on_success: false
  oauth_identity_exposed: false
  oauth_scope_exposed: false
  quota_headers_exposed: false
permission_error_class: AUTHENTICATED_SUCCESS_LIVE_SCOPE_UNKNOWN
connector_variance_fact: CONNECTOR_EXPOSES_ID_ONLY_SEARCH_BUT_NO_METADATA_ONLY_GET_CONTROL; AVAILABLE_READ_EMAIL_ACTION_RETURNS_BODY
credentials:
  connector_authenticated: true
  operator_login_required_this_wake: false
  token_identity: UNKNOWN
  token_scope: UNKNOWN
  token_storage: CONNECTOR_MANAGED_UNINSPECTED
durability: MAILBOX_PROVIDER_DURABILITY_ONLY_NO_WORKFLOW_REPLAY_RESUME_OR_EXACTLY_ONCE_CLAIM
observability: MESSAGE_COUNT_PAGE_TOKEN_PRESENCE_LATENCY_CONNECTOR_AND_ACTION_IDS_EXPOSED; RAW_HTTP_REQUEST_ID_SCOPE_QUOTA_RETRY_AND_AUDIT_HIDDEN
portability: MEDIUM_TO_GMAIL_API_LOW_TO_OTHER_MAIL_PROVIDERS_UNTESTED
failure_behavior: NOT_PROBED_IN_PHASE1
direct_cost_quota_evidence:
  incremental_paid_cost_usd_observed: 0
  official_messages_list_quota_units: 5
  actual_project_quota_consumption_receipt: NOT_EXPOSED
custom_code_avoided_estimate: 25_to_80_LOC_FOR_BASIC_ID_LIST_AND_PAGINATION_WRAPPER_UNVALIDATED
operator_relay_minutes: 0
operator_minutes_removed_estimate: 1_to_3_PER_BOUNDED_ID_DISCOVERY_UNVALIDATED
supported_claims:
  - ONE_BOUNDED_INBOX_ID_LIST_SUCCEEDED_WITHOUT_BODY_RETURN
  - CONNECTOR_EXPOSED_356_MS_EXTERNAL_CALL_TIME
  - OFFICIAL_GMAIL_LIST_CONTRACT_RETURNS_IDS_AND_THREAD_IDS_ONLY
  - OFFICIAL_Q_PARAMETER_IS_INCOMPATIBLE_WITH_GMAIL_METADATA_SCOPE
excluded_claims:
  - LIVE_TOKEN_USES_GMAIL_METADATA_OR_ANY_LEAST_PRIVILEGE_SCOPE
  - CONNECTOR_CAN_FETCH_HEADERS_WITHOUT_BODY
  - QUERY_SEARCH_IS_AVAILABLE_UNDER_METADATA_SCOPE
  - NO_PRIVATE_BODY_CAN_BE_RETURNED_BY_OTHER_CONNECTOR_ACTIONS
  - DURABLE_WORKFLOW_OR_EXACTLY_ONCE_BEHAVIOR
  - ZERO_COST_BEYOND_THIS_OBSERVED_NO_SPEND_WAKE
strongest_falsifier: A_METADATA_ONLY_MESSAGE_GET_WITH_EXPLICIT_FORMAT_AND_HEADER_CONTROLS_IS_EXPOSED_AND_PROVEN_OR_THE_SAME_BOUNDED_ID_LIST_FAILS_WITHOUT_MAILBOX_OR_AUTH_CHANGE
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_FOR_SCOPE_OR_PRIVACY_CLAIMS
consumer: X13_PHASE2_AND_RATATOSKR
consumer_ack: NOT_OBSERVED
expiry_utc: 2026-08-08T09:47:05Z
honest_flaw: ONE_SUCCESSFUL_ID_LIST_PROVES_ONLY_CURRENT_CONNECTOR_REACHABILITY; LIVE_SCOPE_IS_HIDDEN_AND_THE_EXPOSED_CONNECTOR_HAS_NO_METADATA_ONLY_GET_CONTROL, SO MESSAGE_METADATA_ADOPTION_IS_NOT_YET_SUPPORTED
next_phase: PHASE2_SMALLEST_HARMLESS_READ_ONLY_MICRO_USE_WITH_NO_BODY_EXTERNALIZATION
same_provider_binding_weight: 0
---

# X13 Gmail connector phase 1 baseline

The direct connector returned one Inbox message ID and a pagination token without returning
headers or body content. The exact identifier values remain only in the source-system tool
receipt and are intentionally absent from Git and Slack.

Official Gmail documentation separates ID listing from message retrieval. `messages.list`
returns IDs and thread IDs; `messages.get` supports a metadata format and selected headers.
The current connector exposes an ID-only search action, but its message-read action returns
the body and does not expose Gmail's `format=METADATA` or `metadataHeaders` controls.
Therefore, ID discovery is directly measured, while least-privilege message-metadata fetch
remains unproven.

This is same-provider, nonbinding evidence with binding weight zero.
