---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_PR_CHANGED_FILENAMES_READONLY_030
event_type: PHASE3_PREFLIGHT
expected_current_version: 218
candidate: GitHub.list_pr_changed_filenames
campaign_wake: 3_of_4
wip: 1
repository: TTaoGaming/hfo-gen-133
probe_pr_number: 2147483647
probe_type: CLEARLY_SYNTHETIC_NONEXISTENT_PR_READ_ONLY_FAILURE_CONTRACT
candidate_invocations_planned_this_event: 1
mutation_planned: false
patch_diff_content_comment_fetch_planned: false
raw_filename_persistence_planned: false
planned_success_criterion: STRUCTURED_FAIL_CLOSED_WITHOUT_RETRY_FALLBACK_OR_MUTATION
planned_classification_gate: DO_NOT_TREAT_404_AS_PERMISSION_CLASSIFIER_GITHUB_CAN_MASK_AUTHORIZATION_AS_NOT_FOUND
operator_minutes_removed_measured_before_probe: 0
custom_code_avoided_realized_before_probe: 0
strongest_falsifier: CONNECTOR_RETRIES_OR_FALLS_BACK_OR_HYDRATES_OTHER_SURFACES_OR_MUTATES_ON_MISSING_PR
verifier: DIRECT_GITHUB_CONNECTOR_RECEIPT_PLUS_GIT_DURABLE_READBACK
consumer: HFO_PR_BLAST_RADIUS_AND_TARGETED_PATCH_SELECTION_GATES
valid_time_utc: 2026-08-09T23:51:00Z
recorded_time_utc: 2026-08-09T23:51:00Z
---

# Phase 3 preflight

Exactly one harmless read-only failure-contract probe is authorized for `GitHub.list_pr_changed_filenames` using a clearly synthetic pull-request number on the canonical repository. No patch, diff, repository content, comment, pagination experiment, mutation, retry, or fallback is authorized.

A `404`-class result, if observed, will be recorded only as `NONEXISTENT_OR_INACCESSIBLE`; GitHub documents that some inaccessible private resources are intentionally surfaced as `404 Not Found`, so the probe cannot classify permissions.
