# gen-130 snapshot pointer — 2026-07-31

```yaml
schema_id: hfo.gen133.archive.gen130_pointer.v0_1
valid_time_utc: 2026-07-31T18:40:00Z
claim_status: wired_with_receipts
author: sonnet-5 valkyrie · gen-133 PARA reorg execution
```

gen-130 was placed under **narrow freeze** on 2026-07-31 (operator directive via
Olrún dispatch). This is not a copy of gen-130 — it is a pointer.

## Where the live archive actually is

```
C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/
```

That forge is frozen for *new* work-product but **not decommissioned** — see
`NARROW_FROZEN_20260731.md` at its root for what still runs there (existing
Codex hourly automations, Garmr heartbeat, Claude Desktop scheduled tasks).
Do not delete it. Do not assume it is static.

## What was pulled into gen-133 as of this snapshot

- `projects/2026-08_cold_outreach_launch/` — copied from gen-130
  `projects/2026-08_cold_outreach_launch/` (campaign copy, kill-switch
  runbook, target schema, lint spec). SHA-verified clean copy.
- `resources/reports/2026-07-31/gen130_income_lane_strategy/` — 23
  `SIGRUN_*.md` strategy/status reports copied from gen-130 root. SHA-verified
  clean copy.

## What was deliberately NOT pulled

- gen-130's `contracts/`, `canon/`, `AGENTS.md` (83 KB), and the rest of its
  root doc corpus — gen-133 already has its own independently-evolved
  versions of these. Merging risks canon drift; if you need gen-130's
  version of something specific, go to the live path above and read it
  directly rather than trusting a stale copy here.
- Any `.venv`, `.wrangler`, `.hypothesis`, or other tool-state directories —
  not work-product, not migrated.

## Honest flaw

This snapshot is a point-in-time pointer only two categories deep. If gen-130
accumulates more unique work-product post-freeze under paths other than
`projects/2026-08_cold_outreach_launch/` or root `SIGRUN_*.md`, this README
will not reflect it. Re-run the inventory before assuming completeness.
