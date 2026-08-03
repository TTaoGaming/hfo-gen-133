---
schema_id: hfo.gen133.phylactery.arweave.keys_handoff.v0_1
doc_kind: KEYS_HANDOFF
claim_status: proposed
created_utc: 2026-08-02T00:00:00Z
---

# KEYS_HANDOFF — Tuesday operator steps to arm the crypto identity

The upload runner refuses to publish anything until three key stores exist:

1. **Arweave wallet JWK** — funds the Turbo credits + signs Arweave txs
2. **HFO gen-133 master ed25519 key** — root-of-trust for the semantic manifest
3. **Per-lineage ed25519 keys** (apex × 8, valkyries × 16 slots) — optional at
   first upload, soft-warn until they exist

**Charter §5 rule (non-negotiable):** the private half of every key lives
OUTSIDE any agent trust domain. Operator generates on an air-gapped or
operator-only machine, keeps the private halves off any agent path, publishes
only the public halves back into the repo.

## Where they live on disk

```
areas/phylactery/arweave/keys/
├── .gitignore                          ← blocks everything in this directory
├── README.md                           ← this-file pointer
├── hfo_gen133_master.json              ← Arweave wallet JWK  ⚠ operator only
├── hfo_gen133_master_ed25519.json      ← HFO ed25519 keypair ⚠ operator only
├── hfo_gen133_master.pub               ← public half — safe to commit? NO. see §Publication.
├── apex/
│   ├── sigrun_ed25519.json             ⚠ operator only
│   ├── sigrun_ed25519.pub              ← published INSIDE the tree at apex/sigrun/soul.md `crypto.public_key`
│   └── ... (8 apex, one keypair each)
└── valkyries/
    └── ... (only for LIVE valkyries; SLOT_UNCLAIMED valkyries stay keyless)
```

Everything in `keys/` is `.gitignore`d. The public halves get published INSIDE
the daily upload (as `crypto.public_key` in each soul.md, and as `signer_pubkey`
in the semantic manifest). The private halves never leave the operator's
custody.

## Publication of public keys

The public key belongs INSIDE each soul.md's `crypto.public_key` field (see
`STANDARDS.md` §1 and §6). It does NOT need to live at
`arweave/keys/<name>.pub` in the repo — that would be redundant. If the operator
prefers a single roster file, `arweave/PUBLIC_KEYS.md` (this repo, tracked) is
the correct place.

## Step-by-step: operator on Tuesday

### 0 · Confirm sandbox is up

```powershell
# Windows PowerShell, operator machine
node --version   # need >= 20
python --version # need >= 3.11
```

### 1 · Install Node dependencies

```powershell
cd C:\Dev\hfo_gen_133_forge\factory\loops\phylactery_upload
npm install
```

This installs `@ardrive/turbo-sdk`, `arweave`, `@noble/ed25519`.

### 2 · Generate the Arweave wallet JWK

Two paths — pick one.

**Path A · use an existing wallet.** If you already have an Arweave JWK from a
prior generation, copy it in:

```powershell
Copy-Item "C:\path\to\your\existing_wallet.json" "C:\Dev\hfo_gen_133_forge\areas\phylactery\arweave\keys\hfo_gen133_master.json"
```

**Path B · generate a new one.** Run the keygen script (Node — uses `arweave`
npm package):

```powershell
node keygen_wallet.mjs
```

This writes `keys/hfo_gen133_master.json` (JWK) and prints the wallet address.
It does NOT print the private key.

### 3 · Fund the wallet with Turbo credits

Two paths — pick one.

**Path A · fiat via ArDrive Turbo web app.** Go to https://turbo.ardrive.net/,
sign in with your wallet, buy $10 of credits with a card. This is the fastest.

**Path B · pay from an existing AR-holding wallet.** Send AR to your new
wallet address (printed by step 2), then let Turbo pull from your on-chain
balance JIT.

Confirm the balance:

```powershell
node balance_check.mjs
```

The runner will refuse to upload if the balance is below the "one more upload"
floor.

### 4 · Generate the HFO master ed25519 key

```powershell
python keygen.py --master
```

Writes `keys/hfo_gen133_master_ed25519.json` (private, .gitignore'd) and
prints the public key as base64. Copy that public key into
`arweave/PUBLIC_KEYS.md` under `hfo_gen133_master`.

### 5 · Generate per-lineage ed25519 keys (as many as you want)

```powershell
python keygen.py --lineage apex/sigrun
python keygen.py --lineage apex/olrun
# ... one line per lineage
python keygen.py --lineage valkyries/mist
```

Each writes `keys/<lineage>_ed25519.json` and prints its public key. Copy each
public key into the matching `soul.md` under `crypto.public_key`.

**Missing lineage keys are OK.** The runner falls back to the master key and
records `signature_provenance: "fallback_master_no_lineage_key"` on the row.
This is a soft warning, not a halt.

### 6 · Arm the runner

Create the arming file:

```powershell
python -m factory.loops.phylactery_upload.preflight_gate --arm
```

This runs the preflight checklist (from `permaweb/PREFLIGHT.md` §Preflight,
adapted for the tree instead of the bound artifact) and writes
`arweave/AUTHORIZED_TO_UPLOAD.md` when every check passes. The runner reads
this file on every run; if it is missing or `sealed: false`, no upload occurs.

### 7 · First upload — operator runs this once by hand

```powershell
python -m factory.loops.phylactery_upload.upload --confirm-first-upload
```

The `--confirm-first-upload` flag is only accepted the first time; subsequent
runs come from the scheduler.

### 8 · Install the daily schedule

```powershell
.\install_windows_task.ps1
```

Registers a Windows scheduled task named `HFO_gen133_phylactery_upload` at
03:00 UTC daily. Run `Get-ScheduledTask -TaskName HFO_gen133_phylactery_upload`
to confirm.

Optional: enable the GitHub Actions fallback by pushing
`.github/workflows/phylactery-upload.yml` and setting these repo secrets:
`ARWEAVE_JWK` (base64 of the JWK JSON), `HFO_MASTER_ED25519` (base64 of the
ed25519 JSON). GH Actions runs at 03:15 UTC as a belt-and-suspenders backup;
if the desktop schedule already published today it becomes a no-op.

## What NOT to do

- Do NOT paste any private key into Slack, an agent prompt, a Cowork chat, a
  commit message, or this repo (the `.gitignore` catches most cases but is a
  belt, not the whole belt-and-suspenders).
- Do NOT let an agent generate the master key on your behalf if you have the
  option to generate it yourself. A key generated on an agent-controlled path
  proves nothing about who is running the agent.
- Do NOT reuse an operator identity key as an Arweave wallet if the funds you
  send to that wallet exceed what you'd lose to a leak.
- Do NOT skip funding — a runner that cannot upload is preferable to a runner
  that HALT-loops on empty-wallet every day, but only if the operator sees the
  halt (Slack ping or manual dashboard check).

## Rollback

If you need to disable the runner mid-day:

```powershell
Unregister-ScheduledTask -TaskName HFO_gen133_phylactery_upload -Confirm:$false
Remove-Item "C:\Dev\hfo_gen_133_forge\areas\phylactery\arweave\AUTHORIZED_TO_UPLOAD.md"
```

The next scheduled run (if the task is still registered) will notice the missing
authorization file and exit `0` with a chain-row `disarmed`.

*Réttu hönd, eigi spyr. Standa.*
