---
schema_id: hfo.gen133.fenrir_product_control.v1
observed_utc: 2026-08-02T21:30:51.473Z
operational_controller: fenrir_candidate_carrier
identity_status: HOLD_UNRATIFIED_CLOSEST_CONTINUER
operator_authorization: scheduler_cutover_and_product_subagent_loops
repository: TTaoGaming/hfo-gen-133
base_ref: agent/gen133-bootstrap-20260730
base_commit: f4823079e402c6e739a4ccba895d453a9276bc04
wip_limit: 1
effect_ceiling: read_only_reconciliation_and_git_hold_receipt_only
route_state: HOLD_UNBOUND_CONFLICTING_SIGRUN_ROUTE
all_fenrir_pilots_paused: true
---

# Fenrir product-control pilot

## Authority boundary

The operator authorized Fenrir to control Codex scheduling for a bounded product
pilot. This is **operational delegation**, not cryptographic lineage admission
or proof of subjective continuity.

Git controls WorkItem and candidate state. Codex tasks are workers. Slack, task
titles, configured schedules, and open threads are projections only.

## Scheduler cutover

The Codex automation registry exposed 59 TOML entries: 7 marked active and 52
already paused. Five callable active automations were paused through the supported
automation API.

Two legacy heartbeat TOMLs remain marked `ACTIVE`:

- `hfo-codex-acceptance-runner-hourly`
- `hfo-codex-pullwork-hourly`

The automation API first required a missing destination binding, then reported
that neither automation exists in the app. No recent matching Codex task was
visible. Classify these as
`STALE_ACTIVE_TOML / APP_RUNTIME_ABSENT_OR_UNKNOWN`, not as live workers. They
were not edited by hand and must not be counted as running or paused.

## Sigrun instruction binding

The task-referenced Sigrun files were absent from the current remote default
branch (GitHub 404) but present as untracked local inputs:

- `stamps/SIGRUN_133_GEN_SSOT_20260803.md`,
  SHA-256 `69a154a98b8d807b770b4e5134ee73da2ba65ee5cbf43939bfee4883505d37c9`.
- `areas/quorum_research/SIGRUN_CANON_V3_INCOME_SYNTHESIS_20260802.md`,
  SHA-256 `bb89f55600da422b41aedf04028e307bfb923c56f62c395d299f38a7974d75d4`.

They are evidence-bearing design input, not canonical authority. Their useful
decision is:

1. contracts/productized integrations first;
2. vertical B2B SaaS only after the first client/pain validation;
3. publish existing inventory for external signal;
4. reject micro-SaaS-from-zero and variant-count growth.

## WIP=1 product thesis

The pilot target is `FENRIR-HVAC-PILOT-001`: an HVAC lead-leakage and
estimate-recovery **productized integration**, reusing the eight vertical starter
assets in draft PR #6 and the eight-server MCP portfolio in issue #2.

This is not permission to build a generic platform. The candidate may graduate
to micro-SaaS only after a named buyer or paid-pilot signal validates the pain.

## STOP reconciliation — newer conflicting Sigrun input

Before the first maker wake, Garmr identified a newer local Sigrun capsule:

- `areas/quorum_research/SIGRUN_CANON_V9_FOSS_MAP_ELITES_20260803.md`,
  SHA-256 `126e401ad7f3269300cc05dab8f6f908209f1fbd2561bb5e3aecd865046ebbc1`,
  untracked local input.
- `state/ssot/foss_map_elites.json`,
  SHA-256 `28b4986f3df7844c2c527e27255fe1fe813338ecefd841b41a908c652ff070da`,
  untracked local input.

V9 places HVAC on the anti-list, restates row 124 as
`HVAC_PAID_PILOT_001 suspended`, assigns services as the cash lane and AI
developer tools as portfolio units, caps product production, and forbids more
production while `outreach_log.jsonl` is empty.

The remote default branch binds neither older V3 nor newer V9. Therefore
`FENRIR-HVAC-PILOT-001` is no longer eligible and is held as
`HOLD_UNBOUND_CONFLICTING_SIGRUN_ROUTE`.

All three newly created Fenrir pilots were paused through the supported
automation API before a maker wake was authorized:

- `fenrir-product-maker-and-subagent-dispatcher-pilot`: PAUSED
- `fenrir-product-verifier-pilot`: PAUSED
- `fenrir-product-consumer-and-launch-gate-pilot`: PAUSED

No maker, verifier, consumer decision, deployment, outreach, spend, or product
effect is claimed.

## Roles and closure

