#!/usr/bin/env python3
"""Gen-133 lineage task-claim lease manager (EMERGENCY_FORGE build, 2026-08-01).

A distributed mutex over `task_id`, scoped to `lineage_id`, so two agent
lineages never both work the same task concurrently. This is NOT the gen-130
`vault_lease` system (operator-verb access-control gate over action classes
like SEND/SPEND/PUBLISH) -- that system was searched for and found at
`hfo_dev_2026_5_30/hfo_gen_130_forge/scripts/vault_lease/{lease_lib,grant_lease}.py`
but solves a different problem (WHO may perform a gated action) from this one
(WHICH lineage owns a task right now). Built fresh; the atomic-append idiom
(`os.open` with O_CREAT|O_APPEND, `os.fsync`) is ported from that codebase's
`grant_lease.append_row`.

Ledger: append-only JSONL at `state/ssot/leases.jsonl`. Every claim/heartbeat/
release is one row; current holder is derived by replaying the log, never by
mutating a row in place. Mutual exclusion around the read-decide-append
critical section uses an `os.O_CREAT|os.O_EXCL` lockfile (atomic create is
the CAS primitive; no external deps). A stale lock (older than
`lock_stale_seconds`) is broken automatically so a crashed holder cannot wedge
the ledger forever.
"""
from __future__ import annotations

import argparse
import json
import os
import secrets
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

FORGE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LEASES_PATH = FORGE_ROOT / "state" / "ssot" / "leases.jsonl"
DEFAULT_LOCK_PATH = FORGE_ROOT / "state" / "ssot" / "leases.lock"


