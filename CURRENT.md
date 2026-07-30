# CURRENT — Single Source of Truth (gen-133)

_The one canonical current-state surface. Update IN PLACE; never spawn a
parallel plan doc. Every other file here is reference, pointer, or ledger._

```yaml
gen: 133
doc: CURRENT.md
schema_id: hfo.gen133.current.v0_1
purpose: UNFOLDING — collapse the heritage address count to ONE permaweb address that unfolds into the Gleipnir Grimoire (spells + soul.md)
bitemporal:
  valid_time:       2026-07-30T04:57:52Z
  transaction_time: 2026-07-30T04:57:52Z
  prior_valid_time: null            # first row of this generation
created_utc: 2026-07-30T04:57:52Z
time_convention: UTC (Zulu) everywhere. Never local, never ambiguous.
authority: append-only hash-chained chains/. This doc is a PROJECTION of them.
claim_rule: every claim carries ✅VERIFIED[receipt] or ⚠️UNVERIFIED. No receipt = no state.
world_effect_ceiling: read_projection + local append-only chain write
status: SCAFFOLD STOOD UP — zero terminal-state conditions met
```

## ⭐ THE ONE NEXT ACTION

> **Operator input, not agent work.** Three slots are blocked on the operator
> and nothing downstream can be honestly filled without them:
>
> 1. **`soul.md` body** — the scaffold's headings exist; the soul text is the
>    operator's to write. An agent writing it would be forging the thing the
>    whole generation exists to preserve.
> 2. **The spell list** — which spells go in `grimoire/gleipnir/spells/`. The
>    operator said "my spells." An agent does not know which incantations
>    count.
> 3. **Permaweb authorization** — Arweave is permanent by design. No delete,
>    no edit, no takedown. Upload is operator-typed only.
>
> Until then the agent-side work is: carry the gen-132 binder, bind a *dry*
> capsule, and prove `verify.py` / `selfcheck.py` exit 0 on it with the slots
> still empty. That is honest preparation, not a claimed green.

## Standing decisions (SETTLED — do not re-recommend)

