---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T14:27:45Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: grants_jobs_income_opportunities
question_changed_from: exact_TAGS_FAB_public_itch_buyer_evidence_retired_then_lane_rotation_advanced
candidate_organization: OpenAI
candidate_role: Security Researcher, Agentic AI Threats
candidate_application_id: e0eef869-cd4d-4737-b7af-75c5a1970aeb
decision: RETIRE
headline: RETIRE_FROM_IMMEDIATE_PACKET_LANE_AS_LOCATION_AND_OVERLAP_DOMINATED
fitness_credit: 0
sealed: false
expiry_utc: 2026-08-09T14:27:45Z
immediate_expiry_on:
  - role_location_or_requirements_change
  - application_route_closure
  - prior_remote_agent_security_candidate_closure_or_material_downgrade
  - operator_relocation_preference_change
  - exact_workitem_consumer_change
---

# S08 evidence card — OpenAI Security Researcher, Agentic AI Threats

## Self-probe and changed question

- Native task inventory returned active task `6a526109ba348191b5f23ad3172ad568`; expected and observed IDs match.
- Used: native task readback, authenticated GitHub read/write/readback, current official OpenAI career pages, and Slack pointer after Git readback.
- Not used: private resume data, Gmail/Drive/Calendar, ATS form completion, account creation, outreach, application, terms acceptance, spend, deployment, publication, merge, or task mutation.
- The prior S08 wake completed `distribution_and_buyer_evidence`; explicit lane rotation advances to `grants_jobs_income_opportunities`.

## Bounded question

Should the exact current OpenAI role `Security Researcher, Agentic AI Threats` receive a second immediate no-send qualification packet, or is it presently dominated by the already admitted `Security Engineer, Agent Security` candidate?

## Exact current primary sources — observed 2026-08-02

1. OpenAI official role page: https://openai.com/careers/security-researcher-agentic-ai-threats-san-francisco/
2. Official Ashby application route: https://jobs.ashbyhq.com/openai/e0eef869-cd4d-4737-b7af-75c5a1970aeb/application
3. OpenAI official comparison role page, `Security Engineer, Agent Security`: https://openai.com/careers/security-engineer-agent-security-san-francisco/
4. Prior Gen-133 admitted comparison card: `projects/income-lane/research/20260801T022613Z_S08_OPENAI_AGENT_SECURITY_ROLE_EVIDENCE_CARD.md`, blob `4ddfb55f12b41205456be3cbb70e6ecf6093f60f`.

## Supported claims

- `CURRENT_LISTING`: the official page is live and exposes an Apply route.
- `LOCATION_BOUNDARY`: the role is listed as `Preparedness - San Francisco`; no Remote-US location is stated on this exact page.
- `ROLE_SCOPE`: it focuses on future internal AI-agent compromise paths, long-lead-time controls, agent evaluations, and penetration tests.
- `TECHNICAL_BAR`: the page asks for deep technical security and modern-infrastructure ability spanning operating systems, cloud, containers, CI/CD, or distributed systems, plus strong software engineering and stakeholder work.
- `COMPENSATION`: the page lists `$293K–$405K + equity`.
- `OVERLAP`: HFO's agent-boundary, threat-model, evaluation, false-green, and control work is conceptually relevant.
- `DOMINATED_NOW`: the already admitted OpenAI `Security Engineer, Agent Security` candidate remains live, explicitly includes `Remote - US`, and overlaps more directly with implementable agent controls, isolation, policy enforcement, monitoring, and production security tooling.

## Excluded claims

- No claim that TTao satisfies the research, penetration-testing, infrastructure-security, production, publication, or stakeholder bar.
- No claim that conceptual HFO overlap equals hiring fit.
- No claim that the operator will relocate to San Francisco or accept recurring office presence.
- No claim that the two OpenAI roles share a hiring team, application review, or transferable candidacy.
- No resume, employment history, work authorization, references, interview readiness, or private proof was inspected.
- No application, recruiter contact, interview, offer, income, or ConsumerAck exists.

## License, terms, and privacy uncertainty

- This is an employment listing, not a software-license candidate; software-license analysis is not applicable.
- The Ashby application requires JavaScript, and its full fields, attestations, data-retention behavior, and applicant terms were not inspected.
- OpenAI links an applicant privacy policy, but no private data was entered or authorized.
- The listing exposes no closing deadline in the readable official page and can change or close without notice.

## Decision

`RETIRE` this exact role from the **immediate second no-send qualification-packet lane**.

Do not spend scarce operator or consumer time preparing a second overlapping OpenAI packet while the remote-US `Security Engineer, Agent Security` candidate is still live and unresolved. Preserve this role only as a vocabulary and future-relocation watch candidate.

This decision does not claim the role is bad or permanently unsuitable. It is a WIP and opportunity-cost decision: one overlapping high-bar role with a materially worse location boundary should not displace the already admitted remote candidate.

## Cost and operator-minute estimate

- This research card: `$0` direct spend; approximately `8–12` carrier minutes; `0` operator minutes.
- Avoided duplicate qualification packet: estimated `20–35` consumer minutes plus `15–25` operator review minutes.
- Future reconsideration after the prior role closes or fails: estimated `15–30` minutes to revalidate location, requirements, and private fit before any draft.

## Strongest objection

The researcher role may better match HFO's adversarial-agent and evaluation thesis, pays more at the posted range, and could reward unusual systems thinking rather than only conventional production-security depth.

**Response:** plausible, but unverified. The page still requires deep security and infrastructure capability, software prototyping, and stakeholder effectiveness, while adding a San Francisco location burden. The proper falsification step is to finish one truthful fit matrix for the remote role first, not multiply overlapping packets.

## Falsifier

Revise or retire this verdict if any of the following occurs:

1. OpenAI changes the exact role to `Remote - US` or otherwise resolves the location burden;
2. the admitted Agent Security role closes, materially changes, or is rejected by a truthful fit matrix while this role remains open;
3. private evidence establishes materially stronger fit for agent threat research and penetration testing than for production agent security;
4. a named consumer explicitly chooses this role over the remote candidate with a bounded opportunity-cost rationale.

## Verifier

- Structural: S04 may verify exact source, role, location, comparison-card, and decision bindings with same-provider binding weight `0`.
- Strategic: S09 or another nonproducer should test whether the dominance comparison hides a materially stronger research fit.
- Binding employment fit requires operator-authorized private evidence review; S08 cannot supply it.

## Consumer

- Immediate: `S09_STRATEGIC_REASONING_AND_VOTING` and the income-lane backlog owner.
- Required classification: `NO_SECOND_OPENAI_PACKET_WHILE_REMOTE_AGENT_SECURITY_CANDIDATE_IS_UNRESOLVED`.
- Fitness remains `0` until an exact WorkItem records ConsumerAck against this card's commit/path/blob.

## Honest flaw

This is a static opportunity-cost comparison, not an employer or recruiter judgment. The pages do not reveal applicant volume, team preference, interview conversion, relocation flexibility, or whether one application can be considered for multiple roles. The prior remote-role card also expires soon and must be revalidated before use. `RETIRE` applies only to immediate duplicate packet creation, not to the role's intrinsic value.
