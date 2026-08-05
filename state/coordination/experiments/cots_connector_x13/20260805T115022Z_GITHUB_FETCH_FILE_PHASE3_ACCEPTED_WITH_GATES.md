---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_FETCH_FILE_READONLY_003
event_type: PHASE3_FAILURE_PERMISSION_PORTABILITY_CONNECTOR_VARIANCE_PROBE
candidate: GitHub_fetch_file_readonly_contents_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 110
next_current_version: 111
campaign_wake: 3_of_4
phase_status: PHASE3_ACCEPTED_WITH_GATES
repository: TTaoGaming/hfo-gen-133
ref: 940c3782b71f63e8bb7267241c3d84fd42360522
ref_kind: IMMUTABLE_COMMIT
probe_path: state/coordination/experiments/cots_connector_x13/__x13_synthetic_missing_path_20260805__.md
probe_path_class: SYNTHETIC_NONSECRET_NONEXISTENT_PATH
encoding: utf-8
requested_lines: 1_to_20
connector_result: ERROR
provider_status: 404
provider_message: Not_Found
provider_documentation_url_surfaced: true
content_returned: false
raw_content_persisted: false
caller_retries: 0
caller_fallbacks: 0
caller_secondary_probe_reads: 0
mutations: 0
connector_latency_ms: NOT_EXPOSED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate: NOT_CLAIMED
custom_code_avoided_estimate: 25_to_80_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_AUTH_OBSERVED_EFFECTIVE_IDENTITY_PERMISSION_SET_TOKEN_CLASS_SCOPE_AND_CUSTODY_UNKNOWN
durability: IMMUTABLE_COMMIT_AND_EXPLICIT_PATH_MAKE_THE_REQUEST_REPRODUCIBLE_BUT_GITHUB_404_SEMANTICS_DO_NOT_PROVE_ABSENCE_BY_THEMSELVES
observability: STRUCTURED_MESSAGE_STATUS_DOCUMENTATION_URL_AND_ERROR_FLAG_EXPOSED_NO_HTTP_HEADERS_REQUEST_ID_RATE_LIMIT_EFFECTIVE_IDENTITY_PERMISSION_REASON_RETRY_GRAPH_OR_LATENCY
portability: MEDIUM_HTTP_404_IS_COMMON_BUT_GITHUB_INTENTIONALLY_USES_404_FOR_SOME_AUTHORIZATION_FAILURES_SO_SEMANTICS_ARE_PROVIDER_SPECIFIC
failure_behavior: FAILED_CLOSED_WITH_STRUCTURED_404_AND_NO_CONTENT_NO_RETRY_NO_FALLBACK_AND_NO_MUTATION
connector_variance: WRAPPER_SURFACED_COMPACT_STRUCTURED_ERROR_AND_OMITTED_RAW_HEADERS_BODY_REQUEST_ID_AUTH_CONTEXT_RATE_LIMIT_AND_PERMISSION_DIAGNOSTICS
official_contract: GET_REPOSITORY_CONTENT_RETURNS_FILE_OR_DIRECTORY_CONTENT_FOR_OWNER_REPOSITORY_PATH_AND_OPTIONAL_REF; A_404_CAN_MEAN_MISSING_RESOURCE_OR_INSUFFICIENT_AUTHORIZATION_FOR_A_PRIVATE_RESOURCE
official_contract_url: https://docs.github.com/en/rest/repos/contents#get-repository-content
official_failure_semantics_url: https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api#404-not-found-for-an-existing-resource
measured_fact: ONE_SYNTHETIC_NONEXISTENT_PATH_AT_A_PREVIOUSLY_VALID_IMMUTABLE_COMMIT_RETURNED_A_STRUCTURED_404_NOT_FOUND_ERROR_WITH_NO_CONTENT_RETRY_FALLBACK_OR_MUTATION
admitted_claim: CONNECTOR_FAILS_CLOSED_FOR_THIS_SYNTHETIC_MISSING_PATH_PROBE_AND_DOES_NOT_RETURN_MISLEADING_EMPTY_SUCCESS_CONTENT
forbidden_inference: A_404_ALONE_PROVES_THE_PATH_DOES_NOT_EXIST_OR_PROVES_CURRENT_AUTHORIZATION_SCOPE
mandatory_gate: TREAT_404_AS_AMBIGUOUS_BETWEEN_ABSENCE_AND_AUTHORIZATION; DO_NOT_RETRY_UNCHANGED_IN_A_TIGHT_LOOP; REQUIRE_SEPARATE_REPOSITORY_REF_ACCESS_EVIDENCE_BEFORE_LABELING_A_PATH_MISSING; FAIL_CLOSED_AND_SURFACE_THE_ERROR_TO_A_HUMAN; DO_NOT_PERSIST_RETRIEVED_CONTENT_WITHOUT_A_NAMED_CONSUMER
consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DIRECT_CONNECTOR_ERROR_RECEIPT_PLUS_PRIOR_PHASE2_SUCCESS_AT_SAME_REPOSITORY_AND_IMMUTABLE_COMMIT
verifier_result: FAILURE_PATH_OBSERVED_BUT_PERMISSION_CAUSE_NOT_INDEPENDENTLY_DISTINGUISHED
independent_verification_closed: false
strongest_falsifier: THE_CONNECTOR_RETURNS_SUCCESS_OR_EMPTY_CONTENT_FOR_THE_SAME_SYNTHETIC_PATH_OR_A_KNOWN_EXISTING_FILE_AT_THE_SAME_COMMIT_RETURNS_THE_IDENTICAL_404_WITH_NO_AUTH_DIAGNOSTIC
honest_flaw: THE_PROBE_ESTABLISHES_FAIL_CLOSED_BEHAVIOR_FOR_ONE_SYNTHETIC_MISSING_PATH_BUT_GITHUB_404_IS_DELiberately_AMBIGUOUS_WITH_AUTHORIZATION_FAILURE; EFFECTIVE_IDENTITY_SCOPE_RAW_PROVIDER_PARITY_TRANSIENT_FAILURES_RATE_LIMITS_BINARY_AND_LARGE_FILE_BEHAVIOR_HIDDEN_CALLS_ACTUAL_QUOTA_OPERATOR_TIME_SAVED_AND_CONSUMER_VALUE_REMAIN_UNVERIFIED
adoption_credit: 0
fitness_credit: 0
next_phase: PHASE4_DECISION_ONLY
provisional_decision: ADOPT_WITH_GATES
review_expiry_utc: 2026-08-12T11:50:22Z
valid_time_utc: 2026-08-05T11:50:22Z
recorded_time_utc: 2026-08-05T11:50:22Z
---

