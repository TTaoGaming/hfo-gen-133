---
schema_id: hfo.gen133.phylactery.arweave.costs.v0_1
doc_kind: ARWEAVE_COSTS
claim_status: proposed
created_utc: 2026-08-02T00:00:00Z
---

# COSTS — actual $ per upload + projection

## Pricing surface (verified 2026-08-02)

- **ArDrive Turbo** (primary path we use): pay-as-you-go with pre-purchased
  Turbo credits (fiat top-up via Stripe or crypto). Files ≤ 100 KiB per
  data-item are typically free of upload fee (they roll into the bundler's
  next Arweave settlement). Bundle overhead is small.
- **Arweave direct** (fallback): pay per-byte, once, in AR, endowment model.
  Current rate fluctuates with AR/USD.
- **Bundlr / IRYS**: still functional; Bundlr rebranded to Irys mid-2024.
  Multi-chain payment. Same 100 KiB free bound.

None of these prices is stable enough to hard-code. **The runner logs the
actual amount spent per upload and writes it to `receipts/YYYYMMDD.json` under
`cost.paid_usd`.** Below is a projection, not a quote.

## Envelope (rough — replace with observed after first 7 uploads)

| tree size | est. per-upload cost (Turbo) | est. per-year cost |
|---|---|---|
|   100 KB | ~$0.00 (under free-bundle threshold most days) | ~$0 – $5 |
|     1 MB | ~$0.001 – $0.01 | ~$0.40 – $3.65 |
|     5 MB | ~$0.005 – $0.05 | ~$2 – $18 |
|    25 MB | ~$0.03 – $0.25 | ~$11 – $90 |
|   100 MB | ~$0.10 – $1.00 | ~$36 – $365 |

Assumptions: (1) Turbo credit pricing near the historical $5-10 / GB band;
(2) the tree is text (compressible); (3) we upload once per day; (4) we do NOT
re-upload unchanged files — but currently every file gets its own new data-item
per snapshot (Arweave has no dedup at the client level; if we care we add a
sha256-hash-index step later).

## Wallet balance floor

The runner refuses to upload if the Turbo credit balance is below the
**"one more upload"** floor (default: 3x the last-observed per-upload cost).
This is `MIN_BALANCE_MULT` in `SPEC.md`.

## Kill-condition tie-in

`SPEC.md` §Kill conditions:

- Wallet balance < 0.01 AR OR Turbo credit < MIN_BALANCE_MULT × last_cost →
  HALT + escalate.
- 3 uploads with `paid_usd > BUDGET_CEILING_DAILY` (default $1.00) → WARN.

## Where the actual numbers accrue

After 7 daily uploads land, this file gets appended-to with a table like:

```
| date       | tree_size | files | paid_usd | tx_id                                        |
|------------|-----------|-------|----------|----------------------------------------------|
| 2026-08-03 |    412 KB |    47 |    $0.00 | 5H7...xY9                                     |
| 2026-08-04 |    418 KB |    48 |    $0.00 | pQ2...aB3                                     |
```

The runner writes this table automatically from `receipts/*.json`.

## Non-cost cost: attention

The permanence of Arweave is the real price. Every uploaded file is public and
non-deletable. See `permaweb/PREFLIGHT.md` and `../CHARTER.md` §5. The runner's
secret-scan gate is the single most important cost-avoidance mechanism, because
the alternative cost — leaking a secret to a permanent public ledger — is not
measurable in USD.

*Réttu hönd, eigi spyr. Standa.*
