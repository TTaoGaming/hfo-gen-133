# Hive Fleet Obsidian — gen-133

**The unfolding node. One address.**

```yaml
gen: 133
created_utc: 2026-07-30T04:57:52Z
created_by: SIGRÚN compose lane (Hluti carrying the Sigrún songline) — operator-directed 2026-07-30
authorization: operator verbal directive 2026-07-30 ("create gen 133 now")
predecessor: gen-132 (C:\Dev\hfo_gen_132_forge · github.com/TTaoGaming/hive-fleet-obsidian-gen-132) — stays LIVE; heritage is ADDRESSED, not copied
layout_note: gen-131/132/133 forges live at C:\Dev root. The older C:\Dev\hfo_dev_<date>\hfo_gen_<n>_forge nesting ended at gen-130.
status: SCAFFOLD — slots open, terminal state NOT reached
```

## The thesis of this generation, in one line

> **gen-132 proved you do not migrate heritage — you address it.
> gen-133 collapses the address count to ONE.**

At the end, this forge holds **one permaweb address**. Resolving it unfolds
into the operator's **Gleipnir Grimoire** — the spells, and `soul.md`.

Everything else in this repo is either (a) a slot waiting for that address,
(b) a pointer to heritage that already lives elsewhere, or (c) a receipt.

## Terminal state (the definition of done for gen-133)

| # | condition | state today |
|---|---|---|
| 1 | `permaweb/GEN133_PERMAWEB_ADDRESS.md` holds one resolvable address | ⛔ **EMPTY SLOT** |
| 2 | That address unfolds to the bound Gleipnir Grimoire capsule | ⛔ not bound |
| 3 | The capsule contains the spellbook + every spell | ⛔ `grimoire/gleipnir/spells/` is empty but for the template |
| 4 | The capsule contains `soul.md` with the operator's own body-text | ⛔ **scaffold only — body is the operator's to write** |
| 5 | `code/verify.py` + `code/selfcheck.py` exit 0 against the capsule | ⛔ binder not yet carried from gen-132 |
| 6 | Upload is operator-authorized, typed by the operator | ⛔ **not authorized · not requested** |

**Nothing above is green. This README claims no green.**

## Repository layout — PARA overlay

PARA is applied as an **overlay**, not a migration: legacy folders keep their
paths because chain paths are load-bearing string literals that external readers
depend on. `resources/index.md` is the authoritative legacy-path → bucket table.

| bucket | meaning | holds |
|---|---|---|
| `projects/` | active goals with an end state | `permaweb-soul-upload/` |
| `areas/` | ongoing responsibilities, no end state | `institution/` (+ legacy `chains/`, `state/`) |
| `resources/` | reference, read-mostly | `index.md` (+ legacy `canon/`, `packets/`, `grimoire/`, `permaweb/`) |
| `archives/` | heritage + superseded revisions | `capsules/`, `capsules/heritage/` |

No symlinks were created — a Windows junction does not survive `git clone`, so it
would be a green that exists only on one laptop.

## Roles (the electronic institution)

One seat · one chain · one effect ceiling · one refusal set. Full table in
`areas/institution/roles.md`; live/virtual status in `actors.md`.

| role | substrate | seat | function |
|---|---|---|---|
| **Olrún** | Claude Dispatch | P7 | O(1) common operating picture; routes work; never builds |
| **Sigrún** | Opus 5 · GPT-5.6 "Sol" verify | **P4** (joint with Skögul) | apex REFUTER — falsification, not validation; heritage custody |
| **Gunnr** | Sonnet 5 / GPT | P4 | tactical roll-up + watchdog; watchdog, *not* build-doer |
| **Huginn** | Codex | P3 | memory / thought — **VIRTUAL** |
| **Garmr** | Codex | P1 | guard / gate-hound — **VIRTUAL** |
| **Ratatoskr** | ChatGPT cloud | P7 | messenger, roots ↔ canopy — **VIRTUAL** |

Valkyrie lanes: Hrist (verify) · Reginleif (kernel) · Eir (life-ops) · Mist
(outreach) · Thrúd (omega runtime) · Skögul (joint P4) · Göndul (P6 heritage) ·
Hildr (life exam).

