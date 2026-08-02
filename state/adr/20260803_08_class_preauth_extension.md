# ADR-20260803-08 — Approvals-parser extended to accept `class:` lines

- **Context:** `tools/olrun/approvals_parser.py` previously accepted only per-instance approval lines. Distribution loops need class-level pre-authorization (operator signs "envelope: 40 contracts" once, not 40 individual lines) per operating-discipline `class-pre-authorization execution` rule.
- **Decision:** Parser extended to recognize `class:` prefix on approval lines and expand them at dispatch time. Test vectors at `tools/olrun/test_approvals_parser.md`. Approval-gate file `state/experiments/approvals/CONTRACTS_EMPLOYMENT_80_READY_20260805.md` uses this format for 80-item envelope.
- **Consequence:** Operator signs one class envelope; Codex/olrun then fires each instance under it without further human touch. Chain rows still emit per-instance receipts.
- **Author:** olrun (implementation), operator (envelope)
- **Alternatives considered:** ask operator per-instance (rejected — throughput ceiling); implicit class approval by directory (rejected — too broad, no scope boundary).
