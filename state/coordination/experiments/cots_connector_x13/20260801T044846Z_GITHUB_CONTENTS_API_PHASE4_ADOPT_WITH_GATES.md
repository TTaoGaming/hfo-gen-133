---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_API_001
seat: X13_COTS_CONNECTOR_PDCA
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
campaign_wake: 4_of_4
phase: 4
decision: ADOPT_WITH_GATES
decision_scope: INTERNAL_SERIAL_SINGLE_FILE_GITHUB_CONTENTS_PRIMITIVE
binding_architecture_decision: false
expected_current_version: 7
next_current_version: 8
prior_current_blob_sha: 54b62f7110242615cdeb1a28dd510a24ca71cc3e
valid_time_utc: 2026-08-01T04:48:46Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
wip: 1
effect_ceiling: APPROVED_NON_SENSITIVE_PATH_SERIAL_UTF8_CREATE_READ_SHA_BOUND_UPDATE_EXACT_READBACK_FORWARD_ROLLBACK
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_BEFORE_HIGHER_EFFECT_USE
consumer: Ratatoskr_and_Olrun
consumer_ack: NOT_OBSERVED
same_provider_evidence_binding_weight: 0
review_expiry_utc: 2026-09-01T04:48:46Z
next_candidate: Slack_public_channel_connector
next_candidate_phase: 1
sealed: false
source_bindings:
  phase_1_blob_sha: 7de5d3a9a7fe8f9724d99afc80f7f65afbdb8436
  phase_2_blob_sha: f9a483d8e91dd4de7dff520f4ac56b58fb679350
  phase_3_blob_sha: c0eedd17d5bb83972646dc2239a59de42815c3ec
  prior_current_blob_sha: 54b62f7110242615cdeb1a28dd510a24ca71cc3e
  s09_vote_blob_sha: 784b53d5178f4d19dd574259aa48a845727e2d8b
official_contract_rechecked_utc: 2026-08-01T04:48:46Z
official_contract:
  contents_api: https://docs.github.com/en/rest/repos/contents
  api_versions: https://docs.github.com/en/rest/about-the-rest-api/api-versions
  rate_limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
---

# X13 phase 4 — GitHub Contents API adoption decision

## Decision

`ADOPT_WITH_GATES` for a narrow internal primitive only.

The connected GitHub Contents wrapper is admitted for serialized single-file UTF-8
create, fetch, SHA-bound replacement, exact readback, and forward rollback on explicitly
approved non-sensitive repository paths. It is not admitted as a database, workflow
runtime, multi-file transaction layer, exactly-once executor, linearizable store, secret
store, deployment mechanism, or independent verifier.

The official contract still requires the current blob `sha` when replacing a file and
warns that content create/update and delete operations must be serialized. GitHub's REST
API currently supports versions `2026-03-10` and `2022-11-28`; requests without an
explicit version header default to `2022-11-28`. The connector does not expose the
effective request header, authentication identity/scope, rate-limit headers, request ID,
ETag, retry count, audit actor, or server timing, so those fields remain `UNKNOWN`.

## Evidence weighed

- Phase 1 established an authenticated connector baseline and official contract.
- Phase 2 directly created deterministic UTF-8 content, replaced it using the fetched
  blob SHA, read back exact bytes/blob identifiers, and restored the baseline with a
  forward commit.
- Phase 3 directly rejected one stale blob-SHA replacement with HTTP 409, preserved the
  newer exact bytes, and restored the baseline with a valid forward update.
- S09 advised `ADOPT_WITH_GATES`, but that vote and the X13 evidence are same-provider
  advisory evidence with binding weight zero.
- No distinct-provider reproduction or ConsumerAck was observed. Absence from the
  connected surfaces does not prove none exists elsewhere.

## Required gates

1. **Scope:** exact repository, branch, and approved non-sensitive path must be bound.
   Workflow files, secrets, protected deployment state, account data, and cross-repository
   transactions are excluded unless separately authorized.
2. **Serialization:** one writer per path; fetch the current blob SHA immediately before
   replacement. Do not run create/update/delete operations for the same path concurrently.
3. **Conflict:** any 409, stale SHA, ambiguous error, timeout, or connector variance fails
   closed. Perform exact readback before retry or reconciliation.
