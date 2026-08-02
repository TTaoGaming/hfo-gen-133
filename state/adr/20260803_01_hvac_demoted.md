# ADR-20260803-01 — HVAC vertical demoted

- **Context:** Prior research surfaced HVAC dispatcher as a candidate B2B micro-SaaS target (see `outputs/staged_sends/b2b_saas/hvac_dispatcher/`). Operator anchor `state/operator_voice/OPERATOR_NO_WARM_NETWORK_ANCHOR_20260803.md` filters unfamiliar domains.
- **Decision:** HVAC removed from active target set for the 1-unit/week factory. Existing staged HVAC artifacts remain on disk as ghosts (not fired).
- **Consequence:** B2B micro-SaaS lane narrows toward AI-dev-adjacent verticals (agent-status, agent-changelog, agent-cost-tracker, docsend-lite, prompt-versioning-lite, local-whisper-web).
- **Author:** olrun (per operator anchor + Sigrún V11)
- **Alternatives considered:** keep HVAC as speculative branch (rejected — violates domain-familiarity filter); pivot to plumbing/electrician SaaS (rejected — same defect).
