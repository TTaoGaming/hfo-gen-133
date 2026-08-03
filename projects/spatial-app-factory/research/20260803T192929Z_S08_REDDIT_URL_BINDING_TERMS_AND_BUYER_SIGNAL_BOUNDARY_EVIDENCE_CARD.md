---
schema_id: hfo.gen133.s08.evidence_card.v1
generation: 133
seat: S08
task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
lane: distribution_and_buyer_evidence
question: Can the current Reddit lane bind a standing artifact URL to Reddit posts and interpret returned metrics without inventing demand or crossing current API terms?
decision: REVISE
observed_utc: 2026-08-03T19:29:29Z
expiry_utc: 2026-08-10T19:29:29Z
canonical_repo: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
queue_source: https://github.com/TTaoGaming/hfo-gen-133/issues/5
consumer: EXTERNAL_SIGNAL_MONITOR_REDDIT_URL_BINDING_TERMS_AND_METRIC_SEMANTICS_GATE_001
fitness_credit: 0
privacy_class: PUBLIC_SOURCE_METADATA_ONLY
world_effect_ceiling: GIT_RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
sealed: false
---

# S08 evidence card — Reddit URL binding, terms, and buyer-signal boundary

## Bounded uncertainty

Gen-133 issue #5 says a Reddit source lane is implemented, but the publication registry supplies no Reddit URLs. The bounded question is whether an exact artifact URL can be bound to Reddit post identifiers and which claims may be made from the resulting public post fields. This card does not review the monitor implementation, credentials, accepted terms, raw response schema, rate-limit behavior, or any private Reddit data.

## Exact candidate and current sources

| item | exact candidate / version | dated primary source | supported observation |
|---|---|---|---|
| URL lookup surface | Reddit legacy Data API `GET [/r/subreddit]/api/info`, `url=<valid URL>` | Reddit API documentation, accessed 2026-08-03: https://www.reddit.com/dev/api | The documented read endpoint accepts a valid `url` query parameter and returns a listing. This is a candidate exact-URL binding path, not proof of canonicalization, completeness, or visibility. |
| post fields | Reddit Developer Platform `Post`, `@devvit/public-api v0.13.8-dev` | Reddit for Developers, accessed 2026-08-03: https://developers.reddit.com/docs/api/redditapi/models/classes/Post | The current model exposes `id`, `permalink`, `url`, `score`, `numberOfComments`, removal/quarantine state, and related metadata. |
| Data API contract | Data API Terms, effective 2023-06-19, last revised 2026-07-20 | https://redditinc.com/policies/data-api-terms | API access requires identifying information, authorized access information such as OAuth, compliance with limits, purpose-bounded retention, and deletion of data no longer required. Commercial use or other unpermitted use may require a separate agreement. |
| developer contract | Developer Terms, effective 2024-09-24, last revised 2026-03-24 | https://redditinc.com/policies/developer-terms | Access constitutes agreement; commercial use is restricted absent express permission or a separate agreement, and privacy, retention, deletion, and security duties apply. |
| queue fact | Gen-133 issue #5, updated 2026-08-02 | https://github.com/TTaoGaming/hfo-gen-133/issues/5 | Reddit is listed as an implemented source lane, but the publication registry currently has no Reddit URLs. |

## Supported claims

1. Reddit documents one read endpoint with a valid-URL parameter, so the lane does not need to treat external-URL binding as categorically impossible.
2. A successful response may be normalized only after binding each returned object to an exact Reddit `id`, `permalink`, and returned `url`.
3. `score` may be stored as a Reddit platform-attention/ranking proxy. `numberOfComments` may be stored as a discussion-volume proxy.
4. With no registry URL, the correct state is `UNBOUND_SOURCE_SKIPPED_OR_UNKNOWN`, not zero posts, zero attention, zero discussion, or zero demand.
5. Removed, deleted, spammed, quarantined, inaccessible, or otherwise visibility-limited posts require explicit status or `UNKNOWN`; they must not silently become zero.

## Excluded claims

This evidence does **not** support any claim of:

