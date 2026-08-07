---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_ID_ONLY_SEARCH_READONLY_017
expected_prior_current_version: 165
candidate: Gmail_search_email_ids_bounded_query
campaign_wake: 2_of_4
phase: 2
phase_status: PHASE2_BLOCKED_ANDON_REQUEST_PREIMAGE_NOT_DURABLE
wip: 1
candidate_calls_this_wake: 0
campaign_calls_total: 1
successful_nonempty_calls: 1
successful_empty_calls: 0
connector_errors_observed: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
phase1_max_results: 3
phase1_returned_message_ids_count: 3
phase1_next_page_token_present: true
phase1_request_digest_sha256: 91fa1bb6bba78deada9b4d1097a9082a56d4a76ff2b6e5d0b04b63580c1263bd
phase1_ordered_message_id_digest_sha256: 6ccac4a570c0d9375ed10f43b45eb71e139b8db12684857dd4dfa2acf44cd26d
phase1_exact_query_preimage_persisted: false
phase1_canonical_request_bytes_persisted: false
phase1_request_canonicalization_algorithm_persisted: false
identical_phase2_replay_provable: false
speculative_gmail_probe_issued: false
message_body_hydration_this_wake: false
message_header_hydration_this_wake: false
thread_id_hydration_this_wake: false
raw_message_ids_persisted_in_receipt: false
raw_next_page_token_persisted_in_receipt: false
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_PAID_COST_SURFACED
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR_THIS_WAKE
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPES_UNKNOWN
durability: GIT_EVENT_DURABLE;PHASE1_GMAIL_REQUEST_PREIMAGE_NOT_DURABLE
observability: PHASE1_COUNT_TOKEN_PRESENCE_DIGEST_AND_LATENCY_ARE_DURABLE_BUT_EXACT_QUERY_AND_CANONICAL_REQUEST_BYTES_ARE_NOT;PROVIDER_REQUEST_ID_RATE_HEADERS_EFFECTIVE_SCOPE_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_LIST_AND_PAGINATION_CONCEPTS_PORTABLE;GMAIL_QUERY_SYNTAX_MESSAGE_IDS_AND_SCOPE_MODEL_GOOGLE_SPECIFIC
failure_behavior: EXPERIMENT_CONTROL_PLANE_REPLAYABILITY_FAILURE_NOT_A_GMAIL_CONNECTOR_FAILURE;NO_GMAIL_CALL_ISSUED_THIS_WAKE
verifier: GITHUB_READBACK_OF_AUTHORITATIVE_PHASE1_CORRECTION_AND_CURRENT;NO_PROVIDER_REPLAY_CLAIM
consumer: GMAIL_DISCOVERY_CANDIDATE_NO_OPERATIONAL_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
mandatory_gate: DO_NOT_CLAIM_IDENTICAL_REPLAY_WITHOUT_DURABLE_EXACT_REQUEST_PREIMAGE_AND_CANONICALIZATION;READONLY_SEARCH_EMAIL_IDS_ONLY;SMALL_MAX_RESULTS;DO_NOT_PERSIST_RAW_MESSAGE_IDS_OR_PAGE_TOKENS;NEXT_PAGE_TOKEN_MEANS_FIRST_PAGE_IS_NOT_COMPLETE;DO_NOT_INFER_MAILBOX_WIDE_ABSENCE_OR_COMPLETENESS;DO_NOT_FETCH_MESSAGE_CONTENT_UNLESS_SEPARATELY_JUSTIFIED;EFFECTIVE_OAUTH_SCOPE_MUST_BE_TREATED_UNKNOWN;LEAST_DATA_OUTPUT_IS_NOT_EVIDENCE_OF_LEAST_PRIVILEGE_AUTHORIZATION;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED_NOT_AS_ABSENCE
strongest_falsifier: AN_AUTHORITATIVE_PRIOR_TOOL_RECEIPT_OR_OTHER_DURABLE_SOURCE_RECOVERS_THE_EXACT_PHASE1_GMAIL_SEARCH_ARGUMENTS_AND_CANONICALIZATION_SUFFICIENT_TO_RECOMPUTE_REQUEST_DIGEST_91fa1bb6bba78deada9b4d1097a9082a56d4a76ff2b6e5d0b04b63580c1263bd_BYTE_FOR_BYTE
honest_flaw: THIS_WAKE_TESTED_EVIDENCE_REPLAYABILITY_NOT_GMAIL_CONNECTOR_REPEATABILITY;NO_GMAIL_PROVIDER_CALL_WAS_ISSUED;PHASE2_RESULT_REPEATABILITY_REMAINS_UNKNOWN;THE_MISSING_PREIMAGE_IS_AN_X13_RECEIPT_DESIGN_FLAW_NOT_EVIDENCE_AGAINST_GMAIL
next_phase: PHASE3_ONE_BOUNDED_SYNTHETIC_NONMATCHING_ID_ONLY_SEARCH_NO_RETRY_NO_MAILBOX_WIDE_ABSENCE_CLAIM
valid_time_utc: 2026-08-07T18:50:00Z
recorded_time_utc: 2026-08-07T18:50:00Z
---

# X13 Gmail ID-only search — Phase 2 replayability Andon

Phase 2 was supposed to issue one identical bounded `Gmail.search_email_ids` replay and compare the ordered message-ID digest with Phase 1. The authoritative Phase-1 correction receipt and `CURRENT v165` retain only a one-way request digest plus the description “generic recent-mail query”; they do **not** retain the exact query string, canonical request bytes, or the request canonicalization algorithm.

Because the exact Phase-1 request cannot be reconstructed byte-for-byte from durable state, an “identical replay” claim would be unprovable. No speculative Gmail search was issued this wake. This avoids converting a guessed query into false repeatability evidence and avoids consuming connector quota for an experiment whose input identity cannot be verified.

## Measured Andon

- Phase-1 exact query preimage durable: **false**
- Phase-1 canonical request bytes durable: **false**
- Phase-1 request canonicalization algorithm durable: **false**
- Phase-1 one-way request digest durable: **true**
- Identical Phase-2 replay provable from canonical state: **false**
- Gmail candidate calls this wake: **0**
- Gmail mutations this wake: **0**
- Campaign Gmail calls remain: **1**

This is an X13 experiment-control-plane failure, not a Gmail connector failure. The prior Phase-1 connector observation remains valid on its own terms: one bounded ID-only search returned three IDs plus a continuation token without content hydration. What is not supported is the planned cross-wake identical-request repeatability claim.

## Measures

Custom-code avoidance remains `40_to_120_LOC_UNVALIDATED`; measured operator minutes removed remain `0`; direct connector quota debit/cost evidence remains absent; effective principal/scopes remain unknown. Durability is now explicitly split: the Git observation receipt is durable, while the exact request needed to reproduce it is not.

## Strongest falsifier

Recover an authoritative prior tool receipt or other durable source containing the exact Phase-1 Gmail search arguments and canonicalization, then recompute the stored request digest `91fa1bb6bba78deada9b4d1097a9082a56d4a76ff2b6e5d0b04b63580c1263bd` byte-for-byte. Without that, identical replay must remain unknown.

## Honest flaw

No Gmail connector behavior was probed this wake. This receipt measures the reproducibility of X13’s evidence, not Gmail search stability. The missing request preimage is a lab-receipt design defect and must not be misreported as connector instability.

## Next

Proceed to Phase 3 with one bounded synthetic nonmatching ID-only query whose exact privacy-safe request descriptor is durable before the call. No retry and no mailbox-wide absence claim.