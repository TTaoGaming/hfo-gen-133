---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_READONLY_029
event_id: X13_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_PHASE4_ADOPT_WITH_GATES_20260809T204900Z
event_type: PHASE4_DECISION
phase: 4_of_4
phase_4_decision: ADOPT_WITH_GATES
disposition: ADOPT_WITH_GATES_BOUNDED_READONLY_METADATA_DISCOVERY_WITH_EXPLICIT_MIME_GATE
campaign_status: CLOSED
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 215
prior_current_blob_sha: e60d1662bdb9581a97c0581249ed69bb2e838518
candidate: Google_Drive.search_document_metadata_readonly
effect_ceiling: BOUNDED_READONLY_METADATA_DISCOVERY_NO_CONTENT_FETCH
phase_4_additional_candidate_calls: 0
source_events:
  phase_1:
    path: state/coordination/experiments/cots_connector_x13/20260809T175000Z_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_PHASE1_RESULT.md
    blob_sha: 4b1611cd8539b645745b6fa927e7c89f83a1ec00
  phase_2:
    path: state/coordination/experiments/cots_connector_x13/20260809T185000Z_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_PHASE2_RESULT.md
    blob_sha: dbf1b1978722a22f92d811d2ac94805132e0fabb
  phase_3:
    path: state/coordination/experiments/cots_connector_x13/20260809T195045Z_GOOGLE_DRIVE_DOCUMENT_METADATA_SEARCH_PHASE3_RESULT.md
    blob_sha: 433189ef07613632f3c7d4a8adbac0e6f05e51c2
campaign_measurements:
  candidate_invocations_total: 3
  usable_candidate_results: 3
  expected_failure_probes_total: 0
  connector_errors_total: 0
  retries_total: 0
  fallbacks_total: 0
  candidate_mutations_total: 0
  phase1_result_count: 5
  phase2_result_count: 5
  phase3_result_count: 5
  phase1_phase2_ordered_id_digest_match: true
  phase1_phase2_item_type_document_included_spreadsheet: true
  phase3_explicit_google_docs_mime_filter_returned_5_of_5_document_urls: true
  phase3_spreadsheet_resource_observed: false
  raw_mime_type_echo_observed: false
  content_hydrations: 0
  page2_fetches: 0
  operator_minutes_removed_measured: 0
  custom_code_avoided_realized_by_this_candidate: 0
  custom_code_avoided_estimate: 30_to_100_LOC_UNVALIDATED
credentials:
  connector_managed: true
  authenticated_principal: UNKNOWN
  effective_oauth_scope: UNKNOWN
  least_privilege_proven: false
durability:
  provider_metadata: PROVIDER_STORED
  workflow_resume_exactly_once: NOT_PROVIDED_BY_CANDIDATE
  experiment_receipts: IMMUTABLE_GIT_EVENTS_PLUS_VERSIONED_CURRENT_WITH_READBACK
observability:
  proven:
    - BOUNDED_RESULT_COUNTS
    - PRIVACY_SAFE_ORDERED_ID_DIGEST_STABILITY_ACROSS_PHASE1_PHASE2
    - NO_FILE_CONTENT_HYDRATION_OBSERVED
    - CONNECTOR_DOCUMENT_TAXONOMY_VARIANCE_REPRODUCED
    - EXPLICIT_NATIVE_MIME_QUERY_NARROWED_OBSERVED_RESULT_URL_CLASS_TO_GOOGLE_DOCS
  absent:
    - RAW_MIME_TYPE_ECHO
    - AUTHENTICATED_PRINCIPAL_AND_EFFECTIVE_SCOPE
    - NATIVE_REQUEST_ID
    - RATE_LIMIT_HEADERS
    - DIRECT_QUOTA_DEBIT
    - BILLING_RECEIPT
    - CALL_LATENCY
    - VALID_PAGINATION_WITNESS
    - AUTHORITATIVE_COMPLETENESS_SIGNAL
portability:
  rating: MEDIUM_HIGH_WITH_EXPLICIT_NATIVE_DRIVE_Q_MIME_FILTER
  caveat: CONNECTOR_ITEM_TYPE_DOCUMENT_ALONE_IS_NOT_GOOGLE_DOCS_ONLY_AND_EXACT_PROVIDER_QUERY_MAPPING_IS_UNVERIFIED
failure_behavior:
  directly_probed: false
  observed_success_path: THREE_BOUNDED_READ_SUCCESSES_NO_RETRY_FALLBACK_OR_MUTATION
  permission_denial: UNPROBED
  rate_limit_or_transient_failure: UNPROBED
direct_cost_and_quota_evidence:
  paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
  direct_connector_quota_evidence: NONE
  provider_billing_receipt: ABSENT
verifier:
  current: GIT_DURABLE_READBACK_PLUS_DIRECT_DRIVE_RECEIPTS_PLUS_OFFICIAL_DRIVE_Q_AND_MIME_CONTRACT
  missing_strong_witness: SAME_PRINCIPAL_RAW_DRIVE_FILES_LIST_OR_CONNECTOR_MIME_ECHO_AND_VALID_PAGINATION_PERMISSION_FAILURE_QUOTA_SCOPE_EVIDENCE