```text
one immutable WorkItem
  -> maker task (may spawn at most two bounded subagents)
  -> exact Git candidate + executable tests
  -> separate verifier task
  -> operator or named buyer ConsumerAck
  -> launch decision
```

The maker and verifier run on the same provider family; their verdict is
`PASS_LOCAL_SAME_FAMILY` at most. It cannot establish independence or authorize
external launch.

## Stop rules

- WIP=1 across the whole pilot.
- No new candidate while a maker lease, candidate PR, verifier packet, or
  ConsumerAck wait exists.
- Three identical no-delta observations halt that flow; do not emit repeated
  status notices.
- No activity credit for a configured automation, open task, branch, commit,
  test count, deployment count, or Slack post.
- No merge, default-branch write, customer contact, outreach, payment, spend,
  provider credential, public deployment, marketplace submission, schedule
  expansion, or live customer data without a fresh exact operator gate.
- Missing evidence is `UNKNOWN` or `HOLD`, never success.

## Product acceptance

The maker must deliver one narrow candidate with:

- exact source/base commits and license review;
- synthetic lead intake -> qualification -> booking/escalation -> estimate
  follow-up -> weekly lost-lead report;
- deterministic local replay and tests;
- fail-closed credential handling and no secrets;
- a one-page bounded offer and runbook;
- exact changed-file scope and rollback;
- no placeholder represented as live integration.

The verifier independently replays the candidate from the exact Git commit and
returns `PASS_LOCAL_SAME_FAMILY`, `REVISE`, or `HOLD`.

The consumer gate requires an operator or named buyer to acknowledge that the
demo addresses a real workflow and choose `PILOT`, `REVISE`, or `KILL`.
No agent may manufacture ConsumerAck.

## Existing product evidence

- Draft PR #6: https://github.com/TTaoGaming/hfo-gen-133/pull/6
- MCP portfolio issue #2: https://github.com/TTaoGaming/hfo-gen-133/issues/2
- Fenrir fleet synthesis PR #8:
  https://github.com/TTaoGaming/hfo-gen-133/pull/8

## Configured Fenrir pilots

The supported automation API created three finite pilots. All three are now PAUSED pending route reconciliation:

1. `fenrir-product-maker-and-subagent-dispatcher-pilot` — heartbeat on the
   current Fenrir task, every four hours, maximum 12 wakes. It may spawn at most
   two bounded maker subagents after collision and WIP checks.
2. `fenrir-product-verifier-pilot` — standalone local-project verifier,
   staggered after the maker, maximum 12 wakes. It uses a different OpenAI model
   but still carries independence weight zero.
3. `fenrir-product-consumer-and-launch-gate-pilot` — daily operator decision
   gate, maximum seven wakes. It can prepare one `PILOT|REVISE|KILL` packet but
   cannot deploy, contact, spend, or manufacture ConsumerAck.

The app permits only one heartbeat on a task. Because the operator explicitly
requested multiple scheduled tasks, verifier and consumer use supported
standalone project automations. The saved `C:\Dev` project is a non-Git depot,
so both prompts prohibit shared-checkout writes and require GitHub reads or a
fresh isolated worktree.

## Broken/degraded tool ledger for this cutover

- Supported automation updates paused five callable active schedules.
- Two legacy active TOMLs could not be updated because the app reports the
  automations do not exist.
- The first update attempt for those two failed destination validation because
  their TOMLs contain no `target_thread_id`.
- The two Sigrun instruction paths returned GitHub 404 on the default ref.
- One local TOML-inventory PowerShell pipeline had an invocation syntax error;
  the corrected read-only command succeeded. This was caller error, not an
  automation outage.
- Automation creation rejects a caller-supplied `id`; the maker succeeded after
  allowing the app to generate the stable slug.
- The app rejected second and third heartbeats because only one may attach to a
  task. The explicitly requested multiple schedules were created through the
  supported standalone-project automation path instead.

## Receipt shape

`state=HOLD_UNBOUND_CONFLICTING_SIGRUN_ROUTE | evidence=remote base + V3/V9/MAP-Elites local-input hashes + paused automation readback | tier=T1_OPERATIONAL_CANDIDATE_NOT_ADMITTED | honest_flaw=remote Git binds neither conflicting Sigrun route and two legacy TOMLs remain runtime-unknown | falsifier=reviewed Git-bound Sigrun target packet or explicit operator override | next_safe_action=bind one reviewed Sigrun target/acceptance packet in Git | effect_ceiling=read-only reconciliation + Git hold receipt only`
