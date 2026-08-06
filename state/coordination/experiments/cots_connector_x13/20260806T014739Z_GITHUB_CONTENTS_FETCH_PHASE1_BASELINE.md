---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_FETCH_READONLY_007
phase: 1_of_4
decision: PHASE1_ACCEPTED_WITH_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
expected_current_version: 124
observed_current_blob_sha: 07e0a3db90de1617104b9ce235e4a939229d42ab
valid_time_utc: 2026-08-06T01:47:39Z
candidate_calls: 1
request: GitHub.fetch_file TTaoGaming/hfo-gen-133 README.md ref agent/gen133-bootstrap-20260730 utf-8 lines 1-40
request_sha256: 4b8232c36d295c93d530d2f620cf7b01f90a1e9f9beb88d10f7b34588847f7a9
result_class: UTF8_TEXT_FILE_BOUNDED_LINE_SLICE
blob_sha: a77cfc55c6bf9b72b272d373092e4c0be92cb5a9
candidate_mutations: 0
retries: 0
fallbacks: 0
custom_code_avoided_estimate: 20_to_80_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_AUTH_CONTEXT_UNKNOWN
durability: BRANCH_MUTABLE_BLOB_SHA_CONTENT_ADDRESSED_BLOB_REPLAY_UNTESTED
observability: CONTENT_SHA_URL_ENCODING_VISIBLE_HTTP_STATUS_ETAG_RATE_HEADERS_REQUEST_ID_NOT_VISIBLE
portability: MEDIUM_GITHUB_SPECIFIC_API_PLAIN_UTF8_OUTPUT
failure_behavior: SUCCESS_PATH_ONLY
paid_cost_usd_observed: 0
actual_quota_consumed: UNKNOWN
consumer: HFO_COTS_CAPABILITY_INVENTORY_ONLY
verifier: MATCHED_RAW_GITHUB_CONTENTS_OR_BLOB_FETCH
verifier_result: NOT_RUN
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
strongest_falsifier: MATCHED_RAW_FETCH_RETURNS_DIFFERENT_BYTES_OR_REVEALS_WRAPPER_TRANSFORMATION_OR_DIFFERENT_AUTH_CONTEXT
honest_flaw: ONE_SMALL_KNOWN_UTF8_FILE_ONLY; FAILURE_PERMISSION_RATE_LIMIT_BINARY_LARGE_FILE_AND_RAW_PARITY_UNTESTED
next_phase: REPEAT_BOUNDED_FETCH_COMPARE_BLOB_SHA_AND_RESULT_CLASS
---

# GitHub contents fetch phase 1

One read-only connector call returned a bounded UTF-8 slice of `README.md` from the explicit branch and exposed blob SHA `a77cfc55c6bf9b72b272d373092e4c0be92cb5a9`. No retries, fallbacks, or candidate mutations occurred. The returned content was not copied into this event.

GitHub documents the repository Contents endpoint as a path-and-ref read surface. Fine-grained access to private resources requires repository `Contents: read`; public resources can be read without authentication. Documented responses include 200, 302, 304, 403, and 404. Files up to 1 MB are fully supported; 1-100 MB files have media-type restrictions; files over 100 MB are unsupported by this endpoint. Official contract: https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-repository-content

GitHub REST limits vary by authentication context and secondary limits also apply. The connector did not expose rate headers or a quota receipt, so actual consumption is unknown. Official limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28

Provisional result: `ADOPT_WITH_GATES` for catalog-only use. Pin an explicit ref, retain the blob SHA for replay, do not treat a branch read as immutable, bound content reads, and do not infer identity, permissions, or quota from success. Adoption and fitness credit remain zero.
