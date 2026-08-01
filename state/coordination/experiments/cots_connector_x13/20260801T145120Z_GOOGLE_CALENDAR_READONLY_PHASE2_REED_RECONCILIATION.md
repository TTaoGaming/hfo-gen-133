---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_READONLY_CONNECTOR_001
candidate: Calendar_read_only_event_search_and_free_busy_connector
phase: 2
phase_name: SMALLEST_HARMLESS_READ_ONLY_MICRO_USE
result: PHASE2_MICRO_USE_ACCEPTED_WITH_PRIVACY_GATE_TIGHTENED
expected_prior_version: 17
next_version: 18
prior_current_blob_sha: 2d225f3dbb8c5b864b2ac9a956c1b3e2d109df54
prior_phase_event_commit: d9d13734a133c06258bb324118ac6e2b66a7b224
prior_phase_event_blob_sha: fc4fdb3484e9b931d561886f7dd984cdf3a63e3a
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
wip: 1
effect_ceiling: READ_ONLY_BOUNDED_PRIMARY_CALENDAR_RECONCILIATION_NO_CALENDAR_WRITE_NO_PRIVATE_BODY_PERSISTENCE
valid_time_utc: 2026-08-01T14:51:20Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
expiry_utc: 2026-08-08T14:51:20Z
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_FOR_PRIVACY_AND_REQUEST_EFFICIENCY_CLAIMS
consumer: S05_OPERATOR_RELIEF_CELL_AND_X11_CARRIER_SURFACE_LAB
same_provider_binding_weight: 0
fitness_credit: 0_PENDING_EXPLICIT_CONSUMER_ACK
---

# X13 Google Calendar read-only connector — phase 2 micro-use

## Bounded uncertainty

Can the connected Google Calendar read surface reconcile one known, already-externalized operator obligation without Calendar mutation, operator relay, or persistence of private event-body data?

## Bound input

- Existing sanitized obligation receipt:
  - path: `state/coordination/receipts/chatgpt_runtime/seat-05/20260801T131604Z_REED_HVAC_FEE_VERIFICATION_BOUND.md`
  - blob SHA: `33bc64957bdd42c366a0ba20f2454b143411f931`
- Expected sanitized event-ID SHA-256 from that receipt: `8f140505576d3ab7d666f8c4b0c76c9d32f9ec94c777f49b4600a498b43d1e78`
- Search window: `2026-08-03T06:00:00Z` through `2026-08-04T06:00:00Z`
- Calendar selector: `primary`
- Query: `Reed AC`
- Result cap: `5`

## Direct micro-use receipts

### Probe A — bounded event search

- connector/action: `Google Calendar / search_events`
- connector ID: `connector_947e0d954944416db111db556030eea6`
- result: success; exactly one candidate returned; `next_page_token=null`
- exposed latency: `364 ms`
- permission/error class: authenticated success; no connector or provider error exposed
- sanitized match: title, all-day date, transparency, and prior event-ID digest were consistent with the existing S05 receipt

Material privacy observation: the search wrapper returned the full event description and identity-bearing fields even though the micro-use needed only candidate metadata. Those private values were read in the source connector response but were not copied into Git or Slack. This tightens the gate: bounded event search is not metadata-only on this connector.

### Probe B — exact event readback

- connector/action: `Google Calendar / read_event`
- input: exact event ID returned by Probe A; raw ID not persisted
- result: success
- exposed latency: `NOT_EXPOSED`
- permission/error class: authenticated success; no connector or provider error exposed
- recomputed event-ID SHA-256 matched the prior S05 digest exactly
- sanitized readback matched the previously externalized title, date, private visibility, transparent availability, and two popup reminder offsets

No event write, account change, send, spend, login, or operator relay occurred.

## Measurements

- operator_relay_minutes: `0`
- operator_minutes_removed_estimate: `2_to_4` for locating and confirming the already-bound event; not yet independently validated
- custom_code_avoided_estimate:
  - bounded Calendar query, event normalization, pagination token handling, and exact event fetch: `60_to_160_LOC_UNVALIDATED`
  - authentication and token refresh handling: `MATERIAL_BUT_UNQUANTIFIED`
  - additive total: `NOT_CLAIMED_DUE_TO_OVERLAP`
- credentials: connector was authenticated; live identity, OAuth client, token type, scopes, refresh policy, and credential custody remain hidden
- durability: Google Calendar provider durability only; no replay, resume, transaction, exactly-once, or cross-system atomicity claim
- observability: action name, connector ID, normalized result, search latency, pagination token, and error envelope were exposed; raw HTTP status, headers, retries, request IDs, quota counters, audit identity, and read-event latency were hidden
- portability: medium for Calendar event-search/read semantics; low for wrapper-specific normalized schemas and privacy behavior; no other calendar provider tested
- direct_cost_or_quota_evidence: no paid charge surfaced; exact upstream request count, quota consumption, project class, billing account, and retry amplification remain unknown
- failure_behavior: only authenticated success was measured in this phase; permission and not-found errors remain untested
- request_efficiency: two connector actions were used; after Probe A returned full event details, Probe B was useful only for exact readback and digest binding, not for discovering additional required data

## Supported claims

- The connector can find and read back one known primary-calendar obligation inside an explicit one-day window without Calendar mutation or operator relay.
- The returned event ID bound exactly to the prior sanitized S05 digest.
- A source-system reconciliation can be externalized as sanitized facts and hashes while keeping the private body out of Git and Slack.
- The search wrapper currently over-reads for metadata-only use because it returns full descriptions and identity-bearing fields.

## Excluded claims

- Least-privilege scope, metadata-only search, secondary-calendar access, permission-denial behavior, recurrence correctness, quota safety, one-to-one upstream request count, independent verification, workflow durability, exactly-once behavior, or explicit ConsumerAck.
- This readback does not prove the underlying vendor fee is valid, due, or paid; it only proves the private Calendar obligation exists in the expected bounded window.

## Revised gates

1. Prefer free/busy for availability-only questions.
2. Treat `search_events` as a private-body read surface on this connector, not a metadata-only index.
3. Use event search only for an existing named obligation with an explicit time window, low result cap, privacy ceiling, and source-system-only body handling.
4. Do not persist event descriptions, attendees, email identities, contact details, raw event IDs, URLs, or exact private busy intervals unless an explicit WorkItem requires them.
5. Avoid a second `read_event` call when the search result already contains every field required by the bounded task; use exact readback only when digest binding or fields omitted by search are necessary.
6. Empty search remains `NOT_FOUND_OR_UNKNOWN`, never permission proof or global absence.
7. Do not describe the connector as least privilege while scope and credential custody are hidden.
8. Do not claim provider durability as workflow durability or exactly-once execution.

## Strongest falsifier

A distinct verifier reproduces the same bounded obligation query and either cannot bind the known event, observes a materially different event/version, shows that the connector can suppress private body fields through an available metadata-only action, or shows hidden retries/request amplification that defeats the low-rate safety assumption.

## Honest flaw

This was a same-provider read of one primary-calendar all-day event that had already been created and externalized by S05. It did not test recurrence, secondary calendars, timezone transitions, inaccessible calendars, not-found or permission errors, concurrent edits, pagination, provider portability, or live OAuth scope. The connector exposed more private content than the micro-use needed. Although none of that content was persisted to Git or Slack, the runtime still received it. The second read call added request cost without proving independent correctness.

## Next phase

Phase 3: run one harmless failure and connector-variance probe using a synthetic nonexistent event or inaccessible calendar selector, record the exact normalized error class, and avoid any private event read.
