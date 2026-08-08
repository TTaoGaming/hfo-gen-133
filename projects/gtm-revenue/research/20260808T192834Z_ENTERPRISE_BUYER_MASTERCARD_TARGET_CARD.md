# S08 GTM Target Card — Mastercard — Agent Pay / Agent Pay for Machines

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
result: READY
seat: S08_GTM_TARGET_SCOUT
wip: 1
valid_time_utc: 2026-08-08T19:28:34Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
campaign_packet: projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md
campaign_packet_expiry_utc: 2026-08-14T14:08:00Z

self_probe:
  expected_task_id: 6a526109ba348191b5f23ad3172ad568
  observed_task_id: 6a526109ba348191b5f23ad3172ad568
  task_id_match: true
  task_enabled: true
  github_read_available: true
  github_write_available: true
  public_web_research_available: true
  slack_pointer_send_available: true
  task_inventory_read_available: true
  task_mutation_performed: false

target:
  company: Mastercard
  target: Agent Pay / Agent Pay for Machines partner-integration and trust-control surface
  species: ENTERPRISE_BUYER
  vertical: payments / agentic commerce / autonomous machine payments
  route: RELATIONSHIP_ONLY
  current_signal: >-
    Mastercard launched Agent Pay for Machines on 2026-06-10 with more than thirty initial
    industry participants. The service is designed for permissioned, orchestrated, machine-speed
    transactions and explicitly includes credentialing, Verifiable Intent, programmatically
    enforced authorization rules and spending limits, plus settlement across cards, accounts,
    and stablecoins. Mastercard also reported live agentic-payment production activity in Europe
    on 2026-06-02 and describes live Agent Pay activity across Asia Pacific and beyond.
  best_persona: >-
    Product, security, platform, or partner-integration owner responsible for taking an Agent Pay
    or Agent Pay for Machines ecosystem change from partner implementation through evidence-backed
    production acceptance. The practical artifact user is an engineer, security reviewer, or
    partner-certification reviewer who must determine whether a change preserves delegated intent,
    authority, transaction controls, and audit evidence.
  public_bridge_person: >-
    Jorn Lambert — Mastercard Chief Product Officer, directly quoted in Mastercard's 2026-06-10
    Agent Pay for Machines launch. This is a public product bridge only; this card does not establish
    procurement authority, consulting ownership, willingness to engage, or responsibility for a
    specific partner certification workflow.

pain_hypothesis:
  status: HYPOTHESIS_NOT_COMPANY_FACT
  statement: >-
    As Mastercard expands Agent Pay for Machines across many partners, payment types, and machine-
    driven use cases, product/integration teams may incur material review and promotion cycle time
    when each partner or control-plane revision must prove that the exact deployed change still
    binds agent identity, authenticated user or business intent, programmatic permissions and spend
    limits, rail-specific transaction behavior, trace/audit evidence, and safe rollback or dispute
    handling. Public evidence proves these control dimensions matter; it does NOT prove Mastercard
    has a slow certification process, missing controls, excess reviewer headcount, or an unmet
    external-services need.
  measurable_value_metric: >-
    Engineering/reviewer hours from a proposed Agent Pay partner or policy revision to
    evidence-backed production acceptance, with elapsed integration-certification cycle time as
    the primary metric. No current Mastercard baseline or savings figure is asserted.

