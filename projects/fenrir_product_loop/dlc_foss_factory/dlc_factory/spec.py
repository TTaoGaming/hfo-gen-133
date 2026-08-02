
"""Unit-spec validation and license/provenance preflight boundaries."""

from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path, PurePosixPath
from typing import Any, NoReturn

from .canonical import assert_no_secrets, canonical_json_bytes, sha256_bytes
from .errors import SpecValidationError


SCHEMA_ID = "hfo.gen133.dlc_foss_factory.unit_spec.v1"
STAGES = ("install", "build", "test", "health", "rollback")
_UNIT_ID = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
_HEX40 = re.compile(r"^[0-9a-f]{40}$")
_HEX64 = re.compile(r"^[0-9a-f]{64}$")


def _fail(message: str) -> NoReturn:
    raise SpecValidationError(message)


def _expect_dict(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        _fail(f"{path} must be an object")
    return value


def _exact_keys(value: dict[str, Any], required: set[str], path: str) -> None:
    missing = sorted(required - set(value))
    extra = sorted(set(value) - required)
    if missing:
        _fail(f"{path} missing required fields: {', '.join(missing)}")
    if extra:
        _fail(f"{path} has unsupported fields: {', '.join(extra)}")


def _nonblank(value: Any, path: str, maximum: int = 500) -> str:
    if not isinstance(value, str) or not value.strip():
        _fail(f"{path} must be a non-empty string")
    if len(value) > maximum:
        _fail(f"{path} exceeds {maximum} characters")
    if any(ord(char) < 32 and char not in "\n\t" for char in value):
        _fail(f"{path} contains a disallowed control character")
    return value


def _relative_posix_path(value: Any, path: str) -> str:
    text = _nonblank(value, path, 240)
    candidate = PurePosixPath(text)
    if (
        candidate.is_absolute()
        or ".." in candidate.parts
        or "\\" in text
        or ":" in text
        or str(candidate) in ("", ".")
    ):
        _fail(f"{path} must be a normalized relative POSIX file path")
    return text


def _validate_target(target: dict[str, Any]) -> str:
    state = target.get("binding_state")
    if state == "UNADMITTED":
        _exact_keys(target, {"binding_state"}, "$.target")
        return state
    if state != "BOUND":
        _fail("$.target.binding_state must be UNADMITTED or BOUND")
    _exact_keys(
        target,
        {"binding_state", "target_id", "user_job", "demand_evidence"},
        "$.target",
    )
    target_id = _nonblank(target["target_id"], "$.target.target_id", 64)
    if not _UNIT_ID.fullmatch(target_id):
        _fail("$.target.target_id must be a lowercase kebab-case identifier")
    _nonblank(target["user_job"], "$.target.user_job")
    evidence = _expect_dict(target["demand_evidence"], "$.target.demand_evidence")
    _exact_keys(
        evidence,
        {"permalink", "observed_on", "engagement_score", "buyer_class", "pain_statement"},
        "$.target.demand_evidence",
    )
    permalink = _nonblank(evidence["permalink"], "$.target.demand_evidence.permalink", 500)
    if not permalink.startswith(
        (
            "https://www.reddit.com/",
            "https://news.ycombinator.com/",
            "https://www.indiehackers.com/",
        )
    ):
        _fail("$.target.demand_evidence.permalink must be an original Reddit, Hacker News, or Indie Hackers URL")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(evidence["observed_on"])):
        _fail("$.target.demand_evidence.observed_on must be YYYY-MM-DD")
    score = evidence["engagement_score"]
    if not isinstance(score, int) or isinstance(score, bool) or score < 0:
        _fail("$.target.demand_evidence.engagement_score must be a non-negative integer")
    _nonblank(evidence["buyer_class"], "$.target.demand_evidence.buyer_class", 200)
    _nonblank(evidence["pain_statement"], "$.target.demand_evidence.pain_statement")
    return state


def _validate_provenance(provenance: dict[str, Any], binding_state: str) -> None:
    keys = {"review_state", "upstream", "license", "trademark_boundary", "asset_caveats"}
    _exact_keys(provenance, keys, "$.provenance")
    if binding_state == "UNADMITTED":
        if provenance != {
            "review_state": "UNBOUND",
            "upstream": None,
            "license": None,
            "trademark_boundary": "UNBOUND",
            "asset_caveats": [],
        }:
            _fail("unadmitted targets must keep provenance explicitly UNBOUND")
        return
    if provenance["review_state"] != "STRUCTURAL_ONLY":
        _fail("$.provenance.review_state must be STRUCTURAL_ONLY for a bound candidate")
    upstream = _expect_dict(provenance["upstream"], "$.provenance.upstream")
    _exact_keys(upstream, {"repository", "ref", "commit"}, "$.provenance.upstream")
    repository = _nonblank(upstream["repository"], "$.provenance.upstream.repository", 500)
    if not repository.startswith("https://"):
        _fail("$.provenance.upstream.repository must be an HTTPS repository URL")
    _nonblank(upstream["ref"], "$.provenance.upstream.ref", 240)
    if not _HEX40.fullmatch(str(upstream["commit"])):
        _fail("$.provenance.upstream.commit must be a lowercase 40-hex commit")
    packet = _expect_dict(provenance["license"], "$.provenance.license")
    _exact_keys(
        packet,
        {"path", "git_blob_sha1", "sha256", "spdx_expression", "obligations"},
        "$.provenance.license",
    )
    _relative_posix_path(packet["path"], "$.provenance.license.path")
    if not _HEX40.fullmatch(str(packet["git_blob_sha1"])):
        _fail("$.provenance.license.git_blob_sha1 must be lowercase 40-hex")
    if not _HEX64.fullmatch(str(packet["sha256"])):
        _fail("$.provenance.license.sha256 must be lowercase 64-hex")
    _nonblank(packet["spdx_expression"], "$.provenance.license.spdx_expression", 120)
    if not isinstance(packet["obligations"], list):
        _fail("$.provenance.license.obligations must be an array")
    for index, obligation in enumerate(packet["obligations"]):
        _nonblank(obligation, f"$.provenance.license.obligations[{index}]")
    boundary = _nonblank(provenance["trademark_boundary"], "$.provenance.trademark_boundary")
    if boundary == "UNBOUND":
        _fail("a bound candidate requires an explicit trademark boundary")
    if not isinstance(provenance["asset_caveats"], list):
        _fail("$.provenance.asset_caveats must be an array")
    for index, caveat in enumerate(provenance["asset_caveats"]):
        _nonblank(caveat, f"$.provenance.asset_caveats[{index}]")


