---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08
carrier_task_id: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
research_lane: agent-runtime/COTS capabilities
queue_source: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_version: 142
experiment_id: X13_GDRIVE_SEARCH_READONLY_011
bounded_uncertainty: "Can one high-entropy synthetic nonmatching metadata-only Drive search validly test the connector's empty-success versus error response shape without supporting an authoritative absence claim?"
candidate: Google_Drive.search connector surface
candidate_schema_observed_utc: 2026-08-06T19:28:40Z
phase: 3
consumer: X13_GDRIVE_SEARCH_READONLY_011_PHASE3_SYNTHETIC_NONMATCH_EMPTY_OR_ERROR_SHAPE_GATE
verifier: DISTINCT_SAME_PRINCIPAL_RAW_DRIVE_V3_FILES_LIST_WITH_EXACT_QUERY_MAPPING_CORPORA_SPACES_SCOPES_AND_RESPONSE_FLAGS
verifier_result: NOT_RUN
decision: ADMIT
decision_scope: EMPTY_SUCCESS_OR_ERROR_SHAPE_PROBE_ONLY
paid_cost_usd_observed: 0
operator_minutes_removed_measured: 0
producer_operator_minutes_estimate: 5_to_10
verifier_operator_minutes_estimate: 15_to_30
review_expiry_utc: 2026-08-13T19:28:40Z
valid_time_utc: 2026-08-06T19:28:40Z
recorded_time_utc: 2026-08-06T19:28:40Z
---

# S08 Evidence Card — Drive phase-3 synthetic nonmatch boundary

## Decision

`ADMIT` only as an `EMPTY_SUCCESS_OR_ERROR_SHAPE_PROBE`.

A single high-entropy, punctuation-free alphanumeric token is a suitable bounded diagnostic input for phase 3 because the exposed `Google_Drive.search` schema says all query tokens must match, and an explicit `item_type=document` request is metadata-only and searches one provider page without fetching file contents. The probe must use one token, one call, `topn=1`, `item_type=document`, `best_effort_fetch=false`, `require_viewed_by_user=false`, no `special_filter_query_str`, no `page_token`, no retry, and no automatic broadening after an empty result.

Recommended token form generated immediately before the producer call: `hfonomatch` + at least 32 lowercase hexadecimal characters, with no spaces, punctuation, quotes, Drive operators, known project terms, or pre-existing repository/workspace identifiers. The exact token and request fields should be persisted before execution. The token is not proven absent; it only minimizes accidental collision.

## Current primary evidence

1. Google Drive API v3 `files.list`, last updated 2026-07-07 UTC:
   https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
   - `q` filters file results.
   - `pageSize` is a maximum and the service may return fewer items.
   - response fields include `files[]`, `nextPageToken`, and `incompleteSearch`.
   - `incompleteSearch=true` means some search results might be missing.
   - the default corpus is `user`, but corpora can vary with filters; shared-drive behavior requires separate parameters.

2. Google Drive API search query terms/operators, last updated 2026-07-22 UTC:
   https://developers.google.com/workspace/drive/api/guides/ref-search-terms
   - `fullText contains` matches entire string tokens.
   - `name contains` uses prefix matching.
   - quoting and punctuation have query-language semantics, so a punctuation-free high-entropy single token is less confounded than a phrase or operator-bearing string.

3. Google Drive API search guide, current read 2026-08-06:
   https://developers.google.com/workspace/drive/api/guides/search-files
   - clients are expected to inspect pagination and `incompleteSearch` when making completeness claims.
   - default `corpora=user`; broader corpora can produce incomplete searches.

4. Exposed connector contract observed 2026-08-06:
   `Google_Drive.search`
   - short specific keywords; all query tokens must match.
   - explicit `image`, `document`, or `folder` item type performs one metadata-only provider page and never fetches file contents.
   - search covers all accessible drives by default.
   - provider-owned `next_page_token` is returned when exposed.
   - schema suggests broadening an empty-result search, but this phase intentionally forbids broadening because the goal is to observe the first empty/error branch exactly once.

## Supported claims

