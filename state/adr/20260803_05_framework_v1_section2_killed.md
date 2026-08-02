# ADR-20260803-05 — FRAMEWORK_GEN133_V1 §2 (10-17 units/week target) killed

- **Context:** §2 of `state/olrun/FRAMEWORK_GEN133_V1_20260803T010000Z.md` originally read "Target output per week: 10-17 units". Jörmungandr predicted this exact drift as decoration-without-pickup.
- **Decision:** §2 is now marked SUPERSEDED v1.1 with the 1-unit/week cap. The old numbers stay in the doc as a strikethrough with the ⛔-KILLED banner so no future rehydration re-derives them.
- **Consequence:** Any agent that reads FRAMEWORK_GEN133_V1 will hit the ⛔ block before touching the old §2 numbers. Anti-frame-capture: cannot revert without a new ADR.
- **Author:** olrun + Jörmungandr
- **Alternatives considered:** delete §2 outright (rejected — audit trail matters); leave §2 with a footnote (rejected — footnotes get skimmed past).
