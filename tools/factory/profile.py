"""
OPERATOR PROFILE — the only claims the factory is allowed to make.

Every entry carries a verification status. The generator may only cite assets
whose status is "verified"; "unverified" entries exist so a human can promote
them deliberately, not so prose can quietly borrow them.

Re-probed 2026-08-02T04:0xZ (clock_source: host_read):
  curl -sSI https://demo01-handpiano.pages.dev/   -> HTTP 200
  gh api users/TTaoGaming                          -> public_repos=4 followers=1
  ls C:/Dev/hfo_dev_2026_3/omega_games/            -> 61 entries
"""
from __future__ import annotations

OPERATOR = {
    "handle": "TTaoGaming",
    "email": "ttaogaming@gmail.com",
    "github": "https://github.com/TTaoGaming",
    "timezone": "US Pacific",
    "availability": "part-time contract, remote, can start within 1 week",
}

# ---------------------------------------------------------------------------
# EVIDENCE ASSETS — citable in outreach only when status == "verified"
# ---------------------------------------------------------------------------
ASSETS = [
    {
        "id": "demo01_handpiano",
        "status": "verified",
        "is_live_demo": True,          # opens in a browser, provable in one click
        "url": "https://demo01-handpiano.pages.dev/",
        "verified_utc": "2026-08-02T04:04Z",
        "verified_by": "curl -sSI -> HTTP 200",
        # --- prose OWNED BY THE ASSET. Templates interpolate these and never
        # --- hardcode a claim, so a claim can no longer mismatch its URL.
        "pitch": "I build browser-based webcam input layers",
        "proof_sentence": ("it opens in a browser with no install and no hardware, and it "
                           "tracks your hands well enough to play a piano with them"),
        "scale_fact": "~316 KB shipped, running on a laptop's built-in camera",
        "one_line": "browser webcam hand-tracking demo: MediaPipe landmarks drive a playable piano, no install, no hardware",
        "technical_seams": [
            "setVideoSource() -- swap the camera for any MediaStream or file",
            "injectRawLandmarks() -- drive it from recorded landmark data",
            "injectNoisyLandmarks() -- deterministic jitter injection for robustness tests",
            "injectCursorDTO() -- headless cursor stream, no camera at all",
        ],
        "why_it_matters": "those seams make the tracking layer testable in CI with no camera and no human, which is the part most webcam demos cannot do",
        # unambiguous only: "accessibility"/"canvas"/"input" produced webcam
        # pitches at data-science and HR listings. See STRONG_CAPABILITIES note.
        "relevant_to": ["computer vision", "computer-vision", "mediapipe",
                        "hand tracking", "hand-tracking", "gesture", "webcam",
                        "pose estimation", "augmented reality", "webxr", "ar/vr",
                        "webgl", "three.js", "spatial computing", "human-computer",
                        "interaction design", "opencv", "real-time video"],
    },
    {
        "id": "omega_games",
        "status": "verified",
        "is_live_demo": False,         # local corpus, no public URL yet -- see GAME_CATALOGUE
        "url": "",
        "verified_utc": "2026-08-02T05:12Z",
        "verified_by": ("audited all 34 index.html files: 34/34 self-contained (no external "
                        "src/href), 34/34 carry a viewport meta, 32/34 canvas-based, "
                        "29/34 handle touch/pointer, median 5,795 B"),
        "pitch": "I ship small self-contained browser games",
        "proof_sentence": ("I have 34 finished HTML5 titles that each run from a single "
                           "self-contained index.html with no external requests"),
        "scale_fact": "median 5.8 KB per title, 4.5-12.5 KB across the catalogue",
        "one_line": "a catalogue of 34 self-contained HTML5 browser games, median 5.8 KB each",
        "technical_seams": [
            "one index.html per title, no build step and no external network calls",
            "canvas rendering with touch and pointer input already wired in 29 of 34",
        ],
        "why_it_matters": ("a 5.8 KB self-contained title loads instantly on a mobile "
                           "connection, which is the constraint web portals actually care about"),
        "relevant_to": ["game development", "game developer", "html5 game",
                        "browser game", "game jam", "web game", "portal", "phaser",
                        "canvas game", "casual game", "webgl"],
    },
    {
        "id": "agent_harness",
        "status": "verified",
        "is_live_demo": False,         # a repo, not a one-click demo
        "url": "https://github.com/TTaoGaming/hfo-gen-133",
        "verified_utc": "2026-08-02T04:19Z",
        "verified_by": "gh api repos/TTaoGaming/hfo-gen-133 -> private=False, pushed 2026-08-02T04:18Z",
        "pitch": "I build the verification layer under LLM agent systems",
        "proof_sentence": ("I run a multi-agent build harness where every irreversible action "
                           "is policy-gated and acceptance tests are held out from the agent "
                           "that generated the work"),
        # NOT "sealed": every chain row in this forge carries hmac: null
        # (HIVE_REVIEW §2, L_UNSIGNED_CONTINUITY_ASSUMED). Calling them sealed
        # would be a false claim a buyer could check.
        "scale_fact": "an append-only JSONL event log with a single writer per lane",
        "one_line": "a multi-agent build harness: append-only JSONL event log, policy-gated irreversible actions, held-out acceptance tests that a passing agent cannot self-grade",
        "technical_seams": [
            "append-only JSONL state, single-writer",
            "OPA/Rego policy gate in front of every irreversible action",
            "held-out test runner separate from the generating agent",
        ],
        "why_it_matters": "the verification layer is the interesting part, not the model calls, because agents cannot mark their own homework",
        "relevant_to": ["llm", "multi-agent", "prompt engineering", "langchain",
                        "evaluation harness", "openai api", "anthropic",
                        "ai engineer", "ml engineer", "mlops", "agentic"],
    },
]

