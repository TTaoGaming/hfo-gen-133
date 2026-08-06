---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_FETCH_READONLY_007
event_id: X13_GITHUB_CONTENTS_FETCH_READONLY_007_PHASE3_20260806T034735Z
candidate: GitHub_fetch_file_contents_readonly_surface
phase: 3_of_4
phase_status: PHASE3_ACCEPTED_WITH_GATES
prior_current_version: 126
expected_current_version: 127
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate_calls_this_wake: 1_READONLY_FAILURE_PROBE
campaign_calls_total: 3_READONLY_FETCH_FILE_CALLS_2_SUCCESS_1_STRUCTURED_404_0_RETRY_0_FALLBACK_0_CANDIDATE_MUTATION
repository: TTaoGaming/hfo-gen-133
ref: agent/gen133-bootstrap-20260730
path_class: SYNTHETIC_NONEXISTENT_PATH
synthetic_path_retained: true
encoding_requested: utf-8
line_range_requested: 1_to_10
canonical_request_sha256: c861e80439cb6959b820150ca7d73a6d661eb60e59567b79217a39fe02d95d30
result: STRUCTURED_ERROR
wrapper_message: Not_Found
wrapper_status: 404
wrapper_is_error: true
wrapper_documentation_url: https://docs.github.com/rest/repos/contents#get-repository-content
raw_content_returned: false
secret_exposure: NONE_OBSERVED
candidate_mutations: 0
retries: 0
fallbacks: 0
custom_code_avoided_estimate: 25_to_80_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_SCOPES_INSTALLATION_AND_SSO_CONTEXT_UNKNOWN
durability: FAILURE_RECEIPT_IS_RECORDED_GIT_FIRST_BUT_PROVIDER_REQUEST_ID_ETAG_AND_RAW_RESPONSE_ARE_UNAVAILABLE
observability: WRAPPER_EXPOSED_MESSAGE_STATUS_DOCUMENTATION_URL_AND_IS_ERROR_BUT_NOT_HTTP_HEADERS_REQUEST_ID_RATE_LIMIT_STATE_MEDIA_TYPE_EFFECTIVE_AUTH_OR_RAW_PROVIDER_ENVELOPE
portability: MEDIUM_HTTP_404_IS_COMMON_BUT_GITHUB_CAN_USE_404_FOR_MISSING_OR_UNAUTHORIZED_PRIVATE_RESOURCES_AND_WRAPPER_ERROR_SHAPE_IS_PROVIDER_SPECIFIC
failure_behavior: FAIL_FAST_STRUCTURED_404_WITH_NO_RETRY_OR_FALLBACK
external_call_latency: NOT_MEASURED_BY_WRAPPER
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
verifier: DISTINCT_RAW_GITHUB_GET_REPOSITORY_CONTENT_REQUEST_USING_THE_SAME_EFFECTIVE_PRINCIPAL_REPOSITORY_REF_AND_SYNTHETIC_PATH
verifier_result: NOT_RUN
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
measured_fact: A_SINGLE_SYNTHETIC_MISSING_PATH_REQUEST_RETURNED_A_STRUCTURED_404_NOT_FOUND_ERROR_WITH_ZERO_RETRY_FALLBACK_OR_CANDIDATE_MUTATION
andon: GITHUB_404_IS_NOT_AUTHORITATIVE_ABSENCE_BECAUSE_IT_CAN_ALSO_MASK_AUTHENTICATION_OR_AUTHORIZATION_FAILURE_AND_THE_WRAPPER_OMITS_IDENTITY_HEADERS_AND_RAW_PROVIDER_CONTEXT
mandatory_gate: TREAT_404_AS_MISSING_OR_INACCESSIBLE; DO_NOT_RETRY_UNCHANGED_404_IN_A_TIGHT_LOOP; VERIFY_AUTHORIZATION_AND_EXACT_REF_BEFORE_ASSERTING_ABSENCE; RETAIN_REQUEST_DIGEST_NOT_SECRETS; REQUIRE_RAW_OR_INDEPENDENT_WITNESS_FOR_HIGH_STAKES_NEGATIVE_CLAIMS
strongest_falsifier: THE_SYNTHETIC_PATH_EXISTS_AT_THE_EXACT_REF_OR_A_MATCHED_RAW_GITHUB_CONTENTS_REQUEST_RETURNS_A_MATERIALLY_DIFFERENT_STATUS_OR_ERROR_CONTEXT
honest_flaw: ONE_SYNTHETIC_404_DOES_NOT_TEST_PERMISSION_DENIAL_SEPARATELY_INVALID_REF_RATE_LIMITS_TRANSIENT_5XX_TIMEOUTS_BINARY_OR_LARGE_FILES_DIRECTORIES_SYMLINKS_SUBMODULES_RAW_PARITY_OPERATOR_SAVINGS_OR_OPERATIONAL_VALUE
next_phase: PHASE4_DECIDE_FROM_EXISTING_RECEIPTS_ONLY_WITH_NO_ADDITIONAL_CANDIDATE_CALL
primary_contract: https://docs.github.com/en/rest/repos/contents
primary_failure_guidance: https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api
review_expiry_utc: 2026-08-13T03:47:35Z
valid_time_utc: 2026-08-06T03:47:35Z
recorded_time_utc: 2026-08-06T03:47:35Z
---

# X13 GitHub Contents Fetch — Phase 3

## Failure and permission-variance probe

One read-only `fetch_file` request targeted a synthetic nonexistent path on the same repository and explicit branch used in phases 1–2. The wrapper returned a structured error with message `Not Found`, status `404`, `is_error=true`, and the GitHub repository-contents documentation URL. It returned no file content. No retry, fallback, or candidate mutation occurred.

## Measured fact

The connector failed fast and preserved a machine-readable 404 result rather than returning an empty text payload or silently falling back.

## Andon

A GitHub 404 is not authoritative proof that a path is absent. GitHub documents `404 Resource not found` for the contents endpoint, and separately documents that private resources can return 404 when authentication or authorization is insufficient to avoid confirming their existence. The wrapper did not expose the effective identity, accepted permissions, SSO state, HTTP headers, request ID, rate-limit fields, or raw provider envelope.

Consumers must classify this result as `missing_or_inaccessible`, not simply `missing`. They must not retry an unchanged 404 in a tight loop, and they must independently verify authorization and the exact ref before making a high-stakes negative claim.

## Current boundary

The provisional decision remains `ADOPT_WITH_GATES_CATALOG_ONLY`. This phase adds bounded failure-shape evidence but does not earn operational adoption or fitness credit.

Phase 4 should make the campaign decision from existing receipts only, with no additional candidate call.
