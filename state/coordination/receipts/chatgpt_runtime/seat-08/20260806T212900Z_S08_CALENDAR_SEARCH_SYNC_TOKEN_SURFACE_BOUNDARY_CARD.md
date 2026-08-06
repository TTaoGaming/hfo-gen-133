---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08
task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
lane: agent-runtime/COTS capabilities
queue_source:
  path: state/coordination/experiments/cots_connector_x13/CURRENT.md
  version: 144
  experiment_id: X13_GDRIVE_SEARCH_READONLY_011
  next_campaign_candidate: GOOGLE_CALENDAR_OR_GMAIL_READONLY_SURFACE_PENDING_SELECTION
question: CAN_THE_CURRENT_GOOGLE_CALENDAR_SEARCH_EVENTS_CONNECTOR_BE_TREATED_AS_AN_INCREMENTAL_SYNC_OR_DURABLE_CHANGE_CURSOR_SURFACE_FOR_THE_NEXT_X13_CAMPAIGN
candidate: Google_Calendar.search_events wrapper observed 2026-08-06; upstream Google Calendar API v3 events.list
candidate_version: CONNECTOR_SCHEMA_OBSERVED_2026-08-06__CALENDAR_API_V3_CURRENT_DOCS_2026-07-16
bounded_uncertainty: Whether X13 may use the exposed Calendar search connector as a provider incremental-sync cursor rather than as bounded time-window discovery.
decision: REVISE
supported_claims:
  - GOOGLE_CALENDAR_API_V3_EVENTS_LIST_SUPPORTS_INCREMENTAL_SYNC_USING_NEXTSYNCTOKEN_RETURNED_AFTER_A_COMPLETE_INITIAL_OR_INCREMENTAL_PAGE_SEQUENCE_AND_SYNCTOKEN_ON_LATER_CALLS
  - GOOGLE_DOCUMENTS_THAT_INCREMENTAL_SYNC_RETURNS_CHANGES_SINCE_THE_PRIOR_SYNC_TOKEN_AND_INCLUDES_DELETED_EVENTS
  - GOOGLE_DOCUMENTS_410_GONE_FOR_EXPIRED_OR_INVALID_SYNC_TOKENS_REQUIRING_A_FULL_RESYNC
  - THE_CURRENT_EXPOSED_GOOGLE_CALENDAR_SEARCH_EVENTS_SCHEMA_ACCEPTS_TIME_MIN_TIME_MAX_QUERY_MAX_RESULTS_CALENDAR_ID_AND_NEXT_PAGE_TOKEN_BUT_DOES_NOT_EXPOSE_SYNC_TOKEN_OR_NEXT_SYNC_TOKEN
  - THE_EXPOSED_CONNECTOR_CAN_THEREFORE_BE_RESEARCHED_AS_BOUNDED_TIME_WINDOW_SEARCH_AND_PAGINATION_BUT_NOT_CLAIMED_AS_A_DURABLE_PROVIDER_INCREMENTAL_SYNC_CURSOR_FROM_ITS_CURRENT_PUBLIC_SCHEMA
excluded_claims:
  - THE_CONNECTOR_BACKEND_DOES_NOT_INTERNALLY_USE_SYNC_TOKENS
  - THE_CONNECTOR_RESULTS_ARE_COMPLETE_OR_SNAPSHOT_CONSISTENT
  - PAGE_TOKEN_IS_A_DURABLE_CHANGE_CURSOR
  - THE_CONNECTOR_CAN_RESUME_CHANGE_DETECTION_ACROSS_WAKES_WITHOUT_RESCANNING
  - EFFECTIVE_OAUTH_IDENTITY_SCOPE_PROJECT_QUOTA_BUCKET_OR_BACKEND_PROVIDER_METHOD
  - PRIVATE_CALENDAR_CONTENT_OR_ANY_USER_EVENT_FACT
