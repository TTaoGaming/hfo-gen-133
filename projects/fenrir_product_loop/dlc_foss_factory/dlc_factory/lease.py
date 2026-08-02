"""Checkout-local, atomic WIP=1 lease for factory mutations."""

from __future__ import annotations

import os
import re
import stat
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from .canonical import canonical_json_bytes, sha256_bytes
from .errors import WipCollisionError


LEASE_SCHEMA_ID = "hfo.gen133.dlc_foss_factory.wip_lease.v1"
_RUN_ID = re.compile(r"^[0-9a-f]{64}$")
_HOLDER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,159}$")


def package_runs_root() -> Path:
    return Path(__file__).resolve().parent.parent / "runs"


def is_link_or_reparse(path: Path) -> bool:
    try:
        status = os.lstat(path)
    except FileNotFoundError:
        return False
    attributes = getattr(status, "st_file_attributes", 0)
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    return stat.S_ISLNK(status.st_mode) or bool(attributes & reparse_flag)


def _utc_text(clock: Callable[[], datetime] | None) -> str:
    moment = clock() if clock is not None else datetime.now(timezone.utc)
    if not isinstance(moment, datetime) or moment.tzinfo is None:
        raise ValueError("lease clock must return a timezone-aware datetime")
    return moment.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


@dataclass(frozen=True)
class LeaseRecord:
    holder: str
    run_id: str
    lease_id: str
    acquired_utc: str

    def as_dict(self) -> dict[str, str]:
        return {
            "schema_id": LEASE_SCHEMA_ID,
            "holder": self.holder,
            "run_id": self.run_id,
            "lease_id": self.lease_id,
            "acquired_utc": self.acquired_utc,
        }


@dataclass
class WipLease:
    runs_root: Path
    active_dir: Path
    path: Path
    record: LeaseRecord
    _record_bytes: bytes = field(repr=False)
    _released: bool = field(default=False, init=False, repr=False)

    @classmethod
    def acquire(
        cls,
        holder: str,
        run_id: str,
        *,
        runs_root: Path | None = None,
        clock: Callable[[], datetime] | None = None,
    ) -> "WipLease":
        if not isinstance(holder, str) or not _HOLDER.fullmatch(holder):
            raise ValueError("holder must be 1..160 safe identifier characters")
        if not isinstance(run_id, str) or not _RUN_ID.fullmatch(run_id):
            raise ValueError("run_id must be a lowercase 64-hex digest")
        requested = Path(runs_root) if runs_root is not None else package_runs_root()
        if requested.exists() and is_link_or_reparse(requested):
            raise WipCollisionError("runs root is a symlink or reparse point")
        requested.mkdir(parents=True, exist_ok=True)
        root = requested.resolve(strict=True)
        active = root / ".active"
        try:
            # Do not pass a POSIX mode here. On Windows, a restricted token can
            # create a directory whose resulting ACL then denies its own child
            # write. Inherited ACLs preserve atomic mkdir semantics portably.
            active.mkdir()
        except FileExistsError as error:
            record_path = active / "lease.json"
            try:
                detail = f"lease_record_sha256={sha256_bytes(record_path.read_bytes())}"
            except OSError:
                detail = "lease_record=UNAVAILABLE"
            raise WipCollisionError(f"checkout WIP lease already active at {active}; {detail}") from error
        record = LeaseRecord(
            holder=holder,
            run_id=run_id,
            lease_id=uuid.uuid4().hex,
            acquired_utc=_utc_text(clock),
        )
        data = canonical_json_bytes(record.as_dict())
        path = active / "lease.json"
        try:
            with path.open("xb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
        except BaseException:
            try:
                path.unlink(missing_ok=True)
                active.rmdir()
            except OSError:
                pass
            raise
        return cls(root, active, path, record, data)

    @property
    def released(self) -> bool:
        return self._released

    def release(self) -> None:
        if self._released:
            return
        try:
            entries = {entry.name for entry in self.active_dir.iterdir()}
            current = self.path.read_bytes()
        except OSError as error:
            raise WipCollisionError("active lease record is unavailable") from error
        if entries != {"lease.json"} or current != self._record_bytes:
            raise WipCollisionError("active lease ownership changed; refusing release")
        self.path.unlink()
        try:
            self.active_dir.rmdir()
        except OSError as error:
            raise WipCollisionError("lease record removed but WIP directory remains blocked") from error
        self._released = True

    def __enter__(self) -> "WipLease":
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.release()
