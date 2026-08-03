# S08 evidence card — Anthropic Cybersecurity Products agentic-portfolio fit gate

```yaml
schema_id: hfo.gen133.s08.evidence_card.v1
observed_at_utc: 2026-08-03T15:29:46Z
seat: S08
expected_task_id: 6a526109ba348191b5f23ad3172ad568
runtime_identity_claim: HFO Gen-133 S08 Research and Candidate Scout
self_probe:
  task_id_match: true
  wip: 1
  authenticated_identity: TTaoGaming
  tools_observed:
    - GitHub read/search/write/readback
    - Slack post
    - current public web research
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: grants_jobs_income_opportunities
queue_change_basis: "The immediately prior S08 card resolved one Hacker News distribution/buyer-signal uncertainty, so explicit rotation advances to the income lane. No Gen-133 card or repository hit was found for Anthropic Greenhouse role 5063007008. Gen-133 issue #2 now exposes a dated, exact eight-server TypeScript MCP portfolio that can be compared against the role without inventing cybersecurity-product or customer evidence."
bounded_question: "Does Anthropic role 5063007008 merit one portfolio-fit WorkItem based on current agentic-product and rapid-prototyping evidence, without treating generic MCP integration demos as proof of cybersecurity product delivery, customer discovery, or research collaboration?"
decision: REVISE
classification: ANTHROPIC_CYBERSECURITY_PRODUCTS_AGENTIC_MATCH_REQUIRES_CYBER_PRODUCT_CUSTOMER_AND_LOCATION_EVIDENCE_GATE
fitness_credit: 0
fitness_condition: "Only after an exact WorkItem consumes this card and a named consumer emits ConsumerAck."
expiry_utc: 2026-08-10T15:29:46Z
```

## Exact candidate

- Employer: **Anthropic**
- Role: **Software Engineer, Cybersecurity Products**
- Official ATS role ID: `5063007008`
- Official role page: `https://job-boards.greenhouse.io/anthropic/jobs/5063007008`
- Official careers index: `https://www.anthropic.com/careers/jobs`
- Listed locations when observed: `San Francisco, CA | New York City, NY | Seattle, WA | Washington, DC`
- Listed annual salary when observed: `$320,000–$405,000 USD`
- Work pattern: Anthropic states a location-based hybrid policy expecting staff in an office at least 25% of the time; some roles may require more.
- Exact portfolio basis: `TTaoGaming/hfo-gen-133#2`, observed `2026-08-02T18:46:38Z`, binding eight public MIT TypeScript MCP servers, 82 discovered tools, stdio plus Streamable HTTP transports, tests, CI, and eight credential-free Cloudflare Worker discovery endpoints.

## Primary/current evidence

| Observed | Primary source | Material fact |
|---|---|---|
| 2026-08-03 | Anthropic official Greenhouse role page, role `5063007008` | The role builds AI-powered cybersecurity products across the stack, prototypes rapidly, collaborates with research, iterates from customer feedback, and engages customers and partners. The listing asks for 7+ years of software-engineering experience and cybersecurity-product experience; agentic-application and AI/ML product experience are additional positives. It lists no application deadline and says review is rolling. |
| 2026-08-03 | Anthropic official careers index | The exact role remained present among current Engineering & Design — Product openings. |
| 2026-08-02 | `TTaoGaming/hfo-gen-133#2` | The portfolio proves eight public integration-shaped TypeScript MCP repositories with exact heads, tests, CI, two transports, official Inspector discovery, 82 tools, and live credential-free Workers. The same receipt explicitly excludes provider-authenticated operations, customer use, publication, production hardening, and business impact. |

## Supported claims

1. The portfolio supports **rapid full-stack integration prototyping**, TypeScript service construction, agent-tool interfaces, transport packaging, CI, testing, and fail-closed credential handling.
2. Eight exact repositories are inspectable evidence of repeated implementation, not a résumé-only claim.
3. The role explicitly values AI/ML product and agentic-application experience, making one bounded fit audit rational.
4. The role remained active when checked and exposes a concrete compensation range and work-location policy.
5. The evidence is sufficient for a **gap audit**, not for an application-ready, likely-interview, or likely-hire claim.

