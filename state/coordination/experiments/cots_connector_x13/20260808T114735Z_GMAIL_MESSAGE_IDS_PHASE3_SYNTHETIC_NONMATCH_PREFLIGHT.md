---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_MESSAGE_IDS_SEARCH_READONLY_021
event_type: PHASE3_SYNTHETIC_NONMATCH_REQUEST_PREFLIGHT
candidate: Gmail_search_email_ids
phase: 3
wip: 1
expected_current_version: 182
canonical_branch: agent/gen133-bootstrap-20260730
mutation_surface: GitHub
surface_owner: X13_COTS_CONNECTOR_PDCA_LAB
permission_basis: OPERATOR_DIRECTED_GIT_FIRST_IMMUTABLE_EXPERIMENT_EVENT
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_privacy_safe: true
request_descriptor_exact: '{"label_ids":null,"max_results":3,"next_page_token":"","query":"subject:\"__HFO_X13_SYNTHETIC_NONMATCH_20260808T114735Z_6b4d0f7c__\" -in:spam -in:trash"}'
request_descriptor_sha256: 256af453455d451eb193ce55eb08eef06cb9d4a6d07cd00abc576d53e05c0333
request_hash_must_be_recomputed_before_candidate_call: true
result_digest_subject: ORDERED_MESSAGE_IDS_ONLY
result_digest_canonicalization: UTF8_JSON_ARRAY_COMPACT_ORDERED_NO_ASCII_ESCAPING
empty_result_canonical_bytes_utf8: '[]'
empty_result_digest_sha256_reference: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
request_intent: BOUNDED_READONLY_SYNTHETIC_NONMATCH_MESSAGE_ID_DISCOVERY_ONLY
interpretation_gate: EMPTY_SUCCESS_IS_DISTINCT_FROM_ERROR_BUT_IS_NOT_MAILBOX_WIDE_ABSENCE_OR_AUTHORIZATION_COMPLETENESS
mutation_allowed: false
message_content_fetch_allowed: false
attachment_fetch_allowed: false
send_allowed: false
retry_allowed: false
valid_time_utc: 2026-08-08T11:47:35Z
recorded_time_utc: 2026-08-08T11:47:35Z
---

# X13 Gmail message-ID search Phase 3 synthetic nonmatch preflight

The exact privacy-safe request preimage and the ordered-message-ID result canonicalization are persisted before the candidate call. This wake is permitted one bounded ID-only Gmail search and no retry.

Exact connector request:

```json
{"label_ids":null,"max_results":3,"next_page_token":"","query":"subject:\"__HFO_X13_SYNTHETIC_NONMATCH_20260808T114735Z_6b4d0f7c__\" -in:spam -in:trash"}
```

The synthetic subject token is intentionally improbable and carries no user mailbox content. If the connector returns zero IDs without error, the only admissible claim is that this bounded synthetic query produced an empty success. It is not evidence that the mailbox lacks any real class of messages, that search is complete, or that authorization covers the mailbox.

Before invoking Gmail, the runner must read this artifact back and independently recompute the request SHA-256 over the declared canonical request bytes. The result digest, if any, must use `UTF8_JSON_ARRAY_COMPACT_ORDERED_NO_ASCII_ESCAPING` over the ordered message-ID array only. Raw message IDs and page tokens must not be persisted in X13 receipts.
