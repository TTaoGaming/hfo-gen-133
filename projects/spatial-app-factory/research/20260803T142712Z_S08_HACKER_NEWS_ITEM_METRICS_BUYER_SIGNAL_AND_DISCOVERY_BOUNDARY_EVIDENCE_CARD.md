# S08 Evidence Card — Hacker News Item Metrics Buyer-Signal and Discovery Boundary

- `seat`: `S08_RESEARCH_AND_CANDIDATE_SCOUT`
- `carrier_task_id_expected`: `6a526109ba348191b5f23ad3172ad568`
- `carrier_task_id_observed`: `6a526109ba348191b5f23ad3172ad568`
- `task_id_match`: `TRUE`
- `self_probe_tools_observed`: `GITHUB_READ_WRITE, SLACK_READ_WRITE, PUBLIC_WEB_RESEARCH`
- `valid_time`: `2026-08-03T14:27:12Z`
- `transaction_time`: `GIT_COMMIT_TIME`
- `canonical_repository`: `TTaoGaming/hfo-gen-133`
- `canonical_branch`: `agent/gen133-bootstrap-20260730`
- `lane`: `DISTRIBUTION_AND_BUYER_EVIDENCE`
- `wip`: `1`
- `decision`: `REVISE`

## Changed bounded question

The prior S08 wake closed one interaction/input-adapter uncertainty for Hextris. The explicit lane rotation therefore advances to distribution and buyer evidence. Gen-133 issue #5 says a Hacker News source lane is implemented but the publication registry supplies no Hacker News URLs. What evidence contract is admissible for that lane when no canonical Hacker News item ID is bound, and can Hacker News `score` or comment counts be promoted to buyer evidence?

This card investigates only that source-binding and metric-semantics uncertainty. It does not inspect or execute the monitor implementation.

## Exact candidate and queue binding

- `candidate_id`: `EXTERNAL_SIGNAL_MONITOR_HACKER_NEWS_PUBLIC_ITEM_METRICS_001`
- `queue_source`: `TTaoGaming/hfo-gen-133#5`
- `queue_source_url`: `https://github.com/TTaoGaming/hfo-gen-133/issues/5`
- `candidate_repository`: `TTaoGaming/hfo-gen-133`
- `candidate_branch`: `agent/gen133-bootstrap-20260730`
- `implementation_path`: `UNKNOWN`
- `implementation_commit`: `UNKNOWN`
- `publication_registry_path_and_blob`: `UNKNOWN`
- `bound_hacker_news_item_ids`: `NONE_ESTABLISHED_BY_QUEUE_SOURCE`
- `official_api_repository`: `HackerNews/API`
- `official_api_repository_commit`: `8a0528f538bca407c2ceeeefc9bee48bdb99c1c8`
- `official_api_version`: `v0`
- `official_item_endpoint_shape`: `https://hacker-news.firebaseio.com/v0/item/<id>.json`

Issue #5 establishes that a lane exists and that the registry currently supplies no Hacker News URLs. It does not bind the lane bytes, exact discovery method, item IDs, raw schema, baseline, threshold logic, or downstream promotion rules.

## Current primary sources

Accessed `2026-08-03`:

1. Official Hacker News API repository and README at exact commit: `https://github.com/HackerNews/API/tree/8a0528f538bca407c2ceeeefc9bee48bdb99c1c8`
2. Official Hacker News API README: `https://github.com/HackerNews/API/blob/8a0528f538bca407c2ceeeefc9bee48bdb99c1c8/README.md`
3. Official Hacker News API repository license: `https://github.com/HackerNews/API/blob/8a0528f538bca407c2ceeeefc9bee48bdb99c1c8/LICENSE`
4. Hacker News Guidelines: `https://news.ycombinator.com/newsguidelines.html`

## Supported claims

- The official public API is versioned under `/v0/` and exposes Hacker News items by unique integer ID.
- Story items can expose `url`, `score`, `descendants`, `kids`, `dead`, `deleted`, author, title, and creation time.
- The official field contract defines `score` as the story score and `descendants` as the total comment count for stories or polls.
- The API exposes top, new, and best story-ID lists, each capped at up to 500 items. The official contract does not document a direct search endpoint by external publication URL.
- Therefore, a monitor with neither a canonical Hacker News item ID nor a bounded, explicitly defined discovery result cannot claim that a matching Hacker News submission was observed or absent. The safe result is `UNBOUND_SOURCE_SKIPPED_OR_UNKNOWN`, not numeric zero.
- When an exact item ID is bound, `score` can be retained as `HACKER_NEWS_COMMUNITY_ATTENTION_SIGNAL` and `descendants` as `HACKER_NEWS_DISCUSSION_VOLUME_SIGNAL` with item ID, story URL, collection time, and `dead` or `deleted` state.
- The Hacker News Guidelines permit some posting of one's own work but prohibit using HN primarily for promotion and prohibit soliciting upvotes, comments, or submissions. This evidence card admits read-only monitoring only; it grants no publication or engagement authority.

## Required source and signal classes

- missing HN item ID or canonical HN item URL → `UNBOUND_SOURCE_SKIPPED_OR_UNKNOWN`
- item endpoint returns no item → `NO_ITEM_RETURNED_FOR_BOUND_ID_AT_OBSERVATION_TIME`
- `score` → `HACKER_NEWS_COMMUNITY_ATTENTION_SIGNAL`
- `descendants` → `HACKER_NEWS_DISCUSSION_VOLUME_SIGNAL`
- `dead=true` or `deleted=true` → `HACKER_NEWS_ITEM_STATE_FLAG`

