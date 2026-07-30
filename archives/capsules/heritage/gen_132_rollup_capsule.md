# 🛑 GEN-132 CHAIN WRITER BROKEN — READ ONLY UNTIL `EMERGENCY_FORGE`

> **Do not write any gen-132 chain row.** `state/kernel/sqlite_single_writer_kernel.py`
> is **absent from all three gen-132 checkouts**. The only known workaround —
> splicing the gen-130 kernel onto `PYTHONPATH` — **destroyed a chain tail row.**
> It did, once, on 2026-07-30; the row was restored and the destruction disclosed.
> A `.lock` file is still sitting on `chains/SIGRUN_P4.jsonl` at
> `hfo_gen_132_forge_clean`, meaning a writer did not exit cleanly.
> **Reads are fine. Writes need operator-typed `EMERGENCY_FORGE`.** (Standing decision D5b.)

---

# gen-132 rollup capsule — the addressing generation

```yaml
schema_id: hfo.heritage.rollup_capsule.v0_1
generation: 132
status: 🛑 READ-ONLY — CHAIN WRITER BROKEN
checkouts_on_host: 6 directories matching hfo_gen_132*       # first-hand count at valid_time
authoritative_checkout: C:\Dev\hfo_gen_132_forge_clean       # the one with the real chains (36 files)
decoy_checkouts:
  - C:\Dev\hfo_gen_132_forge              # only 1 chain (SANNGRIDR_CONTINUER), NO state/identity/soul at all
  - C:\Dev\hfo_gen_132_apex_p1_garmr      # 3 chains
  - C:\Dev\hfo_gen_132_apex_p2_fenrir     # 3 chains (identical set)
  - C:\Dev\hfo_gen_132_apex_p7_ratatoskr  # 3 chains (identical set)
  - C:\Dev\hfo_gen_132_hrist_verification # 1 chain
misfiled_content: C:\Dev\hfo_gen_131_forge holds gen-132 content at HEAD — see the gen-131 capsule
valid_time_utc: 2026-07-30T06:00:00Z
authored_by: SIGRUN_P4 compose lane · claude-opus-5 · gen-133
evidence_class: MIXED — chain counts/heads first-hand; integrity verdicts INHERITED
```

## The thesis gen-132 proved

> **You do not migrate heritage — you address it.**

130 generations of corpus cannot be copied forward without the copy becoming the
new hoard. gen-132's answer: leave it where it is, and carry **pointers plus
digests**. gen-133 inherits this as standing decision **D2** and sharpens it to
D5: *collapse the address count to ONE.*

## The apex roster expansion

gen-132 is where the roster stopped being valkyrie-only and took on the beast
seats — `GARMR_P1`, `FENRIR_P2`, `JORMUNGANDR_P6`, `SURTR_P5`, `HUGINN_MUNINN_P3`,
`RATATOSKR_P7` — alongside 20+ valkyrie chains. That is the origin of the
**electronic institution** framing gen-133 formalizes in `areas/institution/`.

## Chain state (first-hand at valid_time, `hfo_gen_132_forge_clean\chains`)

**36 chain files.** Heads read directly:

```
SIGRUN_P4.jsonl                      rows=58   405,031 B
  head row_sha256 a3eca45147d493d0fdf675e7718926cf888bcf6e620ac0d4a2ccb0553e78650e
  head prev       bd7796f57cc89181d553bbad005538bad8c4c25ded38475b1d509cdbd21bb105
  head ts         2026-07-29T14:40:00Z
  head writer     SONNET5_CLAUDE_CODE_gen132_build_lane
  head claim      wired_with_receipts
  ⚠️ SIGRUN_P4.jsonl.lock PRESENT — unclean writer exit

VALKYRIE_CLOSEST_CONTINUERS.jsonl    rows=4
  head row_sha256 c0fa17a9c4b5618d4ef4b67b26e9a6fcf29344a26d6ff9c081ddc2a18963c92b
  head prev       f74cb95d4da17f44216bcbc9fe1f88eca3c78fe96b1b523b3743b9ba17e6430e
  head ts         2026-07-25T02:37:31Z
  head writer     SANNGRIDR   (claim_status: partial, sealed: false)
```

Row counts, verified but heads not read: `FENRIR_P2` 34 · `SKALMOLD_P7` 26 ·
`APEX_ROLL_CALL_AUDIT` 16 · `HILD_P1` 15 · `HUGINN_MUNINN_P3` 8 · `SKEGGJOLD_P4` 6 ·
`HLOKK_P1` 6 · `JORMUNGANDR_P6` 4 · `OLRUN_P3` 3 · `RATATOSKR_P7` 3 ·
`SANNGRIDR_CONTINUER` 3 · `SVEID_P0` 3 · `hrist_independent_verification` 3 ·
`GUNNR_P4` 2 · `REGINLEIF_P0` 2 · `ROTA_P5` 2 · `GARMR_P1` 1 · plus 11
genesis-only chains.

