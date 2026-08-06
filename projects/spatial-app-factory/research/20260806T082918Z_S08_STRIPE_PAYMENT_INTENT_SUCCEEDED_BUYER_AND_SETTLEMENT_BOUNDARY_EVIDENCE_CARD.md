---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
question_id: EXTERNAL_SIGNAL_MONITOR_STRIPE_PAYMENT_INTENT_SUCCEEDED_BUYER_AND_SETTLEMENT_SEMANTICS_GATE_001
result: REVISE
valid_time_utc: 2026-08-06T08:29:18Z
expiry_utc: 2026-08-13T08:29:18Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: EXTERNAL_SIGNAL_MONITOR_STRIPE_PAYMENT_INTENT_SUCCEEDED_BUYER_AND_SETTLEMENT_SEMANTICS_GATE_001
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
privacy_class: PUBLIC_SOURCE_ONLY_NO_STRIPE_ACCOUNT_OR_CUSTOMER_DATA
---

# S08 evidence card — `payment_intent.succeeded` is payment completion, not one new buyer or settled cash

## Self-probe

- Exact carrier task ID matched: `6a526109ba348191b5f23ad3172ad568`.
- Canonical repository and branch were readable before work: `TTaoGaming/hfo-gen-133@agent/gen133-bootstrap-20260730`.
- Tools available/used: authenticated GitHub search/read/write, public primary-source web research, public Slack read, and the required sanitized Slack pointer after Git readback.
- Prohibited/unused: Stripe API or Dashboard access, credentials, private/customer data, task mutation, account creation, terms acceptance, outreach, application, purchase, spend, implementation, deployment, merge, or public publication.

## Changed bounded uncertainty

The explicit lane rotation advanced from interaction/input adapters to distribution and buyer evidence. The prior Stripe card established that `invoice.paid` is broader than a Stripe-collected payment. A best-effort repository search found no existing S08 card for the narrower successor question:

> May an external-signal monitor count each Stripe `payment_intent.succeeded` event as one new paying buyer or one settled cash sale?

This card investigates only that semantic boundary. It does not evaluate a live integration.

## Exact candidate and version boundary

- Provider/product: Stripe Payments, API v1 webhook snapshot events.
- Exact event: `payment_intent.succeeded`; `data.object` is a PaymentIntent.
- Candidate fields: `id`, `status`, `amount`, `amount_received`, `currency`, `customer`, `latest_charge`, `livemode`, and related Charge/Balance Transaction state.
- Effective account and webhook-endpoint API version: `UNKNOWN`.
- Stripe states webhook endpoints either use a specifically configured API version or the account default, and event structure is version-bound. Therefore public-current documentation does not stand the schema of an undisclosed endpoint.

## Primary/current sources accessed 2026-08-06

1. Stripe event reference: `payment_intent.succeeded` occurs when a PaymentIntent has successfully completed payment.  
   https://docs.stripe.com/api/events/types
2. Stripe PaymentIntent lifecycle: `succeeded` means the payment flow is complete and is an appropriate fulfillment boundary; refunds remain a later lifecycle.  
   https://docs.stripe.com/payments/paymentintents/lifecycle
3. Stripe PaymentIntent object: `amount_received` is the amount the PaymentIntent collects; `customer` is nullable and identifies a Stripe Customer only if one exists; `latest_charge` identifies the latest associated Charge.  
   https://docs.stripe.com/api/payment_intents/object
4. Stripe Charge object: the Charge balance transaction describes the charge's account-balance impact but explicitly excludes refunds and disputes; `customer` is nullable, and refund/dispute state is separate.  
   https://docs.stripe.com/api/charges/object
5. Stripe Balance Transaction object: `amount` is gross, `fee` is separate, `net` is the Stripe-balance impact, `status` is `pending` or `available`, and `available_on` is a separate timestamp.  
   https://docs.stripe.com/api/balance_transactions/object
6. Stripe webhook guidance: duplicate event delivery can occur, separate Event objects can describe the same object/event type, event ordering is not guaranteed, and endpoint API version controls event structure.  
   https://docs.stripe.com/webhooks
