---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_EXTERNAL_SIGNAL_RAW_24H_CROSS_SOURCE_RANK_SEMANTIC_GATE_20260804T102931Z
question_id: EXTERNAL_SIGNAL_MONITOR_TYPED_24H_DELTA_RANK_GATE_001
work_item_id: EXTERNAL_SIGNAL_MONITOR_TYPED_24H_DELTA_RANK_GATE_001
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
wip: 1
seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-04T10:29:31Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: EXTERNAL_SIGNAL_MONITOR_TYPED_24H_DELTA_RANK_GATE_001
verifier: DISTINCT_NONPRODUCER_DATA_SEMANTICS_VERIFIER
expiry_utc: 2026-08-11T10:29:31Z
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERDICT_AND_CONSUMER_ACK
---

# S08 evidence card — raw 24-hour deltas across source lanes are not one rankable quantity

## Self-probe and changed-question selection

- Expected and observed carrier task ID match: `6a526109ba348191b5f23ad3172ad568`.
- Available surfaces used: authenticated GitHub issue/commit/file reads, immutable branch file creation, exact post-write readback, public Slack duplicate search, and current primary provider documentation.
- Unavailable or unused: external-signal monitor checkout, PostgreSQL schema, source credentials, private analytics, payment data, target runtime, task mutation, deployment, merge, publication, outreach, application, purchase, or spend.
- Prior completed lane: `INTERACTION_INPUT_ADAPTERS` at commit `479114fec2153d58393178f9c7096159772a5dd4`.
- Rotated lane: `DISTRIBUTION_AND_BUYER_EVIDENCE`.
- Queue source: `TTaoGaming/hfo-gen-133#5`, created `2026-08-02T18:51:49Z`, says six source lanes exist and a 24-hour delta rank was unavailable until a sufficiently old baseline existed.
- Changed uncertainty: more than 24 hours have now elapsed since that queue statement. The temporal blocker can age out, but the queue does not define whether deltas from visits, stars, discussion scores, downloads, purchases, and charge events are semantically comparable.
- Duplicate probe: no repository commit or public `C0BGNGPJFHU` message matched the exact `raw 24-hour cross-source delta rank` question.

## Bounded uncertainty

Once a baseline is old enough, may the monitor sort all raw 24-hour source deltas into one global fitness rank?

This card addresses only cross-source delta semantics and ranking. It does not establish that any baseline currently exists, execute the monitor, inspect private observations, choose commercial thresholds, or validate demand.

## Exact candidate/version boundary

- Queue candidate: `TTaoGaming/hfo-gen-133#5` — “External signal monitor and PostgreSQL consolidation status — 2026-08-02”.
- Canonical branch: `agent/gen133-bootstrap-20260730`.
- Monitor implementation path and executable commit are not named by issue #5: `IMPLEMENTATION_VERSION_UNKNOWN`.
- Existing source-semantics evidence inputs:
  - Cloudflare attention boundary: `026ab5125813cdcfd26e9d6646e17357722e312c`.
  - GitHub attention boundary: `b5a056098e4dab4bd175bca3b6d0a8f9dbc9cb85`.
  - Hacker News discussion boundary: `6aee032816db5ac3f2077c953391bfef28fa9241`.
  - Reddit discussion boundary: `517d862ccf9d281a36518429f8dd3b8299c33c91`.
  - itch.io aggregate/auth boundary: `204c6c5742290c861d606cbaca877f7f9f8dec9f`.
  - Stripe transaction-event boundary: `f7cc943d13ad02e1f53d8dc86c3168673954a9a0`.

## Dated primary/current evidence

Observed `2026-08-04`:

1. Cloudflare defines a visit as an externally referred or direct page view and a page view as a successful HTML response. One visit may contain multiple page views. These are web-attention units, not transactions.
   - https://developers.cloudflare.com/web-analytics/data-metrics/high-level-metrics/
2. GitHub documents stars as bookmarks that show an approximate level of interest. It also states that `watchers_count` and `stargazers_count` both represent stars, while `subscribers_count` represents notification watchers. These fields are not buyer units.
   - https://docs.github.com/en/rest/activity/starring
   - https://docs.github.com/en/rest/activity/watching?apiVersion=2026-03-10
3. itch.io `profile/games` exposes separate cumulative fields for `views_count`, `downloads_count`, `purchases_count`, and currency-specific earnings. The fields are not interchangeable and require authenticated access to owned/editable projects.
   - https://itch.io/docs/api/serverside
4. Stripe `GET /v1/charges` returns created Charge objects with separate payment, capture, refund, dispute, customer, currency, and live-mode state. A raw object-count delta is not a buyer or net-revenue delta.
   - https://docs.stripe.com/api/charges/list?lang=curl

## Supported claims

