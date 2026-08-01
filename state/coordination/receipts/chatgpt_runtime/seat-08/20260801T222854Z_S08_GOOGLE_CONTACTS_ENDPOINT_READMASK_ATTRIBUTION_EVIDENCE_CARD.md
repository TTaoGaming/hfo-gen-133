---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_GOOGLE_CONTACTS_ENDPOINT_READMASK_ATTRIBUTION_20260801T222854Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
wip: 1
valid_time_utc: 2026-08-01T22:28:54Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: agent_runtime_cots_capabilities
candidate_name: Google_Contacts_read_only_lookup_and_recipient_resolution_connector
candidate_version: UNKNOWN_NOT_EXPOSED
possible_upstream_endpoint: people.searchContacts_UNVERIFIED
source_commit: f2e4df9e1aabd72ff89fe3c1686dc9ff30759ded
source_path: state/coordination/experiments/cots_connector_x13/20260801T214825Z_GOOGLE_CONTACTS_READONLY_PHASE1_BASELINE.md
source_blob: db1b207ce2baac4c3e5f3e68cc51168b08a9e248
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_COUNTS_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_then_distinct_nonproducer_trace_capable_review
consumer: X13_COTS_AND_CONNECTOR_PDCA_LAB_and_S05_OPERATOR_RELIEF_CELL
expiry_utc: 2026-08-03T22:28:54Z
fitness_credit: ZERO_UNTIL_EXACT_WORKITEM_CONSUMPTION
same_provider_binding_weight: 0
sealed: false
---

# S08 evidence card — Google Contacts endpoint and `readMask` attribution boundary

## Changed queue edge and bounded uncertainty

X13 phase 1 recorded one bounded synthetic `Google_Contacts.search_contacts` call with
`max_results=3`: `SUCCESS_EMPTY`, zero normalized results, no contact body, no
identity-bearing result, no surfaced error, and 972 ms connector latency. The exposed
wrapper accepted only `query` and `max_results`; it did not expose the upstream method,
`readMask`, source selection, cache warmup, OAuth scope, retries, or request count.

**Question:** may HFO attribute that successful wrapper call to Google People API
`people.searchContacts` and inherit that endpoint's corpus, freshness, and field-mask
semantics?

## Decision

`REVISE`.

Admit only this claim:

> One connector-defined, bounded candidate-lookup invocation completed without a
> surfaced error and returned no normalized match.

Do not label the result a verified `people.searchContacts` call, a fresh Contacts
search, or evidence that a person is absent. Exact upstream endpoint, field mask,
cache state, searched corpus, OAuth scope, and least privilege remain unknown.

## Primary-source evidence observed on 2026-08-01

1. Google `people.searchContacts` reference:
   https://developers.google.com/people/api/rest/v1/people/searchContacts
2. Google Contacts search guide:
   https://developers.google.com/people/v1/contacts
3. Google `otherContacts.search` reference:
   https://developers.google.com/people/api/rest/v1/otherContacts/search
4. Google `people.searchDirectoryPeople` reference:
   https://developers.google.com/people/api/rest/v1/people/searchDirectoryPeople
5. Google People API Person resource:
   https://developers.google.com/people/api/rest/v1/people

The official `people.searchContacts` contract requires a `readMask`, searches the
signed-in user's grouped contacts, defaults `sources[]` to `CONTACT`, caps page size at
30, and documents an empty-query warmup followed by a delay because search uses a lazy
cache. Google exposes separate APIs for other contacts and Workspace directory search.

## Inference, explicitly bounded

Because the direct `people.searchContacts` API requires a `readMask`, while the HFO
wrapper exposes no field-mask argument, one of at least two conditions must be true:

1. the wrapper injects a hidden field mask and calls `people.searchContacts`; or
2. the wrapper calls a different provider endpoint or internal abstraction.

The phase-1 receipt cannot distinguish these cases. Therefore, inheriting exact People
API endpoint semantics from the wrapper name would be evidence inflation.

## Supported claims

- The exact X13 source event exists at commit and blob named above.
- One bounded wrapper call accepted a synthetic no-match query and returned zero
  normalized candidates without a surfaced error.
- No contact body or identity-bearing result was externalized by that event.
- If the wrapper actually uses `people.searchContacts`, some `readMask` must have been
  supplied upstream, and the default documented source would be grouped contacts.

## Excluded claims

- Exact upstream Google method, request URL, API version, request count, or retries.
- Exact `readMask`, returned-field ceiling, cache age, warmup execution, or delay.
- Coverage of other contacts, Workspace directory, Gmail history, another account, or
  all people data.
- Freshness, uniqueness, completeness, deterministic recipient selection, or absence.
- OAuth identity, token type, scope, credential custody, or least privilege.
- Any email send, invite, account action, contact write, or consumer acceptance.

## License, terms, cost, and operator burden

```yaml
documentation_license_observed: Google_documentation_CC_BY_4_0_and_code_samples_Apache_2_0_per_site_notice
connector_software_license: UNKNOWN
connector_terms_and_version: UNKNOWN_NOT_EXPOSED
live_oauth_scope_and_identity: UNKNOWN
credentials_used_by_s08: none
account_or_terms_action: none
direct_research_cost_usd: 0
operator_minutes_this_research: 0
estimated_operator_review_minutes_for_one_future_positive_probe: 2_to_5_UNVALIDATED
estimated_operator_minutes_avoided_per_successful_unambiguous_lookup: 1_to_3_UNVALIDATED
```

## Strongest objection

X13 already recorded that `readMask`, cache warmup, scope, and source are hidden. The
increment here is narrower: it turns that caveat into an endpoint-attribution gate and
prevents grouped contacts, other contacts, and directory semantics from being blended
into one unsupported "Google Contacts" claim.

## Strongest falsifier

Revise or retire this attribution warning when a source-bound provider trace or
connector contract exposes all of the following for the same wrapper version:

- exact upstream endpoint and API version;
- exact `readMask` and source parameters;
- warmup and delay behavior;
- normalized field mapping and result-source class;
- request count, retries, OAuth scope class, and privacy handling.

A positive trace showing a different endpoint would strengthen the need for a
connector-specific contract rather than People API inheritance.

## Reversible next experiment

Only after an exact WorkItem names an existing operator obligation, run one no-send,
low-cap lookup for an already-known recipient. Persist no identity-bearing value in Git
or Slack. Record only result count, returned field classes, ambiguity class, latency,
source class if exposed, and a digest held in the private source system. If the wrapper
permits an empty-query warmup, compare the same bounded lookup before and after the
documented warmup delay. Never auto-select a fuzzy or multi-candidate result.

If the wrapper cannot expose or attest endpoint, `readMask`, and warmup behavior, retain
the connector-defined lookup claim ceiling even when a positive candidate is returned.

## Verifier, consumer, expiry, and honest flaw

- **Verifier:** S04 may verify exact source/card structure; a distinct trace-capable
  nonproducer must verify any endpoint-attribution claim.
- **Consumer:** X13 may use this gate in Contacts phases 2–4; S05 may consume it only
  inside a named no-send recipient-resolution WorkItem.
- **Expiry:** `2026-08-03T22:28:54Z`; revalidate official contracts and connector
  version after expiry.
- **Fitness:** zero until an exact WorkItem records consumption or evidence-backed
  rejection against this card blob.

Honest flaw: S08 made no live Contacts call, used no private contact data, and saw no
provider trace, connector source, version, OAuth grant, or positive normalized result.
The endpoint alternatives are a constrained inference from the mismatch between the
official required parameter and the wrapper's exposed schema, not proof of the hidden
implementation. This is same-provider advisory evidence with binding weight zero.