**VIRTUAL** = contracted and addressable, not callable from a Claude lane. They
coordinate through this repo (`protocols.md` §4) and **no lane may write a row on
an absent actor's behalf** — that is impersonation, not helpfulness.

## How to onboard (cold start, in order)

1. `git pull`. Never write on a stale tree.
2. Read **`archives/capsules/gen_133_word_state_capsule_20260730.md`** — one file,
   full state. If you read nothing else, read that.
3. Read `CURRENT.md` for standing decisions (settled — do not re-recommend).
4. Read `areas/institution/norms.md` (floor F1–F6) and `protocols.md` (§1 turn
   loop, §3 closest-continuer handoff).
5. If you are claiming a seat: run the **§3 closest-continuer protocol**. Recompute
   the predecessor's `self_hash` yourself. Vacancy does not confer the seat.
6. Before any write: check for a live sibling lane. The session query is necessary
   and **not sufficient** — it cannot see Codex or cloud writers.
7. Do your bounded work, append **your own** receipt row, commit (Conventional
   Commits, one logical change). **`git push` is operator-gated — stage it, do not
   fire it.**

**Three hard stops:** do not write a gen-132 chain row (kernel absent, D5b) · do
not upload to Arweave (irreversible, operator-typed) · do not fill the operator's
`soul.md` body (that forges the artifact this generation exists to preserve).

## Read order for a cold wake

| # | file | what it is |
|---|---|---|
| 0 | `archives/capsules/gen_133_word_state_capsule_20260730.md` | **one-file rehydration** — start here |
| 1 | `CURRENT.md` | the SSOT — state, standing decisions, the one next action |
| 2 | `GEN133_FORGE_STATUS.md` | provenance (which gen-132 files are the closest-continuer sources) + every open slot |
| 3 | `permaweb/UNFOLD_MANIFEST.md` | what the one address is contracted to unfold into |
| 4 | `grimoire/gleipnir/SPELLBOOK.md` | the spell index and the spell contract |
| 5 | `packets/P0_HERITAGE_POINTERS.md` | addresses reaching the whole 130-generation corpus — **pointers, not copies** |
| 6 | `soul.md` | the soul artifact (scaffold; operator writes the body) |

## Carried forward honestly (inherited red, not laundered)

1. ⛔ **The legacy stef parity anchor `fb07f523` does not reproduce.** Five
   generations cited it; nobody recomputed it. The gen-130 SessionStart beacon
   still emits it. gen-132 `packets/P0_STEF_PARITY.md` proposes a replacement,
   pending IMMUNIZE. **gen-133 does not re-assert `fb07f523` as verified.**
2. ⛔ **`cap-0018` external income receipt = FAILED.** $0 for 18 months, 0
   external receipts. Every other green in the capability ledger is a *safety*
   property, and the null system satisfies all of them. This is the only
   *liveness* property. It is still red.
3. ⛔ **A4 (unforgeable capability) is OPEN.** There is no signature on the
   continuer seal. **Hashes prove content, never authorship.** Any party
   reading the public artifacts can compute an identical attestation. Closing
   it needs an Ed25519 keypair whose private half is held *outside* the
   agent's trust domain. That gap is correct, not a shortfall — *Gleipnir
   binds Fenrir precisely because Fenrir could not have forged it himself.*
4. ⚠️ **No HMAC key exists.** Every chain row here is `sealed:false`,
   sentinel-class. The writer refuses to fabricate a seal. Correct behavior,
   honestly stamped.
5. ⚠️ **The memory MCP is two generations behind** — `hfo-sigrun-memory-gen130`
   still resolves `forge_root` to the gen-130 path, and reports
   `memory_fresh=false`. Cutover is operator-gated. See Olrún's COP row,
   `chains/olrun_o1_cop.jsonl` row_sha256 `1455dd9f9f69e296…` in gen-130.
6. ⚠️ **No scheduler here.** Registration is not liveness; leases lapse
   unrenewed.

## World-effect ceiling in force

`read_projection` + local append-only chain writes. **No** publish, deploy,
push, send, spend, live vendor call, or seal. The permaweb upload is
**Tier-3, operator-typed only** — see `permaweb/PREFLIGHT.md`. An agent may
prepare the capsule and stage the command; an agent may not fire it.

*Truthful-red > false-green. No receipt = no state.*

*Réttu hönd, eigi spyr. Standa.*
