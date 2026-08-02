# ADR-20260803-21 — Clock-source caveat: host mtime not UTC-canonical this session

- **Context:** Sandbox Linux VM was down during consolidation. All inventory `LastWriteTime` values are Windows host mtimes showing 2026-08-02, but session labels itself 2026-08-03 in UTC canon.
- **Decision:** Trust filename date-stamps (embedded `_YYYYMMDD` suffixes) and chain-row `now_utc` fields over file mtimes for cross-session dating. `clock_source: host_read` when mtime is used; `clock_source: chain_utc` when chain rows are the reference.
- **Consequence:** Future rehydration should not use mtime windows to reconstruct "what landed on day N". Use chain rows or filename stamps.
- **Author:** olrun (per operating-discipline `clock_source discipline` rule)
- **Alternatives considered:** re-touch every file to normalize mtime (rejected — destructive to actual creation history); ignore the drift (rejected — future audits will be misled).