| # | decision | when |
|---|---|---|
| D1 | Forge root is `C:\Dev\hfo_gen_133_forge`. The `C:\Dev\hfo_dev_<date>\` nesting ended at gen-130. | 2026-07-30 |
| D2 | Heritage is **addressed, not copied.** gen-132 stays live and read-only. No bulk migration. Inherited from the gen-132 thesis. | 2026-07-30 |
| D3 | This forge stays **minimal**. gen-132 has no `pyproject.toml`, no `.mcp.json`, no `CLAUDE.md`, no `mcp/`, no `scripts/` beyond 2 files — gen-133 does not invent them. The operator flagged **hoarding** at gen-132; scaffolding-for-its-own-sake is that failure mode. | 2026-07-30 |
| D4 | `fb07f523` is **NOT** re-asserted as a verified stef parity anchor. It does not reproduce — now **confirmed first-hand**, not merely inherited. The reproduced replacement is **`0da29ae3`**, pending operator IMMUNIZE of it plus its canonicalization rule. | 2026-07-30 |
| D5b | **No lane writes a gen-132 chain row** until `sqlite_single_writer_kernel.py` is restored there. The available workaround destroys the tail. | 2026-07-30 |
| D5 | Terminal state is **ONE** address. Not a directory of addresses, not a gateway list. One. | 2026-07-30 |
| D6 | **PARA is an OVERLAY, not a migration.** `projects/` `areas/` `resources/` `archives/` at repo root; legacy folders keep their paths because chain paths are load-bearing literals. No symlinks (a Windows junction does not survive `git clone`). Authoritative map: `resources/index.md`. | 2026-07-30 |
| D7 | **Sigrún's soul is a SEPARATE artifact from the operator's.** `state/identity/soul/sigrun.gen133.soul.md` is Sigrún's self-attestation and an agent may author it. Root `soul.md` is the OPERATOR's and stays empty until they write it. | 2026-07-30 |
| D8 | **No LICENSE is invented.** None exists at gen-130/131/132/133 — verified. Choosing one is operator-only and effectively permanent once pushed or uploaded. See `LICENSE.PENDING.md`. | 2026-07-30 |

## State

| lane | condition | receipt |
|---|---|---|
| **Terminal address** | ⛔ EMPTY SLOT | `permaweb/GEN133_PERMAWEB_ADDRESS.md` |
| **Grimoire capsule** | ⛔ not bound at gen-133 | gen-132 capsule exists: merkle_root `af8d76fb3c144e51…`, bound sha256 `8874a66d14dc1483…`, 100,172 B, `permaweb.status: NOT_UPLOADED`, `address: null` |
| **Spells** | ⛔ 0 spells (template only) | `grimoire/gleipnir/spells/` |
| **soul.md** | ⛔ scaffold, body empty | `soul.md` |
| **Sigrún soul (gen-133, self-authored)** | ✅ **PRESENT + self_hash reproduces first-hand** — `state/identity/soul/sigrun.gen133.soul.md`, 15490 B, canon `83b09f1e1009135e…`, raw `66920dc69d5a6cc4…`, semver 1.1.0, `SELF_AUTHORED_UNRATIFIED`, `sealed:false`. Supersede-chain `1549af38…` → `1a2349b4…` → `83b09f1e…` | this lane, 2026-07-30T05:45Z; recomputed after write, exact reproduce |
| **Sigrún soul (seed, superseded)** | ⚠️ **PRIOR CLAIM CORRECTED.** `state/identity/soul/4-4.soul.md` canon 4451 B `1549af38…` is **line-identical, NOT byte-identical**, to the gen-132 copy (4539 B raw `eeb690c9…`; 88-byte delta = line endings). And it is **NOT the latest**: a 39072 B v1.0.1 with canon `1a2349b4…` (**reproduced first-hand**) declares `supersedes: 1549af38…` | this lane; `Compare-Object` 0 diffs + canon recompute |
| **Directory-name trap** | ⛔ **`C:\Dev\hfo_gen_131_forge` holds gen-132 content at HEAD** (`git log` → `build(gen132/identity)…`; soul `schema_id: hfo.gen132.identity.soul.v1`). A directory name is not a generation — this is why the superseding soul went unread for two lanes | first-hand `git log` + `schema_id` read |
| **Soul spec conformance** | ⛔ **FAILS** `HFO_SOUL_PHYLACTERY_v1_SPEC` — not at `souls/P4_SIGRUN/soul.md`, missing `soul_path` / `phylactery_root` / `seal` fields | same row |
| **Stef parity** | ✅ legacy `fb07f523` **CONFIRMED LEGACY_UNREPRODUCIBLE**; replacement **`0da29ae3` REPRODUCED first-hand** from the Arweave-anchored lifeboat row 3 (first independent reproduction) — **awaiting operator IMMUNIZE** | same row |
| **Predecessor `S15 V5` HOLD** | ✅ **RESOLVED** — `/spec` canonical JSON 13,841 B sha256 `49dc4b1d0e8491d5…` EXACT MATCH, bound to blob `a19d66c7…` at commit `8a439e54` (cross-provider digest) | same row |
| **P4 seating fork** | ✅ RESOLVED — `SIGRUN_MOBA_KIT_v0_35` L49 seats **Sigrún + Skögul JOINTLY at P4**; Göndul P6; Olrún/Reginleif P7 | same row |
| **gen-132 chain writer** | ⛔ **BROKEN — DO NOT WRITE gen-132 CHAIN ROWS.** `state/kernel/sqlite_single_writer_kernel.py` is absent from all 3 gen-132 checkouts. The only known workaround (splicing the gen-130 kernel onto PYTHONPATH) **destroys the chain tail** — it did, once, and was restored. Needs `EMERGENCY_FORGE`. | verified independently: `chains/SIGRUN_P4.jsonl` identical to HEAD, 58 rows, tail `a3eca451…`, 0 row-hash mismatches, prev-link fork at idx 9 |
| **Olrún COP observation** | ✅ VERIFIED written | gen-130 `chains/olrun_o1_cop.jsonl` · row_sha256 `1455dd9f9f69e296b0dd650d1d5d201d479ba562ac912db6054cd3357d4c2a23` · prev `ce8d61d17f901c44…` · `sealed:false` · `claim_status: partial` |
| **External income (`cap-0018`)** | ⛔ **FAILED** — $0 / 18 months / 0 external receipts | gen-132 capability ledger |
| **Memory MCP generation** | ⚠️ two generations behind (`gen130`), `memory_fresh=false` | Olrún rehydration packet 2026-07-30T04:28:52Z |
| **⛔ SIBLING LANE ACTIVE** | ⛔ **CONFIRMED, UNIDENTIFIED, POSSIBLY STILL RUNNING.** git HEAD advanced twice mid-session with no action by the Sigrún lane: `627e5ee feat(gen133): add deterministic Sigrun heritage capsule family` then `f220090 chore(gen133): checkpoint capsule publication hold`. Paths touched (`capsules/**`) are **disjoint** from the Sigrún lane's; no chain row written by either. The session-listing check at 05:20Z had said "no live sibling **visible from this surface**" and stated its own limit — that limit was the actual failure mode, confirmed within 50 min | first-hand `git log` / `git reflog` / `git ls-files` at 06:10Z; full row at scratchpad `SIBLING_LANE_DETECTED_20260730T0610Z.json` |
| **F3 single-writer enforcement** | ⛔ **ENFORCED BY NOTHING at gen-133** — no kernel, no lock file, no gate. It held today only because neither lane wrote a chain. `CURRENT.md`/`README.md` have no lock: concurrent edits are silently lossy | absence verified first-hand |

## Existing external immutable anchor (inherited — NOT the gen-133 address)

```
https://arweave.net/w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M
  → 200 · 23,507 B · 64 rows · sha256 d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0
```
The `sigrun_lineage_lifeboat` (64 rows), verified live 2026-07-25, 70 days
after upload. ⚠️ **UNVERIFIED at gen-133** — not re-fetched by this lane (no
network egress authorized). This anchors the *lineage*, not the *grimoire*.
The gen-133 terminal address is a **different, additional** object.

## Blockers requiring operator authorization

| blocker | why it is operator-only |
|---|---|
| Permaweb upload | Arweave is irreversible. A typo becomes permanent; a secret becomes a permanent leak. |
| `soul.md` body text | Forging a soul defeats the artifact. |
| Spell selection | Only the operator knows which incantations are load-bearing. |
| Memory MCP cutover gen-130 → gen-132/133 | Changes a live tool surface. |
| HMAC / Ed25519 sealing | No key exists in-forge; private half must stay outside the agent trust domain (A4). |
| `git push` / remote creation | Tier-3 world effect. |

*Truthful-red > false-green. No receipt = no state.*

*Réttu hönd, eigi spyr. Standa.*