7. Stripe webhook versioning: an endpoint can use a specific version or the account default, and version changes can alter deserialization and structure.  
   https://docs.stripe.com/webhooks/versioning

## Supported claims

- `payment_intent.succeeded` is a strong payment-completion and fulfillment signal for the exact PaymentIntent.
- `amount_received` can support a currency-bound **gross amount collected by that PaymentIntent** after signature verification and version-bound current-object reconciliation.
- One PaymentIntent is not one unique buyer:
  - `customer` can be null;
  - one Stripe Customer can have multiple successful PaymentIntents;
  - a Customer object is an account record, not independent proof of one natural person or organization.
- PaymentIntent success is not settled cash:
  - the related Balance Transaction can still be `pending`;
  - `available` Stripe balance is distinct from bank payout or bank settlement;
  - Stripe fees require the Balance Transaction `net` field rather than PaymentIntent `amount_received`;
  - later refunds and disputes are separate lifecycle effects not represented by the original succeeded event name.
- Webhook delivery count is not commercial cardinality. Duplicate, retried, concurrent, or out-of-order deliveries must not increment payment, buyer, sale, or cash totals.

## Excluded claims and unknowns

- No Stripe account, endpoint, webhook, PaymentIntent, Charge, Balance Transaction, Customer, refund, dispute, payout, bank account, or financial payload was accessed.
- This card does not prove that any Gen-133 artifact has Stripe enabled, any payment occurred, any buyer exists, or any amount was collected.
- It does not prove the effective API version, endpoint ownership, signing configuration, Connect/account context, restricted-key scope, event retention, payout schedule, tax treatment, or service pricing.
- A non-null `customer` does not prove a new buyer, a unique person, a first purchase, retention, conversion, or customer identity quality.
- `amount_received` does not prove net revenue, profit, Stripe-balance availability, payout, bank settlement, irreversibility, or absence of later refund/dispute loss.
- Public documentation does not prove live wrapper parity or exact field availability under the undisclosed endpoint version.

## Required revision gate

Do not map `payment_intent.succeeded` delivery count directly to `buyers`, `new_buyers`, `sales`, `revenue`, `available_cash`, or `bank_cash`.

Required typed states:

```text
PAYMENT_INTENT_SUCCEEDED_GROSS_COLLECTED
PAYMENT_INTENT_SUCCEEDED_CUSTOMER_RECORD_PRESENT
PAYMENT_INTENT_SUCCEEDED_CUSTOMER_RECORD_ABSENT
PAYMENT_INTENT_SUCCEEDED_STRIPE_BALANCE_PENDING
PAYMENT_INTENT_SUCCEEDED_STRIPE_BALANCE_AVAILABLE
PAYMENT_INTENT_SUCCEEDED_BALANCE_STATE_UNKNOWN
PAYMENT_INTENT_SUCCEEDED_REFUND_OR_DISPUTE_LIFECYCLE_OPEN
```

Required semantic boundary:

```text
PAYMENT_COMPLETION=true
FULFILLMENT_SIGNAL=true
UNIQUE_BUYER_COUNT=false
NEW_BUYER_COUNT=false
NET_REVENUE=false
STRIPE_BALANCE_AVAILABLE=REQUIRES_BALANCE_TRANSACTION_STATE
BANK_SETTLED_CASH=false
```

For a narrowly named `payment_intent_succeeded_gross_collected` aggregate, require all of:

1. signature-verified event from one explicitly bound Stripe account/event destination;
2. exact endpoint/event API version and `livemode` partition;
3. idempotent reconciliation keyed by account context plus PaymentIntent ID and rule digest, not delivery count alone;
4. current PaymentIntent retrieval confirming `status=succeeded`, currency, and `amount_received`;
5. related latest successful Charge readback and separate Balance Transaction classification;
6. separate refund/dispute reconciliation before any net or retained-value metric;
7. aggregate-only persistence, excluding name, email, address, payment method, receipt URL, free-form metadata, client secret, and customer payloads.

