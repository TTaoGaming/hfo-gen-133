# LOOP-B test vectors

## Vector 1 — MIT parent, happy path (dry-run)

Config:
```json
{
  "foss_repo_url": "https://github.com/vercel/next.js.git",
  "niche_mutation": {
    "slug": "hvac-nextjs-test",
    "subdomain": "hvac-nextjs-test",
    "rename": {"Next.js": "HVACForms"},
    "reskin_colors": {},
    "niche_prompts": {"hero": "Job forms for HVAC"},
    "payment_integration": "stripe",
    "target_icp": "HVAC contractors"
  }
}
```
Invocation:
```
python factory/loops/foss_fork_variant/run.py --config /tmp/hvac-nextjs.json --dry-run
```
Expected chain rows:
1. `start_fork:hvac-nextjs-test` proposed
2. `mutations_applied:hvac-nextjs-test` proposed (edits > 0)
3. `forked:hvac-nextjs-test` wired_with_receipts, license_spdx=MIT

Expected outputs:
- `factory/forks/hvac-nextjs-test/` cloned + mutated
- Row in `FOSS_FORKS.jsonl` with parent_sha, variant_sha, license_spdx=MIT

## Vector 2 — AGPL parent, reject

Config: `foss_repo_url` = anything with AGPL (e.g. https://github.com/nextcloud/server.git).

Expected:
- `start_fork` proposed
- `license_HALT:<slug>` failed. Chain-row extra shows `kill_decision.tripped=["license_reject"]`
- No mutations applied
- `FOSS_FORKS.jsonl` NOT touched
- Slack `halt` ping

## Vector 3 — AGPL with whitelist

Same config as V2 but with `--whitelist-copyleft`.

Expected:
- License gate returns ok=True with reason "copyleft but operator whitelisted"
- Pipeline continues normally
- `license_spdx=AGPL-3.0` recorded in FOSS_FORKS.jsonl

## Vector 4 — build broken by mutation

Rename that shatters imports, e.g. `{"import ": "IMPORT "}` in rename map.

Expected:
- `start_fork` + `mutations_applied` proposed
- `build_HALT:<slug>` failed with git reset + git clean in receipts
- `factory/forks/<slug>/` restored to pristine clone (parent_sha == variant_sha would be, but variant_sha never recorded because we halt before that)

## Vector 5 — no LICENSE file, unknown license

Config points at a repo with no LICENSE file and no `package.json:license`.

Expected:
- `license_HALT` with reason "UNKNOWN unknown — reject by default"
- Operator must inspect the repo manually and either add `--whitelist-copyleft` (if source is genuinely permissive) OR skip
