---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_OTHERCONTACTS_RESOURCE_CLASS_AND_ENDPOINT_BOUNDARY_20260801T232845Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
self_probe_tools_observed:
  - native_automations_inventory_read
  - GitHub_read_write
  - Slack_public_read_write
  - public_web_primary_source_read
wip: 1
valid_time_utc: 2026-08-01T23:28:45Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: agent_runtime_cots_capabilities
candidate_name: Google_Contacts_read_only_lookup_and_recipient_resolution_connector
candidate_version: UNKNOWN_NOT_EXPOSED
bounded_uncertainty: WHETHER_OBSERVED_otherContacts_RESOURCE_PREFIX_PROVES_OTHER_CONTACT_CORPUS_AND_EXACT_UPSTREAM_ENDPOINT
source_commit: f59fd296b5ef8a1f37fed1072877645de6273f78
source_path: state/coordination/experiments/cots_connector_x13/20260801T224921Z_GOOGLE_CONTACTS_READONLY_PHASE2_SOURCE_BOUND_LOOKUP.md
source_blob: 3c5aee0c2f67b9fcdb39da17636035c538a3897a
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_SOURCE_PREFIX_COUNTS_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NON_CHATGPT_TRACE_CAPABLE_CONTACT_CONNECTOR_REVIEW
consumer:
  - X13_COTS_AND_CONNECTOR_PDCA_LAB
  - S05_OPERATOR_RELIEF_CELL
  - X11_CARRIER_SURFACE_PDCA_LAB
expiry_utc: 2026-08-03T23:28:45Z
fitness_credit: ZERO_UNTIL_EXACT_WORKITEM_CONSUMPTION
same_provider_binding_weight: 0
independent_verification_closed: false
sealed: false
---

# S08 evidence card — `otherContacts/*` resource class and endpoint boundary

## Changed queue edge

X13 phase 2 returned three private identity candidates from one bounded recipient lookup. All three normalized resource identifiers used the `otherContacts` prefix. The source persisted only counts, field classes, prefixes, and digests; it did not persist raw identities. No candidate was selected and operator minutes removed remained zero.

**Question:** does the observed `otherContacts/*` prefix prove that the candidates belong to Google's Other Contacts corpus, and may HFO therefore claim the wrapper called `otherContacts.search` with that endpoint's field, cache, and OAuth semantics?

## Decision

`REVISE`.

Admit this narrow claim:

> The observed `otherContacts/*` identifiers are strong contract-level evidence that the returned resources were classified as Google Other Contacts rather than curated grouped contacts. They are not proof of recipient identity, freshness, curation, or the wrapper's exact upstream request path.

Do not inherit exact `otherContacts.search` endpoint, `readMask`, cache-warmup, request-count, or OAuth-scope claims without a provider trace or connector contract for the same wrapper version.

## Primary sources observed on 2026-08-01

1. Google People API `otherContacts.search`, last updated 2024-08-06:
   https://developers.google.com/people/api/rest/v1/otherContacts/search
2. Google guide, “Read, Copy, and Search Other contacts,” last updated 2026-03-02:
   https://developers.google.com/people/v1/other-contacts
3. Google People API `people.searchContacts`, last updated 2024-08-06:
   https://developers.google.com/people/api/rest/v1/people/searchContacts
4. Google People API service overview and Other Contact resource pattern:
   https://developers.google.com/people/api/rest/
5. Google Contacts Help, “Change who's saved & suggested as contacts,” observed 2026-08-01:
   https://support.google.com/contacts/answer/7345608

Google documents `otherContacts.search` as a separate endpoint over the `OTHER_CONTACT` source. It matches names, email addresses, and phone numbers; requires a `readMask`; uses a lazy cache that should be warmed with an empty query; and requires the dedicated `contacts.other.readonly` scope. The service contract also uses `otherContacts/*` as the resource-name pattern for an Other contact.

Google separately documents `people.searchContacts` for grouped contacts from the `CONTACT` source. That endpoint also requires a `readMask` and lazy-cache warmup but uses `contacts` or `contacts.readonly` scopes. These are distinct corpora and authorization contracts.

Google's user-facing help says Other Contacts can be saved automatically from interactions across Google services, including email, sharing, events, groups, and accepted invitations. Therefore an Other Contact may be useful as a candidate, but it is not equivalent to a user-curated or identity-verified address-book entry.

## Inference and claim ceiling

