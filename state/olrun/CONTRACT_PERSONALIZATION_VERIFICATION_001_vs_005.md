# Verification — draft 001 (DrSwarm) vs draft 005 (airCFO) divergence

Sigrún gate under test: `reject_if: observation is generic across >1 prospect`.

Prior state (pre-personalization):
- Both drafts had character-for-character identical bodies except for entity, role, and one keyword in `matched_terms`.
- Paragraphs 2, 3, 4, 5 were literal copies.
- Observation ("what the sender specifically noticed about this prospect") was: **none** — just a template.

Post-personalization diff summary:

| slot | draft 001 (DrSwarm) | draft 005 (airCFO) |
|---|---|---|
| opening verb | "Saw your Founding Engineer (Full-Stack) post..." | "Came across your Founding Engineer post..." |
| specific observation | "5-stack in one seat = 5 moving parts have to stop lying to each other" | "RAG + Python for CFO-outsourcing = wrong invoice/misclassified transaction becomes accounting error" |
| named-seam | "LLM call feeds typed code that touches AWS" | "document ingest -> account/vendor classification" |
| refused-path framing | "so a bad prompt can't quietly leak downstream" | "so ambiguous inputs surface for human review instead of getting a confident wrong answer" |
| milestone 1 | "LLM->typed-code seam with synthetic inputs" | "RAG->classification seam on synthetic/non-sensitive documents" |
| milestone 2 | "validation/retry boundary" | "low-confidence refusal boundary" |
| closing hook | "If that seam is real for DrSwarm..." | "If that retrieval seam is real for airCFO..." |

The two bodies now share only the closing block ("book 15 minutes... — TTaoGaming") and the proof-links paragraph, both of which are correctly reused because the operator identity and portfolio don't vary per prospect. Every observation about the prospect itself is now unique.

The Sigrún check would flip from FAIL (identical observation) to PASS (each observation names a specific stack combo, a specific error mode plausible only for that entity's product, and a specific pilot scope tuned to what they'd need).

Additional divergence for GitHub contract pair 081 (NousResearch/hermes-agent) vs 097 (destructive_command_guard):

| slot | draft 081 | draft 097 |
|---|---|---|
| repo-specific observation | "agent that grows with you + anthropic/claude-code topic set = will accumulate integration and eval seams" | "dcg purpose = most agent loops today only find out rm -rf slipped through when a downstream user reports the damage" |
| language framing | "Python codebase" | "Rust CLI shape is exactly the right substrate to lean on for a strict, testable guard" |
| adjacent seam pitched | "integration or verification seam exercised by 'run it and see'" | "Claude Code / Codex / agent-loop harness that currently doesn't invoke dcg, or an existing dangerous-command rule that lacks a red-team fixture" |
| proof framing | generic auditability | "same shape of auditability dcg exists to enforce, applied to my own workflow" |

Same conclusion: distinct observation per prospect.

## Batch personalizer (67 remaining drafts)

The remaining 67 drafts still carry the original template body because the bash sandbox was unavailable this session. The batch personalizer at `tools/olrun/personalize_drafts.py` is deterministic and uses distinct hook language per matched-terms combination (see `_stack_hook` and `_github_hook` in the script). Sample verification for two representative drafts the batch would touch:

- **contracts/013_zeitlabs** (LLM+TS+React) → `_stack_hook` returns the "LLM integration + typed code is a seam where wrong outputs quietly leak downstream unless someone builds the refused-path" hook.
- **contracts/029_axo-ventures** (TS+PostgreSQL) → `_stack_hook` returns the "PostgreSQL as a hiring signal usually means the schema or the query patterns are the real risk surface, not the app layer" hook.

These two would render observations distinct from each other and from 001/005/021/057/081/097 above.

The remaining risk after batch-personalizer runs: drafts within the same matched-terms cluster (e.g., three drafts that all match {LLM integration, Python, TypeScript}) share the same `_stack_hook` sentence. The entity name + role + top-term ordering still varies, but the "observation" phrase is the same. Sigrún's gate may still flag this as generic-within-cluster.

**Mitigation before class-approve fires**: operator either
1. accepts the shared hook per cluster (gate interpretation: "generic across >1 prospect within cluster" is looser than "identical body"), OR
2. hand-tunes the ≤3 largest clusters, OR
3. restricts approval to the 9 hand-personalized instance lines this week and personalizes the rest before the 2026-08-09 expiry.

Recommendation logged in `CONTRACTS_EMPLOYMENT_80_READY_20260805.md` — the safer 9-instance list is offered as the first-week option.