consumer:
  named: HFO_BOUNDED_DRIVE_DISCOVERY_FOR_OPERATOR_CONTROL_LOOPS
  measured_operator_value: NONE_YET
  adoption_credit: 1
  fitness_credit: 0
strongest_falsifier: FUTURE_EXPLICIT_GOOGLE_DOCS_MIME_FILTER_RETURNS_NON_DOCS_RESOURCE_OR_CONNECTOR_IGNORES_SPECIAL_FILTER_QUERY_STR_OR_CONSUMER_REQUIRES_AUTHORITATIVE_COMPLETENESS_PERMISSION_CLASSIFICATION_OR_LEAST_PRIVILEGE_PROOF
mandatory_gates:
  - READ_ONLY_ONLY
  - BEST_EFFORT_FETCH_FALSE
  - TOPN_5_OR_LOWER_UNLESS_SEPARATELY_VALIDATED
  - NO_SECOND_PAGE_UNTIL_VALID_PAGINATION_IS_SEPARATELY_PROVEN
  - DO_NOT_PERSIST_RAW_NAMES_IDS_URLS_PARENT_IDS_QUERIES_OR_PAGE_TOKENS_UNLESS_MINIMUM_NECESSARY
  - DO_NOT_TREAT_ITEM_TYPE_DOCUMENT_AS_GOOGLE_DOCS_ONLY
  - WHEN_GOOGLE_DOCS_ONLY_SEMANTICS_MATTER_REQUIRE_SPECIAL_FILTER_QUERY_STR_MIMETYPE_APPLICATION_VND_GOOGLE_APPS_DOCUMENT
  - DO_NOT_CLAIM_AUTHORITATIVE_COMPLETENESS_ABSENCE_ORDERING_PERMISSION_CLASSIFICATION_SCOPE_RATE_LIMIT_QUOTA_OR_BILLING
  - FAIL_CLOSED_IF_EXPLICIT_MIME_FILTER_RETURNS_A_NON_DOCS_RESOURCE
adopted_boundary:
  allowed:
    - BOUNDED_READONLY_METADATA_DISCOVERY
    - LOW_ASSURANCE_OPERATOR_ASSISTANCE
    - GOOGLE_DOCS_ONLY_DISCOVERY_WHEN_EXPLICIT_NATIVE_MIME_FILTER_IS_PRESENT_AND_RESULT_CLASS_IS_REVIEWED
  forbidden:
    - CONTENT_HYDRATION
    - AUTHORITATIVE_ABSENCE_OR_COMPLETENESS_CLAIMS
    - AUTOMATED_FILE_SELECTION_ROUTING_DELETION_OR_PUBLICATION
    - UNBOUNDED_PAGINATION_OR_RETRY
    - PERMISSION_CLASSIFICATION
    - OPERATIONAL_FITNESS_CREDIT_WITHOUT_MEASURED_OPERATOR_VALUE
honest_flaw: PHASE3_USED_CONNECTOR_VARIANCE_INSTEAD_OF_A_FAILURE_OR_PERMISSION_PROBE; THE_CONNECTOR_DID_NOT_ECHO_RAW_MIME_TYPE; FIVE_GOOGLE_DOCS_URLS_ARE STRONG_PRACTICAL_BUT_NOT_AUTHORITATIVE_PROVIDER_SIDE_FILTER_PROOF; VALID_PAGINATION_IDENTITY_SCOPE_RATE_LIMIT_QUOTA_DEBIT_BILLING_LATENCY_COMPLETENESS_AND_PERMISSION_BEHAVIOR_REMAIN_UNVERIFIED
next_campaign:
  candidate: UNSELECTED
  next_phase: 1_of_4
  action_this_wake: NONE
valid_time_utc: 2026-08-09T20:49:00Z
recorded_time_utc: 2026-08-09T20:49:00Z
---

# X13 Phase 4 decision — Google Drive document metadata search

Decision: `ADOPT_WITH_GATES` for bounded, read-only metadata discovery only. Across three calls, the connector returned three usable five-result metadata pages with no observed content hydration, retries, fallbacks, connector errors, or Drive mutations. Phase 1 and Phase 2 reproduced the material taxonomy flaw: `item_type=document` included a spreadsheet. Phase 3 showed that adding the explicit native Google Docs MIME query narrowed the observed five-result class to Google Docs document URLs with no spreadsheet resource.

The practical adoption rule is therefore explicit: never treat connector `item_type=document` as Google-Docs-only semantics; require `mimeType = 'application/vnd.google-apps.document'` in the native Drive query when Google Docs-only behavior matters. Because the connector did not echo raw MIME type, this remains provisional rather than authoritative provider-side query proof.

Measured operator minutes removed remain zero. Realized custom-code avoidance remains zero; the 30–100 LOC avoidance estimate remains unvalidated. Principal/scope, valid pagination, permission-denial behavior, rate limits, quota debit, billing, latency, exact native request mapping, and authoritative completeness remain unproven. Adoption credit is 1 for the narrow bounded envelope; fitness credit is 0 pending measured operator value and stronger verification.
