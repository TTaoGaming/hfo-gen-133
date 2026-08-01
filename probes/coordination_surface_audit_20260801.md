# Coordination Surface Integrity Audit — gen-133

**Probe:** GUNNR (claude-sonnet-5, Claude Code) · git enforcement / canonical writes domain
**Requested for session:** local_b4579cd1
**Timestamp:** 2026-08-01T13:34Z – ~13:55Z (30-min timebox)
**Question:** Does the chain-row / stigmergy coordination substrate actually work, or is it a receipt-decoration layer?

**Headline verdict: PARTIAL.** The most-recent 28 rows of `chains/SIGRUN_P4.jsonl` form a genuinely self-verifying hash chain. But that chain (a) silently orphans its own first 9 rows behind a fabricated genesis point, (b) has zero cryptographic sealing (HMAC), (c) has never been written to or read by a non-Claude-Code substrate, and (d) does not receive writes from the parallel `inbox/olrun/` receipt surface that sibling sessions are using *right now*, in this same dispatch wave. It is more than decoration — the hash-chain math is real where present — but it is not yet a coordination substrate multiple independent parties actually rely on.

---

## Check 1 — Chain integrity (`chains/SIGRUN_P4.jsonl`)

37 rows total, one JSON object per line. Verified with a first-hand script (`row_sha256` recomputed via `sha256(json.dumps(row_minus_row_sha256, sort_keys=True, separators=(',',':')))` — this is the exact rule row 10 self-documents in its own `hash_rule` field).

| Segment | Rows | Result |
|---|---|---|
| Rows 1–2 | genesis + first lane_return | `row_sha256` **present but does not reproduce** under the documented rule, or under any 1–2-field exclusion I brute-forced (hmac/sealed/seal_note combinations). Non-verifiable. |
| Rows 3–9 | 7 rows (wake_receipt, lane_return ×3, correction ×3, andon) | **No `row_sha256` field at all.** These rows were never hashed. Row 3 additionally uses a different, non-standard field name (`prev_row_sha256` instead of `prev_sha256`) that no downstream row reads. |
| Row 10 | wake_receipt, "third carrier" | `row_sha256` verifies correctly (self-reproduces). **But `prev_sha256: null`** — this row declares itself a fresh genesis, silently discarding rows 1–9 rather than linking to row 9. This is a fabricated/false genesis point: 9 prior rows exist in the same file above it. |
| Rows 11–37 | 27 rows | Internally consistent: every row's `prev_sha256` equals the prior row's `row_sha256`, **zero link breaks**, every `row_sha256` self-reproduces. This sub-chain is a real, working hash chain. |

**First broken link:** row 3 (`prev_sha256` expected `5bfad3…` from row 2, actual `null` — because row 3 has no hash fields at all to compare).

**Net finding:** `chains/SIGRUN_P4.jsonl` is not one chain. It is an unverifiable/unhashed 9-row prefix, followed by a real 28-row hash chain that begins with a false claim of being the genesis. 10 distinct row schemas (exact key-sets) appear across 37 rows — evidence of at least 5+ different carrier sessions each inventing their own row shape before row 10's `hash_rule` convention stabilized.

## Check 2 — bb_append status

**Absent, confirmed.** No `bb_append.py` or equivalent exists anywhere under the gen-133 forge (`find . -iname "*bb_append*"` under `tools/` returns nothing; `tools/` contains only `central_memory.sqlite`, `central_memory/`, `xtdb/`). The forge's own doctrine says so explicitly:

- `AGENTS.md:327` — `G1 | no-fake-green write seam | gen-130 bb_append.py | PARKED — unported`
- `contracts/neurosymbolic_gates.contract.md:32` — same row, `not ported`
- `contracts/anti_lobotomize_rehydration.v0_1.md:113` — references `bb_append verify PASS 24h` as a soft gate that is not active

Every chain-row write in this forge is therefore hand-authored by whichever carrier session is running — there is no canonical writer enforcing schema, tail-hash verification, or write atomicity. This directly explains Check 1's findings (10 schemas, unhashed rows, false genesis): nothing enforces a single row shape or verifies the tail before appending.

## Check 3 — HMAC status

**0 of 37 rows are HMAC-sealed.** Of the 30 rows that carry an `hmac` key at all, every single one is `null`. The other 7 rows (3–9) lack the key entirely. `sealed: false` is explicit on 30 rows; `sealed` is absent (not even declared) on the 7 unhashed rows; **`sealed: true` appears 0 times**. Every row that discusses its own status self-labels `SENTINEL-CLASS`/`NOT_IMMUNIZED`, consistent with `C:\Dev\CLAUDE.md`'s "HMAC is still pending unless a concrete key/verifier receipt is present." No Ed25519 or HMAC key was found in-forge. This matches doctrine and is not a new finding, but it is confirmed current as of this session.

