---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_MESSAGE_ID_SEARCH_READONLY_026
event_type: PHASE1_PREFLIGHT
phase: 1
campaign_wake: 1_of_4
expected_current_version: 200
next_current_version_if_accepted: 201
candidate: Gmail_search_email_ids_readonly
wip: 1
request_preimage_canonical_json: '{"label_ids":["INBOX"],"max_results":5,"next_page_token":"","query":"newer_than:30d -in:spam -in:trash","tool":"Gmail.search_email_ids"}'
request_sha256: a2b11d537fd576e1e837039c744a551638c0ce4bff25fa9cc857e0a0f06d745b
request_scope: BOUNDED_ID_ONLY_SEARCH_NO_MESSAGE_BODY_OR_ATTACHMENT_HYDRATION
persist_policy: PERSIST_ONLY_COUNT_PAGE_TOKEN_PRESENCE_ORDERED_ID_DIGEST_AND_NONCONTENT_TOOL_METADATA;DO_NOT_PERSIST_RAW_MESSAGE_IDS_THREAD_IDS_SUBJECTS_SENDERS_SNIPPETS_BODIES_ATTACHMENTS_OR_TOKENS
mutation_allowed: false
retries_allowed_this_wake: 0
fallbacks_allowed_this_wake: 0
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 30_to_90_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
credentials: GMAIL_CONNECTOR_MANAGED_EFFECTIVE_OAUTH_SCOPE_PRINCIPAL_AND_CLOUD_PROJECT_UNKNOWN
consumer: HFO_BOUNDED_MAILBOX_DISCOVERY_AND_PREFLIGHT_FILTERING
strongest_falsifier: BOUNDED_SEARCH_FAILS_NONINTERACTIVELY_OR_RETURNS_RESULTS_INCONSISTENT_WITH_THE_DECLARED_QUERY_LABEL_OR_MAX_RESULTS_CONTRACT
honest_flaw: PHASE1_CANNOT_PROVE_COMPLETENESS_STABLE_ORDERING_PAGINATION_PERMISSION_DENIAL_RATE_LIMITING_EFFECTIVE_SCOPE_OR_QUOTA_DEBIT
valid_time_utc: 2026-08-09T05:52:00Z
recorded_time_utc: 2026-08-09T05:52:00Z
---

# X13 Phase 1 Preflight — Gmail message-ID search

Candidate: the native Gmail connector's read-only `search_email_ids` surface for bounded mailbox discovery without content hydration.

Exact request is frozen above and hashed before invocation. This wake permits one connector call only, no retries or fallbacks, and no Gmail mutation. Raw mailbox identifiers and content will not be persisted into X13 receipts.

Official native baseline checked before invocation: Gmail API `users.messages.list` is a GET list operation; it accepts `maxResults`, `pageToken`, `q`, and `labelIds`, returns message IDs/thread IDs plus optional `nextPageToken` and an estimated result size, and supports Gmail read scopes. The connector's exact native mapping and effective OAuth scope remain unproven until direct evidence surfaces.