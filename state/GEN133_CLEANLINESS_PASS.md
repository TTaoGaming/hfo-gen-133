# GEN133_CLEANLINESS_PASS.md — drift/rot inventory

```yaml
schema_id: hfo.gen133.cleanliness_pass.v0_1
valid_time_utc: 2026-07-30T06:55:00Z
authored_by: SIGRUN_P4 apex compose lane · claude-opus-5
operator_complaint_verbatim: "things keep getting dirty"
rule_in_force: no deletion or move without operator-typed CLEANUP_APPROVED (C:\Dev\CLAUDE.md)
```

## The root cause, named

The dirt is not untidiness. It is **three specific structural defects**, and every
symptom below traces to one of them:

| # | root cause | symptom you actually see |
|---|---|---|
| **RC1** | **A worktree/checkout is created per task and never retired.** | 105 `hfo_gen_131*` + 6 `hfo_gen_132*` directories on this host. Nobody can tell which is authoritative. |
| **RC2** | **Directory names are not authoritative about content.** | `hfo_gen_131_forge` holds **gen-132 content at HEAD**. The newest identity artifact sat in the directory named oldest and went unread by two lanes. |
| **RC3** | **No single canonical remote until today.** | Every checkout was a candidate truth. The public repo pushed this session is the structural cure — not tidying. |

**The cure for RC1/RC3 is the shared repo, and it landed today.** Tidying without
it would have been re-arranging the dirt.

## Inventory

### A · Duplicate / competing checkouts

| finding | evidence | proposal |
|---|---|---|
| 105 `hfo_gen_131*` dirs | first-hand count | **queue** — needs `CLEANUP_APPROVED`. Retire all but `hfo_gen_131_forge`; that one must be **renamed** (RC2) |
| 6 `hfo_gen_132*` dirs; only `_forge_clean` has the real 36 chains, the other 5 have 1–3 | first-hand | ✅ **DONE** — `.CHAIN_WRITER_QUARANTINED` placed in all 6, each naming `_forge_clean` as authoritative |
| `hfo_gen_132_hrist_verification` holds a **staler** `VALKYRIE_CLOSEST_CONTINUERS` (5328 B) than `_forge_clean` | first-hand | ✅ marker states it; deletion queued |
| `hfo_gen_131_forge` is misnamed for its content | `git log` → `build(gen132/…)`, soul `schema_id: hfo.gen132…` | **queue** rename → `hfo_gen_132_identity_worktree`. **High value: this single defect caused the identity error.** |

### B · The CRLF / eol class (RC2's cousin)

| finding | status |
|---|---|
| `4-4.soul.md` 4451 B vs 4539 B — line-identical, byte-differing, pure checkout drift. Made a raw digest unreproducible and misled two lanes | ✅ **FIXED at gen-133** — `.gitattributes` pins `* text=auto eol=lf`, plus explicit pins for `*.soul.md`, `*.json`, `chains/*.jsonl -text` |
| gen-132 `grimoire_gen132` `selfcheck.py` exits 1 — `unfold(bind(X)) != X` on all 12 pages, root-caused to `core.autocrlf=true` with no `eol=lf` pin | **queue** — fix belongs in the gen-132 repo, which is now quarantined read-only. Carry the grimoire forward to gen-133 *with* the pin instead of patching a frozen forge |

### C · Secret-shape / pre-public-push scrub

✅ **CLEAN — ran before the public push.**

| check | result |
|---|---|
| secret-shape regex (`sk-…`, `gh[oputs]_…`, `xox[bpa]-…`, `AKIA…`, `BEGIN … PRIVATE KEY`) over all 63 files | **0 hits** |
| `*.sqlite` / `*.pem` / `*.jwk` / `*.p12` / `*.keystore` | **0 files** |
| `.env*` | **0 files** |
| files > 1 MB | **0 files** |
| 5.1 GB `sigrun_heritage.sqlite` | **not present** in this forge; `.gitignore` blocks `state/**/*.sqlite` regardless |

