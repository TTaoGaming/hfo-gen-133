---
name: hfo-hyperpersonalized-outreach-packet
version: 0.1.0
status: proposed
claim_ceiling: T0 draft/no-send only
send_authority: none
---

# Hyperpersonalized Outreach Packet

## Trigger
Use after a target card and verified two-minute proof kit exist and the operator needs a human-reviewable outreach/application relationship packet.

## Procedure
1. Read the target card, proof-kit bytes, and only source-backed public context.
2. Choose the appropriate relationship surface: warm practice, hiring-team relationship, non-hiring company relationship, partner/recruiter, or product ecosystem.
3. Draft a message with exactly three moves:
   - `OBSERVATION` — one current source-backed fact or context.
   - `UTILITY` — what the tiny artifact may help them think through.
   - `ASK` — one low-friction question or permission-based next step.
4. Keep the first message short. Do not explain the whole technical stack.
5. For hiring targets, separate `APPLY` from `RELATIONSHIP`: an application may be submitted through the official path while a different message starts a genuine technical/business conversation.
6. For non-hiring targets, do not ask for a job in the first message; ask about the problem/workflow or offer the useful artifact.
7. For recruiters, ask for a relationship around a narrow problem/role family, not generic representation.
8. Include a 7-day follow-up draft and a retirement condition.
9. Mark every packet `OPERATOR_REVIEW_REQUIRED / NO_SEND`.

## Packet
```yaml
target:
persona:
route:
source_signal:
proof_kit_ref:
message_1:
followup_1:
claim_ceiling:
operator_review_questions: []
falsifier:
retire_if:
status: NO_SEND
```

## Stop rules
- No guessed private email addresses.
- No mass personalization tokens.
- No false familiarity.
- No autonomous send/apply/connect request.
- No promise of savings or outcomes without evidence.

## Fitness
Reply quality, discovery call, interview, referral, qualified problem, proposal request, or paid receipt — not messages sent.
