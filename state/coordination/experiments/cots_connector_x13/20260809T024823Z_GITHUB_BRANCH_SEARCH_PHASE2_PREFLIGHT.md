---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_BRANCH_SEARCH_READONLY_025
event_type: PHASE2_PREFLIGHT
expected_current_version: 197
candidate: GitHub_search_branches_readonly
campaign_wake: 2_of_4
wip: 1
valid_time_utc: 2026-08-09T02:48:23Z
recorded_time_utc: 2026-08-09T02:48:23Z
request_sha256: fcf48deba34027fe7f23bbf28db29d34f3f4847e3a5317be606480f49039ce6f
mutation_allowed: false
---

# X13 GitHub Branch Search Phase 2 Preflight

One exact replay of the durable Phase-1 request is authorized after this preflight is read back and the request digest is verified.

Canonical request preimage:

```json
{"cursor":null,"owner":"TTaoGaming","page_size":5,"query":"agent/gen133-bootstrap-20260730","repo_name":"hfo-gen-133"}
```

Comparison boundary: result count, exact-match presence, and cursor presence only. No completeness inference, pagination use, branch mutation, merge, publication, secret access, or task mutation.
