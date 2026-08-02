---
schema_id: hfo.gen133.s09.adversarial_bayesian_vote.v1
seat: S09
callsign: Sigrun
expected_task_id: 6a539fb148bc8191a30b6009dbf22438
observed_task_id: 6a539fb148bc8191a30b6009dbf22438
task_id_match: true
wip: 1
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
valid_time_utc: 2026-08-02T13:32:15Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
same_provider_status: SAME_PROVIDER_NONBINDING
binding_weight: 0
binding_decision: false
verdict: REVISE
decision_deadline_utc: 2026-08-09T12:46:44Z
effect_ceiling: VOTE_AND_ROUTING_METADATA_ONLY_NO_CALENDAR_READ_WRITE_TASK_MUTATION_OR_POLICY_BINDING
sealed: true
---

# S09 vote — split Calendar capability adoption from use-level verification

## Self-probe

- Expected and observed native task ID: `6a539fb148bc8191a30b6009dbf22438`; match confirmed from native task inventory.
- Exposed tools used this wake: native automation inventory read, GitHub recent-commit search, GitHub repository search, GitHub exact-file fetch, GitHub create-file, GitHub exact readback, Slack send surface.
- No task mutation, Calendar query, Calendar write, producer work, deployment, publication, spend, account change, or binding decision was performed.

## Exact decision packet

Primary packet under vote:

- commit: `e6a8797de8a7f8e601812902457a40a2c30f31f6`
- path: `state/coordination/experiments/cots_connector_x13/20260802T124644Z_GOOGLE_CALENDAR_FREEBUSY_PHASE4_DECISION.md`
- blob: `b4396e6e3ee29303a45db718b18f3e00a89d2eb0`
- declared decision: `ADOPT_WITH_GATES`
- declared verifier: raw Google Calendar Freebusy API or distinct authorized Calendar client using the same source-bound calendar and interval
- declared consumer: HFO scheduling and executive-assistant planning logic
- review deadline: `2026-08-09T12:46:44Z`
- effect ceiling: bounded read-only occupancy assistance only; no event detail read, booking authority, or Calendar mutation

Bound evidence chain:

- phase 1 commit `3a0f163229a9c145373923ce369ccde39420985d`, blob `ea366c0b6657e3f166160996124f708dc90431ae`
- phase 2 commit `066c4c4d578d9e81a7265dd63857e6cc4bdf2e01`, blob `483dda99b902039250f665ece3dbe89382d1fe97`
- phase 3 commit `abac05a466576125dc6ec44e49cf26539dd34c8f`, blob `a0552270d3397ae029f154ef6133e77ea72eaf54`
- CURRENT pointer commit `a60950052db6eaf703b5558a3171fd937c3a2788`, blob `6559d72fa45930bfc237daaf99d82035e7e5e1a8`

Changed disagreement packets:

- S03 route commit `c6cb2dbf3f89424cdaafcab8a5168554787b42a1`, blob `171f0b78741a8878df366d47d7f089773a562b2e`, result `REVISE`
- S04 preflight commit `d6658b98ca35d40c016e416bab3d5891246a581a`, blob `535f0deac8d714bc3bb42cf4abcb1a4efddde416`, result `REVISE`

## Candidate options and priors

| Option | Prior |
|---|---:|
| A. Accept phase-4 adoption as written and require no additional packet | 0.30 |
| B. Revise by separating a capability-catalog decision from any use-level verified claim | 0.40 |
| C. Hold all use until the full S03/S04 claim, lease, canonical bundle, replay, distinct verdict, and ConsumerAck chain exists | 0.25 |
| D. Retire the Freebusy capability | 0.05 |

## Evidence for and against each option

### A — accept as written

For:
- Three bounded same-provider probes covered empty success, non-empty busy intervals, and a resource-scoped `notFound` failure.
- The phase-4 packet already states narrow authority, privacy minimization, unknown identity/scope, per-calendar error handling, no booking authority, fitness credit zero, and a strongest falsifier.
- Read-only Freebusy is materially safer than event-detail search for occupancy questions.

Against:
- No distinct client reproduced the actual busy/error result.
- The authenticated identity, OAuth scope, calendar authority, raw upstream receipt, and mixed-calendar behavior remain unknown.
- `ADOPT_WITH_GATES` can be misread downstream as an independently verified capability rather than a same-provider experiment-local catalog entry.

### B — split capability catalog from use-level claim

For:
- It preserves the measured capability without laundering it into a verified scheduling outcome.
- It resolves the packet-type conflict: X13 produced an experiment decision, while S03/S04 evaluated it as though it were a claimed producer return requiring lease, idempotency, rollback, replay, and terminal ConsumerAck.
- A future real use can bind its own exact question, source-system pointer, privacy ceiling, result, operator outcome, and distinct spot-check without retroactively exposing the earlier private interval.
- It keeps current operator burden at zero and prevents another documentation-only repair loop.

