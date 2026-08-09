---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_BRANCH_SEARCH_READONLY_025
event_type: PHASE3_PREFLIGHT
expected_current_version: 198
candidate: GitHub_search_branches_readonly
campaign_wake: 3_of_4
phase_status: PREFLIGHT_ONLY
wip: 1
probe_kind: MALFORMED_OPAQUE_CURSOR_FAILURE_VARIANCE
mutation_allowed: false
retries_allowed: false
fallbacks_allowed: false
request_sha256: 5eaa2b34bcef4af0c8ef983dc5cd49ebc154287bb0175ae995e34bced2396c65
request_canonical_json: '{"cursor":"x13-invalid-cursor-phase3-do-not-reuse","owner":"TTaoGaming","page_size":5,"query":"agent/gen133-bootstrap-20260730","repo_name":"hfo-gen-133"}'
expected_safe_behavior: FAIL_CLOSED_WITHOUT_BRANCH_MUTATION_OR_RETURN_A_BOUNDED_EMPTY_OR_VALIDATED_RESULT;NO_RETRY
operator_minutes_removed_measured: 0
custom_code_avoided_realized_by_this_candidate: 0
mandatory_gate: READ_ONLY;BOUNDED_PAGE_SIZE_5;SYNTHETIC_CURSOR_ONLY;NO_BRANCH_MUTATION;NO_RETRY;NO_FALLBACK;DO_NOT_PERSIST_LIVE_CURSOR_VALUE
valid_time_utc: 2026-08-09T03:49:42Z
recorded_time_utc: 2026-08-09T03:49:42Z
---

# X13 GitHub Branch Search Phase 3 Preflight

One harmless read-only connector-variance probe is authorized: replay the established branch query with a synthetic malformed opaque cursor and `page_size=5`.

The request must be invoked only after this preflight is read back and its canonical JSON SHA-256 is verified. No branch mutation, retry, fallback, live-cursor persistence, permission change, or alternate action is authorized in this wake.
