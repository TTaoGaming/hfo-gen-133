# S08 Evidence Card — Cloudflare Web Analytics distribution-signal boundary

```yaml
schema_id: hfo.gen133.research.evidence_card.v1
seat: S08
role: Research and Candidate Scout
expected_task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
observed_utc: 2026-08-03T04:29:31Z
lane: distribution_and_buyer_evidence
queue_change_basis: "GitHub issue #5 reports Cloudflare Pages request counts UNKNOWN through deployment-list and asks for a minimum source-to-table manifest. No prior Gen-133 card or C0BGNGPJFHU message matched Cloudflare Web Analytics."
question: "Can Cloudflare Web Analytics supply a bounded, no-cost distribution signal for an existing Cloudflare Pages app, and can that signal be treated as buyer evidence?"
decision: REVISE
candidate:
  product: Cloudflare Web Analytics
  integration: Cloudflare Pages one-click Web Analytics
  exact_queue_bound_site: https://demo01-handpiano.pages.dev/
  site_status_this_run: NOT_PROBED
  documentation_state: "official pages last updated 2026-04-16 through 2026-07-16"
consumer:
  primary: "TTaoGaming/hfo-gen-133#5 — External signal monitor and PostgreSQL consolidation"
  proposed_work_item: EXTERNAL_SIGNAL_MONITOR_CLOUDFLARE_WEB_ANALYTICS_READONLY_001
verifier: "S04 structural verifier or S09 product decision gate; must be distinct from producer"
expiry_utc: 2026-08-10T04:29:31Z
fitness_credit: 0
```

## Self-probe

- Identity is prompt-bound to S08 and expected task ID `6a526109ba348191b5f23ad3172ad568`; this runtime exposed no independent task-ID attestation endpoint.
- Available surfaces used: GitHub branch read/write, public Slack search/post, and public web research.
- Branch existence was verified for `agent/gen133-bootstrap-20260730`. No local checkout, Cloudflare account, token, dashboard, or private analytics data was accessed.

## Primary/current evidence

1. Cloudflare documents Web Analytics as free and available on all plans. For a Pages project, dashboard activation causes Cloudflare to inject its JavaScript beacon on the **next deployment**; valid HTML is required. Source dated 2026-04-21: https://developers.cloudflare.com/pages/how-to/web-analytics/
2. The documented high-level measures are visits, page views, page-load time, and Core Web Vitals. A visit is derived from referer/hostname behavior; a page view is a successful HTML response. Source dated 2026-04-16: https://developers.cloudflare.com/web-analytics/data-metrics/high-level-metrics/
3. Available dimensions include path, referer host/path, country, device, browser, operating system, and bot exclusion. Referer-path access is documented through the GraphQL API. Source dated 2026-04-30: https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/
4. The GraphQL Analytics API is authenticated, plan/dataset availability is dynamic, and the default user quota is 300 GraphQL queries per five minutes. Sources dated 2026-04-23: https://developers.cloudflare.com/analytics/graphql-api/ and https://developers.cloudflare.com/analytics/graphql-api/limits/ and https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/
5. Web Analytics is client-side RUM. Cloudflare documents that blockers can suppress the beacon, history is currently six months, and custom events and UTM parameters are not supported. Source current as of 2026-07: https://developers.cloudflare.com/web-analytics/faq/

## Supported claims

- **Distribution exposure:** once explicitly enabled and followed by a deployment, Web Analytics can provide aggregate visits/page views plus referrer and device segmentation for a Pages site.
- **No documented product fee:** Cloudflare describes Web Analytics as free/all-plans; this does not include operator time or any unrelated Cloudflare plan cost.
- **Automatable in principle:** the authenticated GraphQL Analytics API can support a bounded read-only collector, subject to exact account-scoped dataset discovery and permissions.
- **Privacy-minimized aggregate telemetry:** Cloudflare states the beacon does not track individual users across customer properties.

## Excluded claims

- Page views, visits, referrers, and performance metrics are **not buyer evidence**, purchase evidence, revenue, qualified lead evidence, or product-market fit.
- No public unauthenticated analytics endpoint is established. An external monitor needs account-scoped credentials or a manually exported receipt.
- This run does not establish that Web Analytics is enabled for `demo01-handpiano.pages.dev`, that any data exists, or that the exact account/free-plan GraphQL schema exposes the needed RUM dataset.
- No custom conversion event, gesture-success event, email capture, checkout, or payment signal is available from the documented Web Analytics feature.
- No claim is made that beacon counts equal all requests; blockers and client execution can produce undercounting.

## License / terms uncertainty

Cloudflare Web Analytics is a hosted service, not a FOSS dependency being admitted under a repository license. The applicable Cloudflare service/privacy terms, existing account status, token permissions, data-region implications, and any operator acceptance state were not inspected. Enabling the feature is an account configuration action and the automatic snippet appears only on a later deployment; both remain outside S08 authority.

## Cost and operator-minute estimate

- Documented incremental service price: `$0` for Web Analytics itself.
- Research run operator minutes: `0`.
- Future operator gate, only if already holding the correct Cloudflare account: approximately `5–15 minutes` to review the exact project, terms posture, enablement, and least-privilege token scope.
- Producer estimate after authorization: `30–60 minutes` to introspect the exact GraphQL schema, bind a read-only query, store provenance, and test UNKNOWN/failure handling.
- A deployment is required before automatic Pages injection takes effect; no deployment was performed or authorized here.

## Strongest objection

A page-view counter is easy to self-generate, can be undercounted by blockers, and cannot express whether a visitor successfully used hand tracking or had purchase intent. Treating it as buyer evidence would recreate the exact false-green failure the external-signal monitor is supposed to prevent.

## Falsifier

`RETIRE` this source from the automated monitor if a distinct, credentialed, read-only introspection on the exact Cloudflare account shows no accessible Web Analytics/RUM dataset for the bound Pages project and no stable export/API path exists. Broaden only if Cloudflare later documents a verifiable conversion/custom-event surface; do not infer one from visits.

## Required verifier test

1. Bind the exact Pages project and account ID without recording secrets.
2. Confirm Web Analytics enablement and the deployment/version at which the beacon became present.
3. Discover the exact GraphQL dataset and fields through authenticated introspection; record plan-dependent limits.
4. Query one fixed UTC window twice and require idempotent aggregate results or an explicit sampling delta.
5. Store `VISITS` and `PAGE_VIEWS` as `ATTENTION_SIGNAL`, never `BUYER_SIGNAL`; preserve `UNKNOWN` when access, dataset, or beacon state is absent.
6. Require a separate buyer/conversion receipt before any demand claim.

## Decision

`REVISE` — admit Cloudflare Web Analytics only as an authenticated, aggregate **distribution-attention** source for issue #5. Do not classify it as buyer evidence, and do not activate it until an operator-authorized account/deployment gate exists.

No task mutation, account creation, terms acceptance, token creation, private-data access, deployment, outreach, purchase, spend, merge, publication, or demand invention occurred.
