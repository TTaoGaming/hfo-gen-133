---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
queue_source: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_version: 149
queue_experiment_id: X13_GMAIL_SEARCH_IDS_READONLY_013
queue_phase: PHASE2_IDENTICAL_BOUNDED_REPLAY_AND_ORDERED_DIGEST_COMPARISON
bounded_question: Can equality of the ordered message-ID digest from one identical bounded replay be treated as evidence of deterministic or contractually stable Gmail search ordering?
decision: REVISE
candidate: Gmail.search_email_ids
candidate_connector_schema_version: NOT_EXPOSED
upstream_candidate: Gmail_API_v1_users.messages.list
valid_time_utc: 2026-08-07T02:27:25Z
recorded_time_utc: 2026-08-07T02:27:25Z
expiry_utc: 2026-08-14T02:27:25Z
consumer: X13_GMAIL_SEARCH_IDS_READONLY_013_PHASE2_IDENTICAL_BOUNDED_REPLAY_AND_ORDERED_DIGEST_COMPARISON
verifier: S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_SAME_PRINCIPAL_RAW_GMAIL_V1_USERS_MESSAGES_LIST_WITNESS_IF_OPERATIONAL_CLAIM_IS_LATER_REQUIRED
cost_usd_observed: 0
operator_minutes_removed_measured: 0
research_operator_minutes_estimate: 8_to_15
distinct_verification_operator_minutes_estimate: 15_to_30
nominal_provider_quota_if_wrapper_maps_one_to_one: 5_GMAIL_QUOTA_UNITS_PER_MESSAGES_LIST_REQUEST
connector_actual_quota_debit: UNKNOWN
license_terms_uncertainty: GOOGLE_DEVELOPER_DOC_TEXT_CC_BY_4_0_AND_SAMPLES_APACHE_2_0_PER_PAGE_FOOTERS; CONNECTOR_EFFECTIVE_OAUTH_SCOPE_IDENTITY_BACKEND_MAPPING_RETENTION_AND_SERVICE_TERMS_NOT_BOUND_BY_THIS_CARD
---

# S08 evidence card — Gmail phase-2 ordered-digest semantics

## Finding

`REVISE`: keep the identical replay, but interpret it as a **two-sample ordered-output drift canary**, not proof of deterministic Gmail search ordering.

The currently exposed `Gmail.search_email_ids` wrapper accepts `query`, `label_ids`, `max_results`, and `next_page_token`; it exposes no caller-controlled sort/order parameter and its tool contract states no ordering guarantee.

Google's current `users.messages.list` contract likewise documents `maxResults`, `pageToken`, `q`, `labelIds[]`, and `includeSpamTrash`, and returns `messages[]`, `nextPageToken`, and `resultSizeEstimate`. The contract does not document an `orderBy` parameter or promise a stable return order. The separate `Message.internalDate` field is documented as determining inbox ordering, but that is not stated as a `messages.list` ordering contract.

Phase 1 already observed `next_page_token_present=true` at `max_results=3`. The queried mailbox/search view is mutable: new matching mail or label-state changes can legitimately alter the first page between two calls. Therefore an unequal ordered digest cannot by itself distinguish provider drift, wrapper transformation, mailbox mutation, or undocumented ordering behavior.

## Supported claim

- An identical bounded replay can detect whether the wrapper returned the same normalized first-page ordered ID sequence and page-token-presence bit in two samples.
- Equal digests mean only `NO_ORDERED_OUTPUT_DRIFT_OBSERVED_ACROSS_TWO_SAMPLES`.
- Unequal digests mean only `ORDERED_OUTPUT_DRIFT_OBSERVED_CAUSE_UNKNOWN`.
- Preserving only the digest is privacy-minimizing but intentionally reduces root-cause diagnosability.

## Excluded claims

This card does **not** support:

- deterministic Gmail search results;
- a provider-guaranteed message ordering for `users.messages.list`;
- stable ordering across mailbox mutations;
- snapshot consistency between pages or calls;
- completeness of a first page, especially while a next-page token is present;
- raw-provider parity, effective OAuth scope, or connector backend equivalence;
- operator value, adoption, or fitness credit.

## Required phase-2 interpretation

```text
EQUAL_ORDERED_DIGEST   => NO_ORDERED_OUTPUT_DRIFT_OBSERVED_ACROSS_TWO_SAMPLES
UNEQUAL_ORDERED_DIGEST => ORDERED_OUTPUT_DRIFT_OBSERVED_CAUSE_UNKNOWN

EQUAL_ORDERED_DIGEST != DETERMINISTIC_SEARCH
EQUAL_ORDERED_DIGEST != DOCUMENTED_ORDER_GUARANTEE
EQUAL_ORDERED_DIGEST != COMPLETE_RESULT_SET
EQUAL_ORDERED_DIGEST != SNAPSHOT_CONSISTENCY
```

Retain the exact phase-1 request bytes and normalization contract. Do not persist raw Gmail message IDs or the page token. Do not widen, retry, or page through results merely to explain a mismatch during this phase.

## Primary/current sources

1. Google Gmail API `users.messages.list`, last updated 2026-04-15 UTC: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
   - Documents the list request parameters and response shape; no `orderBy` parameter or stable-order guarantee is stated.
2. Google Gmail API `Message` resource, last updated 2026-05-06 UTC: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages
   - States that `internalDate` determines ordering in the inbox; this is not documented as a `users.messages.list` response-order contract.
3. Google Gmail API search/filter guide, last updated 2026-06-03 UTC: https://developers.google.com/workspace/gmail/api/guides/filtering
   - Documents Gmail API query semantics and differences from the Gmail UI.
4. Google Gmail API usage limits, current page read 2026-08-07: https://developers.google.com/workspace/gmail/api/reference/quota
   - `messages.list` costs 5 quota units; standard use is currently no-additional-cost below the daily billing threshold. Connector mapping/debit remains unverified.

## Strongest objection

Gmail's user-facing inbox is ordered by message internal date, so repeated search results are likely to be newest-first and an ordered digest is operationally useful.

That is plausible, but the API contract retrieved for `users.messages.list` does not bind its response array to a documented stable sort. A likely implementation behavior is not a safe contract claim, especially for a phase explicitly intended to characterize connector behavior.

## Falsifier

Move this boundary toward `ADMIT` as a stable-order claim only if either:

1. a current official Gmail API or connector contract explicitly specifies the ordering and stability semantics for this exact search surface; or
2. a named operational WorkItem requires the property and a distinct same-principal raw-provider experiment demonstrates the claimed semantics under a frozen fixture while still acknowledging that experimental stability is not a provider contract.

## Consumer / expiry / fitness

Consumer: `X13_GMAIL_SEARCH_IDS_READONLY_013_PHASE2_IDENTICAL_BOUNDED_REPLAY_AND_ORDERED_DIGEST_COMPARISON`.

Expiry: `2026-08-14T02:27:25Z` or earlier on connector-schema/API-contract change.

Fitness/adoption credit: `0` until exact WorkItem consumption and explicit ConsumerAck.

## Honest flaw

This card intentionally does not execute the Gmail replay and does not inspect mailbox data. It establishes only the interpretation ceiling for the next producer call. Absence of a documented ordering guarantee is not proof that the backend order is random or unstable.
