---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-04T00:28:55Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: distribution_and_buyer_evidence
question_changed_from: native_key_repeat_filter_before_shared_direction_command
decision: REVISE
headline: ITCH_URL_ALONE_CANNOT_SUPPLY_AGGREGATE_ENGAGEMENT_OR_BUYER_METRICS
fitness_credit: 0
expiry_utc: 2026-08-11T00:28:55Z
immediate_expiry_on:
  - itch_api_or_privacy_terms_change
  - publication_registry_binding_change
  - authorized_credential_or_project_id_binding
  - monitor_source_implementation_change
---

# S08 evidence card — itch.io aggregate metrics, authorization, and buyer-signal boundary

## Self-probe

- Identity: expected and observed carrier task IDs match: `6a526109ba348191b5f23ad3172ad568`.
- Available surfaces used: authenticated GitHub branch/issue/file/commit reads; current official itch.io documentation; authenticated GitHub immutable create and readback; authenticated Slack pointer after readback.
- Not available or not used: target monitor source path, itch.io account/API key, publisher dashboard, project page, buyer records, shell/runtime assay, account creation, terms acceptance, upload, publication, purchase, outreach, deployment, merge, or private-data access.

## Changed bounded question

For the itch.io source lane described in `TTaoGaming/hfo-gen-133` issue `#5`, can a bound public project URL alone provide trustworthy views, downloads, purchases, or earnings to the read-only external-signal monitor?

This is not a duplicate of `20260802T132906Z_S08_TAGS_FAB_ITCH_PUBLIC_BUYER_EVIDENCE_BOUNDARY_CARD.md`, which judged one simulated FAB candidate unsuitable for public publication. This card isolates the monitor transport and metric-semantics boundary after the HN and Reddit source-binding reviews.

## Exact candidate and queue binding

- Candidate system: Gen-133 external-signal monitor itch.io lane.
- Queue receipt: `TTaoGaming/hfo-gen-133` issue `#5`, observed 2026-08-04, states that the publication registry supplies no itch.io URL and that missing metrics are recorded as unknown or skipped rather than synthetic zeroes.
- Exact monitor implementation path/version: **not bound by issue #5 and not established in this run**.
- Platform interface reviewed: current itch.io modern server-side API, JavaScript API, creator dashboard/FAQ, download-key semantics, and Terms/Privacy guidance; documentation observed 2026-08-04.

## Primary sources observed 2026-08-04

1. itch.io, **Server-side API reference** — https://itch.io/docs/api/serverside
   - Analytics-bearing `profile/games` is authenticated and returns games the credential owner uploaded or can edit.
   - Its documented aggregate fields include `views_count`, `downloads_count`, `purchases_count`, and `earnings`.
   - Purchase/download-key lookups require `game:view:purchases` plus an email, user ID, or download key; these are not needed for an aggregate monitor.
   - The documented unauthenticated `wharf/latest` exception reports build version only, not traffic or purchases.

2. itch.io, **JavaScript API reference** — https://itch.io/docs/api/javascript
   - `Itch.getGameData` accepts seller username and project slug and returns basic game metadata, current price, rewards, and sale state.
   - The documented response does not include views, downloads, purchases, or earnings.

3. itch.io, **Creator FAQ** — https://itch.io/docs/creators/faq
   - Usage information such as page views, downloads, and purchases is collected and displayed to the creator.
   - Buyer-identifiable fields including email, name, IP address, country code, and transaction IDs may not be publicly shared or shared with third-party services; the documented allowed purpose is personal records and necessary bookkeeping.

4. itch.io, **Getting started / dashboard** — https://itch.io/docs/creators/getting-started
   - The publisher dashboard provides overview and detailed analytics for views, downloads, and purchases.
   - This is an owner surface, not a public-URL analytics contract.

5. itch.io, **Download keys** — https://itch.io/docs/creators/download-keys
   - A free download does not create a download key or ownership.
   - A payment creates ownership/download-key access, so raw download count must not be treated as purchase count.

6. itch.io, **Terms of Service** — https://itch.io/docs/legal/terms
   - Current page notes an April 15, 2023 update and states that terms may be amended without notice.
   - Acceptable use prohibits harvesting information about others, and publishers warrant rights to distributed content.

## Supported claims

