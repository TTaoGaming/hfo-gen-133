#!/usr/bin/env python3
"""Read-only external-signal monitor for published HFO artifacts.

One lead process owns all state writes. Six persistent worker processes poll
Cloudflare, itch.io, Hacker News, Reddit, GitHub, and Stripe concurrently once
per tick. The default run is 24 ticks, 30 minutes apart (12 hours total).

Truth boundary:
* Missing/private analytics are recorded as UNKNOWN (JSON null), never zero.
* ``wrangler pages deployment list`` proves deployment metadata only; it does
  not expose Cloudflare request counts and is never used as a traffic proxy.
* No worker posts, sends, deploys, purchases, or persists credentials.
"""

from __future__ import annotations

import argparse
import base64
import concurrent.futures
import email.utils
import json
import math
import multiprocessing
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENTS = ROOT / "state" / "experiments"
PUBLICATIONS = EXPERIMENTS / "publications.jsonl"
FITNESS = EXPERIMENTS / "fitness.jsonl"
RANKING = EXPERIMENTS / "fitness_rank_24h.json"
STATUS = EXPERIMENTS / "fitness_monitor_status.json"
PID_FILE = EXPERIMENTS / "fitness_monitor.pid"
LOCK_FILE = EXPERIMENTS / "fitness_monitor.lock"
REPORT_DIR = ROOT / "state" / "olrun"

DEFAULT_INTERVAL_SECONDS = 30 * 60
DEFAULT_DURATION_HOURS = 12.0
DEFAULT_TICKS = 24
USER_AGENT = "hfo-external-signal-monitor/1.0 (read-only; operator-owned artifacts)"

SOURCE_NAMES = ("cloudflare", "itchio", "hn", "reddit", "github", "stripe")

CLOUDFLARE_PROJECTS = {
    "hfo-games": "https://hfo-games.pages.dev/",
    "hfo-suika-dlc-5-timer-mode": "https://hfo-suika-dlc-5-timer-mode.pages.dev/",
    "hfo-suika-dlc-6-gravity-flip": "https://hfo-suika-dlc-6-gravity-flip.pages.dev/",
    "hfo-suika-dlc-7-boss-fruits": "https://hfo-suika-dlc-7-boss-fruits.pages.dev/",
    "hfo-suika-dlc-8-character-select": "https://hfo-suika-dlc-8-character-select.pages.dev/",
    "hfo-suika-dlc-9-daily-seed": "https://hfo-suika-dlc-9-daily-seed.pages.dev/",
    "hfo-suika-dlc-10-combo-burst": "https://hfo-suika-dlc-10-combo-burst.pages.dev/",
    "hfo-suika-dlc-11-reverse-suika": "https://hfo-suika-dlc-11-reverse-suika.pages.dev/",
    "hfo-suika-dlc-12-gauntlet-mode": "https://hfo-suika-dlc-12-gauntlet-mode.pages.dev/",
    "hfo-suika-dlc-13-relic-draft": "https://hfo-suika-dlc-13-relic-draft.pages.dev/",
    "hfo-suika-dlc-14-joker-hands": "https://hfo-suika-dlc-14-joker-hands.pages.dev/",
    "hfo-suika-dlc-15-evolution-frenzy": "https://hfo-suika-dlc-15-evolution-frenzy.pages.dev/",
    "hfo-suika-dlc-16-curse-pacts": "https://hfo-suika-dlc-16-curse-pacts.pages.dev/",
}

GITHUB_REPOS = {
    "TTaoGaming/agentreleasegate-oss": "https://github.com/TTaoGaming/agentreleasegate-oss",
    "TTaoGaming/hfo-gen-133": "https://github.com/TTaoGaming/hfo-gen-133",
}

