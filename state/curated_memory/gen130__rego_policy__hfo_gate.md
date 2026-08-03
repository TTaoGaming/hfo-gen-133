---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 130
pattern_type: rego_policy_with_adjacent_tests
source_path: C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/work/policy_gate_gen130/policies/hfo_gate.rego
source_bytes: 82041
source_sha256: cec96ccd8db1e86f09379d94451883c837b08e0a26533d9daa60b52e5c5c4a2f
source_binding: local_modified_vs_HEAD repo=C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge historical_head=b857c161a23a7187afaaa999d8f720aaea3fb612 historical_blob=8911e32c8ad60311006df9c71820d7e78378e27f
content_abstract: Central OPA gate policy with an adjacent Rego test corpus covering the policy package.
receipt_type: live_opa_test_pass
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G130-002; C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/work/policy_gate_gen130/policies/hfo_gate_test.rego sha256=4f3591c0d5c2d6d18f15f219779afcac79e973239fe57dd377973e76ffe5f469
verification_result: PASS 294/294 across policy directory
evidence_tier: T0_local_modified_replay
proposed_disposition: isolate_and_commit_exact_bytes_before_consideration
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: Policy tests passed on dirty-local bytes and do not prove deployment or enforcement at any decision point.
claim_ceiling: Byte-hashed local policy behavior under OPA tests.
---