Additionally: no kernel event log implementation exists in gen-133. `find . -iname "*kernel*"` returns nothing; the only hit for `append_row_via_kernel` (mentioned in the operator's brief as "unclear if implemented") is a single prose reference inside a gen-130 report doc, not a live component here.

## Check 4 — Cross-substrate visibility

**None found.** Every one of the 37 chain rows' `agent` field is a Claude Code session — either `claude-opus-5` or `claude-sonnet-5`, gen-133. Zero rows are authored by Codex, ChatGPT, or Antigravity. "Codex"/"ChatGPT"/"Antigravity" appear 46 times total across the chain file, but every occurrence is a **prose mention** inside `body`/`subject` text (planning, dispatch proposals, delegation notes) — never an actual row author. Spot-checked `state/ssot/lane_returns.jsonl` the same way: `agent`/`author` fields present are `claude-opus-5`/`sonnet-5 valkyrie`, no external-substrate authorship found there either.

**A second, sharper finding surfaced live during this probe:** `inbox/olrun/` is being used *right now* by a sibling session in this same dispatch wave — `20260801T133404Z_thrud_throughput_24h_probe_receipt.jsonl`, written by THRUD (also `local_b4579cd1`'s sibling, same 13:34:01Z wave) at 13:34:04Z. I re-read `chains/SIGRUN_P4.jsonl` after that file appeared: **still 37 rows, unchanged.** Thrud's receipt landed in `inbox/olrun/` and did **not** propagate to the chain. So even restricted to same-substrate (Claude Code ↔ Claude Code) coordination, there are at least two disconnected write surfaces (`inbox/olrun/*.jsonl` receipts vs. `chains/SIGRUN_P4.jsonl` rows) with no observed sync between them this session.

**Conclusion for Check 4:** no row has been written-by-one-substrate-and-read-by-another. Cross-substrate coordination via this chain is currently theoretical, not demonstrated.

## Check 5 — Silent-drop rate

`list_sessions` (50-row cap, most-recent-first) shows this GUNNR probe is one of **5 sessions dispatched together** at 2026-08-01T13:34:01Z, all `cwd: hfo_gen_133_forge`, all `isRunning: true` at check time:

| Session | Title | Chain rows landed | Inbox receipts landed |
|---|---|---|---|
| local_b4579cd1 | Sigrún opus5 REHYDRATED (parent) | 0 | 0 |
| Thrud sonnet5 | Throughput probe | 0 | 1 (`inbox/olrun/20260801T133404Z_thrud_…`) |
| Rota sonnet5 | Adversarial red-team probe | 0 | 0 (not yet checked complete) |
| Hrist sonnet5 | Heritage probe | 0 | 0 (not yet checked complete) |
| Reginleif sonnet5 | Substrate readiness probe | 0 | 0 (not yet checked complete) |
| GUNNR (this probe) | Coordination surface audit | pending (this row, being written now) | pending |

**Honest limitation:** these sessions are still in-flight at the time of this check (mid-wave); a true silent-drop ratio requires waiting for all 5 to terminate, which this probe's own instructions (no polling, 30-min timebox) do not permit. The only clean data point right now: 1 of 5 has produced *any* artifact so far (Thrud, via `inbox/olrun/`, not via the chain), 0 of 5 have produced a chain row. This is a floor, not a final count.

For historical context beyond this wave, Thrud's own probe (`probes/throughput_24h_20260801.md`) already flagged the identical limitation for the ~40-session, 24h window: `list_sessions` gives no per-session artifact attribution, so a real silent-drop ratio needs `list_events`/`search_session_transcripts` opened per-session — explicitly out of scope for a 30-min timeboxed probe. I did not duplicate that broader sweep; deferring to Thrud's finding rather than re-deriving it.

---

## Verdict

**"Chain rows exist as coordination substrate": PARTIAL.**

What's real:
- The hash-chain math for rows 10–37 is genuine and self-verifying (28/37 rows, 0 link breaks in that span).
- `inbox/olrun/` is being actively used this session by a sibling probe as a lightweight file-drop coordination point.

What's missing to make this a YES:
1. **A canonical writer.** `bb_append.py` is spec'd but unported — nothing currently prevents a new carrier from inventing an 11th row schema or another unhashed row like rows 3–9.
2. **A true, unbroken root.** Row 10's `prev_sha256: null` needs to be corrected to point at row 9's content (or rows 1–9 need to be explicitly marked out-of-chain/deprecated) before any external verifier could trust the chain's start.
3. **Sealing.** 0/37 rows carry an HMAC; anyone with file access can rewrite history undetected. This is flagged consistently by the forge's own doctrine, not a new gap.
4. **A merge point between `inbox/*` and `chains/*`.** Right now they are two write surfaces that don't sync — a receipt in `inbox/olrun/` is invisible to anything that only reads the chain, and vice versa.
5. **Actual non-Claude-substrate participation.** Every actor that has ever written a row is Claude Code. Codex/ChatGPT/Antigravity/$0-mesh substrates are discussed in prose but have never appended a verifiable row. Until one does, "cross-substrate coordination surface" is a design intent, not a demonstrated property.

## Honest flaw

This audit itself has no HMAC and was written by the same substrate class (Claude Code) it is auditing — it cannot rule out that I share blind spots with the rows I'm grading. I did not exhaustively grep every `state/ssot/*.jsonl` file for cross-substrate authorship (sampled `lane_returns.jsonl` only, given the 30-min timebox); a more thorough sweep could surface a counter-example I missed. The silent-drop-rate check (5) is admittedly incomplete — the wave was still running when I checked, so "0/5 chain rows" is a snapshot, not a settled outcome.

## Next safe action

Operator or a non-authoring verifier: (a) decide whether rows 1–9 should be retroactively hashed/linked or explicitly marked deprecated-prefix; (b) port `bb_append.py` from gen-130 if a single canonical writer is wanted before more carriers add more schemas; (c) decide whether `inbox/olrun/` receipts should mirror into `chains/SIGRUN_P4.jsonl` or whether the two are intentionally separate tiers (fast local receipt vs. slow verified chain).
