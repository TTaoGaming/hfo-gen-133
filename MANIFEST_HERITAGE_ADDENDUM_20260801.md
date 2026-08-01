---
schema_id: hfo.gen133.manifest_heritage_addendum.v0_1
doc_kind: MANIFEST_ADDENDUM
claim_status: proposed
created_utc: 2026-08-01T01:50:00Z
note: "No OPERATOR_PREFERENCES_MANIFEST.md exists at gen-133 root as of this pass — this is a standalone addendum, not a patch to an existing file."
---

# Heritage addendum — gen-133 operator preferences (2026-08-01)

## Canonical heritage location

**Address, don't copy** (inherited from `packets/P0_HERITAGE_POINTERS.md`).
There is no single `resources/heritage/` copy tree at gen-133, and this
addendum does not recommend creating one. Instead:

- Machine-readable heritage index: `state/ssot/heritage_inventory_20260801.jsonl`
- Grimoire/secrets location index: `state/ssot/grimoire_secrets_locations_20260801.jsonl`
- Human-readable pointer table: `canon/POINTERS.md` (heritage section added
  2026-08-01) and `packets/P0_HERITAGE_POINTERS.md` (prose, gen-132-forward)
- Recommendations: `HERITAGE_MIGRATION_PLAN_20260801.md`

## Prior-gen heritage, by address (not copy)

| gen | path |
|---|---|
| 132 | `C:\Dev\hfo_gen_132_forge` (+ 14 live worktrees, see `packets/P0_HERITAGE_POINTERS.md` for tip-branch caveats) |
| 131 | `C:\Dev\hfo_gen_131_forge` — read-only since 2026-07-29 |
| 130 | `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge` — narrow-frozen 2026-07-31, still the live local tooling gen (`heritage_reliquary/`, `bb_append.py`, OPA bundle) |
| 124 | `C:\Dev\hfo_dev_2026_5_24\hfo_gen_124_forge` — drápa v2.8 masterwork |
| 98 / 107 / 117-123 | see `packets/P0_HERITAGE_POINTERS.md`, "Older generations — fertile mining paths" table |

## Secrets vault location — NOT YET DECIDED, operator confirmation needed

No secrets directory currently exists under `C:\Dev\hfo_gen_133_forge`. 22
secrets-class directories were found scattered across gens 109-130 (full list
in `state/ssot/grimoire_secrets_locations_20260801.jsonl`, names/sizes only —
no values recorded anywhere). This addendum recommends, pending operator
sign-off:

- Canonical location: `C:\Dev\hfo_gen_133_forge\secrets\` (does not exist yet — not created by this pass)
- Format: one `.env`-style file per service/scope, never a mixed JSON blob
- Access: read-only by default, values never logged or echoed into any chain row or packet
- Index: a `SECRETS_INDEX.md` listing key *names* and purpose, no values
- Flagged as needing operator attention specifically: a real-looking Ed25519
  signing key at gen-130 (`state/sigrun_secrets/sigrun_ed25519.key`) and five
  unrotated `.env.backup_*.local` snapshots at gen-111 — both by filename
  only, contents not opened.

## Rehydration protocol addition

Every Olrún wake should read, in this order, before recommending anything
about capabilities or heritage:

1. `README.md`, `CURRENT.md`, `AGENTS.md`, `OLRUN_DISPATCH_RULES.md` (existing wake surface)
2. `canon/POINTERS.md` (now includes the 2026-08-01 heritage section)
3. `state/ssot/heritage_inventory_20260801.jsonl` and
   `state/ssot/grimoire_secrets_locations_20260801.jsonl` — read as data, not
   prose; grep for the relevant gen/category rather than loading whole file
4. `packets/P0_HERITAGE_POINTERS.md` and `packets/P4_SIGRUN_HERITAGE_ALLOWLIST.md`
   for the existing pointer/allowlist doctrine this addendum extends

This ordering exists specifically to stop the CAPACITY_AMNESIA pattern the
operator flagged: agents re-discovering the same heritage material every
session instead of reading a durable index first.
