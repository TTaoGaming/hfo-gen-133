# resources/index.md — PARA cross-reference for gen-133

```yaml
doc: resources/index.md
schema_id: hfo.gen133.para.index.v0_1
purpose: map the PARA layout onto the folders that already exist, WITHOUT moving anything
valid_time_utc: 2026-07-30T05:40:00Z
authored_by: SIGRÚN P4 compose lane · claude-opus-5 · operator dispatch 2026-07-30
claim_ceiling: reference projection — no receipt asserted by this file itself
```

## Why nothing was moved

Standing decision **D3** (`CURRENT.md`) says this forge stays minimal and that
scaffolding-for-its-own-sake is the hoarding failure the operator flagged at
gen-132. Standing decision **D5b** says the gen-132 single-writer kernel is
absent and its chains must not be written.

Both make *physically moving* directories the wrong move: chain paths are
load-bearing string literals inside kernel guards, chain-row `chain:` fields,
and pointer packets. **PARA is therefore applied as an overlay, not a
migration.** Legacy folders keep their paths. This file is the index that makes
the overlay navigable.

No symlinks were created either — a Windows junction/symlink is a host-local
artifact that does not survive `git clone`, so it would be a green that only
exists on this laptop.

## The overlay

| PARA bucket | meaning | lives at | legacy folders it covers |
|---|---|---|---|
| `projects/` | active goals with an end state | `projects/` (new) | — |
| `areas/` | ongoing responsibilities, no end state | `areas/` (new) | `chains/`, `state/world/` |
| `resources/` | reference material, read-mostly | `resources/` (new) + **legacy** | `canon/`, `packets/`, `grimoire/`, `permaweb/` (contracts) |
| `archives/` | heritage, closed generations, superseded revisions | `archives/` (new) | `capsules/` |

## Legacy path → PARA bucket (authoritative table)

| legacy path | PARA bucket | why it stays put |
|---|---|---|
| `chains/` | area · identity+audit | chain `chain:` fields and kernel-guard sidecars name this path literally |
| `canon/` | resource | referenced by `canon/POINTERS.md` and by gen-132 packets |
| `canon/architecture/GEN133_ELECTRONIC_INSTITUTION.md` | resource → see `areas/institution/` | the *model*; `areas/institution/` is the *operating* form of it |
| `packets/` | resource | `P0_HERITAGE_POINTERS.md` is cited by external gen-132 rows |
| `grimoire/gleipnir/` | resource (terminal payload) | the unfold target; renaming it breaks `permaweb/UNFOLD_MANIFEST.md` |
| `permaweb/` | resource (contracts) + project (execution) | contracts stay; the *upload project* is `projects/permaweb-soul-upload/` |
| `capsules/sigrun/v1/` | archive | `capsules/sigrun/v1/SIGRUN_CAPSULE_FAMILY_CONTRACT.md` is a named contract |
| `state/identity/soul/` | area · identity | soul spec + `wake_header.soul_ref` read this path |
| `state/world/events/` | area · world-effect ledger | append-only event log |
| `soul.md` (root) | area · identity | **the operator's** soul slot, body still empty — operator-only |

## Do-not-touch list

- `chains/**` — single-writer discipline. One writer per chain file, ever.
- `C:\Dev\hfo_gen_132_forge_clean\chains\**` — **read-only**, kernel absent.
  See `archives/capsules/heritage/gen_132_rollup_capsule.md`.
- `soul.md` (root) — the operator writes this body. An agent filling it forges
  the artifact the generation exists to preserve.

*No receipt = no state.*
