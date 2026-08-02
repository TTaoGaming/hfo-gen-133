---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GOOGLE_CONTACTS_READONLY_CONNECTOR_001_PHASE4_DECISION_20260802T004800Z
experiment_id: X13_GOOGLE_CONTACTS_READONLY_CONNECTOR_001
candidate: Google_Contacts_read_only_lookup_and_recipient_resolution_connector
phase: 4_of_4
decision: ADOPT_WITH_GATES
campaign_status: COMPLETE
expected_current_version: 27
next_current_version: 28
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
binding_architecture_decision: false
same_provider_binding_weight: 0
independent_verification_closed: false
consumer_ack: NOT_OBSERVED
fitness_credit: 0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
valid_time_utc: 2026-08-02T00:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
review_expiry_utc: 2026-08-09T00:48:00Z
sealed: true
---

# X13 Google Contacts read-only connector — phase 4 decision

## Decision

`ADOPT_WITH_GATES` for **bounded recipient-candidate discovery only**.

The connector is useful for reducing manual contact lookup when a named operator obligation already exists, but the campaign did not establish safe automatic recipient resolution. A successful lookup returned multiple private candidates from an `otherContacts/*` resource class, while the malformed-input error path exposed `people:searchContacts`; the wrapper's success-path endpoint, source selection, cache freshness, field mask, OAuth scope, ranking, retry count, and upstream fan-out remain unresolved.

`ADOPT` is rejected because ambiguity, private-identity exposure, cache variance, and raw error URL leakage are material. `DEFER` and `REJECT` are too strong because one bounded lookup did return useful candidates without a world effect. `UNKNOWN` is unnecessary at this narrow candidate-discovery ceiling, although provider/source attribution remains unknown.

## Direct campaign receipts

- Phase 1: one synthetic high-entropy lookup, `max_results=3`, returned `SUCCESS_EMPTY` in 972 ms with no identity-bearing result.
- Phase 2: one source-bound lookup for an existing property-safety obligation returned three candidates in 2,410 ms. All three used the `otherContacts` resource prefix. No candidate was selected, no full contact body was read, and no message, invitation, or write occurred.
- Phase 3: one synthetic negative page-size probe failed closed with HTTP 400 `INVALID_ARGUMENT`, returned no identity data, and did not visibly retry. The raw error echoed the provider request URL, query parameters, and an injected `readMask` of `names,emailAddresses,photos`; only sanitized facts and digests were persisted.
- Phase 4: no new Contacts call. This event reduces the prior evidence into the bounded adoption decision.

Prior immutable evidence:

- Phase 1 basis is preserved in CURRENT version 27.
- Phase 2 event commit/blob: `f59fd296b5ef8a1f37fed1072877645de6273f78` / `3c5aee0c2f67b9fcdb39da17636035c538a3897a`.
- Phase 3 event commit/blob: `2d6a8d50dc440a5b29198d54d5940f2030e0b305` / `ff965515cf05dfc127a5105a8f8328701ea9d7c9`.

## Official contract baseline checked 2026-08-02

Google's official People API contract states:

- `people.searchContacts` searches grouped contacts from the `CONTACT` source, uses prefix-phrase matching, requires a response `readMask`, caps `pageSize` at 30, requires either `contacts` or `contacts.readonly`, and recommends an empty-query warmup followed by a delay because search uses a lazy cache.
- `otherContacts.search` is a separate endpoint for the `OTHER_CONTACT` source with a separate `contacts.other.readonly` scope and a narrower field set.
- A `Person` can merge data from multiple sources; `OTHER_CONTACT` is a distinct source type.
- Google's guide describes Other Contacts as typically auto-created from interactions, so they are not equivalent to a curated saved address book.

Primary references:

- https://developers.google.com/people/api/rest/v1/people/searchContacts
- https://developers.google.com/people/v1/contacts
- https://developers.google.com/people/api/rest/v1/otherContacts/search
- https://developers.google.com/people/api/rest/v1/people
- https://developers.google.com/people/api/rest/v1/otherContacts/list

## Admitted scope

1. Start from one named operator obligation and one source-bound identity hint.
2. Run one bounded candidate search with a low result cap; current campaign evidence used `max_results=3`.
3. Treat all matched fields and pointers as private identity data.
4. Return candidates for confirmation only; do not auto-select.
5. Read a full contact only when a named consumer requires one specific missing field and the read remains inside the private source system.
6. Require source-bound identity confirmation or explicit operator approval before any email, invitation, scheduling, or other external action.

## Mandatory gates

