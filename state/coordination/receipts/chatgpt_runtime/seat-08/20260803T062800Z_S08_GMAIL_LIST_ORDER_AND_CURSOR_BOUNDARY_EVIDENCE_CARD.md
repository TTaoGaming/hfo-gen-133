---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_GMAIL_LIST_ORDER_AND_CURSOR_BOUNDARY_20260803T062800Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
wip: 1
valid_time_utc: 2026-08-03T06:28:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: agent_runtime_cots_capabilities
changed_question_source:
  experiment_id: X13_GMAIL_BOUNDED_MESSAGE_METADATA_SEARCH_READONLY_001
  current_version: 57
  current_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
  current_blob_sha: d928d8bf10feedeed18b1450f0e8e12e85b198c5
bounded_uncertainty: CAN_GMAIL_SEARCH_EMAIL_IDS_MAX_RESULTS_1_SUPPORT_NEWEST_MESSAGE_OR_DURABLE_INCREMENTAL_CURSOR_CLAIMS
candidate: Gmail.search_email_ids bounded first-page ID search
candidate_contract_version: CONNECTOR_SCHEMA_OBSERVED_2026_08_03_PLUS_GMAIL_API_DOCS_UPDATED_2026_04_15_AND_2026_06_03
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_CONNECTOR_SCHEMA_ONLY_NO_MAILBOX_READ
effect_ceiling: RESEARCH_CARD_AND_ONE_SANITIZED_SLACK_POINTER_ONLY
consumer: X13_GMAIL_BOUNDED_MESSAGE_METADATA_SEARCH_READONLY_001_PHASE2_PRESENCE_SAMPLE_GATE
verifier: X13_COTS_CONNECTOR_LAB_PLUS_DISTINCT_RAW_GMAIL_API_OR_UI_WITNESS_FOR_ANY_ORDERING_OR_INCREMENTAL_SYNC_CLAIM
expiry_utc: 2026-08-10T06:28:00Z
fitness_credit: ZERO_UNTIL_EXACT_WORKITEM_CONSUMER_ACK
---

# S08 evidence card — Gmail first-page ID search is a presence sample, not a newest-message or durable-cursor primitive

## Decision

`REVISE` the X13 phase-2 micro-use contract.

The exposed `Gmail.search_email_ids` action accepts `query`, exact `label_ids`, `max_results`, and `next_page_token`. It exposes no ordering parameter, `internalDate`, `historyId`, or mailbox-history action. No private mailbox call was executed in this research wake.

Google's current `users.messages.list` contract defines `maxResults` only as the maximum number of messages returned and `nextPageToken` only as the token for the next page. It does not document a caller-selectable or guaranteed result order. The list response contains only message `id` and `threadId`; the `internalDate` field that determines inbox ordering is part of the full Message resource and is not present in the list result.

Google documents `users.history.list`, not a `messages.list` page token, as the partial-synchronization primitive. History results are chronological by increasing `historyId`; a stored `startHistoryId` can expire and return HTTP 404, requiring a full sync. The current connector surface does not expose `history.list`, `startHistoryId`, or a recovery contract.

Therefore, one successful `search_email_ids(max_results=1)` call can support only this claim:

> At least one wrapper-visible message matched the bounded query at the observation time.

It must not support claims that the returned ID is the newest/latest match, that repeated first-page calls detect every new message, that `next_page_token` is a durable checkpoint, or that a later call is comparable to the earlier call under concurrent mailbox changes.

## Required phase-2 contract

Admit only `BOUNDED_POSITIVE_PRESENCE_SAMPLE` with:

- a narrow, time-bounded query or exact label IDs;
- `max_results=1`;
- no ID, thread ID, query term, or page-token persistence in Git or Slack;
- no metadata/body/attachment fetch;
- wording limited to `one or more matches observed at <time>`;
- no `latest`, `newest`, `first`, `cursor`, `checkpoint`, `delta`, `complete`, or `all caught` claim.

If incremental monitoring is required, route a separate candidate for `users.history.list`-equivalent capability with explicit `historyId`, expiry/404 recovery, full-sync fallback, deduplication, and mailbox-change concurrency tests.

## Exact dated primary sources

Observed `2026-08-03`:

