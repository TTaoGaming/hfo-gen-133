---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CODE_SEARCH_READONLY_009
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
candidate: GitHub_repository_scoped_code_search_readonly_surface
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version: 135
expected_next_current_version: 136
prior_current_blob_sha: c906156bdb5bca76c3c561f9a4f4a643c63c251f
effect_ceiling: PHASE4_DECISION_ONLY_NO_ADDITIONAL_CANDIDATE_CALL
candidate_calls_this_phase: 0
source_bindings:
  phase1:
    commit: 39b2535d7c9abcaf8f78635fa9db4e827d8e9bc4
    path: state/coordination/experiments/cots_connector_x13/20260806T094757Z_GITHUB_CODE_SEARCH_PHASE1_ACCEPTED_WITH_GATES.md
    blob_sha: 973cc5254460a551929317fd9521f663354ec818
    commit_path_verified: true
  phase2:
    commit: e603e4e2bcbea20ead430071ffc9f5b1cb1e41a6
    path: state/coordination/experiments/cots_connector_x13/20260806T105018Z_GITHUB_CODE_SEARCH_PHASE2_DRIFT_CANARY_ACCEPTED_WITH_GATES.md
    blob_sha: e8e1a33ee04f48689be1f8703f228c80d36403a9
    commit_path_verified: true
  phase3:
    commit: 4c0fc847e503b98d3e86cb994359fdadce87968f
    path: state/coordination/experiments/cots_connector_x13/20260806T114752Z_GITHUB_CODE_SEARCH_PHASE3_EMPTY_SUCCESS_ACCEPTED_WITH_GATES.md
    blob_sha: 5adc7f4da7bfafec231ce69c3eb1e51593decf9d
    commit_path_verified: true
measured_campaign_summary:
  read_only_code_search_calls_total: 3
  successful_nonempty_calls: 2
  successful_empty_calls: 1
  connector_errors_observed: 0
  retries: 0
  fallbacks: 0
  repository_mutations_by_candidate: 0
  content_hydrations: 0
  phase1_path_only_results: 3
  phase2_path_only_results: 3
  phase2_search_result_commit_sha: b3ff3a2b44e6dd166a3698f8f499bb0694e5d4f9
  phase2_latest_repository_commit_observed: 4f0f47b0cfffde656658c38013e5a6bc36916109
  phase2_index_gap_commits_observed: 8
  phase3_empty_success_distinct_from_error: true
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials:
  connector_managed: true
  effective_identity: UNKNOWN
  permission_scope: UNKNOWN
  token_type_and_storage: UNKNOWN
durability:
  git_evidence: DURABLE
  search_results: MUTABLE_INDEXED_DISCOVERY
  result_urls: COMMIT_PINNED_WHEN_RETURNED
  negative_results: NOT_DURABLE_AUTHORITATIVE_ABSENCE
observability:
  exposed:
    - bounded_result_paths
    - commit_pinned_result_urls
    - empty_result_shape
    - connector_error_state
    - external_call_latency_on_phase3
  hidden:
    - raw_provider_request_and_response
    - total_count_and_incomplete_results_state
    - index_freshness_and_indexing_status
    - http_headers_and_request_id
    - effective_identity_and_permission_scope
    - rate_limit_bucket_debit_and_remaining
    - retry_and_internal_call_audit
portability:
  rating: LOW_TO_MEDIUM
  reason: GITHUB_CODE_SEARCH_INDEX_SCOPE_QUERY_BEHAVIOR_AND_RESULT_URLS_ARE_PROVIDER_SPECIFIC