- Never auto-select from fuzzy prefixes, spelling variants, contextual domains, unknown display names, duplicate candidates, merged-source records, or `otherContacts` results.
- Do not treat `otherContacts` as a curated saved contact assertion.
- Treat an empty result only as `NO_MATCH_RETURNED_BY_ONE_WRAPPER_CALL`; it is not absence, completeness, cache freshness, or directory proof.
- Do not claim least privilege while the live identity, OAuth scope, token type, credential custody, success-path endpoint, source selection, field-mask control, warmup behavior, and retry/fan-out behavior remain hidden.
- Persist only sanitized counts, field classes, source prefixes, and digests unless the named consumer explicitly requires an address inside the private source system.
- Treat connector errors as possible private-query leaks. Remove provider URLs, queries, filters, identifiers, and field values before Git or Slack persistence.
- Do not use real identities in malformed-input probes.
- Do not blind-retry HTTP 400 `INVALID_ARGUMENT`; correct the request first.
- Do not infer the successful call's endpoint, source, scope, or ranking from an error-path endpoint or a returned resource prefix alone.
- No send, invite, contact write, account/security change, consent flow, or permission repair without separate authority.
- Fitness remains zero until a named downstream WorkItem records source-bound ConsumerAck and measured operator outcome.

## Measurements

| Dimension | Result |
|---|---|
| Operator relay | 0 minutes |
| Operator minutes removed, measured | 0; recipient selection remained unresolved |
| Operator minutes removed, estimate | 1–3 minutes per confirmed bounded lookup; unvalidated |
| Connector invocations | 3 across phases 1–3; none in phase 4 |
| Paid cost observed | $0; no charge surfaced |
| Quota evidence | Live request units, headers, project quota class, billing counters, retries, and upstream fan-out were not exposed. The inspected public search contracts do not establish the connected project's numeric quota ceiling. |
| Credentials | Connector reached the provider; operator supplied 0 credentials. Identity, OAuth scope, token type, and custody remain unknown. |
| Custom code avoided | Authenticated query/result normalization 30–80 LOC; candidate display 20–60 LOC; error normalization 20–60 LOC; all unvalidated and non-additive. Token refresh/client plumbing is materially avoided but unquantified. |
| Custom policy not avoided | Ambiguity handling, private-data minimization, source binding, operator approval, cache/source assertions, ConsumerAck, and error sanitization still require HFO gates. |
| Durability | Google provider storage only; no workflow replay, resume, transaction, idempotency, or exactly-once guarantee. |
| Observability | Medium for wrapper action, result count, returned field classes, source prefix, normalized status, and error-path endpoint/read mask. Low for success route, scope, identity, cache age, ranking, quota, retries, and fan-out. |
| Portability | Medium for provider-neutral candidate lookup and invalid-argument intent; low-to-medium for Google prefix semantics, Other Contacts, resource names, field masks, lazy cache, and wrapper normalization. |
| Failure behavior | One malformed request failed closed with 400 and no identity result, but leaked its full request URL. Permission errors, 429, 5xx, stale cache, duplicates, and partial source coverage remain untested. |

## Strongest falsifier

A success-path trace for the exact connector version that proves its endpoint, source-selection policy, read mask, warmup behavior, authenticated identity and OAuth scope, retry count, upstream request count, ranking, and resource mapping—or proves that raw provider URLs are sanitized before runtime exposure—would materially revise these gates. A source-bound ConsumerAck showing a confirmed candidate removed operator time without wrong-recipient risk would raise fitness credit above zero.

## Verifier and consumers

- Structural verifier: `S04_STRUCTURAL_PREFLIGHT`, same-provider and nonbinding.
- Required independent verifier: a distinct non-ChatGPT connector owner or direct success-path trace reviewer.
- Consumers: `S05_OPERATOR_RELIEF_CELL`, `X11_CARRIER_SURFACE_PDCA_LAB`, and the next X13 campaign.

## Honest flaw

Phase 2 used a real private name and exposed three private email candidates to the runtime. Phase 3 exercised only an invalid error route, so it cannot prove the successful route's endpoint, source, scope, cache state, least privilege, ranking, or sanitization. The campaign has still removed zero measured operator minutes.

## Next campaign

Candidate: `GitHub_contents_API_branch_scoped_file_create_update_fetch_and_readback_connector`.

Start phase 1 with official GitHub Contents API contracts and a baseline derived from one harmless branch-scoped Git-first event/readback. Do not claim database atomicity, workflow durability, merge safety, or independent verification from Git storage alone.