- `MISSING_URL_IS_UNKNOWN`: with no exact itch.io publication URL, the lane must remain `UNBOUND_SOURCE_SKIPPED_OR_UNKNOWN`; absence is not zero demand.
- `PUBLIC_URL_IS_STILL_INSUFFICIENT`: username/slug can retrieve documented public metadata and price through the JavaScript API, but not aggregate views, downloads, purchases, or earnings.
- `AGGREGATE_METRICS_REQUIRE_AUTHORIZATION`: the documented analytics-bearing route is authenticated `profile/games`, scoped to projects the credential owner can edit.
- `AGGREGATE_ONLY_IS_THE_SAFE_MONITOR_SHAPE`: a monitor needs only aggregate counters and earnings totals. It must not request, persist, or project emails, names, IP addresses, country codes, transaction IDs, download keys, or per-buyer purchase records.
- `METRIC_SEMANTICS_DIFFER`: views are attention; downloads are acquisition/usage interest and may be free; purchases and realized earnings are transactional buyer evidence. None alone proves retention, satisfaction, or product-market fit.
- `PRICE_IS_NOT_DEMAND`: a public price, reward, or sale state proves an offer exists, not that anyone bought or wanted it.

## Excluded claims

- No claim that any HFO artifact currently has an itch.io page, project ID, API credential, views, downloads, purchases, earnings, or buyer.
- No claim that public page scraping is authorized, stable, or equivalent to the documented API.
- No claim that `downloads_count` means owners, customers, or revenue.
- No claim that `purchases_count` is net of refunds without an exact assay and field definition.
- No claim that aggregate metrics may be published publicly; the privacy guidance explicitly forbids sharing listed buyer-identifiable fields, while the treatment of every possible aggregate projection was not legally adjudicated here.
- No account, API, dashboard, project, or buyer-data call was performed.

## License and terms uncertainty

- The modern API documentation does not present a versioned schema contract for these fields; field behavior and terms can change.
- No existing itch.io account, already-authorized API key, credential owner, project ID, retention rule, secret-storage path, or revocation procedure was bound.
- The creator FAQ clearly prohibits sharing buyer-identifiable data with third-party services. Whether a specific internal Git/PostgreSQL aggregate projection is acceptable under every applicable privacy, processor, and account term requires operator/legal review; this card therefore requires aggregate-only minimization and forbids raw buyer fields.
- itch.io publication rights and content-quality gates remain separate from metric collection and are not stood by this card.

## Decision

`REVISE` the itch.io monitor lane.

Do not implement URL-only scraping or report zeroes. Require an exact publication URL plus an already-authorized owner credential and resolve the numeric game ID through authenticated `profile/games`. Ingest only an allowlist of aggregate fields: `views_count`, `downloads_count`, `purchases_count`, and currency/amount earnings totals. Record missing credential, missing project match, authorization failure, or absent field as typed `UNKNOWN | SKIPPED | AUTH_BLOCKED`, never as zero.

No per-buyer purchase endpoint belongs in this monitor.

## Required gate / verifier

A distinct nonproducer should run one no-write assay against an already-authorized test project and return:

1. credential identity/scopes without exposing the secret;
2. exact normalized project URL, owner/slug, numeric game ID, and response timestamp;
3. allowlisted aggregate field names and value types only;
4. proof that no buyer-identifiable or per-transaction fields entered logs, Git, Slack, or PostgreSQL;
5. typed behavior for missing URL, missing credential, 401/403, project mismatch, absent field, and rate limit;
6. a baseline and second read proving that deltas are calculated only after a sufficiently old observation;
7. a statement that views/downloads are not promoted to buyer or revenue evidence.

Required result: `STOOD | FELL`, bound to the exact monitor commit and test fixture.

## Cost and operator-minute estimate

- This evidence card: `$0` direct spend; `0` operator minutes.
- Estimated implementation after an existing credential and project are authorized: `20–45` producer minutes.
- Estimated independent verification: `15–30` minutes.
- Estimated operator work to authorize and securely bind an existing key/project: `5–15` minutes; account creation, terms acceptance, publication, and payment setup are excluded and not authorized.

## Strongest objection

A public itch.io URL and `Itch.getGameData` are enough to prove the page exists and expose price, so the monitor could proceed without credentials.

**Response:** that supports only artifact/offer presence. It does not expose the documented engagement or transaction counters that issue #5 expects. Treating page existence or price as demand would be demand invention.

## Falsifier

Revise this verdict if itch.io publishes a current official unauthenticated endpoint that returns aggregate views, downloads, purchases, or earnings for an arbitrary project URL, or if a bound monitor implementation already proves an authorized aggregate-only `profile/games` read with secret hygiene, typed failures, no private fields, and independent readback.

## Consumer

- Gate: `EXTERNAL_SIGNAL_MONITOR_ITCH_URL_CREDENTIAL_AND_METRIC_SEMANTICS_GATE_001`.
- Immediate consumers: external-signal monitor owner and `S09_STRATEGIC_REASONING_AND_VOTING`.
- Fitness remains `0` until an exact WorkItem records ConsumerAck against this card's commit/path/blob.

## Honest flaw

No authenticated itch.io response or exact monitor source file was available, so field presence and failure behavior were not executed. The findings are documentation-bound and intentionally stop short of claiming legal approval for aggregate storage or operational compatibility.