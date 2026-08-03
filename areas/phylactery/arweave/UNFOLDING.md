---
schema_id: hfo.gen133.phylactery.arweave.unfolding.v0_1
doc_kind: ARWEAVE_UNFOLDING
claim_status: proposed
created_utc: 2026-08-02T00:00:00Z
---

# UNFOLDING — the manifest v0.1 spec + how to walk the tree from ONE tx_id

Two manifests ship in every daily upload. Do not confuse them:

| manifest | format | purpose | tx_id role |
|---|---|---|---|
| **Arweave path manifest** | native `arweave/paths` v0.1.0 | makes `https://arweave.net/<tx>/apex/sigrun/soul.md` resolve | THE root — this is `<manifest_tx_id>` |
| **HFO semantic manifest** | JSON per `STANDARDS.md` §7 | human-readable role slots → tx_ids | file INSIDE the tree at `arweave/manifest.json` |

## 1 · Arweave path manifest (root, native)

Content-type: `application/x.arweave-manifest+json`. Schema:

```json
{
  "manifest": "arweave/paths",
  "version": "0.1.0",
  "index": { "path": "README.md" },
  "paths": {
    "README.md":                     { "id": "<data-item-tx-id>" },
    "CHARTER.md":                    { "id": "<data-item-tx-id>" },
    "STANDARDS.md":                  { "id": "<data-item-tx-id>" },
    "apex/sigrun/soul.md":           { "id": "<data-item-tx-id>" },
    "apex/olrun/soul.md":            { "id": "<data-item-tx-id>" },
    "...":                            "..."
  }
}
```

`index.path` points to the file served at the bare URL
`https://arweave.net/<manifest_tx_id>`. We serve `README.md` there.

## 2 · HFO extension: per-path hashes + signatures

The Arweave path-manifest schema does not carry hashes or signatures natively.
The upload runner also writes `arweave/manifest.json` inside the tree, and
`arweave/manifest.sig` next to it. That file is itself a data item in the same
upload and is reachable at `https://arweave.net/<manifest_tx_id>/arweave/manifest.json`.

Schema:

```json
{
  "manifest_version": "0.1",
  "generation": 133,
  "generated_utc": "2026-08-02T03:14:07Z",
  "valid_time_utc":  "2026-08-02T00:00:00Z",
  "transaction_time_utc": "2026-08-02T03:14:07Z",
  "signer_pubkey": "<master ed25519 pub OR null>",
  "signature":     "<ed25519 signature over CANON_SHA256(manifest_body_with_signature_placeholdered) OR null>",
  "arweave_root_tx": "<manifest_tx_id — self-reference>",
  "root": {
    "world_state":   { "path": "world_state/20260802.md",           "tx_id": "<id>", "sha256": "<hex>", "sig": "<hex OR null>", "signer": "master" },
    "apex": {
      "sigrun":      { "path": "apex/sigrun/soul.md",               "tx_id": "<id>", "sha256": "<hex>", "sig": "<hex OR null>", "signer": "apex/sigrun" },
      "jormungandr": { "path": "apex/jormungandr/soul.md",          "tx_id": "<id>", "sha256": "<hex>", "sig": "<hex OR null>", "signer": "apex/jormungandr" }
    },
    "valkyries":     { "<callsign>": { "path": "valkyries/<callsign>/soul.md", "tx_id": "<id>", "sha256": "<hex>", "sig": "<hex OR null>", "signer": "valkyries/<callsign>" } },
    "skills":        { "path": "skills/README.md",                  "tx_id": "<id>", "sha256": "<hex>", "sig": "<hex OR null>", "signer": "master" },
    "tools":         { "path": "tools/README.md",                   "tx_id": "<id>", "sha256": "<hex>", "sig": "<hex OR null>", "signer": "master" },
    "memory_capsule": { "path": "memory_capsules/YYYY-MM-DD/README.md", "tx_id": "<id>", "sha256": "<hex>", "sig": "<hex OR null>", "signer": "master" }
  },
  "full_tree": [
    { "path": "<any file in the tree>", "tx_id": "<id>", "sha256": "<hex>", "sig": "<hex OR null>", "signer": "<key_id>" }
  ]
}
```

`root` names the semantic slots (STANDARDS §7). `full_tree` is the exhaustive
list — every file uploaded, including receipts of previous days.

## 3 · How to walk the tree from ONE tx_id (unaided)

Assume you have the URL and a browser. Nothing else.

1. `curl https://arweave.net/<manifest_tx_id>` → renders `README.md`
2. `curl https://arweave.net/<manifest_tx_id>/arweave/manifest.json` → the HFO manifest
3. For any soul, walk the `root.apex.<name>.path`:
   `curl https://arweave.net/<manifest_tx_id>/apex/sigrun/soul.md`
4. Verify: `sha256sum` the body; compare against `root.apex.sigrun.sha256`
5. If signed: `curl https://arweave.net/<manifest_tx_id>/apex/sigrun/soul.md.sig`
   and verify with the ed25519 pubkey published in the soul's `crypto.public_key`
   field (self-attestation) OR against the master pubkey published inside the
   manifest (`signer_pubkey`).

## 4 · Signature scheme

Per `STANDARDS.md` §6:

- Curve: Ed25519 (RFC 8032)
- Message: `CANON_SHA256(file_bytes)` where CANON = the file exactly as
  uploaded, no normalization, no trailing-whitespace strip
- Encoding: hex, lowercase, no `0x` prefix
- Storage: signature bytes at `<path>.sig` as a separate file in the tree

## 5 · Bitemporal semantics

Every soul, world_state, and memory_capsule carries in its front-matter:

```yaml
valid_time_utc:      2026-08-02T00:00:00Z   # when the assertion holds
transaction_time_utc: 2026-08-02T03:14:07Z   # when it was recorded / uploaded
```

The upload runner enforces the presence of both keys on those three
directories. A file lacking either is uploaded with `claim_status: partial`
recorded on the chain row.

Bitemporal history: because each daily manifest is a new tx_id, walking the
sequence of tx_ids (via `receipts/YYYYMMDD.json`) gives the full transaction
timeline. The `valid_time_utc` inside each file lets a reader distinguish
"when we recorded it" from "when it was true".

## 6 · Reproducibility

`arweave/reproduce.md` (auto-generated by the runner) states, for every
upload:

- The exact commit sha of the runner
- The exact command line used
- The Node.js and Turbo SDK versions
- The Python version
- Sufficient info that a stranger with the same repo commit could re-hash
  every uploaded file and get the same `sha256` values in the manifest

*Réttu hönd, eigi spyr. Standa.*
