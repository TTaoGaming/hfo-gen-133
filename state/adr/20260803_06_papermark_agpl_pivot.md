# ADR-20260803-06 — Papermark fork abandoned; docsend-lite built ground-up (AGPL pivot)

- **Context:** Original plan (in SIGRUN_FACTORY_TARGETS_V0) had Papermark as a fork candidate for the "sales-doc share + view analytics" unit. Papermark is AGPL-3.0 licensed. AGPL contamination for a paid closed-source Cloudflare Workers unit is a legal hazard.
- **Decision:** Do not fork Papermark. Build `factory/units/docsend-lite/` from scratch on the microsaas_template with a minimal `functions/api/view.js` Worker for view-tracking. Own LICENSE (permissive).
- **Consequence:** docsend-lite ships as a clean-room unit; can be sold without AGPL disclosure obligations. Feature parity is deliberately narrower than Papermark (view count + email capture + expiry, no full annotations).
- **Author:** olrun (docsend-lite build path in `factory/units/docsend-lite/`)
- **Alternatives considered:** Papermark fork with AGPL compliance (rejected — commercial friction); DocSend clone via MIT-licensed reference implementation (deferred — none found with sufficient parity).
