# S08 GTM Target Card — 1Password

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
target: 1Password
species: PRODUCT_PLATFORM
vertical: identity_security | agent_identity | secrets_and_credential_brokering
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT
next_consumer: S07
consumer_workitem: S07_1PASSWORD_AGENT_AUTHORITY_DRIFT_GATE_V1
valid_time_utc: 2026-08-09T21:29:00Z
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: ef8a08e325297d6b55c4ef66110448c965e094ac77258e94fe49a0decb0f6ecc
send_authority: NONE
```

## Current product / business signal

1Password is actively expanding from human credential management into identity and access controls for AI agents and machine workloads.

- **2026-03-17 — Unified Access Pro GA.** 1Password launched Unified Access to discover and secure human, machine, and AI-agent identities, apply access controls, and build auditability around credential use. The launch also described scoped runtime credentials for agent and machine workloads as a later-2026 expansion.  
  Source: https://1password.com/press/2026/mar/1password-unified-access
- **2026-06-15 — Credential Broker private beta.** 1Password introduced a broker that verifies trusted identity signals before releasing approved credentials, initially using GitHub Actions workload identity and with a roadmap spanning humans, machine workloads, and AI agents.  
  Source: https://1password.com/press/2026/june/credential-broker
- **2026-07-16 — 1Password for Claude + Agentic Mode.** The integration gives Claude per-task, user-approved credential use while keeping secrets outside model context; Agentic Mode restricts the browser agent to the credentials approved for that task, and 1Password says the framework is intended to extend to other browser agents/platforms.  
  Source: https://1password.com/press/2026/july/1password-for-claude
- **2026-07-21 — delegated local-agent reference architecture.** 1Password published an architecture for a locally running agent to borrow human authority in a scoped, short-lived, auditable way.  
  Source: https://1password.com/blog/ai-agent-identity-delegated-local

These are direct product and architecture signals. They are **not** evidence that 1Password has a control failure, release bottleneck, or unmet need for an external specialist.

## Best buyer / user persona

**Primary persona:** 1Password Unified Access / Agent Security product-engineering or identity-platform leadership responsible for agent identity, credential brokering, delegated authority, developer integrations, and production assurance across supported agent surfaces.

**Named public bridge:** **Nancy Wang, CTO of 1Password**, directly named in the 2026-06-15 and 2026-07-16 official announcements. Her title is source-backed; procurement authority, accessibility, partnership authority, or interest are not inferred.

## Expensive pain hypothesis

**Hypothesis:** as 1Password adds more agent runtimes and credential-broker integrations, product/security engineers *may* spend material **engineering + security-review hours per accepted integration or authority-model revision** proving that the exact revision preserves identity binding, credential scope, delegated-vs-workload authority semantics, revocation behavior, audit provenance, and fail-closed behavior across heterogeneous agents.

**Primary measurable value metric:** engineering + security-review hours per accepted agent-integration revision.

**Secondary metrics:** integration release cycle time; number of authority-regression defects caught before release; audit/reconstruction time for a synthetic credential-use event.

No public source found establishes current values for those metrics or proves that this burden is excessive.

## Evidence for the hypothesis

- 1Password is now supporting multiple authority shapes: human-delegated browser agents, machine/workload identities, CI/CD workloads, and future broader runtime credential issuance.
- The Claude integration is explicitly per-task and session-scoped, while Credential Broker begins from workload identity signals; those are distinct authority models whose semantics can drift when integrations evolve.
- 1Password publicly emphasizes proving **which identity** used a credential, **under whose authority**, with scoped access and auditability. That makes revision-level authority evidence adjacent to its stated product goals.

## Evidence against the hypothesis

- 1Password is already building the identity, credential-brokering, scope, revocation, and audit primitives directly; this is evidence of internal maturity, not a missing capability.
- Agentic Mode already constrains accessible credentials to the current approved task/session, and Credential Broker is explicitly designed around trusted identity before credential release.
- No official source found reports authorization regressions, credential-scope incidents, excessive integration-review burden, slow releases, or demand for an external policy/release-gate layer.

## 2-minute utility gift / proof-kit concept

**Agent Authority Drift Card — Principal × Agent × Credential × Scope × Evidence × Revoke**

Given one tiny synthetic before/after integration fixture, emit only the authority delta:

- human/workload principal identity;
- agent/runtime identity;
- credential or token class;
- allowed target/audience/action scope;
- required approval or attestation;
- expiration/session boundary;
- audit provenance fields;
- revocation / cancel behavior;
- exact candidate and baseline digests;
- verdict: `PROMOTE | HOLD | REJECT`.

The useful result is not another IAM diagram; it is a compact answer to **“did this integration revision widen or ambiguously change effective agent authority?”**

## Deeper proof artifact

**Synthetic Agent Authority Regression Harness**

Build a public-safe offline harness using invented users, workloads, vault items, browser tasks, and mocked downstream services. Keep authorization independent from model behavior with a deterministic OPA/Rego-style oracle. Exercise:

- delegated-human vs machine-bound principals;
- wrong-principal and wrong-audience requests;
- credential-scope widening;
- stale/absent attestation;
- session expiry and replay;
- approval-required vs autonomous edges;
- credential non-exposure assertions;
- missing audit provenance;
- revocation/cancel propagation;
- baseline-vs-candidate authority graph diff;
- exact policy/integration/fixture digests and rollback target.

No 1Password account, real credential, customer data, paid call, deployment, secret handling, vulnerability claim, or production security claim.

## Apply-now vs relationship-only route

**RELATIONSHIP_ONLY.** The public evidence supports a product/platform relationship or ecosystem-integration hypothesis, not an apply-now claim. S07 should build the narrow proof artifact first; any later external contact remains operator-approved and outside this carrier's authority.

## Strongest falsifier

Kill this wedge if 1Password already has a low-overhead first-party mechanism that binds each exact agent/integration revision to principal identity, authority type, credential scope, approval/attestation, audit provenance, revocation semantics, negative-control tests, and rollback evidence across supported agent platforms.

Also kill it if 1Password intentionally treats policy-level action authorization as the downstream application's responsibility and does not want that concern represented in its integration acceptance surface.

## Privacy / effect ceiling

`PUBLIC_SAFE_SYNTHETIC_ONLY / T0_PREP_RESEARCH_GIT`.

No private data, account access, terms acceptance, credential handling, external outreach, application submission, paid tool call, deployment, publication, merge, or autonomous negotiation.

## Honest flaw

**High redundancy risk.** 1Password is already shipping directly into agent identity and credential authorization, so a generic “secure AI agents with OPA” kit would be weak and duplicative. The only defensible seam is narrower: **regression-testing effective authority across exact integration revisions and heterogeneous authority models**. If S07 cannot make that distinction concrete in a small artifact, this card should not consume more WIP.

## Evidence digest preimage

`evidence_digest_sha256` is SHA-256 over UTF-8 lines in the following exact order, each encoded as `date|url|claim\n`:

```text
2026-03-17|https://1password.com/press/2026/mar/1password-unified-access|Unified Access Pro GA; discovers/secures human, machine, and AI-agent identities; continuous authorization; audit roadmap; scoped runtime credentials planned later in 2026.
2026-06-15|https://1password.com/press/2026/june/credential-broker|Credential Broker private beta; verifies trusted workload identity signals before releasing approved credentials; roadmap spans humans, machine workloads, and AI agents.
2026-07-16|https://1password.com/press/2026/july/1password-for-claude|1Password for Claude launched; Agentic Mode; per-task user-approved credential access; secrets remain outside model context; multi-site sessions; framework intended to extend to other browser agents.
2026-07-21|https://1password.com/blog/ai-agent-identity-delegated-local|Reference architecture for locally running AI agents using scoped, short-lived, auditable delegated authority.
```
