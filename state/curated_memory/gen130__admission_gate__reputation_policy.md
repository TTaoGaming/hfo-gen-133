---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 130
pattern_type: admission_hook_with_test
source_path: C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/scripts/hooks_gen130/pretooluse_gate.py
source_bytes: 28248
source_sha256: 552904c3972e75355a7ae011b38b07d8b8485ed1f20c1577ad0d43c0101664c4
source_binding: local_modified_vs_HEAD repo=C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge historical_head=b857c161a23a7187afaaa999d8f720aaea3fb612 historical_blob=5f091353fab81c84a53ed757aa9700b41cb1b5dc
content_abstract: Pre-tool admission hook that incorporates reputation and reason-first checks before allowing effects.
receipt_type: live_pytest_pass
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G130-001; C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/scripts/hooks_gen130/test_pretooluse_reputation_admission.py sha256=4e3e86ae313138a64868a93741c0553097457c6f142d77b6bc5ffb9f64b6451b
verification_result: included in focused suite with 76 passed
evidence_tier: T0_local_modified_replay
proposed_disposition: isolate_and_commit_exact_bytes_before_consideration
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: Passing unit tests do not prove hook registration or runtime enforcement; bytes differ from HEAD.
claim_ceiling: Byte-hashed dirty-local hook behavior on tests.
---
