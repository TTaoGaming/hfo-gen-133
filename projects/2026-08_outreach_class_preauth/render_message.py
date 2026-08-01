#!/usr/bin/env python3
"""
render_message.py -- the envelope enforcement CLI for class-preauthorized outreach.

This program IS the envelope. A campaign_authorization document (see
campaign_authorization.schema.json) pre-authorizes a CLASS of send:
audience + copy template + variable allowlist + cadence + opt-out + kill
switch. This program is the only path that turns a template + a prospect
row into a message body, and it refuses to do so unless every element of
the authorized envelope is satisfied. It has no network access and sends
nothing itself -- it only renders text to stdout, or refuses with a
non-zero exit code and a reason on stderr.

Usage:
    python render_message.py --auth AUTH.json --template TEMPLATE.txt --target PROSPECT_ID --targets TARGETS.jsonl

Exit codes:
    0  success -- rendered message printed to stdout
    1  usage / file-not-found / target-not-found error (not a security refusal)
    2  template uses a variable not present in the authorization variable_allowlist
    3  a template variable is in the allowlist but has no usable value in the target row
    4  the rendered body does not contain the authorization opt_out_language verbatim
    5  the target row is not sendable: suppression=true, email is null, or
       email_verification_status != "valid"
    6  the template file sha256 does not match authorization.copy_template_sha256
    7  the kill switch for this campaign_id is not in state ARMED

Check order (kill switch first, everything else follows): a halted campaign
must be refused before any other work is done, regardless of how well-formed
the request otherwise is.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

import kill_switch

VAR_RE = re.compile(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}")


def load_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))


def load_targets(path):
    rows = []
    with open(path, "r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
    return rows


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def find_target(rows, prospect_id):
    for row in rows:
        if row.get("prospect_id") == prospect_id:
            return row
    return None


def extract_variables(template_text):
    return set(VAR_RE.findall(template_text))


def render(template_text, target_row):
    def repl(match):
        var = match.group(1)
        val = target_row.get(var)
        return "" if val is None else str(val)

    return VAR_RE.sub(repl, template_text)


def is_value_usable(value):
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == "":
        return False
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description="Render an outreach message inside its authorized envelope, or refuse.")
    parser.add_argument("--auth", required=True, help="path to campaign authorization JSON")
    parser.add_argument("--template", required=True, help="path to the template text file")
    parser.add_argument("--target", required=True, help="prospect_id of the row to render for")
    parser.add_argument("--targets", required=True, help="path to the targets JSONL file")
    args = parser.parse_args(argv)

    try:
        auth = load_json(args.auth)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: could not load authorization {args.auth}: {exc}", file=sys.stderr)
        return 1

    campaign_id = auth.get("campaign_id")
    kill_switch_path = auth.get("kill_switch_path")

    try:
        armed = kill_switch.is_armed(kill_switch_path, campaign_id)
    except Exception as exc:
        print(f"REFUSED (exit 7): could not confirm kill switch is ARMED for {campaign_id}: {exc}", file=sys.stderr)
        return 7
    if not armed:
        print(
            f"REFUSED (exit 7): kill switch for campaign {campaign_id!r} at {kill_switch_path!r} is not ARMED.",
            file=sys.stderr,
        )
        return 7

    try:
        template_bytes = pathlib.Path(args.template).read_bytes()
    except OSError as exc:
        print(f"ERROR: could not read template {args.template}: {exc}", file=sys.stderr)
        return 1
    template_text = template_bytes.decode("utf-8")

    actual_sha = sha256_bytes(template_bytes)
    expected_sha = auth.get("copy_template_sha256")
    if actual_sha != expected_sha:
        print(
            f"REFUSED (exit 6): template {args.template} sha256 {actual_sha} "
            f"does not match authorization copy_template_sha256 {expected_sha}.",
            file=sys.stderr,
        )
        return 6

    variables_in_template = extract_variables(template_text)
    allowlist = set(auth.get("variable_allowlist", []))
    not_allowed = sorted(variables_in_template - allowlist)
    if not_allowed:
        print(
            f"REFUSED (exit 2): template uses variable(s) outside variable_allowlist: {not_allowed}",
            file=sys.stderr,
        )
        return 2

    try:
        targets = load_targets(args.targets)
    except (OSError, ValueError) as exc:
        print(f"ERROR: could not load targets {args.targets}: {exc}", file=sys.stderr)
        return 1

    target_row = find_target(targets, args.target)
    if target_row is None:
        print(f"ERROR: prospect_id {args.target!r} not found in {args.targets}", file=sys.stderr)
        return 1

    suppression = target_row.get("suppression")
    email = target_row.get("email")
    verification = target_row.get("email_verification_status")
    if suppression is True or email is None or verification != "valid":
        print(
            "REFUSED (exit 5): target is not sendable "
            f"(prospect_id={args.target!r}, suppression={suppression!r}, "
            f"email={email!r}, email_verification_status={verification!r}).",
            file=sys.stderr,
        )
        return 5

    missing = sorted(v for v in variables_in_template if not is_value_usable(target_row.get(v)))
    if missing:
        print(
            f"REFUSED (exit 3): required variable(s) have no usable value in target row {args.target!r}: {missing}",
            file=sys.stderr,
        )
        return 3

    rendered = render(template_text, target_row)

    opt_out = auth.get("opt_out_language", "")
    if not opt_out or opt_out not in rendered:
        print(
            "REFUSED (exit 4): rendered body does not contain authorization opt_out_language verbatim.",
            file=sys.stderr,
        )
        return 4

    print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())