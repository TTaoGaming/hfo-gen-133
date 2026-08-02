# Batch Receipt - Eight Vertical B2B Starters

```yaml
schema_id: hfo.gen133.b2b_vertical_batch_receipt.v1
observed_utc: 2026-08-02T17:37:22Z
claim_status: partial
vertical_count: 8
public_http_200_count: 8
pricing: "$1,500 setup + $249/month"
stripe_live_mode: false
stripe_api_calls_allowed: false
customer_deployments: 0
customer_messages_sent: 0
charges_created: 0
cold_emails_sent: 0
cal_embed_bound_count: 0
```

## Deployment readback

| Vertical | Canonical URL | Immutable deployment URL | Readback |
|---|---|---|---|
| HVAC dispatcher | https://hfo-hvac-dispatcher-b2b.pages.dev | https://8d304b5e.hfo-hvac-dispatcher-b2b.pages.dev | landing 200; `site.json` 200 |
| Real-estate proposal | https://hfo-real-estate-proposal-b2b.pages.dev | https://134c7b49.hfo-real-estate-proposal-b2b.pages.dev | landing 200; `site.json` 200 |
| Tattoo studio booking | https://hfo-tattoo-studio-booking-b2b.pages.dev | https://772de006.hfo-tattoo-studio-booking-b2b.pages.dev | landing 200; `site.json` 200 |
| Auto detailer intake | https://hfo-auto-detailer-intake-b2b.pages.dev | https://f7483c55.hfo-auto-detailer-intake-b2b.pages.dev | landing 200; `site.json` 200 |
| Dog groomer booking | https://hfo-dog-groomer-booking-b2b.pages.dev | https://69985769.hfo-dog-groomer-booking-b2b.pages.dev | landing 200; `site.json` 200 |
| Dental appointment SMS | https://hfo-dental-appointment-sms-b2b.pages.dev | https://b9520671.hfo-dental-appointment-sms-b2b.pages.dev | landing 200; `site.json` 200 |
| Coach booking | https://hfo-coach-booking-b2b.pages.dev | https://758a7d6d.hfo-coach-booking-b2b.pages.dev | landing 200; `site.json` 200 |
| Freelance contract sender | https://hfo-freelance-contract-sender-b2b.pages.dev | https://034c34f2.hfo-freelance-contract-sender-b2b.pages.dev | landing 200; `site.json` 200 |

## Verification receipts

- Gen-133 local and remote branch readback matched `f362525eb4fccfbc1aad1ab3f6a0a224f9b498aa` before the copy-forward.
- Eight local fork heads matched their selected upstream SHAs and preserved their upstream remotes.
- All 24 JSON files parsed; each workflow has five steps; each landing has five steps.
- All price presets read back `$1,500` setup, `$249` monthly, `live_mode: false`, and `api_calls_allowed: false`.
- Eight PDFs reopened as exactly one page, contained the required price/boundary/acceptance text, rendered to PNG, and stayed within measured page bounds.
- Eight landing shells and eight `site.json` files returned local HTTP 200.
- Eight canonical public URLs and eight deployed `site.json` files returned HTTP 200 with matching vertical identities.
- The first Cloudflare project-create call returned HTTP 500/code 8000000. One same-target retry succeeded; no alternate account, project, or existing site was used.

## Falsifier

This receipt is invalidated if any canonical URL stops returning 200, a deployed `site.json` no longer matches its vertical, a chosen fork head/license differs from the recorded commit, or any Stripe preset permits live mode/API calls.

## Remaining risk

- Cal.com booking is not operational because the operator's exact event link was not provided.
- Workflow JSON is provider-neutral starter configuration, not an import/runtime execution receipt.
- No customer, market-response, payment, or independent-review receipt exists.
- Dental deployment would require customer-specific privacy, consent, security, vendor BAA, and legal review.

## Exactly one next safe action

Operator provides the exact Cal.com event link; replace the placeholder in all eight `landing/site.json` files and redeploy only the static landing directories.