# ---------------------------------------------------------------------------
# CAPABILITY LATTICE — drives deterministic fit scoring.
# weight = how strongly a listing hit on this term predicts a real fit.
# ---------------------------------------------------------------------------
# STRONG = unambiguous in context. If one of these appears in a title or a
# requirement line, the buyer is genuinely asking for this work. These are the
# only terms allowed to establish that a listing is a real target.
#
# Word-boundary matching (fit._matcher) fixed SPELLING collisions ("rag" inside
# "coverage"). It does NOT fix SENSE collisions: "accessibility" matched
# "accessibility of core data" on a Data Scientist role and produced a
# hand-tracking pitch that graded LOW risk. Ambiguity is a property of the term,
# so it is recorded on the term.
STRONG_CAPABILITIES: dict[str, float] = {
    "computer vision": 3.0, "mediapipe": 3.5, "hand tracking": 3.5,
    "hand-tracking": 3.5, "gesture": 3.0, "pose estimation": 3.0,
    "webcam": 2.5, "opencv": 2.5, "real-time video": 2.5,
    "augmented reality": 2.5, "spatial computing": 2.5, "webxr": 2.5,
    "ar/vr": 2.0, "three.js": 2.0, "webgl": 2.0,
    "multi-agent": 2.5, "prompt engineering": 1.8, "evaluation harness": 2.5,
    "langchain": 1.8, "llm": 2.0, "openai api": 1.5, "anthropic": 2.0,
    "human-computer": 2.0, "interaction design": 1.5,
    "computer-vision": 3.0, "ml engineer": 1.8, "applied scientist": 1.5,
}

# WEAK = real signal, but each appears in unrelated contexts often enough that
# it cannot on its own justify contacting anyone. Contributes to fit ranking;
# never sufficient for `capability_evidence`.
WEAK_CAPABILITIES: dict[str, float] = {
    "landmark": 0.8, "unity": 0.8, "agent": 0.8, "rag": 0.8, "eval": 0.5,
    "typescript": 1.0, "javascript": 0.9, "react": 0.9, "canvas": 0.8,
    "html5": 0.9, "cloudflare": 1.0, "wasm": 1.0,
    "python": 1.0, "fastapi": 0.8, "ci/cd": 0.8, "github actions": 0.8,
    "docker": 0.5, "automation": 0.6,
    "accessibility": 0.8, "hci": 1.2, "prototyping": 0.8, "rapid prototype": 1.2,
}

CAPABILITIES: dict[str, float] = {**STRONG_CAPABILITIES, **WEAK_CAPABILITIES}

# Terms that mean "this listing is not reachable by a solo remote contractor".
DISQUALIFIERS: dict[str, float] = {
    "security clearance": -6.0, "ts/sci": -6.0, "on-site required": -3.0,
    "must be located in": -1.5, "phd required": -2.5, "no remote": -4.0,
    "relocation required": -3.0, "citizens only": -2.0, "w2 only": -1.0,
    "10+ years": -1.0, "unpaid": -5.0, "equity only": -5.0,
    "manager of managers": -2.5, "vp of": -2.0, "director of engineering": -1.5,
}

