---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CODE_SEARCH_READONLY_009
candidate: GitHub_repository_scoped_code_search_readonly_surface
phase: 1
campaign_wake: 1_of_4
status: PHASE1_ACCEPTED_WITH_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version_expected: 132
request_digest_sha256: 2365cb47b5e6d3bd0aad7747c1fdf1ba9645e1e7d7906d189d69836ff84d5347
request_class: REPOSITORY_SCOPED_EXACT_TOKEN_SEARCH_TOP3
raw_query_persisted: false
search_repository_scope: TTaoGaming/hfo-gen-133
search_topn: 3
results_returned: 3
result_class: THREE_PATH_ONLY_MATCHES_WITH_COMMIT_PINNED_URLS
result_commit_sha_observed: d6029c6c36e29a76f67ce662bc73d016bea14557
result_summary_digest_sha256: edef35734a05ac00fe1d1d4c1d6912c314dc2c85e9768d7ef9abfbd40e006bbb
repository_default_branch_observed: agent/gen133-bootstrap-20260730
repository_default_branch_matches_canonical: true
repository_metadata_external_call_ms: 265
search_external_call_ms: NOT_EXPOSED
retries: 0
fallbacks: 0
mutations_by_candidate: 0
content_hydrated_by_candidate: false
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_SEARCH_PRINCIPAL_TOKEN_TYPE_SCOPE_SSO_AND_INSTALLATION_CONTEXT_NOT_EXPOSED
durability: GIT_EVENT_DURABLE_SEARCH_INDEX_AND_RANKING_MUTABLE_RESULT_URLS_COMMIT_PINNED
observability: PATH_URL_AND_RETURN_COUNT_EXPOSED_TOTAL_COUNT_INCOMPLETE_RESULTS_SCORE_TEXT_MATCHES_INDEX_FRESHNESS_HEADERS_REQUEST_ID_AUTH_CONTEXT_AND_RATE_LIMIT_NOT_EXPOSED
portability: LOW_TO_MEDIUM_GITHUB_SPECIFIC_INDEX_QUERY_AND_COMMIT_URL_MODEL
failure_behavior: SUCCESS_PATH_ONLY_EMPTY_INVALID_QUERY_PERMISSION_INDEX_UNAVAILABLE_THROTTLE_AND_TRANSIENT_FAILURE_UNTESTED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_or_quota_evidence: NONE
quota_contract: GITHUB_EXPOSES_A_DISTINCT_CODE_SEARCH_RATE_LIMIT_RESOURCE_BUT_WRAPPER_DID_NOT_EXPOSE_DEBIT_HEADERS_OR_BUCKET_STATE
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DISTINCT_RAW_GITHUB_GET_SEARCH_CODE_CALL_UNDER_SAME_EFFECTIVE_PRINCIPAL_AND_EQUIVALENT_REPOSITORY_SCOPED_QUERY
verifier_result: NOT_RUN
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
adoption_credit: 0
fitness_credit: 0
measured_fact: REPOSITORY_SCOPED_SEARCH_RETURNED_THREE_PATH_MATCHES_WITH_COMMIT_PINNED_URLS_AND_NO_CONTENT_HYDRATION
andon: SEARCH_HAS_NO_REF_PARAMETER_AND_GITHUB_CODE_SEARCH_INDEXES_THE_DEFAULT_BRANCH_ONLY_SO_NONDEFAULT_OR_UNINDEXED_STATE_MUST_NOT_BE_TREATED_AS_ABSENT
mandatory_gate: VERIFY_REPOSITORY_DEFAULT_BRANCH; TREAT_TOPN_AS_CAP_NOT_COMPLETENESS; TREAT_RESULTS_AS_INDEXED_DISCOVERY_NOT_AUTHORITATIVE_TREE_STATE; RETAIN_COMMIT_PINNED_URL_OR_FETCH_BY_PATH_AND_EXPLICIT_REF; REQUIRE_RAW_WITNESS_FOR_CONSEQUENTIAL_NEGATIVE_CLAIMS; DO_NOT_INFER_AUTH_INDEX_FRESHNESS_OR_QUOTA; NO_UNBOUNDED_RETRY
strongest_falsifier: MATCHED_RAW_GET_SEARCH_CODE_CALL_RETURNS_MATERIALLY_DIFFERENT_PATHS_COMMIT_ASSOCIATION_TOTAL_COUNT_INCOMPLETE_RESULTS_OR_RATE_LIMIT_BEHAVIOR_OR_PROVES_THE_WRAPPER_SEARCHED_A_DIFFERENT_REF
honest_flaw: ONE_EXACT_TOKEN_SUCCESS_QUERY_OVER_ONE_PUBLIC_REPOSITORY_DID_NOT_TEST_EMPTY_RESULTS_QUERY_SYNTAX_PERMISSION_PRIVATE_REPOSITORY_INDEX_LAG_BRANCH_VARIANCE_THROTTLING_TRANSIENT_FAILURE_RAW_PROVIDER_PARITY_OPERATOR_SAVINGS_OR_CONSUMER_VALUE
next_phase: PHASE2_REPEAT_IDENTICAL_BOUNDED_QUERY_AND_COMPARE_PATH_AND_COMMIT_DIGEST
valid_time_utc: 2026-08-06T09:47:57Z
recorded_time_utc: 2026-08-06T09:47:57Z
---

# X13 GitHub repository-scoped code search — phase 1

## Direct baseline

A single bounded read-only `GitHub.search` call used an exact known token, `topn=3`, and repository scope `TTaoGaming/hfo-gen-133`. It returned three path-only matches. All returned URLs were pinned to commit `d6029c6c36e29a76f67ce662bc73d016bea14557`; no file body or snippet was hydrated.

A separate repository metadata read reported the canonical branch `agent/gen133-bootstrap-20260730` as the repository default branch. That matters because GitHub code search indexes only the default branch. The connector search action exposes no branch or commit-ref parameter.

## Official contract baseline

Primary references checked:

- GitHub REST search endpoint: https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-code
- GitHub code-search branch/index contract: https://docs.github.com/en/search-github/github-code-search/about-github-code-search
- GitHub REST rate-limit contract: https://docs.github.com/en/rest/rate-limit/rate-limit

GitHub exposes code search as `GET /search/code`, requires a nonempty query, and maintains a distinct `code_search` rate-limit resource. Search results are index-derived and default-branch-bound; they are not an authoritative traversal of an arbitrary Git ref.

## Evidence boundary

The wrapper exposed result paths and commit-pinned URLs but omitted `total_count`, `incomplete_results`, ranking score, text-match metadata, index freshness, HTTP status, provider request ID, effective authentication context, and rate-limit headers. Therefore a success result establishes bounded indexed discovery only.

No measured operator relief, operational consumer, ConsumerAck, raw-provider parity witness, direct quota debit, or adoption credit exists.

## Andon

Do not use this surface to prove absence on a nondefault branch, an unindexed commit, or a repository whose index state is unknown. A zero-result response would mean only that this search call returned no indexed matches under its effective scope.
