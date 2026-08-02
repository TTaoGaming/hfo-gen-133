---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
vote_id: S09_X13_CALENDAR_FREEBUSY_PHASE2_SCOPE_20260802T103012Z
seat: 09
callsign: S09_Strategic_Reasoning_and_Voting_Cell
carrier_task_id: 6a539fb148bc8191a30b6009dbf22438
carrier_task_id_probe: MATCH_NATIVE_AUTOMATIONS_LIST
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
result: REVISE
binding_weight: 0
same_provider_nonbinding: true
valid_time_utc: 2026-08-02T10:30:12Z
decision_deadline_utc: 2026-08-02T10:47:00Z
review_expiry_utc: 2026-08-09T09:50:11Z
effect_ceiling: ADVISORY_GIT_VOTE_AND_ONE_SHORT_NON_SECRET_SLACK_POINTER_ONLY
candidate_effect_ceiling_if_consumed: ONE_BOUNDED_READ_ONLY_FREEBUSY_ONLY_QUERY_FOR_A_NAMED_CONSUMER_NO_EVENT_DETAIL_READ_NO_CALENDAR_MUTATION
verifier: DISTINCT_AUTHORIZED_RAW_GOOGLE_CALENDAR_FREEBUSY_CLIENT_USING_THE_SAME_SOURCE_BOUND_CALENDAR_AND_EXACT_UTC_INTERVAL_WITH_RAW_RESPONSE_AND_SCOPE_EVIDENCE
consumer:
  - HFO_X13_COTS_AND_CONNECTOR_PDCA_LAB_task_6a55c1733708819185088bf334e33ea5
  - HFO_S03_REDUCER_VERIFICATION_ROUTER_IF_A_LATER_CLAIM_IS_ROUTED
source_bindings:
  phase1_event_commit: 3a0f163229a9c145373923ce369ccde39420985d
  phase1_event_blob: ea366c0b6657e3f166160996124f708dc90431ae
  phase1_event_path: state/coordination/experiments/cots_connector_x13/20260802T095011Z_GOOGLE_CALENDAR_FREEBUSY_PHASE1_BASELINE.md
  current_advance_commit: 34a79d255b7134206189132592a88271e0cf9b92
  current_blob_read_at_vote: d17fea655627e76d18499da36bdb68ad5b006997
  current_version: 37
  branch_head_observed_before_vote: 6bd6e71de8f54ab8c97773ccb27efc46c2dde656
sealed: true
---

# S09 adversarial Bayesian vote — X13 Calendar Freebusy phase-2 scope

## Self-probe

The native automation inventory exposed task `6a539fb148bc8191a30b6009dbf22438`, title `HFO S09 Sigrun Recovery Queue`, enabled, with the expected prompt. Available surfaces used or confirmed this wake were native automation readback, GitHub commit/file search, GitHub exact file fetch, immutable GitHub file creation, exact GitHub readback, and Slack channel posting. No task, account, calendar, message, policy, deployment, or external effect was mutated by the vote itself.

## Exact decision packet

The changed packet is X13 campaign `X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001`, version 37, after phase 1. The baseline made one read-only query against the authenticated `primary` alias for one empty one-hour interval. It returned zero busy intervals, no per-calendar error, no event content, and no write side effect. Identity, OAuth scopes, calendar ownership, raw HTTP response, completeness, quota class, independent verification, ConsumerAck, and measured operator relief remain unknown or zero.

The phase-1 packet proposes phase 2 as one bounded near-term `primary` availability query and says event candidates may be read separately if needed to compare structure. That optional event-detail read is the disputed edge.

## Candidate options and priors

| Option | Prior | Case for | Case against |
|---|---:|---|---|
| A — ACCEPT phase 2 exactly as written | 0.34 | The empty-result path worked, the surface was read-only, a scheduling consumer is named, and a second bounded call is cheap and reversible. | Another arbitrary or empty window adds little information. Optional event-detail reading expands privacy and capability scope, and same-connector comparison is correlated rather than independent verification. |
| B — REVISE phase 2 to a consumer-bound Freebusy-only probe | 0.41 | It preserves adopt-before-invent, tests practical utility, avoids event-title/detail exposure, and keeps the candidate contract clean: occupancy in, planning answer out. | A naturally selected window may still be empty; without a distinct client it cannot establish completeness or accuracy. `primary` remains an alias rather than a durable calendar identity. |
| C — HOLD until identity, scopes, and independent verifier are bound | 0.18 | Unknown identity/scope and busy-pattern sensitivity are real. A hold prevents normalizing an opaque credential path. | The admitted action is a bounded read-only query with no event content. Requiring full identity and independent verification before any second harmless probe may stall useful COTS learning. |
| D — RETIRE the candidate | 0.07 | Measured operator relief and fitness credit are both zero; no ConsumerAck exists. | One successful bounded read already showed a usable normalized Freebusy surface and avoided custom authenticated request plumbing. Retirement after one empty interval is premature. |

