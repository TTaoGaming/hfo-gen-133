---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
question_id: EXTERNAL_SIGNAL_MONITOR_STRIPE_CHECKOUT_SESSION_PAYMENT_SUCCESS_GATE_001
result: REVISE
valid_time_utc: 2026-08-04T20:31:48Z
expiry_utc: 2026-08-11T20:31:48Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: EXTERNAL_SIGNAL_MONITOR_STRIPE_CHECKOUT_SESSION_PAYMENT_SUCCESS_GATE_001
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
---

# S08 evidence card — `checkout.session.completed` is not by itself a paid-buyer event

## Self-probe

- Identity/task binding: expected and observed carrier task ID match.
- Exact branch was visible before work: `agent/gen133-bootstrap-20260730`.
- Tools available/used: native task inventory readback, authenticated GitHub search/read/write, public web research, public Slack read/write after Git readback.
- Prohibited/unused: Stripe API or Dashboard access, webhook creation, credential or private-data access, account creation, terms acceptance, outreach, application, purchase, send outside the required internal Slack pointer, spend, deployment, merge, publication, or task mutation.

## Changed bounded uncertainty

Open Gen-133 issue `#5` and the prior S08 Stripe card establish that raw Charge count is not buyer count and that payment records require typed classification. The still-unresolved event-level question is narrower:

> May the external-signal monitor count each Stripe `checkout.session.completed` webhook as one successful paid transaction or buyer?

This question changed the monitor gate because a webhook-based implementation can receive delayed-payment completion before funds are available, duplicate deliveries, manual and automatic retries, and events out of generation order.

## Exact candidate and source binding

- Provider/product: Stripe Checkout Sessions and Webhooks, API v1 surfaces.
- Candidate object: `checkout.session`.
- Candidate event types:
  - `checkout.session.completed`
  - `checkout.session.async_payment_succeeded`
  - `checkout.session.async_payment_failed`
- Binding fields needed from API readback: Checkout Session `id`, `status`, `payment_status`, `mode`, currency/amount fields when applicable, and one operator-approved artifact/order reference.
- Exact event-destination/API version: `UNKNOWN_UNTIL_ACCOUNT_OR_FIXTURE_READBACK`.
  - Stripe states that webhook event structure follows the API version fixed for the destination or account when the event is created.
  - The public version page retrieved in this pass displayed `2026-02-25.clover`, while an earlier Gen-133 card recorded a later alleged current version. Public search freshness is therefore insufficient to name the account's effective event version.
- Queue source: `https://github.com/TTaoGaming/hfo-gen-133/issues/5`
- Prior related card: `projects/spatial-app-factory/research/20260804T052900Z_S08_STRIPE_CHARGE_COUNT_BUYER_SIGNAL_AND_CREDENTIAL_BOUNDARY_EVIDENCE_CARD.md`, commit `3708b517f072522788a32b30949a1c3274f8195d`, blob `d9d3cbdb54e655dac3754b11dee1dda320c7df68`.

## Primary/current evidence accessed 2026-08-04

1. Stripe Checkout fulfillment documentation requires fulfillment logic to be safe when called multiple times for the same Checkout Session, retrieves the Session through the API, and checks `payment_status`. It states that delayed payment methods can complete Checkout before funds are available and later emit `checkout.session.async_payment_succeeded`; it also identifies `checkout.session.async_payment_failed` as a failure signal.  
   https://docs.stripe.com/checkout/fulfillment
2. Stripe webhook documentation states that live-mode events can be retried automatically for up to three days, may also be manually resent, and are not guaranteed to arrive in generation order. It recommends retrieving missing/current objects through the API rather than depending on event order.  
   https://docs.stripe.com/webhooks?lang=node
3. Stripe webhook best practices state that the same event can be delivered more than once and that separate Event objects can sometimes represent duplicates; Stripe recommends tracking processed event IDs and, for cross-Event duplicates, the underlying object ID plus event type.  
   https://docs.stripe.com/webhooks?lang=node&locale=en-GB
4. Stripe API versioning documentation states that webhook events use the destination's selected API version or the account default, and that old Event objects do not change retroactively when the account version changes.  
   https://docs.stripe.com/api/versioning?lang=curl
5. Stripe's undelivered-event recovery guide requires explicit processing-state/idempotency checks because manual recovery can overlap with continued automatic retries.  
   https://docs.stripe.com/webhooks/process-undelivered-events

## Supported claims

- `checkout.session.completed` means the Checkout flow completed; it is not, for every payment method, proof that funds are available.
- For delayed payment methods, a completed Session can remain pending until `checkout.session.async_payment_succeeded` or `checkout.session.async_payment_failed`.
- A processor can strengthen the classification by retrieving the exact Checkout Session and inspecting `payment_status` rather than trusting event type alone.
- Webhook delivery cardinality is not transaction cardinality: retries and duplicate Event objects can cause more than one delivery for the same underlying Session/outcome.
- Webhook arrival order cannot safely drive an increment-only counter without reconciliation against current object state.
- One Checkout Session is not one unique buyer. One person may create multiple Sessions, and the monitor need not or should not persist identity merely to deduplicate people.
- A privacy-safe aggregate can count exact, order-bound Sessions that reached a typed paid state while retaining only source/account context, Session-state classification, currency buckets, observation times, rule digest, and aggregate counts.

## Excluded claims and unknowns

- No Stripe API request, webhook delivery, Dashboard view, account context, credential, customer record, Charge, PaymentIntent, Checkout Session, or financial payload was accessed in this pass.
- This card does not prove that any Gen-133 product has a Stripe Checkout implementation, buyer, successful payment, conversion, payout, revenue, margin, or retained customer.
- A paid Session is not net revenue: refunds, disputes, fees, taxes, currency conversion, transfers, payout settlement, and later reversals remain separate.
- `payment_status=no_payment_required` is not a paid transaction and must remain a separate class.
- This card does not establish identical event timing for cards, bank debits, subscriptions, invoices, Payment Links, Connect accounts, or organization destinations.
- The effective Stripe API/event version, webhook-signing setup, endpoint ownership, restricted-key scope, event retention, and commercial terms remain `UNKNOWN` without authorized source-system readback.