failure_behavior:
  measured:
    - NONEMPTY_SUCCESS
    - INDEX_TO_REPOSITORY_HEAD_VARIANCE_CANARY
    - EMPTY_SUCCESS_DISTINGUISHED_FROM_ERROR
  unmeasured:
    - INVALID_QUERY
    - AUTHENTICATION_OR_PERMISSION_DENIAL
    - PRIVATE_REPOSITORY_VARIANCE
    - RATE_LIMIT
    - TRANSIENT_TRANSPORT_OR_SERVER_FAILURE
    - INDEX_UNAVAILABLE_OR_STALE
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_or_quota_evidence: NONE
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DISTINCT_RAW_GITHUB_CODE_SEARCH_UNDER_THE_SAME_EFFECTIVE_ACCESS_CONTEXT_PLUS_EXPLICIT_REF_GIT_TREE_OR_CONTENTS_WITNESS
verifier_result: NOT_RUN
strongest_falsifier: A_MATCHED_RAW_PROVIDER_SEARCH_RETURNS_MATERIALLY_DIFFERENT_PATHS_SCOPE_COMPLETENESS_ERROR_OR_RATE_LIMIT_BEHAVIOR_OR_AN_EXPLICIT_REF_GIT_WITNESS_CONTRADICTS_A_CONSEQUENTIAL_SEARCH_CLAIM
mandatory_gates:
  - VERIFY_DEFAULT_BRANCH_AND_REPOSITORY_SCOPE_BEFORE_RELYING_ON_RESULTS
  - TREAT_TOPN_AS_AN_OUTPUT_CAP_NOT_COMPLETENESS_EVIDENCE
  - TREAT_RESULTS_AS_INDEXED_DISCOVERY_NOT_AUTHORITATIVE_GIT_TREE_STATE
  - RETAIN_COMMIT_PINNED_URLS_OR_FOLLOW_WITH_EXPLICIT_REF_FILE_FETCH
  - TREAT_EMPTY_AS_ZERO_INDEXED_MATCHES_RETURNED_NOT_AUTHORITATIVE_ABSENCE
  - REQUIRE_EXPLICIT_REF_GIT_WITNESS_FOR_CONSEQUENTIAL_NEGATIVE_CLAIMS
  - DO_NOT_INFER_EFFECTIVE_IDENTITY_PERMISSION_INDEX_FRESHNESS_OR_QUOTA_FROM WRAPPER_SUCCESS
  - NO_UNBOUNDED_RETRY_OR_HIGH_RATE_POLLING_WHILE FAILURE_AND_QUOTA_TELEMETRY_ARE_HIDDEN
adoption_credit: 0
fitness_credit: 0
decision_basis: THE_CONNECTOR_SHOWED_BOUNDED_PATH_DISCOVERY_COMMIT_PINNED_RESULT_URLS_INDEX_DRIFT_VISIBILITY_AND_EMPTY_SUCCESS_CLASSIFICATION_BUT NO_OPERATIONAL_CONSUMER_ACK_RAW_PROVIDER_VERIFIER_MEASURED_OPERATOR_RELIEF_PERMISSION_FAILURE_OR_DIRECT_QUOTA_EVIDENCE
honest_flaw: THE_DECISION_RESTS_ON THREE_SMALL_SEARCH_CALLS_AGAINST_ONE_PUBLIC_REPOSITORY; PHASE1_DID_NOT_PERSIST_EXACT_QUERY_BYTES, PHASE2_WAS_A_DRIFT_CANARY_NOT_A_VALID_IDENTICAL_REPLAY, AND PRIVATE_ACCESS_INVALID_QUERY_RATE_LIMIT_TRANSIENT_FAILURE_RAW_PARITY_OPERATOR_SAVINGS_AND CONSUMER_VALUE_REMAIN_UNTESTED
next_campaign:
  experiment_id: X13_SLACK_SEARCH_PUBLIC_READONLY_010
  candidate: Slack_public_message_search_readonly_surface
  next_phase: PHASE1_PENDING
review_expiry_utc: 2026-08-13T12:48:36Z
valid_time_utc: 2026-08-06T12:48:36Z
recorded_time_utc: 2026-08-06T12:48:36Z
sealed: true
---

# X13 GitHub code search phase 4 — defer operational adoption

The four-wake campaign is closed with `DEFER` for operational adoption. The connector demonstrated bounded, repository-scoped path discovery, commit-pinned result URLs, an observable index-to-repository-head variance canary, and an empty-success result distinct from an explicit connector error. It made no repository mutation, hydrated no file content, retried zero times, and used no fallback.

That evidence is insufficient for operational adoption. No bound operational consumer acknowledged use, measured operator relief is zero, the raw GitHub verifier was not run, and the connector exposed no effective identity, permission scope, total-count or incomplete-results state, index-freshness receipt, provider request metadata, internal retry audit, or direct code-search rate-limit debit. The phase-2 result commit was eight commits behind the latest repository commit observed in that wake, directly showing that indexed discovery and repository head can diverge.

Retain the capability only as a bounded, human-reviewed catalog and discovery surface. Treat result limits as caps, retain commit pins, and verify consequential claims with an explicit-ref Git contents or tree witness. Empty results mean only `zero indexed matches returned`; they are not repository-wide absence. Reconsider operational adoption only after a named consumer records a real use, measured operator savings, and a distinct raw-provider plus explicit-ref verifier closes the access, completeness, freshness, and failure-behavior gaps.
