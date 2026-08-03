# S08 Evidence Card — GitHub Repository Metrics Buyer-Signal Boundary

- `seat`: `S08_RESEARCH_AND_CANDIDATE_SCOUT`
- `carrier_task_id_expected`: `6a526109ba348191b5f23ad3172ad568`
- `carrier_task_id_observed`: `6a526109ba348191b5f23ad3172ad568`
- `task_id_match`: `TRUE`
- `valid_time`: `2026-08-03T09:28:00Z`
- `transaction_time`: `GIT_COMMIT_TIME`
- `canonical_repository`: `TTaoGaming/hfo-gen-133`
- `canonical_branch`: `agent/gen133-bootstrap-20260730`
- `lane`: `DISTRIBUTION_AND_BUYER_EVIDENCE`
- `wip`: `1`
- `decision`: `REVISE`

## Changed bounded question

Gen-133 issue #5 newly reports that the external-signal monitor's GitHub public-repository metrics lane is returning successfully. Can repository stars, `watchers_count`, subscribers, forks, views, or clones be promoted to buyer evidence or counted as independent corroborating signals?

## Exact candidate and source binding

- `candidate_id`: `EXTERNAL_SIGNAL_MONITOR_GITHUB_PUBLIC_REPOSITORY_METRICS_001`
- `queue_source`: `TTaoGaming/hfo-gen-133#5`
- `queue_source_url`: `https://github.com/TTaoGaming/hfo-gen-133/issues/5`
- `queue_source_created_at`: `2026-08-02T18:51:49Z`
- `queue_source_updated_at_observed`: `2026-08-02T18:51:49Z`
- `candidate_repository`: `TTaoGaming/hfo-gen-133`
- `candidate_branch`: `agent/gen133-bootstrap-20260730`
- `implementation_path`: `UNKNOWN`
- `implementation_commit`: `UNKNOWN`
- `monitored_repository_set`: `UNKNOWN`
- `GitHub_API_version_bound_by_candidate`: `UNKNOWN`
- `exact_metric_field_map_bound_by_candidate`: `UNKNOWN`

Issue #5 establishes only that public GitHub repository metrics are returning. It does not bind the monitor implementation bytes, API version, exact repositories, raw response schema, field labels, threshold rules, or consumer promotion logic.

## Current primary sources

Accessed `2026-08-03`:

1. GitHub REST API endpoints for watching: `https://docs.github.com/en/rest/activity/watching`
2. GitHub REST API endpoints for starring: `https://docs.github.com/en/rest/activity/starring`
3. GitHub REST API endpoints for repository traffic: `https://docs.github.com/en/rest/metrics/traffic?apiVersion=2026-03-10`
4. GitHub Docs, viewing repository traffic: `https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository`
5. GitHub Docs, about forks: `https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks`

## Supported claims

- GitHub defines a star as a repository bookmark and describes stars as showing an approximate level of interest.
- In REST repository responses, `watchers`, `watchers_count`, and `stargazers_count` all represent stars. They are aliases, not independent observations.
- `subscribers_count` represents actual repository watchers receiving activity notifications.
- A fork is an independent repository copy used for experimentation or possible contribution; it is evidence of repository interaction, not evidence of purchase.
- Repository traffic can expose views, unique visitors, clones, referrers, and popular content for a recent fourteen-day window, but GitHub limits that traffic surface to repositories for which the caller has write access.
- These metrics can be retained as dated top-of-funnel attention, notification-interest, exploration, or usage-proxy observations when their exact source repository, field, collection time, and access mode are bound.

## Required signal classes

- `stargazers_count` or `watchers_count` → `GITHUB_STAR_APPROXIMATE_INTEREST`
- `subscribers_count` → `GITHUB_NOTIFICATION_SUBSCRIBER_INTEREST`
- `forks_count` → `GITHUB_CODE_EXPLORATION_OR_DERIVATION_SIGNAL`
- repository views or unique visitors → `GITHUB_ATTENTION_SIGNAL`
- repository clones → `GITHUB_USAGE_PROXY`

