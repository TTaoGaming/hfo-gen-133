---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-05T07:29:27Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: grants_jobs_income_opportunities
question_changed_from: stripe_balance_transaction_net_revenue_settlement_boundary
candidate_employer: Theori
candidate_role: Backend Software Engineer
candidate_product: Xint_autonomous_penetration_testing_framework
candidate_posting_id: e043b073-3807-4d94-9e87-0c7d7356da18
candidate_location: United_States_or_Canada_remote
candidate_employment_type: full_time
decision: REVISE
headline: REVISE_TO_PRIVATE_PRODUCTION_PYTHON_ELIGIBILITY_GATE_BEFORE_ANY_APPLICATION_PACKET
fitness_credit: 0
sealed: false
consumer: THEORI_XINT_BACKEND_PRODUCTION_PYTHON_ELIGIBILITY_GATE_001
expiry_utc: 2026-08-12T07:29:27Z
immediate_expiry_on:
  - posting closes or materially changes
  - United States or Canada location eligibility fails
  - operator cannot truthfully bind the stated professional production threshold
  - named consumer changes
---

# S08 evidence card — Theori Xint backend production-Python fit gate

## Self-probe and changed question

- Expected and observed carrier IDs match: `6a526109ba348191b5f23ad3172ad568`.
- Exposed surfaces used: authenticated GitHub branch/search/read/write/readback, public Slack read/pointer, and current public web research.
- Prior S08 wake completed `distribution_and_buyer_evidence`; explicit rotation advances to `grants_jobs_income_opportunities`.
- Repository search found no prior S08 card for this exact posting UUID.

## Bounded uncertainty

Does the current exact public portfolio justify an immediate application-packet WorkItem for Theori's Xint Backend Software Engineer role, or must the role first pass a private evidence gate for its stated production-Python threshold?

## Exact candidate and dated primary sources

Observed `2026-08-05`:

1. Theori official Ashby posting, UUID `e043b073-3807-4d94-9e87-0c7d7356da18`: https://jobs.ashbyhq.com/theori/e043b073-3807-4d94-9e87-0c7d7356da18/
2. Exact public MCP portfolio index: `TTaoGaming/mcp-notion-fast@5536b76be960540c5306f94483000d5fd92ba1fa:INDEX.md`: https://github.com/TTaoGaming/mcp-notion-fast/blob/5536b76be960540c5306f94483000d5fd92ba1fa/INDEX.md
3. AgentReleaseGate architecture: `TTaoGaming/hive-fleet-obsidian-gen-131@a1da68d8932c74d7819178fc24467dae4595b0d8:canon/adr/g131-0008-agentreleasegate-effect-integrity-microkernel.md`, blob `fd223f098c5c9949aba696c4830c44a49fd1e6fd`.
4. Python synthetic transaction gate: same commit, `projects/assurance/nonce_gate_proof/nonce_gate_demo.py`, blob `85028100b8ee7a09e54f6c2e0a781fc71cca749b`.
5. BIEI evaluation protocol: same commit, `projects/assurance/nonce_gate_proof/BIEI_SWEEP_PROTOCOL.md`, blob `9b8a72104ff97b2c9b2d699637999a01560af293`.

Exact MCP portfolio heads bound by the index receipt:

- `TTaoGaming/mcp-notion-fast@5536b76be960540c5306f94483000d5fd92ba1fa`
- `TTaoGaming/mcp-airtable-query@4420c1ba6ad000f2b09e296d24d23559ceba7588`
- `TTaoGaming/mcp-stripe-reports@730d13aaa6fe957168a4e619db2cb5aa9d233663`
- `TTaoGaming/mcp-google-calendar-batch@51214249a9a648d43687612097c0c15ae7191556`
- `TTaoGaming/mcp-trello-board-ops@d462b120a369c9cf937e89711dc873679409c5c8`
- `TTaoGaming/mcp-hubspot-crm@4f62ef2f8fa83747e530b626a523340028a5d9e3`
- `TTaoGaming/mcp-linear-issue-manager@318dad8c305f0b48e880dcf4c3454b4a6ef0578e`
- `TTaoGaming/mcp-jira-issue-manager@4d961bfce8cd47cdea726168dee951057f8aafde`

## Supported claims

- The posting is remote in the United States or Canada and concerns backend systems for Xint, an autonomous penetration-testing framework.
- The role directly values secure APIs, distributed-system reliability, data pipelines for LLM-agent workflows, testing, CI/CD, Python, asynchronous/event-driven architecture, Docker, PostgreSQL, Redis, and design-to-deployment ownership.
- The eight-server portfolio supports truthful claims of TypeScript MCP server construction, structured tool/API schemas, stdio plus Streamable HTTP transports, credential-fail-closed behavior, unit tests/CI, packaging checks, and credential-free discovery endpoints.
- The exact Python simulation supports truthful claims of implementing a local SQLite-backed reference monitor with HMAC capabilities, request/audience/version binding, expiry, nonce and effect-ID replay checks, fresh policy recheck, row-version checks, and an atomic transaction path.
- The AgentReleaseGate and BIEI artifacts support truthful discussion of agent-security threat modeling, deterministic effect mediation, idempotency/replay boundaries, adversarial evaluation design, and failure-mode analysis.

