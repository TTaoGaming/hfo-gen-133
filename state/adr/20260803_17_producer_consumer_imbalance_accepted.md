# ADR-20260803-17 — 6 units built with distribution capacity == 0 (imbalance accepted, debt logged)

- **Context:** JORMUNGANDR_REDTEAM warned: deposits without pickups = decoration. This session added 6 more shipped units before distribution capacity was proven above zero.
- **Decision:** Accept the imbalance as a one-time debt, recorded here. The 1-unit/week cap (ADR-04) plus the Tuesday-distribution deferral (ADR-16) is the corrective path — no more shipping until pickups start clearing.
- **Consequence:** Next session opens with a debt of "6 shipped, 0 distributed". Cap enforcement is now the operative brake, not shipping-throttle at build time.
- **Author:** olrun (per Jörmungandr red-team + operator debt-acknowledgement)
- **Alternatives considered:** halt at 3 units and don't ship the 4-6 (rejected — 4-6 were mid-flight when throttle landed); ship & pretend no debt (rejected — decoration-drift pattern operator warned about).
