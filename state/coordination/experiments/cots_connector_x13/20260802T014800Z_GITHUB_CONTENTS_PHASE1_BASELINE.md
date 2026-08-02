---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GITHUB_CONTENTS_CONNECTOR_001_PHASE1_20260802T014800Z
experiment_id: X13_GITHUB_CONTENTS_CONNECTOR_001
candidate: GitHub_contents_API_branch_scoped_file_create_update_fetch_and_readback_connector
phase: 1_of_4
decision: PHASE1_BASELINE_ACCEPTED_WITH_BRANCH_REF_AND_QUOTA_VISIBILITY_GATES
prior_current_version: 28
expected_current_version: 29
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T01:48:00Z
branch: agent/gen133-bootstrap-20260730
effect_ceiling: BRANCH_SCOPED_TEXT_EVENT_AND_READBACK_ONLY
---

# GitHub Contents connector phase 1

A branch-scoped `GitHub.fetch_file` read the existing X13 `CURRENT.md` from `TTaoGaming/hfo-gen-133` at ref `agent/gen133-bootstrap-20260730`.

## Direct receipt

- path: `state/coordination/experiments/cots_connector_x13/CURRENT.md`
- result: `SUCCESS_FILE_CONTENT`
- encoding: `utf-8`
- returned blob SHA: `24fa0c71d82268d4908a2d52c2c4b6f861d2eb0b`
- returned state version: `28`
- branch-qualified display URL returned: true
- response headers, request ID, request count, latency, retry count, authenticated identity, permission set, and rate-limit values exposed: false
- operator relay minutes: `0`
- operator minutes removed measured: `0`
- paid cost surfaced: `$0`; billing and quota counters were not exposed

This proves only that this wrapper could retrieve one known UTF-8 file from one named branch and return its body plus blob SHA.

## Official contract checked 2026-08-02

GitHub documents that repository-content reads accept a commit, branch, or tag ref; omission uses the default branch. Fine-grained reads require `Contents: read` for non-public access. Full endpoint features apply through 1 MB; 1–100 MB requires raw or object media types; larger than 100 MB is unsupported.

Create/update uses the repository Contents endpoint with a commit message and Base64 content. Updating requires the current blob SHA. The branch parameter is optional and otherwise defaults to the default branch. Fine-grained writes require `Contents: write`; workflow-file changes require additional permission. GitHub warns that create/update and delete operations must be serialized because concurrent calls can conflict.

GitHub's general REST limits vary by authentication class. Public unauthenticated access is documented at 60 requests/hour and authenticated-user access at 5,000/hour, with other app and enterprise classes differing. Most reads and writes also consume secondary-limit points. This connector did not expose headers or identity, so no live quota class is claimed.

## Measurements

- direct candidate read invocations: `1`
- custom code avoided estimate: `40–120 LOC`, unvalidated
- estimated operator relief per bounded event and readback: `1–4 minutes`, unvalidated
- durability: Git object and branch history only; no workflow replay, resume, transaction, or exactly-once claim
- observability: medium for path, ref, body, blob SHA, and display URL; low for headers, latency, retries, identity, and quota
- portability: medium for repository/path/ref/body/blob concepts; lower for GitHub-specific permissions and wrapper shape
- verifier: structural readback plus distinct non-carrier review
- consumer: X13 phase 2 and Git-first state readers
- strongest falsifier: a commit-pinned independent read disagrees with the body or blob SHA, or a branch-variance probe shows that the wrapper ignored the requested ref
- honest flaw: the baseline used a known state file and the same wrapper will perform bookkeeping writes, so this is not independent verification

## Gates

1. Always pass an explicit branch or commit ref for canonical state.
2. Require the current blob SHA before update and serialize writes to one path.
3. Treat event creation and pointer update as two commits, not an atomic transaction.
4. Read back the exact event and `CURRENT.md`; compare expected version, path, and blob SHA.
5. Do not claim independent verification from same-connector readback.
6. No merge, delete, force-push, branch creation, workflow edit, or production effect.
7. Keep artifacts small and text-only.
8. Make no live quota or cost claim without direct evidence.

## Next

Phase 2: create one uniquely named harmless text artifact on the existing experiment branch, fetch it back, compare body and blob SHA, and update `CURRENT.md` serially.