hypothesis_evidence:
  for:
    - >-
      Mastercard says Agent Pay for Machines launched with more than thirty industry participants
      and is intended to support high-frequency, low-latency, multi-provider machine transactions.
      That creates a plausible repeatability surface for partner-change acceptance, though scale
      alone is not evidence of pain.
    - >-
      Mastercard explicitly requires credentialing, Verifiable Intent, permissioning, authorization
      rules, spending limits, interoperability, reliability, and governance. Those dimensions map
      directly to a version-bound change-acceptance contract rather than a generic AI checklist.
    - >-
      Mastercard says Verifiable Intent should ground agent actions in explicit user permissions
      and preferences with a clear auditable record across the ecosystem, making evidence binding
      and provenance first-order product concerns.
  against:
    - >-
      Mastercard already exposes mature primitives for registered/traceable agents, network-token
      governance, Verifiable Intent, explicit consent, authorization controls, and multi-rail
      settlement, so a generic policy or identity layer would likely be redundant.
    - >-
      Mastercard has already completed live agentic transactions in production with banks and
      payment partners, which is direct counterevidence against assuming that production acceptance
      is immature or blocked.
    - >-
      The 2026-06-10 launch names specialist partners contributing transaction-level risk,
      Know Your Agent verification, traceability, policy control, and secure wallets. Those ecosystem
      capabilities may already cover the exact evidence-normalization seam hypothesized here.

proof_kit:
  two_minute_utility_gift: >-
    "Agentic Payment Partner Change Acceptance Diff — Agent × Intent × Permission × Rail × Evidence":
    a one-page before/after matrix for one hypothetical partner revision showing agent credential
    and principal, authenticated/verifiable intent, allowed transaction classes, spend/velocity
    ceilings, payment rail, required approval or step-up, trace/evidence pointers, replay/revocation
    checks, dispute/rollback trigger, and GO/HOLD verdict. It should be useful as a review aid even
    if Mastercard already has deeper internal certification infrastructure.
  deeper_proof_artifact: >-
    Public-safe synthetic partner-conformance harness using fake agents, fake merchants, mock cards/
    accounts/stablecoins, an OPA/Rego-style authorization oracle, multi-rail transaction stubs, and
    held-out negative controls for forged or stale intent, budget violation, cross-partner identity
    confusion, replay, revoked authority, rail mismatch, missing trace evidence, and rollback/dispute
    failure. Bind every verdict to an exact synthetic revision and evidence manifest. Use no
    Mastercard account, credentials, proprietary APIs, partner systems, customer data, or private
    payment information.

work_item:
  id: S07_MASTERCARD_AGENTIC_PAYMENT_PARTNER_ACCEPTANCE_DIFF_V1
  state: READY_FOR_ADMISSION
  next_consumer: S07_GTM_PROOF_KIT_BUILDER
  next_consumer_task_id: 6a506f6dc5c08191b95f1707d7f00c2d
  acceptance: >-
    Produce exactly one public-safe two-minute Agentic Payment Partner Change Acceptance Diff
    grounded in Mastercard's current Agent Pay / Agent Pay for Machines public controls. Keep the
    pain explicitly hypothetical and do not imply Mastercard lacks identity, intent, authorization,
    tokenization, auditability, or production deployment capability. If current Mastercard material
    exposes an equivalent low-overhead revision-bound acceptance record, return HOLD/kill rather
    than duplicate it.

strongest_falsifier: >-
  Kill this wedge if Mastercard already provides partner teams a low-overhead, versioned acceptance
  mechanism that binds the exact Agent Pay/AP4M revision to agent identity, Verifiable Intent,
  permission/spend policy, rail behavior, held-out negative tests, audit evidence, dispute/rollback
  conditions, and production promotion. Also kill it if partner certification is not a material
  engineering/reviewer cost surface or is intentionally handled entirely by existing Mastercard
  and ecosystem tooling.

privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
effect_ceiling: T0_PREP_RESEARCH_GIT
verifier:
  primary: S04_HRIST_STRUCTURAL_PREFLIGHT
  task_id: 6a52861fbdb08191b9ef33a0b9c3c15c
  same_provider_binding_weight: 0
  independent_followup_required_before_external_claim: true
expiry_utc: 2026-08-14T14:08:00Z

