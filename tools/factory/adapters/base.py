"""Adapter contract. Every platform surface implements exactly this."""
from __future__ import annotations

from typing import Iterator

from ..core import Opportunity


class OpportunityAdapter:
    name: str = "base"
    market: str = "M0"
    surface: str = ""            # human label for the PDCA table
    blocked_reason: str = ""     # non-empty => needs operator credential/OAuth
    legal_note: str = ""         # attribution required by the source's ToS

    def __init__(self, queries: list[str] | None = None, limit: int = 60,
                 ttl: int = 3600) -> None:
        self.queries = queries or DEFAULT_QUERIES
        self.limit = limit
        self.ttl = ttl

    def search(self) -> Iterator[Opportunity]:      # pragma: no cover - interface
        raise NotImplementedError


DEFAULT_QUERIES = [
    "computer vision",
    "machine learning engineer",
    "ai engineer",
    "frontend engineer",
    "python",
]

# Terms used to pre-filter large public boards down to plausibly-relevant rows
# before the (more expensive) fit scorer runs.
RELEVANCE_TERMS = (
    "computer vision", "mediapipe", "hand tracking", "gesture", "pose",
    "opencv", "webcam", "camera", "augmented reality", "ar/vr", "webxr",
    "three.js", "webgl", "spatial", "unity", "llm", "agent", "ai engineer",
    "machine learning", "prompt", "rag", "typescript", "javascript", "react",
    "python", "canvas", "frontend", "full stack", "accessibility", "prototype",
    "real-time", "video", "ml engineer", "research engineer",
)


def looks_relevant(text: str) -> bool:
    low = text.lower()
    return any(t in low for t in RELEVANCE_TERMS)
