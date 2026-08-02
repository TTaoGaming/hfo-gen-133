# ADR-20260803-16 — Distribution deferred to Tuesday

- **Context:** 150 personalized distribution drafts staged this session at `outputs/staged_sends/`. Contracts expire 2026-08-09. Class-preauth gate wired. Personalization gate has 9 PASS + 67 cluster-generic.
- **Decision:** Do NOT fire distribution this session. Operator reviews `state/outreach/READY_TO_FIRE_TUESDAY.md` on Tuesday, signs class envelope for the subset they accept, then Codex-loop-2 fires.
- **Consequence:** No cold outreach lands until operator explicit go on Tuesday. Every draft remains `STAGED_FOR_OPERATOR_APPROVAL_NEVER_SENT`.
- **Author:** operator (default: no unattended send this session); olrun
- **Alternatives considered:** fire 9 hand-tuned drafts under sub-envelope (rejected — operator's decision, not olrun's); fire all 150 (rejected — cluster-generic risk + Sigrún gate).