- buyer identity, qualified lead, purchase intent, conversion, revenue, retention, willingness to pay, or product-market fit;
- exhaustive discovery of every Reddit post, crosspost, duplicate, comment mention, or URL variant;
- canonical-equivalence across redirects, tracking parameters, fragments, host aliases, HTTP/HTTPS variants, or historical URL changes;
- authoritative absence when the endpoint returns no visible result;
- current API authorization, approved use case, accepted terms, commercial permission, quota, rate-limit headroom, or monetary price;
- implementation correctness, raw API parity, deterministic retries, durable ingestion, or threshold validity.

## Required revision

The Reddit worker should remain disabled or skipped until all of the following are bound:

1. A publication-registry row supplies one exact source URL and immutable artifact identity.
2. An already-authorized Reddit identity and approved use case are documented; this WorkItem must not create an account, register an app, accept terms, or seek commercial approval.
3. One no-retry read-only assay calls `GET /api/info` with the exact URL and records only the minimum fields: returned `id`, `permalink`, `url`, `score`, `numberOfComments`, visibility/removal state, observation time, and pagination metadata if exposed.
4. URL normalization is deterministic and preserves both the source URL and every attempted normalized variant. Multiple returned posts are separate observations, not one summed buyer signal.
5. Metrics remain typed as `PLATFORM_ATTENTION_PROXY` and `DISCUSSION_VOLUME_PROXY`; promotion to buyer evidence requires a separate commercial receipt.
6. Retention and deletion rules are represented in the schema before any Reddit data is persisted.

## License / terms uncertainty

There is no FOSS license question for this API surface. Contractual permission is the blocker. The current Data API Terms say commercial-purpose use may require a separate agreement, and the Developer Terms restrict business/monetized use unless expressly permitted or approved. Whether the Gen-133 monitor's income-fitness use is an approved noncommercial internal use, a restricted commercial use, or covered by an existing agreement is `UNKNOWN`. Existing app registration, OAuth principal, accepted revision, approved use case, data-retention policy, and deletion mechanism are also `UNKNOWN`.

## Cost and operator-minute estimate

- This research pass: surfaced external spend `$0`; operator minutes consumed `0`; no Reddit API call executed.
- Proposed implementation revision: `30–60` producer minutes for URL binding, normalization, typed metrics, and retention fields.
- Distinct verification: `20–40` minutes for one authorized exact-URL assay and raw/normalized parity review.
- Reddit API monetary cost and any commercial-agreement cost: `UNKNOWN`.

## Strongest objection

A URL-parameter endpoint is not a discovery guarantee. The same artifact may appear through redirects, UTM variants, mirrors, crossposts, text mentions, deleted posts, private/quarantined communities, or multiple submissions. A clean zero response can therefore be false-negative evidence even when the call and credentials are valid.

## Falsifier

`RETIRE` the proposed URL-binding path if current official documentation removes the `url` parameter, an authorized known-positive exact submitted URL cannot be bound to its expected Reddit post ID/permalink, or Reddit confirms that the intended Gen-133 use requires an unavailable commercial agreement. `REVISE` further if normalization changes which post set is returned or duplicates cannot be deterministically separated.

## Verifier

A distinct verifier using an already-authorized Reddit principal should perform exactly one known-positive, read-only, no-retry assay; retain a sanitized digest of request parameters and raw response bytes; recompute the normalized record; and issue `STOOD | FELL` bound to the exact source URL, post IDs, terms revision, response digest, and schema version. Same-provider S08 review has binding weight zero.

## Consumer, expiry, and decision

- Consumer: `EXTERNAL_SIGNAL_MONITOR_REDDIT_URL_BINDING_TERMS_AND_METRIC_SEMANTICS_GATE_001`, routed through issue #5 / the external-signal monitor owner.
- Expiry: `2026-08-10T19:29:29Z`, or immediately upon Reddit API/terms revision or publication-registry change.
- Decision: `REVISE`.
- Fitness: `0` until an exact WorkItem consumes this card, a distinct verifier returns a source-bound verdict, and the named consumer acknowledges the resulting gate.

## Actions not taken

No Reddit API call, account or app registration, OAuth action, terms acceptance, publication, outreach, vote, comment, private-data use, purchase, spend, deployment, merge, task mutation, or demand claim occurred.
