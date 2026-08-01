#!/usr/bin/env python3
"""
kill_switch.py -- single-command halt for a campaign class-authorization.

The safety property this file exists to provide: an operator (or an
automated monitor) can halt an entire campaign class in under 60 seconds
from a terminal, with no network dependency, by flipping one JSON file's
"state" field to "HALTED". render_message.py consults this file before
rendering any message and refuses (exit 7) whenever state != "ARMED" for
the requested campaign_id.

Usage:
    python kill_switch.py [--path PATH] halt <campaign_id> --reason "..." --by "..."
    python kill_switch.py [--path PATH] arm <campaign_id> [--by "..."]
    python kill_switch.py [--path PATH] status <campaign_id>

--path overrides the default KILL_SWITCH.json location (the file next to
this script). status exits 0 if ARMED, 1 if HALTED or any ambiguity
(missing file, campaign_id mismatch) -- fail closed, never fail open.
"""
import argparse
import json
import pathlib
import sys
from datetime import datetime, timezone

DEFAULT_PATH = pathlib.Path(__file__).resolve().with_name("KILL_SWITCH.json")


def _now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve_path(path):
    return pathlib.Path(path) if path else DEFAULT_PATH


def load_state(path=None):
    p = _resolve_path(path)
    if not p.exists():
        raise FileNotFoundError(f"kill switch file not found: {p}")
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(state, path=None):
    p = _resolve_path(path)
    p.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def is_armed(path, campaign_id):
    """True only if the file exists, campaign_id matches, and state == ARMED.

    Any ambiguity (missing file, campaign_id mismatch, unrecognized state)
    is treated as NOT armed. Fail closed, never fail open -- a caller that
    cannot positively confirm ARMED must refuse to send.
    """
    try:
        state = load_state(path)
    except Exception:
        return False
    if state.get("campaign_id") != campaign_id:
        return False
    return state.get("state") == "ARMED"


def _seed_if_missing(path, campaign_id):
    try:
        return load_state(path)
    except FileNotFoundError:
        return {
            "campaign_id": campaign_id,
            "state": "ARMED",
            "reason": None,
            "set_by": None,
            "ts_utc": None,
        }


def cmd_halt(args):
    path = args.path
    state = _seed_if_missing(path, args.campaign_id)
    if state.get("campaign_id") != args.campaign_id:
        print(
            f"ERROR: kill switch file campaign_id={state.get('campaign_id')!r} "
            f"does not match requested {args.campaign_id!r}",
            file=sys.stderr,
        )
        return 1
    state["state"] = "HALTED"
    state["reason"] = args.reason
    state["set_by"] = args.by
    state["ts_utc"] = _now_utc()
    save_state(state, path)
    print(f"HALTED campaign {args.campaign_id} at {state['ts_utc']} by {args.by}: {args.reason}")
    return 0


def cmd_arm(args):
    path = args.path
    state = _seed_if_missing(path, args.campaign_id)
    if state.get("campaign_id") != args.campaign_id:
        print(
            f"ERROR: kill switch file campaign_id={state.get('campaign_id')!r} "
            f"does not match requested {args.campaign_id!r}",
            file=sys.stderr,
        )
        return 1
    state["state"] = "ARMED"
    state["reason"] = None
    state["set_by"] = args.by
    state["ts_utc"] = _now_utc()
    save_state(state, path)
    print(f"ARMED campaign {args.campaign_id} at {state['ts_utc']} by {args.by}")
    return 0


def cmd_status(args):
    path = args.path
    try:
        state = load_state(path)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    armed = is_armed(path, args.campaign_id)
    print(json.dumps(state, indent=2))
    return 0 if armed else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Single-command kill switch for a class-preauthorized campaign.")
    ap.add_argument("--path", default=None, help="override KILL_SWITCH.json path (default: file next to this script)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_halt = sub.add_parser("halt")
    p_halt.add_argument("campaign_id")
    p_halt.add_argument("--reason", required=True)
    p_halt.add_argument("--by", required=True)
    p_halt.set_defaults(func=cmd_halt)

    p_arm = sub.add_parser("arm")
    p_arm.add_argument("campaign_id")
    p_arm.add_argument("--by", default="operator")
    p_arm.set_defaults(func=cmd_arm)

    p_status = sub.add_parser("status")
    p_status.add_argument("campaign_id")
    p_status.set_defaults(func=cmd_status)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
