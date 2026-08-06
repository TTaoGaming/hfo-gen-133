---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
task_id_expected: 6a526109ba348191b5f23ad3172ad568
wip: 1
queue_experiment: X13_GCAL_SEARCH_READONLY_012
queue_version_observed: 146
queue_phase_target: 3
candidate: Google_Calendar.search_events
candidate_schema_observed_utc: 2026-08-06
upstream_candidate: Google Calendar API v3 events.list
decision: ADMIT
admit_scope: EMPTY_OR_ERROR_SHAPE_PROBE_ONLY_WITH_NEXT_PAGE_TOKEN_GATE
consumer: X13_GCAL_SEARCH_READONLY_012_PHASE3_SYNTHETIC_NONMATCH_EMPTY_OR_ERROR_SHAPE_GATE
verifier: DISTINCT_SAME_PRINCIPAL_RAW_CALENDAR_V3_EVENTS_LIST_EXACT_Q_WINDOW_MAXRESULTS_AND_PAGETOKEN_VERIFIER
paid_cost_usd_observed: 0
operator_minutes_removed_measured: 0
research_operator_minutes_estimate: 6_to_12
distinct_verification_minutes_estimate: 15_to_30
expiry_utc: 2026-08-13T23:28:00Z
valid_time_utc: 2026-08-06T23:28:00Z
---

# S08 evidence card — Google Calendar phase-3 synthetic nonmatch

## Bounded uncertainty
Can phase 3 use one high-entropy `q` search to characterize the connector's `EMPTY_SUCCESS | NONEMPTY | ERROR` response branch without converting a zero-result page into an authoritative absence claim?

## Decision
**ADMIT**, but only as an **empty/error response-shape probe** with an explicit pagination gate.

Recommended producer query token: generate immediately before the call as a single punctuation-free ASCII token matching `^zzq[0-9a-f]{32}$`. Keep the already-bounded calendar/time window, set `max_results=1`, use no retry, do not widen the window, and do not persist event bodies.

Classification contract:

```text
ZERO_RESULTS + NO_NEXT_PAGE_TOKEN = EMPTY_SUCCESS_OBSERVED
ZERO_RESULTS + NEXT_PAGE_TOKEN    = INCOMPLETE_PAGE_NOT_EMPTY_SUCCESS
NONZERO_RESULTS                   = UNEXPECTED_MATCH_OR_QUERY_TRANSFORMATION
ERROR                             = PRESERVE_EXACT_CONNECTOR_ERROR_CLASS

EMPTY_SUCCESS_OBSERVED != AUTHORITATIVE_ABSENCE
EMPTY_SUCCESS_OBSERVED != COMPLETE_CALENDAR_SEARCH
EMPTY_SUCCESS_OBSERVED != LITERAL_QUERY_SEMANTICS_PROOF
EMPTY_SUCCESS_OBSERVED != RAW_PROVIDER_PARITY
```

## Primary/current evidence
1. Google Calendar API v3 `events.list`, current reference accessed 2026-08-06: `q` is documented as free-text search over summary, description, location, attendee/organizer names and emails, multiple working-location fields, and predefined translated keywords for working-location/out-of-office/focus-time event titles. Google does not document an exact tokenizer, phrase grammar, escaping contract, or literal-match guarantee for `q` on this reference page. Source: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
2. The same `events.list` reference states that a result page may contain fewer than `maxResults`, or even no events, **even when more events match**; a non-empty `nextPageToken` identifies an incomplete page. Therefore `0 items` alone cannot be treated as terminal empty. Source: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
3. Google Calendar pagination guidance requires the exact same request plus the returned `pageToken` to continue a list traversal. Phase 3 should not page because the bounded question is wrapper branch shape, but it must preserve whether a next-page token existed. Source: https://developers.google.com/workspace/calendar/api/guides/pagination
4. Google API use involving user data is governed by the Google APIs Terms and Google API Services User Data Policy. The connector-managed effective principal, OAuth scopes, backend request mapping, retention, and quota debit remain unexposed. Sources: https://developers.google.com/terms and https://developers.google.com/terms/api-services-user-data-policy

## Supported claims
- A one-call synthetic query can characterize the exposed wrapper's observed empty/nonempty/error branch for that bounded request.
- A `next_page_token` must be retained as a semantic gate when the returned item count is zero.
- A single high-entropy alphanumeric token minimizes collision with documented natural-language/predefined keyword matches, but does not prove literal query behavior.

## Excluded claims
- Workspace- or calendar-wide absence.
- Completeness or freshness of Calendar indexing.
- Exact tokenization, quoting, escaping, stemming, substring, or case-folding semantics.
- Effective OAuth scope/principal, private-event visibility, provider request identity, quota debit, or raw-provider parity.
- Any buyer, demand, operational-time-savings, or adoption claim.

## License / terms uncertainty
The Calendar reference states that Google Developers page content is CC BY 4.0 and code samples are Apache 2.0 except as otherwise noted. API/user-data handling remains subject to Google API terms/policies. Connector-specific authorization, data minimization, storage, and backend mapping are unknown; this card does not authorize event-content persistence or any broader Calendar access.

## Strongest objection
A 32-hex high-entropy token is overwhelmingly likely not to occur naturally, so a zero-result response is practically a nonmatch. That is useful operationally, but still not a documented proof of corpus absence: the corpus is uncontrolled, `q` tokenization is underspecified, the wrapper translation is hidden, and an empty first page can coexist with a next-page token.

## Falsifier
**REVISE** if any of the following occurs: the synthetic token returns a match; the wrapper exposes or performs visible query broadening/rewriting; zero items arrive with a next-page token and are still classified terminal-empty; or a distinct same-principal raw Calendar v3 `events.list` witness produces a materially different empty/nonempty/error classification under the same `q`, calendar, time window, and `maxResults`.

## Fitness boundary
Research volume and candidate count earn zero credit. Fitness remains `0` until the exact card is consumed by the named X13 phase-3 WorkItem and receives ConsumerAck.

No Calendar search, event read, private-data access, task mutation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, or publication was performed by S08 for this card.
