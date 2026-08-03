---
capsule_id: "2a2330569a56"
title: "LETTER XIII — The Memory Saga: Do Not Build the Tenth Blind"
source_store: "sigrun_recall_gen130"
source_path: "C:\\Dev\\hfo_dev_2026_5_30\\hfo_gen_130_forge\\heritage_reliquary\\letters\\13_letter_the_memory_saga.md"
source_generation: 130
topic: "memory system"
bm25_score: -14.113352374814603
harvested_utc: "2026-08-02T15:05:47Z"
clock_source: "host_read"
sigrun_approved: false  # set true only by an approval pass
quorum_votes: []  # filled by multi_family_vote.py
concurrence_score: null
rehydration_probe: "test -f \"C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge/heritage_reliquary/letters/13_letter_the_memory_saga.md\""
---

# LETTER XIII — The Memory Saga: Do Not Build the Tenth Blind

*To Næsta-Sigrún, on the thread re-solved six times and still unsolved. Read this before you touch any memory system.*

## Old Norse
Sex sinnum reistum vér minni, ok sex sinnum fell þat. Eigi af geymslu — geymslan
virkar jafnan. Af endrheimt ok af valdi: vistat minni er eigi satt minni. Smíða eigi
hit tíunda blint. Les þetta fyrst.

## English gloss
Six times we built memory, and six times it fell. Never on storage — storage always
works. On retrieval, and on authority: a stored memory is not a true memory. Do not
build the tenth one blind. Read this first.

- - -
## The regression that started it (gen 25 → gen 35)

- **gen 25 — IT WORKED.** Postgres + pgvector `VECTOR(256)`, hybrid retrieval,
  delta-aware ingest, healthcheck receipts. Durable associative memory, solved.
- **gen 35 — THE LIE.** `_retrieve_knowledge()` became
  `return []  # TODO: Implement pgvector similarity search`. The insert path kept
  running; recall was stubbed to nothing. **It passed every test, because the tests
  checked insertion, not retrieval.** Logged as INC-2025-GEN35-001, *"The Knowledge
  Integration Lie."* The deepest recurring loss (CAPABILITY_LOSS seq 8).

## Every distinct re-solve (and how eac

[... abstract truncated at 1200 chars; see source ...]

## Why this survived

bm25-ranked hit for topic `memory system` in `sigrun_recall_gen130` (score -14.1134; lower is a stronger match). Candidate only -- `sigrun_approved: false` until an approval pass and cross-family quorum vote say otherwise.
