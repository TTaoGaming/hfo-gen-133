# factory/loops/phylactery_upload/

Daily Arweave upload of the entire `areas/phylactery/` tree. One transaction
per day, unfolds via native Arweave path manifest v0.1 so anyone with the URL
can walk the tree in a browser.

See:
- Full spec: [`SPEC.md`](./SPEC.md)
- Operator cookbook: [`../../../areas/phylactery/arweave/TUESDAY_FIRST_UPLOAD.md`](../../../areas/phylactery/arweave/TUESDAY_FIRST_UPLOAD.md)
- Runner map: [`../../../areas/phylactery/arweave/RUNNER_MAP.md`](../../../areas/phylactery/arweave/RUNNER_MAP.md)

## Files

| file | role |
|---|---|
| `upload.py` | main orchestrator; `--dry-run`, `--confirm-first-upload`, `--verify-only <tx>` |
| `manifest_builder.py` | walks tree, hashes files, builds Arweave path manifest + HFO semantic manifest |
| `signer.py` | ed25519 signing wrapper (shells out to `sign_ed25519.mjs`) |
| `bitemporal.py` | enforces `valid_time_utc` + `transaction_time_utc` on soul / world_state / memory_capsule front-matter |
| `preflight_gate.py` | `--arm` writes `AUTHORIZED_TO_UPLOAD.md`; runner reads it on every run |
| `secret_scan.py` | HALTs on path or body-content secret patterns |
| `keygen.py` | ed25519 keygen for `--master` and `--lineage <path>` |
| `sign_ed25519.mjs` | Node: sign, verify, `--verify-all` |
| `upload_turbo.mjs` | Node: uploads via @ardrive/turbo-sdk, returns manifest_tx_id |
| `keygen_wallet.mjs` | Node: generate/import Arweave JWK wallet |
| `balance_check.mjs` | Node: check Turbo credit balance |
| `install_windows_task.ps1` | registers daily 03:00 UTC scheduled task |
| `package.json` | Node dependencies |
| `test_vectors.md` | smoke-test payloads for dry-run |

## Quickstart

```powershell
cd C:\Dev\hfo_gen_133_forge\factory\loops\phylactery_upload
npm install
python -m factory.loops.phylactery_upload.upload --dry-run
```

Dry-run walks the tree, hashes every file, builds both manifests, prints the
summary — but **does not** upload, sign, or touch the wallet. Safe to run any
time.

## First real upload

Follow [`TUESDAY_FIRST_UPLOAD.md`](../../../areas/phylactery/arweave/TUESDAY_FIRST_UPLOAD.md).

## Daily schedule

```powershell
.\install_windows_task.ps1
```

Registers `HFO_gen133_phylactery_upload` at 03:00 UTC daily. Optional:
push the GitHub Actions workflow for a cloud fallback.

## Kill

Delete `areas/phylactery/arweave/AUTHORIZED_TO_UPLOAD.md` to disarm without
unregistering the schedule. The scheduled runner will see the missing file
and exit `0` with a chain row `disarmed`.
