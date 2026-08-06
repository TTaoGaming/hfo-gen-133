---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_SEARCH_READONLY_008
event_type: PHASE4_ADOPTION_DECISION
phase: 4
phase_status: COMPLETE
campaign_wake: 4_of_4
campaign_status: COMPLETE
adoption_decision: DEFER
operational_decision: DEFER_OPERATIONAL_ADOPTION_CATALOG_ONLY
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Gmail_search_email_ids_readonly_surface
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version: 131
expected_next_current_version: 132
prior_current_blob_sha: 98a43038ba4308ebd5356ee7c05ad360ee5c1e3d
effect_ceiling: PHASE4_DECISION_ONLY_NO_ADDITIONAL_GMAIL_CALL
candidate_calls_this_phase: 0
source_bindings:
  phase1:
    commit: db4e26cee37d52189af1d019f64e225a2c0f2f4b
    path: state/coordination/experiments/cots_connector_x13/20260806T054917Z_GMAIL_SEARCH_PHASE1_BASELINE.md
    blob_sha: 8d4f4b9f81698a138e4a24724ffb65d711fc4699
    commit_path_verified: true
  phase2:
    commit: 102886dfcfd08b63251d8c85823a95645d5d3d08
    path: state/coordination/experiments/cots_connector_x13/20260806T065056Z_GMAIL_SEARCH_PHASE2_ABSOLUTE_REPEATABILITY.md
    blob_sha: c43cf2c1d6f97002c2fac7aa4b6b038ff87d84ad
    commit_path_verified: true
  phase3:
    commit: 1c6824da08cec785b850503c8f5a9c22d1fe3807
    path: state/coordination/experiments/cots_connector_x13/20260806T074749Z_GMAIL_SEARCH_PHASE3_EMPTY_SUCCESS.md
    blob_sha: 318b95850c8c058f358a59da7e91164e349c9643
    commit_path_verified: true
measured_campaign_summary:
  read_only_id_search_calls_total: 4
  phase1_dynamic_success_calls: 1
  phase2_fixed_window_repeatability_calls: 2
  phase3_synthetic_empty_success_calls: 1
  successful_nonempty_calls: 3
  successful_empty_calls: 1
  connector_errors_observed: 0
  retries: 0
  fallbacks: 0
  mailbox_mutations: 0
  content_hydrations: 0
  phase2_message_id_digest_match: true
  phase2_continuation_token_digest_match: true
  phase3_empty_success_distinct_from_error: true
custom_code_avoided_estimate: 25_to_70_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials:
  connector_managed: true
  effective_identity: UNKNOWN
  oauth_scope: UNKNOWN
  cloud_project: UNKNOWN
  token_type_and_storage: UNKNOWN
durability:
  git_evidence: DURABLE
  mailbox_results: DYNAMIC
  page_tokens: OPAQUE_AND_NOT_DURABLE_STATE
  negative_results: NOT_DURABLE_AUTHORITATIVE_ABSENCE
observability:
  exposed:
    - result_count
    - continuation_presence
    - connector_error_state
    - connector_external_latency
  hidden:
    - raw_provider_request_and_response
    - result_size_estimate
    - http_headers_and_request_id
    - effective_identity_and_oauth_scope
    - cloud_project_and_quota_bucket
    - retry_and_internal_call_audit
portability:
  rating: LOW_TO_MEDIUM
  reason: GMAIL_QUERY_GRAMMAR_MESSAGE_IDS_AND_PAGE_TOKENS_ARE_PROVIDER_SPECIFIC_AND_EPOCH_OPERATOR_FORM_WAS_UNDOCUMENTED
