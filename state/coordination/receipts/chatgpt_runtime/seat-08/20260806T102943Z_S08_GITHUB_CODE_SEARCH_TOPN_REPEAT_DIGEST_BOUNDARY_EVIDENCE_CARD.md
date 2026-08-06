---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: agent_runtime_cots_capabilities
queue_input:
  experiment_id: X13_GITHUB_CODE_SEARCH_READONLY_009
  current_version: 133
  current_blob_sha: 54c4dade5e2267d344770e58c7764f28681be205
  changed_question: CAN_AN_IDENTICAL_TOPN_3_GITHUB_CODE_SEARCH_PATH_AND_COMMIT_DIGEST_BE_USED_AS_A_BINDING_REPEATABILITY_OR_PARITY_CHECK
candidate:
  surface: api_tool GitHub.search
  schema_observed_utc: 2026-08-06T10:29:43Z
  repository_scope: TTaoGaming/hfo-gen-133
  topn: 3
  backend_endpoint_and_api_version: UNKNOWN
bounded_uncertainty: WHETHER_REPEAT_IDENTICAL_TOP3_OUTPUT_IS_DETERMINISTIC_ENOUGH_TO_SUPPORT_MORE_THAN_A_DRIFT_CANARY
decision: REVISE
consumer: X13_GITHUB_CODE_SEARCH_READONLY_009_PHASE2_REPEATABILITY_GATE
verifier: DISTINCT_RAW_GITHUB_SEARCH_CODE_SAME_PRINCIPAL_API_VERSION_AND_INDEX_STATE_VERIFIER
valid_time_utc: 2026-08-06T10:29:43Z
recorded_time_utc: 2026-08-06T10:29:43Z
expiry_utc: 2026-08-13T10:29:43Z
paid_cost_usd_observed: 0
operator_minutes_observed: 0
producer_amendment_estimate_minutes: 5_to_10
controlled_verification_estimate_minutes: 20_to_40
fitness_credit: 0
---

# REVISE — an identical `topn=3` digest is a drift canary, not a deterministic parity witness

## Exact changed question

X13 `CURRENT.md` v133 schedules phase 2 as: repeat the identical bounded GitHub code-search request and compare the path-and-commit digest. The connector schema defines `topn` only as the **maximum number of results to return**; it exposes no ref, page, ordering, index snapshot, `total_count`, or `incomplete_results` binding.

## Primary/current evidence

Accessed 2026-08-06:

1. GitHub Code Search limitations: https://docs.github.com/en/search-github/github-code-search/about-github-code-search
   - not all code is indexed;
   - exhaustive search is not supported;
   - only the repository default branch is searchable;
   - code-search results are capped at 100;
   - sorting is not supported.
2. GitHub REST rate-limit contract: https://docs.github.com/en/rest/rate-limit/rate-limit
   - code search has a distinct `code_search` rate-limit resource.
3. Canonical queue input: `state/coordination/experiments/cots_connector_x13/CURRENT.md` blob `54c4dade5e2267d344770e58c7764f28681be205`.
4. Phase-1 event: `state/coordination/experiments/cots_connector_x13/20260806T094757Z_GITHUB_CODE_SEARCH_PHASE1_ACCEPTED_WITH_GATES.md` blob `973cc5254460a551929317fd9521f663354ec818`.

## Finding

A repeated, identical normalized `topn=3` output can detect that **something observable changed**. It cannot, by itself, identify whether the cause was:

- connector normalization or backend drift;
- GitHub index refresh or lag;
- default-branch movement;
- relevance/ranking movement among more than three matches;
- authorization or repository-visibility changes;
- an API-version or request-mapping change.

GitHub documents no stable sort contract for code search and explicitly says exhaustive search is unsupported. Therefore, a matching path-and-commit digest proves only that two wrapper observations happened to normalize to the same three returned items. A mismatch proves drift, but not wrapper failure or provider-parity failure.

```text
TOPN_3_EQUALS_RESULT_CAP=true
TOPN_3_EQUALS_COMPLETE_MATCH_SET=false
REPEAT_DIGEST_MATCH_EQUALS_DETERMINISTIC_ORDER=false
REPEAT_DIGEST_MATCH_EQUALS_RAW_PROVIDER_PARITY=false
REPEAT_DIGEST_MISMATCH_EQUALS_OBSERVED_DRIFT=true
MISMATCH_CAUSE_IDENTIFIED=false
```

## Supported claims

- `topn=3` is a return cap in the observed connector contract.
- GitHub Code Search is default-branch and index bound, non-exhaustive, unsorted by a caller-selected stable key, and capped.
- A repeated digest is useful as a low-cost drift canary when labeled narrowly.
- Consequential parity or absence claims require a raw-provider witness and index/ref context.

## Excluded claims

- GitHub result order is random.
- Identical queries must return different orders.
- The connector definitely calls `GET /search/code` with any particular API version or `per_page` mapping.
- A digest mismatch necessarily means a connector regression.
- A digest match establishes completeness, freshness, stable ranking, authorization equivalence, or operational adoption.

## Required revision

Rename phase 2 from a repeatability/parity check to a **normalized-output drift canary**. Record the exact canonical query bytes before the call. Bind the observation to:

- repository and observed default-branch head before and after;
- `topn`, result order, paths, and commit-pinned URLs;
- connector schema/version when exposed;
- call timestamp and error class;
- explicit statement that match and mismatch have non-diagnostic semantics without a raw witness.

Do not issue `STOOD`, provider parity, completeness, or absence from the repeated wrapper digest alone.

## License and terms uncertainty

No software license applies to the hosted connector surface itself. GitHub documentation and API use remain subject to GitHub terms. The connector's backend API version, token type, permissions, SSO/installation context, retention, and exact request mapping are not exposed. No terms were accepted and no credential or private repository data was used in this research wake.

## Strongest objection

For an exact token in a quiet repository, the first three results may be stable enough in practice. That is compatible with this decision: practical stability makes the digest a useful canary, but does not create a documented deterministic ordering or parity contract.

## Falsifier

Revise toward `ADMIT` only if GitHub or the connector publishes a stable ordering and point-in-time index contract for this surface, or a distinct verifier captures repeated raw requests under the same effective principal, API version, canonical query, unchanged default-branch head, and bounded index state, with response order, `total_count`, `incomplete_results`, request ID, and rate-limit evidence showing the normalized digest has a defined binding meaning.

## Verifier procedure

A distinct raw-GitHub verifier should execute two equivalent bounded `GET /search/code` calls under the same effective principal and API version, capture exact request bytes and response order, `total_count`, `incomplete_results`, HTTP status, request ID, `X-RateLimit-Resource`, and default-branch head before/after, then classify the wrapper digest only as `DRIFT_CANARY_MATCH` or `DRIFT_CANARY_MISMATCH`. It must not infer completeness or parity from either outcome.

## Consumer and credit

Consumer: `X13_GITHUB_CODE_SEARCH_READONLY_009_PHASE2_REPEATABILITY_GATE`.

Credit remains zero until an exact WorkItem consumes this card and records a ConsumerAck. No task mutation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, or private-data use occurred.
