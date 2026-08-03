---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GITHUB_BOUNDED_FILE_READONLY_001_PHASE4_DECISION_20260803T204855Z
experiment_id: X13_GITHUB_BOUNDED_FILE_READONLY_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: GitHub_bounded_readonly_repository_file_and_content_addressed_blob_fetch_surface
phase: 4_of_4
event_type: DECISION
decision: ADOPT_WITH_GATES
adoption_mode: CATALOG_ONLY_NONOPERATIONAL
valid_time_utc: 2026-08-03T20:48:55Z
recorded_time_utc: 2026-08-03T20:48:55Z
prior_current_version: 71
next_current_version: 72
candidate_capability_calls_this_wake: 0
retries_this_wake: 0
fallbacks_this_wake: 0
mutations_on_candidate_surface_this_wake: 0
paid_cost_usd_observed_this_wake: 0_NO_CHARGE_SURFACED
operator_minutes_removed_measured: 0
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
---

# X13 GitHub bounded read-only campaign — Phase 4 decision

## Decision

`ADOPT_WITH_GATES`

Retain this capability in the HFO COTS catalog for bounded, explicit, read-only retrieval of a known repository path/ref or a known content-addressed Git blob. It is not promoted to autonomous or binding control-plane use.

No additional GitHub candidate-capability call was made in phase 4. The decision is based only on the three sealed campaign observations already recorded under this experiment.

## Measured campaign record

| Measure | Observed |
|---|---:|
| Explicit path/ref UTF-8 reads | 1 successful |
| Content-addressed blob reads | 1 successful |
| Improbable nonexistent blob probes | 1 structured `404` |
| Completed connector responses | 3 |
| Candidate retries | 0 |
| Candidate fallbacks | 0 |
| Candidate mutations | 0 |
| File/blob bodies returned | 2 complete decoded text bodies |
| Raw HTTP headers/request IDs/rate-limit fields exposed | 0 |
| Surfaced paid cost | $0 |
| Measured operator minutes removed | 0 |
| Consumer acknowledgment | Not observed |

Estimated custom code avoided remains unvalidated: approximately 25–70 LOC for authenticated path/ref retrieval and 30–85 LOC for authenticated blob retrieval, decoding, and normalized missing-object handling. Secret classification, independent digest verification, commit pinning, permission disambiguation, quota telemetry, retry policy, and consumer workflow are not avoided.

## Adopted boundary

Admit only:

1. One explicit repository/path/branch UTF-8 read succeeded and returned a blob SHA.
2. One fetch by that blob SHA succeeded without branch, tag, or default-ref traversal.
3. One syntactically valid improbable SHA returned a caller-visible structured `404` with no body.
4. Successful reads can expose complete private or internal file contents.
5. Success and failure telemetry are asymmetric and omit high-assurance provider telemetry.

Do not admit:

- branch reads as immutable or commit-pinned snapshots;
- wrapper-returned bytes as independently hash-verified;
- every `404` as authoritative absence;
- least-privilege identity, token class, repository scope, quota capacity, or retry safety;
- binary, large-blob, symlink, submodule, directory, timeout, conflict, validation, or rate-limit behavior;
- operational readiness, consumer value, or measured time savings.

## Mandatory gates

- Require explicit repository, path, and ref for path reads; never rely on the default branch for control state.
- Prefer content-addressed blobs or commit-pinned reads for binding decisions.
- For high-assurance use, require response-SHA echo or independent Git blob hash recomputation plus a distinct authorized raw API or local-Git parity check.
- Classify and minimize returned content before durable cross-surface fan-out. Never persist secrets, tokens, private keys, or unnecessary personal content.
- Distinguish missing-object `404` from permission-masked `404`, `403`, `409`, `422`, `429`, timeout, and provider failure. Do not automatically retry without an explicit bounded policy and provider telemetry.
- Require size, encoding, binary, symlink, submodule, and large-object checks before generalizing.
- Require a named consumer acknowledgment and measured operator outcome before operational adoption or fitness credit.

## Dimensions

- **Credentials:** connector-managed and uninspected; authenticated principal, token class, effective scope, custody, and least privilege remain unknown.
- **Durability:** high for Git-first event records and stronger for content-addressed reads than mutable branch reads; response binding remains incomplete without digest/parity verification.
- **Observability:** adequate for explicit inputs, returned body, and structured `404`; weak for HTTP status on success, request ID, ETag, resolved commit, rate-limit state, hidden retries, and upstream attempt count.
- **Portability:** medium at the Git object-model level; low-to-medium across providers because auth, permission masking, media types, errors, and quotas are provider-specific.
- **Failure behavior:** one same-repository missing-object probe preserved a structured `404`; broader failure taxonomy remains untested.
- **Direct cost/quota evidence:** no charge surfaced; actual request count, token class, rate-limit resource, and consumed quota were not exposed.

## Strongest falsifier

A distinct authorized raw GitHub or local-Git read using the same repository and phase-2/phase-3 object IDs returns different bytes, returns `200` for the supposedly missing object, or demonstrates that the connector substituted an object, retried invisibly, or normalized permission, quota, timeout, or transport failure into the observed response.

## Verifier

Use a distinct authorized raw `GET /repos/{owner}/{repo}/git/blobs/{file_sha}` or local `git cat-file` check for the same known and improbable object IDs. Capture object SHA, byte length, encoding, HTTP status, request ID, rate-limit headers, and zero-retry behavior; independently recompute the Git blob object ID for returned bytes.

## Consumer

- Immediate: `HFO_COTS_CAPABILITY_INVENTORY`
- Future operational consumer: must be explicitly named in a new work item.

## Honest flaw

The campaign observed only one small UTF-8 path read, one small UTF-8 content-addressed read, and one improbable-SHA structured `404`. Response SHA, encoding, size, independent byte hashing, resolved commit, raw headers, request ID, identity, scopes, permission masking, quota, binary and large-object behavior, hidden retries, raw-API parity, consumer acknowledgment, and actual operator-time reduction remain unverified.

## Next campaign candidate

`Gmail bounded read-only metadata/search surface`, phase 1 only, provided the already-authorized native connector can perform a smallest harmless read without permission, account, terms, send, draft, label, archive, or deletion changes.
