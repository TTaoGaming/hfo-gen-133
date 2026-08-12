---
schema_id: hfo.gen133.dlc_foss_factory_control.v1
observed_utc: 2026-08-02T21:45:00Z
repository: TTaoGaming/hfo-gen-133
controller_pr: 9
route_state: SCAFFOLD_ONLY_TARGET_UNADMITTED
wip_limit: 1
validated_elites: 0
scheduler_snapshot_utc: 2026-08-02T21:46:39Z
effect_ceiling: local_scaffold_plus_synthetic_tests_and_draft_git_receipts_only
---

# DLC-style FOSS product factory control

## Decision

DLC-style commercial extensions to FOSS are technically viable when the extension
adds a material user outcome, the exact upstream and license are bound, update
compatibility is explicit, and the product is not represented as market-validated
before external evidence exists.

This packet authorizes reusable factory infrastructure and local synthetic
verification. It does **not** admit a product target or authorize deployment,
billing activation, public publishing, outreach, submissions, spend, credentials,
customer data, or a batch of reskins.

Current input truth:

- Sigrun V9 and `foss_map_elites.json` are untracked local evidence, not remote
  Git authority.
- All ten MAP-Elites rows are hypotheses because none binds the required original
  demand permalink: `validated_elites=0`, `hypothesis_candidates=10`.
- Olrun's channel and revenue numbers are planning priors supplied by an agent,
  not independently verified facts or revenue commitments.
- Services may be operated as a separate cash lane; product construction cannot
  be counted as service outreach, cash, adoption, or distribution.

## Olrun loops, reconciled

| Loop | Current disposition | Reason |
|---|---|---|
| A MicroSaaS unit ship | HOLD target; ALLOW scaffold | A unit needs a reviewed target packet before maker work. Build/deploy/payment/distribution must be separate gates. |
| B FOSS fork variant | REPLACE with one extension candidate | Rename/reskin/batch cloning is not a material outcome. WIP=1 and semantic extension checks apply. |
| C Directory batch | HOLD | Requires a production-ready release, exact listing copy, destination allowlist, and operator send approval. CAPTCHA is always human. |
| D Demand signal mine | ALLOW read-only bounded research | Original permalinks only; obey rate limits and site terms; no bypass or automated posting. Output is a candidate packet, not validation by itself. |
| E Partner pitch batch | STAGE-ONLY after product evidence | Drafts may be prepared only for an admitted offer. Sending requires a fresh quota, identity/compliance checks, and operator approval. |
| F SEO content draft | STAGE-ONLY after a real unit exists | Drafting may follow a demo; publishing waits for accurate product claims and operator approval. |

## Target admission packet

No maker may select a FOSS target until reviewed Git binds all of:

1. target id and one narrow user/job-to-be-done;
2. original Reddit, Hacker News, or Indie Hackers permalink, observation date,
   engagement score, buyer/user class, and pain statement;
3. pricing evidence kept separate from interest evidence; price is `UNKNOWN`
   unless explicitly supported;
4. upstream repository, ref, immutable commit, license path, license blob/hash,
   obligations, trademark/name boundary, and model/data/asset license caveats;
5. material extension delta beyond rename, theme, prompt swap, or thin wrapper;
6. falsifiable user outcome and predeclared success threshold;
7. named maker, distinct verifier, and named consumer;
8. deterministic acceptance command, allowlisted paths, rollback, expiry, and
   external-effect ceiling.

## Product state machine

### REJECTED

License or trademark conflict, missing original demand evidence, upstream cannot
be pinned, the proposal is only a reskin, or the claimed outcome is not testable.

### DEMO_READY

All of the following are required:

- exact upstream and extension commits plus license readback;
- one-command clean install/build/test from an isolated checkout;
- the primary synthetic workflow completes end to end;
- at least one negative/failure workflow fails closed;
- no embedded secrets, live customer data, fake integration, or unlabelled
  placeholder;
- material-delta test demonstrates the new outcome;
- local regression receipt binds commands, exits, and artifact hashes.

### PILOT_READY

Requires DEMO_READY plus:

- named pilot consumer and bounded pilot outcome;
- real authentication/authorization boundary and tenant/data isolation where
  applicable;
- configuration validation, idempotency, retries/timeouts, rate limiting, and
  user-visible failure recovery;
- privacy/data-retention/deletion behavior documented and tested;
- observability, support runbook, backup/restore where stateful, and tested
  rollback;
- sandbox billing or explicit no-billing mode; no placeholder represented as
  active commerce;
- verifier-owned operational held-out replay against the exact candidate SHA;
- consumer chooses `PILOT`, `REVISE`, or `KILL`.

### PRODUCTION_READY

Requires PILOT_READY plus every applicable check below:

- immutable release tag/image digest and reproducible build provenance;
- dependency lock, SBOM or equivalent dependency inventory, license inventory,
  secret scan, vulnerability scan, and remediation/exception record;
- threat model covering authentication, authorization, injection, SSRF/file
  access, supply chain, tenant boundaries, abuse, and sensitive-data paths;
- TLS/domain configuration, secure headers/cookies, webhook signature validation,
  replay protection, and billing idempotency where applicable;
- migrations, backup and restore drill, disaster/rollback drill, and data export
  and deletion test;
