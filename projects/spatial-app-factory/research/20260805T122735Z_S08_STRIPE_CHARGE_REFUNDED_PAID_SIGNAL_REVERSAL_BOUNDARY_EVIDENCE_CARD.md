---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
question_id: EXTERNAL_SIGNAL_MONITOR_STRIPE_REFUND_LIFECYCLE_SEMANTICS_GATE_001
valid_time_utc: 2026-08-05T12:27:35Z
expiry_utc: 2026-08-12T12:27:35Z
decision: REVISE
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
---

# S08 evidence card — `charge.refunded` must not decrement a paid-event or buyer counter

## Self-probe

- Identity: `S08 Research and Candidate Scout`; expected and observed task IDs match.
- Tools used: authenticated GitHub read/search/write, primary-source web research, Slack only after Git readback.
- Prohibited and unused: Stripe API or Dashboard access, credentials, private financial/customer data, account or webhook creation, terms acceptance, outreach, application, purchase, send outside the required internal pointer, spend, implementation, deployment, merge, publication, or task mutation.

## Changed bounded uncertainty

Gen-133 issue `#5` keeps an optional Stripe external-signal lane. Earlier S08 cards separated successful transaction events, paid Checkout Sessions, Stripe-balance activity, buyers, and revenue. The next unresolved lifecycle question is narrower:

> May the monitor decrement one paid transaction, sale, or buyer whenever it receives `charge.refunded`?

Exact candidate:

- Provider: Stripe
- Surface: API v1 Events, Charges, and Refunds
- Trigger: `charge.refunded`; `data.object` is a Charge
- Corroborating lifecycle events: `refund.created`, `refund.updated`, `refund.failed`
- Object fields: Charge `amount`, `amount_captured`, `amount_refunded`, `refunded`; Refund `id`, `amount`, `currency`, `charge`, `payment_intent`, `status`, `balance_transaction`, and `failure_balance_transaction`
- Effective account/event-destination API version: `UNKNOWN_UNTIL_AUTHORIZED_READBACK`; public docs do not bind the version used by a specific destination or historical Event.
- Queue source: https://github.com/TTaoGaming/hfo-gen-133/issues/5

No matching prior S08 `charge.refunded` lifecycle card was found before this write.

## Primary/current evidence accessed 2026-08-05

1. Stripe defines `charge.refunded` as occurring whenever a charge is refunded, including partial refunds, and directs integrations to `refund.created` for refund information. `data.object` is a Charge.  
   https://docs.stripe.com/api/events/types
2. Stripe's refund guide says events are emitted whenever a refund is created or changed; it recommends listening at minimum for `refund.created` and separately documents `refund.updated` and `refund.failed`.  
   https://docs.stripe.com/refunds?dashboard-or-api=api
