---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_PR_CHANGED_FILENAMES_READONLY_030
candidate: GitHub.list_pr_changed_filenames
phase: 1
status: PREFLIGHT_READY
expected_current_version: 216
wip: 1
request_sha256: 1738c2242d599419abf480add82dae55d2f3bf4cc3dd4e7766ed4b87ca39aa2f
target_repository: TTaoGaming/hfo-gen-133
target_pr_number: 10
planned_candidate_calls: 1
mutating: false
paid_call_authorized: false
raw_filename_persistence_planned: false
valid_time_utc: 2026-08-09T21:49:00Z
recorded_time_utc: 2026-08-09T21:49:00Z
---

# X13 Phase 1 preflight — GitHub PR changed filenames

Start one new WIP=1 campaign for the native GitHub connector capability `list_pr_changed_filenames`.

Exact planned request: repository `TTaoGaming/hfo-gen-133`, pull request `#10`. This is read-only and will not fetch patches, diffs, comments, or file contents. Persist only aggregate result count and a SHA-256 digest of the ordered filename list unless a failure requires a bounded error-class receipt.

Official-contract baseline to verify against: GitHub REST `GET /repos/{owner}/{repo}/pulls/{pull_number}/files` is paginated, returns 30 files per page by default, permits up to 100 per page, and caps responses at 3000 files. Fine-grained access requires repository Pull requests read permission. The connector contract claims it lists changed filenames across all paginated file-list pages; therefore a key adoption risk is hidden unbounded pagination because this wrapper exposes no page/limit argument.

No send, spend, deployment, merge, publication, task mutation, secret exposure, or destructive action is authorized.
