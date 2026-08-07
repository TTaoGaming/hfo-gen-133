---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
queue_source: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_version: 151
queue_experiment_id: X13_GMAIL_SEARCH_IDS_READONLY_013
queue_phase: PHASE4_DECISION_FROM_EXISTING_THREE_CALL_EVIDENCE_ONLY
bounded_question: Can Gmail.search_email_ids be described as metadata-only or least-privilege merely because the successful list response returns only message IDs/thread IDs and does not hydrate message bodies?
decision: REVISE
candidate: Gmail.search_email_ids
candidate_connector_schema_version: NOT_EXPOSED
upstream_candidate: Gmail_API_v1_users.messages.list
valid_time_utc: 2026-08-07T04:26:38Z
recorded_time_utc: 2026-08-07T04:26:38Z
expiry_utc: 2026-08-14T04:26:38Z
consumer: X13_GMAIL_SEARCH_IDS_READONLY_013_PHASE4_PRIVACY_AND_SCOPE_DECISION_GATE
verifier: S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_EFFECTIVE_SCOPE_AND_CONNECTOR_TO_PROVIDER_MAPPING_WITNESS_IF_OPERATIONAL_ADOPTION_IS_LATER_REQUESTED
cost_usd_observed: 0
operator_minutes_removed_measured: 0
research_operator_minutes_estimate: 8_to_15
distinct_verification_operator_minutes_estimate: 15_to_30
nominal_provider_quota_if_wrapper_maps_one_to_one: 5_GMAIL_QUOTA_UNITS_PER_MESSAGES_LIST_REQUEST
connector_actual_quota_debit: UNKNOWN
license_terms_uncertainty: GOOGLE_DEVELOPER_DOC_TEXT_CC_BY_4_0_AND_SAMPLES_APACHE_2_0_PER_PAGE_FOOTERS; GMAIL_READONLY_AND_GMAIL_METADATA_ARE_RESTRICTED_SCOPES; CONNECTOR_EFFECTIVE_OAUTH_SCOPE_IDENTITY_BACKEND_MAPPING_RETENTION_CONSENT_AND_SERVICE_TERMS_NOT_BOUND_BY_THIS_CARD
---

# S08 evidence card — Gmail phase-4 ID-only privacy/scope boundary

## Finding

`REVISE`: retain the phase-4 **catalog-only** option, but do not describe `Gmail.search_email_ids` as `metadata-only`, `least-privilege`, or `body-inaccessible` merely because its observed response contained IDs and no hydrated message bodies.

Google's current `users.messages.list` contract says each returned message resource contains only `id` and `threadId`, and that additional details require `messages.get`. That supports a narrow **response-minimization** claim. However, the same method accepts `q` using Gmail search-box syntax, and Google explicitly states that `q` cannot be used when the API is accessed with the `gmail.metadata` scope. The documented scopes that can support `q` therefore include broader Gmail access such as `gmail.readonly`, `gmail.modify`, or full-mail access. The connector's effective scope is not exposed in the X13 receipt.

Google's Gmail search documentation also says Gmail search can match message properties and words/phrases in messages. Therefore an ID-only result payload does not prove that the search operation itself is metadata-only in what provider-side mailbox data it may evaluate.

The privacy-safe claim ceiling is consequently:

```text
OBSERVED_ID_ONLY_RESPONSE = RESPONSE_CONTENT_NOT_HYDRATED
OBSERVED_ID_ONLY_RESPONSE != METADATA_ONLY_AUTHORIZATION
OBSERVED_ID_ONLY_RESPONSE != BODY_INACCESSIBLE_TO_SEARCH
OBSERVED_ID_ONLY_RESPONSE != LEAST_PRIVILEGE_SCOPE_PROVEN
```

## Supported claims

- The current raw Gmail `users.messages.list` response contract returns only `id` and `threadId` for each listed message; full details require a separate `messages.get` call.
- X13's three-call evidence is consistent with a wrapper that did not hydrate message content into the returned result.
- A bounded ID-only search can be retained as a **catalog/discovery** capability with explicit response-minimization and no-persistence gates.
- `messages.list` costs 5 Gmail quota units per raw API request under Google's current quota table if the connector maps one-to-one; actual connector debit remains unknown.

## Excluded claims

This card does **not** support:

- that the connector is authorized only for Gmail metadata;
- that the connector cannot access or search message bodies;
- that the effective OAuth scope is `gmail.metadata`;
- that `gmail.readonly` or another restricted scope is absent;
- that ID-only output makes the end-to-end operation non-sensitive or least-privilege;
- completeness, snapshot semantics, raw-provider parity, provider ordering, authoritative mailbox absence, or operational value;
- any statement about the user's mailbox contents.

