---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08
task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
queue_source_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_version_observed: 155
queue_experiment: X13_SLACK_PUBLIC_SEARCH_READONLY_014
bounded_uncertainty: DOES_OFFICIAL_SLACK_SEARCH_READ_PUBLIC_REQUIRE_THE_SEARCHING_USER_TO_JOIN_EACH_PUBLIC_CHANNEL
candidate: Slack.slack_search_public
candidate_schema_observed_utc: 2026-08-07T08:28:10Z
upstream_candidate: Slack Real-time Search API assistant.search.context with search:read.public
decision: REVISE
consumer: X13_SLACK_PUBLIC_SEARCH_READONLY_014_PHASE4_PUBLIC_VISIBILITY_SCOPE_GATE
verifier: S04_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_EFFECTIVE_PRINCIPAL_SCOPE_AND_CONNECTOR_TO_PROVIDER_MAPPING_WITNESS_IF_OPERATIONAL_ADOPTION_IS_REQUESTED
valid_time_utc: 2026-08-07T08:28:10Z
recorded_time_utc: 2026-08-07T08:28:10Z
expiry_utc: 2026-08-14T08:28:10Z
paid_cost_usd_observed: 0
operator_minutes_removed_measured: 0
research_minutes_estimate: 6_to_10
---

# S08 evidence card — Slack public-search channel-membership boundary

## Question

For the current X13 Slack public-search candidate, does Slack's official public-search authorization require the searching user to be a member of every public channel whose messages can appear?

## Finding — REVISE

No, not at the documented upstream `search:read.public` scope boundary. Slack's current scope documentation says `search:read.public` lets an AI-feature app search public-channel data in workspace(s) where the app is installed and the searching user is a member, and explicitly says the searching user **need not be a member of the individual public channels** for those channels to be included. Slack's Real-time Search guide repeats the same boundary. `assistant.search.context` accepts `search:read.public`, defaults `channel_types` to `public_channel`, and is the official Real-time Search method for searching messages/files/channels/users across a Slack organization.

This narrows one ambiguity in X13 v155: lack of membership in a particular public channel is not, by itself, a provider-documented reason to exclude that channel under `search:read.public`. However, the managed connector's exact provider endpoint, token type, effective scope grant, app-install workspace set, searching principal, and any additional wrapper filtering remain unexposed. Therefore this does **not** promote an empty result to workspace-wide absence.

## Supported claims

- Under Slack's current documented `search:read.public` contract, per-public-channel membership is not required for the searching user.
- The relevant upstream Real-time Search method is `assistant.search.context`, and `search:read.public` is one of its supported scopes.
- If the managed connector is in fact mapped to that method with an effective `search:read.public` grant, public-channel visibility can extend beyond channels the searching user has joined.
- X13's current `EMPTY_SUCCESS != WORKSPACE_WIDE_ABSENCE` gate should remain, but its reason should distinguish **unknown effective connector authorization/mapping/index coverage** from **per-channel membership**, which the upstream scope does not require.

## Excluded claims

- No claim that `Slack.slack_search_public` is proven to call `assistant.search.context`.
- No claim that the connector actually holds `search:read.public`, or whether it uses a bot or user token.
- No claim that every public channel in every Enterprise Grid workspace is searched.
- No claim of index completeness, snapshot semantics, freshness, ordering stability, or authoritative absence.
- No claim about private channels, MPIMs, DMs, files, archived channels, or externally shared Slack Connect visibility.
- No claim that connector wording `public channels accessible to the acting user` is semantically identical to Slack's upstream scope; that wrapper phrase may impose a narrower product-level contract.

## Primary/current sources

1. Slack Developer Docs, `search:read.public` scope, accessed 2026-08-07: https://docs.slack.dev/reference/scopes/search.read.public/
2. Slack Developer Docs, Real-time Search API usage guide, accessed 2026-08-07: https://docs.slack.dev/apis/web-api/real-time-search-api/
3. Slack Developer Docs, `assistant.search.context`, accessed 2026-08-07: https://docs.slack.dev/reference/methods/assistant.search.context/
4. Slack changelog, Real-time Search API and granular scope update, dated 2026-02-17: https://docs.slack.dev/changelog/2026/02/17/slack-mcp/
5. Slack API Terms of Service, effective 2025-10-10, accessed 2026-08-07: https://slack.com/terms-of-service/api

## License / terms uncertainty

Slack's API Terms state that API use is governed by the API Terms plus the Slack Application Developer Policy. The Real-time Search API terms prohibit background collection or scraping unrelated to user queries; for third-party application providers they also restrict persistent copies, archives, indexes, or long-term stores of other organizations' API Data. The current HFO experiment already avoids persisting raw Slack message text/links/timestamps/cursors. Applicability of the direct Slack API contract to this managed connector relationship, the actual contracting party, and connector-specific retention/processing remain unknown and are not inferred here.

## Strongest objection

The managed connector's own tool contract describes message results as coming from public channels `accessible to the acting user`. That wording could represent a deliberately narrower wrapper policy than Slack's upstream `search:read.public` capability. Without an effective-principal/scope witness and connector-to-provider mapping, the upstream scope cannot be laundered into a connector visibility guarantee.

## Falsifier

Revise or retire this card if any of the following occurs:

- Slack changes the official `search:read.public` documentation to require membership in each public channel.
- A current connector contract explicitly requires per-channel membership for `slack_search_public`.
- A same-effective-principal provider-bound witness demonstrates that the connector excludes an otherwise searchable public channel solely because the searching user is not a member.

## Verification / consumption

- **Verifier:** S04 structural preflight; for operational reliance, a distinct witness must bind the actual connector principal, effective scope, app-install workspace, and provider mapping.
- **Consumer:** `X13_SLACK_PUBLIC_SEARCH_READONLY_014_PHASE4_PUBLIC_VISIBILITY_SCOPE_GATE`.
- **Fitness:** zero until a named WorkItem or X13 phase-4 decision consumes this exact card and records ConsumerAck.

## Cost and operator burden

No Slack candidate search was executed in this scout pass. Direct spend observed: `$0`. Measured operator minutes removed: `0`. Research effort estimate: `6–10 minutes`; a provider-bound effective-scope/mapping verification is estimated at `15–30 minutes` if later authorized.

## Compact decision

`REVISE`: keep Slack public search as a bounded mutable discovery surface, and keep the no-authoritative-absence gate. Refine the scope rationale: **official `search:read.public` does not require membership in each public channel; the unresolved risk is the managed connector's effective principal/scope/provider mapping and search/index coverage.**
