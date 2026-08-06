---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
question_id: EXTERNAL_SIGNAL_MONITOR_STRIPE_INVOICE_PAID_BUYER_AND_CASH_SEMANTICS_GATE_001
result: REVISE
valid_time_utc: 2026-08-06T03:28:10Z
expiry_utc: 2026-08-13T03:28:10Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: EXTERNAL_SIGNAL_MONITOR_STRIPE_INVOICE_PAID_BUYER_AND_CASH_SEMANTICS_GATE_001
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
privacy_class: PUBLIC_SOURCE_ONLY_NO_STRIPE_ACCOUNT_OR_CUSTOMER_DATA
---

# S08 evidence card — `invoice.paid` is not one paying buyer or one Stripe-collected cash sale

## Self-probe

- Exact S08 carrier task ID matched: `6a526109ba348191b5f23ad3172ad568`.
- Canonical branch was visible before work: `agent/gen133-bootstrap-20260730`.
- Tools available/used: authenticated GitHub search/read/write, public primary-source web research, public Slack read and required internal pointer after Git readback.
- Prohibited/unused: Stripe API or Dashboard access, credentials, private/customer data, task mutation, account creation, terms acceptance, outreach, application, purchase, spend, deployment, merge, public publication, or demand invention.

## Changed bounded uncertainty

Gen-133 issue `#5` retains an optional Stripe external-signal lane. Existing S08 cards already bound Charge count, Checkout Session completion, refunds, disputes, Balance Transactions, and authorization/capture semantics. No prior repository card was found for this narrower question:

> May the monitor count each Stripe `invoice.paid` event as one paying buyer or one Stripe-collected cash sale?

## Exact candidate and version boundary

- Provider/product: Stripe Billing/Invoicing, API v1 snapshot events.
- Exact event: `invoice.paid`; `data.object` is an Invoice.
- Related event: `invoice.payment_succeeded`.
- Candidate object fields for later authorized readback: Invoice `id`, `status`, `currency`, `amount_due`, `amount_paid`, `amount_remaining`, `billing_reason`, `collection_method`, and payment relationship fields available under the effective API version.
- Public Stripe API documentation accessed on `2026-08-06` displayed current version `2026-02-25.clover`.
- Effective account and webhook-endpoint API version: `UNKNOWN`. Stripe states webhook endpoints use their configured version or the account default; public-current documentation cannot stand the version of an undisclosed account endpoint.

## Primary/current sources accessed 2026-08-06

1. Stripe event reference: `invoice.paid` occurs when an invoice payment attempt succeeds **or** when the invoice is marked paid out of band.  
   https://docs.stripe.com/api/events?event_types-invoice.paid=
2. Stripe Invoicing integration: `invoice.payment_succeeded` is emitted for successful invoice payments but not for `paid_out_of_band`; `invoice.paid` covers both.  
   https://docs.stripe.com/invoicing/integration
3. Stripe Invoicing lifecycle: an invoice can transition to `paid` without a successful associated PaymentIntent when it is a trial/free subscription, its amount due is covered by customer credit or is below the minimum charge amount, or it is marked `paid_out_of_band`.  
   https://docs.stripe.com/invoicing/overview?dashboard-or-api=api
4. Stripe Invoice object: `amount_due` can be zero because the total is below the minimum charge amount or account credit applies.  
   https://docs.stripe.com/api/invoices/object
5. Stripe trial documentation: starting a trial still creates an immediate invoice whose amount is zero.  
   https://docs.stripe.com/billing/subscriptions/trials
6. Stripe API versioning: webhook events use the endpoint-selected API version or the account default.  
   https://docs.stripe.com/api/versioning?lang=curl

## Supported claims

- `invoice.paid` is a reliable invoice-lifecycle and fulfillment trigger, but its event name alone does not prove Stripe collected money.
- The event can represent at least four materially different states:
  1. a successful Stripe invoice payment;
  2. an invoice marked `paid_out_of_band`, where Stripe did not make the charge;
  3. a trial or free-subscription invoice with no payment required;
  4. an invoice whose amount due was handled by customer credit or the minimum-charge rule rather than a new Stripe collection.
- One Invoice is not one unique buyer. The same customer can generate multiple invoices, and an invoice event contains no safe proof of unique-person cardinality.
- Invoice-paid count is not collected cash, net revenue, profit, payout, bank-settled cash, conversion, demand, retention, or customer count.
- A monitor can preserve a typed invoice-state aggregate without persisting customer identity.

## Excluded claims and unknowns

- No Stripe account, endpoint, webhook, Invoice, Invoice Payment, PaymentIntent, Charge, Balance Transaction, customer, subscription, tax record, or financial payload was accessed.
- This card does not prove that any Gen-133 artifact has Stripe Billing enabled, any invoice exists, any payment occurred, or any buyer exists.
- `paid_out_of_band` records operator/provider-reported lifecycle state; this card does not independently prove that external money moved.
- A nonzero `amount_paid` alone does not prove funds are available in Stripe balance or settled to a bank.
- The exact effective API version, Connect/account context, endpoint ownership, signing configuration, restricted-key scope, event retention, and service terms remain unknown.
- Exact classification of credit-balance versus minimum-charge versus free/trial cause may remain `UNKNOWN` unless version-bound Invoice and related-object fields support the distinction.

## Required revision gate

Use `invoice.paid` only as a reconciliation trigger. Never increment a generic `buyers`, `sales`, `cash`, or `revenue` metric from delivery count.

Required typed states:

