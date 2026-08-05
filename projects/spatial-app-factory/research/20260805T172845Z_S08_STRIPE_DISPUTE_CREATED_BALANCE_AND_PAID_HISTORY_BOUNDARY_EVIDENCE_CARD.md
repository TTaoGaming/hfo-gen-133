---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
question_id: EXTERNAL_SIGNAL_MONITOR_STRIPE_DISPUTE_LIFECYCLE_SEMANTICS_GATE_001
valid_time_utc: 2026-08-05T17:28:45Z
expiry_utc: 2026-08-12T17:28:45Z
decision: REVISE
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
---

# S08 evidence card — `charge.dispute.created` is not a lost-sale or cash-withdrawal unit

## Self-probe

- Identity: `S08 Research and Candidate Scout`; expected and observed task IDs match.
- Tools used: authenticated GitHub read/search/write, current Stripe primary-source research, Slack only after Git readback.
- Prohibited and unused: Stripe API or Dashboard access, credentials, private financial/customer data, account or webhook changes, terms acceptance, outreach, application, purchase, spend, implementation, deployment, merge, public publication, or task mutation.

## Changed bounded uncertainty

Gen-133 issue `#5` retains an optional read-only Stripe signal lane. The immediately prior S08 card separated Refund lifecycle adjustments from historical paid-event counts and explicitly left dispute handling unresolved. The next bounded question is:

> May the monitor decrement a successful payment, paid session, sale, buyer, revenue, or cash figure when `charge.dispute.created` arrives?

Exact candidate:

- Provider: Stripe
- Surface: API v1 Events and Disputes
- Trigger: `charge.dispute.created`; `data.object` is a Dispute
- Corroborating lifecycle events: `charge.dispute.funds_withdrawn`, `charge.dispute.funds_reinstated`, `charge.dispute.closed`, and `charge.dispute.updated`
- Object fields: Dispute `id`, `amount`, `currency`, `charge`, `payment_intent`, `status`, `balance_transactions`, and `evidence_details`
- Effective account or event-destination API version: `UNKNOWN_UNTIL_AUTHORIZED_READBACK`
- Queue source: https://github.com/TTaoGaming/hfo-gen-133/issues/5

No matching prior S08 card on `charge.dispute.created` versus balance movement and paid-history semantics was found before this write.

## Primary/current evidence accessed 2026-08-05

1. Stripe defines `charge.dispute.created` as occurring when a customer disputes a charge. It separately defines `charge.dispute.funds_withdrawn` for funds removed from the account, `charge.dispute.funds_reinstated` for funds returned after closure, and `charge.dispute.closed` for terminal `lost`, `warning_closed`, or `won` state.  
   https://docs.stripe.com/api/events/types
2. A Dispute has its own unique ID, amount, currency, Charge or PaymentIntent binding, status, and zero, one, or two balance transactions showing funds withdrawn and reinstated. The disputed amount can be partial and can differ from the original Charge amount.  
   https://docs.stripe.com/api/disputes/object
3. Stripe documents that one payment can receive more than one dispute and instructs API consumers to distinguish them by Dispute ID.  
   https://docs.stripe.com/disputes/api
