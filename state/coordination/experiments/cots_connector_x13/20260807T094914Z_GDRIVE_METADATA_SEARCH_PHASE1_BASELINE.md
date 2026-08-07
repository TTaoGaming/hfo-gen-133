---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_015
phase: 1
status: PHASE1_ACCEPTED_WITH_GATES
candidate: Google_Drive_metadata_only_document_search
wip: 1
prior_current_version: 156
candidate_calls_this_wake: 1
campaign_calls_total: 1
read_only: true
candidate_mutations: 0
retries: 0
fallbacks: 0
query_class: bounded_keyword_document_metadata_search
result_limit: 3
results_returned: 3
content_hydration_requested: false
content_hydration_observed: false
raw_drive_ids_urls_titles_parent_ids_persisted_in_receipt: false
request_digest_sha256: 10d22ab08a13d84dbe724be7a76fa44a50af51617bd6edbbb9248241cd882ceb
ordered_metadata_result_digest_sha256: 8638e3335ea369bfebeec28ca607021e8f74a3db623461d45be7b1781953708a
next_page_token_observability: NOT_SURFACED_IN_RETURN_RESOURCE
incomplete_search_observability: NOT_SURFACED_IN_RETURN_RESOURCE
provider_request_id_observability: NOT_SURFACED
connector_latency_observability: NOT_SURFACED
effective_identity_and_scopes: UNKNOWN_CONNECTOR_MANAGED
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 50_to_150_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_BY_CONNECTOR
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
provider_contract_quota: FILES_LIST_100_QUOTA_UNITS_AS_OF_2026_08_07
provider_contract_limits: 1000000_UNITS_PER_MINUTE_PROJECT;325000_UNITS_PER_MINUTE_USER_PROJECT;400000000_UNITS_PER_DAY_PROJECT_BILLING_THRESHOLD
provider_contract_pricing: STANDARD_USE_NO_ADDITIONAL_COST;OVER_THRESHOLD_CHARGING_PLANNED_LATER_2026_WITH_NOTICE
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPE_UNKNOWN
durability: GIT_RECEIPT_DURABLE;DRIVE_SEARCH_VIEW_MUTABLE
observability: METADATA_FIELDS_VISIBLE;NO_CONTENT_HYDRATION;NO_PROVIDER_REQUEST_ID_RATE_HEADERS_QUOTA_DEBIT_INCOMPLETE_SEARCH_OR_LATENCY
portability: MEDIUM_DRIVE_QUERY_SEMANTICS_PROVIDER_SPECIFIC
failure_behavior: NOT_TESTED_IN_PHASE1
verifier: GITHUB_READBACK_PLUS_GOOGLE_DRIVE_V3_PRIMARY_DOCS
consumer: X13_NEXT_WAKE_ONLY_NO_OPERATIONAL_CONSUMER_ACK
strongest_falsifier: MATCHED_RAW_DRIVE_V3_FILES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_MATERIALLY_DISAGREES_ON_RESULT_SCOPE_ORDERING_PAGINATION_OR_METADATA_ONLY_BEHAVIOR
honest_flaw: ONE_SUCCESSFUL_BOUNDED_METADATA_QUERY_ONLY; PAGINATION_COMPLETENESS_PERMISSION_DENIAL_SHARED_DRIVE_VARIANCE_TRANSIENT_FAILURE_RATE_LIMIT_NATIVE_PARITY_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_AND_CONSUMER_VALUE_REMAIN_UNTESTED_OR_UNEXPOSED
valid_time_utc: 2026-08-07T09:49:14Z
recorded_time_utc: 2026-08-07T09:49:14Z
---

# X13 Google Drive metadata search — Phase 1

A single bounded Google Drive connector search used `item_type=document`, `topn=3`, `best_effort_fetch=false`, and returned three metadata records without document-body hydration. The immutable receipt intentionally stores only counts, booleans, and digests, not raw Drive identifiers, URLs, titles, or parent IDs.

Primary contract baseline: Google Drive v3 `files.list` supports `q`, `pageSize`, `pageToken`, multiple corpora, and returns `nextPageToken` plus `incompleteSearch`. The connector exposes a simpler metadata search surface, but this call did not expose provider request identity, effective OAuth principal/scopes, latency, `incompleteSearch`, or a provider quota debit. Absence of those fields is an observability gap, not evidence that they do not exist.

Official docs:
- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- https://developers.google.com/workspace/drive/api/guides/search-files
- https://developers.google.com/workspace/drive/api/guides/limits

Decision remains open. Phase 2 should replay the identical bounded metadata-only request and compare request/result digests without persisting raw Drive metadata.
