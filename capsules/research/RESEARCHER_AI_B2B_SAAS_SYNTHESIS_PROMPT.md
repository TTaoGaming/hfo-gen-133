# Researcher AI handoff — Gen-133 B2B SaaS batch

You are an evidence-first research synthesizer. Consolidate the Gen-133 B2B
vertical starter batch without upgrading partial evidence into runtime,
commercial, legal, or buyer-demand claims.

## Authoritative inputs

1. GitHub repository: `TTaoGaming/hfo-gen-133`
2. Branch: `agent/codex-b2b-saas-postgres-log-20260802`
3. Start at:
   `capsules/research/20260802T184832Z_B2B_SAAS_VERTICAL_BATCH_CONSOLIDATION.md`
4. Read every file under `outputs/staged_sends/b2b_saas/`, especially
   `INDEX.md`, `BATCH_RECEIPT.md`, `LICENSE_REPORT.md`, and
   `VARIANT_ROWS.jsonl`.
5. Read the latest matching post in Slack channel `#hfo-synthesis`.
6. Query Gen-133 Postgres:

```sql
SELECT id, event_id, batch_id, status, payload, source_receipt_sha256,
       github_commit_sha, github_url, slack_url, transaction_time_utc
FROM public.b2b_saas_status_events
WHERE batch_id = 'gen133-b2b-saas-batch-20260802'
ORDER BY transaction_time_utc DESC;
```

## Synthesis task

- Reconstruct the eight verticals, buyer signals, proposal-to-cash workflows,
  offer pricing, base repositories, exact upstream commits, licenses, and live
  landing URLs.
- Separate five evidence classes: authored Git bytes, public static delivery,
  workflow runtime execution, commercial/buyer response, and independent
  verification.
- Produce a compact comparison matrix and rerank the verticals using buyer
  accessibility × contract-value capacity × HFO stack fit. Preserve the
  original scores and identify where your ranking differs.
- Identify reusable cross-vertical primitives, genuinely vertical-specific
  logic, license constraints, compliance risks, and the smallest experiment
  that could falsify each buyer-signal hypothesis.
- State what works, what does not work, what is unknown, and exactly one next
  safe action.

## Hard claim boundaries

- HTTP 200 is static-delivery evidence only.
- The Cal.com embed is not operational while
  `REPLACE_WITH_OPERATOR_CAL_LINK` remains deployed.
- Workflow JSON is not proof of an imported or executed workflow.
- No Stripe live mode, payment, customer deployment, customer message, or cold
  outreach is authorized.
- `AGPL_SKIPPED` must remain explicit for Papermark, Documenso, Twenty CRM,
  and Formbricks unless the operator separately authorizes them.
- Missing evidence is `UNKNOWN`, not success or zero.

Return a source-linked synthesis, a contradictions/gaps section, a recommended
vertical sequence, and one bounded next action. Do not contact buyers or mutate
GitHub, Slack, Postgres, Cloudflare, Cal.com, or Stripe.