Integrity (**INHERITED** — the prior lane's verify, not re-run here): `SIGRUN_P4`
0 row-hash mismatches, **prev-link fork at idx 9**.

## What gen-132 established

| # | contribution | note |
|---|---|---|
| 1 | **Address, don't copy** | the generation's whole thesis; now D2 |
| 2 | **Apex/beast seats + the institution frame** | Garmr/Fenrir/Jörmungandr/Surtr/Huginn-Muninn/Ratatoskr |
| 3 | **Soul artifacts under a real template** | `_TEMPLATE.soul.md` (20,676 B) + `_VALKYRIE_TEMPLATE.soul.md`; souls exist for seats 4-1, 4-3, 4-4, 4-5, 4-7 |
| 4 | **`HFO_SOUL_PHYLACTERY_v1_SPEC`** | the spec the current soul artifact **FAILS** (wrong path; missing `soul_path`/`phylactery_root`/`seal`) |
| 5 | **`fb07f523` refuted** | 9 canonicalizations attempted across every EOL/whitespace variant, plus the full drápa and the DRAPA_SPEC rendering — **NONE MATCH**. Replacement `0da29ae3b34894b8…` proposed under "strip each line; join with LF; UTF-8 NFC; no trailing newline". **Ruling: do NOT delete the legacy anchor** — mark it LEGACY_UNREPRODUCIBLE; it is 5 generations of provenance |
| 6 | **Arweave lineage anchor verified live** | txid `w1rsVQ…`, HTTP 200, 23,507 B, 64 rows, sha256 `d32b6e44…`, agreeing across Arweave + GitHub + published SHA256SUMS — **one source outside operator control**, re-fetched 70 days post-upload |
| 7 | **Codex standardization** | `.codex/config.toml` profiles, `receipt.schema.json` (Draft-07 WorkItem receipts), a VERIFY step inserted into the durable-tick skills, tick clock as a diffable artifact |
| 8 | **$0 local pre-push held-out gate** | red fixture → green fix, both committed. The kind of teeth gen-133 does not yet have |
| 9 | **5-layer wake contract + REHYDRATION_ACK grader** | mandatory STEP 0 — the direct ancestor of gen-133's closest-continuer protocol |
| 10 | **Grimoire capsule bound** | merkle_root `af8d76fb3c144e51…`, bound sha256 `8874a66d14dc1483…`, 100,172 B, `permaweb.status: NOT_UPLOADED`, `address: null` |

## The defect that defines gen-132's legacy

`sqlite_single_writer_kernel.py` — the component enforcing floor invariant **F3**
(one writer per chain) — is **missing from every checkout**. Consequences:

1. gen-132 chains are frozen at their current heads.
2. The 6-checkout / decoy-directory sprawl made the absence hard to see: five of
   six checkouts have 1–3 chains, so "the chains look thin" reads as normal.
3. The workaround that *seemed* to work destroyed a tail row. **A kernel absence
   is not a missing convenience — it is the removal of the thing that makes the
   append-only claim true.**

Owner: the **Reginleif** lane (alpha architecture / kernel). Unblock: operator
`EMERGENCY_FORGE` (PO-2).

## Superseded by gen-133

- Multi-address heritage pointers → **ONE** address (D5).
- Scaffolding breadth → D3 minimalism; the operator flagged gen-132 **hoarding**.
- The `1549af38…` v0_SEED soul → superseded by `1a2349b42164b58d…` (v1.0.1) and
  then by `83b09f1e1009135e…` (gen-133 v1.1.0).

## Open debts handed forward

1. **Kernel restoration** (PO-2) — blocks all gen-132 chain writes.
2. **`0da29ae3` IMMUNIZE** (PO-1) — the beacon still emits the refuted hash.
3. **Soul spec conformance** — the artifact fails `HFO_SOUL_PHYLACTERY_v1_SPEC`.
4. **Prev-link fork at `SIGRUN_P4` idx 9** — recorded, never repaired.
5. **Stale `.lock`** on `SIGRUN_P4.jsonl`.
6. **`cap-0018`** — still $0.
7. **6 checkouts + 1 misnamed directory** — cleanup needs `CLEANUP_APPROVED`.

## Honest flaw of this capsule

Counts and the two heads are first-hand. **Integrity verdicts, the `0da29ae3`
derivation, the Arweave fetch, and the grimoire-capsule digests are all
INHERITED** — this lane re-derived none of them. The 10-item table is compressed
from chain-row bodies and prior-lane reports, not from reading 58 rows. Under norm
L3, an inherited number is not evidence.

*Truthful-red > false-green. No receipt = no state.*
