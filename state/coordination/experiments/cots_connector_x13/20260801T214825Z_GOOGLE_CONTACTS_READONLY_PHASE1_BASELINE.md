---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GOOGLE_CONTACTS_READONLY_PHASE1_20260801T214825Z
experiment_id: X13_GOOGLE_CONTACTS_READONLY_CONNECTOR_001
seat: X13_COTS_AND_CONNECTOR_PDCA_LAB
candidate: Google_Contacts_read_only_lookup_and_recipient_resolution_connector
phase: 1_of_4
result: PHASE1_BASELINE_ACCEPTED_WITH_CACHE_FRESHNESS_AND_FIELD_MASK_UNKNOWN
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: NATIVE_AUTOMATIONS_LIST_READBACK
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
prior_current_version: 24
prior_current_commit: c64fd4fd6016dd7ce80856eb0a779fbb32621fb7
prior_current_blob_sha: 7bab581d06e41007d3fee142a1b664c37ffbd406
effect_ceiling: ONE_SYNTHETIC_READ_ONLY_CONTACT_SEARCH_NO_MATCH_NO_CONTACT_BODY_READ_NO_RECIPIENT_SELECTION_NO_SEND_NO_CONTACT_WRITE_NO_IDENTITY_EXTERNALIZATION
valid_time_utc: 2026-08-01T21:48:25Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 Google Contacts read-only connector — phase 1 baseline

## Direct connector receipt

A single synthetic, non-sensitive query was sent through `Google_Contacts.search_contacts` with `max_results=3`.

- query class: synthetic high-entropy no-match probe
- query SHA-256: `e72c906ca73ab85339ac2259a07643060c1dae8ce9244873cb3781f89388be3e`
- result: `SUCCESS_EMPTY`
- result count: `0`
- contact body returned: `false`
- identity-bearing result returned: `false`
- connector error: `none`
- external call time: `972 ms`
- connector ID present: `true`
- connector ID SHA-256: `478d5d64c3c1cd5739c60eca0bcb3b6b9fbc7107545f88cf77f165f2dd77b26f`
- operator-supplied credentials this wake: `0`
- paid cost surfaced: `$0`
- provider request count, quota units, headers, retries, and wrapper fan-out: `NOT_EXPOSED`

The successful private-source query proves only that an authenticated read path was available for this bounded call. It does not prove the authenticated identity, OAuth scope, token type, credential custody, directory access, completeness, cache freshness, or least privilege.

## Official contract baseline

Primary references reviewed on 2026-08-01:

- `people.searchContacts`: https://developers.google.com/people/api/rest/v1/people/searchContacts
- Contact search guide: https://developers.google.com/people/v1/contacts
- `people.get`: https://developers.google.com/people/api/rest/v1/people/get
- Person resource and merged-source semantics: https://developers.google.com/people/api/rest/v1/people
- People API introduction: https://developers.google.com/people

The official contract states:

1. `people.searchContacts` searches the authenticated user's grouped contacts from the `CONTACT` source and matches prefix phrases against names, nicknames, email addresses, phone numbers, and organizations.
2. `pageSize` is bounded and capped at 30.
3. A `readMask` is required to restrict returned fields.
4. Clients should first send an empty-query warmup request, wait several seconds, and then search because the endpoint uses a lazy cache.
5. Search requires either the `contacts` or `contacts.readonly` OAuth scope.
6. `people.get` requires a field mask and can return highly sensitive fields, including addresses, birthdays, phone numbers, organizations, biographies, relations, and user-defined data.
7. Person data may be merged from contacts, profiles, and Workspace directory sources when those sources are linked.

## Connector variance found

The exposed connector accepts only `query` and `max_results` for search. It does not expose or attest:

- `readMask`
- source selection
- empty-query cache warmup
- warmup-to-search delay
- upstream method or request URL
- OAuth scope or authenticated identity
- whether results include grouped contacts only or additional directory/profile sources
- request count, quota class, retries, or response headers

