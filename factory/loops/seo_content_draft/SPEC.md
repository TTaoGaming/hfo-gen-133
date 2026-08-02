# LOOP-F · SEO_CONTENT_DRAFT — SPEC

```yaml
AIH2O:
  version: gen-133
  loop: seo_content_draft
  role: executor
  actor: factory_loop
  verifier: word_count in [500, 2000] + landing_link present + at least 1 cross_link
  clock_source: host_read
  chain: state/loop_receipts/seo_content_draft_<UTCDATE>.jsonl
  publish_queue: content/PUBLISH_QUEUE.md
```

## Inputs

- `--units state/factory_ships/MICROSAAS_SHIPS.jsonl`
- `--keywords keywords.json`:
  ```json
  {
    "promptbin":  ["organize chatgpt prompts", "prompt version control small teams"],
    "hvac-jobsheets": ["hvac digital job sheet template", "field service form builder"]
  }
  ```

## Outputs

- Article: `content/blog/<unit_slug>/<keyword-slug>.md`
  with frontmatter `awaiting_operator_publish: true`
- Publish queue: `content/PUBLISH_QUEUE.md` — checkboxes for the operator
- Chain rows in `state/loop_receipts/seo_content_draft_<UTCDATE>.jsonl`

## Kill conditions

- LLM output <500 or >2000 words → `reject:<unit>:<kw>` failed, skip
- Article already exists for `(unit, keyword)` → `skip_exists` proposed (idempotent)
- Unknown unit slug (not in ships log) → `skip_unknown_unit` partial

## LLM contract

Uses `factory.loops.lib.litellm_client.complete()` with:
- system: senior SaaS marketer, no hype
- structured prompt: hook / why generic advice fails / concrete workflow /
  where product fits / cross-links / CTA
- Deploy URL must appear in the body; injected if missing

Without `LITELLM_PROXY_URL`, `--dry-run` produces a stub article
(≈50 words, no LLM cost) so pipeline still runs.

## Cadence

Mon/Wed/Fri 04:00:

```powershell
schtasks /Create /TN "hfo-loop-F-seo-mon" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\seo_content_draft\run.py --units C:\Dev\hfo_gen_133_forge\state\factory_ships\MICROSAAS_SHIPS.jsonl --keywords C:\Dev\hfo_gen_133_forge\content\keywords.json" `
  /SC WEEKLY /D MON /ST 04:00 /F
```

Repeat for `WED` and `FRI`.

## Chain-row axes

| action | claim_status | notes |
|---|---|---|
| `start_draft` | proposed | counts |
| `skip_unknown_unit:<slug>` | partial | unit not in ships |
| `skip_exists:<unit>:<kw>` | proposed | idempotent |
| `reject:<unit>:<kw>` | failed | word count OOB |
| `drafted:<unit>:<kw>` | wired_with_receipts | file written |
| `finish_draft` | wired_with_receipts | summary |