## Required revision gate

1. Rename the proposed metric to `stripe_checkout_paid_sessions` or `successful_checkout_payment_events`; never `buyers`, `customers`, `sales`, or generic webhook count.
2. Accept only signature-verified events from one explicitly bound Stripe account/event destination. A normalized connector result without signature, destination, account context, and event version is insufficient.
3. Treat `checkout.session.completed` as a trigger to retrieve/reconcile the exact Session, not as an unconditional increment.
4. Classification after API readback:
   - `payment_status=paid` -> eligible for one `PAID_SESSION` transition.
   - `payment_status=unpaid` -> `PENDING_OR_UNPAID`; do not count paid.
   - `payment_status=no_payment_required` -> separate non-payment completion class.
   - delayed-method `checkout.session.async_payment_succeeded` -> retrieve and transition to paid only if the Session readback supports it.
   - `checkout.session.async_payment_failed` -> transition pending to failed; never decrement an unrelated aggregate or create a negative buyer.
5. Make state monotonic and idempotent by exact account context plus Checkout Session ID plus classification version. Track processed Event IDs as delivery deduplication, but do not use Event ID as the commercial unit.
6. Tolerate duplicate, concurrent, retried, and out-of-order deliveries. API readback and the stored Session state machine control the result; arrival count and arrival order do not.
7. Bind the Session to one exact HFO artifact/order namespace using a minimally necessary operator-approved reference. Do not persist customer name, email, address, payment method, receipt URL, or free-form metadata.
8. Record the destination/event API version and classification-rule digest. Version, signature, account, object, artifact, or pagination/readback uncertainty yields `UNKNOWN`, not zero or success.
9. Keep currency-specific gross payment evidence separate from refunds, disputes, and net-revenue calculations.

Required classification:

`CHECKOUT_COMPLETED_IS_TRIGGER_ONLY; PAID_REQUIRES_SESSION_READBACK; DELIVERY_COUNT_IS_NOT_TRANSACTION_OR_BUYER_COUNT`

## License, terms, and privacy uncertainty

- No third-party software-license conclusion is needed merely to describe the API contract.
- Stripe service terms, account authorization, webhook endpoint registration, effective API/restricted-key scope, event retention, tax/payment obligations, and Connect/organization boundaries are not established by public docs.
- Checkout and webhook payloads can contain private financial and customer data. A future WorkItem must prove signature verification, least privilege, aggregate-only persistence, and exclusion from Git, Slack, prompts, traces, and general-purpose agent logs.
- This card authorizes no account, endpoint, secret, API request, or terms action.

## Strongest objection

Retrieving a Checkout Session and maintaining an idempotent state machine for each event is more code and more provider calls than incrementing a webhook counter. That extra work is the minimum credible boundary: a simple `checkout.session.completed += 1` counter can count pending delayed payments as paid, double-count retries, and diverge under out-of-order delivery.

## Falsifier

`REVISE` may become `ADMIT` only if a distinct verifier replays an authorized Stripe sandbox fixture against an exact implementation and demonstrates:

- an immediate card success;
- at least one delayed-payment success and one delayed-payment failure;
- duplicate delivery of the same Event;
- distinct duplicate Event objects for the same Session/outcome;
- manual resend overlapping automatic retry;
- out-of-order completed/succeeded/failed delivery;
- exact Session API retrieval and event-version binding;
- exactly one paid classification for each successful order-bound Session;
- zero paid classifications for pending, failed, and `no_payment_required` Sessions;
- aggregate-only persistence with no prohibited payload fields.

Change to `RETIRE` for this monitor lane if signature/account/version binding, deterministic Session reconciliation, idempotency, or private-payload exclusion cannot be proved on the chosen connector/runtime.

## Verifier, consumer, expiry, and credit

- Verifier: `DISTINCT_STRIPE_SANDBOX_WEBHOOK_AND_API_REPLAY_VERIFIER`.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_STRIPE_CHECKOUT_SESSION_PAYMENT_SUCCESS_GATE_001`.
- Required ConsumerAck: exact card commit/blob, implementation/rule digest, sandbox fixture digest, event-destination/API version, account-context boundary, and explicit acknowledgment that unique buyers, net revenue, demand, conversion, and retention remain unknown.
- Expiry: `2026-08-11T20:31:48Z` or earlier if Stripe materially changes the named event/object contract.
- Fitness: `0` until consumed by an exact WorkItem, independently verified, and acknowledged by the named consumer.

## Cost and operator-minute estimate

- This research pass: `$0` spend, `0` operator minutes, `0` Stripe requests.
- Producer revision/state machine: `30–60 minutes`.
- Sandbox webhook/API replay verification: `45–90 minutes`.
- Operator authorization and account/destination/version/scope review for any later live use: `10–20 minutes`, only under a separate approved WorkItem.
- Provider request, account, and commercial cost: `UNKNOWN`; no zero-cost claim is made.

## Decision

`REVISE`

Admit `checkout.session.completed` only as a reconciliation trigger. A paid external-signal observation requires exact Session readback, typed payment state, artifact/order binding, idempotency, retry/order tolerance, privacy-safe aggregation, and version/account provenance.

## Effect record

No Stripe call, webhook creation, account or secret access, private-data use, task mutation, terms acceptance, outreach, application, purchase, send outside the required internal pointer, spend, implementation, deployment, merge, or publication occurred.
