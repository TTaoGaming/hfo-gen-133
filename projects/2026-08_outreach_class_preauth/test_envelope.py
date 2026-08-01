#!/usr/bin/env python3
"""
test_envelope.py -- red-first held-out tests for render_message.py + kill_switch.py.

These tests build a fully isolated fixture set in a temp directory (its own
authorization, targets, kill switch, and template files) so nothing here
reads or mutates the real campaign_arg_c1.authorization.json, KILL_SWITCH.json,
or targets_arg_c1.jsonl in this project directory. No network access.

The claim under test: every refusal path actually fires at least once, and
the happy path actually succeeds. A suite where no refusal ever fires would
be a fake green -- it would prove nothing about whether the envelope
constrains anything.
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
RENDER = HERE / "render_message.py"
KILL_SWITCH = HERE / "kill_switch.py"

CAMPAIGN_ID = "TEST-C0"
OPT_OUT = "Reply STOP and you will not hear from me again."
ALLOWLIST = ["first_name", "company", "hook_quote"]


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class EnvelopeTestCase(unittest.TestCase):
    """Base: builds one throwaway campaign fixture per test in a tmp dir."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name)

        self.kill_switch_path = self.dir / "KILL_SWITCH.json"
        self.kill_switch_path.write_text(json.dumps({
            "campaign_id": CAMPAIGN_ID,
            "state": "ARMED",
            "reason": None,
            "set_by": None,
            "ts_utc": None,
        }), encoding="utf-8")

        self.template_path = self.dir / "template.txt"
        self.template_text = (
            "Hi {{first_name}} at {{company}},\n\n"
            "{{hook_quote}}\n\n"
            + OPT_OUT + "\n"
        )
        self.template_path.write_bytes(self.template_text.encode("utf-8"))
        self.template_sha = sha256_text(self.template_text)

        self.auth_path = self.dir / "auth.json"
        self.auth = {
            "campaign_id": CAMPAIGN_ID,
            "copy_template_sha256": self.template_sha,
            "variable_allowlist": list(ALLOWLIST),
            "opt_out_language": OPT_OUT,
            "kill_switch_path": str(self.kill_switch_path),
        }
        self._write_auth()

        self.targets_path = self.dir / "targets.jsonl"
        self.good_row = {
            "prospect_id": "p1",
            "first_name": "Ada",
            "last_name": "Lovelace",
            "title": "CTO",
            "company": "Analytical Engines Inc",
            "company_domain": "analyticalengines.example",
            "email": "ada.lovelace@example.invalid",
            "email_source": "enriched",
            "email_verification_status": "valid",
            "linkedin_url": None,
            "hook_quote": "the loom weaves algebraic patterns",
            "hook_source_url": "https://example.invalid/hook",
            "hook_date": "2026-01-01",
            "confidence": "HIGH",
            "suppression": False,
            "notes": "test fixture row",
        }
        self._write_targets([self.good_row])

    def tearDown(self):
        self.tmp.cleanup()

    def _write_auth(self):
        self.auth_path.write_text(json.dumps(self.auth), encoding="utf-8")

    def _write_targets(self, rows):
        with open(self.targets_path, "w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row) + "\n")

    def _write_template(self, text):
        self.template_path.write_bytes(text.encode("utf-8"))

    def run_render(self, target_id="p1", template_path=None):
        cmd = [
            sys.executable, str(RENDER),
            "--auth", str(self.auth_path),
            "--template", str(template_path or self.template_path),
            "--target", target_id,
            "--targets", str(self.targets_path),
        ]
        return subprocess.run(cmd, capture_output=True, text=True, cwd=str(HERE))


class TestHappyPath(EnvelopeTestCase):
    def test_exit0_valid_render_succeeds(self):
        result = self.run_render()
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Ada", result.stdout)
        self.assertIn(OPT_OUT, result.stdout)


class TestExit2VariableNotAllowlisted(EnvelopeTestCase):
    def test_exit2_fires_for_disallowed_variable(self):
        bad_template_text = self.template_text.replace(
            "{{hook_quote}}", "{{hook_quote}} from {{company_domain}}"
        )
        self._write_template(bad_template_text)
        self.auth["copy_template_sha256"] = sha256_text(bad_template_text)
        self._write_auth()

        result = self.run_render()
        self.assertEqual(result.returncode, 2, msg=result.stderr)
        self.assertIn("company_domain", result.stderr)


class TestExit3MissingRequiredValue(EnvelopeTestCase):
    def test_exit3_fires_when_allowlisted_var_is_null_on_target(self):
        row = dict(self.good_row)
        row["hook_quote"] = None
        self._write_targets([row])

        result = self.run_render()
        self.assertEqual(result.returncode, 3, msg=result.stderr)
        self.assertIn("hook_quote", result.stderr)


class TestExit4MissingOptOut(EnvelopeTestCase):
    def test_exit4_fires_when_optout_language_absent(self):
        bad_template_text = "Hi {{first_name}} at {{company}}, {{hook_quote}}\n"
        self._write_template(bad_template_text)
        self.auth["copy_template_sha256"] = sha256_text(bad_template_text)
        self._write_auth()

        result = self.run_render()
        self.assertEqual(result.returncode, 4, msg=result.stderr)


class TestExit5NotSendable(EnvelopeTestCase):
    def test_exit5_fires_for_suppressed_row(self):
        row = dict(self.good_row)
        row["suppression"] = True
        self._write_targets([row])

        result = self.run_render()
        self.assertEqual(result.returncode, 5, msg=result.stderr)

    def test_exit5_fires_for_null_email(self):
        row = dict(self.good_row)
        row["email"] = None
        self._write_targets([row])

        result = self.run_render()
        self.assertEqual(result.returncode, 5, msg=result.stderr)

    def test_exit5_fires_for_unverified_email(self):
        row = dict(self.good_row)
        row["email_verification_status"] = "unverified"
        self._write_targets([row])

        result = self.run_render()
        self.assertEqual(result.returncode, 5, msg=result.stderr)


class TestExit6TemplateHashMismatch(EnvelopeTestCase):
    def test_exit6_fires_when_template_bytes_differ_from_authorized_hash(self):
        # authorization still points at the ORIGINAL hash; mutate the template
        # file on disk after the authorization was written.
        self._write_template(self.template_text + "\nan unauthorized added line\n")

        result = self.run_render()
        self.assertEqual(result.returncode, 6, msg=result.stderr)


class TestExit7KillSwitchHalted(EnvelopeTestCase):
    def test_exit7_fires_when_kill_switch_is_halted(self):
        self.kill_switch_path.write_text(json.dumps({
            "campaign_id": CAMPAIGN_ID,
            "state": "HALTED",
            "reason": "test halt",
            "set_by": "test",
            "ts_utc": "2026-01-01T00:00:00Z",
        }), encoding="utf-8")

        result = self.run_render()
        self.assertEqual(result.returncode, 7, msg=result.stderr)


class TestKillSwitchCli(unittest.TestCase):
    """kill_switch.py itself: single-command halt/arm/status round trip."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = pathlib.Path(self.tmp.name) / "KS.json"
        self.path.write_text(json.dumps({
            "campaign_id": CAMPAIGN_ID,
            "state": "ARMED",
            "reason": None,
            "set_by": None,
            "ts_utc": None,
        }), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def _run(self, *args):
        cmd = [sys.executable, str(KILL_SWITCH), "--path", str(self.path)] + list(args)
        return subprocess.run(cmd, capture_output=True, text=True)

    def test_status_exit0_when_armed(self):
        result = self._run("status", CAMPAIGN_ID)
        self.assertEqual(result.returncode, 0, msg=result.stderr)

    def test_halt_then_status_exit1_then_arm_then_status_exit0(self):
        halt = self._run("halt", CAMPAIGN_ID, "--reason", "held-out test", "--by", "test_envelope.py")
        self.assertEqual(halt.returncode, 0, msg=halt.stderr)

        status_after_halt = self._run("status", CAMPAIGN_ID)
        self.assertEqual(status_after_halt.returncode, 1, msg=status_after_halt.stderr)
        state = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(state["state"], "HALTED")

        arm = self._run("arm", CAMPAIGN_ID)
        self.assertEqual(arm.returncode, 0, msg=arm.stderr)

        status_after_arm = self._run("status", CAMPAIGN_ID)
        self.assertEqual(status_after_arm.returncode, 0, msg=status_after_arm.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)