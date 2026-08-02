# LOOP-B · FOSS_FORK_VARIANT — SPEC

```yaml
AIH2O:
  version: gen-133
  loop: foss_fork_variant
  role: executor
  actor: factory_loop
  verifier: license gate BEFORE code work + git status clean + wrangler deploy 200
  clock_source: host_read
  chain: state/loop_receipts/foss_fork_variant_<UTCDATE>.jsonl
  ship_log: state/factory_ships/FOSS_FORKS.jsonl
```

## Inputs

`--config fork.json`:

```json
{
  "foss_repo_url": "https://github.com/rowyio/rowy.git",
  "niche_mutation": {
    "slug": "hvac-jobsheets",
    "subdomain": "hvac-jobsheets",
    "rename": {"Rowy": "JobSheets", "rowy": "jobsheets"},
    "reskin_colors": {"#4285F4": "#1D8348", "#EA4335": "#B03A2E"},
    "niche_prompts": {"landing_hero": "Job sheets for HVAC crews.", "value_prop": "..."},
    "payment_integration": "stripe",
    "target_icp": "HVAC contractors 5-50 techs"
  }
}
```

Flags:
- `--whitelist-copyleft` — allow GPL/AGPL/SSPL for THIS fork only
- `--dry-run` — skip build + wrangler; still exercises license gate + mutation apply

## License gate (runs BEFORE code work)

Detection: reads `LICENSE`/`LICENSE.md`/`COPYING`; falls back to `package.json:license`.

Compatible (auto-accept): MIT, Apache-2.0, BSD-2/3-Clause, ISC, Unlicense, 0BSD, MPL-2.0

Incompatible (reject unless whitelisted): GPL-2/3, AGPL-3, SSPL-1

Unknown: reject by default. Operator can override with `--whitelist-copyleft` only after reading the LICENSE and confirming.

## Outputs

- `factory/forks/<slug>/` — mutated clone
- `https://<subdomain>.pages.dev`
- Row in `state/factory_ships/FOSS_FORKS.jsonl` with `parent_sha`, `variant_sha`, `license_spdx`
- Multiple rows in `state/loop_receipts/foss_fork_variant_<UTCDATE>.jsonl`

## Kill conditions

- `license_HALT` — incompatible or unknown SPDX without whitelist flag
- `build_HALT` — npm install or npm run build non-zero; `git reset --hard HEAD` + `git clean -fd` executed
- `deploy_HALT` — wrangler non-zero; build preserved for operator diagnosis
- `clone_failed` — git clone non-zero (network / auth / bad URL)

## Cadence

Fire 3-5/day per operator-approved candidate. No cron. Each fire is one
`--config` invocation from a queue file the operator maintains manually.

## Class pre-authorization

FOSS_FORK_VARIANT is NOT gated by `state/experiments/approvals/latest.txt` —
each fork is one deliberate operator action (chose the parent, wrote the
mutation). Downstream distribution IS gated:

```
class:foss_fork_distribution:quota=5/wk:seq_range=001-999:expires=<UTC>
```

## Chain-row axes

| action | claim_status | notes |
|---|---|---|
| `start_fork:<slug>` | proposed | parent url logged |
| `clone_failed:<slug>` | failed | git clone rc≠0 |
| `license_HALT:<slug>` | failed | before mutations run |
| `mutations_applied:<slug>` | proposed | idempotent find/replace |
| `build_HALT:<slug>` | failed | rollback executed |
| `deploy_HALT:<slug>` | failed | build preserved |
| `forked:<slug>` | wired_with_receipts | parent_sha + variant_sha + license logged |
