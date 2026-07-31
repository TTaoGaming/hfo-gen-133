---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_DBOS_PYTHON_DURABLE_KERNEL_001
version: 1
prior_version: 0
candidate: DBOS_Python
candidate_pin: 2.22.0
phase_completed: 1_of_4
phase_status: CONTINUE_TO_PHASE_2
last_event_commit: 18a9edd9146a0975366a859808d5200f43a8d617
last_event_path: state/coordination/experiments/cots_connector_x13/20260731T214800Z_DBOS_PYTHON_PHASE1_OFFICIAL_CONTRACT_BASELINE.md
next_phase: SMALLEST_HARMLESS_REVERSIBLE_MICRO_USE
next_acceptance: deliberate interruption plus restart produces one nonduplicated state advance and inspectable workflow history
carrier_task_id: 6a55c173370881918680ce67c4ecb197
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_SIGRUN_DISTINCT_REVIEW
consumer: Ratatoskr_and_Olrun
valid_time_utc: 2026-07-31T21:48:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: false
---

# X13 current campaign

DBOS Python remains a **candidate**, not an adopted runtime. Phase 1 found a plausible contract fit for HFO's hot workflow-state gap and recorded the important exactly-once boundary: datasource transactions can atomically bind application writes and durability records, while ordinary nontransactional side effects still require idempotency or compensation.

The next accepted wake must attempt one reversible, deterministic, no-external-effect micro-use. Without a real execution surface it must return `HOLD_EXECUTION_SURFACE`, not a synthetic pass.
