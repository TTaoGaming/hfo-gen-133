# LOOP-D test vectors

## Vector 1 — happy path (dry-run, skips LLM)

Files:
```
subs.txt:
  SideProject
  HVAC

patterns.json:
  {"waste": "waste|wasted", "wish": "i wish|looking for a"}

cells.json:
  {"cell_a": {"terms": ["hvac","schedule"], "weight": 1.0},
   "cell_b": {"terms": ["prompt","chatgpt"], "weight": 1.0}}
```

Invocation:
```
python factory/loops/demand_signal_mine/run.py \
  --subreddits subs.txt --patterns patterns.json --cells cells.json --dry-run
```

Expected:
- chain rows `start_scan` proposed + `finish_scan` wired_with_receipts
- rows appended to `DEMAND_SIGNAL_LOG.jsonl`
- `DEMAND_DIGEST_<today>.md` with top 10 + cell coverage

## Vector 2 — Reddit rate limit

Simulate by pointing at 20 subs and running back-to-back. First call may
succeed, second may hit 429.

Expected: backoff kicks in transparently (60s → 300s → 1800s), pipeline
continues once quota resets.

## Vector 3 — zero signals

patterns.json contains regex that never matches (e.g. `"waste":"zzzzz_never_matches"`).

Expected:
- `finish_scan` claim_status=partial
- honest_flaw="zero signals — check patterns.json or source availability"
- Slack warn ping posted
- Digest still written but "Signals collected: 0"

## Vector 4 — HN only

Delete all subs from subs.txt (single `# empty` line), keep `--include-hn`.

Expected: no reddit fetches, HN scanned normally, signals only from `hn:new`.

## Vector 5 — LLM proxy configured

Set `LITELLM_PROXY_URL=http://localhost:4000` and drop `--dry-run`.

Expected: each signal has non-stub `llm_label`. Fall-back stub if proxy
unreachable (returns "UNKNOWN|...|0").