```text
INVOICE_PAID_STRIPE_PAYMENT_CONFIRMED
INVOICE_PAID_OUT_OF_BAND_REPORTED
INVOICE_PAID_ZERO_AMOUNT_TRIAL_OR_FREE
INVOICE_PAID_CREDIT_OR_MINIMUM_THRESHOLD
INVOICE_PAID_PAYMENT_SOURCE_UNKNOWN
```

Required classification boundary:

```text
INVOICE_PAID_IS_LIFECYCLE_TRIGGER
INVOICE_PAID_CAN_HAVE_ZERO_STRIPE_COLLECTION
PAID_OUT_OF_BAND_IS_NOT_STRIPE_COLLECTED_CASH
TRIAL_FREE_CREDIT_MINIMUM_CHARGE_INVOICES_ARE_SEPARATE
STRIPE_COLLECTED_PAYMENT_REQUIRES_VERSION_BOUND_PAYMENT_RELATIONSHIP_READBACK
UNIQUE_BUYER_COUNT_IS_FORBIDDEN
```

For `INVOICE_PAID_STRIPE_PAYMENT_CONFIRMED`, require all of:

1. signature-verified event from one explicitly bound Stripe account/event destination;
2. exact endpoint/event API version;
3. current Invoice retrieval and idempotent state keyed by account context plus Invoice ID and rule digest;
4. nonzero currency-bound payment amount;
5. version-bound Invoice Payment and associated PaymentIntent/Charge evidence showing a successful Stripe payment rather than `paid_out_of_band`, credit-only, minimum-charge, free, or trial state;
6. separate Balance Transaction reconciliation before labeling Stripe balance as pending/available; bank settlement remains a separate source-system claim;
7. aggregate-only persistence, excluding name, email, address, payment method, receipt URL, free-form metadata, and customer payloads.

Duplicate, retried, concurrent, or out-of-order deliveries must not change commercial cardinality. Event ID may deduplicate delivery, but Invoice ID and typed current-state reconciliation control the aggregate. Multiple invoices tied to one customer remain multiple invoices, not multiple unique buyers.

## License, terms, and privacy uncertainty

- No third-party software-license conclusion is required to describe Stripe's public API contract.
- Stripe service terms, account authorization, endpoint registration, payment/tax obligations, Connect boundaries, commercial pricing, and restricted-key permissions are not established by public documentation.
- Invoice and payment payloads can contain private financial and customer data. A later WorkItem must prove least privilege, signature verification, aggregate-only retention, and exclusion from Git, Slack, prompts, traces, and general-purpose agent logs.
- This card authorizes no account, endpoint, key, API request, terms action, or financial operation.

## Strongest objection

Stripe recommends `invoice.paid` for reliable fulfillment because it covers both successful Stripe payments and out-of-band payments. That makes it a strong entitlement/lifecycle signal. It still cannot support a metric labeled paying buyer or Stripe-collected cash because the broader event intentionally includes cases where Stripe collected nothing.

## Falsifier

`REVISE` may become `ADMIT` for a narrowly named typed metric only if a distinct authorized verifier runs a version-bound Stripe sandbox/test-clock replay that covers:

- successful automatic Stripe invoice payment;
- a zero-amount trial invoice;
- a free-subscription invoice;
- customer credit fully covering amount due;
- below-minimum-charge handling;
- `paid_out_of_band` marking with no Stripe charge;
- multiple paid invoices for one Customer;
- duplicate, concurrent, retried, and out-of-order event delivery;
- Invoice, Invoice Payment, PaymentIntent/Charge, and Balance Transaction reconciliation where applicable;
- deterministic exactly-once typed aggregates with no unique-person or prohibited payload persistence.

Retire the collected-cash metric if the chosen runtime cannot prove endpoint/account/version binding, signature verification, deterministic payment-source classification, and private-payload exclusion.

## Verifier, consumer, expiry, and credit

- Verifier: `DISTINCT_STRIPE_SANDBOX_INVOICE_PAID_PAYMENT_SOURCE_AND_ZERO_AMOUNT_CLASSIFICATION_VERIFIER`.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_STRIPE_INVOICE_PAID_BUYER_AND_CASH_SEMANTICS_GATE_001`.
- Required ConsumerAck: exact card commit/blob, implementation/rule digest, sandbox fixture digest, endpoint/API version, account-context boundary, typed aggregate names, and explicit acknowledgment that unique buyers, net revenue, demand, retention, payout, and bank cash remain unknown.
- Expiry: `2026-08-13T03:28:10Z`, or earlier if Stripe materially changes the named event/object contract.
- Fitness: `0` until exact WorkItem consumption, distinct verification, and ConsumerAck.

## Cost and operator-minute estimate

- This research pass: `$0` surfaced spend, `0` operator minutes, `0` Stripe requests.
- Producer classification/state-machine amendment: `25–45 minutes`.
- Sandbox/test-clock verification: `45–90 minutes`.
- Later account/endpoint/version/scope review: `10–20 operator minutes`, only under a separate approved WorkItem.
- Provider quota and commercial cost: `UNKNOWN`; no zero-cost claim is made.

## Decision

`REVISE`

Admit `invoice.paid` only as an invoice-lifecycle reconciliation trigger. A paying-buyer or Stripe-collected-cash interpretation is unsupported without version-bound payment-source readback and typed classification.

## Effect record

No Stripe request, credential/private-data access, account action, task mutation, terms acceptance, outreach, application, purchase, spend, implementation, deployment, merge, public publication, or demand claim occurred. Only this Git evidence write/readback and the required sanitized internal Slack pointer are permitted effects.
