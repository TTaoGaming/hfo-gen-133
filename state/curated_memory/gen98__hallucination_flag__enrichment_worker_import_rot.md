---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 98
pattern_type: hallucination_flag
source_path: C:/Dev/hfo_dev_2026_3/hfo_gen_98_forge/archived_root/hfo_ports/p6_assimilate/enrichment_worker.py
source_bytes: 35989
source_sha256: 7988f0912bcff3f9c629cf14ed64578efe9bc31ac81a1ee48c2dc4a650667d1d
source_binding: committed_current repo=C:/Dev/hfo_dev_2026_3 commit=4bad60e18b70232fb2630ded1f3526edb821d0e3 blob=a81bdc139acc029d05ff0b609ab8ec3f081e4de2
content_abstract: P6 enrichment worker whose adjacent test cannot collect because its hfo_core.ssot dependency is absent.
receipt_type: live_pytest_collection_failure
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G98-002; C:/Dev/hfo_dev_2026_3/hfo_gen_98_forge/archived_root/hfo_ports/p6_assimilate/test_enrichment_worker.py sha256=2624303349e0f51cb1b8fe72d83e14fa95e97d9616b7a4f897fb43ed13db2be4
verification_result: collection error ImportError cannot import ssot from hfo_core
evidence_tier: T1_local_committed_negative_replay
proposed_disposition: quarantine_until_import_contract_repaired
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: The receipt diagnoses the current import boundary, not the worker's full semantics.
claim_ceiling: Verified non-runnable at collection in the inspected environment.
---
