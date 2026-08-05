---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
question_id: EXTERNAL_SIGNAL_MONITOR_STRIPE_AUTHORIZATION_CAPTURE_SETTLEMENT_GATE_002
result: REVISE
valid_time_utc: 2026-08-05T22:27:11Z
expiry_utc: 2026-08-12T22:27:11Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: EXTERNAL_SIGNAL_MONITOR_STRIPE_TRANSACTION_EVENT_SEMANTICS_AND_CREDENTIAL_GATE_001
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
---

# S08 evidence card — Stripe `paid=true` is not captured funds or available cash

## Self-probe

- Identity/task binding: expected and observed task ID match.
- Tools available/used: authenticated GitHub search/read/write, public web research against Stripe primary documentation, public Slack read/write after Git readback.
- Prohibited/unused: Stripe API or Dashboard access, credential or private-data access, account or webhook mutation, terms acceptance, outreach, application, purchase, send outside the required internal pointer, spend, deployment, merge, publication, or task mutation.

## Changed bounded uncertainty

Open Gen-133 issue `#5` keeps an optional Stripe read-only Charge lane in the experiment queue. The prior S08 gate classified `status=succeeded`, `paid=true`, and `livemode=true` as stronger transaction evidence, but did not fully separate successful authorization, capture, Stripe-balance settlement, and bank payout.

Bounded question:

> May the external-signal monitor treat a Charge with `paid=true` or `status=succeeded` as captured money, available Stripe balance, or settled cash?

Answer: **No.** The monitor must reconcile capture and balance state separately.

Queue and prior binding:

- Queue: `https://github.com/TTaoGaming/hfo-gen-133/issues/5`
- Prior card: `projects/spatial-app-factory/research/20260804T052900Z_S08_STRIPE_CHARGE_COUNT_BUYER_SIGNAL_AND_CREDENTIAL_BOUNDARY_EVIDENCE_CARD.md`
- Prior commit/blob: `3708b517f072522788a32b30949a1c3274f8195d` / `d9d3cbdb54e655dac3754b11dee1dda320c7df68`

## Exact candidate and version boundary

- Provider/product: Stripe API v1 Charge and Balance Transaction surfaces.
- Candidate fields: Charge `status`, `paid`, `captured`, `amount`, `amount_captured`, `balance_transaction`, `livemode`; Balance Transaction `status`, `available_on`, `amount`, `fee`, `net`, `currency`.
- Candidate workflows: automatic capture, manual authorization and later capture, partial capture, authorization expiry/cancellation, and settlement from pending to available.
- Effective account, SDK, request, and event-destination API versions: `UNKNOWN_UNTIL_AUTHORIZED_FIXTURE_READBACK`. Public documentation snapshots surfaced inconsistent “current version” labels during this pass, so no current account version is asserted.

## Primary/current evidence accessed 2026-08-05

1. Stripe’s Charge object defines `paid=true` when a Charge succeeded **or was successfully authorized for later capture**. The same object separately exposes `captured` and `amount_captured`; `amount_captured` can be less than the original amount after partial capture.  
   https://docs.stripe.com/api/charges/object
2. Stripe’s manual-capture guide states that authorization places a hold, the PaymentIntent transitions to `requires_capture`, and uncaptured authorization can expire and release the funds. Capture is a separate operation.  
   https://docs.stripe.com/payments/place-a-hold-on-a-payment-method
3. Stripe’s capture API describes capturing an existing uncaptured Charge and returns an updated Charge with `captured=true`; uncaptured Charges can expire before capture.  
   https://docs.stripe.com/api/charges/capture
4. Stripe’s balance documentation separates pending funds from available funds. Captured payment proceeds can remain pending until settlement; only then do they move to available Stripe balance.  
   https://docs.stripe.com/payments/balances
5. Stripe’s Balance Transaction object exposes `status` (`pending` or `available`), `available_on`, and fee/net fields. A Charge’s balance-transaction reference describes account-balance impact but does not include later refunds or disputes.  
   https://docs.stripe.com/api/balance_transactions/object  
   https://docs.stripe.com/api/charges/object

## Supported claims

- `paid=true` is authorization-or-success evidence, not proof of capture.
- `captured=true` and `amount_captured>0` are required before classifying any captured amount.
- Gross captured amount is bounded by `amount_captured`, not the Charge’s original `amount`.
- A successfully authorized but uncaptured payment can later expire or be canceled without capture.
- Captured proceeds can remain `pending` in Stripe; capture does not prove funds are `available` in the Stripe balance.
- Available Stripe balance does not prove bank payout, bank settlement, recognized revenue, profit, or spendable cash outside Stripe.
- Current-object reconciliation is safer than incrementing on deliveries or updates. Capture-related object fields can change, and cumulative fields must not be re-added on every observation.

## Excluded claims and unknowns

- No Stripe request, Charge, PaymentIntent, Balance Transaction, account, key, webhook, customer, or financial payload was accessed.
- This card proves no buyer, sale, capture, balance availability, payout, revenue, profit, conversion, or demand for any HFO artifact.
- It does not define accounting recognition, tax treatment, Connect destination/platform allocation, reserves, cross-currency settlement, payout timing, or bank receipt.
- It does not establish whether the target account uses manual capture, multicapture, delayed capture, Connect, separate charges/transfers, or multiple settlement currencies.
- Refunds, disputes, fees, transfers, taxes, and payout failures remain independent lifecycle adjustments.
- Exact API-version behavior and feature availability remain unknown until a version-bound sandbox fixture is read by an authorized WorkItem.

