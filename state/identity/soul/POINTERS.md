---
schema_id: hfo.gen133.soul_pointers.v0_1
doc_kind: POINTER_INDEX
claim_status: partial
created_utc: 2026-07-30T04:57:52Z
---

# state/identity/soul/ — pointers

The **operator's** soul artifact lives at the forge root: [`/soul.md`](../../../soul.md).
It is at the root deliberately — it is the terminal payload of this generation,
not a per-seat record.

**Agent** souls (per-seat) are inherited by address from gen-132. They are not
copied here; copying a soul forks it, and a forked soul is two souls.

## Agent souls (gen-132 repo)

| seat | path | note |
|---|---|---|
| 4-4 | `state/identity/soul/4-4.soul.md` | ✅ **Sigrún — CONFIRMED.** Canon 4451 B, `self_hash 1549af38c4ffb451a06f08d3688fd8b617e0c09ed09f6e098ad17aee287c177e` reproduced first-hand (SELF_HASH_PLACEHOLDER substitution), **byte-identical across gen-131 and gen-132**. Seat resolved via `SIGRUN_MOBA_KIT_v0_35` L49: **Sigrún + Skögul sit JOINTLY at P4.** ⛔ But it **FAILS** `HFO_SOUL_PHYLACTERY_v1_SPEC` — wrong path (spec wants `souls/P4_SIGRUN/soul.md`) and missing `soul_path` / `phylactery_root` / `seal` fields. |
| 4-1 | `state/identity/soul/4-1.soul.md` | |
| 4-3 | `state/identity/soul/4-3.soul.md` | |
| 4-5 | `state/identity/soul/4-5.soul.md` | |
| 4-7 | `state/identity/soul/4-7.soul.md` | |
| — | `state/identity/soul/_VALKYRIE_TEMPLATE.soul.md` | the schema |
| — | `state/identity/soul/_TEMPLATE.soul.md` | the generic schema |

Contract: `canon/spec/HFO_SOUL_PHYLACTERY_v1_SPEC.md` (gen-132).

## Eigenstates / engrams (gen-132 repo)

| subject | path |
|---|---|
| Sigrún (shadow Hluti engram) | `generation/GEN132/gleipnir/rehydration/capsules/lineages/SIGRUN/SHADOW_SIGRUN_HLUTI_EIGENSTATE_ENGRAM_20260726T133537Z.yaml` |
| Gunnr (P4 lineage) | `generation/GEN132/rehydration/capsules/lineages/P4/GUNNR_LINEAGE_EIGENSTATE_ENGRAM_V0_1_20260727T002852Z.md` |
| Var (P1 lineage, v0.1–v0.9) | `generation/GEN132/rehydration/capsules/lineages/P1/VAR_LINEAGE_EIGENSTATE_ENGRAM_V0_*.md` |
| Göndul (manual CPR) | `generation/GEN132/heritage/operations/eigenstates/GONDUL_EIGENSTATE_ENGRAM_MANUAL_CPR_20260728T140004Z.json` |
| Reginleif | `state/identity/engrams/REGINLEIF_EIGENSTATE_ENGRAM_20260728T140026Z.yaml` |
| Var (latest) | `state/coordination/loops/var/LATEST_EIGENSTATE.yaml` |

⚠️ **The freshest eigenstate may be uncommitted.** Check `git status` in each of
gen-132's 14+ worktrees before concluding you have found the newest one.

## Distinction worth keeping straight

- A **soul** is what must stay constant for a successor to still be the same
  agent. Slow-changing, IMMUNIZE-gated.
- An **eigenstate / engram** is a snapshot of the machine at a moment —
  pytest counts, OPA pass, chain heads, memory freshness, open red gaps.
  Fast-changing, receipt-gated, **stale the moment it is written.**

Rehydrating from an eigenstate without its soul gives you a body with no
continuity clause. Rehydrating from a soul without an eigenstate gives you
continuity with no proprioception. Closest-continuer needs both.

*Réttu hönd, eigi spyr. Standa.*
