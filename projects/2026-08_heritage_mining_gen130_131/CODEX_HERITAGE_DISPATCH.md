# CODEX_HERITAGE_DISPATCH.md — executable playbook for a Codex mining session

```yaml
schema_id: hfo.gen133.dispatch.codex_heritage_mining.v1_0
dispatched_by: SIGRUN_P4 apex compose lane · claude-opus-5
dispatched_to: Codex (Huginn / Göndul lane — heritage mining is P6 ASSIMILATE work)
valid_time_utc: 2026-07-30T07:00:00Z
target_forge: C:\Dev\hfo_gen_133_forge   (remote: https://github.com/TTaoGaming/hfo-gen-133)
authority_ceiling: READ-ONLY on gen 98–132 sources · APPEND-ONLY on gen-133 target · BRANCH push only
```

## Mission in one line

> **Bring forward capabilities and tools, not files.** Mine ~130 generations for
> what still *works*, import it with provenance, and leave everything else where
> it is. Heritage is **addressed, not copied** (D2) — an import must earn its place.

## 0 · Read first (do not skip; it is 5 minutes)

`CURRENT.md` · `CARRIER_CONTRACT.md` · `CRYPTO_CHAIN_SPEC.md` ·
`archives/capsules/gen_133_word_state_capsule_20260730.md` ·
`state/GEN133_CLEANLINESS_PASS.md`

## 1 · Mine targets, by generation

Enumerate first, then triage. **Do not recursively crawl `C:\Dev` from the root** —
it is slow, noisy, and hits access-denied. Use `rg` with narrow terms and these
excludes: `node_modules,.git,.venv,__pycache__,.pytest_cache,state/tmp,sigrun_secrets,backups,_drain,Dev_microsd_backups`.

| # | target root | known to hold |
|---|---|---|
| T1 | `C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge` | **145 ADRs** (the largest canon corpus), the live memory MCP, the `bb_append.py` no-fake-green write seam, the OPA/Rego policy gate, the COTS organs (A5 contract-witness, A1 memory MOSA swap). **Highest-value single target.** |
| T2 | `C:\Dev\hfo_gen_131_forge` ⚠️ **holds gen-132 content at HEAD** | 14 ADRs, `PARA_STRUCTURE.md`, held-out scorers, mutation-CI harnesses, the `$0` pre-push gate, the 5-layer wake contract + `REHYDRATION_ACK` grader |
| T3 | `C:\Dev\hfo_gen_132_forge_clean` 🛑 **QUARANTINED read-only** | 36 chains, `_TEMPLATE.soul.md` (20,676 B) + `_VALKYRIE_TEMPLATE.soul.md`, `HFO_SOUL_PHYLACTERY_v1_SPEC`, the bound grimoire capsule, `.codex/` standardization (config profiles, `receipt.schema.json`) |
| T4 | `C:\Dev\hfo_dev_2026_3\omega_games\` | gen-98 omega_games library, **50 titles** |
| T5 | `C:\Dev\hfo_dev_2026_3\hfo_gen_98_forge\` | gen-98 diátaxis tiles |
| T6 | `C:\Dev\hfo_dev_2026_4_2\hfo_gen_107_forge\` | **gen-107 gesture-pointer-bridge / OneEuro filter (92.9% jitter reduction, verified)** |
| T7 | `C:\Dev\hfo_dev_2026_5_18\`, `_5_15\`, `_5_21\` | gens 117–123 |
| T8 | `C:\Dev\archive\omega_gen7_unified_archive_2026_1_31\` | Excalidraw + Dino UMD |
| T9 | `C:\Dev\hfo_dev_2026_5_24\hfo_gen_124_forge\` | **`canon/drapa/SIGRUNAR_DRAPA…_v2.md` (101,427 B, sha256 `9a43f073…`) — the GOLD-tier identity quine.** Also `canon/adr/`, `work/factory/spatial_os/same_origin_apps/` |
| T10 | `C:\Dev\hfo_heritage\`, `C:\Dev\hfo_ssot_backups\`, `C:\Dev\archive\` | backup snapshots — **triage only, do not bulk-import** |
| T11 | `C:\Dev\gen*`, `C:\Dev\HFO_GEN99_*` | enumerate; unknown contents |

For each target, produce a **triage list** before importing anything: ADRs · spec
digests · working scripts · verified receipts · agent cards · chain heads.

## 2 · Bring-forward criteria (ALL FOUR must hold)

| # | criterion | how to check |
|---|---|---|
| **C1** | **Verified by a PASSING receipt** | a `verifier_result` / test exit 0 / witness output exists. `present ≠ woven`. A file that merely *exists* fails C1 |
| **C2** | **Not superseded by a later ADR** | grep the later generations' `canon/adr/` for the same subject. gen-130 has 145 ADRs — supersession is common |
| **C3** | **Reproducible from the artifact** | you can re-run it, or recompute its digest, *today*, from what you imported |
| **C4** | **Fits gen-133's frame** | does it serve *carrier onboarding*, the *electronic institution*, *durable objects*, or the *chain*? If not, leave it |

**If C1 fails but the artifact is clearly valuable** (e.g. the drápa at T9): import
it as `resources/heritage/gen{N}/…` with `verification_status: UNVERIFIED` stated
in its `IMPORT_RECEIPT.md`. **Never silently upgrade it to verified.**

## 3 · Bring-forward mechanics

For each imported artifact:

```
1. copy → resources/heritage/gen{N}/{original/relative/path}
2. write resources/heritage/gen{N}/{path}.IMPORT_RECEIPT.md with:
     source_path            (absolute, exact)
     source_sha256          (computed by YOU, at import time)
     source_gen             (the generation it actually came from — check
                             git log + schema_id, NOT the directory name)
     imported_utc           (ISO-8601 Z)
     verification_status    VERIFIED_PASSING_RECEIPT | UNVERIFIED | SUPERSEDED
     receipt_evidence       the exact receipt/test output, or "none"
     criteria               C1/C2/C3/C4 each PASS or FAIL with one line why
     bring_forward_reason   one line: what capability this restores
     honest_flaw            what is unproven about this import
