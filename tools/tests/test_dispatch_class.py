"""Held-out tests for the Olrun facade dispatcher.

These are RUNTIME probes, not static checks. In particular the envelope gate is
tested in BOTH directions: a PUBLISH skill must refuse and NOT execute without a
signature, and must proceed with one. Fixtures live in tmp_path -- no real
.agents/skills/ file is read, so the suite passes whether or not the lead has
authored the real skills yet.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
FORGE = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(FORGE, "tools", "olrun"))

import _chain  # noqa: E402
import dispatch_class as dc  # noqa: E402


REPRESENTATIVE_BLOCK = """schema_id: hfo.gen133.olrun_skill.v0_1
class_envelope: BUILD | PROBE | CURATE   # comma list
preauth: class            # 'class' = operator approves once
side_effects_write_paths:
  - state/curated_memory/**
  - state/olrun/relay/
requires_operator_sign: false
acceptance_probe: "python tools/olrun/curate_memory.py health"
runner: "python tools/olrun/curate_memory.py harvest --topics {topics} --limit-per-topic {limit_per_topic} --out {out}"
inputs:
  topics: {type: string, required: true}
  limit_per_topic: {type: int, required: false, default: 12}
  out: {type: string, required: false, default: "state/curated_memory/{date}/"}
"""


def _skill_md(block: str, name: str = "fixture-skill") -> str:
    return (
        "---\n"
        "name: %s\n"
        "description: fixture used by the held-out dispatcher tests\n"
        "---\n\n"
        "# SKILL - %s\n\n"
        "```yaml\n%s```\n\n"
        "## Purpose\nFixture.\n" % (name, name, block)
    )


def write_skill(root, dirname, block, name=None):
    d = os.path.join(str(root), ".agents", "skills", dirname)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "SKILL.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(_skill_md(block, name or dirname))
    return path


# ---------------------------------------------------------------- yaml subset

def test_yaml_subset_loader_parses_representative_block():
    got = dc.yaml_subset_load(REPRESENTATIVE_BLOCK)
    assert got["schema_id"] == "hfo.gen133.olrun_skill.v0_1"
    # trailing '# comma list' comment must be stripped, not folded into the value
    assert got["class_envelope"] == "BUILD | PROBE | CURATE"
    assert got["preauth"] == "class"
    assert got["side_effects_write_paths"] == ["state/curated_memory/**", "state/olrun/relay/"]
    assert got["requires_operator_sign"] is False
    assert got["acceptance_probe"] == "python tools/olrun/curate_memory.py health"
    assert got["runner"].startswith("python tools/olrun/curate_memory.py harvest")
    assert got["inputs"]["topics"] == {"type": "string", "required": True}
    assert got["inputs"]["limit_per_topic"]["default"] == 12
    assert got["inputs"]["limit_per_topic"]["required"] is False
    # a '{date}' inside a quoted inline-map value must survive intact
    assert got["inputs"]["out"]["default"] == "state/curated_memory/{date}/"


def test_yaml_subset_loader_matches_pyyaml_when_available():
    yaml = pytest.importorskip("yaml")
    assert dc.yaml_subset_load(REPRESENTATIVE_BLOCK) == yaml.safe_load(REPRESENTATIVE_BLOCK)


def test_loader_result_does_not_depend_on_pyyaml_being_installed():
    """A contract must parse identically with and without pyyaml.

    pyyaml coerces bare ISO timestamps to datetime objects; the minimal loader
    does not. dc.load_yaml normalizes both, so the gate cannot behave one way on
    a host with pyyaml and another way without it.
    """
    pytest.importorskip("yaml")
    block = REPRESENTATIVE_BLOCK + "now_utc: 2026-08-02T14:58:07Z\nas_of: 2026-08-02\n"
    via_pyyaml = dc.load_yaml(block)             # pyyaml path + normalize
    via_minimal = dc._normalize(dc.yaml_subset_load(block))
    assert via_pyyaml == via_minimal
    assert via_pyyaml["now_utc"] == "2026-08-02T14:58:07Z"
    assert via_pyyaml["as_of"] == "2026-08-02"


@pytest.mark.parametrize("path", sorted(
    __import__("glob").glob(os.path.join(FORGE, ".agents", "skills", "*", "SKILL.md"))))
def test_real_skill_contracts_parse_the_same_on_both_loaders(path):
    """Runs against whatever real contracts exist; auto-skips if none authored."""
    pytest.importorskip("yaml")
    block = dc.extract_contract_block(open(path, encoding="utf-8").read())
    assert block is not None, path
    import yaml as _y
    assert dc._normalize(_y.safe_load(block)) == dc._normalize(dc.yaml_subset_load(block))


def test_envelope_set_splits_on_pipe_and_comma():
    assert dc.envelope_set({"class_envelope": "BUILD | PROBE"}) == ["BUILD", "PROBE"]
    assert dc.envelope_set({"class_envelope": "send,PUBLISH"}) == ["SEND", "PUBLISH"]


def test_extract_contract_block_takes_the_block_after_the_heading():
    md = _skill_md(REPRESENTATIVE_BLOCK)
    block = dc.extract_contract_block(md)
    assert block is not None and "class_envelope" in block
    assert dc.load_yaml(block)["preauth"] == "class"


# ---------------------------------------------------------------- validation

def _validate_block(tmp_path, block, dirname="s"):
    write_skill(tmp_path, dirname, block)
    return dc.validate_contract(
        dc.load_skill(os.path.join(str(tmp_path), ".agents", "skills", dirname, "SKILL.md"))
    )


def test_validate_accepts_the_representative_contract(tmp_path):
    res = _validate_block(tmp_path, REPRESENTATIVE_BLOCK)
    assert res["valid"] is True, res["errors"]
    assert res["errors"] == []


def test_validate_rejects_absolute_write_path(tmp_path):
    block = REPRESENTATIVE_BLOCK.replace(
        "  - state/curated_memory/**", "  - C:/Dev/hfo_gen_133_forge/state/x")
    res = _validate_block(tmp_path, block, "abs")
    assert res["valid"] is False
    assert any("drive letter" in e or "absolute" in e for e in res["errors"]), res["errors"]


def test_validate_rejects_posix_absolute_write_path(tmp_path):
    block = REPRESENTATIVE_BLOCK.replace("  - state/curated_memory/**", "  - /etc/passwd")
    res = _validate_block(tmp_path, block, "absposix")
    assert res["valid"] is False
    assert any("absolute" in e for e in res["errors"]), res["errors"]


def test_validate_rejects_dotdot_escape(tmp_path):
    block = REPRESENTATIVE_BLOCK.replace(
        "  - state/curated_memory/**", "  - ../../outside/state/**")
    res = _validate_block(tmp_path, block, "escape")
    assert res["valid"] is False
    assert any("escapes the forge" in e for e in res["errors"]), res["errors"]


def test_validate_rejects_missing_required_key(tmp_path):
    block = "\n".join(
        ln for ln in REPRESENTATIVE_BLOCK.splitlines() if not ln.startswith("runner:")
    ) + "\n"
    res = _validate_block(tmp_path, block, "missing")
    assert res["valid"] is False
    assert any("missing required key: runner" in e for e in res["errors"]), res["errors"]


def test_validate_rejects_bad_envelope_value(tmp_path):
    block = REPRESENTATIVE_BLOCK.replace(
        "class_envelope: BUILD | PROBE | CURATE   # comma list",
        "class_envelope: BUILD | DESTROY")
    res = _validate_block(tmp_path, block, "badenv")
    assert res["valid"] is False
    assert any("DESTROY" in e for e in res["errors"]), res["errors"]


def test_validate_rejects_bad_preauth(tmp_path):
    block = REPRESENTATIVE_BLOCK.replace("preauth: class", "preauth: whenever")
    res = _validate_block(tmp_path, block, "badpre")
    assert res["valid"] is False
    assert any("preauth" in e for e in res["errors"]), res["errors"]


# ---------------------------------------------------------------- substitution

def test_date_substitution_is_a_valid_utc_date():
    from datetime import datetime, timezone
    out = dc.substitute("state/curated_memory/{date}/", {})
    m = re.search(r"(\d{4}-\d{2}-\d{2})", out)
    assert m, out
    parsed = datetime.strptime(m.group(1), "%Y-%m-%d").date()
    assert parsed == datetime.now(timezone.utc).date()
    assert "{date}" not in out


def test_resolve_runner_keeps_spacey_values_as_one_argv_entry():
    contract = dc.load_yaml(REPRESENTATIVE_BLOCK)
    values, errs = dc.resolve_inputs(contract, {"topics": "a b, c d"})
    assert errs == []
    argv, resolved = dc.resolve_runner(contract, values)
    assert "a b, c d" in argv, argv
    assert argv.count("a b, c d") == 1
    assert resolved["limit_per_topic"] == 12          # default applied
    assert "{date}" not in " ".join(argv)             # default's {date} resolved


def test_resolve_inputs_errors_on_missing_required():
    contract = dc.load_yaml(REPRESENTATIVE_BLOCK)
    _values, errs = dc.resolve_inputs(contract, {})
    assert any("missing required input: topics" in e for e in errs), errs


# ---------------------------------------------------------------- ENVELOPE GATE

SIDE_EFFECT_SCRIPT = (
    "import sys, pathlib\n"
    "pathlib.Path('SIDE_EFFECT_MARKER.txt').write_text('fired ' + ' '.join(sys.argv[1:]))\n"
    "print('SIDE_EFFECT_FIRED')\n"
)


def write_publish_skill(tmp_path):
    """A PUBLISH-envelope skill whose runner leaves a filesystem trace.

    Execution is then provable by the marker file, not by parsing stdout -- so
    'the gate blocked it' cannot be faked by a string that merely appears in the
    refusal payload's echoed command.
    """
    script = os.path.join(str(tmp_path), "side_effect.py")
    with open(script, "w", encoding="utf-8") as fh:
        fh.write(SIDE_EFFECT_SCRIPT)
    runner_line = 'runner: "%s side_effect.py {topics}"' % sys.executable.replace("\\", "/")
    block = "\n".join(
        runner_line if ln.startswith("runner:") else ln
        for ln in REPRESENTATIVE_BLOCK.replace(
            "class_envelope: BUILD | PROBE | CURATE   # comma list",
            "class_envelope: BUILD | PUBLISH").splitlines()
    ) + "\n"
    write_skill(tmp_path, "pubskill", block)
    return os.path.join(str(tmp_path), "SIDE_EFFECT_MARKER.txt")


def _dispatch(tmp_path, extra_args):
    chain = os.path.join(str(tmp_path), "chain.jsonl")
    args = ["--root", str(tmp_path), "--chain", chain] + extra_args
    return dc.main(args), chain


def test_gate_blocks_publish_without_signature(tmp_path, capsys):
    marker = write_publish_skill(tmp_path)
    code, chain = _dispatch(tmp_path, [
        "dispatch", "--skill", "pubskill", "--input", '{"topics":"x"}'])
    out = capsys.readouterr().out
    assert code == dc.EXIT_GATE_REFUSED == 3, out
    payload = json.loads(out)
    assert payload["gate"] == "REFUSED"
    assert payload["executed"] is False
    assert any("PUBLISH" in r for r in payload["refusal_reasons"]), payload
    assert "--operator-sign" in payload["to_sign_run"]
    # the runner must NOT have run -- proven by the absent filesystem trace
    assert not os.path.exists(marker), "gated runner executed anyway"
    rows = _chain.read_rows(chain)
    assert rows and rows[-1]["action"] == "dispatch_refused"
    assert rows[-1]["claim_status"] == "failed"


def test_gate_allows_publish_with_signature(tmp_path, capsys):
    marker = write_publish_skill(tmp_path)
    code, chain = _dispatch(tmp_path, [
        "dispatch", "--skill", "pubskill", "--input", '{"topics":"x"}',
        "--operator-sign", "OPERATOR_TOKEN_TEST"])
    out = capsys.readouterr().out
    payload = json.loads(out)
    assert code == 0, out
    assert payload["exit_code"] == 0
    assert "SIDE_EFFECT_FIRED" in payload["stdout_tail"]
    assert os.path.exists(marker), "signed dispatch did not actually execute"
    assert "fired x" in open(marker, encoding="utf-8").read()
    rows = _chain.read_rows(chain)
    assert rows[-1]["action"] == "dispatch_executed"
    assert rows[-1]["claim_status"] == "wired_with_receipts"


def test_gate_blocks_requires_operator_sign_true(tmp_path, capsys):
    block = REPRESENTATIVE_BLOCK.replace(
        "requires_operator_sign: false", "requires_operator_sign: true")
    write_skill(tmp_path, "signme", block)
    code, _chain_path = _dispatch(tmp_path, [
        "dispatch", "--skill", "signme", "--input", '{"topics":"x"}', "--dry-run"])
    payload = json.loads(capsys.readouterr().out)
    assert code == 3
    assert any("requires_operator_sign" in r for r in payload["refusal_reasons"])


def test_gate_blocks_preauth_instance(tmp_path, capsys):
    block = REPRESENTATIVE_BLOCK.replace("preauth: class", "preauth: instance")
    write_skill(tmp_path, "perfire", block)
    code, _chain_path = _dispatch(tmp_path, [
        "dispatch", "--skill", "perfire", "--input", '{"topics":"x"}', "--dry-run"])
    payload = json.loads(capsys.readouterr().out)
    assert code == 3
    assert any("instance" in r for r in payload["refusal_reasons"])


def test_class_preauthorized_skill_dry_runs_without_signature(tmp_path, capsys):
    write_skill(tmp_path, "curate", REPRESENTATIVE_BLOCK)
    code, _chain_path = _dispatch(tmp_path, [
        "dispatch", "--skill", "curate", "--input", '{"topics":"a,b"}', "--dry-run"])
    payload = json.loads(capsys.readouterr().out)
    assert code == 0
    assert payload["gate"].startswith("ALLOWED")
    assert payload["executed"] is False
    assert payload["resolved_inputs"]["topics"] == "a,b"


def test_agent_native_runner_is_handed_off_not_executed(tmp_path, capsys):
    """An 'AGENT_NATIVE:' runner must not be shelled out to.

    Executing it would yield a misleading exit 127 'command not found' instead
    of the truth: a human/agent still has to do the thing.
    """
    block = "\n".join(
        'runner: "AGENT_NATIVE: computer-use MCP - open {topics}"'
        if ln.startswith("runner:") else ln
        for ln in REPRESENTATIVE_BLOCK.splitlines()) + "\n"
    write_skill(tmp_path, "native", block)
    code, chain = _dispatch(tmp_path, [
        "dispatch", "--skill", "native", "--input", '{"topics":"Notepad"}'])
    payload = json.loads(capsys.readouterr().out)
    assert code == 0
    assert payload["runner_kind"] == "agent_native"
    assert payload["executed"] is False
    assert payload["exit_code"] is None
    assert payload["directive"] == "AGENT_NATIVE: computer-use MCP - open Notepad"
    rows = _chain.read_rows(chain)
    assert rows[-1]["claim_status"] == "proposed", "a handoff must never claim receipts"


# ---------------------------------------------------------------- list/validate CLI

def test_list_and_validate_exit_codes(tmp_path, capsys):
    write_skill(tmp_path, "good", REPRESENTATIVE_BLOCK)
    assert dc.main(["--root", str(tmp_path), "list"]) == 0
    assert "class_envelope" in capsys.readouterr().out

    assert dc.main(["--root", str(tmp_path), "validate"]) == 0
    results = json.loads(capsys.readouterr().out)
    assert results[0]["valid"] is True

    write_skill(tmp_path, "bad",
                REPRESENTATIVE_BLOCK.replace("  - state/curated_memory/**", "  - ../escape"))
    assert dc.main(["--root", str(tmp_path), "validate"]) == 1
    capsys.readouterr()


# ---------------------------------------------------------------- chain append-only

def test_chain_append_is_append_only_and_increments(tmp_path):
    path = os.path.join(str(tmp_path), "chains", "OLRUN_FACADE.jsonl")
    r1 = _chain.append_row("a1", "v1", "proposed", ["r1"], "n1", "f1", chain_path=path)
    with open(path, "r", encoding="utf-8") as fh:
        first_bytes = fh.read()
    r2 = _chain.append_row("a2", "v2", "partial", ["r2"], "n2", "f2",
                           skill="s", chain_path=path)
    with open(path, "r", encoding="utf-8") as fh:
        after = fh.read()

    assert after.startswith(first_bytes), "row 1 bytes were rewritten"
    rows = _chain.read_rows(path)
    assert len(rows) == 2
    assert rows[0] == json.loads(first_bytes.strip())
    assert r1["row_id"] == 1 and r2["row_id"] == 2
    assert rows[1]["row_id"] > rows[0]["row_id"]
    for row in rows:
        assert row["clock_source"] == "host_read"
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", row["ts_utc"])
        assert set(("row_id", "ts_utc", "clock_source", "actor", "action", "skill",
                    "verifier_result", "claim_status", "remaining_risk",
                    "next_safe_action", "honest_flaw")).issubset(row)


def test_chain_rejects_bad_claim_status(tmp_path):
    path = os.path.join(str(tmp_path), "c.jsonl")
    with pytest.raises(ValueError):
        _chain.append_row("a", "v", "green", [], "n", "f", chain_path=path)


# ---------------------------------------------------------------- relay

def test_poll_and_relay_survives_malformed_sources(tmp_path):
    import poll_and_relay as par

    good = os.path.join(str(tmp_path), "good.json")
    with open(good, "w", encoding="utf-8") as fh:
        json.dump({"exit_code": 0, "claim_status": "wired_with_receipts",
                   "honest_flaw": "only the exit code is evidence"}, fh)
    bad = os.path.join(str(tmp_path), "bad.json")
    with open(bad, "w", encoding="utf-8") as fh:
        fh.write("{not json at all")
    missing = os.path.join(str(tmp_path), "nope.json")
    out = os.path.join(str(tmp_path), "relay.md")

    rc = par.main(["--chain", os.path.join(str(tmp_path), "c.jsonl"),
                   "poll", "--sources", ",".join([good, bad, missing]), "--out", out])
    assert rc == 0
    text = open(out, encoding="utf-8").read()
    assert "## Unreadable sources" in text
    assert "nope.json" in text
    assert "wired_with_receipts" in text
    assert len(text.split()) <= par.WORD_BUDGET


def test_poll_and_relay_stays_under_budget_with_many_sources(tmp_path):
    import poll_and_relay as par

    paths = []
    for i in range(40):
        p = os.path.join(str(tmp_path), "r%02d.json" % i)
        with open(p, "w", encoding="utf-8") as fh:
            json.dump({"exit_code": i % 2, "claim_status": "partial"}, fh)
        paths.append(p)
    out = os.path.join(str(tmp_path), "big.md")
    rc = par.main(["--chain", os.path.join(str(tmp_path), "c.jsonl"),
                   "poll", "--sources", ",".join(paths), "--out", out])
    assert rc == 0
    words = len(open(out, encoding="utf-8").read().split())
    assert words <= par.WORD_BUDGET, words


# ---------------------------------------------------------------- subprocess smoke

def test_cli_runs_as_a_subprocess(tmp_path):
    write_skill(tmp_path, "good", REPRESENTATIVE_BLOCK)
    proc = subprocess.run(
        [sys.executable, os.path.join(FORGE, "tools", "olrun", "dispatch_class.py"),
         "--root", str(tmp_path), "validate"],
        capture_output=True, text=True, cwd=FORGE,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert json.loads(proc.stdout)[0]["valid"] is True
