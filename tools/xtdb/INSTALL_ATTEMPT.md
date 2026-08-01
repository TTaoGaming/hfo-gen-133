# XTDB install attempt — gen-133 — 2026-07-31

```yaml
doc: INSTALL_ATTEMPT.md
schema_id: hfo.gen133.xtdb_install_attempt.v0_1
outcome: FALLBACK — Docker daemon did not come up inside the timebox
sealed: false
```

## What was tried

1. `docker ps` → failed immediately: `npipe:////./pipe/dockerDesktopLinuxEngine`
   not found — Docker Desktop was not running.
2. `docker --version` → 29.5.3 (the CLI/engine is installed).
3. Launched `Docker Desktop.exe` via `Start-Process` (background).
4. Polled `tasklist` ~3 min later — `Docker Desktop.exe`, `com.docker.backend.exe`
   processes present (WSL2 VM boot in progress).
5. `docker ps` retried twice more (once hit the 120s tool timeout, once
   explicit `timeout 8 docker ps` → exit 124) over roughly 15 minutes total —
   daemon socket never came up inside that window.

## Decision

Did not keep waiting past ~15 min of the 45-min budget on an unpredictable
Docker Desktop cold-boot. Per CLAUDE.md's own guidance ("If XTDB install fails
at Move 1, land honest partial + recommend fallback... don't force install"),
switched to the SQLite bitemporal fallback specified in the task. See
`tools/central_memory/`.

## If Docker comes up later

`docker pull xtdb/xtdb:latest` was never attempted (daemon never accepted
connections) — no partial image, no dangling container. Nothing to clean up.
A future pass can retry `docker pull xtdb/xtdb:latest` + start on port 6543
once Docker Desktop's daemon is confirmed live (`docker ps` returns instead of
hanging), then port `tools/central_memory/schema/hfo_facts.md`'s entity
tables into real XTDB Datalog documents — the schema doc was deliberately
written entity/attribute-shaped so that port is mechanical, not a redesign.

## Honest flaw

Never verified XTDB v2's actual HTTP API shape / default port for this
environment (no network fetch was performed to confirm — the "6543" in the
task text was taken on faith, not verified against docs). Would need to
confirm before a real install, not just cargo-cult the port number.
