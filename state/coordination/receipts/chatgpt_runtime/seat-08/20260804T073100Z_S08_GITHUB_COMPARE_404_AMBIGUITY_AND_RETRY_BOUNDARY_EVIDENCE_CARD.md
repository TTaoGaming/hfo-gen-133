---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
lane: AGENT_RUNTIME_COTS_CAPABILITIES
result: REVISE
observed_utc: 2026-08-04T07:31:00Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
question: >-
  What can one invalid-or-unknown full-SHA GitHub compare failure establish,
  and which retry and classification boundary should X13 phase 3 enforce?
exact_candidate:
  connector_action: GitHub.compare_commits
  connector_version: NOT_EXPOSED
  underlying_endpoint: GET /repos/{owner}/{repo}/compare/{basehead}
  official_api_version_observed: 2026-03-10
current_workitem:
  id: X13_GITHUB_COMPARE_COMMITS_READONLY_001
  current_version: 82
  source_commit: 17235637e3a60db39f62dc4f3345d7ab64ee7ffa
  source_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
  source_blob_sha: fd66e92e90947a95dc6dfaf5e694bf7965cff315
  planned_phase: 3_of_4
  planned_probe: ONE_NON_SECRET_INVALID_OR_UNKNOWN_FULL_SHA_COMPARE_TO_OBSERVE_FAILURE_NORMALIZATION_WITHOUT_RETRY
consumer:
  immediate: X13_GITHUB_COMPARE_COMMITS_READONLY_001_PHASE3
  downstream: HFO_COTS_CAPABILITY_INVENTORY
verifier: AUTHORIZED_NONPRODUCER_RAW_GITHUB_COMPARE_WITNESS_ON_THE_SAME_REPOSITORY_AND_SYNTHETIC_REF_CLASS
expiry_utc: 2026-08-11T07:31:00Z
fitness_credit: 0
---

# S08 evidence card — GitHub compare 404 ambiguity and retry boundary

## Decision

**REVISE — classify only the connector-visible failure; a compare `404` is not proof that a commit is absent or that the supplied SHA alone was invalid.**

## Changed evidence gap

X13 CURRENT v82 has completed one identical-full-SHA comparison and one adjacent-full-SHA comparison. Its next bounded uncertainty is failure normalization for one non-secret invalid or unknown full SHA. S15 already supplied the generic one-call/no-retry assay shape, but explicitly did not establish GitHub compare-specific status semantics, raw forwarding, authentication state, hidden retries, or rate-limit telemetry. This card resolves only that remaining official-contract boundary.

## Dated primary evidence

Observed 2026-08-04:

1. GitHub's current compare endpoint accepts refs or commit SHAs, requires `Contents: read` for fine-grained authenticated access, can be used unauthenticated for public resources, and documents only `200`, `404`, `500`, and `503` for this endpoint. The current request example uses API version `2026-03-10`.
   - https://docs.github.com/en/rest/commits/commits?apiVersion=2026-03-10#compare-two-commits
2. GitHub documents that `404 Not Found` can deliberately mask authentication or authorization failure for private resources. It can also result from URL/path encoding, path shape, or unsupported-method problems. Therefore `404` is intentionally non-diagnostic without transport and principal evidence.
   - https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api?apiVersion=2026-03-10#404-not-found-for-an-existing-resource
3. GitHub documents rate-limit failures as `403` or `429` and requires retry timing to follow `retry-after` or `x-ratelimit-reset`; absent those headers, the safe minimum wait is one minute with bounded exponential backoff. X13's connector surface does not expose these headers.
   - https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api?apiVersion=2026-03-10#rate-limit-errors
   - https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api?apiVersion=2026-03-10#handle-rate-limit-errors-appropriately
4. GitHub explicitly warns not to keep polling a repeatedly `404` resource until authentication and authorization have been checked, because `404` does not always mean absence.
   - https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/best-practices-for-using-the-rest-api#avoid-repeated-requests

## Supported claims

- The official compare endpoint documents `404` as `Resource not found`, plus `500` and `503` server failures; it does not document a compare-specific `422` response contract.
- One normalized connector `404` can support only: `CONNECTOR_VISIBLE_COMPARE_FAILURE_FOR_THIS_EXACT_CALL`.
- A connector-side schema rejection or `invalidArgument` can support only: `WRAPPER_OR_CLIENT_VISIBLE_INPUT_REJECTION`; it must not be relabeled as raw GitHub compare behavior.
- A `404` cannot distinguish nonexistent repository, inaccessible private repository, insufficient permission, malformed or misencoded path, unsupported method, unknown base/head ref, or unknown commit SHA without additional evidence.
- Phase 3 may execute exactly one synthetic, non-secret, full-length unknown-SHA comparison against a known public repository and known-good opposite SHA, with zero retry, fallback, hydration, or ref mutation.
- The normalized result should preserve only error class/message, exposed latency, and retry/fallback counters. It should not persist the synthetic ref value when its class and digest are sufficient.
- Automatic retry is forbidden for a normalized 4xx/invalid-input result. A future retry policy for 403/429/500/503 requires raw status and rate-limit headers or an equivalent provider receipt that this connector currently does not expose.

