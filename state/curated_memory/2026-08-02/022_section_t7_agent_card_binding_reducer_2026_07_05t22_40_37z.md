---
capsule_id: "fab4e009f9cc"
title: "Section T7 Agent Card Binding Reducer - 2026-07-05T22:40:37Z"
source_store: "sigrun_recall_gen130"
source_path: "C:\\Dev\\hfo_dev_2026_5_30\\hfo_gen_130_forge\\inbox\\var\\SECTION_T7_AGENT_CARD_BINDING_REDUCER_20260705T224037Z.md"
source_generation: 130
topic: "agent card"
bm25_score: -11.006634036639621
harvested_utc: "2026-08-02T15:05:47Z"
clock_source: "host_read"
sigrun_approved: false  # set true only by an approval pass
quorum_votes: []  # filled by multi_family_vote.py
concurrence_score: null
rehydration_probe: "test -f \"C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/inbox/var/SECTION_T7_AGENT_CARD_BINDING_REDUCER_20260705T224037Z.md\""
---

# Section T7 Agent Card Binding Reducer - 2026-07-05T22:40:37Z

```yaml
schema_id: hfo.gen130.section_t7.agent_card_binding_reducer.v0_1
receipt_id: SECTION_T7_AGENT_CARD_BINDING_REDUCER_20260705T224037Z
source_thread_id: 019f190f-3e26-7853-8560-e3c88d7d1a55
role: T7 Rollup / SSOT section-chief card binding reducer
valid_time_utc: 2026-07-05T22:40:00Z
transaction_time_utc: 2026-07-05T22:40:37Z
claim_status: REDUCER_ONLY__T1_T4_SAFE_TO_BIND__T0_T2_T3_T5_T6_T7_HOLD__SPINE_NOT_UPDATED
claim_ceiling: reducer recommendation only; not spine update; not runtime green; not send/runtime/memory/disk/arweave green; not authority expansion
safe_to_bind_count: 2
hold_count: 6
spine_updated: false
world_effects_performed_by_t7:
  wrote_this_receipt: true
  other_world_effects: false
  spine_update: false
  card_file_update: false
  send_spend_publish_deploy_push_seal: false
  login_dns_account_mutation: false
  cleanup_delete_move_format_upload: false
  secret_readback_or_private_payload_read: false
```

## Binding Reducer Rule

Only replace `agent_card_path: MISSING` when the binding manifest row has:

1. high confidence;
2. direct `card_match` or `registry_and_card_match`;
3. no split-lane/conflict/mismatch caveat;
4. primary card path exists and SHA256 ma

[... abstract truncated at 1200 chars; see source ...]

## Why this survived

bm25-ranked hit for topic `agent card` in `sigrun_recall_gen130` (score -11.0066; lower is a stronger match). Candidate only -- `sigrun_approved: false` until an approval pass and cross-family quorum vote say otherwise.
