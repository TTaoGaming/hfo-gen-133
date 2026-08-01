# Campaign 01 — AgentReleaseGate pre-release worksheet, cold sequence

```yaml
status: TEMPLATE -- not send-ready. Requires: validated target list (bounce_status=valid), Instantly
        mailboxes past warmup, operator campaign authorization (see RUNBOOK... and the pending
        Sigrun delegation spec).
authored_by: skogul_sonnet5_cold_outreach_scaffold_builder_20260731
companion: ../schemas/target.v0_1.json, ../scripts/lint_copy.py, ../INSTANTLY_CAMPAIGN_SETUP_CHECKLIST.md
voice: technical, specific, one-sentence value prop, prospect-first ("you"/"{{company}}" over "I").
       No mythic/Norse language in any prospect-facing text. Boring register only.
```

## Sequence description

- **Audience:** engineering/product leadership (CTO, Head of Product, Head of Security, or
  founder-level where the company is small) at AI-agent and dev-tooling startups whose public
  materials already describe agents that take action, handle sensitive data, or ship MCP/tool
  integrations. Real source list: `work/hfo_prey_workflow/scout_agent_release_gate_prospects_20260703/prospect_dossiers.json`
  (24 companies, score >= 7, segments: mcp_tool_startup, vertical_ai_agent, devtool_agent,
  seed_series_b_ai_saas). That file has NO verified individual name or email yet
  (`buyer.name` = "Unknown" on every row) -- this sequence cannot fire until a real
  `targets_template.csv`-shaped file replaces those placeholders with validated people.
- **Offer:** agentreleasegate.com -- a free, public-source-only pre-release worksheet
  (not a paid audit pitch on first touch). It reviews what's already public about the
  prospect's agent surface and lists the release-gate questions a team should be able to
  answer before shipping an agent that can act or touch sensitive data. No vulnerability
  claim, no live probing, no login, no scraping -- this constraint is inherited from the
  frozen precedent packet (`inbox/gunnr/GUNNR_AGENTRELEASEGATE_FIRST_SEND_PACKET_20260703T170353Z.md`)
  and must not be loosened without a fresh Hrist-equivalent review.
- **Expected reply rate benchmark:** general cold B2B outbound benchmarks run roughly
  1-5% positive-reply rate for a well-targeted, personalized sequence at this volume; this
  is an industry-general estimate, not a measurement of this specific list or copy. Track
  actual replies from send #1 onward and treat anything materially below 1% after 100+
  sends as a copy or targeting signal, not proof of failure on day one.
- **Cadence:** 3 touches, Email 1 -> wait 4 days -> Email 2 -> wait 6 days -> Email 3, then stop.
  No further touches without a distinct new hook or offer.

---

## Email 1

**Subject** (34 chars):
```
Pre-release check for {{company}}
```

**Body** (65 words):
```
Hi {{first_name}},

{{personalization_hook}}

I put together a short, public-source worksheet on pre-release
checks for AI agents: the questions to ask before an agent ships,
framed around release-gate evidence rather than pen-test findings.
No vulnerability claim, no probing of {{company}}'s systems, just a
one-page checklist built from what's public.

Want me to send the {{company}} version?

Reply "not relevant" and I will not follow up.
```

---

## Wait 4 days

---

## Email 2 (bump)

**Body** (31 words):
```
Hi {{first_name}},

Following up on the pre-release worksheet for {{company}} --
{{personalization_hook}}

Happy to send it over if useful, no strings attached.

Reply "not relevant" and I will not follow up.
```

---

## Wait 6 days

---

## Email 3 (breakup)

**Body** (29 words):
```
Hi {{first_name}},

Last note on this, closing the loop on {{company}}'s pre-release
worksheet. If it's useful later, just reply and I'll send it.

No hard feelings either way.
```

---

## CAN-SPAM footer template (appended to every email by Instantly, not typed per-email)

```
--
{{sender_name}}, agent-for-{{operator_name}}
{{sender_company}}
{{physical_mailing_address_or_po_box}}

Don't want these? Unsubscribe: {{unsubscribe_link}}
```

Required before ANY send: a real physical address or PO box (currently
`blocked_missing` per the frozen precedent packet), a working unsubscribe link
wired through Instantly's list-unsubscribe header, and the sender name/company
fields filled with the operator-approved identity, not a placeholder.

## Variables allowlist (lint fails on anything else)

| Variable | Source | Notes |
|---|---|---|
| `{{first_name}}` | target.v0_1.json `first_name` | required |
| `{{company}}` | target.v0_1.json `company` | required |
| `{{personalization_hook}}` | target.v0_1.json `personalization_hook` | required; must be real, never fabricated |
| `{{sender_name}}` | campaign config, footer only | operator-approved identity |
| `{{operator_name}}` | campaign config, footer only | operator-approved identity |
| `{{sender_company}}` | campaign config, footer only | |
| `{{physical_mailing_address_or_po_box}}` | campaign config, footer only | CAN-SPAM requirement, currently unfilled |
| `{{unsubscribe_link}}` | Instantly system merge tag, footer only | |

Any `{{other_tag}}` appearing in `copy/campaign_01_sequence.md` outside this table
is a lint failure -- see `scripts/lint_copy.py`.

## Honest flaw

This is copy scaffolding against a real 24-company target list that currently has
zero validated individual emails. It has not been reviewed by an adversarial pass
(the Hrist-equivalent step the 2026-07-03 precedent required before any send), has
no physical mailing address filled in, and has not been checked against Instantly's
own list-unsubscribe / CAN-SPAM feature requirements -- only against this repo's own
prior precedent packet.
