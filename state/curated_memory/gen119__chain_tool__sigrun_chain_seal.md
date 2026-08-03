---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 119
pattern_type: chain_tool_with_test
source_path: C:/Dev/hfo_dev_2026_5_19/hfo_forge_gen_119/scripts/sigrun_chain_seal.py
source_bytes: 17810
source_sha256: 4dcd2f0a21513a2d8eafa0a10fc3a7c73a97ec857c5bcfd811233d6fce105645
source_binding: local_uncommitted_unbound
content_abstract: Chain-sealing utility with explicit integrity fields and local test coverage.
receipt_type: live_pytest_pass_within_partial_suite
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G119-001; C:/Dev/hfo_dev_2026_5_19/hfo_forge_gen_119/tests/test_sigrun_chain_seal.py sha256=de3eba6119e31c6f3cc3e574e87547a9a923dc30fa33d5ada7ef5e64a77985d8
verification_result: named seal tests passed; aggregate suite 103 passed and 1 unrelated configuration assertion failed
evidence_tier: T0_local_unbound_replay
proposed_disposition: repair_provenance_then_consider
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: Local sealing mechanics do not establish key custody, signer identity, or canonical authority.
claim_ceiling: Byte-hashed local seal behavior on tests.
---
