---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_PR_CHANGED_FILENAMES_READONLY_030
candidate: GitHub.list_pr_changed_filenames
phase: 1
status: PHASE1_ACCEPTED_WITH_GATES_ANDON
wip: 1
request_sha256: 1738c2242d599419abf480add82dae55d2f3bf4cc3dd4e7766ed4b87ca39aa2f
target_repository: TTaoGaming/hfo-gen-133
target_pr_number: 10
candidate_invocations_total: 1
usable_candidate_results: 1
result_filename_count: 26
ordered_filename_digest_sha256: 503d2de2bca9c417c86d1de25d5527363d5e318f3cbf997cf7810258b9e12206
raw_filename_persisted: false
connector_external_call_time_ms: 486
connector_errors_total: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_quota_evidence: NONE_FROM_CONNECTOR_RECEIPT
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_PERMISSION_GRANT_UNKNOWN
durability: PHASE1_PREFLIGHT_AND_RESULT_WRITTEN_TO_CANONICAL_BRANCH_WITH_READBACK_REQUIRED
observability: CONNECTOR_RETURNED_FILENAMES_ONLY_PLUS_WRAPPER_EXTERNAL_CALL_TIME;NO_NATIVE_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_PAGE_COUNT_OR_QUOTA_DEBIT_SURFACED
portability: HIGH_TO_GITHUB_REST_PULLS_FILES_RESOURCE_BUT_WRAPPER_AUTO_PAGINATION_SEMANTICS_AND_3000_FILE_CAP_HANDLING_UNVERIFIED
failure_behavior: NOT_YET_PROBED
verifier: OFFICIAL_GITHUB_PULLS_FILES_AND_TOKEN_PERMISSION_DOCS_PLUS_DIRECT_CONNECTOR_RECEIPT
consumer: HFO_PR_BLAST_RADIUS_AND_TARGETED_PATCH_SELECTION_GATES
strongest_falsifier: KNOWN_PR_CHANGED_FILE_COUNT_DISAGREES_WITH_CONNECTOR_FILENAME_COUNT_OR_MULTI_PAGE_PR_IS_SILENTLY_TRUNCATED_OR_WRAPPER_EXCEEDS_OPERATOR_BOUNDEDNESS_REQUIREMENT
honest_flaw: WRAPPER_EXPOSES_NO_PER_PAGE_PAGE_OR_MAX_FILES_BOUND_AND_CLAIMS_ALL_PAGE_PAGINATION;ON_LARGE_PRS_ONE_CALL_CAN_FAN_OUT_TO_MANY_PROVIDER_REQUESTS_UP_TO_GITHUBS_3000_FILE_RESPONSE_CAP;NATIVE_RATE_HEADERS_AND_PAGE_COUNT_ARE_HIDDEN
mandatory_gate: READ_ONLY;KNOWN_SMALL_PR_ONLY_UNTIL_PAGINATION_VARIANCE_IS_PROBED;DO_NOT_FETCH_PATCHES_CONTENT_OR_COMMENTS;DO_NOT_PERSIST_RAW_FILENAMES_UNLESS_MINIMUM_NECESSARY;NO_AUTHORITATIVE_COMPLETENESS_RATE_LIMIT_PERMISSION_OR_COST_CLAIMS
valid_time_utc: 2026-08-09T21:49:01Z
recorded_time_utc: 2026-08-09T21:49:01Z
---

# X13 GitHub changed-filenames Phase 1 baseline

One direct read-only call to `GitHub.list_pr_changed_filenames` on PR #10 returned **26 filenames** in **486 ms** with no connector error, retry, fallback, patch/diff/content hydration, or mutation observed. Only the count and an ordered-list digest were persisted; raw filenames were not copied into this event.

Official GitHub REST contract: `GET /repos/{owner}/{repo}/pulls/{pull_number}/files` is paginated, defaults to 30 results/page, supports up to 100/page, and returns at most 3000 files. Fine-grained tokens can access the endpoint with Pull requests repository permission set to read. The connector is a thin convenience surface that returns filenames and claims to traverse all file-list pages.

## Andon

The wrapper exposes **no caller-controlled page size, page number, or maximum file count**. That removes pagination code, but it also removes a forcing function for bounded reads: a single connector invocation against a large PR may fan out into many underlying provider requests, while the receipt exposes neither page count nor GitHub rate-limit headers. Until Phase 3 validates this variance, adoption is limited to known-small PRs.

Measured operator minutes removed remain `0`; realized custom-code avoidance remains `0`; `20–60 LOC` avoided is only an estimate for replacing manual REST pagination plus filename extraction.

Next wake: Phase 2 exact replay on the same known-small PR, compare filename count and ordered digest, and make no patch/content call.
