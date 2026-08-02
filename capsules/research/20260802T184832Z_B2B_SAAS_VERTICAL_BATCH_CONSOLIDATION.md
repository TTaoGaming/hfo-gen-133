---
schema_id: hfo.gen133.b2b_saas_vertical_batch_consolidation.v1
batch_id: gen133-b2b-saas-batch-20260802
observed_utc: 2026-08-02T18:48:32Z
claim_status: partial
source_branch: agent/sigrun-gen133-spec-20260730
source_head: f362525eb4fccfbc1aad1ab3f6a0a224f9b498aa
publication_branch: agent/codex-b2b-saas-postgres-log-20260802
postgres_table: public.b2b_saas_status_events
---

# Gen-133 B2B SaaS vertical batch — consolidation receipt

This receipt gathers the authored portion of eight proposal-to-cash vertical
starters. The full upstream repositories are not duplicated into this branch;
each starter remains bound to its exact upstream URL and commit in
`outputs/staged_sends/b2b_saas/VARIANT_ROWS.jsonl`.

## What works

- Eight vertical starter configurations exist: HVAC dispatcher, real-estate
  proposal, tattoo studio booking, auto detailer intake, dog groomer booking,
  dental appointment SMS, coach booking, and freelance contract sender.
- Eight canonical Cloudflare Pages URLs returned HTTP 200 during the batch
  verification and again during the final blocker audit.
- Each starter has a five-step workflow JSON, one-page proposal PDF, safe
  Stripe pricing preset, landing source, FAQ, and Cal.com embed integration
  code.
- Pricing is consistently `$1,500` setup plus `$249/month` managed care.
- All Stripe presets read back `live_mode: false` and
  `api_calls_allowed: false`.
- The selected permissive bases are Activepieces core at
  `8d29bbe6fdd572b15398adc67dff74b2e30d3a3d`, Cal.com at
  `038381aeca6261635357957d66b8ba85cdb29737`, and Trigger.dev at
  `8f66af6e18b73ceaf4a8c2d198bb662a7bb85202`.
- Papermark, Documenso, Twenty CRM, and Formbricks were conservatively recorded
  as `AGPL_SKIPPED`.

## What does not work or is not proven

- Demo booking is not functional. All eight deployed `site.json` files serve
  `REPLACE_WITH_OPERATOR_CAL_LINK`; the operator-owned event path is unknown.
- The workflow JSON files are provider-neutral starter configurations. They
  have not been imported into or executed by customer workflow runtimes.
- No customer deployment, customer message, live Stripe API call, charge, or
  cold email occurred.
- No buyer-response, revenue, or independent-review receipt exists.
- Dental use requires customer-specific privacy, consent, security, vendor BAA,
  and legal review.
- HTTP 200 proves static delivery only; it does not prove a bookable calendar,
  workflow execution, buyer demand, or proposal-to-cash completion.

## Durable evidence

| Artifact | SHA-256 |
|---|---|
| `outputs/staged_sends/b2b_saas/INDEX.md` | `382ee37b2afe5152f7dcbbc277b8a1453564da26d00b4f4b63a9e4defa9e08d9` |
| `outputs/staged_sends/b2b_saas/BATCH_RECEIPT.md` | `eb31e19a7bfb61afb8b90cd1e4da180bb8dc9edc89da357427f22d0c93c5362c` |
| `outputs/staged_sends/b2b_saas/LICENSE_REPORT.md` | `ed510eb7dd81d501bb5f0e8ef9352aa8e019a648a53b2f7f690101d162e8c730` |
| `outputs/staged_sends/b2b_saas/VARIANT_ROWS.jsonl` | `3d6466ac89475a44eeac2a72247e1200254d09956895d1a26e210516209cd0b7` |

The publication workflow writes one append-only status event into Gen-133's
local Postgres database and independently reads the row back. The resulting
readback receipt is stored under `state/ssot/b2b_saas/batch_20260802/` after
the GitHub and Slack pointers exist.

## Exactly one next safe action

Operator provides the exact Cal.com event URL. Replace the placeholder in all
eight `landing/site.json` files, redeploy only the eight static landing
directories, and verify both HTTP 200 and a rendered bookable event.