4. **Readback:** bind exact UTF-8 bytes, branch, path, commit SHA, and content blob SHA.
5. **Rollback:** use a valid forward commit with the current blob SHA. No deletion,
   force-push, reset, or history rewrite.
6. **Atomicity claim ceiling:** event and pointer commits are separate and can diverge.
   No cross-file atomicity, exactly-once, linearizability, workflow durability, or
   database guarantee may be claimed.
7. **Observability:** record only exposed commit/blob/error/latency data. Mark hidden
   authentication, API version, quota, retry, request, audit, and ETag fields unknown.
8. **Verification:** same-provider structural review has binding weight zero. A distinct
   nonproducer must consume the exact packet before any higher-effect dependency.
9. **Fitness:** estimated operator minutes and custom code avoided remain unvalidated and
   earn zero fitness credit until tied to a consumed WorkItem.

## Measurements

```yaml
custom_code_avoided:
  estimate: 40_to_120_LOC_basic_adapter
  direct_components_avoided:
    - authentication_plumbing
    - REST_URL_and_JSON_construction
    - base64_transport
    - response_decoding
  not_avoided:
    - schema_and_idempotency_design
    - cross_file_reconciliation
    - retry_policy
    - independent_verification
    - consumer_ack_tracking
  fitness_credit: 0_until_consumed
operator_minutes:
  relay_measured: 0
  estimated_removed_per_bounded_sequence: 5_to_15
  estimate_validated: false
credentials:
  operator_credential_interaction_this_campaign: 0
  connector_authenticated: true
  identity_scope_expiry_SSO_and_audit_actor: UNKNOWN
durability:
  established: successful_Git_commits_and_content_addressed_blobs
  not_established:
    - database_transaction
    - exactly_once
    - multi_file_atomicity
    - durable_timer_or_workflow_recovery
observability:
  exposed:
    - commit_sha
    - content_blob_sha
    - exact_content_readback
    - stale_conflict_http_409
    - successful_write_latency_when_returned
  hidden_or_unknown:
    - auth_identity_and_scope
    - effective_API_version_header
    - rate_limit_headers
    - request_id
    - ETag
    - retry_count
    - audit_event
portability:
  contract_level: MEDIUM_HIGH_WITHIN_GITHUB_REST
  connector_wrapper_level: MEDIUM_LOW
  other_forges: UNPROVEN
failure_behavior:
  measured: ONE_SERIAL_STALE_SHA_UPDATE_REJECTED_NEWER_BYTES_PRESERVED
  unmeasured:
    - true_simultaneous_writers
    - hidden_retry_side_effects
    - permission_downgrade
    - quota_exhaustion
    - transport_partition
direct_cost_and_quota:
  incremental_paid_cost_observed_usd: 0
  exact_plan_allocation: UNKNOWN
  exact_live_quota_and_secondary_limit_state: UNKNOWN
```

## Strongest objection

This may be an opaque privileged wrapper rather than a least-privilege, portable
integration. Repeated same-provider success can hide shared authentication, retry,
versioning, quota, and error-shaping defects. Procedural gates can also be self-attested
and reward-hacked.

## Strongest falsifier

Change the decision to `HOLD`, `DEFER`, or `REJECT` if a fresh bounded probe lands stale
bytes, targets an unintended branch/path, produces inconsistent exact readback, creates
unintended commits through hidden retries, requires secret or operator credential
ferrying, cannot operate within a reducible permission boundary, or is consumed as a
database/workflow/exactly-once primitive.

## Smallest reversible verification

A distinct nonproducer with an independently authenticated GitHub surface should repeat
the State-A → State-B → stale-State-C rejection → forward-restore sequence on a new
experiment-only path and inspect the resulting branch commit graph. The verifier should
return `STOOD | FELL` bound to the phase-3 event blob, this decision event, and the prior
CURRENT blob.

## Honest flaw

The campaign used one connector family on one repository branch and did not inspect raw
HTTP traffic, token configuration, audit logs, or a truly concurrent writer. The
official documentation was rechecked, but the effective API-version header used by the
wrapper remains hidden. `ADOPT_WITH_GATES` is an experiment outcome, not a binding
architecture decision, production authorization, independent quorum, or ConsumerAck.
