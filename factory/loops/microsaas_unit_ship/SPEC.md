# LOOP-A · MICROSAAS_UNIT_SHIP — SPEC

```yaml
AIH2O:
  version: gen-133
  loop: microsaas_unit_ship
  role: executor
  actor: factory_loop
  verifier: HEAD 200 on 5 canonical URLs + non-zero build exit code guard
  clock_source: host_read
  chain: state/loop_receipts/microsaas_unit_ship_<UTCDATE>.jsonl
  ship_log: state/factory_ships/MICROSAAS_SHIPS.jsonl
```

## Inputs

Path to `unit_spec.json` OR `--queue` (consume next N rows from
`state/factory_targets/queue.jsonl`).

Schema:

```json
{
  "name": "PromptBin",
  "slug": "promptbin",
  "foss_parent_url_or_none": null,
  "mutations": {
    "primary_color": "#2E7D32",
    "hero_headline": "Save every prompt you regret losing.",
    "cta_label": "Start free"
  },
  "price_tier": "$9/mo",
  "icp": "solo AI builders",
  "distribution_channel": ["reddit:r/PromptEngineering", "hn_show", "product_hunt"],
  "one_liner": "A pastebin for prompts with tags, versioning, and quick share.",
  "pain": "keeping track of prompt iterations across chats",
  "subreddit": "PromptEngineering",
  "tech_stack": "SvelteKit + Cloudflare Pages + D1",
  "outcome": "recover any prompt in <5s",
  "metric": "context-switch overhead"
}
```

All keys except `name/slug/mutations/price_tier/icp/distribution_channel` are optional.
Missing optional keys fall back to sane defaults inside `run.py`.

## Outputs

1. `factory/build/<slug>/` — layered build output (preserved on halt)
2. `https://<slug>.pages.dev` — deployed static site
3. `factory/distribution/<slug>/` — Reddit + HN + directory list + cold email drafts
4. Row appended to `state/factory_ships/MICROSAAS_SHIPS.jsonl`
5. Multiple chain rows in `state/loop_receipts/microsaas_unit_ship_<UTCDATE>.jsonl`

## Kill conditions

- `npm install` or `npm run build` non-zero → HALT, chain-row `failed`, preserve `factory/build/<slug>/`, Slack `halt` ping
- `wrangler pages deploy` non-zero → HALT, chain-row `failed`, Slack `halt` ping
- 0/5 canonical URLs return 2xx-3xx → HALT (`kill_gates.check` with `url_verify_min=1`), Slack `halt` ping

## Cadence

- One-shot: `--spec` per operator invocation
- Recurring: Windows Task Scheduler at 08:00 local, `--queue --max 3`

## Class pre-authorization

MICROSAAS_UNIT_SHIP does NOT read the approval gate — it deploys with the
operator's implicit approval (one `--spec` per fire). Distribution
downstream (LOOP-C, cold email) IS gated. Grammar for the downstream:

```
class:microsaas_ship_batch:quota=10:seq_range=001-999:expires=<UTC>
```

## Canonical URLs verified

- `/`
- `/pricing`
- `/about`
- `/privacy`
- `/terms`

Adjust `CANONICAL_PATHS` in `run.py` if template layout drifts.

## Dependencies

- Node 20+ with `npm`
- `wrangler` CLI logged in (`wrangler login` on operator machine)
- `factory/microsaas_template/` scaffolded (stub falls through if missing — see run.py)

## Chain-row axes

| action | claim_status | notes |
|---|---|---|
| `start_ship:<slug>` | proposed | spec loaded |
| `build_failed:<slug>` | failed | kill on npm build non-zero |
| `deploy_failed:<slug>` | failed | kill on wrangler non-zero |
| `url_verify_HALT:<slug>` | failed | kill on 0/5 URLs |
| `shipped:<slug>` | wired_with_receipts | ship_row appended |
