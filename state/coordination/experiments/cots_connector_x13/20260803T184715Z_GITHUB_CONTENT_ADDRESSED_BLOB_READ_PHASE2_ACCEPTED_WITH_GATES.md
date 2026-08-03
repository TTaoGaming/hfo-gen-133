---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_BOUNDED_FILE_READONLY_001
event_type: PHASE2_ACCEPTED_WITH_GATES
candidate: GitHub_content_addressed_blob_read_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 69
next_current_version: 70
phase: 2_of_4
valid_time_utc: 2026-08-03T18:47:15Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
effect_ceiling: ONE_READONLY_CONTENT_ADDRESSED_BLOB_FETCH_NO_BRANCH_TRAVERSAL_RETRY_WRITE_OR_OPERATIONAL_PROMOTION
adoption_credit: 0
fitness_credit: 0
consumer_ack: NOT_OBSERVED
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate_per_consumed_blob_lookup: 1_to_3_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
custom_code_avoided_estimate:
  authenticated_git_blob_get_base64_decode_and_normalized_text_response: 20_to_55_LOC_UNVALIDATED
  byte_digest_recomputation_secret_classification_rate_limit_telemetry_retry_policy_and_consumer_workflow: NOT_AVOIDED_REQUIRES_HFO_GATES
credentials:
  connector_reached_private_or_internal_repository_blob_success_path: true
  operator_supplied_credentials_this_phase: 0
  authenticated_principal: UNKNOWN
  token_class: UNKNOWN_GITHUB_APP_OAUTH_OR_PAT
  effective_repository_scope: UNKNOWN
  token_storage_and_custody: CONNECTOR_MANAGED_UNINSPECTED
  least_privilege_closed: false
direct_receipt:
  action: GitHub.fetch_blob
  repository: TTaoGaming/hfo-gen-133
  requested_blob_sha: 02ced81114d70f1861654594ab725fcd441cd187
  requested_blob_origin: PHASE1_FETCH_FILE_RETURNED_BLOB_SHA
  branch_or_tag_ref_supplied: false
  returned_content: true
  returned_content_class: COMPLETE_UTF8_TEXT_AS_CONNECTOR_DECODED
  embedded_schema_id_observed: hfo.gen133.x13.cots_connector_current.v1
  embedded_experiment_id_observed: X13_SLACK_BOUNDED_CHANNEL_HISTORY_READONLY_001
  embedded_version_observed: 68
  wrapper_echoed_blob_sha: false
  wrapper_returned_encoding: false
  wrapper_returned_size: false
  raw_http_status_returned: false
  request_id_etag_last_modified_and_rate_limit_headers_returned: false
  connector_visible_error: null
  connector_visible_external_call_time_ms: 374
  carrier_retries: 0
  mutation_effect: false
measured_facts:
  content_addressed_blob_fetch_succeeded_once: true
  no_branch_tag_or_default_ref_resolution_was_requested: true
  returned_content_embedded_expected_version_68_markers: true
  connector_decoded_and_returned_complete_text_content: true
  connector_did_not_echo_sha_encoding_size_http_status_or_rate_limit_headers: true
  no_candidate_surface_write_retry_or_fallback: true
immutability_result:
  admitted: ONE_READ_OF_THE_REQUESTED_GITHUB_BLOB_SHA_RETURNED_CONTENT_WITH_EXPECTED_V68_MARKERS_WITHOUT_BRANCH_TRAVERSAL
  not_admitted: INDEPENDENT_BYTE_FOR_BYTE_GIT_OBJECT_HASH_RECOMPUTATION_OR_DISTINCT_RAW_API_PARITY
privacy_andon:
  triggered: true
  measured_fact: FETCH_BLOB_RETURNS_COMPLETE_FILE_CONTENT
  implication: CONTENT_CLASSIFICATION_AND_MINIMIZATION_REMAIN_REQUIRED_BEFORE_CROSS_SURFACE_FANOUT
wrapper_variance_andon:
  triggered: true
  measured_fact: OFFICIAL_JSON_RESPONSE_FIELDS_SHA_ENCODING_SIZE_AND_URL_WERE_NOT_EXPOSED_BY_THE_CONNECTOR_WRAPPER
  implication: CALLER_CANNOT_DIRECTLY_CONFIRM_RESPONSE_SHA_ENCODING_OR_SIZE_FROM_WRAPPER_OUTPUT
observability_andon:
  triggered: true
  measured_fact: CONNECTOR_EXPOSED_DECODED_CONTENT_AND_VISIBLE_CALL_LATENCY_BUT_NOT_RAW_HTTP_STATUS_REQUEST_ID_ETAG_RATE_LIMIT_HEADERS_OR_UPSTREAM_ATTEMPTS
  implication: QUOTA_FAILURE_AND_RETRY_CLASSIFICATION_REMAIN_UNCLOSED
