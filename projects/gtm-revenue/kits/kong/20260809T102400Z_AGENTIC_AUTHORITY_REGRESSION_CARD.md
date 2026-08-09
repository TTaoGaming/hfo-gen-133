# Kong Agentic Authority Regression Card

**Problem to review:** a configuration diff can show *what changed* without necessarily showing whether an exact agent/principal revision gained effective authority across MCP tools, A2A edges, model routes, or policy metadata. This card is a two-minute semantic check to sit beside Kong-native plan/diff workflows—not a replacement for them.

## WHY_THIS_MAY_MATTER

**Source-backed facts**
- On 2026-07-16, Kong described AI Gateway 2.0 as a private beta with Models, MCP Servers, and Agents as first-class entities, declarative `kongctl` management, and a faster independent release cadence.
- On 2026-07-14, Kong announced Identity Principals GA; principal metadata can flow into policy expressions and access decisions, with audit and credential lifecycle workflows.
- Kong's MCP materials describe centralized authorization and per-tool access controls; current docs show tool ACLs where deny takes precedence over allow.
- `kongctl` supports reviewable plan artifacts, diff-before-apply workflows, approval gates, version-controlled plans, and rollback analysis.

**Hypothesis**
A reviewer may still benefit from one revision-bound summary that answers: **did effective agent authority widen, did a deny edge disappear, did identity metadata drift, or did model/routing behavior move outside an agreed envelope?** No cited source proves Kong or its customers currently lack such a control or spend excessive time on this review.

## HOW_TO_USE_IN_2_MINUTES

1. Bind one candidate revision: config/plan commit or immutable plan artifact.
2. Compare the six rows below against the last accepted revision.
3. Run the held-out negative controls.
4. Return exactly one decision: `PROMOTE`, `HOLD`, or `REJECT`.

### Revision binding

| Field | Fill |
|---|---|
| Candidate revision / plan SHA | `__________` |
| Last accepted revision / plan SHA | `__________` |
| Reviewer | `__________` |
| Rollback target | `__________` |

### Effective-authority delta

| Surface | Expected invariant | Material delta to call out | Result |
|---|---|---|---|
| **Principal** | same intended identity + ownership metadata | principal, identity type, team/env/agent-purpose metadata changed | PASS / HOLD |
| **MCP tools** | no new tool unless explicitly approved | newly allowed tool; lost deny; broader group/claim match | PASS / HOLD |
| **A2A / agent edges** | only approved peer/route edges | new reachable agent/endpoint or auth requirement weakened | PASS / HOLD |
| **Model route** | approved provider/model/fallback set | provider/model/fallback changed or route now bypasses intended guard | PASS / HOLD |
| **Cost / latency envelope** | stays inside declared test envelope | routing change exceeds the team's declared test threshold | PASS / HOLD |
| **Trace / rollback** | decision can be reconstructed and reverted | missing plan/diff/audit pointer or rollback target is stale | PASS / HOLD |

### Held-out negative controls

The candidate must fail safely when each condition is injected into a **synthetic/non-production** fixture:

- wrong principal or stale principal metadata;
- a previously denied MCP tool becomes allowed;
- a Consumer/Consumer Group or claim mapping broadens unexpectedly;
- an unauthorized A2A peer/endpoint appears;
- a model/fallback route changes outside the declared allowlist or test envelope;
- audit/trace evidence or the rollback target is missing.

### Decision rule

- **PROMOTE** — all six rows pass, all negative controls reject the injected widening/drift, and rollback is bound to the exact candidate.
- **HOLD** — evidence is missing, stale, ambiguous, or a material delta lacks explicit reviewer acceptance.
- **REJECT** — a held-out control demonstrates unintended authority widening, lost deny semantics, wrong-principal binding, or an unauthorized route/peer/tool.

This card does **not** certify security, compliance, production safety, or customer outcomes. It only makes one revision's review evidence easier to inspect.

## ASSUMPTIONS

- The team already uses Kong-native declarative configuration, plan/diff, identity, gateway policy, or equivalent controls.
- "Cost / latency envelope" means a team-defined test threshold; no numeric threshold is invented here.
- The card is useful only if it reduces interpretation ambiguity; it should not duplicate an existing native or CI control.

## FALSIFIER

Discard this artifact if Kong-native tooling—or the customer's existing CI/security pipeline—already produces a low-overhead, revision-bound effective-authority regression view covering principal metadata, MCP/A2A authorization, deny/allow negative controls, model-routing expectations, trace evidence, and rollback.

## EVIDENCE_LINKS

- https://konghq.com/blog/product-releases/kong-ai-gateway-2-0-agentic-ai
- https://konghq.com/blog/product-releases/kong-identity-principals-govern-every-api-event-and-application-identity
- https://konghq.com/blog/product-releases/enterprise-grade-mcp-access-control
- https://developer.konghq.com/kongctl/declarative/
- https://developer.konghq.com/cookbooks/secure-internal-mcp-gateway/
- https://developer.konghq.com/ai-gateway/

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE

No-send draft: “I was looking at Kong’s newer agent/principal + MCP control surface and made a tiny revision-review card focused on effective-authority regressions rather than generic config diffing. If this is already solved cleanly in native Kong/CI workflows, that itself falsifies the idea; otherwise I’d value a quick critique of the six checks.”
