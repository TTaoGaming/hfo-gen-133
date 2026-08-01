#!/usr/bin/env python3
"""
test_proposal_envelope.py -- red-first held-out tests for render_proposal.py.

Each test builds a fully isolated fixture set in a temp directory (its own
template, job.json, and allowlist.json) so nothing here reads or mutates
the real proposal_template.md, allowlist.json, or job_filter.json in this
project directory. No network access.

The claim under test: every refusal path named in the task brief actually
fires at least once, on a real subprocess invocation, with the documented
exit code -- plus the happy path actually succeeds and --dry-run actually
withholds the body. A suite where no refusal ever fires would be a fake
green -- it would prove nothing about whether the envelope constrains
anything.
"""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone

HERE = pathlib.Path(__file__).resolve().parent
RENDER = HERE / "render_proposal.py"

ALLOWLIST = [
    "client_first_name",
    "job_title",
    "job_specific_pain",
    "relevant_portfolio_item",
    "proposed_first_deliverable",
    "timeline_days",
]


def now_minus_days(days):
    return (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")


class ProposalEnvelopeTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name)

        self.allowlist_path = self.dir / "allowlist.json"
        self.allowlist_path.write_text(json.dumps(ALLOWLIST), encoding="utf-8")

        self.template_path = self.dir / "template.md"
        self.template_text = (
            "{{client_first_name}} -- on the {{job_title}} post: "
            "{{job_specific_pain}}.\n\n"
            "Relevant: {{relevant_portfolio_item}}.\n\n"
            "First deliverable: {{proposed_first_deliverable}}, in "
            "{{timeline_days}} days.\n"
        )
        self.template_path.write_text(self.template_text, encoding="utf-8")

        self.job_path = self.dir / "job.json"
        self.good_job = {
            "job_url": "https://www.upwork.com/jobs/~test000000000001",
            "job_title": "AI agent reliability contractor",
            "posted_utc": now_minus_days(2),
            "client_first_name": "Priya",
            "job_specific_pain": "our agents mark tickets resolved without a passing test run",
            "relevant_portfolio_item": "the append-only verdict chain that catches unsealed-claim fake-greens",
            "proposed_first_deliverable": "a write-seam gate that blocks a done status without a verifier_result",
            "timeline_days": 5,
        }
        self._write_job(self.good_job)

    def tearDown(self):
        self.tmp.cleanup()

    def _write_job(self, job):
        self.job_path.write_text(json.dumps(job), encoding="utf-8")

    def _write_template(self, text):
        self.template_path.write_text(text, encoding="utf-8")

    def run_render(self, extra_args=None, template_path=None, job_path=None, allowlist_path=None):
        cmd = [
            sys.executable, str(RENDER),
            "--template", str(template_path or self.template_path),
            "--job", str(job_path or self.job_path),
            "--allowlist-file", str(allowlist_path or self.allowlist_path),
        ]
        if extra_args:
            cmd += extra_args
        return subprocess.run(cmd, capture_output=True, text=True, cwd=str(HERE))


class TestHappyPath(ProposalEnvelopeTestCase):
    def test_exit0_valid_render_succeeds(self):
        result = self.run_render()
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Priya", result.stdout)
        self.assertIn("5 days", result.stdout)


class TestDryRun(ProposalEnvelopeTestCase):
    def test_dry_run_prints_variables_and_withholds_body(self):
        result = self.run_render(extra_args=["--dry-run"])
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        resolved = json.loads(result.stdout)
        self.assertEqual(resolved["client_first_name"], "Priya")
        self.assertEqual(resolved["timeline_days"], 5)
        self.assertNotIn("First deliverable:", result.stdout)


class TestExit2VariableNotAllowlisted(ProposalEnvelopeTestCase):
    def test_exit2_fires_for_disallowed_variable(self):
        bad_template = self.template_text.replace(
            "{{relevant_portfolio_item}}", "{{relevant_portfolio_item}} ({{secret_internal_field}})"
        )
        self._write_template(bad_template)

        result = self.run_render()
        self.assertEqual(result.returncode, 2, msg=result.stderr)
        self.assertIn("secret_internal_field", result.stderr)


class TestExit3MissingRequiredValue(ProposalEnvelopeTestCase):
    def test_exit3_fires_when_allowlisted_var_is_null_on_job(self):
        job = dict(self.good_job)
        job["timeline_days"] = None
        self._write_job(job)

        result = self.run_render()
        self.assertEqual(result.returncode, 3, msg=result.stderr)
        self.assertIn("timeline_days", result.stderr)

    def test_exit3_fires_when_allowlisted_var_is_absent_entirely(self):
        job = dict(self.good_job)
        job.pop("proposed_first_deliverable", None)
        self._write_job(job)

        result = self.run_render()
        self.assertEqual(result.returncode, 3, msg=result.stderr)
        self.assertIn("proposed_first_deliverable", result.stderr)


class TestExit4WordCap(ProposalEnvelopeTestCase):
    def test_exit4_fires_when_rendered_body_exceeds_200_words(self):
        filler = " ".join(["word"] * 210)
        long_template = "{{client_first_name}} " + filler + " {{timeline_days}}\n"
        self._write_template(long_template)

        result = self.run_render()
        self.assertEqual(result.returncode, 4, msg=result.stderr)
        self.assertIn("word cap", result.stderr)

    def test_dry_run_ignores_word_cap(self):
        filler = " ".join(["word"] * 210)
        long_template = "{{client_first_name}} " + filler + " {{timeline_days}}\n"
        self._write_template(long_template)

        result = self.run_render(extra_args=["--dry-run"])
        self.assertEqual(result.returncode, 0, msg=result.stderr)


class TestExit5MissingRequiredJobField(ProposalEnvelopeTestCase):
    def test_exit5_fires_when_job_url_missing(self):
        job = dict(self.good_job)
        job.pop("job_url", None)
        self._write_job(job)

        result = self.run_render()
        self.assertEqual(result.returncode, 5, msg=result.stderr)
        self.assertIn("job_url", result.stderr)

    def test_exit5_fires_when_posted_utc_missing(self):
        job = dict(self.good_job)
        job.pop("posted_utc", None)
        self._write_job(job)

        result = self.run_render()
        self.assertEqual(result.returncode, 5, msg=result.stderr)
        self.assertIn("posted_utc", result.stderr)

    def test_exit5_fires_when_posted_utc_not_z_suffixed(self):
        job = dict(self.good_job)
        job["posted_utc"] = "2026-07-29 12:00:00"
        self._write_job(job)

        result = self.run_render()
        self.assertEqual(result.returncode, 5, msg=result.stderr)


class TestExit6StaleJob(ProposalEnvelopeTestCase):
    def test_exit6_fires_when_job_older_than_max_age_days(self):
        job = dict(self.good_job)
        job["posted_utc"] = now_minus_days(30)
        self._write_job(job)

        result = self.run_render()
        self.assertEqual(result.returncode, 6, msg=result.stderr)
        self.assertIn("days old", result.stderr)

    def test_exit6_respects_custom_max_age_days(self):
        job = dict(self.good_job)
        job["posted_utc"] = now_minus_days(2)
        self._write_job(job)

        result = self.run_render(extra_args=["--max-age-days", "1"])
        self.assertEqual(result.returncode, 6, msg=result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