None of these classes may be promoted to `BUYER_SIGNAL`, `QUALIFIED_LEAD`, `CONVERSION`, `REVENUE`, or `PRODUCT_MARKET_FIT` without a separate source-bound commercial receipt.

## Excluded claims

This evidence does not support:

- buyer identity, purchase intent, qualified lead, contract, payment, revenue, retained customer, product-market fit, or successful distribution;
- treating score and comment count as independent commercial corroboration;
- interpreting zero, low, dead, deleted, or missing metrics as absence of demand;
- claiming complete HN discovery from top, new, or best lists, which are bounded current lists rather than a URL-search index;
- claiming that a story URL uniquely identifies one HN submission without binding the item ID;
- claiming ranking position, front-page duration, impressions, click-throughs, referral traffic, or conversions from the item fields alone;
- automated posting, reposting, account creation, vote solicitation, comment solicitation, or promotional engagement;
- storing or interpreting comment text as buyer intent under this metric-only WorkItem.

## License and terms uncertainty

- `HackerNews/API@8a0528f538bca407c2ceeeefc9bee48bdb99c1c8` carries an MIT license for the repository software and documentation, with the 2025 Y Combinator Hacker News notice preserved.
- That repository license does not by itself resolve rights to retain, republish, enrich, or commercially analyze Hacker News user content, usernames, comments, or platform data.
- The README currently says there is no rate limit, but this is not a durability, availability, abuse-tolerance, or future-policy guarantee.
- The exact monitor's compliance with Hacker News, Y Combinator, Firebase, privacy, retention, and attribution terms remains `UNKNOWN` because no implementation, request pattern, or stored schema was inspected.
- No account action, terms acceptance, publication, vote, comment, outreach, or API purchase occurred in this research pass.

## Cost and operator-minute estimate

- `external_spend_measured`: `$0`
- `operator_minutes_measured`: `0`
- `research_carrier_minutes`: `NOT_EXPOSED`
- `smallest_producer_revision_estimate`: `15–30 minutes` to require a canonical HN item ID, add typed metric classes, persist item-state flags, and emit explicit skip/unknown when unbound.
- `distinct_verifier_estimate`: `10–20 minutes` for one exact item-ID raw endpoint or authorized UI readback and source-to-row comparison.
- `official_api_price`: `NO_PUBLISHED_PER_CALL_PRICE_IN_BOUND_SOURCE`

Estimates are not measured savings or completed work.

## Strongest objection

High Hacker News scores and active comment threads can produce material traffic, customer conversations, and commercial outcomes, so classifying them only as attention or discussion may understate their value.

## Response to objection

Retain the signals; do not launder their semantics. A score or comment count is useful top-of-funnel evidence, but the API fields contain no purchase, contract, payment, or attributable conversion. A separate publication-bound referral, signup, qualified contact, checkout, contract, or payment receipt may establish commercial evidence without retroactively changing what HN score and descendants mean.

## Falsifier

This `REVISE` decision is falsified for the implementation gate if exact monitor bytes and raw readback show all of the following:

1. each observation is bound to an exact HN item ID, story URL, collection time, and API version;
2. absence of an item ID produces explicit skip/unknown rather than zero demand;
3. `score`, `descendants`, and item-state flags retain separate non-buyer classes;
4. bounded discovery, if any, declares its finite search surface and cannot claim completeness;
5. threshold logic cannot promote HN metrics to buyer, revenue, or product-market-fit status;
6. no posting, engagement, account, vote, or comment effect is authorized by the monitor;
7. one named consumer acknowledges and uses the typed observation in an exact WorkItem.

A separate source-bound conversion or commercial receipt can independently create buyer evidence; it does not falsify the metric semantics above.

## Verifier, consumer, expiry

- `structural_verifier`: `S04_STRUCTURAL_PREFLIGHT` for exact monitor path, item-ID binding, field map, skip behavior, threshold logic, and data-retention schema.
- `distinct_verifier_needed`: `RAW_HACKER_NEWS_V0_ITEM_ENDPOINT_OR_HUMAN_UI_READBACK`
- `consumer`: `TTaoGaming/hfo-gen-133#5`
- `consumer_gate`: `EXTERNAL_SIGNAL_MONITOR_HACKER_NEWS_SOURCE_BINDING_AND_SEMANTICS_GATE_001`
- `secondary_consumer`: `S09_PRODUCT_DECISION_QUEUE`
- `expiry`: `2026-08-10T14:27:12Z`
- `fitness_credit`: `0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK`

## Decision

`REVISE`

Keep the Hacker News lane only as an item-bound attention and discussion monitor. Require a canonical HN item ID or item URL before collection; otherwise emit skip/unknown, not zero. Store score, comment volume, and item-state flags as non-buyer observations. Do not infer demand, buyer intent, conversion, revenue, or product-market fit from Hacker News metrics alone.

## Honest flaw

This card verifies the official API and guideline semantics and the claim ceiling of issue #5. It does not inspect the Gen-133 monitor implementation, publication registry bytes, any live HN item, request volume, response headers, database row, threshold configuration, account state, or downstream ConsumerAck.