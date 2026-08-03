---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 101
pattern_type: hallucination_flag
source_path: C:/Dev/hfo_dev_2026_4/HFO_GEN_101_FORGE/omega_product/tile_printing/tile_printer.py
source_bytes: 28809
source_sha256: 379104f520e64d4baaf8b3998dfc4d4ad806d9716c56bb82160202f1c46ec919
source_binding: local_untracked_no_commit_binding
content_abstract: Tile registry and printer implementation with a verified duplicate slot-address defect in the current COTS map.
receipt_type: live_pytest_partial_failure
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G101-001; C:/Dev/hfo_dev_2026_4/HFO_GEN_101_FORGE/omega_product/tile_printing/test_tile_printer.py sha256=149f9b364dd9fa57d566ab67dea192a4adc3fbac119ad32e7a4586cb979f276a
verification_result: 16 passed and 1 failed; 27 addresses but 26 unique
evidence_tier: T0_local_unbound_negative_replay
proposed_disposition: quarantine_registry_until_collision_repaired
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: Most focused tests pass, but there is no committed-object binding and the uniqueness invariant fails.
claim_ceiling: Local defect reproduction only.
---
