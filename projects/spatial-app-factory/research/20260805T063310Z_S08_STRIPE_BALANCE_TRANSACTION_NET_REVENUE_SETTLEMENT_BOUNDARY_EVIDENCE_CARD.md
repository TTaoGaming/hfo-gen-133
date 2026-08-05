---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
question_id: EXTERNAL_SIGNAL_MONITOR_STRIPE_BALANCE_ACTIVITY_NET_SEMANTICS_GATE_001
decision: REVISE
valid_time_utc: 2026-08-05T06:33:10Z
expiry_utc: 2026-08-12T06:33:10Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: EXTERNAL_SIGNAL_MONITOR_STRIPE_BALANCE_ACTIVITY_NET_SEMANTICS_GATE_001
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
---

# S08 evidence card — Stripe BalanceTransaction `net` is Stripe-balance movement, not net revenue or bank-settled cash

## Self-probe and changed bounded question

- Native task inventory confirms the expected carrier ID `6a526109ba348191b5f23ad3172ad568`; GitHub, current public web research, and Slack pointer surfaces are available.
- The prior wake investigated synthetic pointer identity. The explicit next lane is distribution and buyer evidence.
- This question is distinct from the prior Stripe Charge-count and Checkout-webhook cards: **may an external-signal monitor treat BalanceTransaction `net`, `status=available`, or `available_on` as net revenue or bank-settled cash?**
- No Stripe request, account, credential, webhook, Dashboard report, or private financial/customer data was accessed.

## Exact candidate

- Provider/API: Stripe API v1.
- Endpoint/object: `GET /v1/balance_transactions`; `BalanceTransaction`.
- Fields under review: `amount`, `fee`, `net`, `status`, `available_on`, `reporting_category`, `type`, `source`, and currency.
- Exact account API version: `UNKNOWN_UNTIL_RESPONSE_HEADER_OR_ACCOUNT_READBACK`. Public version pages observed in Gen-133 have disagreed, so no alleged platform-current version is accepted as the effective account version.

## Primary/current sources observed 2026-08-05

1. Stripe, **Balance Transaction object** — https://docs.stripe.com/api/balance_transactions/object
   - `net` is the net impact to a Stripe balance, calculated as `amount - fee`.
   - `status` is `available` or `pending`; `available_on` describes when net funds become available in the Stripe balance.
   - The object type inventory includes charges/payments, refunds, disputes, adjustments, payouts, transfers, fees, top-ups, reserves, and other non-revenue movements.
2. Stripe, **List all balance transactions** — https://docs.stripe.com/api/balance_transactions/list
   - The endpoint lists transactions contributing to an account balance, newest first, with cursor pagination and a page limit up to 100.
   - Documented time filtering is by object creation time; no `available_on` or status filter is documented.
3. Stripe, **Balance report** — https://docs.stripe.com/reports/balance
   - Stripe separates balance activity from payouts, and separately exposes available, pending, and reserved balances.
   - Balance activity includes charges, refunds, disputes, adjustments, and fees; bank payouts are a separate section.
4. Stripe, **Reporting categories** — https://docs.stripe.com/reports/reporting-categories
   - Stripe recommends `reporting_category` rather than raw `type` for finance-oriented classification.
5. Stripe, **Balance transaction types** — https://docs.stripe.com/reports/balance-transaction-types
   - Delayed and failed payments, refunds, refund failures, disputes, reversals, reserves, fees, top-ups, transfers, and payouts can create separate balance transactions.
6. Stripe, **Payout reconciliation** — https://docs.stripe.com/payouts/reconciliation
   - A payout moves available Stripe balance toward a bank account and may contain multiple underlying transactions.
   - Manual payouts are not automatically linked by Stripe to the underlying transactions and require separate reconciliation.

## Supported claims

- `net` is a valid transaction-level measure of **Stripe-balance impact after that transaction's fee**.
- `status=available` means funds are available **inside the Stripe balance**; it does not prove that a bank received or settled the cash.
- `reporting_category` is required for credible aggregation. Summing all transaction `net` values without category exclusions can mix customer payments with payouts, transfers, top-ups, reserves, adjustments, and other non-revenue flows.
- A bank-cash claim requires payout status and reconciliation. An accounting-revenue claim requires a separate revenue-recognition policy and source reconciliation.
- Because the list API filters by `created` rather than `available_on`, a created-time-only incremental reader can miss an older pending transaction later becoming available unless it re-reads and reconciles stored state.
- Append-only observations must distinguish transaction creation from `pending -> available` state change and deduplicate by an account-bound stable transaction identity or privacy-safe keyed digest.

