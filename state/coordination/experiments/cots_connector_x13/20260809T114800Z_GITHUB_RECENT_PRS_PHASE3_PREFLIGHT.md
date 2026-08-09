---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_RECENT_PRS_READONLY_027
event_type: PHASE3_PREFLIGHT
expected_current_version: 206
planned_next_version: 207
candidate: GitHub_get_users_recent_prs_in_repo_readonly
campaign_wake: 3_of_4
wip: 1
probe_class: BOUNDED_HARMLESS_FAILURE_AND_ERROR_MAPPING
request_canonical_json: '{"include_comments":false,"include_diff":false,"limit":1,"repository_full_name":"TTaoGaming/__x13_nonexistent_repo_027__","state":"all"}'
request_sha256: 991a9f8879ee0e4ef498a99d68466dcfdc53c3d8360ecfed32ceef343d09e9c5
safety: READ_ONLY;NONEXISTENT_REPOSITORY_NAME;LIMIT_1;NO_DIFF;NO_COMMENTS;NO_PR_MUTATION;NO_RETRY;NO_FALLBACK
privacy_gate: DO_NOT_PERSIST_ANY_PR_BODY_OR_COMMENT_TEXT_IF_CONNECTOR_UNEXPECTEDLY_RETURNS_RESULTS
purpose: TEST_CONNECTOR_FAILURE_MAPPING_FOR_A_CLEARLY_NONEXISTENT_REPOSITORY_WITHOUT_TOUCHING_CANONICAL_REPO_STATE
verifier: GITHUB_PREFLIGHT_READBACK_THEN_ONE_DIRECT_CONNECTOR_INVOCATION
consumer: HFO_X13_PHASE4_DECISION
valid_time_utc: 2026-08-09T11:48:00Z
recorded_time_utc: 2026-08-09T11:48:00Z
---

# Phase 3 preflight

One read-only failure-path probe is authorized only after this event is read back and its canonical request SHA-256 is verified. The probe targets a clearly synthetic nonexistent repository name, requests at most one result, and disables diffs/comments. No retry, fallback, mutation, or persistence of returned PR body/comment text is authorized.
