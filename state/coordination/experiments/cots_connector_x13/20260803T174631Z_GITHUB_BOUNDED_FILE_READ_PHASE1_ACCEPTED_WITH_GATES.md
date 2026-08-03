---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_BOUNDED_FILE_READONLY_001
event_id: X13_GITHUB_FILE_READ_PHASE1_20260803T174631Z
phase: 1
campaign_wake: 1_of_4
result: PHASE1_ACCEPTED_WITH_GATES
expected_current_version: 68
next_current_version: 69
prior_current_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
prior_current_commit: 8c11825b734d76807708130b32c2e2463aa3030d
prior_current_blob_sha: 02ced81114d70f1861654594ab725fcd441cd187
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
candidate: GitHub_bounded_readonly_repository_file_fetch_surface
candidate_selection:
  preferred_next_candidate: Google_Tasks_bounded_readonly_tasklist_and_task_metadata_surface
  google_tasks_native_resource_available: false
  direct_discovery_receipt: NO_TOOL_DEFINED_UNDER_GOOGLE_TASKS_PATH
  valid_connector_names_returned:
    - GitHub
    - Gmail
    - Google_Calendar
    - Google_Contacts
    - Google_Drive
    - Plugin_Management
    - Slack
  account_permission_terms_or_install_change_attempted: false
  fallback_selected: GitHub_bounded_readonly_repository_file_fetch_surface
binding_architecture_decision: false
same_provider_binding_weight: 0
independent_verification_closed: false
consumer_ack: NOT_OBSERVED
fitness_credit: 0
adoption_credit: 0
effect_ceiling: CATALOG_BASELINE_OF_ONE_EXPLICIT_REPOSITORY_PATH_BRANCH_UTF8_FILE_READ_NO_WRITE_OR_OPERATIONAL_PROMOTION
valid_time_utc: 2026-08-03T17:46:31Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
review_expiry_utc: 2026-08-10T17:46:31Z
phase1_probe:
  action: GitHub.fetch_file
  repository: TTaoGaming/hfo-gen-133
  path: state/coordination/experiments/cots_connector_x13/CURRENT.md
  ref: agent/gen133-bootstrap-20260730
  requested_encoding: utf-8
  returned_content: true
  returned_encoding: utf-8
  returned_blob_sha: 02ced81114d70f1861654594ab725fcd441cd187
  returned_display_url: true
  returned_display_title: true
  resolved_branch_commit_sha_returned: false
  raw_http_status_returned: false
  request_id_etag_last_modified_and_rate_limit_headers_returned: false
  connector_retry_count_visible: false
  mutation_effect: false
  surfaced_paid_cost_usd: 0
  operator_minutes_removed_measured: 0
measured_facts:
  explicit_repository_path_and_branch_read_succeeded_once: true
  utf8_content_and_content_addressed_blob_sha_returned: true
  wrapper_returned_full_file_content_not_metadata_only: true
  branch_ref_is_mutable_even_though_blob_sha_is_content_addressed: true
  exact_resolved_branch_commit_not_exposed: true
  private_or_internal_file_content_can_be_exposed_by_successful_read: true
  no_github_mutation_in_phase1_probe: true
  google_tasks_surface_absent_from_current_authorized_connector_inventory: true
privacy_andon:
  triggered: true
  measured_fact: SUCCESSFUL_FETCH_RETURNS_COMPLETE_FILE_CONTENT
  implication: FILE_CLASSIFICATION_AND_LOCAL_MINIMIZATION_ARE_REQUIRED_BEFORE_DURABLE_CROSS_SURFACE_FANOUT
immutability_andon:
  triggered: true
  measured_fact: WRAPPER_EXPOSES_BLOB_SHA_BUT_NOT_THE_RESOLVED_BRANCH_COMMIT_SHA
  implication: BRANCH_REF_READ_IS_POINT_IN_TIME_BUT_NOT_COMMIT_PINNED_AND_MUST_NOT_BE_TREATED_AS_A_DURABLE_SNAPSHOT_WITHOUT_FOLLOWUP_VERIFICATION
