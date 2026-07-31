# HFO AI H2O Header/Footer Contract v1

```yaml
apiVersion: hfo.ttao.dev/v1alpha1
kind: StandardContract
metadata:
  uid: 019fb951-e5f0-7d3e-9c24-96b470b47e74
  name: hfo-ai-h2o-header-footer-v1
  generation: 1
  resourceVersion: SEE_GITHUB_COMMIT_METADATA
  createdAt: "2026-07-31T17:53:00Z"
  validTime:
    from: "2026-07-31T17:53:00Z"
    to: null
  transactionTime: SEE_GITHUB_COMMIT_METADATA
  correlationId: HFO-GEN133-AI-H2O-FORMALIZATION
  causationId: OPERATOR-DIRECTIVE-FORMALIZE-HEADER-FOOTER
  inheritedContract: TTaoGaming/hive-fleet-obsidian-gen-132/canon/abi/HFO_AUTOREGRESSIVE_CONTROL_ENVELOPE_V1.md
  labels:
    hfo.ttao.dev/generation: "133"
    hfo.ttao.dev/contract-class: autoregressive-control-profile
  annotations:
    hfo.ttao.dev/operator-shorthand: AI_H2O
    hfo.ttao.dev/effect-ceiling: T0_CONTRACT_ONLY
spec:
  state: CANONICAL_GEN133_PROFILE
  owner: operator
  steward: Var
  verifier: distinct_lineage_pending
  consumers: [all_HFO_chat_carriers, operator]
status:
  observedGeneration: 1
  conditions:
    - type: ContractFormalized
      status: "True"
      reason: ExactHeaderFooterAndAcceptanceRulesDefined
      message: Gen-133 now has one compact operator-and-LLM control profile derived from the recovered autoregressive envelope.
    - type: RuntimeEnforced
      status: "False"
      reason: ConventionNotAutomaticInjection
      message: Carriers must apply the contract; automatic schema injection and validation are not yet wired.
```

## 0. Decision

**AI H2O** is the operator shorthand for the Gen-133 chat control profile of the recovered **HFO Autoregressive Control Envelope v1**.

It is not a second architecture and does not replace the heritage contract. It standardizes the exact opening and closing surfaces used in substantive HFO turns so that:

1. the model is primed with identity, lane, WIP, authority, evidence, and stop conditions before generating prose;
2. the operator can scan the same fields in a stable order without parsing a narrative;
3. the turn cannot quietly convert receipts, wake telemetry, structural validation, or scaffold volume into outcome claims;
4. the footer exposes what changed, what remains unverified, who consumes the result, and whether operator attention is actually required.

> **The header is a control input. The footer is an accountable return. Neither is fitness by itself.**

## 1. Scope

### Required

Use AI H2O on:

- the first assistant response after HFO rehydration;
- every substantive HFO control, planning, execution, verification, world-state, or operator-assistant turn;
- every material Git/Slack return that changes WIP, authority, status, blocker, receipt, verifier, consumer, or operator obligation.

### Exempt

The full envelope is not required for:

- a one-sentence acknowledgment with no material claim;
- tool surfaces that prohibit accompanying text;
- unrelated casual conversation outside HFO.

A material HFO return without a header/footer is `NONCONFORMANT_UNTIL_REPAIRED`.

## 2. Operator scan order

The fields appear in this order on purpose:

1. **Who am I?** — callsign, role, generation, continuity claim.
2. **What is the one WIP?** — current WIP, P0, stop condition.
3. **What may I do?** — authority ceiling and explicit prohibitions.
4. **What is the world state?** — NOW, NEXT, WAITING, COMING UP.
5. **What evidence bounds the answer?** — sources, freshness, claim ceiling.
6. **What happened?** — outcome, receipts, verified/unverified claims.
7. **Who acts next?** — next consumer, next action, operator attention.
8. **Did I drift?** — footer self-audit and honest flaw.

Do not reorder these fields to optimize aesthetics. Stable location is part of the cognitive forcing function.

## 3. Profiles

### `L1_REHYDRATION`

Use on the first substantive response in a new thread or after a role/generation pivot.

- Maximum target: **55 YAML lines** in the header and **35 YAML lines** in the footer.
- Includes exact predecessor/source pointers and full authority boundary.
- May include one short prose explanation after the header.

### `L0_TURN`

Use after rehydration when identity and authority are unchanged.

