---
schema_id: hfo.gen133.strife_splendor.readme.v0_1
doc_kind: DIRECTORY_GUIDE
created_utc: 2026-08-01T02:10:00Z
author: claude-sonnet-5 - Claude Code - gen-133 heritage inventory carrier
---

# resources/heritage/strife_splendor/ — read this before either subfolder

Governed by `contracts/strife_splendor_rehydration.v0_1.md`. Two very
different things live in this directory — **do not conflate them**:

## `SEED_20260801_sigrun_session.md` — the ADMITTED corpus

This is the canonical source of truth. Every row in it (`S-001`...`S-007`,
`P-001`, `P-002`) already passed the admissibility bar defined in the
contract §2: strife needs a **named mechanism** + cost + cure; splendor needs
a **verified external effect a stranger could see or touch** + consumer
acceptance. A row without these is explicitly rejected by the contract —
"a strife row without a named mechanism is a counter increment, not a
record."

**This file is what Q5 pre-dispatch anchoring reads.** Treat it as append-only
and bitemporal (never delete a row — supersede with a new one and a later
`transaction_time_utc`, per the contract §3).

## `raw_source_material/` — UNMINED candidates, added 2026-08-01

This subfolder holds **20 verbatim copies** of source documents found by a
bounded grep/find pass across gen-130/gen-131 for files named or tagged
`failure`/`success`/`postmortem`/`retro`/`strife`/`splendor`
(`strife_candidates/` = 12 files, `splendor_candidates/` = 8 files).

**None of these are admitted rows.** They are raw material for the mining
step the contract calls for in §6.3 ("mine the 12 heritage-inventory rows
that mention either term"). A future pass (any substrate) should read these,
extract the mechanism/cost/cure (or what_worked/mechanism/evidence) for each
genuine incident they contain, and add properly-formed rows to
`SEED_20260801_sigrun_session.md` (or a new dated supersession file) — not
copy these files' prose wholesale into the corpus.

Full catalog with sha256/preview/label for these plus 130 additional
lower-confidence hits (98 `ambiguous`, 28 `doctrine_mention_only`) is at
`state/ssot/strife_splendor_inventory_20260801.jsonl` (150 rows total).

## What NOT to do with either folder

- Do not treat a file in `raw_source_material/` as query-able corpus for Q5
  anchoring — it has not passed the admissibility bar.
- Do not delete anything here; supersede per the bitemporal rule.
- Do not bulk-copy the remaining ~680 files from `heritage_inventory_20260801.jsonl`
  into this directory — the contract's whole point is selectivity (mechanism
  over volume), not corpus size.