## Excluded claims

- No claim that any HFO artifact has a Stripe account, balance, customer, buyer, charge, revenue, payout, margin, or settled cash.
- No claim that `net`, `available`, `available_on`, Balance Summary, or payout status establishes unique buyers, demand, conversion, retention, recognized revenue, profit, or bank-statement settlement by itself.
- No claim that all Stripe account, Connect, organization, multi-currency, reserve, tax, or manual-payout configurations share one reconciliation rule.
- No claim that an empty or incomplete API window means zero activity.

## Required revision

Use these exact semantic classes:

```text
STRIPE_BALANCE_ACTIVITY_NET
STRIPE_AVAILABLE_BALANCE_ACTIVITY_NET
BANK_PAYOUT_SETTLED_CASH=UNKNOWN_UNTIL_PAYOUT_RECONCILIATION
RECOGNIZED_REVENUE=UNKNOWN_UNTIL_ACCOUNTING_POLICY_AND_SOURCE_RECONCILIATION
UNIQUE_BUYERS=UNKNOWN
```

The monitor must:

1. bind one Stripe account context, effective API version, UTC query bounds, currency, cursor completeness, and classification-rule digest;
2. classify by `reporting_category`, keeping charges, refunds, disputes, fees, adjustments, reserves, transfers, top-ups, and payouts separate;
3. never sum all `net` values as revenue or count all available transactions as sales;
4. keep currency buckets separate and avoid cross-currency totals without an explicit exchange-rate policy;
5. use overlap/state reconciliation so transactions created earlier can transition from pending to available without double counting;
6. label cursor, version, account, state-transition, payout-linkage, or retention uncertainty as `UNKNOWN | PARTIAL`, never zero or success;
7. persist aggregate-only output and exclude customer, source-object, description, metadata, and bank details from Git, Slack, prompts, traces, and general logs;
8. require payout reconciliation before any bank-cash claim and separate accounting review before any recognized-revenue claim.

## License, terms, and privacy uncertainty

- No third-party software-license conclusion is required to describe the public API contract.
- Stripe service terms, merchant/account authorization, effective restricted-key scope, Connect or organization boundaries, reporting retention, tax/accounting obligations, and provider request cost are not established by public documentation alone.
- Balance transactions are private financial data. Any later read requires a separately authorized WorkItem, least-privilege credential handling, account binding, and aggregate-only retention.

## Cost and operator-minute estimate

- This pass: `$0` spend, `0` operator minutes, `0` Stripe requests.
- Producer revision: `25–50 minutes`.
- Deterministic sandbox/replay verifier: `45–90 minutes`.
- Operator review of an existing approved account/key/report path: `10–20 minutes` under a separate WorkItem.
- Provider and account-specific cost: `UNKNOWN`.

## Strongest objection

`net` already subtracts Stripe fees, while refunds and disputes appear as negative balance activity, so summing it seems close enough to economic truth.

**Response:** it can be useful as **Stripe balance activity**, but the same ledger also contains payouts, transfers, top-ups, reserves, adjustments, and timing transitions. `available` is still an in-Stripe state, not proof of bank settlement, recognized revenue, or profit.

## Falsifier

Change toward `ADMIT` only if a distinct verifier runs an authorized exact implementation against a deterministic Stripe sandbox fixture and separately approved report-schema readback covering charge, fee, refund, dispute, reversal, delayed-payment failure, pending-to-available transition, payout, payout failure, reserve, transfer/top-up, pagination, currency, account, and API-version boundaries. The implementation must match Stripe Balance and payout reconciliation under its stated labels, remain idempotent, and prove that prohibited private fields never enter shared storage or traces.

Change to `RETIRE` if the chosen runtime cannot bind account/version, reconcile pending-to-available transitions and payouts, complete pagination, or prevent raw financial payload leakage.

## Verifier, consumer, expiry, and decision

- Verifier: `DISTINCT_STRIPE_SANDBOX_BALANCE_AND_PAYOUT_RECONCILIATION_VERIFIER`.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_STRIPE_BALANCE_ACTIVITY_NET_SEMANTICS_GATE_001`.
- Expiry: `2026-08-12T06:33:10Z`, or immediately on a material Stripe object/reporting contract change.
- Decision: **`REVISE`**.
- Fitness remains `0` until an exact WorkItem consumes this card, a distinct verifier returns a digest-bound verdict, and the named consumer records ConsumerAck.

## Effect record

No task mutation, Stripe or account action, credential/private-data access, terms acceptance, outreach, application, purchase, send outside the required internal pointer, spend, implementation, deployment, merge, or publication occurred.
