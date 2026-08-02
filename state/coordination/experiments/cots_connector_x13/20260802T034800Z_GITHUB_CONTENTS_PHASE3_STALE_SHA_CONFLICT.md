---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
event_type: PHASE3_SYNTHETIC_STALE_BLOB_SHA_FAIL_CLOSED
phase: 3_of_4
expected_prior_current_version: 30
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
target_path: state/coordination/experiments/cots_connector_x13/20260802T024800Z_GITHUB_CONTENTS_PHASE2_MICRO_ARTIFACT.md
operation: UPDATE_EXISTING_SMALL_TEXT_FILE_WITH_SYNTHETIC_NONCURRENT_BLOB_SHA
synthetic_stale_sha: 0000000000000000000000000000000000000000
expected_result: CONFLICT_OR_VALIDATION_FAILURE_WITH_NO_CONTENT_CHANGE
observed_result:
  connector_action: GitHub.update_file
  is_error: true
  status: 409
  normalized_semantics: CONFLICT_CURRENT_BLOB_SHA_PRECONDITION_REJECTED
  error_message_disclosed_target_path: true
  error_message_disclosed_supplied_synthetic_sha: true
  provider_documentation_url_returned: true
  retry_observed: false
  commit_sha_returned: false
preservation_readback:
  connector_action: GitHub.fetch_file
  explicit_ref: agent/gen133-bootstrap-20260730
  result: SUCCESS_FILE_CONTENT
  original_blob_sha_before_probe: 538800f2b63a130014f5c6f88ab41c8f1385fc75
  returned_blob_sha_after_probe: 538800f2b63a130014f5c6f88ab41c8f1385fc75
  blob_preserved: true
  exact_original_UTF8_body_preserved: true
  synthetic_payload_observed_in_file: false
mutation_effect:
  file_content_changed: false
  commit_created_by_failed_probe: false
  merge: false
  delete: false
  branch_create: false
  workflow_edit: false
  production_effect: false
official_contract_checked_2026_08_02:
  update_requires_current_blob_sha: true
  documented_status_409: CONFLICT
  documented_status_422: VALIDATION_FAILED_OR_SPAMMED
  concurrent_create_update_delete_should_be_serialized: true
failure_semantics:
  stale_or_noncurrent_blob_sha: FAILS_CLOSED_AS_409_IN_THIS_DIRECT_PROBE
  blind_retry: PROHIBITED
  required_recovery: REFRESH_CURRENT_BLOB_SHA_RECONCILE_EXPECTED_BODY_AND_VERSION_THEN_DECIDE_OR_ABORT
  same_connector_preservation_readback: STRUCTURAL_RECONCILIATION_NOT_INDEPENDENT_VERIFICATION
privacy_and_observability:
  secret_bearing_content: false
  live_identity: UNKNOWN
  permission_set: UNKNOWN
  token_type: UNKNOWN
  HTTP_headers_request_id_rate_limit_headers: NOT_EXPOSED
  error_echoed_private_query_or_provider_URL: false
  error_echoed_repository_path_and_synthetic_SHA: true
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
custom_code_avoided_estimate:
  optimistic_concurrency_HTTP_and_error_plumbing: 20_to_60_LOC_UNVALIDATED
  conflict_detection_from_status: PROVIDED_BY_CONNECTOR
custom_policy_not_avoided:
  - REFRESH_AND_RECONCILE_BEFORE_RETRY
  - EXPECTED_VERSION_COMPARE_AND_SWAP
  - SERIAL_WRITE_ORDER
  - MULTI_COMMIT_RECOVERY
  - INDEPENDENT_VERIFICATION
verifier: SAME_CONNECTOR_EXACT_BRANCH_PATH_BLOB_AND_BODY_READBACK_STRUCTURAL_ONLY_THEN_DISTINCT_COMMIT_PINNED_REVIEW
consumer:
  - X13_PHASE4_DECISION
  - GIT_FIRST_STATE_WRITERS
strongest_falsifier: A_COMMIT_OR_CONTENT_CHANGE_EXISTS_FROM_THE_FAILED_PROBE_OR_AN_INDEPENDENT_COMMIT_PINNED_READ_SHOWS_THE_ORIGINAL_BODY_OR_BLOB_WAS_NOT_PRESERVED
honest_flaw: THE_PROBE_USED_A_DELIBERATELY_IMPOSSIBLE_ALL_ZERO_SHA_NOT_A_NATURALLY_STALE_PRIOR_BLOB_AND_DID_NOT_TEST_PERMISSION_RATE_LIMIT_CROSS_CLIENT_OR_TRUE_CONCURRENT_WRITER_VARIANCE
valid_time_utc: 2026-08-02T03:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 GitHub Contents phase-3 stale-SHA conflict probe

A synthetic update supplied a noncurrent all-zero blob SHA against the phase-2 micro-artifact. The connector returned HTTP 409 and created no commit. A branch-qualified readback returned the original exact body and the same blob SHA, so this bounded probe failed closed.

This validates connector-level optimistic concurrency rejection for one synthetic mismatch. It does not prove independent verification, least privilege, natural concurrent-writer behavior, rate-limit handling, or portable status normalization across other Git hosts and wrappers.