## Excluded claims

This card does **not** establish:

- 7+ years of qualifying professional software-engineering experience;
- prior development of SIEM, EDR, threat-detection, incident-response, security-automation, or comparable cybersecurity products;
- incident response, reverse engineering, network analysis, penetration testing, or production security operations;
- collaboration with frontier-model research teams or development of new model capabilities;
- direct customer or partner discovery, rapid customer-feedback iteration, go-to-market collaboration, or product-market evidence;
- authenticated production operation, real-user traffic, hardened authorization/scopes, observability, incident ownership, or on-call support for the eight MCP servers;
- office-location feasibility, relocation willingness, work authorization, visa outcome, interview readiness, or hiring probability;
- that MCP repository count is a proxy for cybersecurity depth or customer impact.

## License / terms uncertainty

- The portfolio receipt reports MIT licensing for all eight repositories, but this run did not re-audit every dependency, notice, generated artifact, or hosted-service term at each exact head.
- The employment listing is not a software-license offer. Applicant privacy terms, candidate AI-use policy, screening terms, relocation terms, and employment terms were not accepted or fully reviewed.
- The role page exposes a voluntary application surface and private eligibility questions. No private operator data was consulted, inferred, entered, or externalized.
- Salary, location, policy, and availability can change without notice; expiry is seven days.

## Strongest objection

The role's center of gravity is not generic agent integration. It is senior cybersecurity-product judgment under customer and research feedback: Anthropic explicitly asks about prior cybersecurity products and 7+ years of professional engineering, while the current Gen-133 receipt proves integration demos but explicitly lacks authenticated production operation, customer use, and business impact. The 25%-office policy is a separate unresolved feasibility gate. Promoting this candidate directly to application-ready would be false green.

## Falsifier

Retire this candidate before consumption if any of the following is independently confirmed:

1. role ID `5063007008` disappears from Anthropic's official careers index or closes;
2. office-location, relocation, or work-authorization constraints fail;
3. an exact evidence audit finds no defensible prior cybersecurity-product or security-operations evidence and no adjacent evidence strong enough to state transparently;
4. the seven-plus-year experience gate is not satisfied and the consumer rejects equivalent evidence;
5. the role materially changes away from rapid AI-security product prototyping.

Promote from `REVISE` to `ADMIT` only after an independent audit binds exact pre-existing receipts for: (a) professional experience duration; (b) at least one cybersecurity product, security automation, incident-response, red-team, or comparable security artifact/outcome; (c) one customer/user feedback or cross-functional product iteration; and (d) location feasibility. A newly fabricated demo cannot substitute for prior professional or customer evidence.

## Cost and operator-minute estimate

```yaml
research_run:
  surfaced_external_cost_usd: 0
  operator_minutes: 0
  estimated_agent_minutes: 18
successor_fit_audit:
  estimated_agent_minutes: 35-60
  estimated_operator_minutes: 0-15
  operator_minutes_are_only_for: "confirming private employment history/location constraints or a later explicit apply/no-apply decision"
application_or_outreach_performed: false
```

## Route

```yaml
proposed_work_item: ANTHROPIC_CYBERSECURITY_PRODUCTS_2026_PORTFOLIO_FIT_GATE_001
consumer:
  - S09_PRODUCT_DECISION_QUEUE
  - projects/income-lane owner
verifier: "independent non-S08 reviewer; preferred S04 structural verifier or S09 decision seat"
next_safe_action: "Audit existing Git and operator-approved public evidence for professional duration, cybersecurity products/security automation, customer-feedback iteration, research collaboration, and location feasibility. Bind exact receipts and explicit gaps; do not create claims from MCP server count."
consumer_ack_required: true
```

## No-effect receipt

No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, private-data use, or demand invention occurred.