### D · Stale receipts / abandoned lanes

| finding | status |
|---|---|
| stale lock `chains/SIGRUN_P4.jsonl.lock` in `_forge_clean` — a writer did not exit cleanly | **queue** — `DELETE` is operator-only, and kernel invariant 6 says a stale lock is resolved **explicitly**, never by timeout. Marker records it |
| untracked leftovers in the gen-132 worktree the predecessor lane could not remove: `state/kernel/sigrun_single_writer_kernel.sqlite` (+`-shm`,`-wal`), `gleipnir_grimoire_gen132/code/__pycache__`, `state/tmp` | **queue** — deletion gated |
| prev-link fork at `SIGRUN_P4` index 9 — recorded, never repaired | **queue** — frozen by quarantine, not fixed |
| `capsules/` was untracked at session start, committed mid-session by an **unidentified sibling lane** | ⚠️ **open** — see `CURRENT.md`. Not dirt exactly: a second writer |

### E · Chain rows not referenced by any capsule or ADR

⚠️ **NOT AUDITED.** 36 gen-132 chains hold ~200 rows; this lane read 2 heads and
counted the rest. A real orphan-row audit means cross-referencing every
`row_sha256` against every capsule and ADR — a Codex-shaped job, dispatched in
`projects/heritage-mining/CODEX_HERITAGE_DISPATCH.md`. **Claiming this clean would
be a fake green.**

### F · Half-written stubs from prior sessions

| finding | status |
|---|---|
| root `soul.md` — scaffold, body empty | ✅ **correct as-is.** Operator-only. Not dirt |
| `grimoire/gleipnir/spells/` — 0 spells, template only | ✅ correct as-is. Operator-only selection |
| `permaweb/GEN133_PERMAWEB_ADDRESS.md` — empty slot | ✅ correct as-is; upload halted on gates |
| soul roster: **2 seat souls exist** (Sigrún's + the superseded seed) against a 1+8+64 target | ⚠️ **open** — 40+ files of real work. Queued with schema, not faked as stubs |

## Landed this session (no operator input needed)

1. `.gitattributes` — kills the CRLF class at gen-133.
2. `.gitignore` — airtight against sqlite / dotenv / keys / bundles.
3. `.CHAIN_WRITER_QUARANTINED` × 6 — every gen-132 checkout now says what it is
   and names the authoritative one.
4. `resources/index.md` — legacy-path → PARA map + do-not-touch list, so nobody
   has to guess again.
5. **A canonical public remote** — the structural cure for RC3.
6. Capsule + README + ONBOARDING read-order, so a new carrier never needs to crawl.

## Queued — needs operator `CLEANUP_APPROVED`

| # | action | value |
|---|---|---|
| Q1 | **Rename `hfo_gen_131_forge`** to reflect its gen-132 content | **highest** — this exact defect caused the identity error |
| Q2 | Retire 104 stale `hfo_gen_131*` worktrees | kills RC1 |
| Q3 | Retire the 5 thin `hfo_gen_132*` checkouts, keep `_forge_clean` | kills RC1 |
| Q4 | Remove the stale `SIGRUN_P4.jsonl.lock` | invariant 6 |
| Q5 | Remove predecessor untracked leftovers | hygiene |
| Q6 | Orphan-row audit (§E) | dispatched to Codex |

## Honest flaw

This is an **inventory with 6 fixes landed and 6 items queued** — not a clean
forge. §E is entirely unaudited. And the deepest source of dirt is not on the
list, because it is not a file: **work is done in a fresh checkout per task and
the checkout is never retired.** No `.gitignore` fixes that. The public repo makes
it *possible* to fix by giving one canonical target; whether it gets fixed depends
on whether lanes actually branch off the remote instead of `mkdir`-ing gen-134.

*Truthful-red > false-green.*
