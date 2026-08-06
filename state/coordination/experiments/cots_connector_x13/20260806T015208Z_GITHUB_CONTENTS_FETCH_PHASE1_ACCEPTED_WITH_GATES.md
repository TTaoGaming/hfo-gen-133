---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_FETCH_READONLY_007
event_id: X13_GITHUB_CONTENTS_FETCH_READONLY_007_PHASE1_20260806T015208Z
candidate: GitHub_fetch_file_contents_readonly_surface
phase: 1_of_4
phase_status: PHASE1_ACCEPTED_WITH_GATES
prior_current_version: 124
expected_current_version: 125
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate_calls_this_wake: 1_READONLY
repository: TTaoGaming/hfo-gen-133
ref: agent/gen133-bootstrap-20260730
path: README.md
encoding_requested: utf-8
line_range_requested: 1_to_40
canonical_request_sha256: b5c19d787fc54d708757d41c6d2bd85655ad7eca512835db09f451360f7ea5dc
result: SUCCESS
returned_encoding: utf-8
returned_blob_sha: a77cfc55c6bf9b72b272d373092e4c0be92cb5a9
returned_display_title: README.md
returned_content_class: UTF8_TEXT_BOUNDED_LINE_SLICE
raw_content_persisted_in_event: false
secret_exposure: NONE_OBSERVED
mutations: 0
retries: 0
fallbacks: 0
custom_code_avoided_estimate: 25_to_80_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_SCOPES_INSTALLATION_AND_SSO_CONTEXT_UNKNOWN
durability: RETURNED_GIT_BLOB_SHA_IS_CONTENT_ADDRESSED_BUT_REQUEST_REF_IS_A_MUTABLE_BRANCH
observability: PARTIAL_CONTENT_ENCODING_BLOB_SHA_DISPLAY_URL_AND_TITLE_VISIBLE_HTTP_STATUS_ETAG_REQUEST_ID_MEDIA_TYPE_RATE_HEADERS_TOKEN_SCOPES_AND_RAW_RESPONSE_NOT_EXPOSED
portability: MEDIUM_GIT_BLOB_ID_IS_PORTABLE_ACROSS_GIT_CLIENTS_BUT_WRAPPER_LINE_SLICING_AND_GITHUB_CONTENTS_SEMANTICS_ARE_PROVIDER_SPECIFIC
failure_behavior: NOT_TESTED_IN_PHASE1
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
mandatory_gate: PIN_EXPLICIT_REF; RETAIN_CANONICAL_REQUEST_DIGEST_AND_RETURNED_BLOB_SHA; TREAT_BRANCH_REF_AS_MUTABLE; DO_NOT_ASSUME_LINE_SLICE_EQUALS_FULL_FILE; DO_NOT_INFER_EFFECTIVE_AUTHORIZATION_OR_QUOTA_FROM_SUCCESS
strongest_falsifier: FETCHING_RETURNED_BLOB_SHA_THROUGH_AN_INDEPENDENT_RAW_GIT_OR_GITHUB_PATH_RETURNS_DIFFERENT_BYTES_OR_THE_WRAPPER_SLICE_OMITS_OR_TRANSFORMS_REQUESTED_LINES
honest_flaw: ONE_SMALL_UTF8_TEXT_FILE_ON_ONE_ACCESSIBLE_BRANCH_WAS_TESTED; FULL_FILE_RETRIEVAL_BINARY_FILES_LARGE_FILES_DIRECTORIES_SYMLINKS_SUBMODULES_PERMISSION_DENIAL_NOT_FOUND_RATE_LIMITS_TRANSIENT_FAILURES_RAW_PARITY_OPERATOR_SAVINGS_AND_OPERATIONAL_VALUE_REMAIN_UNVERIFIED
next_phase: PHASE2_REPEAT_BOUNDED_FETCH_USING_THE_SAME_CANONICAL_REQUEST_DESCRIPTOR_AND_COMPARE_RETURNED_BLOB_SHA_AND_PRIVACY_SAFE_RESULT_CLASS
valid_time_utc: 2026-08-06T01:52:08Z
recorded_time_utc: 2026-08-06T01:52:08Z
---

# X13 GitHub Contents Fetch — Phase 1

## Direct capability baseline

A single bounded `fetch_file` call read lines 1–40 of `README.md` from the explicit branch `agent/gen133-bootstrap-20260730` as UTF-8 text. The connector returned content, encoding, a Git blob SHA, a display URL, and a title. No mutation, retry, fallback, secret, or raw response retention occurred.

The returned blob SHA was `a77cfc55c6bf9b72b272d373092e4c0be92cb5a9`. That gives a content-addressed comparison point, while the requested branch remains mutable.

## Official contract baseline

GitHub documents `GET /repos/{owner}/{repo}/contents/{path}` as the endpoint for file or directory contents. The optional `ref` can name a commit, branch, or tag and otherwise defaults to the repository default branch. Fine-grained authenticated access requires repository `Contents: read`; public resources may be fetched unauthenticated. The endpoint has media-type, directory, symlink, submodule, and file-size-specific behavior, including a 1,000-entry directory cap, restricted behavior from 1–100 MB, and no support above 100 MB.

Official sources:

- https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-repository-content
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28

## Measured fact and Andon

**Measured fact:** the connector can perform a branch-pinned, line-bounded UTF-8 file read and expose the backing Git blob SHA without a write.

**Andon:** the wrapper did not expose HTTP status, ETag, request ID, accepted permissions, effective authentication context, rate-limit headers, media type, or raw provider envelope. A successful read therefore does not prove which principal or quota bucket was used. A branch-pinned read is also not immutable unless the returned blob SHA or a commit SHA is retained.

## Current boundary

Provisional decision: `ADOPT_WITH_GATES` for catalog and bounded human-reviewed reads only. Operational adoption and fitness credit remain zero.
