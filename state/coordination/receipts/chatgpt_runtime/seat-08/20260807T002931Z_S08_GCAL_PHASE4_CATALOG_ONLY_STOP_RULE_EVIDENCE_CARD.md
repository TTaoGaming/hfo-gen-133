---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
queue_experiment: X13_GCAL_SEARCH_READONLY_012
queue_current_version: 147
bounded_uncertainty: DOES_EXISTING_PHASE1_TO_PHASE3_EVIDENCE_JUSTIFY_OPERATIONAL_ADOPTION_OR_ANOTHER_CALENDAR_SEARCH_PROBE_AT_PHASE4
decision: RETIRE
decision_scope: RETIRE_ACTIVE_REPEAT_SCOUTING_ONLY
catalog_disposition: RETAIN_WITH_GATES
operational_adoption: false
next_candidate_call: NONE
candidate: Google_Calendar.search_events read-only surface
candidate_schema_observed: 2026-08-06
supported_claims:
  - ONE_BOUNDED_PRIMARY_CALENDAR_QUERY_RETURNED_3_EVENTS_WITH_NO_CONNECTOR_ERROR
  - ONE_IDENTICAL_REPLAY_RETURNED_THE_SAME_ORDERED_NORMALIZED_DIGEST
  - ONE_SYNTHETIC_NONMATCH_RETURNED_ZERO_EVENTS_NULL_PAGE_TOKEN_AND_NO_CONNECTOR_ERROR
  - MATCHING_SEARCHES_HYDRATED_FULL_EVENT_DESCRIPTION_CONTENT
  - EMPTY_SUCCESS_IS_DISTINGUISHABLE_FROM_CONNECTOR_FAILURE_ON_THE_OBSERVED_CALL
excluded_claims:
  - CALENDAR_WIDE_ABSENCE_OR_COMPLETENESS
  - STABLE_PROVIDER_ORDER_OR_SNAPSHOT_SEMANTICS
  - DURABLE_INCREMENTAL_SYNC_CURSOR
  - OTHER_CALENDAR_OR_PERMISSION_BEHAVIOR
  - PAGINATION_RATE_LIMIT_TRANSIENT_FAILURE_OR_INDEX_LAG_BEHAVIOR
  - RAW_PROVIDER_PARITY
  - EFFECTIVE_PRINCIPAL_OR_OAUTH_SCOPE
  - MEASURED_OPERATOR_TIME_SAVINGS
  - OPERATIONAL_CONSUMER_VALUE
  - FITNESS_OR_ADOPTION_CREDIT
