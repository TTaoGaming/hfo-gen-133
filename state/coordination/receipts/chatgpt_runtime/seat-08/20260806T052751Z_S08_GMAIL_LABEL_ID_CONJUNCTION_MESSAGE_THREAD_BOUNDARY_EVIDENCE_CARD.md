---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_GMAIL_LABEL_ID_CONJUNCTION_MESSAGE_THREAD_BOUNDARY_20260806T052751Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
wip: 1
valid_time_utc: 2026-08-06T05:27:51Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: agent_runtime_cots_capabilities
changed_question_source:
  source_event: state/coordination/experiments/cots_connector_x13/20260806T044813Z_GITHUB_CONTENTS_FETCH_PHASE4_DEFER.md
  source_event_blob_sha: 485d1ae653e0e3a857d0aebd56ae25bf9cec1060
  queue_delta: next_campaign_X13_GMAIL_SEARCH_READONLY_008_phase1_pending
bounded_uncertainty: DOES_GMAIL_LABEL_IDS_MEAN_OR_OR_THREAD_WIDE_MATCHING
candidate: Gmail.search_email_ids_and_Gmail.search_emails_label_ids_parameter
candidate_contract_version: CONNECTOR_SCHEMA_OBSERVED_2026_08_06_PLUS_GMAIL_API_USERS_MESSAGES_LIST_UPDATED_2026_04_15_AND_LABEL_GUIDE_UPDATED_2026_06_03
effect_ceiling: PUBLIC_RESEARCH_CARD_AND_ONE_SANITIZED_SLACK_POINTER_ONLY
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_CONNECTOR_SCHEMA_ONLY_NO_MAILBOX_READ
consumer: X13_GMAIL_SEARCH_READONLY_008_PHASE1_LABEL_INTERSECTION_GATE
verifier: DISTINCT_AUTHORIZED_GMAIL_API_MESSAGE_AND_THREAD_LABEL_FIXTURE_VERIFIER
expiry_utc: 2026-08-13T05:27:51Z
fitness_credit: ZERO_UNTIL_EXACT_WORKITEM_CONSUMER_ACK
sealed: false
---

# REVISE — Gmail `label_ids` is message-level AND, not OR or whole-thread state

## Bounded finding

For the exact exposed connector actions `Gmail.search_email_ids(query, label_ids, max_results, next_page_token)` and `Gmail.search_emails(...)`, the upcoming X13 phase-1 contract must not describe multiple `label_ids` as alternatives or as a conversation-wide state.

Google's current `users.messages.list` contract says a message is returned only when it matches **all** specified label IDs. Google also states that messages inside one thread can carry different labels. Its label guide is more explicit: labels exist on messages; a thread-level label view is the union of labels found on any message in that thread, and a label on one message is not automatically added to other messages in the thread.

Therefore:

```text
label_ids=[INBOX,UNREAD] => MESSAGE_HAS_INBOX_AND_UNREAD
label_ids=[A,B] => NOT_A_OR_B
MESSAGE_MATCH => NOT_WHOLE_THREAD_MATCH
THREAD_LABEL_UNION => NOT_EVERY_MESSAGE_HAS_LABEL
```

## Required revision

X13 should bind the phase-1 expected semantics as:

- `label_ids` is an all-label conjunction at the individual-message level;
- a positive result supports only that at least one returned message satisfied every supplied label ID at observation time;
- a zero result does not prove the conversation lacks those labels in aggregate or that no other message in the same thread has one of them;
- thread-level questions require an explicit thread read or thread-list contract and must not be inferred from a message-list result;
- connector-backend mapping remains `UNKNOWN` until a controlled fixture confirms parity.

## Supported claims

- Gmail API `users.messages.list.labelIds[]` requires all specified label IDs on each returned message.
- Labels are attached to messages; thread label summaries can represent labels present on any message in the thread.
- Different messages in the same thread can have different labels.
- `label_ids=[INBOX,UNREAD]` is a valid expected contract for unread messages that are also in Inbox, subject to live connector parity.

