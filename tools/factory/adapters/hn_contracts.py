"""
M1 CONTRACTS adapter — Hacker News monthly hiring / freelancer threads.

Why this and not Upwork: the Upwork public RSS feed documented in the brief
(`https://www.upwork.com/ab/feed/jobs/rss?q=`) returns **HTTP 410 GONE** as of
2026-08-02T04:00Z. It was retired. HN's monthly threads are the nearest
still-public source of contract demand with named buyers and, frequently, a
published contact address -- which is the single attribute that most raises the
probability of a price-or-date reply.

Endpoint: hn.algolia.com public API, no auth, probed 200.
"""
from __future__ import annotations

import re
from typing import Iterator

from .. import httpcache
from ..core import (Opportunity, clean_entity, clean_title, find_contact,
                    make_uid, strip_html)
from .base import OpportunityAdapter, looks_relevant

SEARCH = ("https://hn.algolia.com/api/v1/search_by_date"
          "?tags=story,author_whoishiring&hitsPerPage=12")
ITEM = "https://hn.algolia.com/api/v1/items/{id}"

# Buyer-side markers. We deliberately skip SEEKING WORK (those are competitors).
_BUYER = re.compile(r"(?i)^\s*seeking\s+freelancer\b|^\s*hiring\b")
_LOC_SPLIT = re.compile(r"\s*[|｜]\s*|\s+-\s+|\s+–\s+")


class HNContractsAdapter(OpportunityAdapter):
    """Emits one Opportunity per buyer-side comment in the newest HN threads."""
    name = "hn_contracts"
    market = "M1"
    surface = "Hacker News monthly 'Who is hiring' / 'Seeking freelancer' threads"
    legal_note = "Source: Hacker News via the public hn.algolia.com API."

    #: which thread families to mine
    THREAD_PAT = re.compile(r"(?i)(freelancer|who is hiring|who wants to be hired)")
    SKIP_PAT = re.compile(r"(?i)who wants to be hired")   # candidate-side thread

    def search(self) -> Iterator[Opportunity]:
        data = httpcache.fetch_json(SEARCH, ttl=self.ttl)
        threads = [
            h for h in data.get("hits", [])
            if self.THREAD_PAT.search(h.get("title") or "")
            and not self.SKIP_PAT.search(h.get("title") or "")
        ][:3]

        n = 0
        for th in threads:
            tid = th.get("objectID")
            try:
                item = httpcache.fetch_json(ITEM.format(id=tid), ttl=self.ttl, timeout=45)
            except httpcache.FetchError:
                continue
            thread_title = th.get("title") or ""
            for child in item.get("children") or []:
                op = self._from_comment(child, thread_title)
                if op is None:
                    continue
                yield op
                n += 1
                if n >= self.limit:
                    return

    # ------------------------------------------------------------------
    def _from_comment(self, child: dict, thread_title: str) -> Opportunity | None:
        text = strip_html(child.get("text") or "")
        if len(text) < 160:
            return None
        first = text.split("\n", 1)[0][:200]
        is_freelance_thread = "freelancer" in thread_title.lower()
        if is_freelance_thread and not _BUYER.search(first):
            return None                      # SEEKING WORK -> a competitor, not a buyer
        if not looks_relevant(text):
            return None

        cid = child.get("id") or child.get("objectID")
        url = f"https://news.ycombinator.com/item?id={cid}"

        entity = self._entity(first, child.get("author") or "")
        title = self._title(first, thread_title)

        return Opportunity(
            uid=make_uid(self.name, url, str(cid)),
            adapter=self.name, market=self.market,
            title=clean_title(title), entity=clean_entity(entity), url=url,
            posted_utc=(child.get("created_at") or "")[:19] + "Z"
                       if child.get("created_at") else "",
            location=self._location(first),
            compensation="",
            tags=["hn", "contract" if is_freelance_thread else "role"],
            body=text,
            contact=find_contact(text),
            source_payload={"hn_author": child.get("author"),
                            "thread": thread_title, "comment_id": cid},
        )

    @staticmethod
    def _entity(first: str, author: str) -> str:
        parts = [p.strip() for p in _LOC_SPLIT.split(first) if p.strip()]
        for p in parts:
            low = p.lower()
            if low.startswith(("seeking freelancer", "hiring", "remote", "onsite")):
                continue
            if 2 <= len(p) <= 60:
                return p
        return f"HN user @{author}" if author else ""

    @staticmethod
    def _title(first: str, thread_title: str) -> str:
        parts = [p.strip() for p in _LOC_SPLIT.split(first) if p.strip()]
        for p in parts[1:]:
            if re.search(r"(?i)(engineer|developer|dev\b|scientist|designer|"
                         r"architect|consultant|contractor|lead|research)", p):
                return p[:120]
        return (parts[1][:120] if len(parts) > 1 else thread_title[:120])

    @staticmethod
    def _location(first: str) -> str:
        m = re.search(r"(?i)\b(remote(?:\s+\(\w+\))?|onsite|hybrid|worldwide|"
                      r"us[- ]only|eu[- ]only)\b", first)
        return m.group(0) if m else ""