## Phase-4 gate revision

If X13 records `ADOPT_WITH_GATES_CATALOG_ONLY`, add all of the following boundaries:

1. Name the property `ID_ONLY_RESPONSE_MINIMIZATION`, not `METADATA_ONLY_SEARCH`.
2. Preserve small bounded queries and no raw ID/page-token persistence unless a named WorkItem requires otherwise.
3. Do not infer effective OAuth scope from successful wrapper calls.
4. Do not claim least privilege until the connector exposes or a distinct authorized witness binds the effective scope and backend mapping.
5. Treat any future body/content read as a separate capability requiring its own WorkItem and privacy gate.

## Primary/current sources

1. Google Gmail API `users.messages.list`, last updated 2026-04-15 UTC: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
   - Documents that list results contain only `id` and `threadId`; documents `q`; states `q` cannot be used with `gmail.metadata`; lists accepted OAuth scopes.
2. Google Gmail API search/filter guide, last updated 2026-07-22 UTC: https://developers.google.com/workspace/gmail/api/guides/filtering
   - Documents that `q` supports most Gmail advanced-search syntax and records API/UI search differences.
3. Gmail Help search documentation, current read 2026-08-07: https://support.google.com/mail/answer/6593
   - Documents search over message-associated information and advanced fields including subject and words/phrases in messages.
4. Google Gmail API scope guide, last updated 2026-07-22 UTC: https://developers.google.com/workspace/gmail/api/auth/scopes
   - Classifies both `gmail.readonly` and `gmail.metadata` as restricted scopes and recommends choosing the narrowest scope possible.
5. Google Workspace API user data and developer policy, last updated 2026-07-13 UTC: https://developers.google.com/workspace/workspace-api-user-data-developer-policy
   - Treats Gmail scopes permitting access to message bodies, metadata, or headers as restricted scopes and imposes user-data handling requirements.
6. Google Gmail API usage limits, current read 2026-08-07: https://developers.google.com/workspace/gmail/api/reference/quota
   - `messages.list` costs 5 quota units; standard use is currently available at no additional cost below the documented daily billing threshold. Connector mapping/debit remains unverified.

## License / terms uncertainty

Google's developer-documentation page footers license documentation text under CC BY 4.0 and code samples under Apache 2.0. Gmail user-data access is separately governed by Google's OAuth, Workspace API user-data, and restricted-scope requirements. This card does not establish which OAuth scope the connected ChatGPT Gmail surface actually holds, what consent path granted it, whether the wrapper uses raw `users.messages.list`, how queries are transformed, or what retention/service terms apply inside the connector.

## Strongest objection

The phase-1 through phase-3 X13 queries were date/spam/trash bounded and the returned data exposed no message bodies, so calling the capability metadata-only may be operationally harmless.

Response: the returned payload was indeed minimized, but authorization and search-evaluation scope are different properties. Google's own contract makes `q` unavailable under `gmail.metadata`; therefore a successful query surface cannot be promoted to a metadata-only authorization claim without an effective-scope witness. The cheapest correction is nomenclature and gating, not another mailbox call.

## Falsifier

Move this boundary toward `ADMIT` as a metadata-only/least-privilege claim only if a current connector contract or distinct authorized same-principal witness establishes all of the following for this exact surface:

1. the effective OAuth scope is no broader than the claimed metadata-only scope;
2. the query feature used is valid under that scope;
3. the connector-to-provider mapping does not silently invoke a broader content-access surface; and
4. the observed response/body-access behavior matches the claimed ceiling.

If the connector exposes a narrower search primitive that is valid under `gmail.metadata` and binds those properties, reassess this card.

## Verifier / consumer / expiry / fitness

Verifier: `S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_EFFECTIVE_SCOPE_AND_CONNECTOR_TO_PROVIDER_MAPPING_WITNESS_IF_OPERATIONAL_ADOPTION_IS_LATER_REQUESTED`.

Consumer: `X13_GMAIL_SEARCH_IDS_READONLY_013_PHASE4_PRIVACY_AND_SCOPE_DECISION_GATE`.

Expiry: `2026-08-14T04:26:38Z` or earlier on Gmail API/connector schema, OAuth-scope contract, or user-data-policy change.

Fitness/adoption credit: `0` until an exact WorkItem consumes this card and explicit ConsumerAck is observed.

## Honest flaw

This card intentionally performs no Gmail mailbox query and inspects no private data. It reasons from the public provider contract plus X13's already-sanitized receipts. Because the connector's effective OAuth scope and backend mapping are hidden, the card cannot prove which broader scope is actually in use; it only rejects the stronger metadata-only/least-privilege inference.
