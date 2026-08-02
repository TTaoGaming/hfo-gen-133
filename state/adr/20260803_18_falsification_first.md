# ADR-20260803-18 — Falsification-first: every unit has kill-criteria at launch

- **Context:** Prior units shipped without explicit kill criteria; several drifted for months at 0-signal without ever getting killed. Popperian falsification is the antidote.
- **Decision:** Every unit ships with a `.placeholder-config.json` (or equivalent yaml block) populated: `success_criterion`, `falsifier`, `decision_by` (max 14 days post-launch), and `kill_rules` (0/100/5/0 pattern from FRAMEWORK_GEN133_V1 §5). No exceptions.
- **Consequence:** Portfolio-level rule: if 5 consecutive units die at "0 impressions" — the template or directory list is broken, fix that before shipping unit 6. Turns silent drift into a hard signal.
- **Author:** olrun (FRAMEWORK_GEN133_V1 §5)
- **Alternatives considered:** kill-criteria as separate PR/ADR (rejected — friction, gets skipped); kill-criteria at 30 days (rejected — too slow, wastes attention).