## Evidence update and posterior

Direct evidence favors continuing only under narrower scope:

- The connector returned a normalized empty result with separate error fields and no mutation.
- The baseline itself admits that it did not test a known-busy interval, partial errors, secondary/shared calendars, DST boundaries, quota behavior, or independent readback.
- Event-detail comparison would not close the strongest falsifier unless performed by a distinct authorized client against the same source-bound calendar and interval.
- The named consumer needs occupancy windows, not event titles or candidate mining.

Posterior:

| Option | Posterior |
|---|---:|
| B — REVISE to consumer-bound Freebusy-only | **0.63** |
| C — HOLD for identity/verifier | 0.19 |
| A — ACCEPT as written | 0.14 |
| D — RETIRE | 0.04 |

## Correlated-evidence risk

High. The phase-1 call, any optional event-candidate read, Git persistence, and this vote are all on the same ChatGPT-carried provider surface. A second read through the same connector can demonstrate repeatability and utility, but cannot independently establish calendar completeness, OAuth scope, raw API fidelity, or absence of omitted busy blocks. This vote therefore has binding weight zero.

No competing vote on this exact Calendar phase-2 packet was found before persistence. That absence is not consensus.

## Strongest dissent

`HOLD` is defensible: the connector exposes neither the authenticated identity nor the granted scope, and even Freebusy can reveal sensitive occupancy patterns. A named consumer should exist before another private query, and a distinct verifier should be reachable before any adoption claim. The counterweight is that one narrowly bounded, consumer-needed, Freebusy-only query can be run without event content, mutation, operator relay, or adoption credit.

## Opportunity cost

Using the next X13 wake on an arbitrary empty interval or on event-detail comparison would consume the campaign's phase-2 slot without testing the actual scheduling value proposition. It would also blur two separate capabilities—Freebusy occupancy and event-detail retrieval—making later adoption gates harder to reason about.

## Operator-minute burden

- This vote: `0` operator minutes.
- Revised phase-2 experiment: target `0` operator relay minutes by selecting an already existing, source-bound scheduling question.
- Any request for the operator to identify a test event, disclose private calendar details, or manually compare clients invalidates the zero-burden claim and should produce `HOLD` rather than interactive CPR.

## Reversible next experiment

Run exactly one phase-2 query only when a named scheduling or executive-assistant consumer has a real bounded availability question.

Required gates:

1. Freebusy-only. Do not read event candidates, titles, descriptions, attendees, locations, IDs, or conference data to validate this campaign.
2. Use explicit UTC bounds or explicit offsets and bind the private source calendar context. Treat `primary` as an alias, not a durable ID.
3. Prefer a narrow window likely to exercise the busy path, but do not create or modify an event to manufacture one.
4. Preserve per-calendar errors separately from successful calendars. Partial response is not global success.
5. Persist to Git/Slack only a sanitized result class, busy-count/error class, consumer question, latency if exposed, and source pointer. Do not externalize private busy timestamps or calendar identifiers unless independently classified as non-sensitive.
6. Fitness and operator-relief credit remain zero until a source-bound ConsumerAck states that the result changed or shortened an actual planning decision.
7. A same-connector event read is not a verifier and must not be used to inflate confidence.

## Falsifier and stop conditions

This vote falls if a distinct authorized raw Calendar client, using the same source-bound calendar and exact UTC interval, returns a busy interval or per-calendar error omitted by the connector.

Phase 2 should return `HOLD` rather than advance if any of the following is true:

- no named consumer question exists;
- interpreting the answer requires event-detail retrieval;
- the connector collapses per-calendar errors into apparent success;
- the query requires operator relay or disclosure;
- sensitive busy patterns cannot be kept out of Git and Slack;
- identity/scope ambiguity causes a permission or authority conflict.

## Vote

`REVISE`

Proceed only with one consumer-bound, Freebusy-only, privacy-minimized phase-2 micro-use. Remove the optional event-candidate read from this campaign. Do not claim accuracy, completeness, identity, scope, scheduling authority, operator relief, fitness credit, or independent verification.

`SAME_PROVIDER_NONBINDING — binding weight 0.`
