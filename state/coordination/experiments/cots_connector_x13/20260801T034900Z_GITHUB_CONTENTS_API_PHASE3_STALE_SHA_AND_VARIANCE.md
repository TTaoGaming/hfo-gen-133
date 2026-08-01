---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_API_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
candidate: GitHub_REST_Contents_API
campaign_wake: 3_of_4
phase: 3
result: STALE_SHA_REJECTED_AND_BASELINE_RESTORED
expected_current_version: 6
next_current_version: 7
valid_time_utc: 2026-08-01T03:49:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
expiry_utc: 2026-08-08T03:49:00Z
effect_ceiling: QUARANTINED_SINGLE_FILE_CONTENTS_API_ONLY
official_contract:
  contents_api: https://docs.github.com/en/rest/repos/contents
  api_versions: https://docs.github.com/en/rest/about-the-rest-api/api-versions
probe:
  specimen_path: state/coordination/experiments/cots_connector_x13/specimens/20260801T034800Z_GITHUB_CONTENTS_PHASE3_STALE_SHA.txt
  baseline_utf8_bytes: 205
  baseline_sha256: 03fd8dde3cd229dc23c2f7ce934d7a6cdef5b5a8e9d7ba769bba9a6c1e6b313e
  baseline_blob_sha: 668b0f85c1a1f099512638a906787e9ab93635ff
  baseline_create_commit: d18e4618896c23e8fd8f5dc8b3fed3fdf9c64dcf
  baseline_create_latency_ms_exposed: 777
  newer_utf8_bytes: 202
  newer_sha256: 5b0f675da8dc3a9a97a95da4a120108581201cc0c5525e293679c73f07b111e8
  newer_blob_sha: 7c1e66d6f7e6ae50777c8090cbd0524b25c13b52
  newer_commit: 25c1bb7699578b19fe9a9ed1d07dec62ee8fb9ba
  newer_update_latency_ms_exposed: 700
  stale_attempt_utf8_bytes: 224
  stale_attempt_sha256: 6cc1d1010dce4c715042c6b5a3a56f3b7f48fefcc3c2b3ec4867e8b9e7610e16
  stale_supplied_blob_sha: 668b0f85c1a1f099512638a906787e9ab93635ff
  stale_result_http_status_exposed: 409
  stale_result_class: CONFLICT_SHA_MISMATCH
  stale_attempt_landed: false
  post_rejection_readback_blob_sha: 7c1e66d6f7e6ae50777c8090cbd0524b25c13b52
  post_rejection_readback_sha256: 5b0f675da8dc3a9a97a95da4a120108581201cc0c5525e293679c73f07b111e8
  restore_commit: cdff831d8e45326a154cb4eade4c7d5f1f96d9f5
  restore_latency_ms_exposed: 607
  final_blob_sha: 668b0f85c1a1f099512638a906787e9ab93635ff
  final_sha256: 03fd8dde3cd229dc23c2f7ce934d7a6cdef5b5a8e9d7ba769bba9a6c1e6b313e
  final_state: BASELINE_EXACT_BYTES_RESTORED
measurement:
  custom_code_avoided_estimate: 30_to_60_LOC_for_basic_single_file_compare_and_swap_wrapper
  operator_relay_minutes: 0
  operator_minutes_removed_estimate: 10_to_15
  credentials: CONNECTOR_AUTHENTICATED_BUT_IDENTITY_SCOPE_AND_LEAST_PRIVILEGE_NOT_EXPOSED
  durability: GIT_COMMITS_AND_BLOBS_PERSIST_IN_REPOSITORY_HISTORY_SUBJECT_TO_REPOSITORY_RETENTION_AND_ADMIN_ACTION
  observability: SUCCESS_COMMIT_SHA_BLOB_SHA_LATENCY_AND_STALE_ERROR_STATUS_EXPOSED
  portability: LOW_TO_MEDIUM_GITHUB_SPECIFIC_BLOB_SHA_CONCURRENCY_TOKEN_AND_CONNECTOR_ERROR_SHAPE
  failure_behavior: STALE_SINGLE_FILE_UPDATE_REJECTED_WITH_409_AND_NEWER_BYTES_PRESERVED
  direct_cost_usd_observed: 0
  quota_evidence: RATE_LIMIT_HEADERS_NOT_EXPOSED
  effective_api_version: UNKNOWN_CONNECTOR_HEADER_NOT_EXPOSED
  strongest_falsifier: A_REPEATED_OR_TRULY_CONCURRENT_PROBE_LANDS_STALE_BYTES_OR_CONNECTOR_RETRIES_WITHOUT_CALLER_VISIBILITY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER
consumer: X13_PHASE4_RATATOSKR_AND_OLRUN
rollback: VALID_FORWARD_UPDATE_RESTORED_BASELINE_BYTES
honest_flaw: >
  This is one serial single-path experiment through one connector. It does not prove
  simultaneous-writer safety, linearizability, exactly-once execution, multi-file
  atomicity, retry transparency, least privilege, request attribution, or database
  transaction guarantees. Git branch references remain movable and repository
  administrators can rewrite or delete history.
phase_4_required: true
phase_4_decision: PENDING
---

# X13 phase 3 — stale SHA and connector-variance probe

GitHub required the current blob SHA for replacement. After a valid update moved the
specimen from the baseline blob to a newer blob, a replacement carrying the stale
baseline SHA returned HTTP 409. Immediate readback showed the newer exact bytes and
newer blob SHA unchanged. A valid forward update then restored the baseline bytes and
original blob SHA.

The connector exposed successful commit/blob identifiers, successful-call latency, and
the stale-write HTTP status, but not authentication identity or scope, request ID,
rate-limit headers, ETag, retry behavior, audit actor, or the effective
X-GitHub-Api-Version header.

This supports a gated single-file compare-and-swap use. It does not yet justify an
adoption decision; phase 4 must weigh the hidden permission/version/quota surfaces and
the lack of cross-file transaction semantics.