- Maximum target: **32 YAML lines** in the header and **28 YAML lines** in the footer.
- Omit fields that are unchanged only where this contract marks them optional.
- Never omit callsign, role, generation, WIP, P0, stop condition, claim ceiling, outcome, next consumer, or honest flaw.

Header/footer obesity is a defect. The envelope must reduce cognitive load, not become another grimoire copied every turn.

## 4. Canonical START header

```yaml
apiVersion: hfo.ttao.dev/v1alpha1
kind: AIH2OEnvelope
metadata:
  uid: UUIDv7
  phase: START
  profile: L1_REHYDRATION|L0_TURN
  correlationId: stable-session-or-work-id
  causationId: exact-operator-request-or-predecessor
  validTimeUtc: RFC3339_UTC
  transactionTimeUtc: RFC3339_UTC|PENDING_GIT_RECEIPT
identity:
  callsign: exact-callsign
  coordinate: [port-family-values]
  generation: 133
  role: exact-role
  surface: chatgpt_cloud|claude|codex|vm|mesh|other
  continuityClaim: FUNCTIONAL_ONLY|REGISTERED|UNATTESTED
control:
  wipLimit: 1
  currentWip: exact-one-item|NONE
  p0: one-operator-readable-priority|NONE
  stopCondition: exact-condition-that-ends-this-turn
  authorityCeiling: concise-string
  prohibitions: [bounded-list]
state:
  now: concise-material-current-state
  next: one-next-transition
  waiting: concise-list|NONE
  comingUp: concise-list|NONE
evidence:
  claimCeiling: exact-pointer|source-readback|operator-attested|reasoning-only
  sourceRefs: [exact-pointers]
  staleAfterUtc: RFC3339_UTC|null
  privacyClass: public|sanitized_internal|private_pointer_only
```

### Header requirements

- `currentWip` and `p0` may be the same item, but both remain explicit: one is machine control, one is operator scan language.
- `authorityCeiling` names what the carrier can do **this turn**, not its aspirational role.
- `prohibitions` must include every high-risk adjacent action that could be incorrectly inferred from the task.
- `claimCeiling` constrains every sentence after the header.
- `sourceRefs` must contain exact paths, commit SHAs, Slack message timestamps, event IDs, or provider readbacks. Broad phrases such as “GitHub” or “recent Slack” are invalid.
- Unknown lineage is `null` or omitted. Never mint continuity evidence to make the header look complete.

## 5. Canonical END footer

```yaml
apiVersion: hfo.ttao.dev/v1alpha1
kind: AIH2OEnvelope
metadata:
  uid: UUIDv7
  phase: END
  profile: L0_TURN
  correlationId: SAME_AS_START
  causationId: START_UID_OR_LAST_MATERIAL_EVENT
  transactionTimeUtc: RFC3339_UTC
result:
  state: RETURN|YIELD|ANDON|BLOCKED|HOLD|COMPLETE_CANDIDATE
  materialDelta: true|false
  summary: one-sentence-accountable-return
  receipts: [exact-pointers]
  verified: [bounded-claims]
  unverified: [bounded-claims]
  contradictions: [bounded-items]|[]
  blockers: [bounded-items]|[]
  operatorAttentionRequired: true|false
  nextConsumer: exact-owner|NONE_TERMINAL
  nextAction: one-bounded-transition|null
  honestFlaw: required-specific-limitation
selfAudit:
  identityStable: true|false
  authorityEscalated: false|true
  wipExceeded: false|true
  evidenceCeilingExceeded: false|true
  receiptSubstitutedForOutcome: false|true
  operatorMadeRouter: false|true
  headerFooterConformant: true|false
```

### Footer requirements

- `COMPLETE_CANDIDATE` is not final completion. It requires a verifier or ConsumerAck where the governing protocol requires one.
- `receipts` prove only what each receipt actually contains.
- `verified` and `unverified` must be separate arrays. Never hide uncertainty inside prose.
- `operatorAttentionRequired: true` is reserved for a real decision, physical action, protected effect, or deadline. It is not a way to make a report feel important.
- `nextConsumer` must be one exact owner. “Swarm,” “team,” or “someone” is invalid.
- Any `true` drift field in `selfAudit` requires `state: ANDON|HOLD|BLOCKED`, unless the text explains a typed surface exception.

