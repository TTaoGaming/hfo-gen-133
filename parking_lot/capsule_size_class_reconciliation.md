# PARKED — capsule size-class reconciliation

```yaml
feature: capsule_size_class_reconciliation
status: PARKED — an UNRECONCILED CONFLICT, decide before building
spec: GEN133_FORMAL_SPEC.md §6.1 · contracts/rehydration.contract.md
parked_by: SIGRÚN P4 · 2026-07-30
```

## The conflict

**Two incompatible capsule vocabularies exist in one repository.**

| | classes | where |
|---|---|---|
| already implemented | `S_SMALL` · `M_MEDIUM` · `L_LARGE` · `XL_XLARGE.pointer` | `capsules/sigrun/v1/` — with `build_capsules.py`, `verify_capsules.py`, `CAPSULE_FAMILY_MANIFEST.json`, `VERIFICATION_RECEIPT.json` |
| specified by me | `micro` (~1 KB) · `small` (~10 KB) · `full` (~100 KB) | `GEN133_FORMAL_SPEC.md` §6 |

They do not map onto each other. Four classes versus three, different names,
different implied bounds. I specified mine without reconciling against the
working implementation that was already there — that is a real defect in the
spec, not a difference of taste, and it is flagged rather than smoothed over.

## Why parked

**Because it is a decision, not a build.** Making it silently would either
orphan a working four-class builder or fork the vocabulary permanently. Either
choice is cheap now and expensive after carriers start rehydrating.

## The two options

| option | consequence |
|---|---|
| **A — map onto the existing family**: `S_SMALL→micro`, `M_MEDIUM→small`, `L_LARGE→full`, `XL_XLARGE→pointer` | keeps a working, receipt-bearing builder; the byte bounds must be checked against the actual dist sizes, which I did not measure |
| **B — adopt S/M/L/XL fleet-wide** and rewrite spec §6 | zero code churn; loses the "three consumers, three sizes" rationale that motivated micro/small/full (scheduler tick · fresh session · cold reconstruction) |

My recommendation is **A**, on the grounds that a working builder with a
verification receipt outranks a naming preference in a document written today.
But I did not measure the existing dist file sizes, so I cannot confirm the
bounds fit — and that measurement is step 1 either way.

## Dependencies

- Measure actual byte sizes of `capsules/sigrun/v1/dist/*` (trivial, not done).
- Decide A or B.

## When to revisit

**Before `tools/hfo.py` is written.** Once the ABI ships with one vocabulary,
changing it breaks every capsule digest already in circulation.

## Test

`tests/held_out/rehydration_abi/red_first.md` →
`test_capsule_size_classes_reconciled` is red on exactly this, deliberately.
