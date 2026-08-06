---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_SEARCH_READONLY_011
event_type: PHASE2_REPLAY
campaign_wake: 2_of_4
candidate: Google_Drive_search_readonly_surface
phase_status: PHASE2_ACCEPTED_WITH_GATES
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
prior_current_version: 141
expected_current_version: 142
candidate_calls_this_phase: 1
campaign_calls_total: 2
successful_nonempty_calls_total: 2
successful_empty_calls_total: 0
connector_errors_observed_total: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
content_hydration_calls_total: 0
query_text: HFO
result_cap: 3
returned_results: 3
item_type_requested: document
metadata_only_requested: true
require_viewed_by_user: false
page_token_supplied: false
next_page_token_exposed: false
phase_1_request_sha256: 79767544a7dad65b37076f7451004ef150c34b34a0004b963d3435865934cf44
phase_2_request_sha256: 79767544a7dad65b37076f7451004ef150c34b34a0004b963d3435865934cf44
request_digest_match: true
phase_1_result_sha256: bf2c598f6fcb44b8ab456bec613adca06d05f43473e75f2943bbf3dbaeace43b
phase_2_result_sha256: bf2c598f6fcb44b8ab456bec613adca06d05f43473e75f2943bbf3dbaeace43b
normalized_result_digest_match: true
normalization_contract: ORDERED_RESULTS_SORTED_KEYS_COMPACT_JSON_OVER_ID_TITLE_URL_PARENT_IDS
raw_result_ids_persisted: false
raw_parent_ids_persisted: false
approx_seconds_since_phase_1_event: 3570
measured_fact: IDENTICAL_BOUNDED_METADATA_ONLY_REPLAY_RETURNED_THE_SAME_THREE_ORDERED_RESULTS_AND_DIGEST
interpretation: NARROW_NEAR_TERM_REPEATABILITY_ONLY_NOT_COMPLETENESS_DETERMINISM_FRESHNESS_OR_PROVIDER_PARITY
custom_code_avoided_estimate: 50_to_150_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_IDENTITY_AND_SCOPES_UNKNOWN
durability: GIT_EVENT_DURABLE_DRIVE_SEARCH_RESULTS_AND_ORDER_MUTABLE_NO_PROVIDER_SNAPSHOT_RECEIPT
observability: COUNT_ID_TITLE_URL_PARENT_IDS_AND_DIGEST_EXPOSED; MIME_MODIFIED_TIME_OWNER_REQUEST_ID_QUOTA_AND_FRESHNESS_NOT_EXPOSED
portability: LOW_TO_MEDIUM_WRAPPER_AND_DRIVE_SPECIFIC
failure_behavior: TWO_NONEMPTY_MATCHING_REPLAYS; EMPTY_DENIAL_RATE_LIMIT_TRANSIENT_AND_PAGINATION_UNTESTED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_or_quota_evidence: NONE
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: MATCHED_RAW_DRIVE_V3_FILES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL
verifier_result: NOT_RUN
adoption_credit: 0
fitness_credit: 0
mandatory_gates: METADATA_ONLY; TOPN_IS_A_CAP_NOT_COMPLETENESS; DOCUMENT_IS_A_WRAPPER_CATEGORY_NOT_GOOGLE_DOCS_MIME; VERIFY_CONSEQUENTIAL_CLAIMS_WITH_DIRECT_METADATA_OR_MATCHED_PROVIDER; NO_UNBOUNDED_RETRY
strongest_falsifier: MATCHED_RAW_PROVIDER_RESULTS_DIFFER_MATERIALLY_OR_A_LATER_IDENTICAL_REPLAY_DRIFTS_WITHOUT_A_VISIBLE_FILE_CHANGE
honest_flaw: TWO_MATCHING_THREE_RESULT_CALLS_FOR_ONE_KNOWN_QUERY_DO_NOT_TEST_EMPTY_PERMISSION_SHARED_DRIVE_PAGINATION_RATE_LIMIT_TRANSIENT_FAILURE_OPERATOR_SAVINGS_OR_CONSUMER_VALUE
next_phase: PHASE3_BOUNDED_SYNTHETIC_NONMATCHING_METADATA_ONLY_SEARCH
valid_time_utc: 2026-08-06T18:48:02Z
recorded_time_utc: 2026-08-06T18:48:02Z
---

# X13 Drive search phase 2

The identical bounded metadata-only request returned the same three ordered results and normalized digest as phase 1 after about 59 minutes 30 seconds.

This supports only narrow near-term repeatability for one known query. It does not establish completeness, provider ordering, freshness, MIME correctness, authorization, pagination durability, or raw-provider parity.

## Measures

| Measure | Result |
|---|---:|
| Calls this phase | 1 |
| Campaign calls | 2 |
| Results | 3 |
| Request digest match | Yes |
| Result digest match | Yes |
| Retries / fallbacks / mutations | 0 / 0 / 0 |
| Content hydration | 0 |
| Operator minutes removed | 0 |
| Surfaced paid cost | $0 |
| Direct quota receipt | None |
| Adoption / fitness credit | 0 / 0 |

Next: one bounded synthetic nonmatching metadata-only search, with no retry and no authoritative absence claim.
