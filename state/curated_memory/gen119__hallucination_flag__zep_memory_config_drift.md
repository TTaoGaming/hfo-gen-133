---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 119
pattern_type: hallucination_flag
source_path: C:/Dev/hfo_dev_2026_5_19/hfo_forge_gen_119/scripts/zep_memory_safety.py
source_bytes: 9052
source_sha256: 08919dd8d4281cadfc2089ee84253c75b3206baf3e58c07c2b28b25374463946
source_binding: local_uncommitted_unbound
content_abstract: Safety checker whose static server allowlist has drifted from compose/MCP configuration.
receipt_type: live_pytest_assertion_failure
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G119-001; C:/Dev/hfo_dev_2026_5_19/hfo_forge_gen_119/tests/test_zep_memory_safety.py sha256=939f799c8891a6e4a0e500cb6e94fbd584a6f753e0f3e7a1630faffa684998d3
verification_result: static pin assertion failed for hfo-sigrun-memory and hfo-sigrun-memory-http-local
evidence_tier: T0_local_unbound_negative_replay
proposed_disposition: quarantine_until_config_contract_reconciled
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: The failing test proves configuration drift in this snapshot, not whether a service is live elsewhere.
claim_ceiling: Local configuration inconsistency only.
---
