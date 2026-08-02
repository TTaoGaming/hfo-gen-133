"""Deterministic, atomic materialization of inert NON_PRODUCTION units."""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import uuid
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from .canonical import canonical_json_bytes, contains_secret_text, sha256_bytes
from .errors import MaterializationConflict, PathTraversalError, SecretRejected, SpecValidationError
from .lease import is_link_or_reparse
from .spec import validate_spec


_OUTPUTS = {
    "landing.html.tmpl": "landing/index.html",
    "distribution.json.tmpl": "distribution/manifest.json",
    "README.md.tmpl": "distribution/README.md",
    "adapter_stub.py.tmpl": "adapters/adapter_stub.py",
}
_TOKEN = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def package_template_root() -> Path:
    return Path(__file__).resolve().parent.parent / "templates"


def _relative_parts(relative: str) -> tuple[str, ...]:
    path = PurePosixPath(relative)
    if path.is_absolute() or str(path) in ("", ".") or ".." in path.parts or "\\" in relative or ":" in relative:
        raise PathTraversalError(f"unsafe materialization path: {relative!r}")
    return path.parts


def _reject_reparse_ancestors(path: Path) -> None:
    for candidate in (path, *path.parents):
        if candidate.exists() and is_link_or_reparse(candidate):
            raise PathTraversalError(f"path crosses a symlink or reparse point: {candidate}")


def _safe_destination(root: Path, relative: str) -> Path:
    parts = _relative_parts(relative)
    resolved_root = root.resolve(strict=True)
    candidate = root.joinpath(*parts)
    try:
        candidate.resolve(strict=False).relative_to(resolved_root)
    except ValueError as error:
        raise PathTraversalError(f"path escapes materialization root: {relative!r}") from error
    current = root
    for part in parts[:-1]:
        current /= part
        if current.exists() and is_link_or_reparse(current):
            raise PathTraversalError(f"path crosses a reparse point: {relative!r}")
    return candidate


def _markdown(value: str) -> str:
    text = " ".join(value.split()).replace("\\", "\\\\")
    for character in "`*_{}[]()#+-.!|>":
        text = text.replace(character, f"\\{character}")
    return text.replace("<", "&lt;").replace(">", "&gt;")


def _render(template: str, replacements: Mapping[str, str], name: str) -> bytes:
    result = template
    for token, replacement in replacements.items():
        result = result.replace("{{" + token + "}}", replacement)
    unresolved = _TOKEN.search(result)
    if unresolved:
        raise MaterializationConflict(f"template {name} has unresolved token {unresolved.group(0)}")
    if contains_secret_text(result):
        raise SecretRejected(f"rendered template {name} contains credential-like text")
    result = result.replace("\r\n", "\n").replace("\r", "\n")
    return (result.rstrip("\n") + "\n").encode("utf-8")


@dataclass(frozen=True)
class Artifact:
    path: str
    size: int
    sha256: str

    def as_dict(self) -> dict[str, str | int]:
        return {"path": self.path, "size": self.size, "sha256": self.sha256}


@dataclass(frozen=True)
class MaterializationResult:
    output_root: Path
    artifacts: tuple[Artifact, ...]
    tree_sha256: str
    created: bool

    def manifest(self) -> dict[str, Any]:
        return {
            "schema_id": "hfo.gen133.dlc_foss_factory.materialization.v1",
            "classification": "NON_PRODUCTION",
            "output_root": str(self.output_root),
            "artifacts": [item.as_dict() for item in self.artifacts],
            "tree_sha256": self.tree_sha256,
            "created": self.created,
        }


