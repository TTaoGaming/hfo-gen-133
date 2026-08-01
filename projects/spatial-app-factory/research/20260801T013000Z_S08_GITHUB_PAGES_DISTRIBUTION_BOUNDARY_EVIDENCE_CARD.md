---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_GITHUB_PAGES_DISTRIBUTION_BOUNDARY_20260801T013000Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T01:30:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
work_item_id: SPATIAL_FACTORY_GOLDEN_APP_001
research_lane: distribution_and_buyer_evidence
candidate_capability: GitHub Pages
candidate_contract_version: official_docs_observed_2026-08-01_and_terms_effective_2026-04-27
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
expiry_utc: 2026-08-08T00:00:00Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_provider_nonproducer
consumers:
  - Olrun/Claude-Dispatch_as_spatial_factory_coordinator
  - S09_task_6a539fb148bc8191a30b6009dbf22438
sealed: false
---

# S08 evidence card — GitHub Pages is a later public demo surface, not the current internal QA or commercial runtime

## Changed queue evidence

The prior S08 interaction-contract card at commit `e5b9a6299caae7336d1c78a036854f74494deb47` was consumed into the renewed claim and revised execution contract. The live claim is now:

- claim commit: `47cd1e8bfb7cf78651e8978f4dec1f5e2a76bad4`
- claim path: `projects/spatial-app-factory/claims/20260801T000607Z_SPATIAL_FACTORY_GOLDEN_APP_001_S02_RENEWED.claim.yaml`
- claim blob: `f90e3797b4e5aa398aa386e555e26b53ae27cfc5`
- target: `TTaoGaming/TAGS@1271e25306fe8ef8baea32704cf022435703d498`
- candidate page: `prototypes/fab-prototype.html`
- current ceiling: branch/file/test only; deployment and publication forbidden

The explicit lane rotation therefore advances from interaction/input adapters to one bounded distribution uncertainty.

## Bounded question

After the internal golden-app branch is independently verified, can GitHub Pages serve the exact static HTML/CSS/JavaScript artifact as a zero-incremental-cost buyer-facing demo without creating false assumptions about privacy, commercial hosting, license clearance, or current publication authority?

## Decision

`REVISE` the distribution plan.

GitHub Pages is technically suitable for a later **public, non-sensitive project/demo site** containing static HTML, CSS, and JavaScript. It is not an internal/private preview by default, not evidence of buyer demand, not a rights-clearance mechanism, and not an allowed host for an online business, e-commerce site, or commercial SaaS runtime under the published Pages limits. The current WorkItem must remain no-deploy/no-publication.

Do not select or configure Pages inside `SPATIAL_FACTORY_GOLDEN_APP_001`. After a distinct `STOOD` and explicit Olrun ConsumerAck, a separate operator-authorized packaging WorkItem may evaluate a public demo-only deployment.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: read_write
  slack: read_write
  web_primary_docs: read
  shell_or_browser_runtime: unavailable
  native_task_mutation: not_called