Therefore, `SUCCESS_EMPTY` means only `NO_MATCH_RETURNED_BY_ONE_WRAPPER_CALL`. It cannot prove the named person is absent from Contacts, the directory, Gmail history, another account, or a stale cache.

## Measurements

- operator relay minutes: `0`
- operator minutes removed measured: `0` — no named consumer or obligation was resolved
- operator minutes removed estimate per future bounded lookup: `1_to_3_UNVALIDATED`
- custom code avoided estimate:
  - contact query and result normalization: `30_to_80_LOC_UNVALIDATED`
  - authenticated People API client and token refresh: `MATERIAL_BUT_UNQUANTIFIED`
  - recipient candidate display and selection plumbing: `20_to_80_LOC_UNVALIDATED`
  - duplicate disambiguation, privacy redaction, cache freshness, and approval policy: `NOT_AVOIDED_REQUIRES_HFO_GATES`
  - additive total: `NOT_CLAIMED_BECAUSE_FUNCTIONS_OVERLAP`
- credentials: connector authenticated for this call; live identity, scope, token type, and custody `UNKNOWN`
- durability: Google Contacts provider storage only; no workflow replay, resume, transaction, idempotency, or exactly-once guarantee
- observability: medium for wrapper action, result count, normalized error, connector identity, and latency; low for upstream request shape, field mask, warmup, scope, quota, retries, and cache age
- portability: medium for provider-neutral name/email lookup intent; low-to-medium for Google prefix matching, merged-person semantics, opaque resource names, and wrapper-specific result normalization
- failure behavior: not tested in phase 1
- direct cost/quota evidence: no charge surfaced; exact quota model and per-call units were not exposed or proven

## Provisional gates

1. Use Contacts only for one named obligation and one bounded recipient-resolution question.
2. Search first; do not call `read_contact` unless the named consumer requires a specific missing field.
3. Treat every matched result as private identity data. Persist only sanitized counts, field classes, and digests unless the consumer explicitly requires the address.
4. Never auto-select or send to a recipient from fuzzy, prefix, duplicate, or multi-source results.
5. Require operator approval before any email send, invite, or external action.
6. Treat empty results as `NO_MATCH_RETURNED_BY_ONE_WRAPPER_CALL`, not absence.
7. Until warmup behavior is exposed or independently measured, do not claim current-cache completeness.
8. Do not claim least privilege while OAuth scope and field mask remain hidden.

## Strongest falsifier

A source-bound phase-2 trace shows that the wrapper returns overbroad contact fields, stale or ambiguous candidates, directory/profile entries outside the intended contact source, or cannot preserve a deterministic selected-address digest without exposing private bodies. Any of those would force `DEFER` or a narrower metadata-only gate.

## Reversible next experiment

Resolve one already-known recipient for an existing operator obligation using a bounded name or exact-email query, low result cap, no send, no contact-body persistence, and no automatic selection. Record only result count, returned field classes, ambiguity, stable digest, latency, and whether the named consumer accepted the resolution.

## Verifier and consumer

- structural verifier: `S04_STRUCTURAL_PREFLIGHT`
- distinct nonproducer verifier requested: `NON_CHATGPT_CONTACT_CONNECTOR_REVIEW`
- consumers: `S05_OPERATOR_RELIEF_CELL`, `X11_CARRIER_SURFACE_PDCA_LAB`
- fitness credit: `0_PENDING_EXPLICIT_SOURCE_BOUND_CONSUMER_ACK`
- same-provider binding weight: `0`
- independent verification closed: `false`

## Honest flaw

This phase used one synthetic empty-result query only. It did not perform the official empty-query warmup, wait several seconds, produce a matched contact, test duplicate names, test directory behavior, call `read_contact`, exercise permission or rate-limit errors, verify the field mask, or measure whether the wrapper made one or multiple upstream requests.
