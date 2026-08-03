---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 130
pattern_type: chain_verifier_with_test
source_path: C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/scripts/verify_chain_integrity.py
source_bytes: 15558
source_sha256: 5818077fa5990485e97fadad68237ff2ca0e52b143478aa1cd1422be45329106
source_binding: local_modified_vs_HEAD repo=C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge historical_head=b857c161a23a7187afaaa999d8f720aaea3fb612 historical_blob=e757d64f6b115422e11f781e4ac1a6562fd31970
content_abstract: Chain verifier that checks canonical event hashes and linkage separately instead of inferring integrity from parse success.
receipt_type: live_pytest_pass
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G130-001; C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/scripts/test_verify_chain_integrity.py sha256=a8f039c8977537e16115bbcf8b425718f79258f3b26bdc445bae003833697ebf
verification_result: included in focused suite with 76 passed
evidence_tier: T0_local_modified_replay
proposed_disposition: isolate_and_commit_exact_bytes_before_consideration
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: Local source differs from historical HEAD and verifier success never proves event semantics.
claim_ceiling: Byte-hashed dirty-local verifier behavior on tests.
---