## Excluded claims

- No public proof of `5+` years of professional production-system experience.
- No public proof of production FastAPI service ownership, Redis operation, PostgreSQL operation at scale, container operations, load/performance engineering, on-call responsibility, or customer-impact incident response.
- No public proof that the exact artifacts were deployed for paying users, operated as B2B SaaS, or used in Xint, autonomous penetration testing, real-time scanning, vulnerability analysis, or offensive-security production workflows.
- No public proof of mentoring junior engineers, defining standards for a growing team, or carrying a production service from design through deployment and ongoing operation.
- The SQLite/HMAC specimen is a synthetic local simulation, not evidence of a distributed production backend.
- No application, account, upload, assessment, outreach, submission, or ConsumerAck occurred.

## License, terms, and privacy uncertainty

- The MCP index represents all eight repositories as MIT-licensed; dependency notices, provider API terms, and complete chain of title were not re-audited in this card.
- License and redistribution status for the Gen-131 architecture, simulation, and protocol were not re-audited; use them as applicant evidence links, not assumed third-party reusable components.
- Theori/Ashby privacy, retention, candidate attestation, work-authorization, background-check, and assessment terms were not inspected or accepted.
- Private employment chronology is intentionally absent and must not be inferred from public repositories.

## Decision

`REVISE` the candidate route to:

`THEORI_XINT_BACKEND_PRODUCTION_PYTHON_ELIGIBILITY_GATE_001`

Do not create an application packet from public artifacts alone. First perform one operator-controlled, truth-bound check requiring exact supportable evidence for:

1. the stated professional production-system threshold;
2. strong Python backend-service work;
3. design-to-deployment ownership;
4. credible experience with FastAPI or a comparable Python service framework, plus Redis, PostgreSQL, and Docker or clearly equivalent production systems.

If the private gate passes without invention, admit a successor application packet that uses the MCP and AgentReleaseGate work as differentiating evidence. If it fails, retire this posting rather than building a speculative demo: a new demo can strengthen stack alignment but cannot manufacture five years of professional production history.

## Cost and operator-minute estimate

- This evidence card: `$0` direct spend; approximately `12-20` carrier minutes; `0` operator minutes.
- Private eligibility gate: `10-20` operator minutes.
- Successor application packet after a pass: `30-50` consumer minutes plus `20-35` operator minutes.
- Optional FastAPI/Redis/PostgreSQL specimen: approximately `4-8` builder hours plus independent verification; `$0-$20` likely direct cost, but it does not falsify the experience-threshold gap.

## Strongest objection

The agent-security, MCP, transaction-integrity, and LLM-workflow overlap is unusually direct, so a reach application may be rational even with stack gaps.

**Response:** those artifacts are strong differentiators but do not establish the posting's explicit core threshold: professional production backend depth in Python and its named service stack. A short private truth check is cheaper and safer than spending operator time on a packet that may require unsupported claims.

## Falsifier

- `ADMIT` a successor packet if exact private chronology and project evidence truthfully establish the stated production threshold, Python backend ownership, and sufficient named-stack or equivalent experience.
- `ADMIT` with a revised threshold if Theori publishes or provides a current statement that equivalent open-source/research experience is accepted in place of the listed professional requirement.
- `RETIRE` if the posting closes, location eligibility fails, or the operator cannot support the threshold without invention.
- `REVISE` downward if the application form makes FastAPI/Redis/PostgreSQL production tenure a mandatory attestation rather than a preference.

## Verifier

- `S04_STRUCTURAL_PREFLIGHT_VERIFIER`: exact posting UUID/URL, task ID, branch, source commits/blobs, card bytes, decision, consumer, and expiry; same-provider binding weight `0`.
- `S09_STRATEGIC_REASONING_AND_VOTING`: compare expected value and operator burden against current admitted income candidates.
- Operator: verify all private chronology, production scope, authorization, and final claims; only the operator may authorize submission.

## Consumer and expiry

- Consumer: `THEORI_XINT_BACKEND_PRODUCTION_PYTHON_ELIGIBILITY_GATE_001`.
- Required result: `ELIGIBLE_FOR_TRUTH_BOUND_PACKET | RETIRE_WITH_EXACT_THRESHOLD_GAP` tied to this card's exact commit/path/blob.
- Expiry: `2026-08-12T07:29:27Z`, or immediately on a listed material change.
- Fitness remains `0` until an exact WorkItem records ConsumerAck.

## Honest flaw and effect ledger

This is a public-posting versus public-artifact assessment, not a review of the operator's private resume or complete employment history. Private production depth could materially reverse the decision. No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, or private-data use occurred.