tool_availability_andon:
  triggered: true
  measured_fact: NO_NATIVE_GOOGLE_TASKS_TOOL_RESOURCE_EXISTS_IN_CURRENT_AUTHORIZED_CONNECTOR_INVENTORY
  implication: GOOGLE_TASKS_CAMPAIGN_DEFERRED_WITHOUT_INSTALL_ACCOUNT_PERMISSION_OR_TERMS_CHANGE
official_contract_checked_2026_08_03:
  repository_contents: https://docs.github.com/en/rest/repos/contents
  rate_limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
  get_content_path_parameter_required: true
  ref_accepts_commit_branch_or_tag_and_defaults_to_default_branch: true
  fine_grained_private_repository_permission: CONTENTS_READ
  public_resource_can_be_read_without_authentication: true
  documented_success_and_failure_statuses:
    - 200_OK
    - 302_FOUND
    - 304_NOT_MODIFIED
    - 403_FORBIDDEN
    - 404_NOT_FOUND
  file_size_contract:
    up_to_1_mb: ALL_ENDPOINT_FEATURES_SUPPORTED
    over_1_mb_to_100_mb: RAW_OR_OBJECT_MEDIA_TYPES_REQUIRED_WITH_OBJECT_CONTENT_EMPTY
    over_100_mb: ENDPOINT_NOT_SUPPORTED
  directory_entry_limit: 1000
  rate_limit_headers_documented:
    - x-ratelimit-limit
    - x-ratelimit-remaining
    - x-ratelimit-used
    - x-ratelimit-reset
    - x-ratelimit-resource
custom_code_avoided_estimate:
  authenticated_repository_path_ref_fetch_base64_decode_and_normalized_file_response: 25_to_70_LOC_UNVALIDATED
  secret_classification_commit_pinning_rate_limit_telemetry_retry_policy_and_consumer_workflow: NOT_AVOIDED_REQUIRES_HFO_GATES
credentials:
  connector_reached_private_or_authorized_repository_success_path: true
  operator_supplied_credentials_campaign: 0
  authenticated_principal: UNKNOWN
  token_class: UNKNOWN_GITHUB_APP_OAUTH_OR_PAT
  effective_repository_scope: UNKNOWN
  token_storage_and_custody: CONNECTOR_MANAGED_UNINSPECTED
  least_privilege_closed: false
durability: SOURCE_FILE_AND_RETURNED_BLOB_SHA_ARE_GIT_DURABLE_BUT_THE_REQUEST_USED_A_MUTABLE_BRANCH_REF_AND_THE_WRAPPER_DID_NOT_RETURN_THE_RESOLVED_COMMIT_SHA_ETAG_OR_CONDITIONAL_READ_RECEIPT
observability: MEDIUM_FOR_REPOSITORY_PATH_REF_ENCODING_CONTENT_BLOB_SHA_AND_DISPLAY_URL_LOW_FOR_RAW_HTTP_STATUS_REQUEST_ID_ETAG_RESOLVED_COMMIT_RATE_LIMIT_HEADERS_UPSTREAM_ATTEMPTS_AND_RETRIES
portability: MEDIUM_FOR_GENERIC_REPOSITORY_FILE_READ_LOW_TO_MEDIUM_ACROSS_NON_GITHUB_HOSTS_BECAUSE_ENDPOINT_AUTH_MEDIA_TYPES_ERRORS_AND_RATE_LIMITS_ARE_PROVIDER_SPECIFIC
failure_behavior:
  bounded_positive_utf8_file_read: OBSERVED
  immutable_blob_readback: NOT_TESTED
  missing_path_404: NOT_TESTED
  permission_403_or_private_repo_denial: NOT_TESTED
  invalid_ref: NOT_TESTED
  large_file_media_type_behavior: NOT_TESTED
  symlink_or_submodule_behavior: NOT_TESTED
  rate_limit_or_secondary_limit: NOT_TESTED
  transport_timeout: NOT_TESTED
  raw_api_or_git_parity: NOT_TESTED
