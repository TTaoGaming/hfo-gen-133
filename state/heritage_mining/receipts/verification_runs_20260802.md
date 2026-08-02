# Heritage mining verification runs — 2026-08-02

This is the durable local readback for the candidate capsules drafted at
`2026-08-02T16:45:33Z`.  All commands were run against the source in place.
Passing a local replay proves only the cited source/test relationship; it does
not ratify lineage, authorship, deployment, identity continuity, or Sigrún
approval.

## R-G98-001 — P1 quarantine focused replay

- cwd: `C:/Dev/hfo_dev_2026_3/hfo_gen_98_forge/archived_root`
- command: `python -m pytest -q -p no:cacheprovider hfo_ports/p1_bridge/test_p1_quarantine.py`
- raw terminal summary: `9 passed in 0.34s`
- exit code: `0`

## R-G98-002 — stale hourly/enrichment imports

- cwd: `C:/Dev/hfo_dev_2026_3/hfo_gen_98_forge/archived_root`
- command: `python -m pytest -q -p no:cacheprovider hfo_ports/hourly/tests/test_sweep_engine.py hfo_ports/p6_assimilate/test_enrichment_worker.py`
- raw terminal summary: `2 errors during collection`
- error 1: `ImportError: cannot import name 'ssot' from 'hfo_core'` while collecting `test_sweep_engine.py`
- error 2: `ImportError: cannot import name 'ssot' from 'hfo_core'` while collecting `test_enrichment_worker.py`
- exit code: nonzero

## R-G101-001 — tile printer collision replay

- cwd: `C:/Dev/hfo_dev_2026_4/HFO_GEN_101_FORGE/omega_product/tile_printing`
- command: `python -m pytest -q -p no:cacheprovider test_tile_printer.py`
- raw terminal summary: `1 failed, 16 passed in 0.20s`
- failing assertion: `test_8ary_no_collision`; 27 registered addresses, 26 unique
- exit code: `1`

## R-G107-001 — gesture pointer bridge replay

- cwd: `C:/Dev/hfo_dev_2026_4_2/hfo_gen_107_forge/spatial_os_push/active/gesture-pointer-bridge`
- command: `npm.cmd test`
- raw terminal summary: `tests 31`, `pass 31`, `fail 0`
- exit code: `0`
- environment note: first sandbox attempt hit `spawn EPERM`; the identical command succeeded outside that restriction.

## R-G111-001 — focused schema and assurance suite

- cwd: `C:/Dev/hfo_dev_2026_5_6/hfo_gen_111_forge`
- command: `python -m pytest -q -p no:cacheprovider tests/test_t1_jsonl_parse.py tests/test_t2_issue_template.py tests/test_t3_pr_template_proof.py tests/test_t5_adapter_card_schema.py tests/test_t7_assurance_card_gate.py tests/test_t9_valkyrie_vote_schema.py tests/test_t10_quorum_receipt.py tests/test_gen108_stigmergy_reader.py`
- raw terminal summary: `161 passed, 2 xfailed in 1.02s`
- exit code: `0`
- scope note: a broader suite had unrelated failures/errors; this receipt is deliberately limited to the named focused set.

## R-G114-001 — policy adjacency rejection

- root: `C:/Dev/hfo_dev_2026_5_14/hfo_gen_114_forge`
- inspection: `policies/worker_scope.rego`, `policies/spore.rego`, and `policies/promotion.rego` exist.
- result: no adjacent Rego test or policy probe was found; zero capsules staged.

## R-G119-001 — focused heritage and memory suite

- cwd: `C:/Dev/hfo_dev_2026_5_19/hfo_forge_gen_119`
- command: focused pytest over audit-chain, inventory, migration, seal, lineage, ingest, bridge, safety, no-truncation, and chain-write-discipline tests
- raw terminal summary: `1 failed, 103 passed, 1 warning in 42.20s`
- sole failure: `test_static_pin_matches_compose_and_mcp_config`; missing MCP server pins `hfo-sigrun-memory` and `hfo-sigrun-memory-http-local`
- exit code: `1`
- binding note: this directory did not yield a Git worktree binding, so even passing artifacts remain T0 local candidates.

## R-G120-001 — archive index discovery only

