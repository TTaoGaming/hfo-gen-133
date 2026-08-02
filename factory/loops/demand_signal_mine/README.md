# demand_signal_mine

Pull last-24h posts from Reddit + HN, extract pain patterns with regex,
classify with LiteLLM, score against MAP-Elite cells, emit a daily digest.

## Files you provide

- `subs.txt` — one subreddit per line (no `r/` prefix)
- `patterns.json` — `{label: regex}` for regex-based pain detection
- `cells.json` — MAP-Elite cell definitions with weighted term lists

## One-shot

```powershell
python factory\loops\demand_signal_mine\run.py `
  --subreddits subs.txt --patterns patterns.json --cells cells.json
```

## Daily 06:00 UTC

```powershell
schtasks /Create /TN "hfo-loop-D-demand-mine" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\demand_signal_mine\run.py --subreddits C:\Dev\...\subs.txt --patterns C:\Dev\...\patterns.json --cells C:\Dev\...\cells.json" `
  /SC DAILY /ST 06:00 /F
```

Windows uses local time — `06:00` in your local zone. Convert to UTC if you
need exact daily UTC timing.

## Dry-run (skips LLM cost)

```powershell
python factory\loops\demand_signal_mine\run.py `
  --subreddits subs.txt --patterns patterns.json --cells cells.json --dry-run
```

## Prereqs

- Python 3.11+
- Optional: `LITELLM_PROXY_URL` in `.env` for LLM classification
  (falls back to DRY_RUN stub otherwise)

## Where things land

- Every signal: `state/factory_targets/DEMAND_SIGNAL_LOG.jsonl`
- Daily digest: `state/factory_targets/DEMAND_DIGEST_<YYYYMMDD>.md`
- Receipts: `state/loop_receipts/demand_signal_mine_<YYYYMMDD>.jsonl`