failure_behavior:
  measured:
    - SUCCESS_WITH_CONTINUATION
    - NEAR_IMMEDIATE_FIXED_QUERY_REPEATABILITY
    - EMPTY_SUCCESS_WITH_NULL_CONTINUATION_AND_NULL_CONNECTOR_ERROR
  unmeasured:
    - INVALID_QUERY
    - AUTHENTICATION_OR_PERMISSION_DENIAL
    - RATE_LIMIT
    - TRANSIENT_TRANSPORT_OR_SERVER_FAILURE
    - PAGINATION_ACROSS_MULTIPLE_PAGES
    - STALE_CURSOR
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
nominal_quota_contract: 5_UNITS_PER_USERS_MESSAGES_LIST_REQUEST
nominal_quota_if_one_to_one_campaign_total: 20_UNITS
actual_quota_consumed: UNKNOWN
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DISTINCT_RAW_GMAIL_USERS_MESSAGES_LIST_CALL_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_WITH_EQUIVALENT_FIXED_AND_SYNTHETIC_QUERIES
verifier_result: NOT_RUN
strongest_falsifier: A_MATCHED_RAW_PROVIDER_CALL_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_RETURNS_MATERIALLY_DIFFERENT_MESSAGE_PAGINATION_ERROR_RESULT_ESTIMATE_OR_QUOTA_BEHAVIOR_OR_REJECTS_THE_EPOCH_QUERY_FORM
mandatory_gates:
  - TREAT_MAX_RESULTS_AS_AN_OUTPUT_CAP_NOT_COMPLETENESS_EVIDENCE
  - HANDLE_CONTINUATION_EXPLICITLY_AND_DO_NOT_TREAT_PAGE_TOKENS_AS_DURABLE_STATE
  - KEEP_SEARCHES_ID_ONLY_UNTIL_A_BOUND_CONSUMER_REQUIRES_CONTENT
  - DO_NOT_PERSIST_RAW_MESSAGE_IDS_PAGE_TOKENS_OR_PRIVATE_QUERY_TERMS_BY_DEFAULT
  - USE_DOCUMENTED_DATE_OPERATORS_FOR_PORTABLE_OPERATIONAL_QUERIES
  - TREAT_EMPTY_AS_NO_VISIBLE_MATCHES_RETURNED_NOT_AUTHORITATIVE_ABSENCE
  - REQUIRE_AN_INDEPENDENT_RAW_PROVIDER_WITNESS_FOR_CONSEQUENTIAL_NEGATIVE_CLAIMS
  - DO_NOT_INFER_EFFECTIVE_IDENTITY_SCOPE_PROJECT_PROVIDER_METHOD_OR_QUOTA_FROM_WRAPPER_SUCCESS
  - NO_UNBOUNDED_RETRY_OR_HIGH_RATE_POLLING_WHILE_FAILURE_AND_QUOTA_TELEMETRY_ARE_HIDDEN
adoption_credit: 0
fitness_credit: 0
decision_basis: THE_CONNECTOR_SHOWED_BOUNDED_ID_ONLY_DISCOVERY_NARROW_REPEATABILITY_AND_EMPTY_SUCCESS_CLASSIFICATION_BUT_NO_OPERATIONAL_CONSUMER_ACK_RAW_PROVIDER_VERIFIER_MEASURED_OPERATOR_RELIEF_PERMISSION_OR_RATE_LIMIT_EVIDENCE_OR_DIRECT_QUOTA_RECEIPT
honest_flaw: THE_DECISION_RESTS_ON_FOUR_SMALL_WRAPPER_CALLS_WITHOUT_CONTENT_HYDRATION_OR_MUTATION; INVALID_QUERY_PERMISSION_RATE_LIMIT_TRANSIENT_FAILURE_MULTI_PAGE_PAGINATION_LATER_REPLAY_RAW_PROVIDER_PARITY_OPERATOR_SAVINGS_AND_CONSUMER_VALUE_REMAIN_UNTESTED
next_campaign:
  experiment_id: X13_GITHUB_CODE_SEARCH_READONLY_009
  candidate: GitHub_repository_scoped_code_search_readonly_surface
  next_phase: PHASE1_PENDING
review_expiry_utc: 2026-08-13T08:49:08Z
valid_time_utc: 2026-08-06T08:49:08Z
recorded_time_utc: 2026-08-06T08:49:08Z
sealed: true
---

# X13 Gmail search phase 4 — defer operational adoption

The four-wake campaign is closed with `DEFER` for operational adoption. The Gmail connector demonstrated bounded, read-only message-ID discovery, near-immediate repeatability for one fixed query, and an empty-success result distinct from an explicit connector error. It did not hydrate message content, mutate the mailbox, retry, or fall back.

That evidence is insufficient for an operational adoption claim. No WorkItem or operational consumer consumed the capability, measured operator relief is zero, the raw Gmail verifier was not run, and the connector did not expose effective identity, OAuth scope, Cloud project, provider request metadata, result-size estimate, retry audit, or direct quota debit. Permission denial, invalid syntax, throttling, transient failure, multi-page pagination, stale cursors, and later replay remain untested.

Retain the capability only as a bounded, human-reviewed catalog surface. Treat limits as caps, handle continuation explicitly, keep searches ID-only by default, and treat empty results as `no visible matches returned`, never authoritative absence. Operational adoption can be reconsidered only after a named consumer records a real use, measured operator savings, and a distinct raw-provider or equivalent verifier closes the principal, query, pagination, and failure-behavior gaps.