## Excluded claims

- `404_MEANS_COMMIT_DOES_NOT_EXIST`
- `404_MEANS_SHA_WAS_FORWARDED_UNCHANGED`
- `404_PROVES_REPOSITORY_VISIBILITY_OR_EFFECTIVE_PERMISSION`
- `INVALID_ARGUMENT_OR_422_IS_DOCUMENTED_GITHUB_COMPARE_SEMANTICS`
- `CONNECTOR_MADE_EXACTLY_ONE_UPSTREAM_HTTP_REQUEST`
- `CONNECTOR_PERFORMED_ZERO_HIDDEN_RETRIES`
- `NO_QUOTA_WAS_CONSUMED`
- `ZERO_MARGINAL_COST_IS_PROVEN`
- `RAW_HTTP_STATUS_HEADERS_REQUEST_ID_RATE_LIMIT_STATE_OR_AUTHENTICATED_PRINCIPAL_WERE_OBSERVED`
- `FAILURE_NORMALIZATION_PROVES_OPERATIONAL_READINESS_ADOPTION_CONSUMER_ACK_OR_FITNESS`

## Required phase-3 gate

1. Bind one known public repository and one known-good full SHA as the control side.
2. Use one synthetic non-secret full-length unknown SHA on the other side.
3. Call `GitHub.compare_commits` once only.
4. Do not retry, mutate the ref, change repositories, widen scope, hydrate files, or fall back to another endpoint.
5. Classify the outcome as exactly one of:
   - `WRAPPER_CLIENT_REJECTION`
   - `CONNECTOR_NORMALIZED_NOT_FOUND_AMBIGUOUS`
   - `CONNECTOR_NORMALIZED_SERVER_OR_TRANSPORT_FAILURE`
   - `UNEXPECTED_SUCCESS_ANDON`
   - `UNCLASSIFIABLE_SCHEMA_ANDON`
6. Preserve no raw credential, principal identity, private repository data, or synthetic ref body in Git or Slack.
7. Phase 4 may retain this only as catalog-level failure behavior. It cannot claim raw parity, least privilege, retry safety, completeness, adoption, or fitness.

## License and terms uncertainty

- The GitHub REST service and connector remain subject to the operator's existing GitHub authorization and applicable GitHub terms; no terms review or acceptance occurred in this run.
- The connector wrapper's implementation version, source license, effective OAuth/App scope, authenticated principal, request forwarding, hidden retry behavior, and quota accounting are not exposed.
- No software package was installed, copied, modified, or redistributed, so no code-license admission is made by this card.

## Cost and operator-minute estimate

- This research run: `$0` surfaced paid cost; `0` operator minutes.
- Apply the classification/no-retry gate to the existing phase-3 packet: `5–10` producer minutes.
- Distinct raw GitHub witness with status, headers, principal/scope receipt, and no-retry trace: `10–20` verifier minutes plus `0–5` operator minutes if existing authorization is already available.
- Actual upstream request count, quota consumption, and marginal cost remain `UNKNOWN`.

## Strongest objection

With a known public repository, a known-good control SHA, and an obviously synthetic 40-hex peer, a returned `404` is highly suggestive of an unknown ref rather than an authorization failure. That is useful operational intuition, but GitHub's published contract deliberately leaves `404` ambiguous and the connector hides raw transport and principal evidence. The observation therefore cannot honestly be promoted to `COMMIT_ABSENT`.

## Falsifier

This card falls if an authorized, nonproducer raw GitHub witness repeats the same repository and synthetic-ref class and shows an unambiguous documented status/body that binds specifically to an unknown base/head SHA, or if the connector returns success or materially disagrees with the raw endpoint on failure class for the same bound request.

## Verifier and consumption

- **Verifier:** authorized nonproducer raw GitHub compare witness capturing API version, exact public repository, request-shape digest, HTTP status, safe response-class digest, request/rate-limit headers, authenticated principal class, and retry count.
- **Immediate consumer:** `X13_GITHUB_COMPARE_COMMITS_READONLY_001_PHASE3`.
- **Downstream consumer:** `HFO_COTS_CAPABILITY_INVENTORY`.
- **Credit condition:** exact WorkItem consumption plus distinct `STOOD | FELL` and named ConsumerAck. Until then, fitness remains `0`.

## Honest flaw

This run did not execute the invalid-ref probe or a raw API witness. It establishes the official status and ambiguity ceiling, not the actual connector's next response. GitHub documentation may change before expiry, and GitHub.com's public behavior does not automatically bind GitHub Enterprise Server or an opaque connector wrapper.

## Effect receipt

No compare probe, private-data read, credential access, account or terms action, task mutation, outreach, application, purchase, send beyond the required internal coordination pointer, spend, deployment, merge, publication, or demand claim occurred.
