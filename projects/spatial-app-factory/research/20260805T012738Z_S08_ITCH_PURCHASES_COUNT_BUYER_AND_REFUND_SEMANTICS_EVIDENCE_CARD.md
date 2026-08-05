---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_ITCH_PURCHASES_COUNT_BUYER_AND_REFUND_SEMANTICS_20260805T012738Z
question_id: EXTERNAL_SIGNAL_MONITOR_ITCH_PURCHASE_COUNTER_LIFECYCLE_GATE_001
work_item_id: EXTERNAL_SIGNAL_MONITOR_ITCH_PURCHASE_COUNTER_LIFECYCLE_GATE_001
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
wip: 1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-05T01:27:38Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: EXTERNAL_SIGNAL_MONITOR_ITCH_PURCHASE_COUNTER_LIFECYCLE_GATE_001
verifier: DISTINCT_ITCH_SYNTHETIC_PURCHASE_LIFECYCLE_VERIFIER
expiry_utc: 2026-08-12T01:27:38Z
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERDICT_AND_CONSUMER_ACK
---

# REVISE — itch.io `purchases_count` is not a stood unique-buyer or net-revenue metric

## Self-probe and changed question

- Provider task identity matched expected task ID `6a526109ba348191b5f23ad3172ad568`.
- Available and used: authenticated GitHub issue/file/commit search, exact branch write and readback, current official itch.io documentation, and authenticated Slack pointer after Git readback.
- Unavailable or unused: itch.io account or API credential, project dashboard, purchase records, buyer identifiers, payment processor, monitor checkout/runtime, shell, synthetic purchase fixture, task mutation, deployment, publication, purchase, outreach, or spend.
- Lane rotation followed the explicit order: the preceding accepted S08 card was `INTERACTION_INPUT_ADAPTERS`; this wake selected `DISTRIBUTION_AND_BUYER_EVIDENCE`.
- Queue binding: open issue `TTaoGaming/hfo-gen-133#5` defines an itch.io monitor lane and proposes purchase observations. Prior card `20260804T002855Z_S08_ITCHIO_AGGREGATE_METRICS_AUTH_AND_BUYER_SIGNAL_BOUNDARY_EVIDENCE_CARD.md` admitted only aggregate authenticated collection and explicitly left refund semantics open. The later typed-delta card requires every source metric to have a precise unit before ranking or thresholds.
- Duplicate probe found no Gen-133 card resolving whether exact field `profile/games[].purchases_count` means unique buyers, retained owners, completed purchase events net of reversals, or net collected revenue.

## Bounded uncertainty

**Question:** May the external-signal monitor classify a delta in itch.io `profile/games[].purchases_count` as the same number of new paid buyers or as net realized sales?

## Exact candidate and version boundary

- Candidate system: issue `TTaoGaming/hfo-gen-133#5`, itch.io source lane.
- Provider interface: modern itch.io server-side API endpoint `GET https://api.itch.io/profile/games`.
- Exact field: `games[].purchases_count`.
- API/documentation version: not exposed by the current reference; schema lifecycle is unversioned.
- Exact monitor implementation commit/path: `UNKNOWN` because issue #5 does not bind executable bytes.

## Dated primary evidence — observed 2026-08-05

1. itch.io **Server-side API reference** documents authenticated `profile/games` and shows separate cumulative fields `purchases_count`, `downloads_count`, and currency-specific `earnings`. It does not define `purchases_count` uniqueness, quantity treatment, bundle attribution, donation inclusion, refund decrement, chargeback decrement, or reset behavior. The per-person `/games/GAME_ID/purchases` route instead requires an email or user ID, returns only successfully completed purchases, and exposes distinct purchase IDs, quantity, status, purchase type, and bundle-associated game IDs.
   - https://itch.io/docs/api/serverside
2. itch.io **Accepting Payments and Getting Paid** states that refunds and chargebacks are revenue-adjusting events and may reduce pending or future payouts after the original payment. A completed purchase and realized net proceeds are therefore different lifecycle states.
   - https://itch.io/docs/creators/payments
3. itch.io **Download keys** states that ownership/download keys can arise from direct payment, a bundle purchase, owner-generated keys, or free claims; large bundles may grant ownership before a project key is claimed. Key/owner counts and purchase counts are therefore not interchangeable.
   - https://itch.io/docs/creators/download-keys
   - https://itch.io/docs/creators/bundles
4. itch.io **How buying works** states that successful purchases create transaction-specific download pages and may be made without an itch.io account, with the purchase associated to an email address. One account identifier is not a required one-to-one buyer identity.
   - https://itch.io/docs/creators/how-buying-works

## Supported claims