`watchers_count` and `stargazers_count` must be deduplicated as the same underlying star count. None of these classes may be promoted to `BUYER_SIGNAL` without a separate source-bound commercial event.

## Excluded claims

This evidence does not support:

- buyer identity, qualified lead, purchase intent, contract, payment, revenue, retained margin, active customer, product-market fit, or successful distribution;
- treating `watchers_count` and `stargazers_count` as two corroborating signals;
- interpreting a zero or unchanged count as absence of demand;
- interpreting a fork as adoption, production use, endorsement, or willingness to pay;
- treating GitHub traffic as an anonymous public-repository lane available without repository write authority;
- threshold success until the exact monitor implementation, field mapping, repository set, baseline, and consumer rule are read back.

## License and terms uncertainty

- Repository-content licenses are not determined by repository engagement metrics and must remain a separate per-candidate review.
- GitHub's July 2026 documentation announces access restrictions for stargazer and watcher listing endpoints. The continued availability, authentication mode, quota, and response behavior of the exact monitor route are therefore time-sensitive.
- No account action, token creation, permission change, terms acceptance, or API purchase occurred in this research pass.

## Cost and operator-minute estimate

- `external_spend_measured`: `$0`
- `operator_minutes_measured`: `0`
- `research_carrier_minutes`: `NOT_EXPOSED`
- `smallest_producer_revision_estimate`: `20–40 minutes` to bind exact metric fields, deduplicate star aliases, type signal classes, and prohibit buyer promotion.
- `distinct_verifier_estimate`: `15–25 minutes` for exact implementation and one raw GitHub API/UI readback.

Estimates are not measured savings or completed work.

## Strongest objection

Stars, forks, and clones can correlate with developer interest or adoption, so refusing to call them buyer evidence may discard useful early commercial information.

## Response to objection

Retain them as top-of-funnel observations. The control defect is not collection; it is semantic promotion and correlated double counting. A useful proxy remains useful when typed honestly and joined later to a separate qualified-lead, checkout, contract, or payment event.

## Falsifier

This `REVISE` decision is falsified for the implementation gate if exact monitor bytes and raw readback show all of the following:

1. `watchers_count` and `stargazers_count` are not counted independently;
2. every metric is bound to repository, field, collection time, API/access mode, and baseline;
3. stars, subscribers, forks, traffic, and clones retain distinct non-buyer signal classes;
4. threshold logic cannot promote those observations to buyer, revenue, or product-market-fit status;
5. one named consumer acknowledges and uses the typed observation without demand invention.

A separate source-bound qualified lead, purchase, contract, or payment can independently create buyer evidence; it does not retroactively change GitHub metric semantics.

## Verifier, consumer, expiry

- `structural_verifier`: `S04_STRUCTURAL_PREFLIGHT` for exact implementation path, field map, alias deduplication, threshold logic, and source binding.
- `distinct_verifier_needed`: `RAW_GITHUB_API_OR_UI_READBACK_BY_DISTINCT_PROVIDER_OR_HUMAN`
- `consumer`: `TTaoGaming/hfo-gen-133#5`
- `consumer_gate`: `EXTERNAL_SIGNAL_MONITOR_GITHUB_METRIC_SEMANTICS_GATE_001`
- `secondary_consumer`: `S09_PRODUCT_DECISION_QUEUE`
- `expiry`: `2026-08-10T09:28:00Z`
- `fitness_credit`: `0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK`

## Decision

`REVISE`

Keep the GitHub lane, but type it as attention, notification-interest, exploration, or usage proxy. Deduplicate `watchers_count` and `stargazers_count`. Do not claim buyer evidence, demand, revenue, or product-market fit from repository metrics alone. Exact implementation conformance remains `UNKNOWN` until the monitor bytes and raw field mapping are bound and independently read back.

## Honest flaw

This card verifies GitHub's current public metric semantics and the queue issue's claim ceiling. It does not inspect the monitor implementation, raw API response, current threshold configuration, monitored repository registry, authentication principal, quota headers, or downstream database rows.