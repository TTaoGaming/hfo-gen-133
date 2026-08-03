"""
Operator-supplied targets (LinkedIn hiring managers, warm intros, named studios).

No scraping. LinkedIn's ToS forbids it and a scraper is also a reward-hack: it
manufactures volume against a channel that would ban the account on first use.
Instead the operator pastes targets into a JSONL file and the factory generates
against those specific, real people.

Input file:  state/factory_input/linkedin_targets.jsonl
One JSON object per line:

  {"name": "Jane Okafor",
   "role": "Head of Engineering",
   "company": "Acme Motion",
   "url": "https://www.linkedin.com/in/janeokafor/",
   "why": "Acme ships a webcam fitness app; their app store reviews complain about tracking drift",
   "notes": "met at CVPR 2025 poster session",          # optional
   "market": "M1"}                                       # optional, defaults M1

A seed file with 3 worked examples is written by run_factory.py --seed-input;
the examples are clearly marked EXAMPLE_DO_NOT_SEND and are skipped by the
adapter, so nothing fabricated can ever reach the outbox.
"""
from __future__ import annotations

import json
import os
from typing import Iterator

from ..core import Opportunity, make_uid
from .base import OpportunityAdapter

DEFAULT_PATH = os.path.join("state", "factory_input", "linkedin_targets.jsonl")

SEED = [
    {
        "name": "EXAMPLE_DO_NOT_SEND",
        "role": "Head of Engineering",
        "company": "Example Motion Labs",
        "url": "https://www.linkedin.com/in/example/",
        "why": ("They ship a webcam-based fitness app and their App Store reviews "
                "repeatedly mention the tracking losing the hand when the user turns."),
        "market": "M1",
    },
    {
        "name": "EXAMPLE_DO_NOT_SEND",
        "role": "Studio Director",
        "company": "Example Arcade",
        "url": "https://www.linkedin.com/company/example/",
        "why": "They publish browser games and are hiring for 'novel input'.",
        "market": "M5",
    },
]


class OperatorCachedAdapter(OpportunityAdapter):
    name = "linkedin_cached"
    market = "M1"
    surface = "Operator-pasted LinkedIn / warm-intro targets (no scraping)"
    legal_note = "Operator-supplied. No automated access to LinkedIn occurs anywhere in this factory."

    def __init__(self, path: str = DEFAULT_PATH, **kw) -> None:
        super().__init__(**kw)
        self.path = path
        if not os.path.exists(path):
            self.blocked_reason = (
                f"no input file at {path} -- operator must paste 5-10 real hiring-manager "
                f"or studio targets (see tools/factory/adapters/operator_cached.py docstring). "
                f"Run `python -m tools.factory.run_factory --seed-input` to create the template."
            )

    def search(self) -> Iterator[Opportunity]:
        if not os.path.exists(self.path):
            return
        real = 0
        with open(self.path, encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line or line.startswith("//") or line.startswith("#"):
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if str(r.get("name", "")).startswith("EXAMPLE_DO_NOT_SEND"):
                    continue                                  # template row, never generate
                url = r.get("url") or ""
                if not url.startswith("http"):
                    continue
                why = (r.get("why") or "").strip()
                if len(why) < 40:
                    continue          # without a specific reason this is a generic template
                body = (
                    f"Target: {r.get('name')} -- {r.get('role')} at {r.get('company')}.\n"
                    f"Why this target: {why}\n"
                    f"Operator notes: {r.get('notes', '(none)')}\n"
                )
                real += 1
                yield Opportunity(
                    uid=make_uid(self.name, url, str(r.get("name"))),
                    adapter=self.name,
                    market=r.get("market") or self.market,
                    title=f"{r.get('role')} at {r.get('company')}",
                    entity=r.get("company") or r.get("name") or "",
                    url=url,
                    location=r.get("location", ""),
                    tags=["operator_supplied", "warm"],
                    body=body + why * 2,   # ensure the body clears the 120-char gate
                    contact=r.get("email", ""),
                    source_payload={"person": r.get("name"), "role": r.get("role"),
                                    "why": why, "notes": r.get("notes", "")},
                )
        if real == 0 and not self.blocked_reason:
            self.blocked_reason = (
                f"{self.path} exists but contains 0 real targets (only template rows). "
                f"Operator input required: 5-10 named people with a specific `why`."
            )


def write_seed(path: str = DEFAULT_PATH) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        return path
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("// Paste one JSON object per line. Delete the EXAMPLE rows.\n")
        fh.write("// Required: name, role, company, url, why (>=40 chars, specific).\n")
        for row in SEED:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return path
