# LOOP · PHYLACTERY_UPLOAD — SPEC

```yaml
AIH2O:
  version: gen-133
  loop: phylactery_upload
  role: executor
  actor: factory_loop
  verifier: root manifest tx_id returns 200 on gateway + 3 sample nested paths return 200 + all signatures verify against stored pubkeys
  clock_source: host_read
  chain: state/loop_receipts/phylactery_upload_<UTCDATE>.jsonl
  olrun_log: state/olrun/PHYLACTERY_UPLOAD_LOG.jsonl
  artifact_root: areas/phylactery/
  receipts: areas/phylactery/arweave/receipts/
```

## Purpose

Take a daily snapshot of `areas/phylactery/`, sign each file with its owning
lineage key (or master), and publish the tree as ONE Arweave transaction that
unfolds via native `arweave/paths` v0.1 path manifest. Anyone with the resulting
tx_id can walk the tree in a browser (`https://arweave.net/<tx>/apex/sigrun/soul.md`).

## Inputs

- The tree at `areas/phylactery/` — walked live
- Keys at `areas/phylactery/arweave/keys/` — never uploaded, .gitignore'd
- Arming file at `areas/phylactery/arweave/AUTHORIZED_TO_UPLOAD.md` —
  operator-created by `preflight_gate.py --arm`
- Optional allowlist at `areas/phylactery/arweave/SCAN_ALLOWLIST.md` for
  documented secret-scan false positives

## Outputs

1. **Arweave path manifest tx** — the root `manifest_tx_id`, resolves at
   `https://arweave.net/<tx>`
2. **Per-file data-item tx_ids** — each uploaded file has its own tx_id, all
   referenced by the root path manifest
3. `areas/phylactery/arweave/receipts/YYYYMMDD.json` — daily upload summary
4. `areas/phylactery/arweave/receipts/YYYYMMDD.jsonl` — one row per file
5. `areas/phylactery/arweave/CURRENT_ADDRESS.md` — updated with the new URL
6. `state/loop_receipts/phylactery_upload_<UTCDATE>.jsonl` — chain rows
7. `state/olrun/PHYLACTERY_UPLOAD_LOG.jsonl` — Olrún log per Charter §8

## CLI

```
# dry-run (walks tree, hashes, builds manifest, prints summary; NO network)
python -m factory.loops.phylactery_upload.upload --dry-run

# first real upload (operator by hand; guard flag)
python -m factory.loops.phylactery_upload.upload --confirm-first-upload

# subsequent daily runs (scheduler)
python -m factory.loops.phylactery_upload.upload
```

## Kill conditions

| condition | action | note |
|---|---|---|
| Wallet balance < 0.01 AR OR Turbo credit < 3× last upload cost | HALT + Slack escalate | operator refills |
| Bundler 5xx after 3 exponential retries (1s, 2s, 4s) | HALT + Slack escalate | fail loud |
| Any signature mismatch on any file | HALT | integrity gate; never partial |
| Any secret_scan hit not in SCAN_ALLOWLIST | HALT | permanent leak prevention |
| Tree size > 100 MB | WARN, require `--force-large` | safety |
| 3 consecutive uploads with 0-byte delta | WARN, still uploads | signal-of-signal |
| `AUTHORIZED_TO_UPLOAD.md` missing or `sealed: false` | exit 0 with `disarmed_no_upload` | not a halt; a disarm |

## Cadence

- Recurring: Windows Task Scheduler, daily 03:00 UTC (`install_windows_task.ps1`)
- Fallback: GitHub Actions cron `15 3 * * *` in `.github/workflows/phylactery-upload.yml`
- One-shot: `--confirm-first-upload` (first run only)

## Class pre-authorization

PHYLACTERY_UPLOAD does NOT use the class-pre-auth grammar. It uses the
one-time `AUTHORIZED_TO_UPLOAD.md` arming file. Rationale: this loop is
lower-frequency, higher-permanence, and the operator arms it once instead of
approving batches.

## Dependencies

- Python ≥ 3.11 (stdlib only for orchestration; no pip installs required)
- Node ≥ 20 with `npm`
- Node packages (see `package.json`): `@ardrive/turbo-sdk`, `arweave`,
  `@noble/ed25519`
- Windows PowerShell for scheduled task registration

## Chain-row axes

| action | claim_status | notes |
|---|---|---|
| `start_upload` | proposed | preflight passed, tree walked |
| `disarmed_no_upload` | proposed | AUTHORIZED_TO_UPLOAD absent or sealed:false |
| `secret_scan_HALT` | failed | pattern match; upload never happened |
| `signature_mismatch_HALT` | failed | integrity gate |
| `bundler_5xx_HALT` | failed | 3 retries exhausted |
| `wallet_low_HALT` | failed | balance floor tripped |
| `tree_too_large_WARN` | partial | needs --force-large |
| `bitemporal_partial` | partial | soul/world_state/capsule missing timestamp keys |
| `no_delta_WARN` | partial | 0-byte delta from prior day (still uploaded) |
| `shipped` | wired_with_receipts | manifest tx_id received AND readback verified |
| `readback_HALT` | failed | manifest_tx not resolving after confirmation window |

## Confirmation window

Turbo commits the bundle to Arweave; the manifest tx_id is available
immediately but the gateway index takes 5–10 minutes to serve it reliably.
The runner performs the verification readback after a 6-minute sleep OR when
the operator runs `python -m factory.loops.phylactery_upload.upload --verify-only <tx_id>`.

## Verification (post-upload)

1. `HEAD https://arweave.net/<manifest_tx_id>` returns 200
2. `GET https://arweave.net/<manifest_tx_id>/README.md` returns 200 + expected sha256
3. Sample 3 nested paths (`apex/sigrun/soul.md`, `world_state/<latest>.md`,
   `arweave/receipts/<today>.jsonl`) — each returns 200
4. Verify all signatures against stored pubkeys (via `sign_ed25519.mjs --verify-all`)
5. Row appended: `shipped:<manifest_tx_id>` claim_status `wired_with_receipts`

## Bitemporal enforcement scope

Enforced only on:
- `apex/**/soul.md`
- `valkyries/**/soul.md`
- `world_state/*.md`
- `memory_capsules/**/*.md`

Every other file uploads without bitemporal check.

## Ownership / signing rules

See `../../../areas/phylactery/arweave/RUNNER_MAP.md` §lineage-ownership.
