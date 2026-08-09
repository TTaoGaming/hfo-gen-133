---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_BRANCH_SEARCH_READONLY_025
event_type: PHASE1_PREFLIGHT
expected_current_version: 196
candidate: GitHub_search_branches_readonly
campaign_wake: 1_of_4
wip: 1
valid_time_utc: 2026-08-09T01:49:04Z
recorded_time_utc: 2026-08-09T01:49:04Z
request_sha256: fcf48deba34027fe7f23bbf28db29d34f3f4847e3a5317be606480f49039ce6f
mutation_allowed: false
---

# X13 GitHub Branch Search Phase 1 Preflight

One bounded read-only connector call is authorized after this preflight is read back and the request digest is verified.

Canonical request preimage:

```json
{"cursor":null,"owner":"TTaoGaming","page_size":5,"query":"agent/gen133-bootstrap-20260730","repo_name":"hfo-gen-133"}
```

Safety boundary: repository/branch metadata read only; no branch creation, deletion, protection change, merge, publication, secret access, or task mutation.

Official baseline before direct use: GitHub REST `GET /repos/{owner}/{repo}/branches` is read-only, supports `per_page` up to 100 and page-number pagination, returns 200 or 404, and for private resources requires repository Contents read permission for fine-grained tokens. The available connector exposes an additional query string plus opaque cursor contract, so wrapper/native parity is not assumed.

Primary source: GitHub Docs, REST API endpoints for branches, `https://docs.github.com/en/rest/branches/branches?apiVersion=latest`.
