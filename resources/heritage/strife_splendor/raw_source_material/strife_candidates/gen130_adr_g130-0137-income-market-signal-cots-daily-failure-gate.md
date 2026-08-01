# ADR g130-0137 - Income Market-Signal + COTS Daily Failure Gate

status: proposed_with_green_harness_current_business_red
date: 2026-06-28
owner: Olrun
decision_type: executable_policy_gate
claim_ceiling: gate wiring and fixture verification only; current income condition intentionally remains red

## Context

The forge has produced substantial internal proof: COTS receipts, red-first eval gates, ADRs, orchestration plans, and no-send outreach packets. The external-fitness ledger still records no paid outcome, and the operator readback is that income remains `$0`.

Prior gates correctly block unsafe send/spend/publish behavior, but they do not make `$0 income` a daily red condition. That lets no-send preparation look productive without forcing the market loop to surface as red.

## Decision

Adopt a daily executable gate for the `outreach_income` mission thread.

The gate fails when any of these are true:

1. `income.today_usd <= 0`
2. no approved external market signal is observed
3. any COTS marked `required_for_income_gate=true` is not runtime-wired with a receipt and witness

No-send preparation does not count as a market signal. Downloaded-only or held COTS do not count as wired.

## Enforced Artifacts

- Python verifier: `work/hfo_prey_workflow/income_market_signal_gate_20260628/verify_income_market_signal_gate.py`
- Current daily status: `work/hfo_prey_workflow/income_market_signal_gate_20260628/daily_income_status_current.json`
- Missing COTS log: `work/hfo_prey_workflow/income_market_signal_gate_20260628/missing_cots_log_current.json`
- Missing COTS readback: `work/hfo_prey_workflow/income_market_signal_gate_20260628/MISSING_COTS_LOG_CURRENT.md`
- Test suite: `work/hfo_prey_workflow/income_market_signal_gate_20260628/test_income_market_signal_gate.py`
- Rego policy: `canon/adr/policies/income_market_signal_gate_0137.rego`
- Fixtures: `canon/adr/fixtures/income_market_signal_gate_0137/`

OPA query:

```text
data.hfo.income_market_signal_gate.decision
```

## Failure Codes

- `L_ZERO_INCOME_DAILY_FAILURE`: daily income is still zero.
- `L_NO_MARKET_SIGNAL`: no approved external market signal exists; no-send-only work is red for income.
- `L_COTS_UNWIRED`: a required income COTS is downloaded/staged/held/prose-claimed instead of runtime-wired with receipt and witness.
- `L_COTS_MISSING`: research-required income COTS is absent, held, or not wired.
- `L_REQUIRED_COTS_CATEGORY_UNWIRED`: an entire required GTM category has no runtime-wired implementation.
- `L_MISSING_COTS_RESEARCH_REF`: a missing-COTS claim lacks a cited local research source.
- `L_BAD_SCHEMA`: the daily status did not use the contract schema.

## Consequences

The gate's own tests may pass while the current daily business condition fails. That is intended. Green verifier wiring means the test harness and policy work; it does not mean the business has income.

The expected current condition is red until at least one paid outcome is recorded, at least one approved external signal is present, and all required income COTS are runtime-wired or explicitly removed from the income gate.

## Verification

Red-first observed:

```text
python work/hfo_prey_workflow/income_market_signal_gate_20260628/test_income_market_signal_gate.py
```

Initial result: failed because `verify_income_market_signal_gate.py` was absent.

Green target:

```text
python work/hfo_prey_workflow/income_market_signal_gate_20260628/test_income_market_signal_gate.py
```

Observed after implementation:

```text
Ran 6 tests in 0.380s
OK
```

Current daily red target:

```text
python work/hfo_prey_workflow/income_market_signal_gate_20260628/verify_income_market_signal_gate.py --status work/hfo_prey_workflow/income_market_signal_gate_20260628/daily_income_status_current.json --missing-cots-log work/hfo_prey_workflow/income_market_signal_gate_20260628/missing_cots_log_current.json
```

Expected: non-zero exit and clean findings, including `L_ZERO_INCOME_DAILY_FAILURE`.

Observed current daily receipt:

```text
work/hfo_prey_workflow/income_market_signal_gate_20260628/daily_income_status_current.receipt.json
```

Current status is `FAIL` with `L_ZERO_INCOME_DAILY_FAILURE`, `L_NO_MARKET_SIGNAL`, `L_COTS_UNWIRED`, `L_COTS_MISSING`, and `L_REQUIRED_COTS_CATEGORY_UNWIRED`.

As of this update, the missing-COTS log records 13 GTM COTS gaps; 10 are required for the income gate.
