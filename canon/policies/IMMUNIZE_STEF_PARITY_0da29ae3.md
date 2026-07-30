# IMMUNIZED POLICY — stef parity anchor + canonicalization rule

```yaml
schema_id: hfo.gen133.policy.stef_parity.v1_0
policy_id: POL-GEN133-STEF-PARITY-001
status: IMMUNIZED
immunized_by: operator (OBSIDIAN_SPIDER / TTao)
immunize_authorization_utc: 2026-07-30T06:20:00Z
immunize_authorization_verbatim: >-
  "THREE OPERATOR APPROVALS GRANTED — you are now authorized: 1. IMMUNIZE 0da29ae3.
  Write the canonicalization rule to the appropriate policy file … Append the
  immunization row to the canonical chain with claim_ceiling:
  operator_approved_immunize_0da29ae3_canonicalization_rule"
claim_ceiling: operator_approved_immunize_0da29ae3_canonicalization_rule
recorded_by: SIGRUN_P4 apex compose lane · claude-opus-5
valid_time_utc: 2026-07-30T06:40:00Z
chain_row: chains/SIGRUN_P4.jsonl (genesis row, class=immunize)
```

## 1 · The policy

**The stef parity anchor for gen-133 and forward is:**

```
0da29ae3b34894b8fe88698f71476d24ff1fb3ee78d9fc8f5dcefc2fd1e83bc4
```

**The canonicalization rule that produces it (NORMATIVE):**

```
Input:  the four stef lines of the SIGRÚNAR DRÁPA, as they appear in the
        Arweave-anchored sigrun_lineage_lifeboat, row 3.
Steps:  1. strip leading/trailing whitespace from EACH line
        2. join the lines with LF ("\n")
        3. normalize to Unicode NFC
        4. encode UTF-8
        5. NO trailing newline
        6. sha256, lowercase hex
```

Any tool, hook, beacon, or document asserting a stef parity value MUST state which
rule it used. **A parity hash without its canonicalization rule is not a parity
hash** — that is precisely how the legacy anchor drifted undetected for five
generations.

## 2 · The legacy anchor is retired, NOT deleted

```
fb07f523c8af70a19d7ee18759f273c6113b03168eede1b030d7b9b08e2ddc24
  status: LEGACY_UNREPRODUCIBLE
```

**Do not delete it.** It carries five generations of provenance across four repos
(gen-130 `DRAPA_SPEC`, gen-128 `stef_sha8`, gen-124 `append_compose_chain.py`,
`SIGRUN_PERMA_INDEX`, the moba-qwe wake skill). Deleting it would erase the
evidence that the drift happened. Supersede, never delete (floor F4).

Refutation record: **9 canonicalizations** were attempted against the four stef
lines from the anchored lifeboat, plus the full drápa document, plus the
`DRAPA_SPEC` rendering, across every EOL and whitespace variant. **NONE MATCH.**

## 3 · Provenance of the replacement

| fact | value | evidence class |
|---|---|---|
| derived from | `sigrun_lineage_lifeboat` row 3 | INHERITED |
| Arweave txid | `w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M` | INHERITED |
| lifeboat sha256 | `d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0` | INHERITED |
| lifeboat size / rows | 23,507 B / 64 rows | INHERITED |
| agreement | Arweave + GitHub lifeboat repo + published `SHA256SUMS_v0_8_0.txt` — **one source outside operator control** | INHERITED |
| first independent reproduction | predecessor Sigrún code lane, 2026-07-30T05:10:40Z, lane_returns row `78adc3a443139636…` | INHERITED |

## 4 · ⚠️ Honest flaw — read before citing this policy

**This lane did NOT re-derive `0da29ae3` first-hand.** It is recorded here on:

1. the operator's explicit IMMUNIZE authorization (§frontmatter), and
2. the predecessor lane's first-hand reproduction receipt.

Under norm **L3** (count nothing from memory) and **L4** (hashes prove content,
never authorship), that makes the *derivation* **INHERITED**, while the *policy
status* is genuinely IMMUNIZED — the operator's authorization is the thing that
makes it canon, and that authorization is first-hand and verbatim.

**The distinction matters and is not pedantry:** the operator's approval settles
*which value is canonical*. It does not, and cannot, constitute an independent
reproduction of the digest. So exactly **one** independent reproduction exists,
by a same-family lane. A second, cross-provider reproduction remains open work.

**Next safe action:** have a non-Claude verifier (Sol / GPT-5.6, or Codex) fetch
the Arweave lifeboat, apply §1 verbatim to row 3, and return the digest it
computes. If it returns `0da29ae3…`, the policy moves from IMMUNIZED-on-authority
to IMMUNIZED-with-independent-cross-provider-receipt. If it returns anything else,
**this policy is wrong and must be reopened** — and that outcome is exactly what
makes the check worth running.

## 5 · Enforcement gaps to close

| gap | where | state |
|---|---|---|
| gen-130 SessionStart beacon still emits `fb07f523` | `hfo_gen_130_forge` hook | ⛔ **OPEN** — not edited by this lane (out-of-scope forge; would need its own change) |
| no gate asserts the rule | `.github/workflows/spec-digest.yml` | ⏳ workflow authored, never run |
| no executable implementation of §1 | — | ⛔ open |

*Truthful-red > false-green.*
