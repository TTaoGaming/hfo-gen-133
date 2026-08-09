---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_MESSAGE_ID_SEARCH_READONLY_026
event_type: PHASE2_PREFLIGHT
phase: 2
campaign_wake: 2_of_4
expected_current_version: 201
next_current_version_if_accepted: 202
candidate: Gmail_search_email_ids_readonly
wip: 1
request_preimage_canonical_json: '{"label_ids":["INBOX"],"max_results":5,"next_page_token":"","query":"newer_than:30d -in:spam -in:trash","tool":"Gmail.search_email_ids"}'
request_sha256: a2b11d537fd576e1e837039c744a551638c0ce4bff25fa9cc857e0a0f06d745b
phase1_request_sha256_expected: a2b11d537fd576e1e837039c744a551638c0ce4bff25fa9cc857e0a0f06d745b
phase1_request_digest_match: true
request_scope: EXACT_PHASE1_REPLAY_BOUNDED_ID_ONLY_SEARCH_NO_MESSAGE_BODY_OR_ATTACHMENT_HYDRATION
persist_policy: PERSIST_ONLY_COUNT_PAGE_TOKEN_PRESENCE_ORDERED_ID_DIGEST_AND_NONCONTENT_TOOL_METADATA;DO_NOT_PERSIST_RAW_MESSAGE_IDS_THREAD_IDS_SUBJECTS_SENDERS_SNIPPETS_BODIES_ATTACHMENTS_OR_TOKENS
mutation_allowed: false
retries_allowed_this_wake: 0
fallbacks_allowed_this_wake: 0
comparison_fields: RESULT_COUNT;NEXT_PAGE_TOKEN_PRESENCE;ORDERED_MESSAGE_ID_SHA256
mailbox_drift_policy: RELATIVE_30_DAY_QUERY_CAN_DRIFT;COUNT_OR_DIGEST_CHANGE_IS_MEASURED_VARIANCE_NOT_AUTOMATIC_FAILURE_IF_BOUND_AND_CONTRACT_HOLD
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 30_to_90_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
credentials: GMAIL_CONNECTOR_MANAGED_EFFECTIVE_OAUTH_SCOPE_PRINCIPAL_AND_CLOUD_PROJECT_UNKNOWN
consumer: HFO_BOUNDED_MAILBOX_DISCOVERY_AND_PREFLIGHT_FILTERING
strongest_falsifier: EXACT_REPLAY_FAILS_NONINTERACTIVELY_OR_VIOLATES_MAX_RESULTS_OR_PAGE_TOKEN_CONTRACT_WITHOUT_EXPLANATION
honest_flaw: RELATIVE_WINDOW_AND_LIVE_MAILBOX_MEAN_ORDERED_DIGEST_REPEATABILITY_IS_NOT_A_STABILITY_GUARANTEE
valid_time_utc: 2026-08-09T06:47:00Z
recorded_time_utc: 2026-08-09T06:47:00Z
---

# X13 Phase 2 Preflight — Gmail message-ID search exact replay

The Phase-1 request was read back from canonical Git state and its canonical JSON SHA-256 independently recomputed as `a2b11d537fd576e1e837039c744a551638c0ce4bff25fa9cc857e0a0f06d745b`, matching the durable Phase-1 preflight.

This wake permits exactly one Gmail connector call using the same request, no retries or fallbacks, no content hydration, and no Gmail mutation. Only result count, next-page-token presence, wrapper metadata, and a privacy-safe ordered message-ID digest may be persisted.

Because `newer_than:30d` and the mailbox are live, a changed digest is allowed as measured mailbox variance; it does not by itself falsify the connector contract.