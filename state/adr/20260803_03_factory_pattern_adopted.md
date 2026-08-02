# ADR-20260803-03 — Factory pattern adopted (template + units + loops)

- **Context:** Prior sessions shipped units ad-hoc with no shared skeleton, causing duplicated legal-shell files, inconsistent Cloudflare deploys, and drift in analytics setup.
- **Decision:** Standardize on `factory/microsaas_template/` (Cloudflare Pages + Workers + Stripe Checkout skeleton with `.placeholder-config.json` substitution), `factory/scripts/{build,deploy,verify}-unit.mjs` for pipeline, and `factory/loops/*/run.py` for stigmergic distribution loops. Six units this session all inherit template.
- **Consequence:** Every new unit is a fill-in-the-blanks operation; regressions in the template auto-propagate to every unit at next rebuild. Loops (`microsaas_unit_ship`, `foss_fork_variant`, `directory_submission_batch`, `demand_signal_mine`, `partner_pitch_batch`, `seo_content_draft`) provide the automation surface.
- **Author:** olrun (design in `state/olrun/FACTORY_DESIGN_20260803T003000Z.md`)
- **Alternatives considered:** per-unit ad-hoc (rejected — duplication defect); nx/turborepo monorepo (rejected — over-engineered for 20-30 unit ceiling).
