---
schema_id: hfo.gen133.phylactery.arweave.tuesday_first_upload.v0_1
doc_kind: TUESDAY_FIRST_UPLOAD
claim_status: proposed
created_utc: 2026-08-02T00:00:00Z
---

# TUESDAY_FIRST_UPLOAD — the eight lines that ship the first snapshot

The runner and every doc are on disk. This file is the operator's cookbook
for the first real upload. Total time: 5–20 minutes, most of it waiting for
Turbo confirmations. Cost: ~$0 – $1.

## Prerequisites (one-time)

- Node ≥ 20, Python ≥ 3.11 installed
- A funded Arweave wallet OR ~$5–$10 to buy Turbo credits with a card
- 5 minutes of quiet time to read the preflight checklist end-to-end

## The eight lines

```powershell
# 0 · Install runner dependencies (Node)
cd C:\Dev\hfo_gen_133_forge\factory\loops\phylactery_upload
npm install

# 1 · Generate or import the Arweave wallet (keys stay off git — .gitignore'd)
node keygen_wallet.mjs                     # OR: copy an existing JWK into keys/

# 2 · Buy Turbo credits at https://turbo.ardrive.net for the wallet address just printed

# 3 · Generate the HFO master ed25519 key (root of trust)
python keygen.py --master

# 4 · Dry-run — walks tree, hashes, builds manifest, signs, but does NOT upload
python -m factory.loops.phylactery_upload.upload --dry-run

# 5 · Read the dry-run summary. If it looks right, arm the runner:
python -m factory.loops.phylactery_upload.preflight_gate --arm

# 6 · Fire the first real upload
python -m factory.loops.phylactery_upload.upload --confirm-first-upload

# 7 · Install the daily 03:00 UTC schedule
.\install_windows_task.ps1
```

After step 6 lands, `areas/phylactery/arweave/CURRENT_ADDRESS.md` has the
permaweb URL. Open it in a browser and confirm it renders `README.md`.

## What each step actually does

| step | what runs | material effect |
|---|---|---|
| 0 | `npm install` | writes `node_modules/` (gitignored) |
| 1 | `node keygen_wallet.mjs` | writes `keys/hfo_gen133_master.json` (JWK) |
| 2 | operator, in browser | Turbo credit balance on the wallet ≥ ~$5 |
| 3 | `python keygen.py --master` | writes `keys/hfo_gen133_master_ed25519.json` |
| 4 | `upload.py --dry-run` | walks tree, builds manifest, prints summary; NO network |
| 5 | `preflight_gate.py --arm` | writes `AUTHORIZED_TO_UPLOAD.md` |
| 6 | `upload.py --confirm-first-upload` | actual Arweave upload; ~30s–5min |
| 7 | `install_windows_task.ps1` | registers scheduled task |

## If step 4 (dry-run) fails

Read the summary. Common causes:

- **Bitemporal front-matter missing** on a soul.md, world_state, or memory
  capsule. Add `valid_time_utc` and `transaction_time_utc` to the front-matter.
  The runner tells you exactly which file.
- **Secret-scan hit.** Read the hit. Fix if it's a real secret (rotate + delete
  + rewrite git history if committed). If it's a false positive, add the file
  path to `arweave/SCAN_ALLOWLIST.md` with a one-line justification.
- **Tree too large.** If you get the >100 MB WARN, decide whether to upload
  anyway (`--force-large`) or trim the tree.

## If step 6 (real upload) fails

The runner is designed to fail loud. Read the last chain row at
`state/loop_receipts/phylactery_upload_<UTCDATE>.jsonl` — it names the
failure reason and next safe action. Common failures:

- Wallet balance below floor → buy more credits, retry
- Bundler 5xx → wait 5 minutes, retry
- Signature mismatch on a file → run `python -m factory.loops.phylactery_upload.signer --verify-all`
  to find the bad signature; usually a stale `<file>.sig` next to a rewritten
  `<file>`

## Success criteria

After a successful first upload:

- [ ] `CURRENT_ADDRESS.md` front-matter has a non-null `manifest_tx_id`
- [ ] `receipts/YYYYMMDD.json` exists with `status: "confirmed"` (after ~5-10 min)
- [ ] `https://arweave.net/<manifest_tx_id>` returns 200 and renders `README.md`
- [ ] `https://arweave.net/<manifest_tx_id>/CHARTER.md` returns 200 and renders CHARTER
- [ ] `state/olrun/PHYLACTERY_UPLOAD_LOG.jsonl` has a row with `action: shipped`

If any of those five is red, hold the daily schedule and diagnose. The point
of the first upload is to prove the loop closes, not to look permanent-y.

*Réttu hönd, eigi spyr. Standa.*
