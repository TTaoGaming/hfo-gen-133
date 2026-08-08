---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCAL_CALENDARLIST_READONLY_023
phase: 2
wake: 2_of_4
event_type: PHASE2_CONTROL_RESULT
candidate: Google_Calendar_list_calendars
control_probe: Google_Calendar_get_profile
wip: 1
prior_current_version: 189
preflight_commit: c05005d9475dc02d70b393e886626a5aa4a6db22
preflight_path: state/coordination/experiments/cots_connector_x13/20260808T184627Z_GCAL_CALENDARLIST_PHASE2_GET_PROFILE_CONTROL_PREFLIGHT.md
preflight_blob_sha: 95f9796bbb1c4ae599fcb8af0a4ee2f55afd7026
preflight_readback: true
request_hash_recomputed_before_candidate_call: true
request_hash_match_before_candidate_call: true
candidate_invocations_phase2_wake: 1
usable_control_results: 1
connector_blocked_user_input_phase2: 0
connector_error_phase2: 0
external_call_time_ms: 107
retries_phase2: 0
fallbacks_phase2: 0
candidate_mutations_phase2: 0
profile_identity_values_persisted_in_x13_receipt: false
profile_result_schema_keys_observed: [email,id,name,nickname,picture]
connector_wide_blocking_falsified: true
action_specific_variance_strengthened: true
provider_call_occurrence: CONNECTOR_EXTERNAL_CALL_OBSERVED_PROVIDER_NATIVE_MAPPING_NOT_EXPOSED
operator_minutes_removed_measured: 0
custom_code_avoided_realized_by_this_candidate: 0
adoption_credit: 0
fitness_credit: 0
valid_time_utc: 2026-08-08T18:47:30Z
recorded_time_utc: 2026-08-08T18:47:30Z
---

# Phase 2 control result

One bounded read-only `Google_Calendar.get_profile` control probe succeeded non-interactively after the exact durable preflight was read back and independently hash-verified before invocation.

Measured execution facts: one invocation, usable profile-shaped result, no connector error, no user-input requirement, 107 ms connector external-call time, zero retries, zero fallbacks, and zero Calendar mutations. Raw profile identity values were intentionally not persisted in this X13 receipt.

## Interpretation

This falsifies the hypothesis that the Google Calendar connector family is globally blocked in the scheduled runtime. Combined with Phase 1, the stronger current hypothesis is action-specific variance: `list_calendars` required user input while `get_profile` succeeded under the same run family and without any permission or connection mutation.

This does **not** identify the cause of the `list_calendars` block. OAuth scope, consent state, connector routing, sensitive-action review, and native-provider mapping remain unexposed.

## Gates

- Do not retry `list_calendars` merely because `get_profile` succeeded; no relevant permission/connection state change has been observed.
- Do not infer native Google Calendar API semantics from the profile wrapper.
- Do not persist raw profile identity fields in X13 receipts.
- Keep adoption/fitness credit at zero until the actual calendar-list capability produces usable bounded evidence or is dispositioned at Phase 4.