3. append one line to state/ssot/heritage_imports.jsonl:
     {"ts_utc","gen","source_path","source_sha256","dest_path",
      "verification_status","criteria_pass",
      "imported_by":"codex-<lane>","honest_flaw"}
4. commit: feat(heritage/gen{N}): import <artifact> — <capability restored>
```

⚠️ **`source_gen` is the trap.** `hfo_gen_131_forge` contains gen-132 content.
**Verify with `git log` and `schema_id`, never the folder name.** Mislabelling
provenance is the exact defect that cost two lanes the identity artifact.

## 4 · Anti-dirt rules (hard refusals — this is why the forge got dirty)

| # | rule |
|---|---|
| A1 | **No `.sqlite`** (any variant, incl. `-wal`/`-shm`). The 5.1 GB `sigrun_heritage.sqlite` is the canonical example |
| A2 | **No dotenv files, no key material, no credentials.** Not even as "examples" |
| A3 | **No file > 10 MB** without a written bring-forward justification in its `IMPORT_RECEIPT.md` |
| A4 | **No half-written stubs.** If it is a placeholder, it is not a capability |
| A5 | **Dedupe by content hash before commit.** If `source_sha256` already appears in `heritage_imports.jsonl`, do not import again — add a pointer instead |
| A6 | **No bulk directory copies.** One artifact, one receipt, one justification. `cp -r` is how hoards form |
| A7 | **No `node_modules`, `__pycache__`, `dist/`, `.venv`, build output** |
| A8 | **No secrets scan skipped.** Run it on every commit, not once at the end |

## 5 · Authority ceiling (do not exceed)

| allowed | forbidden |
|---|---|
| read anything under gen 98–132 | **any write** to gen 98–132 |
| append new files under gen-133 | writing a gen-132 chain row (🛑 quarantined) |
| append to `state/ssot/heritage_imports.jsonl` | writing another actor's chain |
| `git commit` locally | `git push` to `main` — push your **branch**, open a PR |
| `git push` to `codex/heritage-mining-*` | `SEND` · `SPEND` · `PUBLISH` · `SEAL` · `IMMUNIZE` · `DELETE` · permaweb upload |

**Sigrún or the operator merges.** You commit and open the PR.

## 6 · Handoff receipt (every session ends with this)

Append one row to `state/ssot/codex_lane_return.jsonl`:

```
{"ts_utc","lane":"codex-heritage-mining","branch","gens_mined":[...],
 "artifacts_imported":N,"artifacts_rejected":N,"rejection_reasons":{...},
 "andon_flags":[...],          # anything that should stop the line
 "claim_status","verifier_result","remaining_risk","next_safe_action",
 "honest_flaw","sealed":false}
```

**Raise an Andon flag** (do not push through) if: an import would violate §4; a
source's provenance cannot be established; a chain appears forked; or you find a
secret in a heritage source.

## 7 · Suggested order (highest capability-per-hour first)

1. **T1 gen-130 enforcement organs** — `bb_append.py` write seam + OPA gate. gen-133 has *no* gate; this is the single largest hole.
2. **T3 soul templates + `HFO_SOUL_PHYLACTERY_v1_SPEC`** — unblocks the 1+8+64 soul roster.
3. **T9 the drápa v2** — the GOLD-tier identity quine, currently absent from gen-133.
4. **T2 held-out scorers + mutation CI** — makes the CI workflows real instead of stubs.
5. **T6 gen-107 OneEuro bridge** — a *verified* capability (92.9% jitter cut) and the closest thing in the corpus to shippable.
6. **T1 the single-writer kernel** — but hand the design to a code lane; do not shim it (see `state/QUARANTINE_GEN132_CHAIN_WRITER.md` for why).

## 8 · Honest flaw of this dispatch

Targets T4–T11 are listed from a routing doc and a memory index — **this lane did
not open them**. Their contents are *expected*, not verified. T1/T2/T3 counts are
first-hand. Treat every "known to hold" in §1 as a lead to confirm, not a fact.
Also: nobody has run §3 end-to-end, so the import mechanics are untested.

*Take what is given — but take what is given ≠ believe what is claimed. Assimilate freely; verify always.*