required_revision: IF_X13_SELECTS_CALENDAR_NEXT_CALL_THE_CAMPAIGN_BOUNDED_EVENT_SEARCH_PAGINATION_NOT_INCREMENTAL_SYNC; REQUIRE_EXPLICIT_TIME_BOUNDS_AND_PAGE_TOKEN_HANDLING; DO_NOT_PERSIST_OR_PROMOTE_PAGE_TOKEN_AS_SYNCTOKEN; IF_INCREMENTAL_SYNC_IS_THE_TARGET_REQUIRE_A_SURFACE_THAT_EXPOSES_NEXTSYNCTOKEN_SYNCTOKEN_AND_410_RECOVERY_SEMANTICS
license_terms_uncertainty: Google developer documentation states CC BY 4.0 for page content and Apache 2.0 for code samples; Calendar API use remains subject to Google API terms and authorization. Effective connector OAuth identity and scopes are not exposed by the observed wrapper schema. No terms were accepted and no Calendar data call was made by S08.
primary_sources:
  - date_checked: 2026-08-06
    title: Google Calendar API - Synchronize resources efficiently
    url: https://developers.google.com/workspace/calendar/api/guides/sync
    source_date: 2026-07-16
  - date_checked: 2026-08-06
    title: Google Calendar API v3 - Events list
    url: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
  - date_checked: 2026-08-06
    title: Google Calendar API - Handle API errors
    url: https://developers.google.com/workspace/calendar/api/guides/errors
internal_sources:
  - path: state/coordination/experiments/cots_connector_x13/CURRENT.md
    version: 144
    relevance: NEXT_CAMPAIGN_SELECTION_CHANGED_AFTER_DRIVE_PHASE4_DEFER
  - path_pattern: state/coordination/receipts/chatgpt_runtime/seat-03/*X13_GOOGLE_CALENDAR_FREEBUSY_PHASE4*
    relevance: PRIOR_CALENDAR_CAMPAIGN_WAS_FREEBUSY_NOT_EVENTS_LIST_INCREMENTAL_SYNC
cost:
  paid_usd_observed: 0
  operator_minutes_removed_measured: 0
  research_minutes_estimate: 12_to_20
  distinct_verification_minutes_estimate: 15_to_30
strongest_objection: The connector may internally call events.list and may even use provider sync tokens while intentionally hiding them, so absence from the public schema does not prove absence in the backend.
response_to_objection: Agreed. The evidence ceiling is interface capability, not backend implementation. Hidden internal synchronization cannot be used as caller-visible durable state or independently verified by X13, so the campaign must not promise sync-token semantics unless the surface exposes equivalent state and failure receipts.
falsifier: A changed connector schema or same-principal provider-bound receipt exposes nextSyncToken/syncToken plus exact 410 invalidation handling, allowing X13 to persist and replay an incremental cursor without private-content externalization.
verifier: DISTINCT_SCHEMA_AND_SAME_PRINCIPAL_CALENDAR_EVENTS_LIST_SYNC_TOKEN_410_RECOVERY_VERIFIER
consumer: X13_NEXT_CAMPAIGN_V145_PHASE1_SELECTION_GATE
expiry_utc: 2026-08-13T21:29:00Z
fitness_credit: 0_UNTIL_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
valid_time_utc: 2026-08-06T21:29:00Z
recorded_time_utc: 2026-08-06T21:29:00Z
---

# S08 evidence card — Calendar search is not an exposed incremental-sync surface

## Decision

`REVISE`

Google Calendar's raw `events.list` API has a real incremental-synchronization protocol: the client performs an initial full sync, persists `nextSyncToken`, later sends that token as `syncToken`, paginates with the same sync token when necessary, and replaces it with the new `nextSyncToken` on the final page. Google explicitly documents `410 Gone` as the recovery signal for an invalid or expired sync token, requiring a new full synchronization.

The Google Calendar connector surface exposed to this carrier is narrower. `search_events` accepts a bounded time window, broad free-text query, result cap, calendar ID, and `next_page_token`; it does not expose `syncToken` input or `nextSyncToken` output. Therefore its caller-visible contract supports bounded event discovery/pagination, not a durable provider change cursor.

## X13 consequence

If X13 selects Calendar after CURRENT v144, phase 1 should test `BOUNDED_EVENT_SEARCH_PAGINATION`, not `INCREMENTAL_SYNC`. Require explicit time bounds and explicit pagination handling. Never rename or persist a page token as a sync token. If the desired experiment is true incremental change polling across wakes, require a surface that exposes the provider sync cursor and the 410 reset path.

## Claim ceiling

This card does not claim the connector backend never uses sync tokens internally, does not inspect private Calendar data, and does not establish completeness, effective OAuth scope, quota accounting, or provider parity. It only binds the currently exposed interface contract against Google's current primary documentation.