mandatory_gates:
  - REQUIRE_EXPLICIT_REPOSITORY_PATH_AND_REF_NEVER_RELY_ON_DEFAULT_BRANCH_FOR_CONTROL_STATE
  - TREAT_BRANCH_TAG_READS_AS_MUTABLE_POINT_IN_TIME_OBSERVATIONS_NOT_COMMIT_PINNED_SNAPSHOTS
  - VERIFY_THE_RETURNED_BLOB_SHA_OR_FETCH_BY_IMMUTABLE_COMMIT_BEFORE A_BINDING_DECISION
  - CLASSIFY_AND_MINIMIZE_FILE_CONTENT_BEFORE_CROSS_SURFACE_LOGGING
  - DO_NOT_PERSIST_SECRETS_TOKENS_PRIVATE_KEYS_OR_UNNEEDED_PERSONAL_CONTENT
  - DISTINGUISH_403_404_INVALID_REF_RATE_LIMIT_TRANSPORT_TIMEOUT_AND_PROVIDER_FAILURE
  - DO_NOT_ASSUME_RETRY_SAFETY_OR_QUOTA_CAPACITY_WITHOUT_RAW_HEADERS_AND_BOUNDED_POLICY
  - CHECK_SIZE_SYMLINK_SUBMODULE_AND_ENCODING_BEHAVIOR_BEFORE_GENERALIZING
  - NO_WRITE_DELETE_BRANCH_MERGE_RELEASE_WORKFLOW_OR_PRODUCTION_OPERATION_FROM_THIS_READ_CAMPAIGN
  - REQUIRE_NAMED_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME_BEFORE_ADOPTION_OR_FITNESS_CREDIT
verifier: DISTINCT_RAW_GITHUB_CONTENTS_API_OR_GIT_BLOB_READ_PINNED_TO_THE_RETURNED_BLOB_SHA_AND_RESOLVED_COMMIT_WITH_HTTP_STATUS_ETAG_RATE_LIMIT_AND_CONTENT_DIGEST
consumer:
  immediate_catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
  future_operational_consumer: MUST_BE_NAMED_IN_NEW_WORKITEM
strongest_falsifier: A_DISTINCT_RAW_GITHUB_OR_GIT_READ_SHOWS_THE_WRAPPER_USED_A_DIFFERENT_REF_RETURNED_CONTENT_NOT_MATCHING_BLOB_SHA_TRUNCATED_OR_REWROTE_BYTES_OR_HID_A_FAILURE_RETRY_OR_UNBOUNDED_CALL
reversible_next_experiment:
  phase: 2_of_4
  action: GitHub.fetch_blob
  input: PHASE1_RETURNED_BLOB_SHA
  purpose: ONE_READONLY_CONTENT_ADDRESSED_READBACK_TO_COMPARE_BYTES_WITH_PHASE1_WITHOUT_BRANCH_TRAVERSAL_OR_WRITE
  mutation: NONE
honest_flaw: ONE_KNOWN_SMALL_UTF8_FILE_READ_SUCCEEDED_BUT_RESOLVED_COMMIT_IDENTITY_RAW_HTTP_STATUS_ETAG_RATE_LIMIT_SCOPE_PERMISSION_FAILURE_LARGE_FILE_SYMLINK_SUBMODULE_TIMEOUT_RETRY_RAW_API_PARITY_CONSUMER_ACK_AND_OPERATOR_TIME_REDUCTION_REMAIN_UNVERIFIED
sealed: true
---

# X13 GitHub bounded file read phase 1

The native Google Tasks surface was unavailable in the current authorized connector inventory, so that candidate was deferred without installation, account, permission, or terms changes.

Fallback phase 1 established one narrow fact: `GitHub.fetch_file` returned the complete UTF-8 contents and blob SHA for one explicit repository path on one explicit branch. This is a useful read baseline, but the branch is mutable and the wrapper did not expose the resolved commit SHA, raw HTTP status, ETag, request ID, rate-limit headers, upstream attempts, or retry behavior.

No GitHub mutation occurred. Adoption and fitness credit remain zero. Phase 2 is limited to one content-addressed `fetch_blob` readback using the returned blob SHA.
