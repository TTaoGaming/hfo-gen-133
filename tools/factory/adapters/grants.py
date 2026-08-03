"""
GRANTS adapter — grants.gov `search2`.

The brief asked for an SBIR RSS adapter. Probed 2026-08-02T04:00Z and again at
05:0xZ, every SBIR surface is down from their side:

    GET https://api.www.sbir.gov/public/api/solicitations?open=1
      -> 429 {"Code":"TooManyRequestsError",
              "Message":"The SBIR Public API is not available at this time."}
    GET https://www.sbir.gov/rss/solicitations.xml  -> 404
    GET https://www.sbir.gov/solicitations/rss      -> 404

That is a server-side outage, not a local rate limit: the FIRST call of the
session already returned 429.

grants.gov is the working substitute and is strictly larger -- SBIR/STTR topics
are a subset of federal funding opportunities, and grants.gov carries NSF and DOD
directly. My earlier 403 on it was my own error: `search2` is **POST-only** and I
had probed it with GET. With POST it returns 200 and needs no key:

    POST https://api.grants.gov/v1/api/search2
    {"rows":10,"keyword":"computer vision","oppStatuses":"forecasted|posted"}
      -> 200, 17,606 B, hitCount=478

⚠️ Canon ranks grants LAST on speed: P(income in 90d) = 0.25, **6-12 months to
cash**. This adapter exists because the operator asked for the market to be
tier-1, not because it is the fastest dollar. Nothing here is sent or submitted.
"""
from __future__ import annotations

import json
import urllib.request
from typing import Iterator

from .. import httpcache
from ..core import Opportunity, clean_entity, clean_title, make_uid
from .base import OpportunityAdapter

ENDPOINT = "https://api.grants.gov/v1/api/search2"
DETAIL = "https://grants.gov/search-results-detail/{id}"

QUERIES = [
    "computer vision",
    "human computer interaction",
    "augmented reality",
    "artificial intelligence software",
    "accessibility technology",
]


def _post(payload: dict, timeout: int = 30) -> dict:
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={"Content-Type": "application/json", "User-Agent": httpcache.UA,
                 "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


class GrantsGovAdapter(OpportunityAdapter):
    name = "grants_gov"
    market = "M6"
    surface = "grants.gov search2 API (POST, no auth)"
    legal_note = "Source: grants.gov public search2 API (U.S. federal grant opportunities)."

    def search(self) -> Iterator[Opportunity]:
        seen: set[str] = set()
        n = 0
        for q in QUERIES:
            try:
                data = _post({"rows": 25, "keyword": q,
                              "oppStatuses": "forecasted|posted"})
            except Exception:                      # one bad query must not kill the run
                continue
            if data.get("errorcode"):
                continue
            for h in (data.get("data") or {}).get("oppHits") or []:
                oid = str(h.get("id") or "")
                if not oid or oid in seen:
                    continue
                seen.add(oid)
                close = (h.get("closeDate") or "").strip()
                agency = h.get("agency") or h.get("agencyCode") or ""
                title = h.get("title") or ""
                body = (
                    f"Federal funding opportunity {h.get('number')} from {agency}.\n"
                    f"Title: {title}\n"
                    f"Opportunity status: {h.get('oppStatus')}. "
                    f"Open: {h.get('openDate') or 'not stated'}. "
                    f"Close: {close or 'not stated'}.\n"
                    f"Matched the search term '{q}', so the solicitation text references "
                    f"{q}.\nCFDA: {', '.join(h.get('cfdaList') or []) or 'not listed'}.\n"
                    f"This is a competitive federal solicitation: a proposal must address "
                    f"the published requirements and be submitted through grants.gov before "
                    f"the close date.\n"
                )
                yield Opportunity(
                    uid=make_uid(self.name, DETAIL.format(id=oid), oid),
                    adapter=self.name, market=self.market,
                    title=clean_title(title),
                    entity=clean_entity(agency) or "U.S. federal agency",
                    url=DETAIL.format(id=oid),
                    posted_utc=_us_to_iso(h.get("openDate")),
                    location="United States",
                    compensation="federal grant (amount stated in the solicitation)",
                    tags=["grant", "federal", q],
                    body=body,
                    source_payload={"number": h.get("number"), "agency": agency,
                                    "closeDate": close, "oppStatus": h.get("oppStatus"),
                                    "matched_query": q},
                )
                n += 1
                if n >= self.limit:
                    return


def _us_to_iso(d: str | None) -> str:
    """grants.gov ships MM/DD/YYYY."""
    if not d or "/" not in d:
        return ""
    try:
        mm, dd, yyyy = d.split("/")
        return f"{yyyy}-{int(mm):02d}-{int(dd):02d}T00:00:00Z"
    except ValueError:
        return ""
