---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 98
pattern_type: hallucination_flag
source_path: C:/Dev/hfo_dev_2026_3/hfo_gen_98_forge/archived_root/hfo_ports/hourly/sweep_engine.py
source_bytes: 53818
source_sha256: 26bc79bc6a748efd7e2a6a9331588e56af9af177c2ef09da5180775b1ccb267c
source_binding: committed_current repo=C:/Dev/hfo_dev_2026_3 commit=4bad60e18b70232fb2630ded1f3526edb821d0e3 blob=554b8eeb359fd87f256617f960516d11b2709eb0
content_abstract: Large hourly sweep implementation whose adjacent test cannot collect because the expected hfo_core.ssot import no longer exists.
receipt_type: live_pytest_collection_failure
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G98-002; C:/Dev/hfo_dev_2026_3/hfo_gen_98_forge/archived_root/hfo_ports/hourly/tests/test_sweep_engine.py sha256=e9693107e953271781dd63c63f65717287ddd95bdb5976a5137f333b4d117716
verification_result: collection error ImportError cannot import ssot from hfo_core
evidence_tier: T1_local_committed_negative_replay
proposed_disposition: quarantine_until_import_contract_repaired
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: The failure proves current test rot, not that every internal sweep algorithm is unsound.
claim_ceiling: Verified non-runnable at collection in the inspected environment.
---
