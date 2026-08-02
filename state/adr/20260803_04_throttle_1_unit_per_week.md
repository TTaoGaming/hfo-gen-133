# ADR-20260803-04 — Ship cadence throttled to 1 unit/week hard cap

- **Context:** FRAMEWORK v1.0 originally targeted 10–17 units/week (2-3 per weekday). JORMUNGANDR_REDTEAM_30DAY §H.3 measured distribution capacity at ZERO (0 outreach rows, 0 booking links, 0 approved gate items) against 53 already-live URLs. Producer-consumer imbalance = deposits without pickups = decoration.
- **Decision:** Hard cap ship cadence at **1 unit/week**, combined across FACTORY A + FACTORY B. Cap lifts only when one shipped unit has ≥1 paying customer OR ≥100 organic impressions.
- **Consequence:** Six units already shipped this session are the ENTIRE next 6 weeks' inventory unless caps lift. All remaining energy shifts to distribution (Tier 0-2) and demand-signal mining.
- **Author:** olrun + Jörmungandr (chain rows 125, 126, 127)
- **Alternatives considered:** keep 10-17/wk with distribution loop parallelism (rejected — same imbalance defect); throttle to 2/wk (rejected — one clear ceiling is more legible than a compromise).