- One bounded high-entropy-token request can test whether this connector invocation returns a successful empty result, an unexpected nonempty result, or an error envelope.
- `item_type=document` plus `best_effort_fetch=false` is metadata-only according to the exposed connector contract.
- A successful empty result from this one call can be recorded as `NO_MATCH_RETURNED_IN_THIS_OBSERVATION`.
- A nonempty result is a valid signal of token collision, query transformation/tokenization, or broader matching than assumed and should cause phase-3 revision rather than retry/broadening.
- An error should be preserved exactly as the observed connector error class without converting it into absence.

## Excluded claims

- No returned result does not prove the token is absent from Drive, all accessible drives, all corpora, hidden/unindexed content, or the authenticated principal's complete visibility set.
- This probe does not establish completeness, freshness, raw-provider parity, stable indexing, effective OAuth scopes, shared-drive coverage, MIME correctness, deterministic ordering, pagination durability, or provider quota accounting.
- `item_type=document` remains a wrapper category and must not be interpreted as the Google Docs MIME type.
- The wrapper's internal mapping from `query` to Drive v3 `q`, its effective `corpora`, `spaces`, shared-drive parameters, OAuth principal, selected fields, and `incompleteSearch` propagation are not exposed by the schema and remain unknown.
- This card does not execute the Drive probe and therefore does not inspect or use private Drive data.

## Probe interpretation contract

```text
EMPTY_SUCCESS => NO_MATCH_RETURNED_IN_THIS_OBSERVATION
NONEMPTY      => UNEXPECTED_MATCH_OR_QUERY_TRANSFORMATION; REVISE; NO_RETRY
ERROR         => EXACT_OBSERVED_CONNECTOR_ERROR_CLASS; NO_ABSENCE_CLAIM

EMPTY_SUCCESS != AUTHORITATIVE_ABSENCE
EMPTY_SUCCESS != COMPLETE_SEARCH
EMPTY_SUCCESS != RAW_PROVIDER_PARITY
EMPTY_SUCCESS != EFFECTIVE_SCOPE_PROOF
```

If the wrapper exposes `next_page_token`, `incompleteSearch`, or another partial-result indicator on the empty branch, persist it. Their absence from the wrapper response is not proof that the provider returned no such state.

## License / terms uncertainty

Google's developer documentation states page prose is generally CC BY 4.0 and code samples Apache 2.0. That documentation license does not determine rights in any Drive file returned by a search. Effective connector OAuth identity/scopes, Google Workspace administrator restrictions, retention policy, shared-drive visibility, and quota accounting are unknown. No account creation, terms acceptance, content hydration, or private-file inspection is authorized by this card.

## Strongest objection

The exposed connector is not documented as a transparent `files.list` wrapper, so even a carefully chosen token cannot prove which provider query was executed or whether an empty wrapper result corresponds to an empty raw Drive result. This objection is valid and is why the admitted claim is limited to wrapper response-shape behavior only.

## Falsifier

`REVISE` if the one-token probe returns any result, if the wrapper visibly rewrites/broadens the query, if an identical same-principal raw Drive v3 request mapped by a distinct verifier produces a materially different empty/nonempty/error classification, or if the wrapper suppresses provider partial-search state needed to interpret the result safely.

## Verification requirement

A distinct verifier may later map the exact wrapper request to a same-principal raw Drive v3 `files.list` request and bind: effective `q`, `corpora`, `spaces`, shared-drive flags, OAuth scope/principal ceiling, selected fields, HTTP/error class, `files[]`, `nextPageToken`, `incompleteSearch`, and timestamp. That verification is not required merely to record the wrapper's observed empty/error shape, but it is required before claiming provider parity or absence.

## Cost / operator burden

- Research/write cost observed: `$0`; no paid call surfaced.
- Drive provider quota debit: not observed and not inferable from this card.
- Operator minutes removed: `0` measured.
- Producer amendment/execution estimate: `5–10 minutes`.
- Distinct raw-provider verification estimate: `15–30 minutes`.

## Consumption / fitness

Consumer: `X13_GDRIVE_SEARCH_READONLY_011_PHASE3_SYNTHETIC_NONMATCH_EMPTY_OR_ERROR_SHAPE_GATE`.

This card earns zero fitness until that WorkItem consumes its exact Git pointer and records ConsumerAck. Research volume and candidate count are not credited.

## Honest flaw

The recommended token has only probabilistic non-collision, and the connector's hidden query translation/access scope prevents this research-only card from proving raw-provider semantics without a distinct same-principal provider witness.
