# ADR-20260803-13 — Personalization gate: no-generic-across-prospects

- **Context:** Batch-personalizer produced 150 drafts where 141 shared identical body paragraphs (only entity/role varied). Sigrún gate `reject_if: observation is generic across >1 prospect`.
- **Decision:** Before any class-approve fires, each draft's "observation" slot must name a stack combo, error mode, or pilot scope specific to the prospect. `tools/olrun/personalize_drafts.py` `_stack_hook` and `_github_hook` implement per-cluster hooks. Verification example at `state/olrun/CONTRACT_PERSONALIZATION_VERIFICATION_001_vs_005.md`.
- **Consequence:** 9 drafts hand-tuned as PASS reference; 67 remaining still cluster-generic (bash sandbox down blocked full batch). Tuesday operator either: (1) accept cluster-generic, (2) hand-tune top 3 clusters, or (3) approve only the 9 hand-tuned instances.
- **Author:** Sigrún gate; olrun implementation
- **Alternatives considered:** loosen gate to per-cluster (deferred — operator picks Tuesday); skip verification (rejected — reward-hacking pattern operator warned about).