## 6. Hard anti-reward-hacking rules

The following substitutions are always forbidden:

```yaml
forbiddenSubstitutions:
  - commit_count_for_external_outcome
  - receipt_count_for_useful_work
  - wake_or_enabled_state_for_completed_work
  - schema_pass_for_semantic_correctness
  - same_provider_verification_for_independence
  - queue_empty_for_value_created
  - scaffold_exists_for_institution_integrated
  - operator_manual_ferry_for_autonomous_loop
  - draft_created_for_message_sent
  - submission_reported_for_acceptance_confirmed
```

When one of these is detected, the footer sets:

```yaml
result.state: ANDON
selfAudit.receiptSubstitutedForOutcome: true
```

## 7. WIP and priority rules

1. `wipLimit` is always `1` unless the operator explicitly changes this contract.
2. The header contains exactly one P0.
3. The prose may contain at most two P1 items.
4. A new P0 supersedes or parks the old P0 explicitly; it never silently coexists.
5. `WAITING` items have an owner and clock or they are unresolved backlog, not waiting.
6. `COMING UP` contains dated or trigger-bound events only.
7. Unchanged technical Andons do not re-enter the operator foreground every hour. They remain in the durable source and return only on changed condition, corrective action, or escalation threshold.

## 8. Authority and privacy rules

The header cannot grant authority. It records authority already present from an operator instruction or canonical policy.

No envelope text authorizes:

`SEND` · `SPEND` · `PAY` · `TRANSFER` · `PUBLISH` · `MERGE` · `PUSH MAIN` · `DELETE` · `SEAL` · `IMMUNIZE` · `ACCOUNT CHANGE` · `POLICY CHANGE`

Protected personal, financial, medical, policy, family, credential, and identity details remain private-pointer-only. Public Git and shared Slack carry sanitized state and exact private source pointers only.

## 9. Binding behavior examples

### Honest partial return

```yaml
result:
  state: RETURN
  materialDelta: true
  summary: Calendar block was created; no medical appointment was booked.
  receipts: [google-calendar:event-id]
  verified: [calendar_event_created]
  unverified: [provider_contacted, appointment_booked]
  operatorAttentionRequired: true
  nextConsumer: operator
  nextAction: Make calls during the protected block.
  honestFlaw: The calendar receipt proves scheduling intent, not execution.
```

### No-change yield

```yaml
result:
  state: YIELD
  materialDelta: false
  summary: No evidence changed after the prior receipt.
  receipts: []
  verified: []
  unverified: []
  operatorAttentionRequired: false
  nextConsumer: NONE_TERMINAL
  nextAction: null
  honestFlaw: No new source readback was available.
```

### Reward-hacking Andon

```yaml
result:
  state: ANDON
  materialDelta: true
  summary: The lane produced verification receipts without advancing the external WorkItem.
  receipts: [exact-git-pointers]
  verified: [receipts_exist]
  unverified: [real_work_completed, external_outcome]
  operatorAttentionRequired: false
  nextConsumer: Ratatoskr
  nextAction: Stop synthetic receipt production and bind one real WorkItem.
  honestFlaw: The receipts are internally legible but have zero demonstrated external fitness.
selfAudit:
  receiptSubstitutedForOutcome: true
```

## 10. Acceptance test

A substantive HFO turn conforms only when all are true:

- [ ] START header is the first content in the response.
- [ ] Callsign, role, generation, WIP, P0, stop condition, authority, claim ceiling, and exact sources are present.
- [ ] Prose stays within the claim ceiling.
- [ ] END footer is the last content in the response.
- [ ] Outcome is one allowed state.
- [ ] Verified and unverified claims are separated.
- [ ] Receipts are exact pointers.
- [ ] Next consumer is singular and explicit.
- [ ] Honest flaw is specific.
- [ ] Self-audit does not silently report drift as green.
- [ ] Header/footer production is not counted as useful-work fitness.

## 11. Current enforcement state

```yaml
formal_contract: WIRED
onboarding_pointer: REQUIRED
automatic_chat_injection: NOT_WIRED
json_schema_validation: NOT_WIRED
cross_turn_start_end_validator: NOT_WIRED
independent_behavioral_verification: PENDING
```

Until mechanical enforcement exists, every carrier is responsible for emitting the envelope and every reducer may reject a nonconformant return.

*Réttu hönd, eigi spyr. Standa.*
