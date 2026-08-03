---
capsule_id: "a93a7076be9e"
title: "20260626T1651Z_JOB_OUTREACH_FANIN_001_gate_admissible_close.json"
source_store: "sigrun_recall_gen130"
source_path: "C:\\Dev\\hfo_dev_2026_5_30\\hfo_gen_130_forge\\inbox\\gunnr\\20260626T1651Z_JOB_OUTREACH_FANIN_001_gate_admissible_close.json"
source_generation: 130
topic: "outreach client"
bm25_score: -8.974063914204319
harvested_utc: "2026-08-02T15:05:47Z"
clock_source: "host_read"
sigrun_approved: false  # set true only by an approval pass
quorum_votes: []  # filled by multi_family_vote.py
concurrence_score: null
rehydration_probe: "test -f \"C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/inbox/gunnr/20260626T1651Z_JOB_OUTREACH_FANIN_001_gate_admissible_close.json\""
---

# 20260626T1651Z_JOB_OUTREACH_FANIN_001_gate_admissible_close.json

{
  "job_id": "JOB-OUTREACH-FANIN-001",
  "utc": "2026-06-26T16:51:00Z",
  "from": "gunnr_tactical",
  "lane": "outreach",
  "status": "done",
  "claim": "done",
  "claim_status": "wired_with_receipts",
  "worker": "Mist",
  "worker_call_sign": "Mist",
  "canonical_chain": "chains/mission_threads/mist_outreach.jsonl",
  "acceptance_gate": "One no-send packet status report plus bad unsupported resume/client claim denied by eval/gate; verifier_result transcript exit0; send, publish, spend, and apply are all false.",
  "verifier_result": {
    "effect_type": "transcript",
    "exit_code": 0,
    "held_out": true,
    "self_graded": false,
    "verifier_lane": "Mist deterministic local gate",
    "command": "tools\\hfo-python.cmd work\\fanin\\outreach\\outreach_fanin_no_send_gate_smoke.py",
    "transcript_path": "work\\fanin\\outreach\\outreach_fanin_no_send_gate_smoke.receipt.json",
    "summary": "No-send packet status report present; unsupported resume/client claim denied; send/publish/spend/apply all false."
  },
  "outputs": {
    "no_send_report": "work\\fanin\\outreach\\OUTREACH_FANIN_NO_SEND_CLAIM_GATE.md",
    "receipt": "work\\fanin\\outreach\\outreach_fanin_no_send_gate_smo

[... abstract truncated at 1200 chars; see source ...]

## Why this survived

bm25-ranked hit for topic `outreach client` in `sigrun_recall_gen130` (score -8.9741; lower is a stronger match). Candidate only -- `sigrun_approved: false` until an approval pass and cross-family quorum vote say otherwise.