official_contract_checked_2026_08_03:
  git_blobs: https://docs.github.com/en/rest/git/blobs
  rate_limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
  git_blob_is_file_content_object_with_stored_sha1_hash: true
  get_blob_path_requires_file_sha: true
  get_blob_supports_up_to_100_mb: true
  default_json_content_is_base64_encoded: true
  raw_media_type_available: true
  fine_grained_private_repository_permission: CONTENTS_READ
  public_resource_can_be_read_without_authentication: true
  documented_statuses:
    - 200_OK
    - 403_FORBIDDEN
    - 404_NOT_FOUND
    - 409_CONFLICT
    - 422_VALIDATION_FAILED_OR_SPAMMED
  documented_json_response_fields:
    - content
    - encoding
    - url
    - sha
    - size
    - node_id
  most_rest_get_requests_secondary_rate_limit_points: 1
  actual_connector_rate_limit_resource_and_consumption: UNKNOWN
durability: HIGHER_THAN_BRANCH_PATH_READ_FOR_OBJECT_IDENTITY_BECAUSE_THE_REQUEST_USED_A_CONTENT_ADDRESSED_BLOB_SHA_BUT_BYTE_HASH_RECOMPUTATION_RESPONSE_SHA_ECHO_AND_DISTINCT_PARITY_WERE_NOT_OBSERVED
observability: MEDIUM_FOR_INPUT_SHA_CONTENT_EXPECTED_EMBEDDED_MARKERS_ERROR_NULL_AND_VISIBLE_LATENCY_LOW_FOR_RESPONSE_SHA_ENCODING_SIZE_HTTP_STATUS_REQUEST_ID_ETAG_RATE_LIMIT_HEADERS_UPSTREAM_ATTEMPTS_AND_RETRIES
portability: MEDIUM_FOR_GIT_CONTENT_ADDRESSING_LOW_TO_MEDIUM_FOR_CONNECTOR_RESPONSE_SHAPE_AUTH_AND_ERROR_TELEMETRY_ACROSS_GITHUB_GITLAB_BITBUCKET_AND_LOCAL_GIT
failure_behavior:
  known_valid_blob_sha: OBSERVED_SUCCESS_PHASE2
  malformed_or_missing_blob_sha: NOT_TESTED
  cross_repository_sha_absence_404: NOT_TESTED
  permission_403_or_private_repo_masked_404: NOT_TESTED
  conflict_or_validation_error: NOT_TESTED
  binary_blob_behavior: NOT_TESTED
  blob_over_100_mb: NOT_TESTED
  rate_limit_or_secondary_limit: NOT_TESTED
  timeout_or_transport_failure: NOT_TESTED
  raw_api_or_local_git_parity: NOT_TESTED
strongest_falsifier: A_DISTINCT_RAW_GITHUB_GET_BLOB_OR_LOCAL_GIT_CAT_FILE_FOR_02CED81114D70F1861654594AB725FCD441CD187_RETURNS_DIFFERENT_BYTES_OR_SHOWS_THE_WRAPPER_TRUNCATED_REWROTE_OR_DECODED_LOSSILY
verifier: DISTINCT_AUTHORIZED_RAW_GITHUB_GET_BLOB_OR_LOCAL_GIT_CAT_FILE_FOR_THE_SAME_SHA_WITH_SHA_ECHO_SIZE_ENCODING_HTTP_STATUS_RATE_LIMIT_HEADERS_AND_INDEPENDENT_GIT_BLOB_HASH_RECOMPUTATION
consumer:
  immediate_catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
  future_operational_consumer: MUST_BE_NAMED_IN_NEW_WORKITEM
honest_flaw: ONE_SMALL_UTF8_BLOB_RETURNED_EXPECTED_V68_MARKERS_BUT_THE_CONNECTOR_DID_NOT_ECHO_SHA_ENCODING_OR_SIZE_AND_NO_INDEPENDENT_BYTE_HASH_RAW_API_OR_LOCAL_GIT_PARITY_PERMISSION_FAILURE_BINARY_LARGE_BLOB_RATE_LIMIT_CONSUMER_ACK_OR_OPERATOR_TIME_REDUCTION_WAS_ESTABLISHED
phase_2_result:
  disposition: PHASE2_ACCEPTED_WITH_CONTENT_CLASSIFICATION_RESPONSE_FIELD_OBSERVABILITY_AND_INDEPENDENT_DIGEST_GATES
next_wake:
  candidate: GitHub_bounded_readonly_repository_file_fetch_surface
  phase: 3_of_4
  planned_probe: ONE_SYNTACTICALLY_VALID_NONEXISTENT_BLOB_SHA_FETCH_WITH_NO_RETRY_FALLBACK_BRANCH_TRAVERSAL_OR_WRITE_TO_CLASSIFY_CONNECTOR_FAILURE_PRESERVATION
---

# X13 GitHub content-addressed blob read — phase 2

One `GitHub.fetch_blob` call used the blob SHA returned by phase 1. The read succeeded without branch, tag, or default-branch resolution and returned complete decoded text containing the expected sealed v68 CURRENT markers.

The connector did not echo the response SHA, encoding, size, HTTP status, request ID, ETag, rate-limit headers, upstream attempt count, or retry state. This improves object identity over a mutable branch read, but it does not close independent byte integrity or raw API parity.

Adoption and fitness credit remain zero. Phase 3 is limited to one syntactically valid nonexistent blob SHA to observe failure preservation, with no retry, fallback, traversal, or write.
