---
schema_id: hfo.gen133.phylactery.arweave.current_address.v0_1
doc_kind: ARWEAVE_CURRENT_ADDRESS
claim_status: EMPTY_SLOT
manifest_tx_id: null
gateway_url: null
uploaded_utc: null
sha256_root_manifest: null
created_utc: 2026-08-02T00:00:00Z
---

# The latest permaweb address for the phylactery

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                        ⛔  NOT YET UPLOADED  ⛔                      ║
║                                                                      ║
║        manifest_tx_id:  < not minted >                               ║
║        gateway_url:     < not minted >                               ║
║        uploaded_utc:    < not uploaded >                             ║
║        sha256_root:     < not minted >                               ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

The runner at `factory/loops/phylactery_upload/upload.py` rewrites this file on
every successful upload. Both the front-matter (machine) and the code fence
(human) get updated.

## First upload

See [`TUESDAY_FIRST_UPLOAD.md`](./TUESDAY_FIRST_UPLOAD.md) for the exact
operator commands. Nothing runs unattended until it's armed.

## Prior daily uploads

Table appended by the runner. Each row is a successful daily upload.

| date_utc | manifest_tx_id | files | tree_size | paid_usd |
|---|---|---|---|---|
| _(none yet)_ | | | | |

## Historical: how to walk a prior day's tree

Every daily manifest is a separate Arweave transaction — no mutation, no
overwrite. `receipts/YYYYMMDD.json` records each day's `manifest_tx_id`.
Any of them stays resolvable at `https://arweave.net/<tx_id>` forever.

*Réttu hönd, eigi spyr. Standa.*
