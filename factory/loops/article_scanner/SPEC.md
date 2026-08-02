# LOOP-A · ARTICLE_SCANNER — SPEC

Broader-signal sibling to LOOP-D (`demand_signal_mine`). LOOP-D mines
Reddit + HN for *pain* patterns; LOOP-A pulls *industry-evolution* signal
from named authors, newsletters, and vendor blogs, then scores each item
against six factory-relevant axes:

- `build_opportunity` — something we could ship
- `distribute_tactic` — a way to move product
- `tool_adoption` — a stack change we should track
- `market_signal` — pricing, funding, org-shape shift
- `competitive_threat` — someone building near us
- `hive_infra_pattern` — HFO-adjacent architecture we should copy or resist

```yaml
AIH2O:
  version: gen-133
  loop: article_scanner
  role: executor
  actor: factory_loop
  verifier: n_signals > 0 OR explicit zero-signal chain-row with reason
  clock_source: host_read
  chain: state/loop_receipts/article_scanner_<UTCDATE>.jsonl
  signal_log: state/factory_targets/article_signals.jsonl
  daily_digest: state/factory_targets/ARTICLE_DIGEST_<UTCDATE>.md
  weekly_digest: state/factory_targets/ARTICLE_WEEK_<UTCDATE>.md
```

## Inputs

- `--sources sources.yaml` — list of feed definitions. Each entry:
  ```yaml
  - name: bytebytego
    url: https://blog.bytebytego.com/feed
    kind: rss           # rss | html | api | reddit_json | hn_top
    tags: [engineering, systems]
    enabled: true
  ```
- `--seed seed_urls.json` — URLs guaranteed to appear in the very next
  digest even if their feed misses them. Prime with operator-flagged
  articles.
- `--window-hours N` — default 24. Widen for backfill.
- `--threshold F` — default 0.05 (composite = relevance × novelty ×
  actionability). Deliberately lenient so first weeks capture wide net;
  operator tightens once signal-to-noise is measured. Seeded rows
  (see `seed_urls.json`) bypass the threshold and always land.
- `--dry-run` — skip LiteLLM classification, keep everything else.

## Sources (per Step 1)

Newsletters/blogs: TLDR AI, Ben's Bites, Import AI, The Rundown,
The Neuron, AlphaSignal, Latent Space, ByteByteGo, Martin Fowler,
Simon Willison, Cal Paterson, Zach Holman, humanlayer, ghuntley,
moekhalil substack, calv.info, spronta.com, Anthropic blog, OpenAI blog.
Aggregators: HN top-50, r/mcp, r/LocalLLaMA, r/AIAgents, r/vibecoding.

Fetch discipline: RSS/Atom preferred, HTML index scrape when no feed
exists, Reddit `.json` (User-Agent set), HN Firebase API. **No auth,
no ToS violation, no paywalled content grabbing** (WSJ/NYT capture only
the public preview snippet the feed already surfaces).

## Outputs

- `state/factory_targets/article_signals.jsonl` — every scored signal,
  ever. Weekly review reads a 7-day window from here.
- `state/factory_targets/ARTICLE_DIGEST_<YYYYMMDD>.md` — top-10 signals
  by composite score with `hfo_action` per signal.
- `state/factory_targets/ARTICLE_WEEK_<YYYYMMDD>.md` — Sunday
  accumulator: top-20 with pick/skip columns.
- Chain rows in `state/loop_receipts/article_scanner_<UTCDATE>.jsonl`.

## Kill conditions

- Per-source: **3 consecutive failed fetches** across runs → source
  marked `degraded`, skipped for 24 h. State kept in
  `state/factory_targets/article_scanner_source_health.json`.
- Digest empty (0 signals above threshold) **3 days running** →
  chain-row `halt`, `slack_escalate` severity=`halt`, operator paged.
- LiteLLM 4xx/5xx → back off (2 → 4 → 8 s), then continue with regex
  fallback labels. Never halts the run.

## LLM classification

Uses `factory.loops.lib.litellm_client.complete()` with a small model
(`gpt-4o-mini` by default). Prompt asks for a strict JSON envelope:

```json
{
  "axis": "build_opportunity",
  "relevance": 0.72,
  "novelty": 0.55,
  "actionability": 0.60,
  "hfo_action": "sketch a webmcp adapter for the calv patterns"
}
```

If `LITELLM_PROXY_URL` is unset, the runner falls back to regex-only
scoring and marks each row `remaining_risk=["stub_llm_label"]`.

## Cadence

Two paths, both installed for resilience:

1. **Windows Task Scheduler** — daily 06:00 local. Installer:
   `install_windows_task.ps1`.
2. **GitHub Actions** — cron `0 6 * * *` UTC. Commits the digest back
   to the repo. Fallback for when operator's PC is off.

## Operator-review workflow (Step 6)

- **Daily** — glance at `ARTICLE_DIGEST_<today>.md`. Marks nothing;
  everything is already in `article_signals.jsonl`.
- **Sunday** — reads `ARTICLE_WEEK_<sunday>.md`. Rows carry columns
  `pick` / `skip` / `note`. Operator flips picks by editing the file
  in place, then commits. A separate downstream step (out of scope
  here) reads picks and pushes them to MAP-Elites cell scoring for
  next build cadence.

## Chain-row axes

| action | claim_status | notes |
|---|---|---|
| `start_scan` | proposed | source count, window hours, threshold |
| `fetch_source` | wired_with_receipts | per source: n_items, ms |
| `fetch_source` | partial | source degraded / skipped |
| `finish_scan` | wired_with_receipts | n_signals, digest path |
| `finish_scan` | partial | zero signals (day <3 in streak) |
| `finish_scan` | failed | zero signals ≥3d — halt-escalated |

## What this loop is NOT

- Not a replacement for LOOP-D. LOOP-D listens to *users complaining*;
  LOOP-A listens to *builders publishing*.
- Not a curation feed. The digest is a rough cut for operator triage,
  not a public-facing artifact.
- Not a paywall bypass. Sources behind a login are dropped, not
  scraped.
