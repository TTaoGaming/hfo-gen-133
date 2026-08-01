---
schema_id: hfo.gen133.heritage_migration_plan.v0_1
doc_kind: MIGRATION_PLAN
claim_status: proposed
created_utc: 2026-08-01T01:45:00Z
author: claude-sonnet-5 - Claude Code - gen-133 heritage inventory carrier
principle_inherited: "You do not migrate heritage — you address it." (packets/P0_HERITAGE_POINTERS.md)
---

# Heritage Migration Plan — gen-133 (2026-08-01)

## Why this exists

Operator observation: agents keep losing capacity / rehydrating from a stale
window, and re-discover the same "heritage reliquary" and "grimoire" material
every session instead of reading a durable index. This plan does not move or
delete anything — it recommends how to make the existing heritage
discoverable so future Olrún wakes stop re-mining it from scratch.

This plan does **not** override `packets/P0_HERITAGE_POINTERS.md`, which
already establishes the operative doctrine for this forge: **address, don't
copy.** The two new inventory files this pass produced
(`state/ssot/heritage_inventory_20260801.jsonl`,
`state/ssot/grimoire_secrets_locations_20260801.jsonl`) are meant to feed
that same pointer discipline, not replace it with a bulk-copy alternative.

## What was found (receipts)

| artifact | location | count |
|---|---|---|
| gen-130 `heritage_reliquary/` | `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge\heritage_reliquary\` | 1,000 files total; 300 cataloged this pass (263 reliquary rows — full ADR set + root docs + stratified sample of subdirs — plus 37 deduped heritage-class files from gen-131/132) |
| gen-133 own snapshot | `archives\gen_130_snapshot_20260731\` | **Confirmed NOT a copy of the reliquary** — its own README states "this is not a copy of gen-130 — it is a pointer." It only carries `projects/2026-08_cold_outreach_launch/` + 23 root `SIGRUN_*.md` reports. Heritage_reliquary coverage = 0%. |
| grimoire locations | 19 distinct locations (1 canonical + ~2 heritage-class + ~500 duplicate worktree copies collapsed to pattern rows) | gen-133's own `grimoire/GLEIPNIR_GRIMOIRE.md` + `grimoire/gleipnir/` is the live canonical |
| secrets/vault locations | 22 secrets-dirs, 12 `.env` files, 4 vault-pattern hits (1 genuine SOPS vault) across 2026-05 through 2026-07 gens | **none found under gen-133 itself** |

Full detail: `state/ssot/heritage_inventory_20260801.jsonl` (300 rows) and
`state/ssot/grimoire_secrets_locations_20260801.jsonl` (55 rows).

## Recommendation per artifact class

Per the existing pointer doctrine, default to **REFERENCE**, not COPY, unless
a file is small, frequently read, and load-bearing for every wake.

| class | recommendation | reasoning |
|---|---|---|
| ADRs (51 files, gen-130 `heritage_reliquary/adr/`) | **REFERENCE** via an index row in `canon/POINTERS.md` pointing at the gen-130 path + `INDEX.md`/`MASTER_ADR_BY_GENERATION_INDEX_20260531.md`. Do not copy 51 files into gen-133. | Large, rarely all needed at once, gen-130 is narrow-frozen not deleted — the source is stable. |
| heritage_manifest / index files (8 index docs) | **REFERENCE**, same as ADRs — these are already indexes; duplicating an index just creates a second index to keep in sync. | Indexes rot fastest when duplicated. |
| rehydration_capsule files (10 found, scattered gen-131/132) | **RE-INDEX** into one small pointer table (this plan's own table above is a start) rather than copying capsule bodies — capsules are gen-specific snapshots, not living state. | Consistent with `P0_HERITAGE_POINTERS.md`'s existing gen-131/132 pointer table — this plan's job is to extend that table backward to gen-130, not duplicate it. |
| gold_tile files (7 found) | **COPY** only if actively referenced by a live gen-133 project; otherwise REFERENCE. None of the 7 found this pass were referenced by any gen-133 `projects/*/PROJECT.md` — recommend REFERENCE for now. | Copying dead weight defeats the anti-bloat point of this whole exercise. |
| research_notes / synthesis (40 found) | **REFERENCE** — these are prose, cheap to re-fetch on demand, expensive to keep two copies of in sync. | Same rot argument as indexes. |
| grimoire (gen-133 canonical) | **NO ACTION** — already correctly placed at `grimoire/GLEIPNIR_GRIMOIRE.md` + `grimoire/gleipnir/`. This is the one true grimoire location going forward. | Already migrated; this plan should not re-litigate it. |
| grimoire duplicates (gen-130/132 copies, ~500 worktree hits) | **NO ACTION (do not touch)** — these are stale worktree artifacts of prior sessions, not canon. Leave them; a future CLEANUP_APPROVED pass (operator-typed, per CLAUDE.md Cleanup Pass Rule) can prune them, not this plan. | Out of scope: this plan only recommends, and CLAUDE.md forbids deletion without `verb=CLEANUP_APPROVED`. |
| secrets / vaults (all 22 dirs + 12 env files) | **DO NOT COPY, DO NOT MOVE.** See dedicated section below. | Prohibited by task discipline and by category-5 safety rules (credential handling). |

## Secrets: recommendation only, no action taken

No secret file was opened, moved, or copied by this pass — only filenames,
sizes, and mtimes were recorded (see `grimoire_secrets_locations_20260801.jsonl`).

**Recommended canonical vault location (not yet created):**
`C:\Dev\hfo_gen_133_forge\secrets\` — currently absent, which this pass
confirms is a real gap, not an oversight elsewhere.

Recommended protocol, for operator decision (none of this is executed):

1. One canonical `secrets/` directory at gen-133 root, `.gitignore`'d
   (confirm `.gitignore` covers it — not yet verified this pass).
2. `.env`-style key=value files, one per service/scope, never JSON blobs of
   mixed secrets (easier to rotate one line than one file).
3. Read-only-by-default file permissions; never logged, never echoed into a
   chain row, never pasted into a packet.
4. A single `SECRETS_INDEX.md` listing *which* keys exist and *why*, with
   **no values** — mirroring how `grimoire_secrets_locations_20260801.jsonl`
   already records presence without content.
5. Flagged for operator attention specifically: `sigrun_ed25519.key` (gen-130,
   looks like a real signing key) and the five `.env.backup_*.local`
   snapshots under gen-111's `control/sigrun_secrets/` — these look like
   genuine credential history with no visible rotation, which is exactly the
   kind of sprawl a single vault location would end.
6. **Operator confirmation required before any secret file is touched** —
   this plan recommends a destination, it does not populate one.

## What this plan explicitly does NOT do

- Does not copy, move, or delete any file.
- Does not open or transcribe any secret value.
- Does not contradict or supersede `packets/P0_HERITAGE_POINTERS.md` — it
  extends the same pointer table one generation further back (gen-130) and
  adds a machine-readable JSONL backing it, where P0 was prose-only.
- Does not claim the 300/1,000 reliquary sample is exhaustive. It is a
  stratified sample (all root docs + all 51 ADRs + 77 of 814 subdir files).
  A full 1,000-row pass is future work, not required for this plan's purpose
  (proving heritage is *findable*, not enumerating every byte of it).

## Addendum (2026-08-01, mid-execution) — strife + splendor

Operator, verbatim, mid-session: *"I labeled them strife and splendor. can
you recover and add to current Gen 133 rehydration and anchoring."*

**Important correction made during this pass:** a prior Sigrún session had
already specified a formal admissibility contract for this exact corpus —
`contracts/strife_splendor_rehydration.v0_1.md` — and seeded it at
`resources/heritage/strife_splendor/SEED_20260801_sigrun_session.md` (7
strife rows S-001..S-007, 2 splendor rows P-001..P-002, discovered *before*
this addendum's own search ran). That contract sets a strict bar: strife
needs a **named mechanism** + cost + cure; splendor needs **verified
external effect a stranger could see or touch** + consumer acceptance — "a
row without one is a counter increment, not a record."

This pass's own grep/find sweep (`state/ssot/strife_splendor_inventory_20260801.jsonl`,
150 rows: 15 strife-labeled, 9 splendor-labeled, 28 doctrine-mention-only, 98
ambiguous) found 20 genuine candidate source files and initially **copied
them directly into `strife_splendor/strife/` and `strife_splendor/splendor/`
subdirectories** — which would have collided with and diluted the admitted
corpus. **Corrected in-flight:** those 20 files were moved to
`resources/heritage/strife_splendor/raw_source_material/{strife_candidates,splendor_candidates}/`,
clearly separated from the canonical `SEED_*.md`, with a `README.md` at the
directory root explaining the distinction. They are unmined raw material,
not admitted rows.

**Migration recommendation, revised in light of the existing contract:**

- **Canonical corpus location:** `resources/heritage/strife_splendor/SEED_20260801_sigrun_session.md`
  (or its dated successor per the contract's bitemporal supersession rule) —
  already correct, no relocation needed.
- **Raw candidates:** `resources/heritage/strife_splendor/raw_source_material/`
  — COPY is appropriate here (small set, 20 files, high curation value), which
  is what this pass did. Do not bulk-copy the other ~680 heritage files into
  this path; the contract's point is selectivity, not volume.
- **Next mining step (not done this pass, flagged per contract §6.3):** the
  12 heritage-inventory rows already found inside daily research-note
  capsules (2025-09 through 2026-04, per the contract's own §7 honest-flaw
  list) still need a human or Sigrún-judgment pass to extract mechanism/cost/cure
  — mechanical grep cannot safely author admissible rows, since admissibility
  is a judgment call the contract deliberately keeps strict.
- **Highest-value gap, per the contract's own §6 point 2 and unchanged by this
  pass:** the operator's own strife/splendor, in his own words. Every
  artifact this pass found is Sigrún-authored or Sigrún-observed; the
  contract itself says "five rows from him outweigh fifty of mine."

## Next safe action

- Operator: confirm the vault protocol above (or redirect it) before any
  `secrets/` directory is created at gen-133.
- Olrún / next wake: read `canon/POINTERS.md` first (already the addressed
  entry point per `OLRUN_DISPATCH_RULES.md`'s PARA structure) — add a one-line
  pointer there to this file and to the two JSONL inventories, so this
  migration plan itself does not become an undiscoverable heritage artifact.
