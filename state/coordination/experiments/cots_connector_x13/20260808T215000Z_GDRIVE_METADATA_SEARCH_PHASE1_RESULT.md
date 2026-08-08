---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GDRIVE_METADATA_SEARCH_READONLY_024
expected_current_version: 192
phase: 1
kind: RESULT
candidate: Google_Drive_search_metadata_only
phase_status: PHASE1_ACCEPTED_WITH_GATES
wip: 1
preflight_commit: 2f9f6b1a2522ae9f6583337086febf7dc1664b63
preflight_blob_sha: 3021195ad80c63d4cb2bb32bfd343a4b010389b2
preflight_readback: true
request_sha256: 0f9761ee65aac92abc2b2166117b05a25a4acc47c0355729c8bc7376248b10b2
result_count: 5
result_ordered_id_sha256: e0b48b1d71593436c4ff9104b5ef6d3226af198d1dbd7c7b4eefa04a32c892cd
continuation_token_observed: false
content_hydration_observed: false
mutations_total: 0
retries_total: 0
fallbacks_total: 0
connector_errors_total: 0
raw_drive_ids_titles_urls_persisted_in_x13: false
connector_document_bucket_included_spreadsheet_url: true
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
custom_code_avoided_realized: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: OFFICIAL_DRIVE_DOCS_STATE_FILES_LIST_100_QUOTA_UNITS;STANDARD_USE_NO_ADDITIONAL_COST_CURRENTLY;CURRENT_STANDARD_LIMITS_1000000_UNITS_PER_MINUTE_PROJECT_325000_PER_MINUTE_USER_PROJECT_1TB_EGRESS_PER_DAY_PROJECT_400000000_UNIT_DAILY_BILLING_THRESHOLD;CONNECTOR_NATIVE_METHOD_PROJECT_AND_ACTUAL_DEBIT_UNKNOWN
credentials: GOOGLE_DRIVE_CONNECTOR_MANAGED;EFFECTIVE_PRINCIPAL_OAUTH_SCOPE_TOKEN_TYPE_AND_CLOUD_PROJECT_UNKNOWN;NATIVE_DRIVE_METADATA_READONLY_SCOPE_EXISTS
observability: DIRECT_CONNECTOR_RETURNED_5_METADATA_RESULTS;NO_PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_LATENCY_EFFECTIVE_SCOPE_NATIVE_METHOD_OR_ACTUAL_QUOTA_DEBIT_EXPOSED
portability: MEDIUM_GENERIC_METADATA_SEARCH_AND_CURSOR_PAGINATION_PORTABLE_BUT_CONNECTOR_QUERY_AND_ITEM_TYPE_SEMANTICS_ARE_WRAPPER_SPECIFIC
durability: GIT_PREFLIGHT_AND_RESULT_EVENTS_DURABLE_WITH_PRIVACY_SAFE_DIGEST;NO_RAW_DRIVE_METADATA_PERSISTED
failure_behavior: NOT_YET_PROBED_PHASE1_ONLY
verifier: GITHUB_PREFLIGHT_READBACK_PLUS_DIRECT_GOOGLE_DRIVE_SEARCH_RECEIPT_PLUS_RESULT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_DRIVE_DOCUMENT_DISCOVERY
adoption_credit: 0
fitness_credit: 0
mandatory_gate: METADATA_ONLY;TOPN_LE_5_DURING_CAMPAIGN;NO_CONTENT_HYDRATION;NO_MUTATION;NO_RAW_IDS_TITLES_URLS_OWNERS_SNIPPETS_OR_PAGE_TOKENS_IN_X13_RECEIPTS;DO_NOT_INFER_COMPLETENESS_FROM_RESULT_COUNT_OR_ABSENT_CONTINUATION_TOKEN;TREAT_ITEM_TYPE_DOCUMENT_AS_CONNECTOR_DEFINED_UNTIL_VARIANCE_PROBED
strongest_falsifier: REPLAY_OF_THE_IDENTICAL_DURABLE_REQUEST_MATERIALLY_DISAGREES_WITHOUT_DRIVE_STATE_CHANGE_OR_PROVIDER_DIRECT_EQUIVALENT_UNDER_SAME_PRINCIPAL_RETURNS_MATERIALLY_DIFFERENT_ACCESSIBLE_MATCHES
honest_flaw: ONE_QUERY_ONLY;RESULT_COUNT_HIT_THE_TOPN_CAP;NO_CONTINUATION_TOKEN_WAS_EXPOSED;NATIVE_METHOD_MAPPING_SCOPE_COMPLETENESS_AND_QUOTA_DEBIT_ARE_UNKNOWN;CONNECTOR_DOCUMENT_BUCKET_INCLUDED_A_SPREADSHEET_URL
valid_time_utc: 2026-08-08T21:50:00Z
recorded_time_utc: 2026-08-08T21:50:00Z
---

# X13 Google Drive metadata search — Phase 1 result

The bounded metadata-only Drive search succeeded with exactly five returned items at `topn=5`. No content hydration, retry, fallback, connector error, or mutation was observed. A privacy-safe SHA-256 over the ordered result IDs was persisted for an exact Phase-2 replay comparison; raw IDs/titles/URLs were not copied into the X13 event.

One returned item used a Google Sheets URL even though the connector request used `item_type=document`. Treat `document` as a connector-defined bucket rather than assuming it means only Google Docs-native documents or excludes spreadsheets.

Official Google Drive v3 documentation establishes a COTS baseline: `files.list` supports query filtering and pagination, and `drive.metadata.readonly` exists as a metadata-only OAuth scope. Current official usage-limit documentation assigns 100 quota units to list operations such as `files.list`; standard use is currently available at no additional cost, with current standard limits of 1,000,000 quota units/minute/project, 325,000/minute/user/project, 1 TB egress/day/project, and a 400,000,000-unit daily billing threshold. The connector did not expose its native Drive method, effective Cloud project, actual quota debit, or billing evidence.

Decision is not yet an adoption decision. Phase 1 is accepted with gates; Phase 2 should replay the exact durable request once and compare only privacy-safe aggregates/digests.

Official references:
- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- https://developers.google.com/workspace/drive/api/guides/search-files
- https://developers.google.com/workspace/drive/api/guides/api-specific-auth
- https://developers.google.com/workspace/drive/api/guides/limits
