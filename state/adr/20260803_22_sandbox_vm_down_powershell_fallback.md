# ADR-20260803-22 — Sandbox VM down; PowerShell substitution used for consolidation

- **Context:** Consolidation Executor received "Sandbox VM may be down — write code to run from operator's normal Windows PowerShell if needed" in the mandate. VM was indeed down at consolidation time.
- **Decision:** All inventory + hashing + git ops performed via `mcp__Desktop_Commander__start_process powershell.exe` with absolute Windows paths. No POSIX assumptions.
- **Consequence:** Every subsequent script that this consolidation references (personalize_drafts.py, factory scripts) should be verified to work under both bash and PowerShell before being called a "dispatchable loop".
- **Author:** olrun
- **Alternatives considered:** wait for VM (rejected — session mandate cap of 2-4 hours); use only file tools without shell (rejected — cannot hash / cannot git-commit without a shell).
