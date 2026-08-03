---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 131
pattern_type: secrets_gate_with_test
source_path: C:/Dev/.gunnr_tmp_node1_pr95_20260719/work/valkyrie_prey_harness/tools/sigrun_secrets_env.py
source_bytes: 31139
source_sha256: 990ddd7eea760122111a6084ba9f7af0780571b23182f5eef8ade94b6b3111a9
source_binding: committed_current repo=C:/Dev/.gunnr_tmp_node1_pr95_20260719 remote=https://github.com/TTaoGaming/hive-fleet-obsidian-gen-131.git commit=0bc7712feaac9ef0a2adb8ed254f09e8e9400b15 blob=7f0294925af0e5447cc2ab588f819ee01bd81f4f
content_abstract: Environment-facing secret-loading boundary with redaction and fail-closed validation tests.
receipt_type: live_pytest_pass
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G131-001; C:/Dev/.gunnr_tmp_node1_pr95_20260719/work/valkyrie_prey_harness/tools/test_sigrun_secrets_env.py sha256=eaaf7be534f7d5ed8d7a71e3c38c6a4a9c855a84b0aa271c0c8397470bac60b0
verification_result: included in full harness suite with 165 passed and 1 skipped
evidence_tier: T1_local_committed_replay
proposed_disposition: bring_forward_candidate
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: Tests use controlled inputs and do not prove production key custody, rotation, or absence of every leak path.
claim_ceiling: Exact committed environment-boundary behavior on local tests.
---
