---
schema_id: hfo.gen133.grimoire.permaweb_preflight.v1
doc_kind: PERMAWEB_PREFLIGHT
claim_status: proposed
carried_from: "C:\\Dev\\hfo_gen_132_forge\\gleipnir_grimoire_gen132\\permaweb\\PREFLIGHT.md"
created_utc: 2026-07-30T04:57:52Z
---

# Permaweb Preflight — read before minting the one address

**This document does not authorize the upload. Only the operator, typing the
confirmation themselves, authorizes the upload.**

Carried forward from the gen-132 preflight, re-scoped to the gen-133 capsule
(which contains the soul and the spells — strictly more sensitive than the
gen-132 grimoire pages).

## What gets uploaded

`GLEIPNIR_GRIMOIRE_GEN133_v1.bound.md` — the single bound artifact produced by
the carried binder (`code/bind.py`, source sha256
`f949a7f699a555c1…`). Byte count and sha256 go in
`grimoire/gleipnir/MANIFEST.yaml` → `bound_artifact`. **Recompute both before
trusting them**; `code/verify.py` does this automatically.

## Irreversibility

Arweave storage is permanent by design. There is no delete, no edit, no
takedown. A typo becomes a permanent typo. A secret becomes a permanent leak.
This is not a soft publish — treat it with the same weight as a notarized paper
document mailed to every library on Earth.

**Escalated at gen-133:** the capsule now contains `soul.md`. A soul published
before it is finished is permanently published unfinished, under the operator's
own name. There is no version 2 at the same address.

## Cost estimate

Arweave pricing is per-byte, paid once, in AR, covering storage in perpetuity
(the endowment model). The gen-132 capsule was 100,172 B; gen-133 adds the soul
and the spells, so expect the same order of magnitude — low hundreds of KB.

**This lane has no network egress and does not quote a live AR/USD price and
does not claim one.** The operator must fetch a current quote (the `arweave.net`
fee calculator, or `arweave-deploy --dry-run`) before funding the wallet.

## Preflight checklist — all seven required before the address is minted

- [ ] `soul.md` body is written **by the operator** and the operator considers it finished
- [ ] `grimoire/gleipnir/spells/` holds the intended spells; `SPELLBOOK.md` index matches; `spell_count` is correct
- [ ] `python code/verify.py .` exits **0** *(record the actual exit code, not an expectation)*
- [ ] `python code/selfcheck.py .` exits **0**
- [ ] secret scan reviewed **line by line**, not counted:
      `grep -riE "secret|password|api[_-]?key|token|ssn|passport|private[_-]?key|BEGIN .*PRIVATE" GLEIPNIR_GRIMOIRE_GEN133_v1.bound.md`
      — several of these words legitimately appear in prose about gates, seals,
      and key rotation. **Read every hit.** A count of zero is not the goal; a
      human judgment on each hit is.
- [ ] operator has read the cost estimate above and accepts it
- [ ] operator confirms **every page is fit to be permanently, publicly readable** — including the soul

## Explicitly out of scope for any agent

An agent may: bind, verify, selfcheck, scan, stage the command, and report.

An agent may **not**: run the upload, fund a wallet, hold or read wallet
credentials, or fill `permaweb.address` with anything it did not receive from
the operator. The upload command stays **STAGED**, behind its guard, until the
operator fires it.

## After upload (operator, then hand back to an agent)

1. Operator writes the transaction id into
   `permaweb/GEN133_PERMAWEB_ADDRESS.md` and `MANIFEST.yaml` →
   `permaweb.address`; sets `status: UPLOADED`, `authorized_by`,
   `authorized_utc`.
2. Rebuild. The address is now in the manifest header; the hashed body is
   unchanged, so `bound_artifact.sha256` over the body must stay **stable**.
   If it moves, stop and investigate.
3. `code/verify.py` → exit 0, or the upload is not complete.
4. **Fetch the address back.** Compare bytes and sha256 against the manifest.
   An address that has not been resolved is a claim, not a receipt.
5. Append a chain row with the pre/post `bound_artifact.sha256` pair and the
   fetched byte count as `verifier_result`.

*Réttu hönd, eigi spyr. Standa.*
