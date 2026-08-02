# ADR-20260803-20 — Instantly domain `tryagentreleasegate.com` locked as sending path

- **Context:** Operator owns and has warmed `tryagentreleasegate.com` via Instantly. It's the only fully-warmed mail-only sending domain. `state/outreach/INSTANTLY_STATE_20260803.md` captures mailbox count + warmup completion + first-send readiness.
- **Decision:** All cold-email in the Tier-3 stack (FRAMEWORK_GEN133_V1 §3) uses this domain until operator provisions a second one. Do not rotate mid-campaign.
- **Consequence:** Contracts + employment + grants campaigns all thread through one sender identity. Deliverability risk concentrated. Second-domain provisioning is a queued operator task, not a blocker.
- **Author:** operator (owns domain); olrun (locked path)
- **Alternatives considered:** use Gmail direct (rejected — deliverability + volume ceiling); provision new domain now (deferred — takes 2-3 weeks warmup, blocks Tuesday fire).
