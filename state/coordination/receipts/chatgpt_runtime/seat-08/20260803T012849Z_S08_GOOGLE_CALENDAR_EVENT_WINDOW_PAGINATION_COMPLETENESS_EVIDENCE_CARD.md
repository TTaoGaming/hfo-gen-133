---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T01:28:49Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: agent_runtime_cots_capabilities
question_changed_from: apollo_mcp_rust_fit_gate_then_explicit_lane_rotation_advanced
queue_trigger:
  source: state/coordination/experiments/cots_connector_x13/CURRENT.md
  experiment_id: X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001
  phase: 1_of_4
candidate: Google_Calendar.search_events
candidate_surface_observed_utc: 2026-08-03T01:28:49Z
candidate_schema_version: NOT_EXPOSED
candidate_parameters_relevant:
  - time_min
  - time_max
  - timezone_str
  - max_results
  - calendar_id
  - next_page_token
decision: REVISE
headline: REVISE_ONE_SHOT_EVENT_WINDOW_INTO_EXHAUST_NEXT_PAGE_TOKEN_PROTOCOL
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
sealed: false
expiry_utc: 2026-08-10T01:28:49Z
immediate_expiry_on:
  - Google Calendar Events.list pagination contract changes
  - connected Google_Calendar.search_events schema changes
  - connector is proven to auto-paginate before returning
  - X13 campaign or exact consumer changes
---

# S08 evidence card — Google Calendar bounded-window pagination completeness

## Self-probe and changed question

- Native task inventory returned active task `6a526109ba348191b5f23ad3172ad568`; expected and observed IDs match.
- Exposed tools used: native task readback, authenticated GitHub read/write/readback, connected-tool schema inspection, current primary-source web research, and Slack pointer after Git readback.
- The prior S08 wake completed `grants_jobs_income_opportunities`; explicit lane rotation advances to `agent_runtime_cots_capabilities`.
- Changed queue state: X13 version 52 completed the GitHub Actions campaign and named `X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001` phase 1 as its next wake.

## Bounded uncertainty

Can one `Google_Calendar.search_events` response with explicit `time_min`, `time_max`, and `max_results` be treated as a complete bounded event window, or must completeness require pagination until `next_page_token` is absent?

## Exact candidate and dated primary sources

1. Connected action schema observed `2026-08-03`: `Google_Calendar.search_events`; schema version is not exposed. It accepts `next_page_token` and instructs callers to continue paging inside the same bounded window.
2. Google Calendar API v3, `Events: list`, last updated `2026-05-12 UTC`: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
3. Google Calendar guide, `Page through lists of resources`, last updated `2026-07-16 UTC`: https://developers.google.com/workspace/calendar/api/guides/pagination
4. Queue source: `TTaoGaming/hfo-gen-133@agent/gen133-bootstrap-20260730:state/coordination/experiments/cots_connector_x13/CURRENT.md`, observed version `52`, next experiment `X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001`.

## Supported claims

- `maxResults` is a maximum page size, not a completeness guarantee.
- Google documents that an Events page can contain fewer results than requested, or even none, while more matching events still exist.
- A non-empty `nextPageToken` is the documented signal that another page exists.
- Complete retrieval requires repeating the same bounded request with the returned page token until no next token remains.
- The connected `Google_Calendar.search_events` action exposes `next_page_token`; therefore the required continuation can be performed without inventing a custom Calendar API client.
- A first-page-only result is admissible as a timestamped bounded sample, not as a complete schedule, conflict census, or proof of no additional events.

## Excluded claims

- No calendar, event, title, attendee, description, identifier, or other private Calendar data was queried or externalized by S08.
- No claim that the connector automatically exhausts pages; its schema exposing `next_page_token` points the other way but is not implementation proof.
- No claim that connector pagination preserves all upstream request parameters internally; this needs a direct phase receipt.
- No claim about recurring-event expansion, cancelled-instance handling, event-type filtering, search-query semantics, all-calendar coverage, or cross-calendar completeness. Those are separate uncertainties.
- No claim that an empty page means no matching events unless the page chain is complete and input/auth/error classes are separately closed.
- No claim that the connector is a durable synchronization feed. A bounded list is a mutable point-in-time read, not a replayable event log.
- No claim about authenticated identity, OAuth scope, least privilege, billing, quota, rate limits, or write authority.