- path: `C:/Dev/archive/GEN120_OLDER_GENERATIONS_ARCHIVE_INDEX_20260520T161243Z.md`
- bytes: `3476`
- sha256: `8aff72639d2345caa8768daa8993c370343810997162525387dac200fd8dee45`
- result: prose/path inventory only; used as a search map, not promoted as a receipt-backed pattern.

## R-G124-001 — signature pad replay

- cwd: `C:/Dev/hfo_dev_2026_5_24/hfo_gen_124_forge`
- command: `node work/factory/spatial_os/same_origin_apps/tests/signature_pad_golden_mp4_replay_gate.mjs`
- raw status: `SIGNATURE_PAD_BROWSER_INK_GREEN`
- observed: 309 pointer events; application state changed from empty to nonempty
- explicit ceiling: `live_camera_proven=false`, `product_claim_proven=false`
- exit code: `0`

## R-G124-002 — Excalidraw replay

- command: `node work/factory/spatial_os/same_origin_apps/tests/excalidraw_golden_mp4_replay_gate.mjs`
- raw status: `EXCALIDRAW_BROWSER_ADAPTER_STATE_GREEN`
- observed: 309 rows; element count changed from 0 to 2
- explicit ceiling: `live_camera_proven=false`, `product_claim_proven=false`
- exit code: `0`

## R-G124-003 — table-tennis replay

- command: `node work/factory/spatial_os/same_origin_apps/tests/table_tennis_golden_mp4_replay_gate.mjs`
- raw status: `GOLDEN_MP4_TO_TABLE_TENNIS_OBSERVED_STATE_GREEN`
- observed: 464 pointer-L2 rows; 224 nonprimary intents suppressed; application state changed
- explicit ceiling: `live_camera_proven=false`, `dom_dispatch_proven=false`
- exit code: `0`

## R-G124-004 — clean signature-pad replay

- command: `node work/factory/spatial_os/same_origin_apps/tests/signature_pad_clean_golden_mp4_replay_gate.mjs`
- raw status: `SIGNATURE_PAD_CLEAN_REPLAY_VISUAL_STROKE`
- observed: 309 rows, 156 stroke points, nonzero bounding box
- explicit ceiling: replay/live-shadow only
- exit code: `0`

## R-G124-005 — kinematic physics replay

- command: `node work/factory/spatial_os/runtime/humanjs_probe/PhysicsKinematicGateAdapter.v0_1.test.mjs`
- raw result: `ok=true`, `assertions=16`, `engine=planck`, `replay_only=true`
- observed cases: teleport bounds, static obstacle, lost frame, deterministic replay, DOM-free path
- exit code: `0`

## R-G130-001 — focused append, chain, and admission suite

- cwd: `C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge`
- command: focused pytest over `bb_append` no-fake-green/concurrency/body-file/verify gates, chain-integrity, and pre-tool reputation admission
- raw terminal summary: `76 passed in 16.17s`
- exit code: `0`
- binding note: tested source bytes differ from historical HEAD `b857c161a23a7187afaaa999d8f720aaea3fb612`; candidates remain T0.

## R-G130-002 — OPA policy suite

- cwd: `C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge`
- command: `opa test work/policy_gate_gen130/policies -v`
- raw terminal summary: `PASS: 294/294`
- exit code: `0`
- binding note: tested Rego bytes differ from historical HEAD; candidate remains T0.

## R-G132-001 — generation label reconciliation

- inspected root: `C:/Dev/.gunnr_tmp_node1_pr95_20260719/work/valkyrie_prey_harness`
- Git root: `C:/Dev/.gunnr_tmp_node1_pr95_20260719`
- remote: `https://github.com/TTaoGaming/hive-fleet-obsidian-gen-131.git`
- commit: `0bc7712feaac9ef0a2adb8ed254f09e8e9400b15`
- result: Jörmungandr's gen-132 label is not used for provenance; the committed source is staged as gen-131.

## R-G131-001 — stranded harness full replay

- cwd: `C:/Dev/.gunnr_tmp_node1_pr95_20260719/work/valkyrie_prey_harness`
- command: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q -p no:cacheprovider tools`
- raw terminal summary: `165 passed, 1 skipped in 14.62s`
- exit code: `0`
- source binding: committed-current at `0bc7712feaac9ef0a2adb8ed254f09e8e9400b15`

## R-G133-001 — reliquary existence check

- path tested: `C:/Dev/hfo_gen_133_forge/heritage_reliquary`
- result: absent at inspection time; zero capsules sourced from that optional root.