class Materializer:
    def __init__(self, template_root: Path | None = None) -> None:
        requested = Path(template_root) if template_root is not None else package_template_root()
        _reject_reparse_ancestors(requested)
        self.template_root = requested.resolve(strict=True)

    def _template(self, name: str) -> bytes:
        path = _safe_destination(self.template_root, name)
        if is_link_or_reparse(path) or not path.is_file():
            raise MaterializationConflict(f"required template unavailable: {name}")
        return path.read_bytes()

    def render(self, spec: dict[str, Any]) -> dict[str, bytes]:
        checked = validate_spec(spec)
        if checked["classification"] != "NON_PRODUCTION" or checked["target"]["binding_state"] != "UNADMITTED":
            raise SpecValidationError("this route materializes NON_PRODUCTION unadmitted units only")
        extension = checked["extension"]
        raw = {
            "UNIT_ID": checked["unit_id"],
            "DISPLAY_NAME": extension["display_name"],
            "USER_JOB": extension["user_job"],
            "MATERIAL_OUTCOME": extension["material_outcome"],
            "SUCCESS_THRESHOLD": extension["success_threshold"],
        }
        replacements: dict[str, str] = {}
        for key, value in raw.items():
            replacements[f"{key}_HTML"] = html.escape(value, quote=True)
            replacements[f"{key}_JSON"] = json.dumps(value, ensure_ascii=False, allow_nan=False)
            replacements[f"{key}_MARKDOWN"] = _markdown(value)
        outputs: dict[str, bytes] = {}
        for template_name, relative in _OUTPUTS.items():
            source = self._template(template_name)
            if template_name == "adapter_stub.py.tmpl":
                from .adapters import BUILTIN_ADAPTER_STUB

                if source != BUILTIN_ADAPTER_STUB:
                    raise MaterializationConflict("adapter template differs from code authority")
                data = source
            else:
                try:
                    data = _render(source.decode("utf-8"), replacements, template_name)
                except UnicodeDecodeError as error:
                    raise MaterializationConflict(f"template is not UTF-8: {template_name}") from error
            outputs[relative] = data
        return dict(sorted(outputs.items()))

    @staticmethod
    def _artifacts(files: Mapping[str, bytes]) -> tuple[tuple[Artifact, ...], str]:
        artifacts = tuple(
            Artifact(path, len(data), sha256_bytes(data)) for path, data in sorted(files.items())
        )
        tree = sha256_bytes(canonical_json_bytes([item.as_dict() for item in artifacts]))
        return artifacts, tree

    @staticmethod
    def _verify_existing(root: Path, expected: Mapping[str, bytes]) -> None:
        if is_link_or_reparse(root) or not root.is_dir():
            raise MaterializationConflict("existing output is not a plain directory")
        files: set[str] = set()
        directories: set[str] = set()
        for directory, children, names in os.walk(root, followlinks=False):
            base = Path(directory)
            if is_link_or_reparse(base):
                raise MaterializationConflict("output contains a reparse point")
            for name in children:
                child = base / name
                if is_link_or_reparse(child):
                    raise MaterializationConflict("output contains a reparse point")
                directories.add(child.relative_to(root).as_posix())
            for name in names:
                child = base / name
                if is_link_or_reparse(child) or not child.is_file():
                    raise MaterializationConflict("output contains a non-regular file")
                files.add(child.relative_to(root).as_posix())
        expected_dirs = {
            str(parent)
            for path in expected
            for parent in PurePosixPath(path).parents
            if str(parent) not in ("", ".")
        }
        if files != set(expected) or directories != expected_dirs:
            raise MaterializationConflict("existing output tree differs from deterministic templates")
        for relative, data in expected.items():
            if _safe_destination(root, relative).read_bytes() != data:
                raise MaterializationConflict(f"existing output differs at {relative}")

    def materialize(self, spec: dict[str, Any], output_root: str | Path) -> MaterializationResult:
        files = self.render(spec)
        artifacts, tree = self._artifacts(files)
        requested = Path(output_root)
        _reject_reparse_ancestors(requested.parent)
        requested.parent.mkdir(parents=True, exist_ok=True)
        _reject_reparse_ancestors(requested.parent)
        parent = requested.parent.resolve(strict=True)
        target = requested.resolve(strict=False)
        if target.parent != parent or (target.exists() and is_link_or_reparse(target)):
            raise PathTraversalError("output root is not a plain direct child")
        if target.exists():
            self._verify_existing(target, files)
            return MaterializationResult(target, artifacts, tree, False)
        # A short staging name avoids legacy Windows MAX_PATH failures even when
        # the final workspace is a digest-derived name.
        staging = parent / f".stage-{uuid.uuid4().hex[:8]}"
        staging.mkdir()
        promoted = False
        try:
            for relative, data in files.items():
                destination = _safe_destination(staging, relative)
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("xb") as handle:
                    handle.write(data)
                    handle.flush()
                    os.fsync(handle.fileno())
            self._verify_existing(staging, files)
            if target.exists():
                self._verify_existing(target, files)
                return MaterializationResult(target, artifacts, tree, False)
            try:
                os.rename(staging, target)
                promoted = True
            except OSError as error:
                if target.exists():
                    self._verify_existing(target, files)
                    return MaterializationResult(target, artifacts, tree, False)
                raise MaterializationConflict(f"atomic promotion failed: {error}") from error
        finally:
            if not promoted and staging.exists():
                shutil.rmtree(staging)
        return MaterializationResult(target, artifacts, tree, True)
