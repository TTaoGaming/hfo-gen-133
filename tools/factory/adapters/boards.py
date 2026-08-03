"""
Public job-board adapters (market M2 employment, with M1 contract rows mixed in).

All five endpoints were probed 2026-08-02T04:0xZ and returned HTTP 200 with no
auth. Attribution required by ToS is carried in `legal_note` and reproduced in
every emitted sample.
"""
from __future__ import annotations

import datetime as _dt
import re
from typing import Iterator

from .. import httpcache
from ..core import Opportunity, clean_entity, clean_title, make_uid, strip_html
from .base import OpportunityAdapter, looks_relevant


def _iso(epoch_or_str) -> str:
    if isinstance(epoch_or_str, (int, float)):
        return _dt.datetime.fromtimestamp(epoch_or_str, _dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return str(epoch_or_str or "")


def _comp(lo, hi, cur="USD", per="year") -> str:
    try:
        lo, hi = int(lo or 0), int(hi or 0)
    except (TypeError, ValueError):
        return ""
    if not lo and not hi:
        return ""
    if lo and hi:
        return f"{cur} {lo:,}-{hi:,} / {per}"
    return f"{cur} {(lo or hi):,} / {per}"


class RemoteOKAdapter(OpportunityAdapter):
    name = "remoteok"
    market = "M2"
    surface = "RemoteOK public JSON API"
    legal_note = ("Source: Remote OK (https://remoteok.com) -- their API ToS requires "
                  "a followed backlink and source attribution on any use.")
    ENDPOINT = "https://remoteok.com/api"

    def search(self) -> Iterator[Opportunity]:
        rows = httpcache.fetch_json(self.ENDPOINT, ttl=self.ttl)
        n = 0
        for r in rows:
            if not isinstance(r, dict) or "position" not in r:
                continue                                   # row 0 is the legal notice
            body = strip_html(r.get("description", ""))
            blob = f"{r.get('position','')} {' '.join(r.get('tags') or [])} {body}"
            if not looks_relevant(blob):
                continue
            url = r.get("url") or r.get("apply_url") or ""
            if not url:
                continue
            yield Opportunity(
                uid=make_uid(self.name, url, r.get("position", "")),
                adapter=self.name, market=self.market,
                title=clean_title(r.get("position", "")),
                entity=clean_entity(r.get("company") or ""),
                url=url,
                posted_utc=_iso(r.get("epoch") or r.get("date")),
                location=r.get("location") or "Remote",
                compensation=_comp(r.get("salary_min"), r.get("salary_max")),
                tags=[t for t in (r.get("tags") or []) if t][:12],
                body=body,
                source_payload={"slug": r.get("slug"), "id": r.get("id")},
            )
            n += 1
            if n >= self.limit:
                return


class ArbeitnowAdapter(OpportunityAdapter):
    name = "arbeitnow"
    market = "M2"
    surface = "Arbeitnow open job-board API"
    legal_note = "Source: Arbeitnow (https://www.arbeitnow.com) free job-board API."
    ENDPOINT = "https://www.arbeitnow.com/api/job-board-api"

    def search(self) -> Iterator[Opportunity]:
        data = httpcache.fetch_json(self.ENDPOINT, ttl=self.ttl)
        n = 0
        for r in data.get("data", []):
            body = strip_html(r.get("description", ""))
            blob = f"{r.get('title','')} {' '.join(r.get('tags') or [])} {body}"
            if not looks_relevant(blob):
                continue
            url = r.get("url") or ""
            if not url:
                continue
            yield Opportunity(
                uid=make_uid(self.name, url, r.get("title", "")),
                adapter=self.name, market=self.market,
                title=clean_title(r.get("title") or ""),
                entity=clean_entity(r.get("company_name") or ""),
                url=url,
                posted_utc=_iso(r.get("created_at")),
                location=r.get("location") or ("Remote" if r.get("remote") else ""),
                compensation="",
                tags=[t for t in (r.get("tags") or []) if t][:12]
                     + [t for t in (r.get("job_types") or []) if t][:4],
                body=body,
                source_payload={"slug": r.get("slug"), "remote": r.get("remote")},
            )
            n += 1
            if n >= self.limit:
                return


class HimalayasAdapter(OpportunityAdapter):
    name = "himalayas"
    market = "M2"
    surface = "Himalayas remote-jobs API"
    legal_note = "Source: Himalayas (https://himalayas.app) public jobs API."
    ENDPOINT = "https://himalayas.app/jobs/api?limit=100&offset={off}"

    def search(self) -> Iterator[Opportunity]:
        n = 0
        for off in (0, 100):
            try:
                data = httpcache.fetch_json(self.ENDPOINT.format(off=off), ttl=self.ttl)
            except httpcache.FetchError:
                break
            for r in data.get("jobs", []):
                body = strip_html(r.get("description") or r.get("excerpt") or "")
                blob = f"{r.get('title','')} {' '.join(r.get('categories') or [])} {body}"
                if not looks_relevant(blob):
                    continue
                url = r.get("applicationLink") or r.get("guid") or ""
                if not url.startswith("http"):
                    continue
                yield Opportunity(
                    uid=make_uid(self.name, url, r.get("title", "")),
                    adapter=self.name, market=self.market,
                    title=clean_title(r.get("title") or ""),
                    entity=clean_entity(r.get("companyName") or ""),
                    url=url,
                    posted_utc=_iso(r.get("pubDate")),
                    location=", ".join(r.get("locationRestrictions") or []) or "Remote",
                    compensation=_comp(r.get("minSalary"), r.get("maxSalary"),
                                       r.get("currency") or "USD",
                                       r.get("salaryPeriod") or "year"),
                    tags=[t for t in (r.get("categories") or []) if t][:12],
                    body=body,
                    source_payload={"seniority": r.get("seniority"),
                                    "employmentType": r.get("employmentType")},
                )
                n += 1
                if n >= self.limit:
                    return
            if len(data.get("jobs", [])) < 100:
                break


class JobicyAdapter(OpportunityAdapter):
    name = "jobicy"
    market = "M2"
    surface = "Jobicy remote-jobs API v2"
    legal_note = "Source: Jobicy (https://jobicy.com) public API v2."
    ENDPOINT = "https://jobicy.com/api/v2/remote-jobs?count=50&industry={ind}"
    INDUSTRIES = ("engineering", "design-multimedia", "data-science")

    def search(self) -> Iterator[Opportunity]:
        n = 0
        for ind in self.INDUSTRIES:
            try:
                data = httpcache.fetch_json(self.ENDPOINT.format(ind=ind), ttl=self.ttl)
            except httpcache.FetchError:
                continue
            for r in data.get("jobs", []):
                body = strip_html(r.get("jobDescription") or r.get("jobExcerpt") or "")
                blob = f"{r.get('jobTitle','')} {' '.join(r.get('jobIndustry') or [])} {body}"
                if not looks_relevant(blob):
                    continue
                url = r.get("url") or ""
                if not url.startswith("http"):
                    continue
                yield Opportunity(
                    uid=make_uid(self.name, url, r.get("jobTitle", "")),
                    adapter=self.name, market=self.market,
                    title=clean_title(r.get("jobTitle") or ""),
                    entity=clean_entity(r.get("companyName") or ""),
                    url=url,
                    posted_utc=_iso(r.get("pubDate")),
                    location=r.get("jobGeo") or "Remote",
                    compensation=_comp(r.get("salaryMin"), r.get("salaryMax"),
                                       r.get("salaryCurrency") or "USD",
                                       r.get("salaryPeriod") or "year"),
                    tags=[t for t in (r.get("jobIndustry") or []) if t]
                         + [t for t in (r.get("jobType") or []) if t],
                    body=body,
                    source_payload={"jobLevel": r.get("jobLevel")},
                )
                n += 1
                if n >= self.limit:
                    return


_ITEM = re.compile(r"<item>(.*?)</item>", re.S)


def _tag(block: str, tag: str) -> str:
    m = re.search(rf"<{tag}>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</{tag}>", block, re.S)
    return (m.group(1) if m else "").strip()


class WeWorkRemotelyAdapter(OpportunityAdapter):
    name = "weworkremotely"
    market = "M2"
    surface = "We Work Remotely category RSS"
    legal_note = "Source: We Work Remotely (https://weworkremotely.com) public RSS."
    FEEDS = (
        "https://weworkremotely.com/categories/remote-programming-jobs.rss",
        "https://weworkremotely.com/categories/remote-design-jobs.rss",
    )

    def search(self) -> Iterator[Opportunity]:
        n = 0
        for feed in self.FEEDS:
            try:
                raw = httpcache.fetch(feed, ttl=self.ttl, accept="application/rss+xml, text/xml")
            except httpcache.FetchError:
                continue
            for block in _ITEM.findall(raw):
                title_raw = strip_html(_tag(block, "title"))
                body = strip_html(_tag(block, "description"))
                if not looks_relevant(f"{title_raw} {body}"):
                    continue
                url = _tag(block, "link")
                if not url.startswith("http"):
                    continue
                # WWR titles are "Company: Role"
                entity, _, role = title_raw.partition(":")
                if not role:
                    entity, role = "", title_raw
                yield Opportunity(
                    uid=make_uid(self.name, url, title_raw),
                    adapter=self.name, market=self.market,
                    title=clean_title(role) or clean_title(title_raw),
                    entity=clean_entity(entity),
                    url=url,
                    posted_utc=_tag(block, "pubDate"),
                    location=strip_html(_tag(block, "region")) or "Remote",
                    compensation="",
                    tags=[t for t in [strip_html(_tag(block, "category"))] if t],
                    body=body,
                    source_payload={},
                )
                n += 1
                if n >= self.limit:
                    return
