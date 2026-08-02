---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_CONTACTS_NEGATIVE_PAGESIZE_CLAIM_BOUNDARY_20260802T002911Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
self_probe_tools_observed:
  - native_automations_inventory_read
  - GitHub_search_compare_fetch_create_readback
  - Slack_pointer_write
  - public_web_primary_source_read
wip: 1
valid_time_utc: 2026-08-02T00:29:11Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: agent_runtime_cots_capabilities
candidate_name: Google_Contacts_read_only_lookup_and_recipient_resolution_connector
candidate_version: UNKNOWN_NOT_EXPOSED
bounded_uncertainty: WHETHER_PHASE3_MAY_GENERALIZE_ONE_NEGATIVE_PAGE_SIZE_FAILURE_INTO_A_DOCUMENTED_PROVIDER_RANGE_0_TO_30
source_current_commit: 89e611adf18a89fa4800afa58657aca355a3db26
source_current_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
source_current_blob: 798eaa1146414668fe2aad0a38c30b1c599c0247
source_event_commit: 2d6a8d50dc440a5b29198d54d5940f2030e0b305
source_event_path: state/coordination/experiments/cots_connector_x13/20260801T234800Z_GOOGLE_CONTACTS_READONLY_PHASE3_SYNTHETIC_INVALID_PAGESIZE.md
source_event_blob: ff965515cf05dfc127a5105a8f8328701ea9d7c9
source_gate_commit: 15df9d9d2390fcbf93dfcff3244a1fa2d88dafe8
source_gate_path: state/coordination/receipts/chatgpt_runtime/seat-15/20260801T235436Z_X13_CONTACTS_PHASE4_REUSE_GMAIL_CORRECTED_ADOPTION_GATE.yaml
source_gate_blob: cc3fbca79eff080413c4955d8efe018c59a28803
source_gate_structural_commit: 9985acdb21ec3dfb03fcdd2d4eed9900a4749ffd
source_gate_structural_blob: f5130269ff6284d5c740aa101ceafc96a8cfb382
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_FAILURE_METADATA_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NON_CHATGPT_CONTACT_CONNECTOR_OWNER_OR_PROVIDER_TRACE_REVIEWER
consumer:
  - X13_COTS_AND_CONNECTOR_PDCA_LAB_PHASE4
  - S05_OPERATOR_RELIEF_CELL
  - X11_CARRIER_SURFACE_PDCA_LAB
expiry_utc: 2026-08-09T00:29:11Z
fitness_credit: ZERO_UNTIL_EXACT_WORKITEM_CONSUMPTION
same_provider_binding_weight: 0
independent_verification_closed: false
sealed: false
---

# S08 evidence card — Contacts negative `pageSize` claim boundary

## Changed queue edge

X13 phase 3 sent one synthetic request through `Google_Contacts.search_contacts` with `max_results=-1`. The provider returned HTTP 400 `INVALID_ARGUMENT`, no identity-bearing result, and the sanitized failure trace exposed `people:searchContacts`. The event labeled the failure class `PAGE_SIZE_OUTSIDE_PROVIDER_RANGE_0_TO_30` and phase 4 is now pending.

**Question:** does that trace plus Google's public documentation establish a general valid provider range of `0..30`, with all values outside that range invalid?

## Decision

`REVISE`.

Use this narrower claim:

> For this connector trace, `max_results=-1` reached `people:searchContacts` and was rejected with HTTP 400 `INVALID_ARGUMENT`. Google documents that omitted or zero `pageSize` defaults to 10 and values above 30 are capped to 30. The documentation does not state a complete valid integer interval or promise the observed error class for every negative value.

Replace `PAGE_SIZE_OUTSIDE_PROVIDER_RANGE_0_TO_30` with an observation-bound class such as `NEGATIVE_PAGE_SIZE_REJECTED_IN_THIS_TRACE`.

## Primary sources checked on 2026-08-02

