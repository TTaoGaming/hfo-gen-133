# ADR-20260803-07 — promptbin unit merged into prompt-versioning-lite

- **Context:** Two overlapping candidate units — "promptbin" (paste-and-share for prompts) and "prompt-versioning-lite" (git-like history for prompts). Both target the same AI-dev ICP with 80%+ feature overlap.
- **Decision:** Merge into single unit `factory/units/prompt-versioning-lite/` that includes paste/share as a subset of the versioning UI.
- **Consequence:** Saves one unit-slot in the 1-per-week cap. Marketing positioning is "prompt versioning that also does share links", not the reverse.
- **Author:** olrun
- **Alternatives considered:** ship both as separate units (rejected — burns two throttle slots for near-duplicate value); ship promptbin as a Setapp-style bundle addon (deferred).
