# microsaas_unit_ship

Ship one micro-SaaS unit end-to-end: layered build → wrangler deploy →
HEAD-verify 5 canonical URLs → generate distribution package.

## One-shot

```powershell
python factory\loops\microsaas_unit_ship\run.py --spec factory\targets\pending\promptbin.json
```

## Queue mode (recurring)

```powershell
# Consume next 3 rows from state/factory_targets/queue.jsonl
python factory\loops\microsaas_unit_ship\run.py --queue --max 3
```

Register a Windows scheduled task to fire daily at 08:00:

```powershell
schtasks /Create /TN "hfo-loop-A-microsaas-ship" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\microsaas_unit_ship\run.py --queue --max 3" `
  /SC DAILY /ST 08:00 /F
```

## Dry-run smoke test

```powershell
python factory\loops\microsaas_unit_ship\run.py --spec .\promptbin.json --dry-run
```

Skips npm install/build and wrangler; still exercises spec load,
distribution package generation, and chain-row writes.

## Prereqs

- Python 3.11+
- Node 20+ + `npm`
- `wrangler` CLI logged in on operator machine
- Optional: `SLACK_WEBHOOK_URL` in `.env` at repo root for halt escalation

## Where things land

- Build: `factory/build/<slug>/`
- Deploy: `https://<slug>.pages.dev`
- Distribution package: `factory/distribution/<slug>/`
- Ship log: `state/factory_ships/MICROSAAS_SHIPS.jsonl`
- Receipts: `state/loop_receipts/microsaas_unit_ship_<YYYYMMDD>.jsonl`