honest_flaw: >-
  Mastercard is a technically strong target precisely because it already appears highly mature in
  agent identity, verifiable intent, authorization, tokenization, auditability, and production
  agentic payments. Public evidence establishes scale, strategic priority, and a plausible
  integration-review cost surface; it does not establish a backlog, buyer, budget, consulting gap,
  or willingness to adopt an external acceptance tool. The proposed artifact has value only if it
  reveals a concrete revision-to-evidence normalization gap rather than repackaging Mastercard's
  existing controls.

evidence_digest_contract:
  canonicalizer: UTF8_LF_EXACT_BLOCK_V1
  canonicalization_rule: >-
    SHA-256 over the exact UTF-8 bytes between BEGIN_EVIDENCE_PREIMAGE_V1 and
    END_EVIDENCE_PREIMAGE_V1, excluding both marker lines, after CRLF-to-LF normalization,
    with no BOM and exactly one trailing LF after the final source line. No trimming,
    field sorting, URL rewriting, or case folding is permitted.
  evidence_preimage_utf8_bytes: 1647
  evidence_digest_sha256: 27eda5467f01017e5894bd94101655b03dcccf30850874478cb38259b13311f8
```

## Primary/current sources

1. **Mastercard — Agent Pay for Machines launch** — **2026-06-10**; observed **2026-08-08**: https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
2. **Mastercard — Greg Ulrich, Chief AI and Data Officer, on trusted agentic commerce** — **2026-05-26**; observed **2026-08-08**: https://www.mastercard.com/us/en/news-and-trends/stories/2026/mastercard-agentic-commerce-vision.html
3. **Mastercard — Worldline, ING and Mastercard live end-to-end European agentic payment in production** — **2026-06-02**; observed **2026-08-08**: https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2026/worldline-ing-and-mastercard-complete-a-live-end-to-end-european-agentic-payment-in-production/
4. **Mastercard — Agent Pay product surface** — publication date not exposed; observed **2026-08-08**: https://www.mastercard.com/us/en/business/artificial-intelligence/mastercard-agent-pay.html

## Recomputable evidence preimage

BEGIN_EVIDENCE_PREIMAGE_V1
source_1|observed_utc_date=2026-08-08|source_date=2026-06-10|url=https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html|supports=Agent_Pay_for_Machines_launch;30_plus_initial_industry_participants;permissioned_orchestrated_machine_speed_settlement;credentialing;Verifiable_Intent;programmatic_authorization_rules;spending_limits;multi_rail_settlement;Jorn_Lambert_Chief_Product_Officer
source_2|observed_utc_date=2026-08-08|source_date=2026-05-26|url=https://www.mastercard.com/us/en/news-and-trends/stories/2026/mastercard-agentic-commerce-vision.html|supports=Greg_Ulrich_Chief_AI_and_Data_Officer;live_agentic_transactions_in_Asia_Pacific_and_beyond;trust_as_defining_constraint;Verifiable_Intent_explicit_permissions_and_preferences;clear_auditable_record_across_ecosystem
source_3|observed_utc_date=2026-08-08|source_date=2026-06-02|url=https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2026/worldline-ing-and-mastercard-complete-a-live-end-to-end-european-agentic-payment-in-production/|supports=live_end_to_end_agentic_payment_in_production;ING_cardholder_and_merchant;existing_authentication_and_authorisation_infrastructure;pan_European_acceptance_acquiring_authentication_issuer_processing
source_4|observed_utc_date=2026-08-08|source_date=NO_PUBLISH_DATE_EXPOSED|url=https://www.mastercard.com/us/en/business/artificial-intelligence/mastercard-agent-pay.html|supports=registered_agents_governed_and_traceable_with_network_tokens;verifiable_intent;explicit_consent;Agent_Pay_for_Machines;secure_initiate_authenticate_complete_payments_for_users_and_businesses
END_EVIDENCE_PREIMAGE_V1

## No-effect receipt

No outreach, application, email/DM, account creation, terms acceptance, purchase, paid call,
deployment, merge, publication outside the operator-controlled repository, private-data use,
credential use, demand claim, or autonomous negotiation was performed.