## Required revision gate

Replace any binary `succeeded_paid` or `paid_charge` bucket with explicit states:

```text
AUTHORIZED_UNCAPTURED
CAPTURED_PENDING_STRIPE_BALANCE
CAPTURED_AVAILABLE_STRIPE_BALANCE
CAPTURED_BALANCE_STATE_UNKNOWN
EXPIRED_OR_CANCELED_UNCAPTURED
REFUNDED_OR_DISPUTED_SEPARATE_LIFECYCLE
```

Minimum rules:

1. `paid=true` with `captured=false` yields `AUTHORIZED_UNCAPTURED`; captured amount is zero for the monitor.
2. A captured classification requires exact account context, `livemode=true`, `captured=true`, and `amount_captured>0` from current Charge readback.
3. Use `amount_captured` as current gross captured state. Do not add the cumulative value on every event or poll; reconcile by account context plus Charge ID and prior state.
4. A balance-availability classification additionally requires the exact associated Balance Transaction readback and its current `status`/`available_on` under the same account context.
5. Keep `CAPTURED_PENDING_STRIPE_BALANCE` separate from `CAPTURED_AVAILABLE_STRIPE_BALANCE`.
6. Never label either class `cash`, `bank-settled`, `revenue`, `profit`, `sale`, or `buyer` without separate evidence and policy.
7. Persist aggregate currency buckets and lifecycle-state counts only. Do not persist Charge IDs, Balance Transaction IDs, customer identity, payment details, receipt URLs, descriptions, or metadata in Git, Slack, prompts, traces, or general-purpose agent logs.
8. Version, account, cursor, capture, balance-transaction, or lifecycle uncertainty yields `UNKNOWN`/`PARTIAL_UNKNOWN`, never zero or success.

Required classification:

`PAID_CAN_MEAN_AUTHORIZED; CAPTURE_REQUIRES_CAPTURE_FIELDS; AVAILABLE_BALANCE_REQUIRES_BALANCE_TRANSACTION_STATE; BANK_CASH_REMAINS_UNKNOWN`

## License, terms, privacy, and cost uncertainty

- No third-party software-license conclusion is needed to describe these API fields.
- Stripe terms, merchant authorization, effective restricted-key permissions, account ownership, event retention, settlement rules, and Connect boundaries are not established by public documentation alone.
- Charge and balance data are private financial records. Future execution requires a separately authorized, least-privilege, aggregate-only WorkItem with raw-payload exclusion.
- Provider request pricing, quota impact, and account-specific commercial cost remain `UNKNOWN`; no zero-cost API claim is made.

## Strongest objection

For a simple demand monitor, `paid=true` may be “good enough” because most small Checkout card payments use automatic capture. That shortcut creates false financial state precisely where the data matters: manual-capture authorizations, partial captures, expiration, delayed settlement, and balance availability are all distinct provider states. A monitor may expose a coarse authorization count, but it must label it as authorization evidence—not captured or available money.

## Falsifier

`REVISE` may become `ADMIT` only if a distinct Stripe sandbox verifier, bound to an exact API version and implementation digest, replays:

- automatic capture;
- manual authorization before capture;
- capture after authorization;
- partial capture;
- uncaptured expiry or cancellation;
- duplicate and out-of-order object/event observations;
- pending-to-available Balance Transaction transition;
- aggregate-only persistence with prohibited fields absent.

The verifier must prove deterministic replay, no captured amount for authorization-only state, no cumulative double count, exact currency buckets, and no promotion from Stripe-balance availability to bank cash.

Change to `RETIRE` for the live monitor lane if restricted read access, account/version binding, capture reconciliation, balance-state reconciliation, or raw-financial-payload exclusion cannot be proved.

## Verifier, consumer, expiry, and credit

- Verifier: `DISTINCT_STRIPE_SANDBOX_AUTHORIZATION_CAPTURE_AND_BALANCE_STATE_REPLAY_VERIFIER`.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_STRIPE_TRANSACTION_EVENT_SEMANTICS_AND_CREDENTIAL_GATE_001`.
- Required ConsumerAck: exact card commit/blob, implementation/rule digest, API-version binding, account-context boundary, fixture digest, aggregate-only retention evidence, and explicit acknowledgement that unique buyers, net revenue, payout, and bank cash remain unknown.
- Expiry: `2026-08-12T22:27:11Z`, or earlier if Stripe materially changes the named fields or capture/settlement contract.
- Fitness: `0` until exact WorkItem consumption, distinct verification, and ConsumerAck.

## Cost and operator-minute estimate

- This research pass: `$0` spend, `0` operator minutes, `0` Stripe requests.
- Producer schema/classifier amendment: `20–40 minutes`.
- Sandbox authorization/capture/balance replay: `45–90 minutes`.
- Operator authorization and account/version/scope review for later live use: `10–20 minutes`, only under a separate approved WorkItem.

## Decision

`REVISE`

`paid=true` must not be promoted to captured funds, available Stripe balance, or bank cash. The external-signal monitor needs separate authorization, capture, and balance-availability states with current-object reconciliation and aggregate-only persistence.

## Effect record

Only the required Git evidence write/readback and one internal Slack pointer are authorized. No Stripe call, credential/private-data access, account or webhook action, terms acceptance, implementation, task mutation, outreach, application, purchase, spend, deployment, merge, external publication, or other send occurred.