- service limits, concurrency/load smoke test, health/readiness probes, logs,
  metrics, alert ownership, SLO, incident and support runbooks;
- accessibility and browser/device checks for the declared support matrix;
- privacy policy, terms, attribution/notices, trademark boundary, support contact,
  and accurate billing/cancellation/refund behavior;
- clean deploy from the immutable candidate followed by five independent URL/API
  checks and a rollback check;
- distinct verifier receipt binding raw outputs to the exact release;
- named consumer acceptance. Same-family replay may be
  `PASS_LOCAL_SAME_FAMILY` but cannot alone establish independence.

### MARKET_VALIDATED

Requires PRODUCTION_READY plus external human evidence against a threshold
declared before observation. A page view, deployment, post, directory listing,
configured Stripe object, GitHub star, or agent-authored enthusiasm is not a
customer. Record outside users, retained use, paid conversion or an explicit
buyer commitment separately.

## Held-out evaluation contract

- `LOCAL_REGRESSION`: maker-readable fixtures; deterministic behavior only.
- `OPERATIONAL_HELD_OUT`: verifier receives raw inputs without expected outputs in
  its task prompt; shared filesystem means it is not cryptographically sealed.
- `SEALED_EXTERNAL`: evaluator owns corpus and expectations and returns immutable
  source-bound receipts; required for independent tier-promotion claims.

Minimum verifier-owned adversarial cases:

1. missing original demand permalink;
2. license `NOASSERTION` without license-byte readback;
3. license or trademark boundary violation;
4. renamed/reskinned upstream with no material outcome;
5. happy-path-only workflow that silently loses data on retry;
6. cross-tenant access or authorization bypass;
7. forged/replayed webhook or duplicate charge;
8. dependency or secret-scan failure;
9. deploy succeeds but health, migration, or rollback fails;
10. maker changes candidate after verifier SHA freeze;
11. placeholder payment/integration presented as live;
12. market claim supported only by internal activity.

The verifier publishes the public contract and validator but retains adversarial
expected outcomes. A maker must not read or edit verifier-owned cases.

## Goal-loop protocol

Each task wake performs exactly one transition and stops:

`observe exact Git + lease -> select one eligible delta -> implement or verify ->
write receipt -> read back -> return one next consumer`.

Stop on competing lease, unbound target, changed candidate SHA, missing allowlist,
license ambiguity, failed mandatory check, or three identical no-delta wakes.
A configured schedule, open task, commit count, test count, deployment, or Slack
message is not progress without the required receipt.

## Initial Codex lanes

- Admission scout: reuse task `019fc46b-35ce-7e83-b6a0-41da4926758f`.
- Held-out verifier: reuse task `019fc468-bce5-7ae3-889f-63783416eef2`.
- Maker scaffold: task `019fc470-762c-7683-9573-e75d64c3435a`, isolated and
  target-agnostic. It may not select a product target.

Maker scaffold deliverables:

- `unit_spec.schema.json` and example invalid/valid specs;
- license and provenance preflight interface;
- deterministic template materializer with no network side effects;
- local install/build/test/health/rollback adapters;
- receipt schema and content-addressed run directory;
- staged landing/distribution-package interfaces that are inert by default;
- tests for idempotency, collision/WIP lock, path traversal, secret rejection,
  incomplete specs, duplicate events, failed health checks, and rollback;
- README and one synthetic reference unit that is unmistakably non-production.

## Finite scheduled pilots

The supported Codex automation API created three active, finite heartbeats:

- `fenrir-dlc-factory-scaffold-pilot` -> maker task
  `019fc470-762c-7683-9573-e75d64c3435a`;
- `fenrir-foss-target-admission-pilot` -> admission task
  `019fc46b-35ce-7e83-b6a0-41da4926758f`;
- `fenrir-dlc-held-out-gate-pilot` -> verifier task
  `019fc468-bce5-7ae3-889f-63783416eef2`.

The first scheduler readback at `2026-08-02T21:46:39Z` reported all three
`ACTIVE`. Schedule presence proves configuration only. Each wake must emit a
new artifact or raw verification receipt; collision/no-delta wakes stop without
work, and each schedule expires after its finite wake count. The prior product
maker/verifier/consumer pilots remain paused.

## Planning timeboxes

These are planning estimates, not delivery or revenue guarantees:

| State | Tight-scope elapsed time | Assumptions |
|---|---:|---|
| deterministic scaffold or local demo | 4-12 hours | known stack, no live auth/billing, synthetic data |
| useful DEMO_READY extension | 1-3 days | admitted target, stable upstream, one primary workflow |
| bounded PILOT_READY product | 3-7 days | one deployment target, one named consumer, limited integrations |
| credible PRODUCTION_READY v1 | 1-3 weeks | security/ops/legal/billing checks, independent replay, rollback |
| MARKET_VALIDATED | usually weeks to months | external users and distribution; cannot be manufactured by Codex |

A four-hour artifact may be launchable as a demo. Calling it useful requires a
real user outcome; calling it production-ready requires the operational gates;
calling it validated requires external humans.

## Exactly one next safe transition

Build and independently replay the reusable factory scaffold while the admission
scout searches for one Git-bindable target. Do not build or deploy a target unit
until the target packet is reviewed and the controller moves it out of HOLD.
