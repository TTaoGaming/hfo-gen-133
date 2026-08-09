---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_RECENT_PRS_READONLY_027
event_type: PHASE2_PREFLIGHT
campaign_wake: 2_of_4
candidate: GitHub_get_users_recent_prs_in_repo_readonly
expected_current_version: 205
wip: 1
request_sha256: 28c55b337428c8262d093d9639eab7a81ed987f74a3c7fed877e869f9c9b94cf
request_sha256_matches_phase1: true
request_canonical_json: '{"include_comments":false,"include_diff":false,"limit":5,"repository_full_name":"TTaoGaming/hfo-gen-133","state":"all"}'
allowed_comparison: result_count;ordered_pr_number_sha256;state_open_count;draft_true_count;merged_true_count;body_text_returned_despite_minimal_request
repository_drift_allowed: true
mutation_allowed: false
persistence_gate: DO_NOT_PERSIST_PR_BODY_OR_COMMENT_TEXT
valid_time_utc: 2026-08-09T10:47:00Z
recorded_time_utc: 2026-08-09T10:47:00Z
---

# X13 GitHub Recent PRs Phase 2 Preflight

Replay the Phase-1 request exactly once. Compare only bounded aggregate/result-order evidence and the existing data-minimization Andon. Ordinary repository drift is allowed and must not be misclassified as connector instability.

No PR mutation, diff fetch, comment fetch, body persistence, pagination expansion, retry, or fallback is authorized.