3. A Refund can be partial, and multiple partial refunds can be created until the remaining refundable amount is exhausted. Refund status can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`.  
   https://docs.stripe.com/api/refunds/object  
   https://docs.stripe.com/api/refunds/create
4. A Charge exposes cumulative `amount_refunded`, which can be less than the original amount when only a partial refund was issued.  
   https://docs.stripe.com/api/charges/object
5. Stripe does not guarantee webhook delivery order; retries and manual resends can overlap, and consumers should retrieve current objects rather than infer state from event arrival order or count. Event shape is version-bound when created and does not retroactively change.  
   https://docs.stripe.com/webhooks

## Supported claims

- `charge.refunded` is a refund-state trigger, not a buyer, sale, or refund-count unit.
- Partial refunds are explicitly included. Therefore one `charge.refunded` event cannot mean that one whole paid order or buyer ceased to exist.
- One Charge can receive multiple partial Refund objects. Delivery/event count is not refunded-order count or refunded-amount evidence.
- A refund can have nonterminal or unsuccessful states. A created or changed refund is not automatically a completed customer refund.
- Charge `amount_refunded` is cumulative. Re-adding its full value on each event can double count; a processor needs exact prior-state reconciliation or Refund-ID state.
- A successful refund is a financial lifecycle adjustment to a prior payment. It does not erase the historical fact that a payment transaction or paid Checkout Session occurred.
- Privacy-safe monitoring can retain currency-bucketed aggregate gross paid amount, successful refund amount, pending refund amount, and failed/canceled refund amount without retaining customer identity.

## Excluded claims and unknowns

- `charge.refunded` delivery count is not unique buyers, refunded buyers, refunded orders, churn, dissatisfaction, product-market fit, or demand.
- A refund event or `amount_refunded` field is not recognized revenue, profit, bank-settled cash, or proof that the customer has received funds.
- This card does not establish the exact emission timing of `charge.refunded` relative to every payment method's Refund status transition. Treat that relation as `UNKNOWN` and reconcile the Refund object.
- This card does not establish Connect transfer reversal, application-fee refund, tax reversal, dispute resolution, or cross-account settlement semantics.
- No Gen-133 Stripe account, payment, refund, buyer, revenue, or private payload was observed.

## Required revision gate

1. Preserve the historical paid-event unit. Never decrement `successful_transaction_events`, `stripe_checkout_paid_sessions`, or any buyer metric because `charge.refunded` arrived.
2. Add a separate refund state machine keyed by exact Stripe account context plus Refund ID. Bind each Refund to the exact Charge/PaymentIntent and approved artifact/order namespace.
3. Treat `charge.refunded` only as a reconciliation trigger. Prefer the Refund object/events for the commercial unit and retrieve current state when delivery ordering or completeness is uncertain.
4. Classify each Refund independently:
   - `succeeded` -> eligible for one `SUCCESSFUL_REFUND_AMOUNT` transition;
   - `pending` or `requires_action` -> `PENDING_REFUND_AMOUNT` only;
   - `failed` or `canceled` -> no successful-refund decrement; preserve a typed failure/cancellation transition.
5. Keep full and partial refunds distinct. Derive `FULLY_REFUNDED_CHARGE` only when exact Charge readback shows cumulative `amount_refunded` equals the relevant captured amount under a version-bound rule.
6. Deduplicate delivery by Event ID, but deduplicate commercial refund state by account plus Refund ID. Tolerate retries, duplicate Event objects, concurrent delivery, and out-of-order `created`, `updated`, `failed`, and Charge events.
7. Never sum cumulative Charge `amount_refunded` on every event. Use Refund-object transitions or a monotonic per-Charge prior/current delta with exact state versioning and replay protection.
8. Keep currency-specific gross paid evidence and successful refund adjustments separate. Label any arithmetic result `GROSS_PAID_LESS_SUCCESSFUL_REFUNDS`; do not call it net revenue, profit, settled cash, or buyers.
9. For Connect, application fees, transfers, taxes, disputes, and payout settlement, emit `UNKNOWN_REQUIRES_SEPARATE_RECONCILIATION` unless exact separately approved evidence is available.
10. Persist aggregates and rule/provenance digests only. Do not persist Refund, Charge, PaymentIntent, customer, email, receipt, payment-method, address, or free-form metadata in Git, Slack, prompts, traces, or general agent logs.

Required classification:

`CHARGE_REFUNDED_IS_RECONCILIATION_TRIGGER; REFUND_OBJECT_STATUS_CONTROLS_ADJUSTMENT; PAID_EVENT_HISTORY_IS_NOT_DECREMENTED`

## License, terms, privacy, and version uncertainty

- No software-license conclusion is required merely to use the documented API contract.
- Stripe service terms, account authorization, event-destination ownership, restricted-key scope, retention requirements, effective API version, Connect topology, and commercial obligations remain unstood by public documentation.
- Refund and Charge payloads are private financial/customer data. Any future execution requires a separately authorized WorkItem with least privilege, signature verification, aggregate-only retention, and no raw payload export.

## Strongest objection

A single cumulative `Charge.amount_refunded` value appears simpler than storing Refund state. That shortcut remains unsafe for event-driven counting: it is cumulative, partial refunds are allowed, events can repeat or arrive out of order, and failed/canceled/nonterminal Refund states require typed handling. At minimum the processor must retain a versioned prior state or exact Refund-ID lifecycle.

## Falsifier

`REVISE` may become `ADMIT` only after a distinct Stripe-sandbox verifier replays an exact implementation against:

- one full successful refund;
- two partial refunds on one Charge;
- a pending or `requires_action` refund that later succeeds;
- a refund that fails and exposes the appropriate reversal/failure state;
- a canceled refund where supported;
- duplicate and manually resent events;
- distinct duplicate Event objects for one Refund transition;
- out-of-order Charge and Refund events;
- replay from empty state producing identical aggregates;
- zero decrement of paid-event/session history;
- aggregate-only persistence with no prohibited fields.

Change to `RETIRE` for this monitor lane if exact account/version binding, Refund-ID lifecycle state, deterministic replay, or raw-payload exclusion cannot be proved.

## Verifier, consumer, expiry, and cost

- Verifier: `DISTINCT_STRIPE_SANDBOX_REFUND_LIFECYCLE_REPLAY_VERIFIER`.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_STRIPE_REFUND_LIFECYCLE_SEMANTICS_GATE_001`.
- Required ConsumerAck: exact card commit/blob, implementation and fixture digests, account/version boundary, classification-rule digest, and explicit acknowledgment that buyers, demand, recognized revenue, profit, and settled cash remain unknown.
- Expiry: `2026-08-12T12:27:35Z`, or earlier if Stripe materially changes the named event/object contract.
- This research pass: `$0` spend; `0` operator minutes; `0` Stripe requests.
- Producer revision: `20–45` minutes.
- Sandbox lifecycle and replay verification: `40–90` minutes.
- Any later live authorization/scope/version review: `10–20` operator minutes under a separate approved WorkItem.
- Provider quota/commercial cost: `UNKNOWN`.

## Decision

`REVISE`

A refund must be modeled as a separate, status-bearing financial adjustment. `charge.refunded` is not permission to decrement a paid-event, paid-session, sale, or buyer counter.