- `purchases_count` is a provider-reported project-level aggregate counter distinct from downloads and earnings.
- Under the same exact project identity, stable schema, complete reads, and monotonic observations, a positive delta may be retained as typed evidence `ITCH_PURCHASE_COUNTER_DELTA`.
- Purchase-event evidence belongs above attention/download evidence, but it does not by itself prove unique humans, retained owners, satisfaction, product-market fit, or net cash collected.
- Refunds and chargebacks can occur after successful payment and alter payout economics; the public aggregate field documentation does not state how or whether those events revise `purchases_count`.
- Bundle purchases, quantity, gifts, pay-what-you-want payments, donations, and accountless checkout prevent an undocumented one-counter-unit equals one unique-buyer assumption.

## Excluded claims

- `purchases_count == unique paid buyers`.
- `delta(purchases_count) == new customer count`.
- `purchases_count` is net of refunds, chargebacks, disputes, or revoked access.
- One project counter increment equals one retained owner or one directly attributable standalone sale.
- The separate `earnings` amount is net collected or available payout without binding fees, taxes, refunds, chargebacks, currency, and payout state.
- Missing, decreasing, reset, unauthorized, partial, or schema-drifted observations are zero.
- No current HFO artifact has an itch.io purchase, buyer, revenue, or bound credential.

## Decision — `REVISE`

Keep the field, but rename and type it narrowly:

`ITCH_PROJECT_PURCHASE_COUNTER` / `ITCH_PURCHASE_COUNTER_DELTA`

Do not expose it as `buyers`, `customers`, `owners`, `paid_users`, `sales`, or `net_revenue`.

### Smallest required amendment

1. Persist exact `game_id`, normalized project URL, observation time, collector version, raw field name, raw integer, authorization state, and completeness state.
2. Add semantic flags fixed to `unique_buyer_semantics=UNKNOWN`, `refund_decrement_semantics=UNKNOWN`, `chargeback_decrement_semantics=UNKNOWN`, `bundle_attribution_semantics=UNKNOWN`, and `net_revenue_semantics=FALSE`.
3. Compute deltas only across exact game/source/schema identity. Negative deltas, field disappearance, project recreation, authorization failure, or counter reset become `UNKNOWN_RECONCILIATION_REQUIRED`, not negative demand.
4. Permit a threshold only as `PURCHASE_COUNTER_INCREASE_OBSERVED`; keep it distinct from `UNIQUE_BUYER_INCREASE`, `NET_REVENUE_INCREASE`, and `RETAINED_OWNER_INCREASE`.
5. Do not call per-buyer purchase endpoints or persist email, user ID, download key, transaction ID, or other buyer-identifiable fields for this aggregate monitor.
6. Bind any future net-revenue decision to a separate currency- and adjustment-aware ledger or payout surface, not this counter.

## License, terms, and privacy uncertainty

- This is a hosted API/metric contract, not a FOSS license question.
- The current API docs expose no versioned schema guarantee for `purchases_count`.
- No effective account terms, credential scope, project authorization, rate limits, or retention policy were assayed.
- itch.io documentation restricts sharing buyer-identifiable data; this card authorizes no buyer-level read and requires aggregate-only minimization.
- Publication rights, payment setup, account creation, terms acceptance, and merchant-of-record obligations remain separate and unauthorized.

## Strongest objection

For operator triage, any positive purchase counter delta is probably enough to say “someone paid,” so the exact lifecycle semantics may be unnecessary.

**Response:** it is useful transaction evidence and should be admitted as such. The correction is the label and downstream boundary: one provider counter increment is not safely promotable to one unique buyer or net realized sale, especially when reversals and bundle attribution are undocumented.

## Falsifier

This verdict may narrow only if current official versioned documentation or an authorized synthetic test project proves, for the exact API version:

- whether repeated purchases by one person increment once or repeatedly;
- quantity, gift, donation, standalone, and bundle attribution behavior;
- refund and chargeback effects on the counter;
- project recreation/reset behavior; and
- reconciliation against a separate adjustment-aware revenue ledger.

The fixture must contain no real buyer data and must be independently replayed.

## Verifier, consumer, cost, and expiry

- **Verifier:** `DISTINCT_ITCH_SYNTHETIC_PURCHASE_LIFECYCLE_VERIFIER`.
- **Consumer:** `EXTERNAL_SIGNAL_MONITOR_ITCH_PURCHASE_COUNTER_LIFECYCLE_GATE_001`, then the exact issue #5 monitor WorkItem if one is admitted.
- Producer schema/label amendment: `20–40 minutes`.
- Deterministic counter-reset and typed-missingness fixtures: `20–40 minutes`.
- Optional authorized synthetic purchase/refund/bundle assay: `45–90 minutes`, excluding account creation, terms acceptance, payment, and spend.
- Direct monetary cost this run: `$0`; operator minutes requested: `0`.
- Expiry: `2026-08-12T01:27:38Z`, or immediately on API/schema/terms change or exact monitor implementation binding.
- Fitness: `0` until exact WorkItem consumption, distinct verdict, and ConsumerAck.

No itch.io request, credential access, private-data use, purchase, refund, account action, terms acceptance, task mutation, implementation, deployment, merge, publication, outreach, send, or spend occurred.
