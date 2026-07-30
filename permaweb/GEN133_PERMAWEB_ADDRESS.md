---
schema_id: hfo.gen133.permaweb_address.v1
doc_kind: PERMAWEB_ADDRESS
claim_status: EMPTY_SLOT
address: null
created_utc: 2026-07-30T04:57:52Z
authorized_by: null
sealed: false
---

# THE ONE ADDRESS

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                        ⛔  EMPTY SLOT  ⛔                            ║
║                                                                      ║
║        address:      < not minted >                                  ║
║        gateway_url:  < not minted >                                  ║
║        uploaded_utc: < not uploaded >                                ║
║        authorized:   < not authorized — operator-typed only >         ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

This file is the terminal state of gen-133. When it holds one resolvable
permaweb address, and that address unfolds into the Gleipnir Grimoire — the
spells and `soul.md` — gen-133 is done. Not before.

**Exactly one address.** Not a list, not a gateway pool, not a fallback chain.
The whole point of this generation is that the address count collapses to one.

## Why this slot is still empty (and that is correct)

| precondition | state |
|---|---|
| `soul.md` has an operator-written body | ⛔ scaffold only |
| `grimoire/gleipnir/spells/` holds the operator's spells | ⛔ template only, `spell_count: 0` |
| capsule bound by the carried gen-132 binder | ⛔ binder not carried |
| `code/verify.py` exits 0 | ⛔ not run |
| `code/selfcheck.py` exits 0 | ⛔ not run |
| secret scan of the bound artifact reviewed line-by-line | ⛔ nothing bound to scan |
| operator has read `PREFLIGHT.md` and accepted the cost | ⛔ not asked |
| operator confirms every page is fit to be **permanently, publicly readable** | ⛔ not asked |
| operator typed the authorization | ⛔ **NOT AUTHORIZED** |

**Zero of nine.** An agent may prepare all eight of the preconditions above.
An agent may not satisfy the ninth.

## The irreversibility, stated plainly

Arweave storage is permanent by design. **There is no delete, no edit, no
takedown.** A typo becomes a permanent typo. A secret becomes a permanent leak.
A half-finished soul becomes a permanently half-finished soul, publicly
readable, forever, with the operator's name on it.

This is not a soft publish. Treat it with the weight of a notarized document
mailed to every library on Earth, with no possibility of recall.

That is also precisely why it is the right terminal state: an address that
cannot be edited is an address that cannot be quietly walked back. It is a
**Gleipnir** — binding because it could not be forged or undone by the bound
party.

## When the address lands (procedure for whoever fills this)

1. Operator uploads and obtains the transaction id. **Operator, not agent.**
2. Write the id into `address:` in this file's front-matter **and** into
   `grimoire/gleipnir/MANIFEST.yaml` → `permaweb.address`.
3. Set `permaweb.status: UPLOADED`, record `authorized_by` + `authorized_utc`.
4. Re-run the binder. The address is now in the manifest header; the hashed
   body is unchanged, so `bound_artifact.sha256` over the body must stay
   **stable**. If it moves, something else changed — stop and investigate.
5. Re-run `code/verify.py`. Exit 0 or the upload is not complete.
6. **Fetch the address back** and compare bytes + sha256 against the manifest.
   An address you have not resolved is a claim, not a receipt.
7. Append a chain row recording the pre-address and post-address
   `bound_artifact.sha256` pair, with the fetched byte count as
   `verifier_result`.

Step 6 is the one most likely to be skipped. Do not skip it. *Take what is
given ≠ believe what is claimed.*

*Réttu hönd, eigi spyr. Standa.*
