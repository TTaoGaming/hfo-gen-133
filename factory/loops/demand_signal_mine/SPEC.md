# LOOP-D · DEMAND_SIGNAL_MINE — SPEC

```yaml
AIH2O:
  version: gen-133
  loop: demand_signal_mine
  role: executor
  actor: factory_loop
  verifier: n_signals > 0 OR explicit zero-signal chain-row with reason
  clock_source: host_read
  chain: state/loop_receipts/demand_signal_mine_<UTCDATE>.jsonl
  signal_log: state/factory_targets/DEMAND_SIGNAL_LOG.jsonl
  daily_digest: state/factory_targets/DEMAND_DIGEST_<UTCDATE>.md
```

## Inputs

- `--subreddits subs.txt` (one sub per line, `#` comments allowed)
- `--patterns patterns.json` — `{label: regex}`. Example:
  ```json
  {
    "wasted_time": "\\b(waste|wasted|hours) (of|on)\\b",
    "manual_process": "\\b(spreadsheet|csv|manual)\\b.*(track|process|sync)",
    "wish_had": "\\b(i wish|is there a|looking for a) (tool|app|service)\\b"
  }
  ```
- `--cells cells.json` — MAP-Elite cell definitions:
  ```json
  {
    "hvac_scheduling_low": {"terms": ["hvac","dispatch","schedule"], "weight": 1.0},
    "prompts_versioning_mid": {"terms": ["prompt","version","chatgpt"], "weight": 1.2}
  }
  ```

## Sources

1. Reddit — `https://www.reddit.com/r/<sub>/new.json?limit=100` (public,
   no auth). 1.5s inter-request delay to stay under rate limit.
2. Hacker News — `hacker-news.firebaseio.com/v0/newstories.json` +
   per-item fetch. 50ms inter-item delay.
3. Indie Hackers — planned via public feeds; not yet wired.

## Outputs

- `state/factory_targets/DEMAND_SIGNAL_LOG.jsonl` — every scored signal
- `state/factory_targets/DEMAND_DIGEST_<YYYYMMDD>.md` — top-10 + cell coverage
- Chain rows in `state/loop_receipts/demand_signal_mine_<UTCDATE>.jsonl`

## Kill conditions

- Reddit 429 → exponential backoff 60s → 300s → 1800s, then continue
- Zero signals across ALL sources → `finish_scan` claim_status=partial +
  Slack warn ping (do not halt — patterns may just be too narrow)

## LLM classification

Uses `factory.loops.lib.litellm_client.complete()`. Prompt asks for
`<icp>|<pain>|<affordability_signal 0-3>`. If LITELLM_PROXY_URL is not
set, returns a DRY_RUN stub — pipeline still runs, chain-row shows this
as `remaining_risk=["stub_llm_label"]`.

## Cadence

Cron daily 06:00 UTC:

```powershell
schtasks /Create /TN "hfo-loop-D-demand-mine" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\demand_signal_mine\run.py --subreddits C:\...\subs.txt --patterns C:\...\patterns.json --cells C:\...\cells.json" `
  /SC DAILY /ST 06:00 /F
```

## Chain-row axes

| action | claim_status | notes |
|---|---|---|
| `start_scan` | proposed | count of subs/patterns/cells |
| `finish_scan` | wired_with_receipts | n_signals, digest path, cell_coverage |
| `finish_scan` | partial | zero signals (Slack warn also posted) |
