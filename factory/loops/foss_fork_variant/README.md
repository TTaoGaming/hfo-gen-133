# foss_fork_variant

Clone a permissive-licensed FOSS project, apply niche mutations, deploy a
variant subdomain. License compatibility is checked BEFORE any code work.

## One-shot

```powershell
python factory\loops\foss_fork_variant\run.py --config factory\targets\forks\hvac-jobsheets.json
```

## Override for copyleft (deliberate)

```powershell
python factory\loops\foss_fork_variant\run.py --config .\fork.json --whitelist-copyleft
```

Only use `--whitelist-copyleft` after you've read the parent's LICENSE and
have a clear plan for AGPL/GPL compliance (source disclosure of your
modifications, users receive a copy of the license, etc.).

## Dry-run smoke

```powershell
python factory\loops\foss_fork_variant\run.py --config .\fork.json --dry-run
```

Skips npm install/build and wrangler; still exercises clone, license
detection, mutation application, and chain-row writes.

## Prereqs

- Python 3.11+
- `git` on PATH
- Node 20+ + `npm`
- `wrangler` CLI logged in
- Optional: `SLACK_WEBHOOK_URL` in repo `.env` for halt escalation

## Where things land

- Fork clone: `factory/forks/<slug>/`
- Deploy: `https://<subdomain>.pages.dev`
- Ship log: `state/factory_ships/FOSS_FORKS.jsonl` (parent_sha, variant_sha, license_spdx)
- Receipts: `state/loop_receipts/foss_fork_variant_<YYYYMMDD>.jsonl`
