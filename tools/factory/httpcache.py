"""Stdlib HTTP with on-disk cache. No third-party deps, no auth, GET only."""
from __future__ import annotations

import gzip
import hashlib
import json
import os
import time
import urllib.error
import urllib.request

CACHE_DIR = os.path.join(os.path.dirname(__file__), "_cache")
UA = "hfo-gen133-factory/0.1 (+https://github.com/TTaoGaming; contact ttaogaming@gmail.com)"
DEFAULT_TTL = 3600  # 1h -- matches the hourly cron cadence


class FetchError(Exception):
    pass


def _key(url: str) -> str:
    return os.path.join(CACHE_DIR, hashlib.sha256(url.encode()).hexdigest()[:24] + ".bin")


def fetch(url: str, *, ttl: int = DEFAULT_TTL, timeout: int = 30,
          accept: str = "application/json, text/xml;q=0.9, */*;q=0.8") -> str:
    """GET with cache. Raises FetchError on non-200 so adapters fail loudly."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = _key(url)
    if ttl > 0 and os.path.exists(path) and (time.time() - os.path.getmtime(path)) < ttl:
        with open(path, "rb") as fh:
            return fh.read().decode("utf-8", "replace")

    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": accept,
        "Accept-Encoding": "gzip",
    })
    last: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                if resp.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                if resp.status != 200:
                    raise FetchError(f"http={resp.status} url={url}")
                with open(path, "wb") as fh:
                    fh.write(raw)
                return raw.decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            # 4xx will not fix itself; do not burn retries on it
            raise FetchError(f"http={exc.code} url={url}") from exc
        except Exception as exc:                    # noqa: BLE001 -- network flake
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise FetchError(f"failed after 3 attempts url={url}: {last}")


def fetch_json(url: str, **kw):
    return json.loads(fetch(url, **kw))


def probe(url: str, timeout: int = 15) -> int:
    """Return HTTP status for a URL without caching. Used to verify a listing is live."""
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0