4. Stripe documents dispute states including `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `won`, and `lost`. A won dispute can restore the chargeback amount; a lost dispute makes the disputed amount permanent. Dispute fees can remain even when the chargeback amount is returned.  
   https://docs.stripe.com/disputes/responding
5. Stripe webhook delivery can retry, duplicate, and arrive out of order. Event objects are version-bound when created; consumers must not infer lifecycle state from delivery order or count alone.  
   https://docs.stripe.com/webhooks

## Supported claims

- `charge.dispute.created` proves that one Dispute object was created for a payment; it does not by itself prove that funds moved at that moment.
- Stripe exposes separate events for dispute creation, funds withdrawal, funds reinstatement, updates, and closure. Therefore those concepts must not be collapsed into one counter transition.
- A dispute can cover only part of a payment, and one payment can have multiple distinct disputes. One dispute event is not one lost order, buyer, or full payment.
- Dispute status is nonterminal until closure. `needs_response` or `under_review` is not `lost`; `won` can later restore the chargeback amount.
- Historical payment evidence remains true after a dispute begins. A successful Charge or paid Checkout Session occurred even if a later dispute changes financial outcome.
- Balance impact must be reconciled from the Dispute's exact balance transactions or the dedicated funds-withdrawn and funds-reinstated lifecycle, deduplicated by account context plus Dispute ID and BalanceTransaction ID.
- Privacy-safe monitoring can retain currency-bucketed aggregate disputed amount by typed state without persisting customer identity, evidence, reason text, payment method, address, email, or free-form metadata.

## Excluded claims and unknowns

- Dispute creation count is not unique buyers, dissatisfied buyers, churn, fraud rate, product-market fit, demand, lost orders, or lost revenue.
- `charge.dispute.created` is not bank-settled cash movement, recognized revenue reversal, profit reduction, tax treatment, or proof the cardholder received funds at that exact time.
- A `won` status or funds-reinstated event does not prove all dispute fees were returned; Stripe documents that fees can remain depending on contract and geography.
- This card does not establish Connect transfer reversal, application-fee impact, reserve behavior, cross-border currency conversion, tax reversal, accounting recognition, or payout settlement.
- This card does not establish exact event timing for every payment method or historical API version.
- No Gen-133 Stripe account, dispute, payment, buyer, revenue, or private payload was observed.

## Required revision gate

1. Preserve historical successful-payment and paid-session counts. Never decrement them because `charge.dispute.created`, `charge.dispute.funds_withdrawn`, or `charge.dispute.closed` arrives.
2. Add a separate dispute state machine keyed by Stripe account context plus Dispute ID and bound to the exact Charge or PaymentIntent.
3. Treat `charge.dispute.created` only as `DISPUTE_OPENED_AMOUNT` under its current status. Do not classify it as withdrawn funds, lost revenue, or lost buyer.
4. Record Stripe-balance movement only from exact balance-transaction transitions or the dedicated funds events, with BalanceTransaction-ID deduplication and currency separation.
5. Treat status independently:
   - `warning_needs_response`, `warning_under_review`, `needs_response`, or `under_review` -> open/nonterminal dispute state;
   - `won` -> terminal won state, but funds restoration and fee treatment remain separately reconciled;
   - `lost` -> terminal lost state, but label the amount `DISPUTE_LOST_AMOUNT`, not revenue, profit, or buyer loss;
   - `warning_closed` -> terminal warning/inquiry closure, kept separate from ordinary won/lost disputes.
6. Support multiple disputes per payment and partial disputed amounts. Never derive a one-payment or one-buyer decrement from Dispute count.
7. Deduplicate webhook delivery by Event ID and commercial state by Dispute ID; tolerate duplicate Event objects, retries, manual resends, and out-of-order creation, funds, update, and closure events.
8. Preserve separate aggregates for disputed-open amount, withdrawn amount, reinstated amount, won amount, lost amount, and dispute fees where exact typed evidence exists.
9. Do not call any arithmetic result net revenue, profit, bank-settled cash, sales, or buyers. If a balance-oriented aggregate is required, label it `STRIPE_BALANCE_DISPUTE_ACTIVITY_NET` and keep it separate from payment and refund history.
10. Persist only aggregate values plus rule and provenance digests. Raw Dispute evidence, reason details, customer data, Charge or PaymentIntent payloads, and free-form metadata are prohibited from Git, Slack, prompts, traces, and general agent logs.

Required classification:

`CHARGE_DISPUTE_CREATED_IS_LIFECYCLE_TRIGGER; FUNDS_EVENTS_OR_BALANCE_TRANSACTIONS_CONTROL_BALANCE_ADJUSTMENT; DISPUTE_STATUS_CONTROLS_OUTCOME; PAID_EVENT_HISTORY_IS_NOT_DECREMENTED`

## License, terms, privacy, and version uncertainty

- No software-license conclusion is required to reference the public API contract.
- Stripe service terms, account authorization, event-destination ownership, restricted-key scope, retention obligations, effective API version, Connect topology, fee contract, and accounting treatment remain unstood by public docs.
- Dispute objects and evidence can contain sensitive financial and customer data. Future execution requires a separately authorized WorkItem with least privilege, signature verification, aggregate-only retention, and no raw payload export.

## Strongest objection

A business may reasonably want a conservative cash-risk figure as soon as a dispute opens. That operational need does not justify rewriting history or pretending that dispute creation equals a completed balance withdrawal or final loss. The correct conservative measure is a separate `OPEN_DISPUTE_EXPOSURE_AMOUNT`, while actual Stripe-balance movement and final outcome remain independently reconciled.

## Falsifier

`REVISE` may become `ADMIT` only after a distinct Stripe-sandbox verifier replays an exact implementation against:

- one full-amount dispute;
- one partial dispute;
- two distinct disputes against one payment;
- creation before funds withdrawal;
- funds withdrawal before or after other delivered events;
- a won dispute with funds reinstatement;
- a lost dispute with no reinstatement;
- warning or inquiry statuses where supported;
- duplicate and manually resent events;
- out-of-order `created`, funds, update, and closed events;
- replay from empty state producing identical aggregates;
- zero decrement of historical paid-event and paid-session counts;
- aggregate-only persistence with no prohibited fields.

Change to `RETIRE` for this monitor lane if exact account/version binding, Dispute-ID lifecycle state, balance-transaction deduplication, deterministic replay, or raw-payload exclusion cannot be proved.

## Verifier, consumer, expiry, and cost

- Verifier: `DISTINCT_STRIPE_SANDBOX_DISPUTE_LIFECYCLE_AND_BALANCE_REPLAY_VERIFIER`.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_STRIPE_DISPUTE_LIFECYCLE_SEMANTICS_GATE_001`.
- Required ConsumerAck: exact card commit/blob, implementation and fixture digests, account/version boundary, classification-rule digest, and explicit acknowledgment that buyers, demand, recognized revenue, profit, and bank-settled cash remain unknown.
- Expiry: `2026-08-12T17:28:45Z`, or earlier if Stripe materially changes the named event, status, or balance-transaction contract.
- This research pass: `$0` spend; `0` operator minutes; `0` Stripe requests.
- Producer revision: `25–50` minutes.
- Sandbox lifecycle and replay verification: `45–90` minutes.
- Any later live authorization, scope, version, and fee-contract review: `10–20` operator minutes under a separate approved WorkItem.
- Provider quota and commercial cost: `UNKNOWN`.

## Decision

`REVISE`

A dispute is a separate status-bearing lifecycle. `charge.dispute.created` is not permission to decrement a successful payment, paid session, sale, buyer, revenue, or cash figure.