## Excluded claims

- No claim that the hosted connector directly maps one-to-one onto `users.messages.list`.
- No claim that multiple label IDs are an OR expression.
- No claim that a matching message proves every message in its thread is unread, in Inbox, or carries the same user labels.
- No claim that a zero-result call proves thread-wide absence, mailbox-wide absence, complete pagination, or stable state under concurrent mailbox changes.
- No private mailbox, message ID, thread ID, label, sender, subject, body, attachment, or count was read.

## Dated primary sources

Observed 2026-08-06:

1. Google Gmail API `users.messages.list`, last updated 2026-04-15: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
2. Google Gmail API `Manage labels`, last updated 2026-06-03: https://developers.google.com/workspace/gmail/api/guides/labels
3. Sanitized connector schema observed 2026-08-06: `search_email_ids` and `search_emails` expose `label_ids` as exact Gmail label IDs; backend method, token scope, and raw request are hidden.

## License, terms, and privacy uncertainty

Google developer documentation is generally CC BY 4.0, with code samples under Apache 2.0; this card paraphrases the contract and copies no implementation. The hosted connector's OAuth app identity, scopes, token custody, retention, subprocessors, quota accounting, and raw Gmail method remain unknown. Label IDs and query results are private mailbox data even when bodies are not returned.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
private_connector_calls_this_wake: 0
estimated_phase1_contract_revision_minutes: 5_to_10
estimated_controlled_fixture_minutes: 20_to_40
estimated_operator_minutes_avoided_per_false_thread_state_incident: 5_to_15_UNVALIDATED
quota_or_paid_cost_evidence: NOT_EXPOSED
```

## Strongest objection

The connector may internally translate `label_ids` into a different query or aggregate results by thread, so the public Gmail REST contract may not describe the live wrapper. Correct. That objection prevents direct admission of live parity; it does not justify OR or thread-wide claims. Until a controlled fixture is observed, the safe result is `REVISE` with the documented message-level conjunction as the expected contract and wrapper behavior marked unknown.

## Falsifier

Revise or retire this card if a sanitized, authorized fixture proves the exact connector version intentionally implements different semantics and documents them. The minimum fixture contains:

1. one thread with message M1 labeled `INBOX` only;
2. message M2 in the same thread labeled `UNREAD` only;
3. message M3 labeled both `INBOX` and `UNREAD`;
4. one call with `label_ids=[INBOX,UNREAD]`;
5. raw Gmail API or Gmail UI source-system readback tied to the same principal.

The card is stood only if the wrapper returns M3 and does not return M1 or M2 for the conjunction. A thread-level aggregate return, OR behavior, hidden query rewriting, or inability to bind raw parity keeps the capability `UNKNOWN/REVISE`.

## Self-probe and credit

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
task_enabled_observed: true
tools_observed:
  - automations.list_readonly
  - GitHub.search_commits
  - GitHub.search
  - GitHub.fetch_file
  - GitHub.create_file
  - web_primary_sources
  - Gmail.connector_schema_only
gmail_private_data_accessed: false
task_mutation_called: false
```

**Decision:** `REVISE`  
**Consumer:** `X13_GMAIL_SEARCH_READONLY_008_PHASE1_LABEL_INTERSECTION_GATE`  
**Verifier:** `DISTINCT_AUTHORIZED_GMAIL_API_MESSAGE_AND_THREAD_LABEL_FIXTURE_VERIFIER`  
**Expiry:** `2026-08-13T05:27:51Z`  
**Fitness:** `0` until an exact WorkItem or X13 event records this card's commit/blob as consumed and a named ConsumerAck exists.

## Honest flaw

This wake did not call Gmail, inspect a private mailbox, observe raw HTTP, or test the connector's implementation. It establishes the current official Gmail claim ceiling and a fixture that can falsify wrapper parity. It does not prove the hosted connector follows the public API contract.