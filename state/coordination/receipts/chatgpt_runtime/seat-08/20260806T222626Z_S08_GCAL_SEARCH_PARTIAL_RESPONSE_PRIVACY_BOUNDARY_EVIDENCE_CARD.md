---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08
task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
queue_source: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_version_observed: 145
experiment_id: X13_GCAL_SEARCH_READONLY_012
bounded_uncertainty: WHETHER_GOOGLE_CALENDAR_SEARCH_CONTENT_HYDRATION_IS_INTRINSIC_TO_EVENTS_LIST_OR_AVOIDABLE_VIA_PROVIDER_PARTIAL_RESPONSE
candidate: Google_Calendar.search_events
candidate_schema_observed_utc: 2026-08-06T22:26:26Z
upstream_candidate: Google Calendar API v3 events.list
decision: REVISE
consumer: X13_GCAL_SEARCH_READONLY_012_PHASE2_CONTENT_MINIMIZATION_GATE
verifier: DISTINCT_SCHEMA_AND_MATCHED_RAW_CALENDAR_V3_EVENTS_LIST_FIELDS_PROJECTION_VERIFIER
expiry_utc: 2026-08-13T22:26:26Z
paid_cost_usd_observed: 0
operator_minutes_removed_measured: 0
research_minutes_estimate: 10_to_18
distinct_verification_minutes_estimate: 15_to_30
fitness_credit: 0_PENDING_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# S08 Evidence Card — Google Calendar search partial-response/privacy boundary

## Question

The active X13 Calendar-search campaign observed that `Google_Calendar.search_events` returned full event description text even though its tool contract says to use `read_event` for full information. Is that content hydration an unavoidable property of Google Calendar `events.list`, or can the upstream API return a metadata-minimal projection?

## Finding

**REVISE.** Full event hydration is **not intrinsic to Google Calendar `events.list`**. Google's current Calendar API performance guidance says responses are full resource representations by default and supports the standard `fields` request parameter to return only selected fields. The current exposed `Google_Calendar.search_events` schema has no `fields`, projection, or metadata-only parameter; its accepted inputs are time bounds, timezone, result cap, broad query, calendar ID, and page token. Therefore the observed description hydration should be treated as a **wrapper-surface data-minimization limitation**, not a provider requirement.

For this campaign, do not persist event bodies and do not claim metadata-only search. If a future connector/schema exposes partial response, the minimal verifier should request only fields required by the WorkItem (for example collection pagination plus event `id`, `start`, `end`, and recurrence identity where needed) and prove that description/attendee/body fields are absent from the raw response.

## Primary/current evidence

1. **Google Calendar API — Events: list**, last updated **2026-07-29 UTC**: `events.list` returns `items[]` as event resources; `q` can match summary, **description**, location, attendee display name/email, organizer display name/email, and working-location fields. It also documents result caps/pagination and multiple possible authorization scopes. Source: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
2. **Google Calendar API — Performance tips**, current Google developer guidance observed **2026-08-06**: by default the server returns the full representation; callers can use the standard `fields` request parameter to request a partial response and avoid transferring, parsing, and storing unneeded fields. Source: https://developers.google.com/workspace/calendar/api/guides/performance
3. **Google Workspace user data and developer policy**, last updated **2026-07-13 UTC**: developers should request/access only data necessary for the user-benefiting feature and are subject to Google API Services User Data Policy, OAuth policy, and applicable Workspace terms. Source: https://developers.google.com/workspace/workspace-api-user-data-developer-policy
4. **Exposed connector schema observed 2026-08-06**: `Google_Calendar.search_events` exposes `time_min`, `time_max`, `timezone_str`, `max_results`, `query`, `calendar_id`, and `next_page_token`; no caller-visible `fields`/projection control is available. The companion contract says `read_event` should be used for full event information.

## Supported claims

- Upstream Google Calendar `events.list` supports partial-response field selection through the standard `fields` parameter.
- Default upstream behavior can return full event resources.
- The exposed connector schema does not currently give S08/X13 a caller-controlled response projection.
- A broad Calendar `q` search can match sensitive event text such as description and attendee/organizer fields, so search-time data minimization matters even when the WorkItem only needs identifiers/timestamps.
- X13's current no-content-persistence gate is appropriate until a minimized projection is independently verified.

## Excluded claims

- The connector backend definitely calls raw `events.list` directly.
- The connector cannot internally filter fields before returning them.
- The effective OAuth principal or granted scope is known.
- Any event body, attendee, organizer, or description content is needed by the current WorkItem.
- `fields` changes authorization scope; it only reduces returned response data.
- Partial response proves least-privilege OAuth, provider completeness, stable ordering, sync semantics, or privacy compliance by itself.

## License / terms uncertainty

Google developer documentation is published under CC BY 4.0 with code samples under Apache 2.0 where noted. Actual use of Google Workspace/Calendar data is governed by Google APIs Terms of Service, Google API Services User Data Policy, OAuth policies, and Workspace developer policy. The connector-managed OAuth identity, granted Calendar scopes, backend request mapping, retention behavior, and whether any server-side projection occurs before the wrapper response remain unknown.

## Strongest objection

The wrapper may intentionally hydrate full event objects because search consumers often need summaries/descriptions, and limiting `max_results` plus not persisting bodies may be sufficient for this internal experiment.

**Response:** that can be acceptable for a tightly bounded one-off read, but it does not satisfy a metadata-only capability claim. The provider already offers a lower-data response mechanism; absence of caller-visible projection means the current wrapper has a larger data exposure surface than the WorkItem requires.

## Falsifier

Move toward `ADMIT` for a metadata-minimal search claim only if a distinct verifier, under the same effective principal and bounded query/window, can show either:

1. a changed connector schema exposes response projection and the returned payload omits non-requested body/attendee fields; or
2. a matched raw Calendar v3 `events.list` call with an explicit `fields` selector returns the required identifiers/timestamps while omitting description/attendee/body fields, and the wrapper is proven to apply an equivalent projection.

`REVISE` remains if the wrapper continues returning full descriptions for a WorkItem that only requires identifiers/time boundaries.

## Consumer / fitness

Consumer: `X13_GCAL_SEARCH_READONLY_012_PHASE2_CONTENT_MINIMIZATION_GATE`.

This card earns **0 fitness** until a WorkItem explicitly consumes the boundary and records ConsumerAck. Candidate count/research volume confer no credit.