# ---------------------------------------------------------------------------
# THE OFFER — the thing an outreach artifact actually asks for.
# Prices come from SIGRUN_CANON §2 (published $2k-20k/project band).
# ---------------------------------------------------------------------------
OFFER = {
    "name": "camera-control layer",
    "scope": "a working webcam/gesture input layer wired into your existing product surface",
    "duration": "2 weeks",
    "price_band": "$4,000-8,000 fixed",
    "hourly_band": "$95-125/hr",
    "deliverable": "a running build on your stack plus the injection seams so your CI can test the tracking without a camera",
    "guarantee": "if it does not run in your environment at the end of week 1, you pay nothing",
}

DISCLOSURE = (
    "Written with an AI assistant; every claim above points at a URL you can open."
)

# ---------------------------------------------------------------------------
# GAME CATALOGUE — measured 2026-08-02T05:12Z from
#   C:\Dev\hfo_dev_2026_3\omega_games\*\index.html
# Full audit: state/factory_input/omega_games_audit.json
# ---------------------------------------------------------------------------
GAME_CATALOGUE = {
    "total_titles": 34,
    "self_contained": 34,
    "touch_ready": 29,
    "canvas": 32,
    "median_bytes": 5795,
    "min_bytes": 4539,
    "max_bytes": 12497,

    # ⛔ The single blocking defect for every portal: an X-Frame-Options
    # SAMEORIGIN meta tag prevents the iframe embed that every web-game portal
    # requires. Present in 28 of 34. The fix is deleting one line per title.
    "xframe_blocked": 28,
    "xframe_fix": ('remove `<meta http-equiv="X-Frame-Options" content="SAMEORIGIN">` '
                   'from index.html -- one line per title'),

    # ⛔ Do NOT submit these to a commercial portal. PAC-MAN and TETRIS are
    # actively enforced trademarks; the rest are named after protected or
    # trademark-contested properties. Submitting them would expose the operator
    # to a takedown at best.
    "ip_encumbered": ["minesweeper", "neon_pong", "pacman", "pong", "simon_says",
                      "sokoban", "space_invaders", "tetris", "whack_a_mole"],

    # clean name + touch input + self-contained
    "portal_candidates": [
        "hex_flip", "ice_slide", "infinite_runner", "light_trail", "magnetic_orbs",
        "match3", "maze_runner", "memory_match", "number_crush", "paint_blast",
        "pipe_puzzle", "platformer_hop", "reaction_test", "rhythm_tap",
        "slide_puzzle", "slingshot", "snake", "snake_neon", "target_aim",
        "tic_tac_toe", "tower_drop",
    ],
    "source_dir": r"C:\Dev\hfo_dev_2026_3\omega_games",
}

#: What counts as the acceptance event, per market. Used by the grader so the
#: operator sees what would actually falsify each artifact -- a job application
#: and a portal submission cannot share one test.
ACCEPTANCE_EVENT = {
    "M1": "a named human replies naming a price or a date",
    "M2": "a named human replies naming a date (screen/interview) or a rate",
    "M5": "the portal or jam host replies with terms, a review date, or a slot",
    "M6": "a proposal is submitted before the published close date, and the agency acknowledges receipt",
}


def verified_assets() -> list[dict]:
    return [a for a in ASSETS if a["status"] == "verified"]


def assets_for(text: str) -> list[dict]:
    """Verified assets relevant to this listing, best first.

    Returns [] when NOTHING is relevant. The earlier version fell back to
    `verified_assets()[0]`, which is how a browser hand-tracking pitch reached a
    car-detailing lot-attendant posting: the fallback manufactured a relevance
    that did not exist. If we have nothing to say to a listing, the correct
    output is no artifact, not a confident irrelevant one.
    """
    from .fit import _matcher                       # word-boundary matching
    low = (text or "").lower()
    scored = []
    for a in verified_assets():
        hits = [t for t in a["relevant_to"] if _matcher(t).search(low)]
        if hits:
            scored.append((len(hits), a))
    scored.sort(key=lambda x: -x[0])
    return [a for _n, a in scored]