1. Google People API `people.searchContacts`, last updated 2024-08-06:
   https://developers.google.com/people/api/rest/v1/people/searchContacts
2. Google People API `otherContacts.search`, last updated 2024-08-06:
   https://developers.google.com/people/api/rest/v1/otherContacts/search
3. Google guide, “Read, Copy, and Search Other contacts,” last updated 2026-03-02:
   https://developers.google.com/people/v1/other-contacts

Both search endpoint references say `pageSize` is optional, defaults to 10 when omitted or set to 0, and values above 30 are capped to 30. Neither reference defines negative-value behavior, a minimum accepted value, or a universal `INVALID_ARGUMENT` mapping for every out-of-range integer. The 2026 guide documents lazy-cache warmup but adds no negative-page-size contract.

## Supported claims

- Exact X13 source pointers and blobs named above existed at review.
- One synthetic `max_results=-1` call produced HTTP 400 `INVALID_ARGUMENT` and no contact identity result.
- The error path exposed `people:searchContacts`; that remains error-path attribution only.
- Google documents zero as defaulting to 10 and values above 30 as being capped to 30 for both Contacts search endpoints.
- The phase-4 gate should preserve sanitized error handling and avoid broad range claims.

## Excluded claims

- A documented inclusive valid range of `0..30`.
- That every negative integer fails identically, or that all failures use HTTP 400 `INVALID_ARGUMENT`.
- That values above 30 fail; Google documents capping, not rejection.
- That the wrapper validates before the provider, forwards every integer unchanged, or uses the same endpoint on successful calls.
- Exact connector version, implementation, retry count, request fan-out, OAuth scope, authenticated identity, quota, billing, or least privilege.
- Recipient correctness, automatic selection, send authority, ConsumerAck, operator outcome, or independent-verification closure.

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
estimated_operator_review_minutes_for_phase4_wording: 1_to_2
estimated_operator_minutes_removed_by_current_card: 0_UNTIL_CONSUMED
```

## Strongest objection

The shorthand `range 0 to 30` is operationally intuitive because zero is accepted as a default and 30 is the documented cap. But it is technically wrong as a provider contract: values above 30 are documented to be capped rather than rejected, and negative behavior is established only by one observed `-1` trace.

## Falsifier

Revise this card if a current official schema, protobuf validation rule, connector contract, or repeatable provider trace for the same wrapper version explicitly defines the accepted integer domain and stable error mapping. A trace showing any negative value accepted or normalized would falsify the current observation-generalization. A source defining all negatives as invalid would support a broader negative-domain rule, but still would not make values above 30 invalid because the current public contract says they are capped.

## Reversible next experiment

No new Contacts call is required for phase 4. Change only the decision wording and failure taxonomy:

- observed: `-1 -> HTTP 400 INVALID_ARGUMENT`;
- documented: `0 or omitted -> default 10`;
- documented: `>30 -> capped to 30`;
- unknown: other negative values, wrapper normalization, and stable error mapping.

If a future WorkItem needs a client-side validator, constrain it to rejecting negative integers locally and capping or allowing provider capping above 30, then verify against a synthetic test surface without real identity data.

## Verifier, consumer, expiry, and honest flaw

- **Verifier:** S04 may verify exact source binding and card structure. A distinct connector owner or provider-trace reviewer must verify runtime semantics.
- **Consumer:** X13 phase 4 should consume or reject this wording before finalizing the Contacts decision. S05 and X11 may reuse the narrower failure class.
- **Expiry:** `2026-08-09T00:29:11Z`; recheck official contracts and connector version after expiry.
- **Fitness:** zero until a named WorkItem records exact consumption or evidence-backed rejection against this card blob.

Honest flaw: S08 performed no live connector call and did not inspect wrapper code or provider schemas. The card relies on one existing sanitized failure receipt plus current official documentation. It narrows an overgeneralized claim; it does not establish complete validation semantics. Same-provider advisory evidence has binding weight zero.
