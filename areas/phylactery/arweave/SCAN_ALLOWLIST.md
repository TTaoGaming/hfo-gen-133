---
schema_id: hfo.gen133.phylactery.arweave.scan_allowlist.v0_1
doc_kind: SCAN_ALLOWLIST
claim_status: proposed
created_utc: 2026-08-02T00:00:00Z
---

# SCAN_ALLOWLIST — false-positive tolerations for the secret scan

Operator adds rows here only after **eyeballing** the specific hit and
confirming it is not a real secret. Each row justifies exactly one file's
false positive.

| path | pattern_matched | justified_by | added_utc | one_line_reason |
|---|---|---|---|---|
| _(none yet)_ | | | | |

## Rules

- One row per (path, pattern) tuple. Do not tolerate a pattern globally.
- If the same false positive appears in five or more files, tighten the
  regex in `secret_scan.py` instead — do not add five rows.
- The runner refuses to accept an allowlist row for `**/*.env`, `**/*.key`,
  `**/*.pem`, `**/*.jwk` — those are hard-coded HALT-and-never-uploads.

*Réttu hönd, eigi spyr. Standa.*
