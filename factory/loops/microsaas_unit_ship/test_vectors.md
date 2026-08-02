# LOOP-A test vectors

Each vector is a dry-run trace over synthetic input. To run any of them
against real infra, drop `--dry-run` — but expect real wrangler deploys.

## Vector 1 — happy path (dry-run)

Spec:
```json
{
  "name": "PromptBin",
  "slug": "promptbin-test",
  "mutations": {"primary_color": "#2E7D32", "hero_headline": "Save prompts"},
  "price_tier": "$9/mo",
  "icp": "solo AI builders",
  "distribution_channel": ["reddit:r/SideProject"]
}
```
Invocation:
```
python factory/loops/microsaas_unit_ship/run.py --spec /tmp/promptbin.json --dry-run
```
Expected chain rows:
1. `start_ship:promptbin-test` claim_status=proposed
2. `shipped:promptbin-test` claim_status=wired_with_receipts, url=https://promptbin-test.pages.dev, url_verify_ok=5

Expected outputs:
- `factory/build/promptbin-test/` with `package.json` + `index.html` (stub template)
- `factory/distribution/promptbin-test/{reddit,hn_show,directory_list,cold_email}.md + MANIFEST.json`
- One row appended to `state/factory_ships/MICROSAAS_SHIPS.jsonl`

## Vector 2 — build failure

Spec identical to V1 but with `factory/microsaas_template/` present AND a
broken package.json (`"scripts": {"build": "exit 1"}`).

Invocation: `python …/run.py --spec /tmp/promptbin.json`

Expected:
- chain row `build_failed:promptbin-test` claim_status=failed
- `factory/build/promptbin-test/` preserved (not rolled back)
- Slack `halt` ping posted if SLACK_WEBHOOK_URL configured
- run.py exit code 2, no row in MICROSAAS_SHIPS.jsonl

## Vector 3 — URL verify failure

Spec deploys successfully but all 5 canonical URLs return 404 (e.g.
template mis-router).

Expected:
- chain row `url_verify_HALT:<slug>` claim_status=failed
- kill_decision extra: `{"tripped": ["url_verify"], "reasons": {"url_verify": "only 0/5 URLs verified"}}`
- No row in MICROSAAS_SHIPS.jsonl
- Slack `halt` ping

## Vector 4 — queue mode

`state/factory_targets/queue.jsonl`:
```
{"name":"A","slug":"a-test","mutations":{},"price_tier":"$9","icp":"x","distribution_channel":[]}
{"name":"B","slug":"b-test","mutations":{},"price_tier":"$9","icp":"x","distribution_channel":[]}
{"name":"C","slug":"c-test","mutations":{},"price_tier":"$9","icp":"x","distribution_channel":[]}
```

Invocation: `python …/run.py --queue --max 2 --dry-run`

Expected: 2 ships attempted (A, B), C left in queue for next fire.

## Vector 5 — missing template

Fresh clone, no `factory/microsaas_template/` yet.

Expected in dry-run:
- Warning `msg="stub template — no factory/microsaas_template present"` in
  first chain row
- Stub build_dir with just `package.json` + `index.html`
- Pipeline continues (does not HALT — operator can scaffold template later)
