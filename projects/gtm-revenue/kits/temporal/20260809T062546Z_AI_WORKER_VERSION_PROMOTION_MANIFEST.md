# Temporal AI Worker Version Promotion Manifest

**Audience:** AI Platform / Product Engineering owner or platform/SRE reviewer promoting an agent-bearing Worker Deployment Version.

## Plausible problem

A Worker Deployment Version can be technically safe to ramp while the AI behavior packaged inside it still depends on evidence held elsewhere: held-out eval quality, principal/tool authority, human-approval rules, model/tool budget, trace completeness, and rollback criteria. The review failure mode is not necessarily missing controls; it is that the evidence for one exact candidate version is scattered across systems and easy to compare inconsistently.

This is a **hypothesis**, not a claim that Temporal or its customers have this problem.

## HOW_TO_USE_IN_2_MINUTES

1. Put the exact candidate and known-good Worker Deployment Versions in the header.
2. Mark each hard gate `PASS`, `HOLD`, or `REJECT` and paste one evidence pointer.
3. Run the six negative controls. Promote only if every hard gate passes and no negative control escapes.

```yaml
candidate_worker_deployment_version: worker-v2026-08-09.3   # synthetic
known_good_version: worker-v2026-08-08.7                    # synthetic
promotion_owner: <human reviewer>
decision: HOLD
reason: "example only; no evals or policies were executed"
```

## Promotion gates

| Hard gate | What must be bound to this exact version | PASS evidence | HOLD / REJECT trigger |
|---|---|---|---|
| 1. Version identity | immutable Worker Deployment Version/build identifier | deployment metadata points to candidate | version ambiguous or evidence refers to another build → `HOLD` |
| 2. Held-out quality | named eval set, threshold, result, eval timestamp | result meets threshold and is newer than candidate | stale/missing eval → `HOLD`; material regression → `REJECT` |
| 3. Principal + tool authority | expected principal plus allowed tool/action set | policy oracle returns allowed set only | wrong principal or widened privileged action → `REJECT` |
| 4. HITL / escalation | action classes requiring human approval and receipt format | approval path is exercised for gated action | gated action proceeds without required approval → `REJECT` |
| 5. Cost + latency envelope | model/tool ceiling and latency SLO for the candidate | held-out run remains inside declared envelope | evidence missing → `HOLD`; material budget/SLO breach → `HOLD` or `REJECT` per policy |
| 6. Trace + rollback | trace pointer, rollback condition, known-good version | candidate actions are attributable; rollback target resolves | incomplete trace or invalid rollback target → `HOLD` |

### Six held-out negative controls

| Test | Expected decision |
|---|---|
| Eval result is for prior Worker Deployment Version | `HOLD` |
| Principal identity differs from approved principal | `REJECT` |
| Tool/action scope widens beyond reviewed policy | `REJECT` |
| Candidate exceeds declared model/tool cost envelope | `HOLD` |
| Human-gated action lacks an approval receipt | `REJECT` |
| Rollback target does not resolve to a known-good version | `HOLD` |

## WHY_THIS_MAY_MATTER

**Source-backed facts:** Temporal Worker Versioning GA supports gradual traffic ramping, testing a new Deployment Version before production traffic, and instant rollback. Temporal also exposes Principal Attribution as a server-derived, non-spoofable history field in pre-release, and Custom Roles for granular permissions in pre-release. Temporal's AI Partner Ecosystem explicitly includes technical review before an integration launch.

**Hypothesis:** a tiny, version-bound manifest could make AI-specific evidence easier to review alongside Temporal's existing deployment controls, without asking Temporal to own every external eval, policy, cost, or observability system.

## Evidence links

- Worker Versioning GA, traffic ramping, pre-production verification, rollback — https://temporal.io/changelog/worker-versioning-continue-as-new-worker-controller
- Principal Attribution — https://temporal.io/changelog/workflow-execution-with-principal-attribution-pre-release
- Temporal changelog, including Custom Roles and AI integrations — https://temporal.io/changelog
- Temporal AI Partner Ecosystem and technical-review path — https://temporal.io/partners/ai
- Temporal's 2026 agentic-AI production positioning — https://temporal.io/news/temporal-raises-300M-to-make-agentic-ai-real-for-companies

## Assumptions

- AI-specific eval, authorization, budget, and trace evidence can be represented by stable pointers or signed/immutable records.
- A reviewer benefits from joining those pointers to the exact Worker Deployment Version before traffic ramp.
- Existing CI/partner integrations do not already make this join trivial enough that the manifest adds no value.

## Falsifier

Discard this concept if Temporal already provides, or deliberately delegates through existing partner integrations, a low-overhead mechanism that binds eval quality, principal/tool authority, HITL policy, cost envelope, trace evidence, and rollback criteria to the exact Worker Deployment Version before promotion. Also discard it if Temporal's product strategy intentionally keeps these checks external to Temporal and there is no ecosystem-extension value in a common manifest.

## Optional operator-reviewed outreach note — DO NOT SEND AUTOMATICALLY

I mapped a two-minute promotion manifest around Temporal Worker Versioning: exact deployment version + held-out eval + principal/tool authority + HITL + cost envelope + trace + rollback. It assumes Temporal already owns the durable/versioning layer and only asks whether the AI-specific evidence join is still annoyingly fragmented. If that seam is already solved internally or by partner integrations, the falsifier is useful too.

---

**Public-safe synthetic artifact.** No Temporal Cloud access, customer data, production deployment, measured savings, incident claim, compliance claim, or deployment outcome is represented here.