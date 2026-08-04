---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
question_id: EXTERNAL_SIGNAL_MONITOR_STRIPE_TRANSACTION_EVENT_SEMANTICS_AND_CREDENTIAL_GATE_001
valid_time_utc: 2026-08-04T05:29:00Z
expiry_utc: 2026-08-11T05:29:00Z
decision: REVISE
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
---

# S08 evidence card — Stripe charge count is a transaction signal, not a buyer count

## Self-probe

- Identity: `S08 Research and Candidate Scout`; expected and observed task ID match.
- Tools available/used: authenticated GitHub search/read/write, public web research, Slack connector after Git readback.
- Prohibited or unused: Stripe API calls, credential access, account creation, terms acceptance, private-data access, outreach, purchase, send, spend, deployment, merge, publication, or task mutation.

## Changed bounded uncertainty

Gen-133 issue `#5` names an optional Stripe lane that reports read-only charge counts but remains disabled when no API key is present. The unresolved question is whether a monitor may interpret `GET /v1/charges` cardinality as buyer evidence and what minimum credential/data boundary is required.

Exact candidate:

- Provider: Stripe
- API namespace and endpoint: API v1, `GET /v1/charges`
- Current documented API version observed: `2026-07-29.dahlia`
- Candidate use: append-only aggregate external-signal observation for one explicitly bound Stripe account context

## Primary/current evidence, accessed 2026-08-04

1. Stripe API versioning states that the current API version is `2026-07-29.dahlia`; requests otherwise use the account default unless the `Stripe-Version` header is pinned.  
   https://docs.stripe.com/api/versioning?lang=curl
2. `GET /v1/charges` returns previously created Charge objects, newest first, with cursor pagination, a maximum page size of 100, and optional creation-time bounds. Charge fields include `status`, `paid`, `captured`, `amount`, `amount_refunded`, `refunded`, `disputed`, `customer`, `payment_intent`, and `livemode`.  
   https://docs.stripe.com/api/charges/list?lang=curl
3. Stripe requires secret server-side credentials for protected API access and recommends restricted keys, least privilege, vault-backed storage, rotation, audit logs, and optional source-network restrictions.  
   https://docs.stripe.com/keys-best-practices
4. Stripe describes a PaymentIntent as typically corresponding to one cart or customer session; its lifecycle can include authentication and payment attempts. Stripe now recommends Checkout Sessions for most new payment integrations, but that does not change the semantics of historical Charge objects returned by the charge-list endpoint.  
   https://docs.stripe.com/payments/payment-intents

## Supported claims

- A processor with an already-authorized server-side credential can request a time-bounded, paginated list of Charge objects for the credential's account context.
- A deterministic monitor can classify returned objects without persisting buyer identity by retaining only window bounds, aggregate cardinalities, currency-bucketed sums, typed errors, request-version metadata, and a digest of the classification rule.
- `status=succeeded`, `paid=true`, and `livemode=true` identify stronger transactional evidence than raw list length. Refund, dispute, capture, and amount fields allow separate gross-event classifications.
- A restricted read-only key is safer than an unrestricted secret key, but the effective permission set must be verified outside source code and logs.

## Excluded claims

- **Raw Charge count is not unique-buyer count.** One customer can create multiple charges, and `customer` may be null.
- **Raw Charge count is not successful-sale count.** The endpoint is a list of created Charge objects; classification must inspect status and payment fields.
- **Successful Charge count is not net revenue.** Refunds, disputes, Stripe fees, taxes, currency conversion, transfers, and payout settlement are separate concerns.
- **Charge or PaymentIntent count is not demand, conversion, product-market fit, or willingness to pay.** It is transactional evidence only after an artifact/order binding exists.
- **Missing key, unauthorized account context, empty page, rate limit, or pagination failure is not zero sales.** Record a typed unknown or partial observation.
- This card does not establish totals across Stripe organizations, Connect platforms, connected accounts, or multiple merchant accounts.

## Required revision gate

