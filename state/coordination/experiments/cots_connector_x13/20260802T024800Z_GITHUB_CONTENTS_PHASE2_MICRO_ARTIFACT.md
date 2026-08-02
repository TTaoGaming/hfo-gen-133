---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
event_type: PHASE2_HARMLESS_BRANCH_SCOPED_CREATE_FETCH_READBACK
phase: 2_of_4
expected_prior_current_version: 29
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
path: state/coordination/experiments/cots_connector_x13/20260802T024800Z_GITHUB_CONTENTS_PHASE2_MICRO_ARTIFACT.md
content_class: SMALL_UTF8_TEXT_EXPERIMENT_EVENT
secret_bearing_content: false
production_effect: false
requested_operation:
  - CREATE_UNIQUE_FILE_ON_EXISTING_BRANCH
  - FETCH_EXACT_PATH_FROM_EXPLICIT_BRANCH
  - COMPARE_EXACT_UTF8_BODY
  - RECORD_RETURNED_BLOB_SHA
mutation_ceiling:
  - NO_MERGE
  - NO_DELETE
  - NO_FORCE_PUSH
  - NO_BRANCH_CREATE
  - NO_WORKFLOW_EDIT
  - NO_PRODUCTION_DEPLOYMENT
operator_relay_minutes: 0
operator_minutes_removed_measured: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
credentials:
  operator_supplied_credentials: 0
  live_identity: UNKNOWN
  live_token_type: UNKNOWN
  live_permission_set: UNKNOWN
verifier: SAME_CONNECTOR_EXACT_PATH_AND_BRANCH_READBACK_STRUCTURAL_ONLY
consumer:
  - X13_PHASE2
  - GIT_FIRST_STATE_READERS
strongest_falsifier: FETCHED_BODY_OR_BLOB_DOES_NOT_MATCH_CREATED_ARTIFACT_OR_REQUESTED_BRANCH_IS_IGNORED
honest_flaw: CREATE_AND_FETCH_USE_THE_SAME_CONNECTOR_AND_DO_NOT_PROVIDE_INDEPENDENT_VERIFICATION
valid_time_utc: 2026-08-02T02:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 GitHub Contents phase-2 micro-artifact

This uniquely named, small UTF-8 event is the harmless branch-scoped create/fetch/readback probe. Its exact body and returned blob SHA must be checked before CURRENT advances.
