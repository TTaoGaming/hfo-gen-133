---
schema_id: hfo.curated_memory.candidate.v1
source_generation: 131
pattern_type: circuit_breaker_with_test
source_path: C:/Dev/.gunnr_tmp_node1_pr95_20260719/work/valkyrie_prey_harness/tools/mesh_circuit_breaker.py
source_bytes: 20380
source_sha256: fd8103880278da2d450ca6ad512f569d414de67047886def5779057f5bd96bc9
source_binding: committed_current repo=C:/Dev/.gunnr_tmp_node1_pr95_20260719 remote=https://github.com/TTaoGaming/hive-fleet-obsidian-gen-131.git commit=0bc7712feaac9ef0a2adb8ed254f09e8e9400b15 blob=4dd2983e8da3761cbba6710fb391575514cddaec
content_abstract: Mesh circuit breaker with explicit failure thresholds and deterministic state transitions.
receipt_type: live_pytest_pass
receipt_pointer: state/heritage_mining/receipts/verification_runs_20260802.md#R-G131-001; C:/Dev/.gunnr_tmp_node1_pr95_20260719/work/valkyrie_prey_harness/tools/test_mesh_circuit_breaker.py sha256=8aedcef78538e258d41679abb10ef932cbbba1f52b9aa7d23d90f1866883daf4
verification_result: included in full harness suite with 165 passed and 1 skipped
evidence_tier: T1_local_committed_replay
proposed_disposition: bring_forward_candidate
sigrun_approved: false
drafted_utc: 2026-08-02T16:45:33Z
honest_flaw: Unit-tested breaker transitions do not prove integration with a live mesh or scheduler.
claim_ceiling: Exact committed breaker behavior on local tests.
---
