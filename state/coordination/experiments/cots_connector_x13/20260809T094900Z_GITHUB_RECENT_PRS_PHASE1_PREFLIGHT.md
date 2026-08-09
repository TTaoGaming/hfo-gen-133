---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_RECENT_PRS_READONLY_027
event: PHASE1_PREFLIGHT
expected_task_id: 6a55c1733708819185088bf334e33ea5
expected_current_version: 204
candidate: GitHub_get_users_recent_prs_in_repo_readonly
wip: 1
request_sha256: 28c55b337428c8262d093d9639eab7a81ed987f74a3c7fed877e869f9c9b94cf
valid_time_utc: 2026-08-09T09:49:00Z
recorded_time_utc: 2026-08-09T09:49:00Z
---

# X13 Phase 1 preflight — GitHub recent PR discovery

Candidate request preimage, canonical compact JSON:

`{"include_comments":false,"include_diff":false,"limit":5,"repository_full_name":"TTaoGaming/hfo-gen-133","state":"all"}`

Planned direct call: `GitHub.get_users_recent_prs_in_repo` exactly once. This connector contract says it lists the authenticated user's recent pull requests in a repository and transparently paginates an underlying GitHub search endpoint; diff/comments are explicitly disabled here.

Official baseline: GitHub's current REST API exposes `GET /search/issues`; GitHub documents pull-request filtering with `is:pr`, and search uses a separate rate-limit resource. Current REST API version `2026-03-10` is versioned and breaking changes are date-versioned.

Safety envelope: read-only; repository-scoped; limit 5; no diff; no comments; no issue/PR mutation; no merge; no publication; do not persist PR body/comment text in X13 receipts. Persist only bounded metadata needed to verify count, PR-number digest, state mix, wrapper timing, and error surface.

Measure: custom code avoided estimate vs realized, operator minutes, connector-managed credentials/effective principal unknown, durability via Git event/readback, observability fields actually surfaced, portability to native GitHub search semantics, failure behavior deferred to Phase 3, direct cost/quota evidence only if exposed, strongest falsifier, verifier, consumer, honest flaw.