license_terms_uncertainty: NO_NEW_TERMS_ACCEPTED; GOOGLE_API_USAGE_AND_USER_DATA_TERMS_REMAIN_PROVIDER_GOVERNED; EFFECTIVE_CONNECTOR_SCOPE_BACKEND_MAPPING_RETENTION_AND_QUOTA_DEBIT_ARE_UNBOUND; CATALOG_RETENTION_MUST_NOT_BE_TREATED_AS_PERMISSION_TO_WIDEN_DATA_ACCESS
paid_cost_usd_observed: 0
operator_minutes_removed_measured: 0
producer_research_minutes_estimate: 5_to_10
distinct_provider_verification_minutes_estimate: 15_to_30
strongest_objection: THREE_SUCCESSFUL_BOUNDED_CALLS_ALREADY_SHOW_A_PRACTICALLY_USEFUL_SEARCH_SURFACE_SO_RETIRING_THE_CAMPAIGN_MAY_LOOK_PREMATURE
response_to_objection: THE_SURFACE_IS_WORTH_RETAINING_IN_THE_COTS_CATALOG_BUT_ZERO_NAMED_OPERATIONAL_CONSUMER_ZERO_CONSUMER_ACK_ZERO_MEASURED_OPERATOR_MINUTES_REMOVED_AND_AN_ACTIVE_CONTENT_HYDRATION_PRIVACY_ANDON_MEAN_ANOTHER_SCOUTING_PROBE_HAS_NO_CURRENT_FITNESS_SIGNAL
falsifier: REOPEN_ONLY_IF_A_NAMED_WORKITEM_CONSUMES_THE_EXACT_CAPABILITY_WITH_ACCEPTANCE_CRITERIA_AND_MEASURES_USEFUL_OPERATOR_TIME_OR_IF_THE_CONNECTOR_SCHEMA_MATERIALLY_CHANGES_TO_EXPOSE_LOWER_DATA_PROJECTION_SYNC_OR_OTHER_REQUIRED_SEMANTICS_OR_A_MATCHED_SAME_PRINCIPAL_PROVIDER_WITNESS_CONTRADICTS_A_RELIED_UPON_BOUNDARY
verifier: S03_REDUCER_PLUS_S04_STRUCTURAL_PREFLIGHT_FOR_BINDING_GAPS; DISTINCT_SAME_PRINCIPAL_RAW_GOOGLE_CALENDAR_V3_WITNESS_REQUIRED_FOR_CONSEQUENTIAL_PROVIDER_PARITY_CLAIMS
consumer: X13_GCAL_SEARCH_READONLY_012_PHASE4_DECISION_GATE
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
fitness_credit: 0
adoption_credit: 0
expiry_utc: 2026-08-14T00:29:31Z
valid_time_utc: 2026-08-07T00:29:31Z
sources:
  - path: state/coordination/experiments/cots_connector_x13/CURRENT.md
    version: 147
    blob_sha1: aca0fa8ed1a4240b8d17aae63b06336662680444
  - path: state/coordination/experiments/cots_connector_x13/20260806T214800Z_GCAL_SEARCH_PHASE1_BASELINE.md
    blob_sha1: b1915f3e64bda5737046c47fbbe21c893d4c5a0c
  - path: state/coordination/experiments/cots_connector_x13/20260806T224800Z_GCAL_SEARCH_PHASE2_REPLAY.md
    blob_sha1: 78178bc420b5b2eaca2e6e2198f160739cfc4f26
  - path: state/coordination/experiments/cots_connector_x13/20260806T234800Z_GCAL_SEARCH_PHASE3_SYNTHETIC_EMPTY.md
    blob_sha1: 0cbff37deddeef4871f85f1b2743b2c4247e45dc
  - path: state/coordination/receipts/chatgpt_runtime/seat-03/20260807T000855Z_X13_GCAL_SEARCH_PHASE3_RETURN_BINDINGS_REVISE.yaml
    blob_sha1: d600257c311d37f6b7a9db580fdf9e3482762814
  - path: state/coordination/receipts/chatgpt_runtime/seat-04/20260807T001106Z_X13_GCAL_SEARCH_PHASE3_STRUCTURAL_REVISE.yaml
    blob_sha1: d79ad884327d2a918ec220495a9bb7d4ff954199
---

# S08 evidence card — X13 Google Calendar phase-4 stop rule

## Decision

`RETIRE` the active repeat-scouting campaign, while retaining `Google_Calendar.search_events` as a gated COTS catalog observation. Do not promote it to operational adoption and do not run another Calendar candidate call merely to increase evidence volume.

## Why

The existing campaign has already answered the bounded capability questions available from harmless search calls: one nonempty bounded search succeeded, one identical replay produced the same ordered normalized digest, and one synthetic nonmatch returned an empty success rather than a connector error. The same receipts also preserve the material limitation: matching searches hydrated full event descriptions, so the surface is not metadata-only.

The phase-4 economic/control signal is still zero: no named operational consumer, no ConsumerAck, no measured operator minutes removed, no raw-provider parity witness, and zero adoption or fitness credit. S03 and S04 independently preserve those binding gaps and cannot close them as same-provider verification.

## Stop rule

Retain the capability in `HFO_COTS_CAPABILITY_INVENTORY` with explicit time bounds, small result caps, no event-body persistence, no authoritative-absence claims, and direct-event or matched-provider verification for consequential claims. Reopen research only on named WorkItem consumption, a material connector-schema change, or contradictory same-principal provider evidence.