class LeaseExpired(Exception):
    """Raised by heartbeat() when the lease is not the current live holder."""


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _fmt(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse(value: str) -> datetime:
    s = value.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


class LineageLease:
    def __init__(
        self,
        leases_path: Path | None = None,
        lock_path: Path | None = None,
        lock_timeout_s: float = 10.0,
        lock_stale_s: float = 30.0,
    ) -> None:
        self.leases_path = leases_path or DEFAULT_LEASES_PATH
        self.lock_path = lock_path or DEFAULT_LOCK_PATH
        self.lock_timeout_s = lock_timeout_s
        self.lock_stale_s = lock_stale_s

    # ------------------------------------------------------------------
    # Mutex: atomic O_CREAT|O_EXCL lockfile. Breaks stale locks by mtime.
    # ------------------------------------------------------------------
    def _acquire_mutex(self) -> None:
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        deadline = time.monotonic() + self.lock_timeout_s
        while True:
            try:
                fd = os.open(str(self.lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode("utf-8"))
                os.close(fd)
                return
            except FileExistsError:
                try:
                    age = time.time() - self.lock_path.stat().st_mtime
                except OSError:
                    age = 0.0
                if age > self.lock_stale_s:
                    try:
                        self.lock_path.unlink()
                    except OSError:
                        pass
                    continue
                if time.monotonic() >= deadline:
                    raise TimeoutError(
                        f"could not acquire lease mutex within {self.lock_timeout_s}s "
                        f"({self.lock_path})"
                    )
                time.sleep(0.05)

    def _release_mutex(self) -> None:
        try:
            self.lock_path.unlink()
        except OSError:
            pass

    # ------------------------------------------------------------------
    # Ledger IO
    # ------------------------------------------------------------------
    def _read_rows(self) -> list[dict[str, Any]]:
        if not self.leases_path.is_file():
            return []
        out: list[dict[str, Any]] = []
        for line in self.leases_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict):
                out.append(row)
        return out

    def _append_row(self, row: dict[str, Any]) -> None:
        self.leases_path.parent.mkdir(parents=True, exist_ok=True)
        payload = (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        flags = os.O_WRONLY | os.O_CREAT | os.O_APPEND | getattr(os, "O_BINARY", 0)
        fd = os.open(str(self.leases_path), flags, 0o600)
        try:
            os.write(fd, payload)
            os.fsync(fd)
        finally:
            os.close(fd)

    # ------------------------------------------------------------------
    # State derivation: latest event per task_id wins (append-only log).
    # ------------------------------------------------------------------
    @staticmethod
    def _holder_for_task(rows: list[dict[str, Any]], task_id: str) -> dict[str, Any] | None:
        holder: dict[str, Any] | None = None
        for row in rows:
            if row.get("task_id") != task_id:
                continue
            event = row.get("event")
            if event in ("claim", "heartbeat"):
                holder = row
            elif event == "release" and holder is not None and row.get("lease_token") == holder.get("lease_token"):
                holder = None
        return holder

    @staticmethod
    def _row_for_token(rows: list[dict[str, Any]], lease_token: str) -> dict[str, Any] | None:
        latest: dict[str, Any] | None = None
        for row in rows:
            if row.get("lease_token") != lease_token:
                continue
            if row.get("event") in ("claim", "heartbeat", "release"):
                latest = row
        return latest

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def claim(self, task_id: str, lineage_id: str, ttl_seconds: int) -> str | None:
        """Atomically claim task_id for lineage_id. Returns a lease_token, or
        None if a DIFFERENT lineage already holds a live (non-expired) claim.
        """
        self._acquire_mutex()
        try:
            now = utc_now()
            rows = self._read_rows()
            holder = self._holder_for_task(rows, task_id)
            if holder is not None:
                holder_lineage = holder.get("lineage_id")
                try:
                    expires = _parse(str(holder.get("expires_utc")))
                except (ValueError, TypeError):
                    expires = now  # unparseable -> treat as expired
                if holder_lineage != lineage_id and expires > now:
                    return None  # held by another lineage, still live
            lease_token = secrets.token_hex(16)
            row = {
                "event": "claim",
                "task_id": task_id,
                "lineage_id": lineage_id,
                "lease_token": lease_token,
                "claimed_utc": _fmt(now),
                "expires_utc": _fmt(now + timedelta(seconds=ttl_seconds)),
                "ttl_seconds": ttl_seconds,
            }
            self._append_row(row)
            return lease_token
        finally:
            self._release_mutex()

    def heartbeat(self, lease_token: str, ttl_seconds: int | None = None) -> str:
        """Extend a live lease. Returns the new expires_utc string, or raises
        LeaseExpired if lease_token is not the current live holder of its task.
        """
        self._acquire_mutex()
        try:
            now = utc_now()
            rows = self._read_rows()
            prior = self._row_for_token(rows, lease_token)
            if prior is None or prior.get("event") == "release":
                raise LeaseExpired(f"lease_token {lease_token} not found or already released")
            task_id = prior.get("task_id")
            current_holder = self._holder_for_task(rows, str(task_id))
            if current_holder is None or current_holder.get("lease_token") != lease_token:
                raise LeaseExpired(f"lease_token {lease_token} is not the current holder of task {task_id}")
            try:
                expires = _parse(str(prior.get("expires_utc")))
            except (ValueError, TypeError):
                expires = now
            if expires <= now:
                raise LeaseExpired(f"lease_token {lease_token} expired at {prior.get('expires_utc')}")
            ttl = ttl_seconds if ttl_seconds is not None else int(prior.get("ttl_seconds", 60))
            new_expires = now + timedelta(seconds=ttl)
            row = {
                "event": "heartbeat",
                "task_id": task_id,
                "lineage_id": prior.get("lineage_id"),
                "lease_token": lease_token,
                "claimed_utc": prior.get("claimed_utc"),
                "expires_utc": _fmt(new_expires),
                "ttl_seconds": ttl,
            }
            self._append_row(row)
            return row["expires_utc"]
        finally:
            self._release_mutex()

    def release(self, lease_token: str) -> None:
        """Idempotent release. No error if already released or unknown."""
        self._acquire_mutex()
        try:
            now = utc_now()
            rows = self._read_rows()
            prior = self._row_for_token(rows, lease_token)
            if prior is None or prior.get("event") == "release":
                return
            row = {
                "event": "release",
                "task_id": prior.get("task_id"),
                "lineage_id": prior.get("lineage_id"),
                "lease_token": lease_token,
                "released_utc": _fmt(now),
            }
            self._append_row(row)
        finally:
            self._release_mutex()

    def expired_locks(self, now_utc: datetime | None = None) -> list[dict[str, Any]]:
        """Read-only: current holders (per task_id) whose expires_utc has
        passed but who have not been released. No mutex needed (read-only).
        """
        now = now_utc or utc_now()
        rows = self._read_rows()
        task_ids = {row.get("task_id") for row in rows if row.get("event") == "claim"}
        expired: list[dict[str, Any]] = []
        for task_id in task_ids:
            holder = self._holder_for_task(rows, str(task_id))
            if holder is None:
                continue
            try:
                expires = _parse(str(holder.get("expires_utc")))
            except (ValueError, TypeError):
                expired.append(holder)
                continue
            if expires <= now:
                expired.append(holder)
        return expired


def _cli(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Gen-133 lineage task-claim lease manager")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("claim")
    c.add_argument("task_id")
    c.add_argument("lineage_id")
    c.add_argument("--ttl", type=int, default=60)

    h = sub.add_parser("heartbeat")
    h.add_argument("lease_token")
    h.add_argument("--ttl", type=int, default=None)

    r = sub.add_parser("release")
    r.add_argument("lease_token")

    sub.add_parser("expired")

    args = ap.parse_args(argv)
    lease = LineageLease()

    if args.cmd == "claim":
        token = lease.claim(args.task_id, args.lineage_id, args.ttl)
        print(json.dumps({"lease_token": token}))
        return 0 if token else 1
    if args.cmd == "heartbeat":
        try:
            expires = lease.heartbeat(args.lease_token, args.ttl)
        except LeaseExpired as exc:
            print(json.dumps({"error": str(exc)}))
            return 1
        print(json.dumps({"expires_utc": expires}))
        return 0
    if args.cmd == "release":
        lease.release(args.lease_token)
        print(json.dumps({"released": True}))
        return 0
    if args.cmd == "expired":
        print(json.dumps(lease.expired_locks(), default=str))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(_cli())