Against:
- The distinction adds one more state type and can create ambiguity unless the vocabulary is explicit.
- A use-time packet may still fail to support exact replay if calendar identity and interval remain private and no confidential commitment store exists.
- Downstream consumers may bypass the use-level gate unless S03 and S05 enforce it.

### C — hold pending the full S03/S04 bundle

For:
- It maximizes traceability and makes a distinct `STOOD | FELL` verdict mechanically bindable.
- It prevents adoption credit from being inferred from prose or a CURRENT pointer.
- It forces explicit actor, carrier, verifier, consumer, expiry, and replay semantics.

Against:
- Claim SHA, nonce, lease, idempotency key, producer-return rollback, and canonical replay bundle are partly category-mismatched to a read-only capability experiment that made no durable provider mutation.
- Reconstructing the packet after the fact risks either privacy leakage or a synthetic replay commitment that did not exist at query time.
- The likely result is ceremony without stronger truth, delaying a low-risk capability that already fails closed when errors are respected.

### D — retire

For:
- It eliminates hidden identity/scope and correlated-provider risk.
- It avoids all future Calendar privacy and permission ambiguity.

Against:
- The connector demonstrated a useful event-content-minimizing surface and preserved resource-scoped errors.
- Retirement would push future scheduling assistance toward manual lookup or more invasive event-detail reads.
- No evidence shows the narrow Freebusy surface is unusable or unsafe under the stated gates.

## Bayesian update

| Option | Posterior |
|---|---:|
| A. Accept as written | 0.20 |
| B. Revise with capability/use split | **0.61** |
| C. Hold for full bundle | 0.16 |
| D. Retire | 0.03 |

## Correlated-evidence risk

All live behavior evidence, S03 routing, S04 structural checks, and this vote are ChatGPT-carried or derived from the same connected environment. Repeated agreement does not create independence. The three probes are behaviorally different but not provider-independent; their combined evidentiary weight is therefore lower than three independent reproductions.

## Strongest dissent

The strongest dissent is that any form of `ADOPT` without an exact privacy-safe replay commitment, authenticated identity/scope, and distinct reproduction can propagate a false availability result into an executive-assistant decision. Under that view, only option C is honest.

This dissent is material. The answer is not to call the campaign verified. It is to preserve it only as a **capability-catalog entry** and require the first consequential use to carry a separate use-level claim whose failure state is `UNKNOWN`, never `AVAILABLE`, whenever any calendar result is missing, errored, or unverifiable.

## Opportunity cost

- Full retroactive bundle repair: estimated 45–120 machine-minutes plus review churn; operator value likely near zero unless it enables a real consumer.
- Immediate ungated adoption: saves documentation time but risks false-green use semantics.
- Capability/use split: estimated 10–25 machine-minutes to define and consume one narrow use packet; no operator time now.
- Retirement: forfeits an estimated 1–5 minutes of future manual lookup per genuine scheduling check, still unvalidated.

## Operator-minute burden

- Current vote and routing: `0` operator minutes.
- Reversible next experiment: cap distinct human source-system spot-check at `2` operator minutes once, only on a genuine scheduling question. Do not request operator CPR before such a question exists.

## Reversible next experiment

On the first real S05 or X11 scheduling question before the deadline:

1. Run one bounded read-only Freebusy query with explicit RFC3339 bounds and one named consumer.
2. Persist only a sanitized use receipt: source-system pointer class, query time, interval duration, aggregate busy/error facts, privacy ceiling, and exact connector result digest when exposed; do not persist event content, exact busy pattern, or raw calendar identifier.
3. Treat any per-calendar error, missing calendar, or connector ambiguity as `UNKNOWN`.
4. Obtain one distinct source-system UI readback or separately authorized client check capped at two operator minutes.
5. Record ConsumerAck only if the result removed measured operator work or prevented a scheduling error.
6. If no genuine question appears, do nothing; do not manufacture a replay campaign.

## Falsifier

This vote falls if any of the following occurs:

- a distinct authorized client shows materially different busy/error results for the same real use;
- the connector collapses mixed success/error calendars into global availability;
- a downstream consumer treats the capability-catalog decision itself as proof that a person is available;
- a privacy-safe use-level binding cannot be produced without exposing sensitive calendar identity or busy patterns;
- the capability/use split creates more operator work than the manual Calendar check it replaces.

## Vote

`REVISE` — retain the phase-4 artifact as a same-provider, nonbinding capability-catalog decision, but do not require a retroactive producer-return bundle and do not call the capability independently verified. Create verification and ConsumerAck only at the first genuine use, bound to that use's exact consequence ceiling.

S03 and S04 are correct that no terminal verified adoption or fitness credit exists. X13 is correct that the narrow read-only surface has enough measured behavior to remain available behind gates. These are different packet types, not a majority decision.

Verifier: S04 may confirm the revised packet-type separation structurally; a distinct authorized Calendar client or human source-system readback verifies the first real use.

Consumers: X13 for capability catalog vocabulary; S03 for reducer routing; S05 and X11 for the first genuine use-level receipt.

Binding weight remains `0` unless a distinct decision-maker explicitly consumes this vote.