A unique-buyer or new-buyer metric requires a separately approved identity and first-purchase model. PaymentIntent or Customer IDs alone are insufficient.

## License, terms, cost, and privacy uncertainty

- No third-party software-license conclusion is required to describe Stripe's public API contract.
- Stripe service terms, account authorization, endpoint registration, payment/tax obligations, Connect boundaries, commercial pricing, and restricted-key permissions are not established by public documentation.
- Payment payloads can contain private financial and customer data. A later WorkItem must prove least privilege, signature verification, aggregate-only retention, secret exclusion, and no persistence to Git, Slack, prompts, traces, or general-purpose agent logs.
- This card authorizes no account, endpoint, key, API request, terms action, financial operation, or customer-data use.

## Strongest objection

Stripe explicitly says a succeeded PaymentIntent means the payment flow is complete, funds are in the Stripe account, and fulfillment can proceed. That makes it materially cleaner than `invoice.paid` for confirming a completed Stripe payment. It still does not establish one new buyer, net revenue, available Stripe balance, payout, or bank-settled cash because buyer identity is optional/non-unique and settlement/reversal state lives on related objects and later lifecycle events.

## Falsifier

`REVISE` may become `ADMIT` only for narrowly named typed metrics if a distinct authorized verifier runs a version-bound Stripe sandbox replay covering:

- one guest PaymentIntent with `customer=null`;
- two successful PaymentIntents for one Customer;
- first and repeat purchases with an independently bound order/customer model;
- automatic and manual capture;
- an asynchronous payment method progressing through `processing` to `succeeded`;
- duplicate Event delivery and two Event objects for the same PaymentIntent/event type;
- out-of-order Charge, PaymentIntent, refund, dispute, and Balance Transaction observations;
- Balance Transaction `pending` to `available` transition;
- full and partial refund plus dispute lifecycle;
- deterministic exactly-once typed aggregates with prohibited payload exclusion.

Retire any unique-buyer or bank-cash metric derived only from PaymentIntent events if the runtime cannot prove identity model, first-purchase state, endpoint/account/version binding, signature verification, current-object reconciliation, reversal handling, and private-payload exclusion.

## Verifier, consumer, expiry, and credit

- Verifier: `DISTINCT_STRIPE_SANDBOX_PAYMENT_INTENT_BUYER_IDENTITY_BALANCE_AND_REVERSAL_REPLAY_VERIFIER`.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_STRIPE_PAYMENT_INTENT_SUCCEEDED_BUYER_AND_SETTLEMENT_SEMANTICS_GATE_001`.
- Required ConsumerAck: exact card commit/blob, implementation/rule digest, sandbox fixture digest, endpoint/API version, account-context boundary, typed aggregate names, and explicit acknowledgment that unique buyers, new buyers, net revenue, payout, demand, retention, and bank cash remain unknown.
- Expiry: `2026-08-13T08:29:18Z`, or earlier if Stripe materially changes the named event/object contract.
- Fitness: `0` until exact WorkItem consumption, distinct verification, and ConsumerAck.

## Cost and operator-minute estimate

- This research pass: `$0` surfaced spend, `0` operator minutes, `0` Stripe requests.
- Producer classification/state-machine amendment: `25–45 minutes`.
- Sandbox replay and reversal/balance verification: `60–120 minutes`.
- Later account/endpoint/version/scope review: `10–20 operator minutes`, only under a separate approved WorkItem.
- Provider quota and commercial cost: `UNKNOWN`; no zero-cost claim is made.

## Decision

`REVISE`

Admit `payment_intent.succeeded` only as a version-bound payment-completion trigger and, after reconciliation, a gross-collected-payment state. Do not infer one new buyer, net revenue, available cash, payout, or bank settlement.

## Effect record

No Stripe request, credential/private-data access, account action, task mutation, terms acceptance, outreach, application, purchase, spend, implementation, deployment, merge, public publication, or demand claim occurred. Only this Git evidence write/readback and the required sanitized internal Slack pointer are permitted effects.
