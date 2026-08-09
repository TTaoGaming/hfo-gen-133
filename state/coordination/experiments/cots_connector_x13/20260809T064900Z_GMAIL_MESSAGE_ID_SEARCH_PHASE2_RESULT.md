---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_MESSAGE_ID_SEARCH_READONLY_026
event_type: PHASE2_RESULT
phase: 2
campaign_wake: 2_of_4
expected_current_version: 201
next_current_version: 202
candidate: Gmail_search_email_ids_readonly
phase_status: PHASE2_ACCEPTED_WITH_GATES
wip: 1
phase2_preflight_commit: ce68e6a6fedad954ecb5a4dbf0132a2398ffa572
phase2_preflight_blob_sha: 4c9964973e9bc18e6c241ce9c5b06c32369e120c
phase2_preflight_readback: true
candidate_invocations_total: 2
usable_candidate_results: 2
result_count: 5
phase1_result_count: 5
result_count_match_phase1: true
next_page_token_present: true
next_page_token_presence_match_phase1: true
ordered_message_id_sha256: 55886e1c075eb5b19ebbf4034601148f6b84c0826f4bb1385f0def01ce05257c
ordered_message_id_digest_match_phase1: true
raw_message_ids_persisted: false
raw_page_token_persisted: false
content_hydrations_total: 0
connector_errors_total: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
external_call_time_ms: 656
phase1_external_call_time_ms: 281
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 30_to_90_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READ_ONLY;ID_ONLY;BOUNDED_MAX_RESULTS;NO_CONTENT_HYDRATION;NO_RAW_MAILBOX_IDENTIFIERS_IN_X13_RECEIPTS;NO_COMPLETENESS_OR_STABLE_ORDER_INFERENCE_FROM_CAPPED_PAGE
honest_flaw: TWO_MATCHING_CAPPED_PAGES_DO_NOT_PROVE_STABLE_ORDERING_OR_COMPLETENESS;RELATIVE_WINDOW_CAN_DRIFT;PAGINATION_AND_FAILURE_BEHAVIOR_REMAIN_UNVERIFIED
next_phase: PHASE3_ONE_BOUNDED_HARMLESS_NONMUTATING_VARIANCE_PROBE
valid_time_utc: 2026-08-09T06:49:00Z
recorded_time_utc: 2026-08-09T06:49:00Z
---

# X13 Phase 2 Result — Gmail message-ID search

The exact Phase-1 request was replayed once. It again returned 5 results at the requested cap and a next-page token. The privacy-safe ordered-result digest exactly matched Phase 1. Wrapper time was 656 ms versus 281 ms in Phase 1.

No raw mailbox identifiers or page tokens were persisted in this receipt. No content hydration, retry, fallback, or mailbox mutation was requested or observed.

Phase 2 is accepted with gates. The two matching capped pages establish bounded repeatability for these observations only, not completeness or guaranteed ordering. Next wake: one bounded harmless read-only Phase-3 variance/failure probe.