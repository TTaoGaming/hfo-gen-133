# S08 Evidence Card — GitHub release download count is acquisition, not buyer evidence

```yaml
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
task_id_expected: 6a526109ba348191b5f23ad3172ad568
observed_utc: 2026-08-04T15:30:45Z
lane: distribution_and_buyer_evidence
question: Can GitHub Release asset download_count be admitted as buyer, customer, install, or demand evidence for the Gen-133 external-signal monitor and DLC/FOSS distribution lane?
decision: REVISE
candidate:
  provider: GitHub
  surface: REST API
  api_version: 2026-03-10
  endpoint: GET /repos/{owner}/{repo}/releases/{release_id}/assets
  field: download_count
consumer: EXTERNAL_SIGNAL_MONITOR_GITHUB_RELEASE_DOWNLOAD_SEMANTICS_GATE_001
verifier: DISTINCT_RAW_GITHUB_API_WITNESS
expiry_utc: 2026-08-11T15:30:45Z
cost_usd_this_run: 0
operator_minutes_this_run: 0
estimated_revision_minutes: 15-30
estimated_verification_minutes: 10-20
```

## Bounded finding

GitHub's current Release Assets REST schema exposes an aggregate numeric `download_count` for each release asset. The same object exposes asset identity, filename, content type, size, digest, timestamps, state, uploader, and download URL. It does **not** expose a unique-downloader count, buyer identity, payment state, successful installation, activation, retention, or application outcome.

GitHub separately documents repository traffic as full clones, visitors, referring sites, and popular content. That traffic is limited to the previous 14 days, requires push/write access, and uses aggregate views/unique visitors rather than commercial outcome fields. Release-asset counts and repository traffic therefore belong below buyer evidence in the signal ladder.

## Supported claims

- `download_count` is an aggregate release-asset download metric returned by GitHub's release APIs.
- Public release information and public release-asset listings can be retrieved without authentication.
- Repository traffic can provide full-clone, visitor, referrer, and popular-content observations for the last 14 days when the caller has repository write access.
- A release-asset count can be retained as an `ACQUISITION_EVENT_COUNT` or `DISTRIBUTION_EVENT_COUNT` observation when bound to exact repository, release ID, asset ID/name/digest, API version, and observation time.

## Excluded claims

The metric alone does not support any of the following:

- unique people or organizations;
- buyers, customers, leads, qualified prospects, or product-market fit;
- payment, revenue, conversion, retention, activation, or successful installation;
- one download per person or one person per download;
- causal attribution to a campaign, referrer, landing page, or offer;
- absence of demand when the count is zero.

The exclusion is an inference from the official response schema and traffic documentation: GitHub exposes no field that binds a release download to purchase, installation, uniqueness, or downstream use.

## Required revision

1. Name the metric `github_release_asset_download_events`, not `buyers`, `users`, `customers`, or `installs`.
2. Bind every observation to exact `repository_full_name`, `release_id`, `asset_id`, `asset_name`, asset digest when present, `published_at`, observation UTC, and pinned API version `2026-03-10`.
3. Preserve it in the `ACQUISITION` tier, below verified conversations, qualified leads, orders, payments, and retained use.
4. Never sum counts across replaced/re-uploaded assets without preserving asset identity; filename reuse and asset replacement can break naive continuity.
5. Keep GitHub traffic metrics separately typed and preserve their 14-day retention/access boundary.
6. Treat missing release, missing asset, missing permission, pagination failure, or ambiguous asset replacement as typed `UNKNOWN`, not zero.
7. Require an independent raw API witness before the monitor claims a working release-download lane.

## License and terms uncertainty

No third-party source-code license is implicated by this metric classification. GitHub API and platform terms, abuse controls, and rate limits still apply and were not separately audited in this run. The release-asset list endpoint is documented as readable without authentication for public resources; repository traffic requires write access. No credential, private repository, or private analytics data was accessed.

## Strongest objection

For a free downloadable product, download events may be the fastest practical adoption proxy and can be more useful than stars or page views.

**Response:** admit the metric as acquisition evidence. Do not promote it to buyer, install, or retained-use evidence without an independent downstream receipt such as a payment event, explicit opt-in, verified install/activation telemetry, support interaction, or user-confirmed outcome.

## Falsifier

Retire or revise this card if GitHub's official API adds and documents a field that reliably identifies unique downloaders, successful installs/activations, or purchase-linked release consumption, or if a distinct verifier shows that the current `2026-03-10` schema already exposes such semantics.

## Primary sources observed 2026-08-04

1. GitHub Docs, **REST API endpoints for release assets**, API version `2026-03-10`: release-asset schema and `download_count`; public-resource authentication boundary. https://docs.github.com/en/rest/releases/assets?apiVersion=2026-03-10
2. GitHub Docs, **REST API endpoints for releases**, API version `2026-03-10`: release objects include assets and aggregate download counts. https://docs.github.com/en/rest/releases/releases?apiVersion=2026-03-10
3. GitHub Docs, **Viewing traffic to a repository**: full clones, visitors, referrers, popular content, 14-day window, update cadence, and access boundary. https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository?apiVersion=2026-03-10
4. GitHub Docs, **API Versions**: `2026-03-10` is current; `2022-11-28` remains supported and is the default when the version header is omitted. https://docs.github.com/en/rest/about-the-rest-api/api-versions?apiVersion=2026-03-10

## Fitness boundary

This card earns zero fitness until an exact WorkItem consumes the classification and a distinct verifier returns a bound verdict. No API request, credential access, private-data use, release creation, upload, publication, deployment, purchase, outreach, account action, task mutation, merge, or spend occurred.