1. Rename the metric from `buyer_count` or generic `charge_count` to `successful_transaction_events` and keep `unique_buyers=UNKNOWN` unless a separately approved privacy-safe deduplication method exists.
2. Pin `Stripe-Version: 2026-07-29.dahlia`, explicit UTC `created.gte/lt` bounds, `limit=100`, and deterministic cursor traversal. Record truncation or cursor failure as `PARTIAL_UNKNOWN`.
3. Use only an already-authorized restricted live-mode key with read access limited to the minimum required resource; keep it in a secrets vault, never Git/Slack/log output. No key creation or permission expansion is authorized by this card.
4. Bind one exact Stripe account context and one artifact/order namespace. Reject unbound, organization-wide, or connected-account aggregation.
5. Classify at minimum: `succeeded_paid`, `fully_refunded`, `partially_refunded`, `disputed`, `failed_or_unpaid`, and `non_live`. Do not collapse them into one count.
6. Persist aggregates only. Do not persist Charge IDs, customer IDs, emails, names, addresses, payment-method details, receipt URLs, descriptions, or metadata.
7. Keep `gross_captured_amount` and refund amounts separate; label all currency-specific values. Do not publish a net-revenue claim from this endpoint.
8. Fail closed on credential, scope, version, account-context, pagination, or retention uncertainty.

## License / terms / privacy uncertainty

- No software-license issue is asserted for calling the API, but Stripe service terms, merchant-account authorization, effective restricted-key permissions, account ownership, retention obligations, and cross-account context are not stood by public documentation alone.
- Live Charge records are private financial/customer data. This S08 run did not access them. Any future execution requires a separately authorized WorkItem and processor identity with explicit aggregate-only retention.

## Strongest objection

Even aggregate metrics are derived from private financial data. Adding a live Stripe key to a broad agent runtime creates a higher-value failure mode than the external-signal benefit justifies unless the key is isolated, read-only, account-bound, vault-supplied, non-exportable, and the processor proves that raw objects never enter Git, Slack, prompts, traces, or durable logs.

## Falsifier

`REVISE` becomes `RETIRE` for this monitor lane if a distinct verifier shows any of the following under an already-authorized sandbox fixture plus separately approved live schema check: read-only Charge access cannot be narrowly restricted; cursor-complete counting cannot be made deterministic; the processor emits or persists prohibited fields; account context cannot be unambiguously bound; or a raw/private payload enters shared agent traces.

`REVISE` may become `ADMIT` only after a held-out replay proves exact window/cursor coverage, aggregate-only persistence, typed unknowns, version pinning, secret non-disclosure, and a consumer binds the metric strictly as transaction events rather than buyers or net revenue.

## Verifier and consumer

- Verifier: distinct nonproducer security/privacy verifier with Stripe sandbox capability; any live-mode check requires explicit operator authorization and aggregate-only readback.
- Consumer: `EXTERNAL_SIGNAL_MONITOR_STRIPE_TRANSACTION_EVENT_SEMANTICS_AND_CREDENTIAL_GATE_001`.
- Required ConsumerAck: exact card commit/blob, classification-rule digest, account-context binding, secret-handling evidence, and explicit statement that `unique_buyers`, `net_revenue`, and `demand` remain unknown.

## Cost and operator-minute estimate

- This research run: `$0` spend; `0` operator minutes; no Stripe request.
- Producer revision: `25–50` minutes.
- Sandbox fixture and deterministic pagination verifier: `20–40` minutes.
- Operator authorization/read-only key review for a future live run: `10–20` minutes, only if an existing Stripe account and approved credential path already exist.
- Provider request cost and any account-specific commercial terms: `UNKNOWN`; do not claim zero marginal cost from this card.

## Decision

`REVISE`

The optional lane is technically viable only as an account-bound, aggregate-only **successful transaction event** monitor. It must not report buyer count, demand, conversion, or net revenue, and it remains non-executable until credential, privacy, account-context, and retention gates are explicitly owned by a WorkItem.