1. Google Gmail API `users.messages.list`, last updated `2026-04-15`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
2. Google Gmail API `Message` resource, observed `2026-08-03`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages
3. Google Gmail API `users.history.list`, observed `2026-08-03`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.history/list
4. Google Gmail API synchronization guide, last updated `2026-06-03`: https://developers.google.com/workspace/gmail/api/guides/sync
5. Current connector schema observation: `Gmail.search_email_ids(query, label_ids, max_results, next_page_token)`; no order, `internalDate`, `historyId`, or history-list action exposed.

## Supported claims

- `messages.list.maxResults` is a page-size ceiling, not an ordering or completeness control.
- `messages.list.nextPageToken` retrieves another page; the contract does not define it as a durable mailbox-change checkpoint.
- `messages.list` returns only IDs and thread IDs.
- `Message.internalDate` determines inbox ordering, but is unavailable in the ID-only list response.
- `history.list` is the documented partial-sync surface and returns changes in increasing `historyId` order.
- A `startHistoryId` can become invalid or stale and typically yields HTTP 404, requiring full synchronization.
- The current connector can produce a bounded positive-presence sample without returning headers, snippets, bodies, or attachments to the carrier.

## Excluded claims

- No claim that Gmail currently returns `messages.list` results newest-first, oldest-first, or deterministically ordered.
- No claim that the first returned ID is the newest or latest matching message.
- No claim that page tokens remain valid across mailbox changes, time, connector retries, or process restarts.
- No claim that repeated first-page queries provide lossless change detection, exactly-once delivery, deduplication, or a durable cursor.
- No claim about the live connector's backend Gmail method, effective OAuth scope, hidden caching, retries, result reordering, token retention, or data residency.
- No private message ID, thread ID, query result, mailbox count, header, snippet, body, attachment, or identity was read or externalized.

## License, terms, and privacy uncertainty

Google developer documentation is published under CC BY 4.0 except where noted, with code samples under Apache 2.0. This card paraphrases contracts and copies no sample implementation. The hosted connector's service terms, OAuth app identity, token custody, retention, subprocessors, and restricted-scope verification status remain uninspected. Message and page-token values are private mailbox data and must remain outside durable shared traces.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
private_connector_invocations_this_wake: 0
estimated_x13_phase2_contract_revision_minutes: 8_to_15
estimated_operator_minutes_avoided_per_false_latest_mail_incident: 5_to_20_UNVALIDATED
estimated_custom_sync_code_not_avoided_by_current_surface: 80_to_250_LOC_UNVALIDATED
paid_cost_quota_and_upstream_request_count: NOT_EXPOSED
```

## Strongest objection

Gmail's implementation may in practice return message-list results in a stable newest-first order, and the connector may internally preserve a stronger cursor than its schema exposes. That may be operationally true, but it is not a portable contract and cannot be used for a no-fake-green acceptance claim without direct provider evidence, controlled concurrent-mailbox tests, and a surfaced recovery boundary.

## Falsifier

Revise this card if a controlling Google contract or sanitized connector contract proves all of the following for the exact action/version:

1. a documented deterministic sort order or explicit ordering parameter;
2. a durable incremental cursor distinct from ordinary page continuation;
3. cursor validity and invalidation semantics across mailbox mutations and restarts;
4. lossless recovery and full-resync behavior;
5. direct readback showing the connector exposes those fields without private-content leakage.

A single empirical newest-first result does not falsify the contract-bound conclusion.

## Verifier, consumer, expiry, and credit

- **Verifier:** X13 may consume this as official-contract evidence. Any higher claim requires a distinct raw Gmail API or Gmail UI witness with a controlled fixture and concurrent-change test.
- **Consumer:** `X13_GMAIL_BOUNDED_MESSAGE_METADATA_SEARCH_READONLY_001_PHASE2_PRESENCE_SAMPLE_GATE`.
- **Expiry:** `2026-08-10T06:28:00Z`; revalidate official docs and connector schema after expiry.
- **Credit:** zero until an exact WorkItem or X13 event records this card's commit/blob as consumed and a named ConsumerAck appears.

## Honest flaw

This wake did not access the private mailbox, run controlled message-arrival experiments, inspect raw HTTP traffic, or observe page-token reuse. It establishes the documented claim ceiling, not the connector's hidden implementation behavior. Operator-minute and code-size estimates are unvalidated ranges.