THRESHOLDS = {
    ("itchio", "downloads"): 100,
    ("hn", "score"): 20,
    ("reddit", "upvotes"): 50,
    ("github", "stars"): 10,
    ("stripe", "paid_charges_24h"): 0,
    ("cloudflare", "requests_24h"): 1000,
}


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_z(value: datetime | None = None) -> str:
    value = value or utc_now()
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_ts(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def json_line(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json_line(row) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def source_for_url(url: str) -> str | None:
    try:
        parsed = urllib.parse.urlparse(url)
    except ValueError:
        return None
    host = parsed.netloc.lower().split(":", 1)[0]
    if host.endswith(".pages.dev"):
        return "cloudflare"
    if host == "itch.io" or host.endswith(".itch.io"):
        return "itchio"
    if host in {"news.ycombinator.com", "hacker-news.firebaseio.com"}:
        return "hn"
    if host == "reddit.com" or host.endswith(".reddit.com") or host == "redd.it":
        return "reddit"
    if host == "github.com":
        return "github"
    return None


def canonical_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url.strip())
    scheme = (parsed.scheme or "https").lower()
    host = parsed.netloc.lower()
    path = parsed.path or "/"
    query = parsed.query
    if source_for_url(url) == "reddit":
        query = ""
    return urllib.parse.urlunparse((scheme, host, path, "", query, ""))


def artifact_id_for(source: str, url: str, explicit: Any = None) -> str:
    if isinstance(explicit, str) and explicit.strip():
        return explicit.strip()
    parsed = urllib.parse.urlparse(url)
    if source == "cloudflare":
        return parsed.netloc.removesuffix(".pages.dev")
    if source == "github":
        parts = [p for p in parsed.path.split("/") if p]
        return "/".join(parts[:2]) if len(parts) >= 2 else parsed.netloc + parsed.path
    if source == "hn":
        match = re.search(r"(?:[?&]id=|/item/)(\d+)", url)
        return f"hn:{match.group(1)}" if match else url
    if source == "reddit":
        match = re.search(r"/comments/([a-z0-9]+)", parsed.path, re.IGNORECASE)
        if not match and parsed.netloc.lower() == "redd.it":
            match = re.search(r"/([a-z0-9]+)", parsed.path, re.IGNORECASE)
        return f"reddit:{match.group(1)}" if match else url
    if source == "itchio":
        return "itchio:" + (parsed.netloc + parsed.path).strip("/")
    return url


def extract_urls(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, str):
        found.extend(re.findall(r"https?://[^\s\]\[<>{}\"']+", value))
    elif isinstance(value, dict):
        for child in value.values():
            found.extend(extract_urls(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(extract_urls(child))
    return found


def load_artifacts() -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any]]:
    by_source: dict[str, list[dict[str, Any]]] = {source: [] for source in SOURCE_NAMES}
    input_status: dict[str, Any] = {
        "path": str(PUBLICATIONS.relative_to(ROOT)).replace("\\", "/"),
        "status": "present" if PUBLICATIONS.exists() else "missing",
        "rows_read": 0,
        "malformed_rows": 0,
        "recognized_urls": 0,
        "ignored_urls": 0,
    }

    for project, url in CLOUDFLARE_PROJECTS.items():
        by_source["cloudflare"].append(
            {"artifact_id": project, "url": url, "project_name": project, "standing": True}
        )
    for repo, url in GITHUB_REPOS.items():
        by_source["github"].append(
            {"artifact_id": repo, "url": url, "repo": repo, "standing": True}
        )
    by_source["stripe"].append(
        {"artifact_id": "stripe:paid_charges_24h", "url": None, "standing": True}
    )

    if PUBLICATIONS.exists():
        with PUBLICATIONS.open("r", encoding="utf-8", errors="replace") as handle:
            for raw in handle:
                if not raw.strip():
                    continue
                input_status["rows_read"] += 1
                try:
                    parsed: Any = json.loads(raw)
                except json.JSONDecodeError:
                    input_status["malformed_rows"] += 1
                    continue
                explicit_id = None
                if isinstance(parsed, dict):
                    explicit_id = parsed.get("artifact_id") or parsed.get("id") or parsed.get("name")
                for raw_url in extract_urls(parsed):
                    url = raw_url.rstrip(".,;:")
                    source = source_for_url(url)
                    if source is None:
                        input_status["ignored_urls"] += 1
                        continue
                    if source == "stripe":
                        continue
                    normalized = canonical_url(url)
                    artifact = {
                        "artifact_id": artifact_id_for(source, normalized, explicit_id),
                        "url": normalized,
                        "standing": False,
                    }
                    if source == "cloudflare":
                        artifact["project_name"] = urllib.parse.urlparse(normalized).netloc.removesuffix(".pages.dev")
                    elif source == "github":
                        parts = [p for p in urllib.parse.urlparse(normalized).path.split("/") if p]
                        if len(parts) < 2:
                            input_status["ignored_urls"] += 1
                            continue
                        artifact["repo"] = "/".join(parts[:2])
                    by_source[source].append(artifact)
                    input_status["recognized_urls"] += 1

    for source, artifacts in by_source.items():
        deduped: list[dict[str, Any]] = []
        seen: set[str] = set()
        for artifact in artifacts:
            key = canonical_url(artifact["url"]) if artifact.get("url") else artifact["artifact_id"]
            if key in seen:
                continue
            seen.add(key)
            deduped.append(artifact)
        by_source[source] = deduped
    return by_source, input_status


def http_get_json(url: str, *, headers: dict[str, str] | None = None, timeout: int = 20) -> tuple[Any, dict[str, str]]:
    request_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    request_headers.update(headers or {})
    request = urllib.request.Request(url, headers=request_headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(4 * 1024 * 1024)
            response_headers = {key.lower(): value for key, value in response.headers.items()}
            return json.loads(body.decode("utf-8", errors="replace")), response_headers
    except urllib.error.HTTPError as exc:
        response_headers = {key.lower(): value for key, value in exc.headers.items()}
        if exc.code == 429 or http_error_requires_backoff(response_headers):
            raise RateLimitError(
                f"HTTP {exc.code}", retry_after=rate_limit_retry_after(response_headers)
            ) from None
        raise PollError(f"HTTP {exc.code}") from None
    except urllib.error.URLError as exc:
        raise PollError(f"network error: {getattr(exc, 'reason', type(exc).__name__)}") from None
    except json.JSONDecodeError:
        raise PollError("response was not valid JSON") from None


def http_get_text(url: str, *, timeout: int = 20) -> tuple[str, dict[str, str]]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(4 * 1024 * 1024)
            return body.decode("utf-8", errors="replace"), {
                key.lower(): value for key, value in response.headers.items()
            }
    except urllib.error.HTTPError as exc:
        response_headers = {key.lower(): value for key, value in exc.headers.items()}
        if exc.code == 429 or http_error_requires_backoff(response_headers):
            raise RateLimitError(
                f"HTTP {exc.code}", retry_after=rate_limit_retry_after(response_headers)
            ) from None
        raise PollError(f"HTTP {exc.code}") from None
    except urllib.error.URLError as exc:
        raise PollError(f"network error: {getattr(exc, 'reason', type(exc).__name__)}") from None


class PollError(RuntimeError):
    pass


class RateLimitError(PollError):
    def __init__(self, message: str, retry_after: Any = None):
        super().__init__(message)
        self.retry_after = parse_retry_after(retry_after)


def parse_retry_after(value: Any) -> int | None:
    if value is None:
        return None
    try:
        return max(0, int(float(str(value))))
    except (TypeError, ValueError):
        try:
            parsed = email.utils.parsedate_to_datetime(str(value))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return max(0, int((parsed.astimezone(timezone.utc) - utc_now()).total_seconds()))
        except (TypeError, ValueError, OverflowError):
            return None


def remaining_rate(headers: dict[str, str]) -> float | None:
    raw = headers.get("x-ratelimit-remaining") or headers.get("ratelimit-remaining")
    if raw is None:
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def rate_limit_retry_after(headers: dict[str, str]) -> int | None:
    retry_after = parse_retry_after(headers.get("retry-after"))
    if retry_after is not None:
        return retry_after
    reset = headers.get("x-ratelimit-reset") or headers.get("ratelimit-reset")
    if reset:
        try:
            return max(0, int(float(reset) - time.time()))
        except ValueError:
            return None
    return None


def http_error_requires_backoff(headers: dict[str, str]) -> bool:
    remaining = remaining_rate(headers)
    return (remaining is not None and remaining <= 0) or "retry-after" in headers


def rate_limit_guard(headers: dict[str, str]) -> None:
    remaining = remaining_rate(headers)
    if remaining is not None and remaining <= 0:
        raise RateLimitError(
            "rate-limit remaining reached zero",
            retry_after=rate_limit_retry_after(headers),
        )


def observation(
    artifact: dict[str, Any],
    source: str,
    metric_name: str,
    value: Any,
    status: str,
    **details: Any,
) -> dict[str, Any]:
    return {
        "artifact_id": artifact["artifact_id"],
        "url": artifact.get("url"),
        "source": source,
        "metric_name": metric_name,
        "value": value,
        "status": status,
        "details": details,
    }


def run_cloudflare(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    rate_limited = False
    retry_after = None
    executable = shutil.which("wrangler.cmd") or shutil.which("wrangler")
    for artifact in artifacts:
        if rate_limited:
            rows.append(observation(artifact, "cloudflare", "requests_24h", None, "skipped_rate_limit"))
            continue
        if not executable:
            rows.append(
                observation(
                    artifact,
                    "cloudflare",
                    "requests_24h",
                    None,
                    "unknown_no_wrangler",
                    reason="wrangler executable not found",
                )
            )
            continue
        project = artifact.get("project_name")
        try:
            result = subprocess.run(
                [executable, "pages", "deployment", "list", "--project-name", project, "--json"],
                capture_output=True,
                text=True,
                timeout=90,
                check=False,
                env=os.environ.copy(),
            )
            combined = ((result.stdout or "") + "\n" + (result.stderr or "")).strip()
            if result.returncode != 0:
                if re.search(r"(?:rate.?limit|HTTP\s*429|too many requests)", combined, re.IGNORECASE):
                    rate_limited = True
                    retry_after = DEFAULT_INTERVAL_SECONDS
                    rows.append(
                        observation(artifact, "cloudflare", "requests_24h", None, "rate_limited", reason="Wrangler reported a rate limit")
                    )
                else:
                    rows.append(
                        observation(
                            artifact,
                            "cloudflare",
                            "requests_24h",
                            None,
                            "unknown_command_error",
                            reason=f"wrangler deployment list exited {result.returncode}",
                        )
                    )
                continue
            raw = result.stdout.strip()
            start = raw.find("[")
            deployments = json.loads(raw[start:]) if start >= 0 else []
            cutoff = utc_now() - timedelta(hours=24)
            recent = 0
            for deployment in deployments if isinstance(deployments, list) else []:
                created = parse_ts(deployment.get("created_on") or deployment.get("created_at")) if isinstance(deployment, dict) else None
                if created and created >= cutoff:
                    recent += 1
            rows.append(
                observation(
                    artifact,
                    "cloudflare",
                    "requests_24h",
                    None,
                    "unknown_metric_not_exposed",
                    project_name=project,
                    deployment_list_ok=True,
                    deployments_returned=len(deployments) if isinstance(deployments, list) else None,
                    deployments_created_24h=recent,
                    reason="wrangler pages deployment list exposes deployments, not request analytics",
                )
            )
        except subprocess.TimeoutExpired:
            rows.append(observation(artifact, "cloudflare", "requests_24h", None, "unknown_timeout", project_name=project))
        except (json.JSONDecodeError, OSError) as exc:
            rows.append(
                observation(
                    artifact,
                    "cloudflare",
                    "requests_24h",
                    None,
                    "unknown_parse_error",
                    project_name=project,
                    reason=type(exc).__name__,
                )
            )
    return worker_result("cloudflare", rows, rate_limited, retry_after)


ITCH_PATTERNS = {
    "downloads": [
        re.compile(r'"downloads_count"\s*:\s*(\d+)', re.IGNORECASE),
        re.compile(r'data-downloads-count=["\'](\d+)["\']', re.IGNORECASE),
        re.compile(r'\b([\d,]+)\s+downloads?\b', re.IGNORECASE),
    ],
    "views": [
        re.compile(r'"views_count"\s*:\s*(\d+)', re.IGNORECASE),
        re.compile(r'data-views-count=["\'](\d+)["\']', re.IGNORECASE),
        re.compile(r'\b([\d,]+)\s+views?\b', re.IGNORECASE),
    ],
}


def parse_public_itch_metric(html: str, name: str) -> int | None:
    for pattern in ITCH_PATTERNS[name]:
        match = pattern.search(html)
        if match:
            try:
                return int(match.group(1).replace(",", ""))
            except ValueError:
                continue
    return None


def run_itchio(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for index, artifact in enumerate(artifacts):
        try:
            html, headers = http_get_text(artifact["url"])
            rate_limit_guard(headers)
            downloads = parse_public_itch_metric(html, "downloads")
            views = parse_public_itch_metric(html, "views")
            status = "ok" if downloads is not None else "unknown_not_public"
            rows.append(
                observation(
                    artifact,
                    "itchio",
                    "downloads",
                    downloads,
                    status,
                    views=views,
                    reason=None if downloads is not None else "public project HTML exposes no unambiguous download count",
                )
            )
        except RateLimitError as exc:
            rows.append(observation(artifact, "itchio", "downloads", None, "rate_limited", reason=str(exc)))
            for later in artifacts[index + 1 :]:
                rows.append(observation(later, "itchio", "downloads", None, "skipped_rate_limit"))
            return worker_result("itchio", rows, True, exc.retry_after)
        except PollError as exc:
            rows.append(observation(artifact, "itchio", "downloads", None, "unknown_error", reason=str(exc)))
    return worker_result("itchio", rows)


def hn_item_id(url: str) -> str | None:
    match = re.search(r"(?:[?&]id=|/item/)(\d+)", url)
    return match.group(1) if match else None


def run_hn(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for index, artifact in enumerate(artifacts):
        item_id = hn_item_id(artifact["url"])
        if not item_id:
            rows.append(observation(artifact, "hn", "score", None, "unknown_bad_url", reason="HN item id not found"))
            continue
        try:
            payload, headers = http_get_json(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json")
            rate_limit_guard(headers)
            if not isinstance(payload, dict):
                raise PollError("HN item was missing")
            rows.append(
                observation(
                    artifact,
                    "hn",
                    "score",
                    payload.get("score") if is_number(payload.get("score")) else None,
                    "ok",
                    item_id=item_id,
                    descendants=payload.get("descendants") if is_number(payload.get("descendants")) else 0,
                    item_type=payload.get("type"),
                    deleted=bool(payload.get("deleted")),
                    dead=bool(payload.get("dead")),
                )
            )
        except RateLimitError as exc:
            rows.append(observation(artifact, "hn", "score", None, "rate_limited", reason=str(exc)))
            for later in artifacts[index + 1 :]:
                rows.append(observation(later, "hn", "score", None, "skipped_rate_limit"))
            return worker_result("hn", rows, True, exc.retry_after)
        except PollError as exc:
            rows.append(observation(artifact, "hn", "score", None, "unknown_error", reason=str(exc)))
    return worker_result("hn", rows)


def reddit_post_id(url: str) -> str | None:
    parsed = urllib.parse.urlparse(url)
    match = re.search(r"/comments/([a-z0-9]+)", parsed.path, re.IGNORECASE)
    if not match and parsed.netloc.lower() == "redd.it":
        match = re.search(r"/([a-z0-9]+)", parsed.path, re.IGNORECASE)
    return match.group(1) if match else None


def run_reddit(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for index, artifact in enumerate(artifacts):
        post_id = reddit_post_id(artifact["url"])
        if not post_id:
            rows.append(observation(artifact, "reddit", "upvotes", None, "unknown_bad_url", reason="Reddit post id not found"))
            continue
        try:
            payload, headers = http_get_json(
                f"https://www.reddit.com/comments/{post_id}.json?raw_json=1&limit=1&depth=0"
            )
            rate_limit_guard(headers)
            post = payload[0]["data"]["children"][0]["data"]
            upvotes = post.get("ups")
            rows.append(
                observation(
                    artifact,
                    "reddit",
                    "upvotes",
                    upvotes if is_number(upvotes) else None,
                    "ok",
                    post_id=post_id,
                    num_comments=post.get("num_comments") if is_number(post.get("num_comments")) else None,
                    score=post.get("score") if is_number(post.get("score")) else None,
                    upvote_ratio=post.get("upvote_ratio") if is_number(post.get("upvote_ratio")) else None,
                    rate_limit_remaining=remaining_rate(headers),
                )
            )
        except RateLimitError as exc:
            rows.append(observation(artifact, "reddit", "upvotes", None, "rate_limited", reason=str(exc)))
            for later in artifacts[index + 1 :]:
                rows.append(observation(later, "reddit", "upvotes", None, "skipped_rate_limit"))
            return worker_result("reddit", rows, True, exc.retry_after)
        except (PollError, KeyError, IndexError, TypeError) as exc:
            rows.append(observation(artifact, "reddit", "upvotes", None, "unknown_error", reason=str(exc)))
    return worker_result("reddit", rows)


def split_gh_response(text: str) -> tuple[dict[str, str], Any]:
    normalized = text.replace("\r\n", "\n")
    body_at = normalized.find("{")
    if body_at < 0:
        raise PollError("gh api response had no JSON body")
    header_text = normalized[:body_at]
    headers: dict[str, str] = {}
    for line in header_text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip().lower()] = value.strip()
    try:
        return headers, json.loads(normalized[body_at:])
    except json.JSONDecodeError:
        raise PollError("gh api response body was not valid JSON") from None


def run_github(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    executable = shutil.which("gh.exe") or shutil.which("gh")
    if not executable:
        for artifact in artifacts:
            rows.append(observation(artifact, "github", "stars", None, "unknown_no_gh", reason="gh executable not found"))
        return worker_result("github", rows)
    for index, artifact in enumerate(artifacts):
        repo = artifact.get("repo")
        try:
            result = subprocess.run(
                [executable, "api", "--include", f"repos/{repo}"],
                capture_output=True,
                text=True,
                timeout=45,
                check=False,
            )
            combined = ((result.stdout or "") + "\n" + (result.stderr or "")).strip()
            if result.returncode != 0:
                if re.search(r"(?:rate.?limit|HTTP\s*429|too many requests)", combined, re.IGNORECASE):
                    raise RateLimitError("gh api reported a rate limit", DEFAULT_INTERVAL_SECONDS)
                raise PollError(f"gh api exited {result.returncode}")
            headers, payload = split_gh_response(result.stdout)
            rate_limit_guard(headers)
            stars = payload.get("stargazers_count")
            rows.append(
                observation(
                    artifact,
                    "github",
                    "stars",
                    stars if is_number(stars) else None,
                    "ok",
                    repo=repo,
                    forks=payload.get("forks_count") if is_number(payload.get("forks_count")) else None,
                    subscribers=payload.get("subscribers_count") if is_number(payload.get("subscribers_count")) else None,
                    rate_limit_remaining=remaining_rate(headers),
                    rate_limit_reset=headers.get("x-ratelimit-reset"),
                )
            )
        except RateLimitError as exc:
            rows.append(observation(artifact, "github", "stars", None, "rate_limited", repo=repo, reason=str(exc)))
            for later in artifacts[index + 1 :]:
                rows.append(observation(later, "github", "stars", None, "skipped_rate_limit"))
            return worker_result("github", rows, True, exc.retry_after)
        except (PollError, subprocess.TimeoutExpired, OSError) as exc:
            rows.append(observation(artifact, "github", "stars", None, "unknown_error", repo=repo, reason=type(exc).__name__ if not str(exc) else str(exc)))
    return worker_result("github", rows)


def stripe_page(key: str, created_gte: int, starting_after: str | None = None) -> tuple[Any, dict[str, str]]:
    query: dict[str, Any] = {"created[gte]": created_gte, "limit": 100}
    if starting_after:
        query["starting_after"] = starting_after
    url = "https://api.stripe.com/v1/charges?" + urllib.parse.urlencode(query)
    encoded = base64.b64encode((key + ":").encode("utf-8")).decode("ascii")
    return http_get_json(url, headers={"Authorization": "Basic " + encoded})


def run_stripe(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    artifact = artifacts[0]
    key = os.environ.get("STRIPE_API_KEY")
    if not key:
        return worker_result(
            "stripe",
            [
                observation(
                    artifact,
                    "stripe",
                    "paid_charges_24h",
                    None,
                    "skipped_no_key",
                    reason="STRIPE_API_KEY is absent",
                )
            ],
        )
    created_gte = int((utc_now() - timedelta(hours=24)).timestamp())
    paid = 0
    pages = 0
    starting_after = None
    try:
        while True:
            payload, headers = stripe_page(key, created_gte, starting_after)
            rate_limit_guard(headers)
            pages += 1
            charges = payload.get("data") if isinstance(payload, dict) else None
            if not isinstance(charges, list):
                raise PollError("Stripe charges response had no data list")
            paid += sum(1 for charge in charges if isinstance(charge, dict) and charge.get("paid") is True)
            if not payload.get("has_more"):
                break
            if not charges or not isinstance(charges[-1].get("id"), str):
                raise PollError("Stripe pagination cursor missing")
            starting_after = charges[-1]["id"]
        return worker_result(
            "stripe",
            [observation(artifact, "stripe", "paid_charges_24h", paid, "ok", pages=pages)],
        )
    except RateLimitError as exc:
        return worker_result(
            "stripe",
            [observation(artifact, "stripe", "paid_charges_24h", None, "rate_limited", reason=str(exc))],
            True,
            exc.retry_after,
        )
    except PollError as exc:
        return worker_result(
            "stripe",
            [observation(artifact, "stripe", "paid_charges_24h", None, "unknown_error", reason=str(exc))],
        )


POLLERS = {
    "cloudflare": run_cloudflare,
    "itchio": run_itchio,
    "hn": run_hn,
    "reddit": run_reddit,
    "github": run_github,
    "stripe": run_stripe,
}


def worker_result(
    source: str,
    rows: list[dict[str, Any]],
    rate_limited: bool = False,
    retry_after: int | None = None,
) -> dict[str, Any]:
    return {
        "source": source,
        "worker_pid": os.getpid(),
        "observations": rows,
        "rate_limited": rate_limited,
        "retry_after_seconds": retry_after,
    }


def run_source_worker(source: str, artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    try:
        return POLLERS[source](artifacts)
    except Exception as exc:  # a worker crash becomes truthful UNKNOWN rows
        rows = [
            observation(
                artifact,
                source,
                {
                    "cloudflare": "requests_24h",
                    "itchio": "downloads",
                    "hn": "score",
                    "reddit": "upvotes",
                    "github": "stars",
                    "stripe": "paid_charges_24h",
                }[source],
                None,
                "unknown_worker_crash",
                reason=f"{type(exc).__name__}: {str(exc)[:240]}",
            )
            for artifact in artifacts
        ]
        return worker_result(source, rows)


def run_source_worker_synchronized(source: str, artifacts: list[dict[str, Any]], barrier: Any) -> dict[str, Any]:
    """Force all six source tasks to occupy distinct processes per tick."""
    barrier.wait(timeout=120)
    return run_source_worker(source, artifacts)


def load_history() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not FITNESS.exists():
        return rows
    with FITNESS.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict):
                rows.append(row)
    return rows


def enrich_rows(
    observations: list[dict[str, Any]],
    history: list[dict[str, Any]],
    tick_time: datetime,
    run_id: str,
    tick_index: int,
) -> list[dict[str, Any]]:
    indexed: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for prior in history:
        key = (str(prior.get("artifact_id")), str(prior.get("metric_name")))
        indexed.setdefault(key, []).append(prior)

    rows: list[dict[str, Any]] = []
    cutoff = tick_time - timedelta(hours=24)
    for item in observations:
        key = (item["artifact_id"], item["metric_name"])
        priors = indexed.get(key, [])
        numeric_priors = [row for row in priors if is_number(row.get("value"))]
        last = numeric_priors[-1] if numeric_priors else None
        baseline_candidates = [
            row
            for row in numeric_priors
            if (parse_ts(row.get("ts_utc")) is not None and parse_ts(row.get("ts_utc")) <= cutoff)
        ]
        baseline = baseline_candidates[-1] if baseline_candidates else None
        value = item.get("value")
        delta_last = value - last["value"] if is_number(value) and last else None
        delta_24h = value - baseline["value"] if is_number(value) and baseline else None
        rows.append(
            {
                "ts_utc": iso_z(tick_time),
                "artifact_id": item["artifact_id"],
                "source": item["source"],
                "metric_name": item["metric_name"],
                "value": value,
                "delta_from_last": delta_last,
                "cumulative": value if is_number(value) else None,
                "delta_24h": delta_24h,
                "rank_24h": None,
                "status": item["status"],
                "url": item.get("url"),
                "details": item.get("details") or {},
                "run_id": run_id,
                "tick_index": tick_index,
            }
        )

    ranked = sorted(
        [row for row in rows if is_number(row.get("delta_24h"))],
        key=lambda row: (-row["delta_24h"], row["artifact_id"], row["metric_name"]),
    )
    last_value: float | int | None = None
    rank = 0
    for index, row in enumerate(ranked, start=1):
        if last_value is None or row["delta_24h"] != last_value:
            rank = index
            last_value = row["delta_24h"]
        row["rank_24h"] = rank
    return rows


def threshold_winners(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    winners: list[dict[str, Any]] = []
    for row in rows:
        threshold = THRESHOLDS.get((row["source"], row["metric_name"]))
        if threshold is not None and is_number(row.get("value")) and row["value"] > threshold:
            winners.append({**row, "threshold": threshold})
    return winners


def write_ranking(rows: list[dict[str, Any]], tick_time: datetime, run_id: str) -> None:
    ranked = sorted(
        [row for row in rows if row.get("rank_24h") is not None],
        key=lambda row: (row["rank_24h"], row["artifact_id"]),
    )
    atomic_write_json(
        RANKING,
        {
            "schema_id": "hfo.external_signal.rank_24h.v1",
            "computed_utc": iso_z(tick_time),
            "run_id": run_id,
            "coverage_status": "ok" if ranked else "unknown_no_24h_baseline",
            "ranking": [
                {
                    "rank_24h": row["rank_24h"],
                    "artifact_id": row["artifact_id"],
                    "source": row["source"],
                    "metric_name": row["metric_name"],
                    "delta_24h": row["delta_24h"],
                    "value": row["value"],
                }
                for row in ranked
            ],
        },
    )


def write_first_signal(winners: list[dict[str, Any]], tick_time: datetime, run_id: str) -> Path:
    path = EXPERIMENTS / f"first_signal_{tick_time:%Y%m%d}.md"
    lines = [
        "# First external fitness signal",
        "",
        f"- detected_utc: {iso_z(tick_time)}",
        f"- run_id: `{run_id}`",
        "- action: HALT_FOR_OPERATOR_REVIEW",
        "",
        "| artifact | source | metric | value | threshold |",
        "|---|---|---:|---:|---:|",
    ]
    for row in winners:
        lines.append(
            f"| `{row['artifact_id']}` | {row['source']} | {row['metric_name']} | {row['value']} | > {row['threshold']} |"
        )
    lines += ["", "## Bound fitness rows", "", "```jsonl"]
    lines.extend(json_line(row) for row in winners)
    lines += ["```", ""]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))
        handle.flush()
        os.fsync(handle.fileno())
    return path


def write_report(
    rows: list[dict[str, Any]],
    tick_time: datetime,
    run_id: str,
    tick_index: int,
    input_status: dict[str, Any],
) -> Path:
    path = REPORT_DIR / f"D2_POLL_REPORT_{tick_time:%H}Z.md"
    numeric = [row for row in rows if is_number(row.get("value"))]
    unknown = [row for row in rows if not is_number(row.get("value"))]
    ranked = sorted(
        [row for row in rows if row.get("rank_24h") is not None],
        key=lambda row: (row["rank_24h"], row["artifact_id"]),
    )
    shape = {
        "schema_id": "hfo.external_signal.poll_report.v1",
        "ts_utc": iso_z(tick_time),
        "run_id": run_id,
        "tick_index": tick_index,
        "artifact_rows": len(rows),
        "numeric_rows": len(numeric),
        "unknown_rows": len(unknown),
        "publications_input": input_status["status"],
    }
    lines = [
        "# D2 external-signal poll report",
        "",
        "```json",
        json.dumps(shape, ensure_ascii=False, sort_keys=True),
        "```",
        "",
        "| rank 24h | artifact | source metric | value | delta 24h | status |",
        "|---:|---|---|---:|---:|---|",
    ]
    display = ranked if ranked else sorted(rows, key=lambda row: (row["source"], row["artifact_id"]))
    for row in display:
        lines.append(
            "| {rank} | `{artifact}` | {source}/{metric} | {value} | {delta} | {status} |".format(
                rank=row.get("rank_24h") if row.get("rank_24h") is not None else "—",
                artifact=row["artifact_id"],
                source=row["source"],
                metric=row["metric_name"],
                value=row["value"] if is_number(row.get("value")) else "UNKNOWN",
                delta=row["delta_24h"] if is_number(row.get("delta_24h")) else "UNKNOWN",
                status=row["status"],
            )
        )
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        if path.stat().st_size:
            handle.write("\n---\n\n")
        handle.write("\n".join(lines))
        handle.flush()
        os.fsync(handle.fileno())
    return path


def acquire_lock():
    LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
    handle = LOCK_FILE.open("a+b")
    try:
        if os.name == "nt":
            import msvcrt

            handle.seek(0)
            if handle.tell() == 0 and LOCK_FILE.stat().st_size == 0:
                handle.write(b"0")
                handle.flush()
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        handle.close()
        raise RuntimeError("another external-signal monitor already holds the lock") from None
    return handle


def monitor_status(
    *,
    run_id: str,
    state: str,
    started: datetime,
    tick_index: int,
    report_count: int,
    input_status: dict[str, Any] | None = None,
    workers: list[dict[str, Any]] | None = None,
    stop_reason: str | None = None,
    backoff_until: str | None = None,
) -> dict[str, Any]:
    return {
        "schema_id": "hfo.external_signal.monitor_status.v1",
        "run_id": run_id,
        "pid": os.getpid(),
        "state": state,
        "started_utc": iso_z(started),
        "updated_utc": iso_z(),
        "tick_index": tick_index,
        "report_count": report_count,
        "input_status": input_status,
        "workers": workers,
        "stop_reason": stop_reason,
        "backoff_until_utc": backoff_until,
        "fitness_path": str(FITNESS.relative_to(ROOT)).replace("\\", "/"),
    }


def run_monitor(args: argparse.Namespace) -> int:
    lock_handle = acquire_lock()
    started = utc_now()
    run_id = started.strftime("fitness-%Y%m%dT%H%M%SZ") + f"-{os.getpid()}"
    interval = args.interval_seconds
    if args.once:
        ticks = 1
    elif args.tick_count is not None:
        ticks = args.tick_count
    else:
        ticks = min(DEFAULT_TICKS, max(1, int(math.ceil(args.duration_hours * 3600 / interval))))
    first_tick_index = args.start_tick_index
    last_tick_index = first_tick_index - 1
    report_count = 0
    PID_FILE.write_text(str(os.getpid()) + "\n", encoding="ascii")
    atomic_write_json(
        STATUS,
        monitor_status(run_id=run_id, state="starting", started=started, tick_index=-1, report_count=0),
    )
    try:
        multiprocessing.freeze_support()
        if args.initial_delay_seconds:
            atomic_write_json(
                STATUS,
                monitor_status(
                    run_id=run_id,
                    state="waiting_for_resume_tick",
                    started=started,
                    tick_index=last_tick_index,
                    report_count=report_count,
                    stop_reason=f"initial delay {args.initial_delay_seconds}s preserves the 30-minute cadence",
                ),
            )
            time.sleep(args.initial_delay_seconds)
        with multiprocessing.Manager() as manager, concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
            barrier = manager.Barrier(len(SOURCE_NAMES))
            for tick_offset in range(ticks):
                tick_index = first_tick_index + tick_offset
                last_tick_index = tick_index
                scheduled = time.monotonic()
                tick_time = utc_now()
                by_source, input_status = load_artifacts()
                futures = {
                    source: executor.submit(run_source_worker_synchronized, source, by_source[source], barrier)
                    for source in SOURCE_NAMES
                }
                worker_receipts: list[dict[str, Any]] = []
                observations: list[dict[str, Any]] = []
                for source in SOURCE_NAMES:
                    result = futures[source].result()
                    worker_receipts.append(
                        {
                            "source": source,
                            "worker_pid": result["worker_pid"],
                            "observations": len(result["observations"]),
                            "rate_limited": result["rate_limited"],
                            "retry_after_seconds": result["retry_after_seconds"],
                        }
                    )
                    observations.extend(result["observations"])
                worker_pids = {worker["worker_pid"] for worker in worker_receipts}
                if len(worker_pids) != len(SOURCE_NAMES):
                    raise RuntimeError(
                        f"six-worker invariant failed: observed {len(worker_pids)} distinct worker processes"
                    )

                history = load_history()
                rows = enrich_rows(observations, history, tick_time, run_id, tick_index)
                append_jsonl(FITNESS, rows)
                write_ranking(rows, tick_time, run_id)
                winners = threshold_winners(rows)

                if tick_index % 6 == 0 and report_count < 4:
                    write_report(rows, tick_time, run_id, tick_index, input_status)
                    report_count += 1

                rate_receipts = [worker for worker in worker_receipts if worker["rate_limited"]]
                if winners:
                    signal_path = write_first_signal(winners, tick_time, run_id)
                    atomic_write_json(
                        STATUS,
                        monitor_status(
                            run_id=run_id,
                            state="halted_threshold",
                            started=started,
                            tick_index=tick_index,
                            report_count=report_count,
                            input_status=input_status,
                            workers=worker_receipts,
                            stop_reason=str(signal_path.relative_to(ROOT)).replace("\\", "/"),
                        ),
                    )
                    return 20
                if rate_receipts:
                    retry_seconds = max(
                        [worker["retry_after_seconds"] or DEFAULT_INTERVAL_SECONDS for worker in rate_receipts]
                    )
                    backoff_until = iso_z(utc_now() + timedelta(seconds=retry_seconds))
                    atomic_write_json(
                        STATUS,
                        monitor_status(
                            run_id=run_id,
                            state="halted_rate_limit",
                            started=started,
                            tick_index=tick_index,
                            report_count=report_count,
                            input_status=input_status,
                            workers=worker_receipts,
                            stop_reason="one or more sources reached a rate limit",
                            backoff_until=backoff_until,
                        ),
                    )
                    return 29

                state = "once_complete" if args.once else "sleeping_until_next_tick"
                atomic_write_json(
                    STATUS,
                    monitor_status(
                        run_id=run_id,
                        state=state,
                        started=started,
                        tick_index=tick_index,
                        report_count=report_count,
                        input_status=input_status,
                        workers=worker_receipts,
                    ),
                )
                if args.once:
                    return 0
                if tick_offset + 1 < ticks:
                    elapsed = time.monotonic() - scheduled
                    time.sleep(max(0.0, interval - elapsed))

        atomic_write_json(
            STATUS,
            monitor_status(
                run_id=run_id,
                state="completed_12h",
                started=started,
                tick_index=last_tick_index,
                report_count=report_count,
                stop_reason=f"completed {ticks} tick(s) in this process; final tick index {last_tick_index}",
            ),
        )
        return 0
    except Exception as exc:
        atomic_write_json(
            STATUS,
            monitor_status(
                run_id=run_id,
                state="failed",
                started=started,
                tick_index=last_tick_index,
                report_count=report_count,
                stop_reason=f"{type(exc).__name__}: {str(exc)[:400]}",
            ),
        )
        raise
    finally:
        try:
            PID_FILE.unlink()
        except FileNotFoundError:
            pass
        lock_handle.close()


def topology_test() -> int:
    """Verify six distinct poller processes without network calls or state writes."""
    multiprocessing.freeze_support()
    with multiprocessing.Manager() as manager, concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        barrier = manager.Barrier(len(SOURCE_NAMES))
        futures = [
            executor.submit(run_source_worker_synchronized, source, [], barrier)
            for source in SOURCE_NAMES
        ]
        receipts = [future.result(timeout=30) for future in futures]
    pids = [receipt["worker_pid"] for receipt in receipts]
    result = {
        "sources": list(SOURCE_NAMES),
        "worker_pids": pids,
        "distinct_worker_pids": len(set(pids)),
        "required_worker_pids": len(SOURCE_NAMES),
    }
    print(json.dumps(result, sort_keys=True))
    return 0 if result["distinct_worker_pids"] == result["required_worker_pids"] else 2


def plan() -> int:
    by_source, input_status = load_artifacts()
    print(
        json.dumps(
            {
                "worker_count": len(SOURCE_NAMES),
                "workers": {source: len(by_source[source]) for source in SOURCE_NAMES},
                "artifact_rows_per_tick": sum(len(items) for items in by_source.values()),
                "publications_input": input_status,
                "interval_seconds": DEFAULT_INTERVAL_SECONDS,
                "ticks": DEFAULT_TICKS,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--once", action="store_true", help="Run one real tick and stop")
    parser.add_argument("--plan", action="store_true", help="Print the worker/artifact plan without network calls or writes")
    parser.add_argument("--topology-test", action="store_true", help="Verify six distinct workers without polling")
    parser.add_argument("--interval-seconds", type=int, default=DEFAULT_INTERVAL_SECONDS)
    parser.add_argument("--duration-hours", type=float, default=DEFAULT_DURATION_HOURS)
    parser.add_argument("--tick-count", type=int, default=None, help="Override the number of ticks")
    parser.add_argument("--start-tick-index", type=int, default=0, help="First tick index for a resumed run")
    parser.add_argument("--initial-delay-seconds", type=int, default=0, help="Wait before the first tick")
    args = parser.parse_args(argv)
    if args.interval_seconds <= 0:
        parser.error("--interval-seconds must be positive")
    if args.duration_hours <= 0:
        parser.error("--duration-hours must be positive")
    if args.tick_count is not None and args.tick_count <= 0:
        parser.error("--tick-count must be positive")
    if args.start_tick_index < 0:
        parser.error("--start-tick-index must be non-negative")
    if args.initial_delay_seconds < 0:
        parser.error("--initial-delay-seconds must be non-negative")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.topology_test:
        return topology_test()
    if args.plan:
        return plan()
    return run_monitor(args)


if __name__ == "__main__":
    raise SystemExit(main())