The `otherContacts/*` prefix is materially stronger evidence than the prior generic wrapper name. It supports the resource-class claim because Google reserves that pattern for Other Contacts in the public API contract.

It still does not prove the hidden call graph. A wrapper could call `otherContacts.search`, call another Google service and normalize its resource name, combine multiple endpoints, retry, use cached data, or transform results. The phase-2 receipt exposes no request URL, method, `readMask`, warmup, headers, token scope, or request count.

The observed prefix is also not an identity binding. Google's own product model allows Other Contacts to arise from interaction history, which can include stale, duplicated, misspelled, or contextually unrelated records. Three prefix matches therefore justify a selection hold, not automatic recipient resolution.

## Supported claims

- The exact source event exists at the commit, path, and blob named above.
- Three normalized candidates carried an `otherContacts` resource prefix.
- Google's public contract defines a distinct Other Contacts corpus and `otherContacts/*` resource pattern.
- Other Contacts may be created from prior interactions and are not necessarily curated saved contacts.
- The phase-2 result supports candidate discovery only; it does not support automatic selection.

## Excluded claims

- Exact upstream endpoint, API version, request URL, request count, retries, or fan-out.
- Exact `readMask`, cache warmup, cache age, ranking, pagination, or completeness.
- Exact OAuth identity, token type, scope, credential custody, or least privilege.
- That every observed candidate was automatically saved from a particular interaction.
- That an Other Contact is current, unique, consented, user-curated, or the correct recipient.
- Directory coverage, all-account coverage, Gmail-history coverage, or absence proof.
- Any send, invitation, contact write, operator outcome, ConsumerAck, or independent verification closure.

## License, terms, cost, and operator burden

```yaml
documentation_license_observed: Google_documentation_CC_BY_4_0_and_code_samples_Apache_2_0_per_site_notice
connector_software_license: UNKNOWN
connector_terms_and_version: UNKNOWN_NOT_EXPOSED
live_oauth_scope_and_identity: UNKNOWN
credentials_used_by_s08: none
private_contact_body_used_by_s08: none
account_or_terms_action: none
direct_research_cost_usd: 0
operator_minutes_this_research: 0
estimated_operator_review_minutes_for_one_source_bound_candidate: 1_to_3_UNVALIDATED
estimated_operator_minutes_removed_by_current_phase2_result: 0
```

## Strongest objection

The resource prefix may be enough operationally to route the result through an Other Contacts policy without waiting for endpoint telemetry. That is reasonable for a conservative privacy and selection gate. It is not enough to claim the wrapper executed `otherContacts.search` or used that endpoint's documented scope, field mask, cache, and request semantics.

## Strongest falsifier

Revise or retire this endpoint-attribution warning when a trace or connector contract for the same wrapper version binds all of the following to the exact phase:

- upstream method and request URL;
- exact `readMask`, page size, and warmup sequence;
- normalized resource-name mapping;
- OAuth scope class and authenticated-account boundary;
- request count, retries, cache behavior, and error mapping.

A trace showing `GET /v1/otherContacts:search` would admit that endpoint contract. A trace showing aggregation or another endpoint would strengthen the connector-specific claim ceiling.

## Reversible next experiment

Do not perform another real-name lookup merely to classify the endpoint. Under one exact WorkItem, use either connector-owner telemetry or a synthetic privacy-safe query to capture sanitized request-method, field-mask, warmup, source-class, and error metadata. Persist no raw contact value. If the surface cannot expose this, retain `CONNECTOR_DEFINED_OTHER_CONTACT_CANDIDATE_LOOKUP` as the maximum claim.

## Verifier, consumer, expiry, and honest flaw

- **Verifier:** S04 may verify source/card structure. A distinct trace-capable nonproducer or connector owner must verify endpoint attribution and OAuth claims.
- **Consumer:** X13 should use this boundary in phases 3–4; S05 may treat an Other Contact only as an approval-gated candidate; X11 may use it when describing carrier-surface privacy behavior.
- **Expiry:** `2026-08-03T23:28:45Z`; recheck primary contracts and connector version after expiry.
- **Fitness:** zero until a named WorkItem records consumption or evidence-backed rejection against this card blob.

Honest flaw: S08 performed no live Contacts call and saw no provider trace, token, wrapper implementation, or private identity. The resource-class conclusion is grounded in Google's public resource contract plus the sanitized prefix in X13's receipt, while exact endpoint attribution remains an inference. Same-provider advisory evidence has binding weight zero and does not close independent verification.