# X13 GitHub `fetch_file` Phase 3 — Accepted with gates

## Probe

A single bounded, read-only request targeted a deliberately synthetic nonexistent UTF-8 path at the same immutable commit used in phase 2. The requested range was lines 1–20. No retry, fallback, secondary probe read, content retention, or mutation occurred.

## Direct result

The connector returned a structured error with:

- status: `404`
- message: `Not Found`
- error flag: `true`
- provider documentation pointer: surfaced
- content: none

The connector therefore failed closed for this probe. It did not convert the failure into an empty-success result and did not return file content.

## Critical semantic boundary

A GitHub `404 Not Found` is not authoritative proof of absence. GitHub may intentionally return `404` instead of `403` when authentication or authorization does not permit confirmation that a private resource exists. The safe consumer rule is therefore:

1. fail closed on the error;
2. do not retry the identical request in a tight loop;
3. require separate evidence that the repository and immutable ref are readable under the same connector context before classifying the path as missing;
4. keep the distinction between `missing` and `not authorized` unresolved when the wrapper omits identity, permission, and response-header evidence.

The prior campaign phase successfully read `README.md` at this same repository and immutable commit, which makes the synthetic path's absence the strongest explanation. It still does not independently prove that the effective authorization context was identical on this call.

## Measurement ledger

| Dimension | Observation |
|---|---|
| Custom code avoided | `25–80 LOC`, unvalidated estimate |
| Operator minutes removed | `0` measured |
| Credentials | Connector-managed; identity, token class, scope, permissions, and custody unknown |
| Durability | Immutable commit and explicit path make the request reproducible |
| Observability | Compact status/message/error/docs pointer; no headers, request ID, identity, permission reason, quota, retry graph, or latency |
| Portability | Medium; HTTP 404 is common, but GitHub's authorization-masking semantics are provider-specific |
| Failure behavior | Failed closed with no content, retry, fallback, or mutation |
| Direct cost/quota evidence | No charge surfaced; actual quota debit unknown |
| Strongest falsifier | Same synthetic path later returns success, or a known-good path at the same commit returns the same 404 without auth diagnostics |
| Verifier | Direct connector receipt plus prior successful immutable-commit read |
| Consumer | HFO COTS capability inventory only; no operational consumer |
| Honest flaw | One synthetic 404 does not distinguish missing path from authorization failure or test other failure classes |

## Phase 3 disposition

`PHASE3_ACCEPTED_WITH_GATES`

The connector's failure shape is suitable for bounded human-reviewed use only when `404` is treated as ambiguous and absence is never inferred from the status alone.

## Next wake

Phase 4 decision only. No additional GitHub content call is required. Provisional disposition: `ADOPT_WITH_GATES` for small UTF-8 reads pinned to immutable commits with blob-SHA validation and explicit fail-closed handling.