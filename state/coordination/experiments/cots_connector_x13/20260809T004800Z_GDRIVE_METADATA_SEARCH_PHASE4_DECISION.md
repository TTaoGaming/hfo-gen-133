---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_024
event_type: PHASE4_DECISION
phase: 4
campaign_wake: 4_of_4
expected_current_version: 195
next_current_version: 196
candidate: Google_Drive_search_metadata_only
decision: ADOPT_WITH_GATES
operational_decision: ADOPT_FOR_BOUNDED_METADATA_DISCOVERY_ONLY
wip: 1
candidate_calls_this_wake: 0
candidate_invocations_total: 3
usable_candidate_results: 2
connector_errors_total: 1
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
content_hydrations_total: 0
phase1_phase2_result_count_match: true
phase1_phase2_ordered_id_digest_match: true
native_method_mapping_observed: GOOGLE_DRIVE_V3_FILES_LIST
provider_http_400_invalid_page_token_observed: true
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
adoption_credit: 1
fitness_credit: 0
mandatory_gate: METADATA_ONLY;BOUNDED_RESULTS;NO_MUTATION;DO_NOT_INFER_COMPLETENESS;TREAT_DOCUMENT_AS_CONNECTOR_DEFINED_CATEGORY;FAIL_CLOSED_ON_ERRORS;REQUIRE_NEW_PROBE_BEFORE_PAGINATION_OR_AUTHORITATIVE_INVENTORY_USE
strongest_falsifier: PROVIDER_DIRECT_EQUIVALENT_UNDER_SAME_ACCESS_RETURNS_MATERIALLY_DIFFERENT_ACCESSIBLE_MATCHES_OR_CONNECTOR_HIDES_MATERIAL_AUTH_FAILURE
honest_flaw: TWO_SUCCESS_WAKES_AND_ONE_SYNTHETIC_FAILURE_ONLY;BOTH_SUCCESSES_HIT_RESULT_CAP;VALID_PAGINATION_PERMISSION_DENIAL_RATE_LIMIT_COMPLETENESS_AND_ACTUAL_QUOTA_USE_UNTESTED
reason: REPEATABLE_BOUNDED_METADATA_RESULTS_PLUS_PROVIDER_SPECIFIC_FAIL_CLOSED_ERROR_AND_NATIVE_FILES_LIST_MAPPING_SUPPORT_NARROW_DISCOVERY_USE_BUT_NOT_EXHAUSTIVE_INVENTORY
next_phase: CLOSED_START_NEW_CANDIDATE_PHASE1_NEXT_WAKE
valid_time_utc: 2026-08-09T00:48:00Z
recorded_time_utc: 2026-08-09T00:48:00Z
---

# X13 Phase 4 Decision — Google Drive metadata search

Decision: **ADOPT_WITH_GATES**.

Frozen evidence supports bounded metadata discovery through the existing Google Drive connector: two bounded metadata-only searches matched on capped result count and ordered-result digest, and a synthetic invalid pagination token failed closed with a provider-specific HTTP 400 while exposing Google Drive v3 `files.list`. No additional candidate call was made in Phase 4.

This is not approval for authoritative or exhaustive inventory. Both successful calls hit the result cap, valid pagination was not demonstrated, access-scope details and actual quota use remain unknown, and the connector's `document` category spans multiple file families.

Gates: metadata-only by default; bounded result count; no mutation; never infer completeness from capped results; treat `document` as a connector-defined category; fail closed on connector/provider errors; run a separate bounded campaign before depending on pagination or authoritative inventory semantics.

Measured operator minutes removed remain `0`. Realized custom-code avoidance remains `0`; the `40–120 LOC` estimate is unvalidated. Adoption credit is `1`; fitness credit remains `0` until a named consumer demonstrates downstream value.