```

## Primary/current sources — observed 2026-08-01

1. GitHub Docs, "What is GitHub Pages?": Pages hosts static HTML, CSS, and JavaScript directly from a repository and supports project sites. https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
2. GitHub Docs, "Configuring a publishing source": Pages can publish from a branch root, a `/docs` folder, or GitHub Actions; published sites are public even when the repository is private unless a separate supported access-control tier is used. https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
3. GitHub Enterprise Cloud Docs, "Changing the visibility of your GitHub Pages site": private Pages access control requires an organization using GitHub Enterprise Cloud. https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site
4. GitHub Docs, "Securing your GitHub Pages site with HTTPS": `github.io` Pages sites support HTTPS; Pages should not handle sensitive transactions. https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
5. GitHub Docs, "GitHub Pages limits": Pages is not intended or allowed as free hosting for an online business, e-commerce site, or commercial SaaS; documented limits include a 1 GB site, 10-minute deployment timeout, soft 100 GB/month bandwidth, and soft 10 builds/hour for branch publishing. https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
6. GitHub Terms of Service, effective 2026-04-27: public repository content is public, users remain responsible for rights and licenses, and public repository content may be viewed and forked through GitHub functionality. https://docs.github.com/en/site-policy/github-terms/github-terms-of-service

## Supported claims

- The current dependency-free FAB candidate is structurally compatible with static hosting if its entry path and relative asset paths are packaged correctly.
- A later demo can publish from a dedicated branch/folder or an Actions artifact; either choice is a deployment/publication effect requiring separate authority.
- HTTPS is available for Pages, but HTTPS does not make the site private.
- A private repository does not by itself create a private Pages preview. Private Pages access control is an Enterprise Cloud organization capability, not a safe default for this personal/project lane.
- Pages can support a public project demonstration or documentation surface after exact license/provenance clearance.
- Incremental service cost may be `$0` for an eligible existing account and public-repository path, but private Actions usage and account-plan constraints must be read back before any cost claim.
- The current card supplies no demand evidence. A public URL, page view, or successful deployment would still not prove a buyer, willingness to pay, conversion, or product-market fit.

## Excluded claims

- No claim that Pages is private, access-controlled, or appropriate for confidential customer testing.
- No claim that Pages permits hosting the commercial SaaS/product runtime envisioned for future spatial applications.
- No claim that publishing from a private repository keeps the deployed bytes private.
- No claim that GitHub Pages clears the missing exact license/provenance gate for the pinned TAGS prototype.
- No claim that existing GitHub plan, Actions minutes, organization type, repository visibility, or Pages settings were inspected or changed.
- No claim that the target branch builds, routes correctly under a project-site subpath, or works in a browser.
- No buyer demand, traffic, conversion, accessibility, browser compatibility, deployment, publication, or ConsumerAck is established.

## License and terms uncertainty

The prior S08 card found `package.json` declared MIT but no root `LICENSE` file at the pinned target revision. Public distribution remains blocked until exact license text, copyright ownership/provenance, third-party asset status, and distribution rights are bound to the producer SHA and independently reviewed.

GitHub's service terms do not grant missing rights to project content. Public repository and Pages publication can expose content broadly and may permit viewing/forking through GitHub functionality. That exposure is a publication effect, not a reversible internal test.

## Cost and operator burden

```yaml
direct_research_cost_usd: 0
new_credentials_required_now: 0
operator_minutes_required_now: 0
estimated_future_pages_configuration_minutes: 5_to_10
estimated_future_license_and_publication_review_minutes: 15_to_30
estimated_operator_minutes_avoided_by_preselecting_boundary: 10_to_20
cost_uncertainty: existing_plan_repository_visibility_and_private_actions_usage_not_read_back
```

## Strongest objection

The best next distribution surface may not be GitHub Pages at all. Pages is public by default and explicitly unsuitable as a commercial SaaS host. Choosing it early can create a misleading "launch" artifact while the actual bottlenecks remain independent browser verification, provenance, buyer definition, and a permitted commercial delivery channel.

## Falsifier

Revise this result only if current official GitHub terms/documentation or a direct account readback proves all of the following for the exact intended use:

1. access control is available on the already-authorized account without a new paid plan or account change;
2. the proposed commercial behavior is permitted under Pages-specific limits;
3. exact license/provenance is cleared for the producer SHA;
4. a distinct browser verifier confirms the packaged project-site path and native fallback;
5. a named buyer experiment defines a measurable action stronger than page views.

Immediate `RETIRE` conditions for Pages in this lane:

- any private or sensitive data would be included;
- the site would collect passwords, payment details, policy data, or other sensitive transactions;
- Pages would be used as the commercial SaaS runtime rather than a project/demo surface;
- publication is attempted before operator authority, rights clearance, distinct `STOOD`, and ConsumerAck;
- success is declared from deployment, traffic, or a public URL without a buyer action.

## Reversible next experiment

After the existing WorkItem closes `STOOD_AND_ACKED`, create at most one separate no-publication packaging specimen that computes the static file manifest and project-site-relative paths locally. Do not enable Pages. The held-out gate is: all required files resolve under `/<repository-name>/` without network dependencies, while the publication action remains disabled.

## Consumer action and credit rule

Olrun should consume this card only to preserve the current no-publication boundary and to decide whether a later demo-packaging WorkItem is warranted. S09 may adversarially vote on Pages versus another demo-only channel after code/browser/provenance evidence exists.

This card earns no primary fitness until a named WorkItem explicitly records `CONSUMED` or `REJECTED_WITH_EVIDENCE` against this exact card digest. It must not create a second production WIP while `SPATIAL_FACTORY_GOLDEN_APP_001` remains open.

## Honest flaw

This carrier reviewed current official GitHub documentation and terms but did not inspect the account's Pages settings, billing tier, organization type, repository visibility, Actions quota, DNS, target runtime, or browser behavior. It produced no buyer interview, usage telemetry, pricing evidence, deployment, publication, or independent verification. GitHub documentation can change; the card expires unless revalidated.