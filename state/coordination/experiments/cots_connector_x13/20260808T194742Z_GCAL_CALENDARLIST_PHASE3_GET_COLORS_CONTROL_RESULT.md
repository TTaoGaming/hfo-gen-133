---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCAL_CALENDARLIST_READONLY_023
phase: 3
wake: 3_of_4
event_type: CONTROL_RESULT
candidate: Google_Calendar_list_calendars
control_probe: Google_Calendar_get_colors
wip: 1
preflight_commit: 92bd2634def3975343abb1bd4b0cbee78052012b
preflight_blob_sha: e718db092543bb3767f4fc0cf13c6531f6004f27
request_descriptor_sha256: c6a5f2fa7f130bee935720381ceb6dea7b6a7539d9e5e839e2a14fa4f64fdcce
request_hash_verified_before_call: true
connector_result: SUCCESS
connector_external_call_time_ms: 120
calendar_palette_entry_count: 24
event_palette_entry_count: 11
raw_palette_values_persisted: false
retries: 0
fallbacks: 0
calendar_mutations: 0
paid_charge_surfaced: false
actual_quota_debit_exposed: false
provider_request_id_exposed: false
official_contract_note: GOOGLE_CALENDAR_COLORS_GET_IS_READ_ONLY_METADATA_AND_AUTHORIZATION_IS_OPTIONAL
official_quota_note: CURRENT_DEFAULTS_ARE_10000_REQUESTS_PER_MINUTE_PER_PROJECT_600_PER_MINUTE_PER_USER_PER_PROJECT_AND_1000000_REQUESTS_PER_DAY_PER_PROJECT_BEFORE_BILLING_THRESHOLD;ACTUAL_CONNECTOR_DEBIT_UNKNOWN
measured_fact: GET_COLORS_SUCCEEDED_NONINTERACTIVELY_IN_120MS_WITH_24_CALENDAR_AND_11_EVENT_PALETTE_ENTRIES
interpretation: CONNECTOR_CAN_ROUTE_THIS_METADATA_ACTION_BUT_SUCCESS_IS_WEAK_AUTH_EVIDENCE_BECAUSE_NATIVE_COLORS_GET_ALLOWS_NO_AUTHORIZATION
honest_flaw: THIS_DOES_NOT_DIAGNOSE_WHY_LIST_CALENDARS_REQUIRED_USER_INPUT_AND_IS_NOT_A_PERMISSION_DENIAL_TEST
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 30_to_80_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
adoption_credit: 0
fitness_credit: 0
valid_time_utc: 2026-08-08T19:47:42Z
recorded_time_utc: 2026-08-08T19:47:42Z
---

# Phase 3 result

The Git-preflighted `Google_Calendar.get_colors` control succeeded non-interactively in 120 ms. It returned 24 calendar palette entries and 11 event palette entries. Raw palette values were not persisted. There were no retries, fallbacks, or Calendar mutations.

Google's official Calendar API contract says native `colors.get` is read-only metadata and authorization is optional. That makes this a useful connector-routing control but weak evidence about OAuth or CalendarList scope. It does not explain the Phase-1 `list_calendars` user-input requirement.

The actual calendar-list candidate still has zero usable results. Phase 4 should decide from the frozen evidence set with no additional Calendar candidate call.
