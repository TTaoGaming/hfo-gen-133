#!/usr/bin/env python
"""Olrun facade DISPATCHER -- class pre-authorization for skill execution.

The operator pre-approves a CLASS ENVELOPE once; this dispatcher fires the
whole class without asking again. The one thing it will NOT do without a fresh
operator signature is anything in the world-effect envelopes (SEND / PUBLISH /
SPEND), anything marked requires_operator_sign, or anything whose preauth is
'instance' rather than 'class'. That refusal is the load-bearing part.

Subcommands
  list                     table of every .agents/skills/*/SKILL.md contract
  validate [--skill NAME]  parse + assert contract; JSON per skill. RUNTIME PROBE.
  probe --skill NAME       run the skill's acceptance_probe, passthrough exit code
  dispatch --skill NAME --input '{...}' [--dry-run] [--operator-sign TOKEN]

stdlib only. pyyaml is used when importable; otherwise a minimal loader for the
restricted subset used by the SKILL contract handles it.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import shlex
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _chain  # noqa: E402

try:  # prefer the real thing when present
    import yaml as _pyyaml
except ImportError:  # pragma: no cover - depends on host
    _pyyaml = None

SCHEMA_ID = "hfo.gen133.olrun_skill.v0_1"
ALLOWED_ENVELOPES = {"BUILD", "PROBE", "STAGE", "CURATE", "SEND", "PUBLISH", "SPEND"}
GATED_ENVELOPES = {"SEND", "PUBLISH", "SPEND"}
ALLOWED_PREAUTH = {"class", "instance"}
REQUIRED_KEYS = (
    "class_envelope",
    "preauth",
    "side_effects_write_paths",
    "acceptance_probe",
    "runner",
    "inputs",
)

EXIT_OK = 0
EXIT_INVALID = 1
EXIT_GATE_REFUSED = 3


# --------------------------------------------------------------------------
# minimal YAML subset loader (scalars, nested maps, block lists, inline maps)
# --------------------------------------------------------------------------

def _strip_comment(line: str) -> str:
    """Drop a trailing ' # comment'. Quote-aware; '#' inside quotes survives."""
    out = []
    quote = None
    prev = ""
    for ch in line:
        if quote:
            out.append(ch)
            if ch == quote and prev != "\\":
                quote = None
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif ch == "#" and (not out or prev in " \t"):
            break
        else:
            out.append(ch)
        prev = ch
    return "".join(out).rstrip()


def _split_top_level(text: str, sep: str = ","):
    """Split on sep, ignoring separators inside quotes/braces/brackets."""
    parts, buf, depth, quote, prev = [], [], 0, None, ""
    for ch in text:
        if quote:
            buf.append(ch)
            if ch == quote and prev != "\\":
                quote = None
        elif ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch in "{[":
            depth += 1
            buf.append(ch)
        elif ch in "}]":
            depth -= 1
            buf.append(ch)
        elif ch == sep and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
        prev = ch
    parts.append("".join(buf))
    return [p.strip() for p in parts if p.strip() != ""]


def _split_key_value(text: str):
    """Split 'key: value' at the first top-level ':' followed by space or EOL."""
    depth, quote, prev = 0, None, ""
    for i, ch in enumerate(text):
        if quote:
            if ch == quote and prev != "\\":
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1
        elif ch == ":" and depth == 0:
            rest = text[i + 1:]
            if rest == "" or rest[0] in " \t":
                return text[:i].strip(), rest.strip()
        prev = ch
    return None, None


def _parse_scalar(raw: str):
    s = raw.strip()
    if s == "":
        return None
    if s[0] in "\"'" and len(s) >= 2 and s[-1] == s[0]:
        return s[1:-1]
    if s.startswith("{") and s.endswith("}"):
        return _parse_inline_map(s)
    if s.startswith("[") and s.endswith("]"):
        return [_parse_scalar(p) for p in _split_top_level(s[1:-1])]
    low = s.lower()
    if low in ("true", "yes", "on"):
        return True
    if low in ("false", "no", "off"):
        return False
    if low in ("null", "none", "~"):
        return None
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


def _parse_inline_map(s: str):
    body = s.strip()[1:-1].strip()
    out = {}
    if not body:
        return out
    for piece in _split_top_level(body):
        key, val = _split_key_value(piece)
        if key is None:
            key, val = piece, ""
        out[key.strip("\"'")] = _parse_scalar(val)
    return out


def _tokenize(text: str):
    toks = []
    for raw in text.splitlines():
        stripped = _strip_comment(raw)
        if not stripped.strip():
            continue
        indent = len(stripped) - len(stripped.lstrip(" "))
        toks.append((indent, stripped.strip()))
    return toks


def _parse_block(toks, idx, indent):
    if idx >= len(toks):
        return None, idx
    if toks[idx][1].startswith("- "):
        return _parse_list(toks, idx, indent)
    return _parse_map(toks, idx, indent)


def _parse_list(toks, idx, indent):
    out = []
    while idx < len(toks):
        cur_indent, text = toks[idx]
        if cur_indent < indent or not text.startswith("- "):
            break
        item = text[2:].strip()
        key, val = _split_key_value(item)
        if key is not None and not item.startswith("{"):
            # list of maps: '- key: value' plus following deeper lines
            sub = {key: _parse_scalar(val)} if val != "" else {}
            idx += 1
            if val == "":
                nested, idx = _parse_block(toks, idx, cur_indent + 2)
                sub[key] = nested
            while idx < len(toks) and toks[idx][0] > cur_indent and not toks[idx][1].startswith("- "):
                k2, v2 = _split_key_value(toks[idx][1])
                if k2 is None:
                    break
                if v2 == "":
                    idx += 1
                    nested, idx = _parse_block(toks, idx, toks[idx][0] if idx < len(toks) else cur_indent + 2)
                    sub[k2] = nested
                else:
                    sub[k2] = _parse_scalar(v2)
                    idx += 1
            out.append(sub)
            continue
        out.append(_parse_scalar(item))
        idx += 1
    return out, idx


def _parse_map(toks, idx, indent):
    out = {}
    while idx < len(toks):
        cur_indent, text = toks[idx]
        if cur_indent < indent:
            break
        if text.startswith("- "):
            break
        key, val = _split_key_value(text)
        if key is None:
            idx += 1
            continue
        key = key.strip("\"'")
        if val != "":
            out[key] = _parse_scalar(val)
            idx += 1
            continue
        idx += 1
        if idx < len(toks) and toks[idx][0] > cur_indent:
            child, idx = _parse_block(toks, idx, toks[idx][0])
            out[key] = child
        else:
            out[key] = None
    return out, idx


def yaml_subset_load(text: str):
    """Minimal YAML loader for the SKILL contract subset. Always available."""
    toks = _tokenize(text)
    if not toks:
        return {}
    obj, _ = _parse_block(toks, 0, toks[0][0])
    return obj


def _normalize(obj):
    """Make the pyyaml path byte-for-byte comparable with the minimal loader.

    pyyaml auto-coerces ISO timestamps to datetime/date objects; the minimal
    loader leaves them as strings. Without this, a contract would parse
    DIFFERENTLY depending on whether pyyaml happens to be installed -- exactly
    the kind of silent environment dependence the gate must not have.
    """
    if isinstance(obj, dict):
        return {k: _normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_normalize(v) for v in obj]
    if isinstance(obj, _dt.datetime):
        return obj.astimezone(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") \
            if obj.tzinfo else obj.strftime("%Y-%m-%dT%H:%M:%SZ")
    if isinstance(obj, _dt.date):
        return obj.strftime("%Y-%m-%d")
    return obj


def load_yaml(text: str):
    """pyyaml when importable, minimal loader otherwise. Results are normalized
    so both paths agree."""
    if _pyyaml is not None:
        loaded = _pyyaml.safe_load(text)
        return _normalize(loaded) if loaded is not None else {}
    return _normalize(yaml_subset_load(text))


# --------------------------------------------------------------------------
# SKILL.md parsing
# --------------------------------------------------------------------------

_FENCE_RE = re.compile(r"^\s*```+\s*([A-Za-z0-9_-]*)\s*$")


def extract_contract_block(md_text: str):
    """Return the yaml fenced block that carries the machine-readable contract.

    Preference: the first ```yaml fence AFTER a '# SKILL' heading.
    Fallback:   any ```yaml fence whose body mentions schema_id / class_envelope.
    """
    lines = md_text.splitlines()
    blocks = []  # (start_line, lang, body)
    i = 0
    while i < len(lines):
        m = _FENCE_RE.match(lines[i])
        if m:
            lang = (m.group(1) or "").lower()
            body, j = [], i + 1
            while j < len(lines) and not _FENCE_RE.match(lines[j]):
                body.append(lines[j])
                j += 1
            blocks.append((i, lang, "\n".join(body)))
            i = j + 1
            continue
        i += 1

    heading = None
    for n, line in enumerate(lines):
        if line.lstrip().startswith("#") and "SKILL" in line.upper():
            heading = n
            break

    yaml_blocks = [b for b in blocks if b[1] in ("yaml", "yml")]
    if heading is not None:
        for start, _lang, body in yaml_blocks:
            if start > heading:
                return body
    for _start, _lang, body in yaml_blocks:
        if "class_envelope" in body or "schema_id" in body:
            return body
    return None


def parse_frontmatter_name(md_text: str):
    lines = md_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, val = _split_key_value(_strip_comment(line))
        if key == "name":
            parsed = _parse_scalar(val)
            return parsed if isinstance(parsed, str) else None
    return None


def skills_dir(root: str = None) -> str:
    return os.path.join(root or _chain.forge_root(), ".agents", "skills")


def discover_skill_files(root: str = None):
    base = skills_dir(root)
    if not os.path.isdir(base):
        return []
    out = []
    for entry in sorted(os.listdir(base)):
        path = os.path.join(base, entry, "SKILL.md")
        if os.path.isfile(path):
            out.append(path)
    return out


def load_skill(path: str):
    """-> dict(name, path, contract, parse_error)."""
    name = os.path.basename(os.path.dirname(os.path.abspath(path)))
    rec = {"name": name, "path": path, "contract": None, "parse_error": None}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        rec["parse_error"] = "unreadable: %s" % exc
        return rec
    fm_name = parse_frontmatter_name(text)
    if fm_name:
        rec["name"] = fm_name
    block = extract_contract_block(text)
    if block is None:
        rec["parse_error"] = "no ```yaml contract block found after the '# SKILL' heading"
        return rec
    try:
        contract = load_yaml(block)
    except Exception as exc:  # noqa: BLE001 - any loader failure is a parse error
        rec["parse_error"] = "yaml parse failed: %s" % exc
        return rec
    if not isinstance(contract, dict):
        rec["parse_error"] = "contract block is not a mapping (got %s)" % type(contract).__name__
        return rec
    rec["contract"] = contract
    return rec


# --------------------------------------------------------------------------
# validation
# --------------------------------------------------------------------------

_DRIVE_RE = re.compile(r"^[A-Za-z]:")


def envelope_set(contract: dict):
    raw = contract.get("class_envelope")
    if raw is None:
        return []
    if isinstance(raw, list):
        items = [str(x) for x in raw]
    else:
        items = re.split(r"[,|]", str(raw))
    return [i.strip().upper() for i in items if i.strip()]


def check_write_path(entry) -> str:
    """Return an error string, or '' when the path is acceptable."""
    if not isinstance(entry, str) or not entry.strip():
        return "side_effects_write_paths entry is not a non-empty string: %r" % (entry,)
    p = entry.strip()
    if p.startswith("~"):
        return "side_effects_write_paths entry expands outside the forge: %r" % p
    if _DRIVE_RE.match(p):
        return "side_effects_write_paths entry has a drive letter (must be forge-relative): %r" % p
    if p.startswith("/") or p.startswith("\\"):
        return "side_effects_write_paths entry is absolute (must be forge-relative): %r" % p
    if os.path.isabs(p):
        return "side_effects_write_paths entry is absolute (must be forge-relative): %r" % p
    parts = re.split(r"[\\/]+", p)
    if ".." in parts:
        return "side_effects_write_paths entry escapes the forge with '..': %r" % p
    return ""


def validate_contract(rec: dict):
    """-> {name, valid, errors:[]}"""
    errors = []
    name = rec.get("name")
    if rec.get("parse_error"):
        return {"name": name, "path": rec.get("path"), "valid": False,
                "errors": [rec["parse_error"]]}

    contract = rec["contract"]

    for key in REQUIRED_KEYS:
        if key not in contract or contract[key] is None:
            errors.append("missing required key: %s" % key)

    schema_id = contract.get("schema_id")
    if schema_id is not None and schema_id != SCHEMA_ID:
        errors.append("unexpected schema_id %r (expected %r)" % (schema_id, SCHEMA_ID))

    if "class_envelope" in contract and contract["class_envelope"] is not None:
        envs = envelope_set(contract)
        if not envs:
            errors.append("class_envelope is empty")
        for env in envs:
            if env not in ALLOWED_ENVELOPES:
                errors.append(
                    "class_envelope value %r not in allowed set %s"
                    % (env, sorted(ALLOWED_ENVELOPES))
                )

    preauth = contract.get("preauth")
    if preauth is not None and str(preauth).strip().lower() not in ALLOWED_PREAUTH:
        errors.append("preauth %r not in %s" % (preauth, sorted(ALLOWED_PREAUTH)))

    paths = contract.get("side_effects_write_paths")
    if paths is not None:
        if not isinstance(paths, list):
            errors.append("side_effects_write_paths must be a list, got %s"
                          % type(paths).__name__)
        else:
            if not paths:
                errors.append("side_effects_write_paths is empty")
            for entry in paths:
                err = check_write_path(entry)
                if err:
                    errors.append(err)

    ros = contract.get("requires_operator_sign")
    if ros is not None and not isinstance(ros, bool):
        errors.append("requires_operator_sign must be a boolean, got %r" % (ros,))

    for key in ("acceptance_probe", "runner"):
        val = contract.get(key)
        if val is not None and (not isinstance(val, str) or not val.strip()):
            errors.append("%s must be a non-empty string" % key)

    inputs = contract.get("inputs")
    if inputs is not None and not isinstance(inputs, dict):
        errors.append("inputs must be a mapping, got %s" % type(inputs).__name__)
    elif isinstance(inputs, dict):
        for iname, spec in inputs.items():
            if not isinstance(spec, dict):
                errors.append("inputs.%s must be a mapping, got %s"
                              % (iname, type(spec).__name__))
                continue
            if "required" in spec and not isinstance(spec["required"], bool):
                errors.append("inputs.%s.required must be a boolean" % iname)

    return {"name": name, "path": rec.get("path"), "valid": not errors, "errors": errors}


# --------------------------------------------------------------------------
# gate + dispatch
# --------------------------------------------------------------------------

def gate_decision(contract: dict, operator_sign):
    """-> (allowed: bool, reasons: [str])

    Refuses without a signature when ANY of:
      * class_envelope touches SEND / PUBLISH / SPEND
      * requires_operator_sign is true
      * preauth is 'instance' (per-fire signing) rather than 'class'
    """
    reasons = []
    envs = envelope_set(contract)
    hit = sorted(set(envs) & GATED_ENVELOPES)
    if hit:
        reasons.append("class_envelope contains world-effect envelope(s): %s" % ", ".join(hit))
    if contract.get("requires_operator_sign") is True:
        reasons.append("contract sets requires_operator_sign: true")
    if str(contract.get("preauth", "")).strip().lower() == "instance":
        reasons.append("preauth is 'instance' (per-fire signature), not class pre-authorization")
    if not reasons:
        return True, []
    if operator_sign:
        return True, reasons
    return False, reasons


def resolve_inputs(contract: dict, provided: dict):
    """-> (values, errors). Provided overrides declared defaults."""
    errors = []
    values = {}
    declared = contract.get("inputs") or {}
    if not isinstance(declared, dict):
        return {}, ["inputs is not a mapping"]
    for iname, spec in declared.items():
        spec = spec if isinstance(spec, dict) else {}
        if iname in provided and provided[iname] is not None:
            values[iname] = provided[iname]
        elif "default" in spec and spec["default"] is not None:
            values[iname] = spec["default"]
        elif spec.get("required") is True:
            errors.append("missing required input: %s" % iname)
        else:
            values[iname] = ""
    for key in provided:
        if key not in declared:
            errors.append("unknown input not declared by the skill: %s" % key)
    return values, errors


_PLACEHOLDER_RE = re.compile(r"\{([A-Za-z0-9_]+)\}")


def substitute(text: str, values: dict, date_str: str = None):
    """Substitute {name} placeholders; {date} is UTC YYYY-MM-DD."""
    date_str = date_str or _chain.utc_today()

    def repl(match):
        key = match.group(1)
        if key == "date":
            return date_str
        if key in values:
            return str(values[key])
        return match.group(0)

    return _PLACEHOLDER_RE.sub(repl, str(text))


def resolve_runner(contract: dict, values: dict, date_str: str = None):
    """Split the runner template FIRST, then substitute per token.

    Splitting before substitution means an input value containing spaces stays
    exactly one argv entry -- no shell, no re-parsing of user data.
    """
    template = contract.get("runner") or ""
    date_str = date_str or _chain.utc_today()
    subbed_values = {k: substitute(v, {}, date_str) if isinstance(v, str) else v
                     for k, v in values.items()}
    if str(template).strip().startswith(AGENT_NATIVE_PREFIX):
        # a directive, not a command line -- never tokenize it
        return [substitute(template, subbed_values, date_str)], subbed_values
    tokens = shlex.split(template, posix=True)
    argv = [substitute(tok, subbed_values, date_str) for tok in tokens]
    return argv, subbed_values


AGENT_NATIVE_PREFIX = "AGENT_NATIVE:"


def is_agent_native(contract: dict) -> bool:
    """A runner the dispatcher must NOT try to exec.

    Some skills are performed by the agent itself (computer-use MCP, browser,
    operator hands) rather than by a subprocess. Their runner is a directive,
    not a command line. Shelling out to it would produce a misleading exit 127
    'command not found' instead of the truth: 'a human/agent must do this'.
    """
    return str(contract.get("runner") or "").strip().startswith(AGENT_NATIVE_PREFIX)


def _tail(text: str, limit: int = 2000) -> str:
    text = text or ""
    return text[-limit:]


def run_command(argv, cwd: str):
    try:
        proc = subprocess.run(  # noqa: S603 - shell=False, argv pre-split
            argv, cwd=cwd, shell=False, capture_output=True, text=True,
        )
        return proc.returncode, proc.stdout, proc.stderr
    except FileNotFoundError as exc:
        return 127, "", "command not found: %s" % exc
    except OSError as exc:
        return 126, "", "exec failed: %s" % exc


# --------------------------------------------------------------------------
# subcommands
# --------------------------------------------------------------------------

def find_skill(name: str, root: str = None):
    for path in discover_skill_files(root):
        rec = load_skill(path)
        if rec["name"] == name or os.path.basename(os.path.dirname(path)) == name:
            return rec
    return None


def cmd_list(args):
    files = discover_skill_files(args.root)
    if not files:
        print("no SKILL.md contracts found under %s" % skills_dir(args.root))
        return EXIT_OK
    rows = []
    for path in files:
        rec = load_skill(path)
        contract = rec["contract"] or {}
        rows.append((
            rec["name"],
            ",".join(envelope_set(contract)) or ("PARSE_ERROR" if rec["parse_error"] else "-"),
            str(contract.get("preauth", "-")),
            str(contract.get("requires_operator_sign", False)),
            str(contract.get("acceptance_probe", "-")),
        ))
    headers = ("name", "class_envelope", "preauth", "requires_operator_sign", "acceptance_probe")
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))
    fmt = "  ".join("{:<%d}" % w for w in widths)
    print(fmt.format(*headers))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        print(fmt.format(*row))
    print("\n%d skill(s) under %s" % (len(rows), skills_dir(args.root)))
    return EXIT_OK


def cmd_validate(args):
    files = discover_skill_files(args.root)
    if args.skill:
        files = [p for p in files
                 if os.path.basename(os.path.dirname(p)) == args.skill
                 or (load_skill(p)["name"] == args.skill)]
    results = [validate_contract(load_skill(p)) for p in files]
    print(json.dumps(results, indent=2, ensure_ascii=False))
    if not results:
        print(json.dumps(
            {"note": "no skills matched; nothing validated",
             "skills_dir": skills_dir(args.root)}, indent=2))
        return EXIT_OK
    return EXIT_OK if all(r["valid"] for r in results) else EXIT_INVALID


def cmd_probe(args):
    rec = find_skill(args.skill, args.root)
    if rec is None:
        print(json.dumps({"error": "skill not found: %s" % args.skill,
                          "skills_dir": skills_dir(args.root)}, indent=2))
        return EXIT_INVALID
    if rec["parse_error"]:
        print(json.dumps({"error": rec["parse_error"], "skill": args.skill}, indent=2))
        return EXIT_INVALID
    probe = rec["contract"].get("acceptance_probe")
    if not probe:
        print(json.dumps({"error": "no acceptance_probe declared", "skill": args.skill}, indent=2))
        return EXIT_INVALID
    root = args.root or _chain.forge_root()
    argv = shlex.split(substitute(probe, {}), posix=True)
    code, out, err = run_command(argv, root)
    print(json.dumps({
        "skill": rec["name"],
        "acceptance_probe": probe,
        "argv": argv,
        "exit_code": code,
        "stdout_tail": _tail(out),
        "stderr_tail": _tail(err, 1000),
    }, indent=2, ensure_ascii=False))
    return code


def cmd_dispatch(args):
    root = args.root or _chain.forge_root()
    rec = find_skill(args.skill, root)
    if rec is None:
        print(json.dumps({"error": "skill not found: %s" % args.skill,
                          "skills_dir": skills_dir(root)}, indent=2))
        return EXIT_INVALID
    if rec["parse_error"]:
        print(json.dumps({"error": rec["parse_error"], "skill": args.skill}, indent=2))
        return EXIT_INVALID

    verdict = validate_contract(rec)
    if not verdict["valid"]:
        print(json.dumps({"error": "contract invalid; refusing to dispatch",
                          "skill": rec["name"], "errors": verdict["errors"]}, indent=2))
        return EXIT_INVALID

    contract = rec["contract"]
    try:
        provided = json.loads(args.input) if args.input else {}
    except ValueError as exc:
        print(json.dumps({"error": "--input is not valid JSON: %s" % exc}, indent=2))
        return EXIT_INVALID
    if not isinstance(provided, dict):
        print(json.dumps({"error": "--input must be a JSON object"}, indent=2))
        return EXIT_INVALID

    values, input_errors = resolve_inputs(contract, provided)
    if input_errors:
        print(json.dumps({"error": "input resolution failed", "skill": rec["name"],
                          "errors": input_errors}, indent=2))
        return EXIT_INVALID

    allowed, reasons = gate_decision(contract, args.operator_sign)
    argv, resolved_values = resolve_runner(contract, values)
    sign_cmd = (
        "python tools/olrun/dispatch_class.py dispatch --skill %s --input '%s' "
        "--operator-sign <TOKEN>" % (rec["name"], json.dumps(provided, separators=(",", ":")))
    )

    if not allowed:
        payload = {
            "skill": rec["name"],
            "gate": "REFUSED",
            "refusal_reasons": reasons,
            "class_envelope": envelope_set(contract),
            "preauth": contract.get("preauth"),
            "requires_operator_sign": bool(contract.get("requires_operator_sign")),
            "resolved_command": argv,
            "executed": False,
            "to_sign_run": sign_cmd,
            "dispatched_utc": _chain.utc_now_iso(),
        }
        if not args.dry_run:
            row = _chain.append_row(
                action="dispatch_refused",
                skill=rec["name"],
                verifier_result="envelope gate REFUSED: %s" % "; ".join(reasons),
                claim_status="failed",
                remaining_risk=["operator signature not supplied for a gated envelope"],
                next_safe_action="operator reviews and re-runs with --operator-sign",
                honest_flaw="gate refusal is advisory-in-process; a caller invoking the "
                            "runner directly bypasses this dispatcher entirely",
                chain_path=args.chain,
                extra={"resolved_command": argv},
            )
            payload["chain_row_id"] = row["row_id"]
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return EXIT_GATE_REFUSED

    if args.dry_run:
        print(json.dumps({
            "skill": rec["name"],
            "gate": "ALLOWED" + (" (operator-signed)" if reasons else " (class pre-authorized)"),
            "gate_notes": reasons,
            "class_envelope": envelope_set(contract),
            "resolved_inputs": resolved_values,
            "resolved_command": argv,
            "side_effects_write_paths": contract.get("side_effects_write_paths"),
            "executed": False,
            "dry_run": True,
            "dispatched_utc": _chain.utc_now_iso(),
        }, indent=2, ensure_ascii=False))
        return EXIT_OK

    if is_agent_native(contract):
        row = _chain.append_row(
            action="dispatch_handoff_agent_native",
            skill=rec["name"],
            verifier_result="runner is an AGENT_NATIVE directive; no subprocess was executed: %s"
                            % argv[0],
            claim_status="proposed",
            remaining_risk=["the agent has not yet performed the directive; nothing has happened"],
            next_safe_action="the calling agent performs the directive and writes its receipt to "
                             "%s" % contract.get("side_effects_write_paths"),
            honest_flaw="this is a handoff, not an execution -- do not read it as work done",
            chain_path=args.chain,
            extra={"directive": argv[0]},
        )
        print(json.dumps({
            "skill": rec["name"],
            "gate": "ALLOWED" + (" (operator-signed)" if reasons else " (class pre-authorized)"),
            "runner_kind": "agent_native",
            "directive": argv[0],
            "executed": False,
            "requires_agent_execution": True,
            "exit_code": None,
            "stdout_tail": "",
            "chain_row_id": row["row_id"],
            "dispatched_utc": _chain.utc_now_iso(),
        }, indent=2, ensure_ascii=False))
        return EXIT_OK

    dispatched = _chain.utc_now_iso()
    code, out, err = run_command(argv, root)
    status = "wired_with_receipts" if code == 0 else "failed"
    row = _chain.append_row(
        action="dispatch_executed",
        skill=rec["name"],
        verifier_result="argv=%s exit_code=%d stdout_tail=%r stderr_tail=%r"
                        % (argv, code, _tail(out, 400), _tail(err, 400)),
        claim_status=status,
        remaining_risk=[
            "declared side_effects_write_paths are not enforced at runtime, only declared",
            "runner exit code is the only evidence; the runner's own claims are unverified here",
        ],
        next_safe_action="read the runner output artifact and confirm it exists on disk",
        honest_flaw="exit_code 0 proves the process ran, not that the skill's claim is true",
        chain_path=args.chain,
        extra={"exit_code": code, "resolved_command": argv,
               "gate": "signed" if reasons else "class_preauth"},
    )
    print(json.dumps({
        "skill": rec["name"],
        "exit_code": code,
        "stdout_tail": _tail(out),
        "stderr_tail": _tail(err, 1000),
        "chain_row_id": row["row_id"],
        "dispatched_utc": dispatched,
    }, indent=2, ensure_ascii=False))
    return code


def build_parser():
    p = argparse.ArgumentParser(
        prog="dispatch_class.py",
        description="Olrun facade dispatcher -- class pre-authorized skill execution.",
    )
    p.add_argument("--root", default=None, help="forge root (default: repo root of this file)")
    p.add_argument("--chain", default=None, help="chain path (default: chains/OLRUN_FACADE.jsonl)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="table of all skill contracts")

    v = sub.add_parser("validate", help="parse + assert contracts (runtime probe)")
    v.add_argument("--skill", default=None)

    pr = sub.add_parser("probe", help="run a skill's acceptance_probe")
    pr.add_argument("--skill", required=True)

    d = sub.add_parser("dispatch", help="fire a skill through the envelope gate")
    d.add_argument("--skill", required=True)
    d.add_argument("--input", default=None, help="JSON object of inputs")
    d.add_argument("--dry-run", action="store_true")
    d.add_argument("--operator-sign", default=None, help="operator signature token")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return {
        "list": cmd_list,
        "validate": cmd_validate,
        "probe": cmd_probe,
        "dispatch": cmd_dispatch,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
