---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_PR_CHANGED_FILENAMES_READONLY_030
event_type: PHASE2_PREFLIGHT
expected_current_version: 217
candidate: GitHub.list_pr_changed_filenames
campaign_wake: 2_of_4
wip: 1
repository: TTaoGaming/hfo-gen-133
target_pr_number: 10
planned_invocations: 1
planned_request: list_pr_changed_filenames(repo_full_name='TTaoGaming/hfo-gen-133', pr_number=10)
phase1_filename_count: 26
phase1_ordered_filename_digest_sha256: 503d2de2bca9c417c86d1de25d5527363d5e318f3cbf997cf7810258b9e12206
acceptance_test: EXACT_REPLAY;COMPARE_FILENAME_COUNT_AND_ORDERED_SHA256_DIGEST
safety: READ_ONLY_CANDIDATE_CALL;NO_PATCH_DIFF_CONTENT_COMMENT_FETCH;NO_RAW_FILENAME_PERSISTENCE;NO_PR_OR_REPO_MUTATION
boundedness_gate: KNOWN_SMALL_PR_ONLY;DO_NOT_GENERALIZE_WRAPPER_AUTO_PAGINATION_TO_LARGE_PRS
operator_minutes_removed_measured: 0
custom_code_avoided_realized_by_this_candidate: 0
valid_time_utc: 2026-08-09T22:49:35Z
recorded_time_utc: 2026-08-09T22:49:35Z
---

# Phase 2 preflight

Replay the exact Phase-1 candidate request once against known-small PR #10. Compare returned filename count and ordered-list SHA-256 digest with Phase 1. Do not fetch patches, diffs, contents, comments, or additional PR surfaces. Do not persist raw filenames.
