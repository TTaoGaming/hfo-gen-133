# HVAC Dispatcher Starter

A proposal-to-cash workflow for owner-led HVAC businesses with 3-15 trucks: lead intake, approved estimate, crew scheduling, and invoice follow-up.

- Base: Activepieces core at `8d29bbe6fdd572b15398adc67dff74b2e30d3a3d`
- License: MIT for core content; `packages/ee/` and `packages/server/api/src/app/ee` are excluded
- Buyer signal: calls and web leads are commonly re-keyed into estimates, calendars, and invoices by the owner or dispatcher
- Starter state: configuration only; no credentials, customer data, live payments, messages, or production deployment

The clone is sparse to keep this batch bounded. Run `git sparse-checkout disable` inside this directory to materialize the complete upstream working tree.

## Included

- `workflow.json` - provider-neutral Activepieces adapter plan
- `stripe_pricing_preset.json` - disabled, test-only offer preset
- `templates/proposal_template.pdf` - editable-content proposal template rendered to PDF
- `../landing.html` and `../landing/` - one-page offer site and deployable directory