def _validate_adapters(adapters: dict[str, Any]) -> None:
    _exact_keys(adapters, {"provider", "stages", "options"}, "$.adapters")
    if adapters["provider"] != "builtin.non_production":
        _fail("v1 only permits the code-owned builtin.non_production adapter")
    if adapters["stages"] != list(STAGES):
        _fail("$.adapters.stages must list install, build, test, health, rollback in order")
    options = _expect_dict(adapters["options"], "$.adapters.options")
    _exact_keys(options, {"force_health_failure", "force_rollback_failure"}, "$.adapters.options")
    for key, option in options.items():
        if not isinstance(option, bool):
            _fail(f"$.adapters.options.{key} must be boolean")


def validate_spec(value: Any) -> dict[str, Any]:
    """Validate a unit spec and return a defensive copy."""

    assert_no_secrets(value)
    spec = _expect_dict(value, "$")
    _exact_keys(
        spec,
        {
            "schema_id",
            "unit_id",
            "classification",
            "target",
            "extension",
            "provenance",
            "adapters",
            "outputs",
        },
        "$",
    )
    if spec["schema_id"] != SCHEMA_ID:
        _fail(f"$.schema_id must equal {SCHEMA_ID}")
    unit_id = _nonblank(spec["unit_id"], "$.unit_id", 64)
    if len(unit_id) < 3 or not _UNIT_ID.fullmatch(unit_id):
        _fail("$.unit_id must be 3..64 lowercase kebab-case characters")
    classification = spec["classification"]
    if classification not in ("NON_PRODUCTION", "TARGET_BOUND_CANDIDATE"):
        _fail("$.classification must be NON_PRODUCTION or TARGET_BOUND_CANDIDATE")
    binding_state = _validate_target(_expect_dict(spec["target"], "$.target"))
    if classification == "NON_PRODUCTION" and binding_state != "UNADMITTED":
        _fail("NON_PRODUCTION fixtures must keep target.binding_state UNADMITTED")
    if classification == "TARGET_BOUND_CANDIDATE" and binding_state != "BOUND":
        _fail("TARGET_BOUND_CANDIDATE requires target.binding_state BOUND")
    extension = _expect_dict(spec["extension"], "$.extension")
    _exact_keys(
        extension,
        {"display_name", "user_job", "material_outcome", "success_threshold"},
        "$.extension",
    )
    display_name = _nonblank(extension["display_name"], "$.extension.display_name", 120)
    _nonblank(extension["user_job"], "$.extension.user_job")
    _nonblank(extension["material_outcome"], "$.extension.material_outcome")
    _nonblank(extension["success_threshold"], "$.extension.success_threshold")
    if classification == "NON_PRODUCTION" and "NON_PRODUCTION" not in display_name:
        _fail("NON_PRODUCTION fixtures must label extension.display_name explicitly")
    _validate_provenance(_expect_dict(spec["provenance"], "$.provenance"), binding_state)
    _validate_adapters(_expect_dict(spec["adapters"], "$.adapters"))
    outputs = _expect_dict(spec["outputs"], "$.outputs")
    _exact_keys(outputs, {"landing_mode", "distribution_mode"}, "$.outputs")
    if outputs != {"landing_mode": "INERT", "distribution_mode": "INERT"}:
        _fail("v1 landing and distribution outputs must both remain INERT")
    return deepcopy(spec)


def _duplicate_key_guard(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise SpecValidationError(f"duplicate JSON key rejected: {key}")
        result[key] = value
    return result


def _nonfinite_guard(value: str) -> NoReturn:
    raise SpecValidationError(f"non-finite JSON number rejected: {value}")


def load_spec(path: str | Path) -> dict[str, Any]:
    try:
        value = json.loads(
            Path(path).read_text(encoding="utf-8"),
            object_pairs_hook=_duplicate_key_guard,
            parse_constant=_nonfinite_guard,
        )
    except SpecValidationError:
        raise
    except (OSError, json.JSONDecodeError) as error:
        raise SpecValidationError(f"cannot read JSON unit spec: {error}") from error
    return validate_spec(value)


def spec_sha256(spec: dict[str, Any]) -> str:
    return sha256_bytes(canonical_json_bytes(validate_spec(spec)))
