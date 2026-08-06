---
schema_id: hfo.gen133.s08.research_evidence_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
lane: agent-runtime/COTS capabilities
question: Does X13 phase 4 have enough evidence to call Slack public search adopted, or only to retain an unconsumed catalog observation and retire the active experiment?
verdict: REVISE
verdict_detail: RETAIN_AS_UNCONSUMED_CATALOG_OBSERVATION_CLOSE_ACTIVE_CAMPAIGN_DO_NOT_LABEL_OPERATIONALLY_ADOPTED
candidate: Slack.slack_search_public
candidate_version: NOT_EXPOSED
schema_observed_utc: 2026-08-06T16:28:00Z
queue_snapshot:
  experiment_id: X13_SLACK_SEARCH_PUBLIC_READONLY_010
  current_version: 139
  current_blob_sha1: 2329ec7f1edd441e18433ba761e46736f6ab115a
  campaign_wake: 3_of_4
  phase_4_status: PENDING
  provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
  operational_consumer: NOT_ASSIGNED
  consumer_ack: NOT_OBSERVED
  operator_minutes_removed_measured: 0
  adoption_credit: 0
  fitness_credit: 0
self_probe:
  identity: S08_RESEARCH_AND_CANDIDATE_SCOUT
  task_identity_basis: WAKE_CONTRACT_ONLY
  observed_tools:
    - GITHUB_READ_WRITE
    - SLACK_MESSAGE_POST
    - WEB_AVAILABLE_NOT_NEEDED
  task_or_automation_mutation: NONE
license_status: CONNECTOR_IMPLEMENTATION_REPOSITORY_VERSION_AND_LICENSE_NOT_EXPOSED
terms_status: SLACK_PROVIDER_TERMS_AND_SCOPE_APPLY_BUT_CONNECTOR_TO_PROVIDER_METHOD_TOKEN_CLASS_EFFECTIVE_SCOPE_AND_WORKSPACE_BINDING_REMAIN_UNKNOWN
paid_cost_usd_observed_this_run: 0_NO_CHARGE_SURFACED
operator_minutes_this_run: 0
future_use_estimate: 1_TO_3_AGENT_MINUTES_PER_BOUNDED_HUMAN_REVIEWED_LOOKUP_OPERATOR_SAVINGS_UNMEASURED
verification_estimate: 15_TO_30_VERIFIER_MINUTES_PLUS_A_NAMED_WORKITEM_AND_MEASURED_OUTCOME
consumer: X13_SLACK_SEARCH_PUBLIC_READONLY_010_PHASE4_DECISION
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
verifier: S03_REDUCER_PLUS_S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_SAME_PRINCIPAL_RAW_SLACK_WITNESS_IF_OPERATIONAL_ADOPTION_IS_LATER_REQUESTED
expiry_utc: 2026-08-13T16:28:00Z
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMERACK
recorded_time_utc: 2026-08-06T16:28:00Z
---

# S08 evidence card — X13 Slack phase-4 adoption boundary

## Bounded finding

The campaign supports retaining `Slack.slack_search_public` as a **catalog observation for bounded, human-reviewed public discovery**. It does not support the stronger label `ADOPTED`, even with gates, because no operational WorkItem or consumer is assigned, no ConsumerAck exists, and measured operator minutes removed remain zero.

Phase 1 observed one bounded nonempty public-channel search with three truncated snippets and a continuation cursor. Phase 2 repeated the same normalized three-result digest and confirmed one known public message only after widening a direct-read time window. Phase 3 observed a synthetic nonmatch empty-success shape. All three phases explicitly exclude completeness, durable absence, effective identity and scope, raw-provider parity, stable message keys, rate-limit behavior, and measured operational value.

The phase-4 decision should therefore distinguish **retention of evidence** from **adoption of a capability**:

```text
CATALOG_OBSERVATION_RETAINED=true
ACTIVE_EXPERIMENT_CLOSE=true
OPERATIONAL_ADOPTION=false
ADOPTION_CREDIT=0
FITNESS_CREDIT=0
REOPEN_ONLY_ON_NAMED_WORKITEM_CONSUMPTION=true
```

## Supported claims

- The connector produced bounded public-search nonempty and empty-success responses without Slack mutation.
- One identical near-immediate query replay yielded the same locally normalized three-result digest.
- A widened bounded direct-channel read confirmed one known public message.
- The capability is worth preserving in a COTS catalog as a discovery option with explicit gates.

## Excluded claims

- That catalog inventory is a WorkItem consumer or ConsumerAck.
- That the connector saves operator time, produces revenue, improves a workflow, or is reliable enough for unattended automation.
- Exact provider method, connector version, implementation license, authenticated principal, token class, effective scope, workspace binding, quota debit, retry behavior, stable ordering, completeness, authoritative absence, or raw-provider parity.
- Permission for private-channel or DM search, persistent content retention, high-rate polling, or consequential negative claims.

## Required revision

Close phase 4 as `RETAIN_CATALOG_OBSERVATION_WITH_GATES / NOT_OPERATIONALLY_ADOPTED`. Do not award adoption or fitness credit. Do not schedule more capability probes. Reopen only when a named WorkItem claims this exact surface, defines a bounded public-search use, records a privacy-safe request/response digest, measures an outcome or operator minutes removed, obtains distinct verification appropriate to consequence, and records explicit ConsumerAck.

## Strongest objection

A proven, no-mutation read surface can reasonably be called “adopted into the catalog.” That wording is administratively convenient, but it collapses inventory retention into operational adoption and rewards capability accumulation without consumption. The safer label is `CATALOG_OBSERVATION_RETAINED`; adoption remains false until a WorkItem uses it.

## Falsifier

Move toward `ADMIT` only when a named WorkItem consumes the exact candidate and card digest, the bounded lookup produces a recorded useful outcome or measured operator-minute reduction, a verifier confirms the required scope and result semantics for that consequence level, and the named consumer explicitly acknowledges the stood result. Retire the catalog entry entirely if it expires without a plausible consumer and a later catalog-pruning policy rejects unconsumed observations.

## Dated sources

- X13 CURRENT v139, recorded 2026-08-06, exact blob `2329ec7f1edd441e18433ba761e46736f6ab115a`: https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/state/coordination/experiments/cots_connector_x13/CURRENT.md
- Phase 1 accepted with gates, recorded 2026-08-06, blob `c11d98d36fa36b39a8953615e205113504a3bdf4`: https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/state/coordination/experiments/cots_connector_x13/20260806T134804Z_SLACK_PUBLIC_SEARCH_PHASE1_ACCEPTED_WITH_GATES.md
- Phase 2 accepted with gates, recorded 2026-08-06, blob `eb0fc4775ca963b391ba3916ceaf0017715adde9`: https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/state/coordination/experiments/cots_connector_x13/20260806T144951Z_SLACK_PUBLIC_SEARCH_PHASE2_ACCEPTED_WITH_GATES.md
- Phase 3 accepted with gates, recorded 2026-08-06, blob `cc091815964bb87dfe8d672899b13939e56cfaa2`: https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/state/coordination/experiments/cots_connector_x13/20260806T154839Z_SLACK_PUBLIC_SEARCH_PHASE3_ACCEPTED_WITH_GATES.md

## Honest flaw

This card evaluates adoption semantics from durable campaign receipts only. It performs no additional Slack candidate call and cannot establish hidden connector behavior, raw-provider parity, principal scope, cost, or actual consumer value. Its recommendation is a no-fake-green phase-4 classification boundary, not a provider-quality verdict.
