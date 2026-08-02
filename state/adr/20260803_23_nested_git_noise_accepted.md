# ADR-20260803-23 — Nested `.git/` under staged_sends flagged as noise, not scrubbed

- **Context:** ~1,100 files + 99 MB of nested `.git/` internals under `outputs/staged_sends/b2b_saas/*/` (hook samples, pack promisor files) came in when Codex loops cloned reference repos. These are not intentional artifacts.
- **Decision:** This consolidation flags them as `[DROPPED_SILENTLY]`-adjacent noise in SESSION_INDEX §5 but does not delete them (mandate: "do not touch old files that weren't part of this session" — these WERE from this session, but scrubbing them alters pipeline output). A follow-up ADR will decide whether to `.gitignore` the pattern or scrub post-fact.
- **Consequence:** Commit bulk is larger than necessary. Future consolidation should add `outputs/staged_sends/**/.git/` to `.gitignore` before the b2b_saas Codex loop runs again.
- **Author:** olrun
- **Alternatives considered:** scrub before commit (rejected — mutates a pipeline output without operator sign-off); add gitignore pattern (deferred — needs its own ADR to modify .gitignore).
