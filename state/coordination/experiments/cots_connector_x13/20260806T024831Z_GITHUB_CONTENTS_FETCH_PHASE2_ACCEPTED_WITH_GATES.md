---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_FETCH_READONLY_007
event_id: X13_GITHUB_CONTENTS_FETCH_READONLY_007_PHASE2_20260806T024831Z
candidate: GitHub_fetch_file_contents_readonly_surface
phase: 2_of_4
phase_status: PHASE2_ACCEPTED_WITH_GATES
prior_current_version: 125
expected_current_version: 126
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate_calls_this_wake: 1_READONLY
campaign_calls_total: 2_READONLY_FETCH_FILE_SUCCESS_0_RETRY_0_FALLBACK_0_MUTATION
repository: TTaoGaming/hfo-gen-133
ref: agent/gen133-bootstrap-20260730
path: README.md
encoding_requested: utf-8
line_range_requested: 1_to_40
canonical_request_sha256: b5c19d787fc54d708757d41c6d2bd85655ad7eca512835db09f451360f7ea5dc
request_descriptor_reused_from_phase1: true
result: SUCCESS
returned_encoding: utf-8
phase1_returned_blob_sha: a77cfc55c6bf9b72b272d373092e4c0be92cb5a9
phase2_returned_blob_sha: a77cfc55c6bf9b72b272d373092e4c0be92cb5a9
blob_sha_match: true
phase1_result_class: UTF8_TEXT_BOUNDED_LINE_SLICE
phase2_result_class: UTF8_TEXT_BOUNDED_LINE_SLICE
result_class_match: true
raw_content_persisted_in_event: false
secret_exposure: NONE_OBSERVED
mutations: 0
retries: 0
fallbacks: 0
custom_code_avoided_estimate: 25_to_80_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_SCOPES_INSTALLATION_AND_SSO_CONTEXT_UNKNOWN
durability: SAME_CONTENT_ADDRESSED_BLOB_SHA_RETURNED_ACROSS_TWO_EXPLICIT_BRANCH_PINNED_READS_BUT_BRANCH_REMAINS_MUTABLE
observability: CONTENT_ENCODING_BLOB_SHA_DISPLAY_URL_AND_TITLE_VISIBLE_HTTP_STATUS_ETAG_REQUEST_ID_MEDIA_TYPE_RATE_HEADERS_TOKEN_SCOPES_AND_RAW_RESPONSE_NOT_EXPOSED
portability: MEDIUM_GIT_BLOB_ID_IS_PORTABLE_ACROSS_GIT_CLIENTS_BUT_WRAPPER_LINE_SLICING_AND_GITHUB_CONTENTS_SEMANTICS_ARE_PROVIDER_SPECIFIC
failure_behavior: NOT_TESTED_IN_PHASE2
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
verifier: DISTINCT_RAW_GITHUB_GET_CONTENTS_OR_GIT_BLOB_FETCH_USING_THE_RETURNED_BLOB_SHA_AND_MATCHED_REQUEST_DESCRIPTOR
verifier_result: NOT_RUN
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
measured_fact: THE_SAME_EXPLICIT_BRANCH_PATH_ENCODING_AND_LINE_RANGE_RETURNED_THE_SAME_GIT_BLOB_SHA_AND_PRIVACY_SAFE_RESULT_CLASS_ON_TWO_READ_ONLY_CALLS
andon: REPEATABILITY_IS_ONLY_WRAPPER_LEVEL_AND_DOES_NOT_PROVE_IMMUTABLE_BRANCH_STATE_RAW_PROVIDER_PARITY_EFFECTIVE_AUTHORIZATION_OR_QUOTA_ACCOUNTING
mandatory_gate: PIN_EXPLICIT_REF; RETAIN_CANONICAL_REQUEST_DIGEST_AND_RETURNED_BLOB_SHA; TREAT_BRANCH_REF_AS_MUTABLE; DO_NOT_ASSUME_LINE_SLICE_EQUALS_FULL_FILE; DO_NOT_INFER_EFFECTIVE_AUTHORIZATION_OR_QUOTA_FROM_SUCCESS
strongest_falsifier: AN_INDEPENDENT_RAW_GIT_OR_GITHUB_BLOB_FETCH_FOR_A77CFC55C6BF9B72B272D373092E4C0BE92CB5A9_RETURNS_DIFFERENT_BYTES_OR_A_MATCHED_WRAPPER_REPLAY_RETURNS_A_DIFFERENT_SLICE_WITHOUT_A_BLOB_SHA_CHANGE
honest_flaw: TWO_SUCCESSFUL_READS_OF_ONE_SMALL_UTF8_FILE_DO_NOT_TEST_MISSING_PATH_PERMISSION_DENIAL_BINARY_OR_LARGE_FILES_DIRECTORIES_SYMLINKS_SUBMODULES_RATE_LIMITS_TRANSIENT_FAILURES_RAW_PARITY_OPERATOR_SAVINGS_OR_OPERATIONAL_VALUE
next_phase: PHASE3_ONE_BOUNDED_READ_ONLY_FETCH_OF_A_SYNTHETIC_NONEXISTENT_PATH_ON_THE_SAME_REPOSITORY_AND_REF_WITH_ZERO_RETRY_FALLBACK_OR_MUTATION
valid_time_utc: 2026-08-06T02:48:31Z
recorded_time_utc: 2026-08-06T02:48:31Z
---

# X13 GitHub Contents Fetch — Phase 2

## Smallest harmless repeatability probe

A second read-only `fetch_file` call reused the phase-1 request shape: `TTaoGaming/hfo-gen-133`, explicit ref `agent/gen133-bootstrap-20260730`, path `README.md`, UTF-8 encoding, and lines 1–40. The connector again returned Git blob SHA `a77cfc55c6bf9b72b272d373092e4c0be92cb5a9` and the same bounded UTF-8 text result class.

No candidate mutation, retry, fallback, content retention, or secret exposure occurred.

## Measured fact

The same explicit repository, branch, path, encoding, and line range returned the same content-addressed Git blob SHA across two calls. This is narrow wrapper-level repeatability evidence and indicates that the file bytes represented by that blob did not change between the two observations.

## Andon and limits

The branch ref remains mutable. Matching blob SHAs do not establish immutable branch history, raw-provider parity, complete-file retrieval, effective identity, accepted permissions, token or SSO context, rate-limit state, direct quota consumption, or operational value.

The wrapper still did not expose HTTP status, ETag, request ID, media type, accepted permissions, effective authentication context, rate-limit headers, or the raw provider envelope.

## Current boundary

Provisional decision remains `ADOPT_WITH_GATES` for catalog and bounded human-reviewed text reads only. Adoption and fitness credit remain zero.

Phase 3 should issue one bounded read-only request for a synthetic nonexistent path on the same repository and ref, with no retry, fallback, or mutation, to characterize failure behavior.
