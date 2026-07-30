# PARKED — pre-registered evolutionary experiment registry

```yaml
feature: experiment_registry
status: PARKED — UNDER_SPECIFIED
spec: GEN133_FORMAL_SPEC.md §13
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

Make the breeding of agent lineages **measurable** rather than merely real.

The operator has been running an evolutionary process by hand for ~130
generations — mutate phenotypes, select champions, carry the genotype forward.
That process is real. Its **measurement** does not exist: no experiment has ever
been pre-registered, no fitness has ever been logged as a time series.

**EV-3:** before a phenotype mutation, write `{hypothesis, metric, threshold,
duration}`. A result interpreted after the fact is a story.

## Schema sketch

```jsonc
{ "schema_id": "hfo.gen133.experiment.v1",
  "experiment_id": "…",
  "hypothesis": "…falsifiable, written BEFORE the mutation…",
  "arm_control":   { "songline": "…", "phenotype_sha256": "…" },
  "arm_treatment": { "songline": "…", "phenotype_sha256": "…" },
  "metric": "external_receipts",       // EV-1: MUST be externally observable
  "threshold": 1,
  "duration_days": 14,
  "registered_utc": "…",
  "result": null,                      // written only after duration elapses
  "verdict": null }                    // STOOD | FELL
```

## Why parked

Two reasons, and the second is the real one.

1. There is no fitness time series to run an experiment against.
2. **EV-1: fitness must be externally observable.** A metric computable entirely
   inside the fleet is a metric the fleet can game — `tests_passing`,
   `rows_written`, `capsules_built` are *activity*, not fitness. The only genuine
   external metric available is `cap-0018`, and it is **FAILED: $0 external
   income, 18 months, 0 external receipts.**

An experiment registry over internal metrics would be a machine for producing
confident-sounding results about nothing.

## Dependencies

| # | dependency |
|---|---|
| 1 | at least one externally-observable fitness metric that is not already zero |
| 2 | rollups carrying `fitness` as a time series (§5.2 has the field; nothing writes it) |
| 3 | EV-2 archival discipline — losing arms move to `archives/`, never deleted. You cannot run an experiment whose losing arms are destroyed; that is selection without a control. |

## When to revisit

When a single external receipt exists. Until `cap-0018` moves off zero, the
population has exactly one selection pressure and it is not being measured — it
is being *failed*, consistently, which is itself the most informative result the
system has produced.
