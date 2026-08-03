---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 119
pattern_type: hook_with_test
source_path: C:/Dev/hfo_dev_2026_5_19/hfo_forge_gen_119/.claude/hooks/pre_write_no_truncation_check.py
source_bytes: 7809
source_sha256: c99885f6c982688d38ed14fbc14e0c0a2f72453e09cc5d5fb099867398668df1
source_binding: local_uncommitted_unbound
content_abstract: Pre-write guard intended to reject truncating writes against append-only or protected artifacts.
receipt_type: live_pytest_pass_within_partial_suite
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G119-001; C:/Dev/hfo_dev_2026_5_19/hfo_forge_gen_119/tests/test_no_truncation_hook.py sha256=277bb131f469ad087863ed1a45f1242b7546101788c78df6d2e28cc406e47a80
verification_result: named hook tests passed; aggregate suite 103 passed and 1 unrelated configuration assertion failed
evidence_tier: T0_local_unbound_replay
proposed_disposition: repair_provenance_then_consider
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: Hook tests do not prove installation, registration, or enforcement in another runtime.
claim_ceiling: Byte-hashed local hook behavior on fixtures.
---