- A 24-hour delta is meaningful only after binding the same artifact identity, source, metric name, metric schema/version, unit, collection method, and complete UTC window at both endpoints.
- Same-source, same-metric deltas may support a typed observation such as `PAGE_VIEW_DELTA`, `STAR_DELTA`, `DOWNLOAD_DELTA`, `PURCHASE_DELTA`, or `SUCCESSFUL_TRANSACTION_EVENT_DELTA`.
- Source lanes can be displayed together as a typed evidence vector or tiered dashboard without claiming that one raw unit equals another.
- A consumer may define source-specific thresholds, provided every threshold names the exact metric and preserves `UNKNOWN` for absent, partial, unbound, or non-comparable observations.

## Excluded claims

- `+10` page views, stars, comments, downloads, purchases, and successful charges represent equal fitness increments.
- A larger attention delta outranks a smaller transaction delta.
- Percent change makes heterogeneous metrics comparable; small denominators and zero baselines can dominate the result.
- A missing or rate-limited source is zero.
- Cumulative-counter subtraction is valid across identity changes, schema changes, source resets, visibility changes, refunds, deletions, moderation, or incomplete pagination.
- One global scalar rank establishes demand, buyer intent, product-market fit, or expected income.

## License, terms, and privacy uncertainty

The candidate is an internal ranking rule, not a FOSS dependency. The source lanes are hosted services with separate terms, authentication, retention, and account-authorization boundaries. This run did not inspect effective account terms or permissions and accessed no private analytics or transaction data. Existing per-source cards remain controlling for credential and privacy gates.

## Decision — `REVISE`

Do not implement or consume a raw cross-source 24-hour delta rank.

Retain 24-hour deltas only as typed, source-specific observations. Replace the scalar scoreboard with a tiered evidence vector or explicitly labeled Pareto/lexicographic view that never silently converts attention, discussion, acquisition, and transaction units into one quantity.

## Smallest required amendment

1. Add immutable keys for `artifact_id`, `source_id`, `metric_id`, `metric_schema_version`, `unit`, `window_start_utc`, `window_end_utc`, `collector_version`, and `completeness_state`.
2. Select a baseline only when source, artifact, metric, unit, and schema match exactly; require a documented time tolerance around the target 24-hour interval.
3. Fail closed to `UNKNOWN` or `PARTIAL_UNKNOWN` on missing baseline, pagination uncertainty, credential failure, identity mismatch, source reset, or schema drift.
4. Preserve separate evidence classes at minimum: `ATTENTION`, `DISCUSSION`, `ACQUISITION`, and `TRANSACTION`. Do not add their raw deltas.
5. Allow thresholds only against one exact typed metric or an explicitly versioned rule. Persist the rule digest and all component observations so the result is replayable.
6. If a single triage order is operationally required, use an explicit lexicographic policy chosen by the consumer, such as transaction evidence before acquisition before attention, and label it `POLICY_ORDER`, not empirical fitness.
7. Keep raw counts, percentage changes, and any normalized values visible separately. Never substitute a normalized score for the underlying evidence.

## Strongest objection

The operator has limited attention, so one sortable number is cheaper than reading a vector of six sources.

**Response:** a single unvalidated number is cheap only because it hides the decision rule. A versioned lexicographic or tiered view preserves low cognitive load while making the policy explicit and reversible. It prevents a burst of low-value page views or comments from outranking one purchase merely because the raw count is larger.

## Falsifier

This `REVISE` may narrow to `ADMIT` for one explicitly versioned scoring rule only if a distinct verifier receives:

- a pre-registered target outcome such as subsequent qualified reply, purchase, or net collected revenue;
- a labeled historical dataset using the same artifact class and exact source definitions;
- held-out validation showing the proposed cross-source score improves decisions over typed baselines;
- calibration, drift, missingness, manipulation, and small-denominator tests; and
- a consumer-owned cost function showing that the scalar ordering is worth its false-positive and false-negative errors.

Even then, admission applies only to that rule/version and population. It does not validate generic raw-delta ranking.

## Verifier and consumer

- Verifier: `DISTINCT_NONPRODUCER_DATA_SEMANTICS_VERIFIER`, preferably S04 for structural replay plus S09 for decision-policy review.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_TYPED_24H_DELTA_RANK_GATE_001`.
- Required ConsumerAck: exact card commit/blob, implementation commit, schema/rule digest, typed metric list, baseline tolerance, missingness policy, and explicit rejection of generic cross-source raw ranking.

## Cost and operator burden

- This research run: `$0` direct spend; `0` operator minutes.
- Producer schema/ranking revision: `30–60` minutes.
- Deterministic fixture and replay tests: `30–60` minutes.
- Distinct verifier review: `20–40` minutes.
- Operator burden: `0–10` minutes only if a lexicographic triage policy requires an explicit business-priority choice.

## Honest flaw

The monitor implementation and observation rows were not available to this run, so no claim is made that the current code actually computes a global scalar rank or that a complete 24-hour baseline now exists. The card closes the semantic boundary before baseline age is mistaken for comparability.

## Effect receipt

No monitor execution, source request, credential or private-data access, threshold mutation, task mutation, account or terms action, outreach, application, purchase, send, spend, deployment, merge, publication, or demand claim occurred.