## License, terms, and privacy uncertainty

- Google developer documentation is published under CC BY 4.0, with code samples under Apache 2.0; this card paraphrases contract facts and copies no sample implementation.
- Google API Terms, OAuth user-data policy, connected-account consent, retention rules, and the connector provider's credential custody were not re-audited or accepted.
- Any future direct Calendar probe must keep private event bodies in the source system and externalize only sanitized counts, token presence, latency, and contract-relevant fields.

## Decision

`REVISE` the X13 phase-1 baseline from a one-shot bounded search into:

`X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001_PHASE1_PAGINATION_GATE`

Minimum protocol:

1. Bind one calendar ID, exact RFC3339 window, timezone interpretation, query value, and `max_results`.
2. Record page number, sanitized item count, and whether `next_page_token` is present.
3. When a token is present, repeat the identical request with only `next_page_token` added.
4. Stop only when the token is absent, an explicit error occurs, or the bounded cost/privacy ceiling is reached.
5. Label an interrupted chain `PARTIAL_WINDOW`, never `NO_MORE_EVENTS` or `COMPLETE`.

## Cost and operator-minute estimate

- This research card: `$0` direct spend; approximately `8-12` carrier minutes; `0` operator minutes.
- X13 phase-1 pagination baseline: typically `1-3` read-only connector calls and `3-8` carrier minutes; direct cost and quota units remain `UNKNOWN` until surfaced by the connector.
- Operator burden can remain `0` if an already-authorized calendar and privacy-safe observation window are used. Any new consent, account, or scope change is outside this card and requires operator action.
- Custom code avoided: an estimated `20-60` lines for raw API pagination/auth plumbing, unvalidated. Policy logic for completeness, privacy, recurrence, and error classes is not avoided.

## Strongest objection

Most personal bounded windows contain far fewer than the connector default of 50 events, so requiring a page loop will usually add no second call and may look like needless ceremony.

**Response:** checking token presence is nearly free, while omitting it permits a false-complete schedule. Google explicitly warns that a page can be short or empty even when more matching events exist. The gate adds one branch, not a new architecture.

## Falsifier

Revise this card toward `ADMIT_ONE_SHOT_COMPLETE_WINDOW` only if an exact current connector contract or direct implementation receipt proves that `Google_Calendar.search_events` exhausts all upstream pages before returning and emits no continuation token until the full bounded result set is complete.

Retire the candidate for complete-window use if the connector drops continuation tokens, changes parameters between pages, duplicates or omits source-bound events against an independently counted control, or cannot distinguish permission/error states from an ordinary empty result.

## Verifier

- Structural: `S04_STRUCTURAL_PREFLIGHT_VERIFIER` may verify task binding, queue version, exact source URLs/dates, candidate schema fields, decision, expiry, and Git blob binding with same-provider binding weight `0`.
- Capability: X13 should produce a direct, privacy-safe multi-page receipt by forcing a small `max_results` within one already-authorized bounded window and proving parameter stability across page 1 and page 2.
- Independent consequence check: a distinct verifier should compare the sanitized total against the Google Calendar UI or raw Events.list response for the identical calendar and window. S08 cannot close that gate.

## Consumer

- Immediate consumer: `X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001`, phase `1_of_4`.
- Suggested exact WorkItem: `X13_GOOGLE_CALENDAR_BOUNDED_EVENT_WINDOW_READONLY_001_PHASE1_PAGINATION_GATE`.
- Downstream consumers: `S03_REDUCER_VERIFICATION_ROUTER` and any operator-relief WorkItem that claims a complete Calendar window.
- Success condition: `COMPLETE_PAGE_CHAIN | PARTIAL_WINDOW | CONNECTOR_ERROR | RETIRE`, bound to exact parameters and sanitized direct receipts.
- Fitness remains `0` until an exact WorkItem records ConsumerAck against this card's commit/path/blob.

## Honest flaw

This card establishes the official pagination boundary and the connected action's exposed continuation field. It does not inspect connector implementation, live Calendar payloads, recurrence behavior, authorization scope, or parameter fidelity across pages. The direct multi-page control is still missing.
