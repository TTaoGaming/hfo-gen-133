#!/usr/bin/env python3
"""
render_proposal.py -- the envelope enforcement CLI for Upwork proposal
rendering.

Same enforcement shape as
projects/outreach_class_preauth/render_message.py: this program is the
only path that turns a proposal template + a job.json row into rendered
proposal text, and it refuses to do so unless every element of the
envelope is satisfied. It has no network access and submits nothing --
Upwork proposals are pasted and submitted by the operator, by hand,
through the Upwork UI. This script only renders text to stdout, or
refuses with a non-zero exit code and a reason on stderr.

Usage:
    python render_proposal.py --template proposal_template.md --job job.json \
        [--allowlist-file allowlist.json] [--max-age-days 7] [--dry-run]

job.json is a single JSON object (not JSONL). It must carry the three
required fields (job_url, job_title, posted_utc) and, for any template
variable to resolve, a value under that variable's own key -- the same
"target row" shape render_message.py uses for prospect rows.

Exit codes:
    0  success -- rendered proposal printed to stdout (or, with --dry-run,
       the resolved variables printed as JSON, body withheld)
    1  usage / file-not-found / bad-JSON error (not a policy refusal)
    2  template uses a variable not present in the variable allowlist
    3  a template variable is in the allowlist but has no usable value in
       job.json
    4  the rendered body exceeds the 200-word cap
    5  job.json is missing a required field: job_url, job_title, or
       posted_utc (or posted_utc is not a parseable Z-suffixed UTC
       timestamp)
    6  the job post is older than --max-age-days (default 7)

Check order (cheapest, most-invalidating checks first): job.json shape
(5) before staleness (6) before template/allowlist (2) before
per-variable values (3) before the word cap (4). A stale or malformed
job is refused before any time is spent resolving copy for it -- stale
posts convert poorly and burn Connects, so that check comes before copy
work, not after.
"""
import argparse
import json
import pathlib
import re
import sys
from datetime import datetime, timezone

VAR_RE = re.compile(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}")
REQUIRED_JOB_FIELDS = ["job_url", "job_title", "posted_utc"]
WORD_CAP = 200
DEFAULT_ALLOWLIST_PATH = pathlib.Path(__file__).resolve().with_name("allowlist.json")


def load_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))


def load_text(path):
    return pathlib.Path(path).read_text(encoding="utf-8")


def extract_variables(template_text):
    return set(VAR_RE.findall(template_text))


def is_value_usable(value):
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == "":
        return False
    return True


def render(template_text, job):
    def repl(match):
        var = match.group(1)
        val = job.get(var)
        return "" if val is None else str(val)

    return VAR_RE.sub(repl, template_text)


def parse_utc(ts):
    """Parse a strict '...Z' ISO-8601 UTC timestamp. Raises ValueError otherwise."""
    if not isinstance(ts, str) or not ts.endswith("Z"):
        raise ValueError(f"not a Z-suffixed UTC timestamp: {ts!r}")
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Render an Upwork proposal inside its allowlisted envelope, or refuse."
    )
    parser.add_argument("--template", required=True, help="path to the proposal template text file")
    parser.add_argument(
        "--job",
        required=True,
        help="path to job.json (single JSON object: required job fields + template variable values)",
    )
    parser.add_argument(
        "--allowlist-file",
        default=None,
        help="path to a JSON array of allowed variable names (default: allowlist.json next to this script)",
    )
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=7,
        help="refuse job posts older than this many days (default 7)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print resolved variables as JSON only; skip the word cap and do not print the body",
    )
    args = parser.parse_args(argv)

    try:
        job = load_json(args.job)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: could not load job {args.job}: {exc}", file=sys.stderr)
        return 1
    if not isinstance(job, dict):
        print(
            f"ERROR: {args.job} must contain a single JSON object, got {type(job).__name__}",
            file=sys.stderr,
        )
        return 1

    missing_fields = [f for f in REQUIRED_JOB_FIELDS if not is_value_usable(job.get(f))]
    if missing_fields:
        print(
            f"REFUSED (exit 5): {args.job} is missing required field(s): {missing_fields}",
            file=sys.stderr,
        )
        return 5

    try:
        posted_at = parse_utc(job["posted_utc"])
    except ValueError as exc:
        print(f"REFUSED (exit 5): job.json posted_utc is unusable: {exc}", file=sys.stderr)
        return 5

    age_days = (datetime.now(timezone.utc) - posted_at).total_seconds() / 86400.0
    if age_days > args.max_age_days:
        print(
            f"REFUSED (exit 6): job post {job.get('job_url')!r} is {age_days:.1f} days old, "
            f"exceeds --max-age-days={args.max_age_days}. Stale posts convert poorly and burn Connects.",
            file=sys.stderr,
        )
        return 6

    try:
        template_text = load_text(args.template)
    except OSError as exc:
        print(f"ERROR: could not read template {args.template}: {exc}", file=sys.stderr)
        return 1

    allowlist_path = args.allowlist_file or DEFAULT_ALLOWLIST_PATH
    try:
        allowlist = set(load_json(allowlist_path))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: could not load allowlist {allowlist_path}: {exc}", file=sys.stderr)
        return 1

    variables_in_template = extract_variables(template_text)
    not_allowed = sorted(variables_in_template - allowlist)
    if not_allowed:
        print(
            f"REFUSED (exit 2): template uses variable(s) outside the allowlist: {not_allowed}",
            file=sys.stderr,
        )
        return 2

    missing_values = sorted(v for v in variables_in_template if not is_value_usable(job.get(v)))
    if missing_values:
        print(
            f"REFUSED (exit 3): required variable(s) have no usable value in {args.job}: {missing_values}",
            file=sys.stderr,
        )
        return 3

    if args.dry_run:
        resolved = {v: job.get(v) for v in sorted(variables_in_template)}
        print(json.dumps(resolved, indent=2))
        return 0

    rendered = render(template_text, job)
    word_count = len(rendered.split())
    if word_count > WORD_CAP:
        print(
            f"REFUSED (exit 4): rendered body is {word_count} words, exceeds the {WORD_CAP}-word cap.",
            file=sys.stderr,
        )
        return 4

    print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
