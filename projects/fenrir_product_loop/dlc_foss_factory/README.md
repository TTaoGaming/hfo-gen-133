# DLC-style FOSS extension factory scaffold

This directory contains one reusable, target-agnostic factory scaffold. It is
bound to controller head
`61314978a4dd1b53eeef3086e6d145b3552bf75a` and frozen contract blob
`44ad12f2b01337ed3f872751252e836f3a0dbf7d`. Its route remains
`SCAFFOLD_ONLY_TARGET_UNADMITTED`.

The scaffold does not select, clone, fork, reskin, or build a real FOSS target.
The included reference unit is explicitly `NON_PRODUCTION`; all landing and
distribution outputs are inert. PR #9 is a draft controller, not independent
review, target admission, or readiness evidence.

## Included interfaces

- `unit_spec.schema.json`: JSON Schema 2020-12 unit contract.
- `receipt.schema.json`: maker-local lifecycle receipt contract.
- `examples/NON_PRODUCTION_unit_spec.valid.json`: synthetic valid reference
  unit, unmistakably labelled `NON_PRODUCTION`.
- `examples/unit_spec.invalid.json`: intentionally invalid input example.
- `dlc_factory/spec.py`: strict semantic validation, including duplicate-key,
  incomplete-spec, traversal, and credential-like input rejection.
- `dlc_factory/provenance.py`: target-independent license/provenance byte
  preflight that makes no compatibility opinion on an unbound target.
- `dlc_factory/materializer.py`: deterministic, atomic materialization of fixed
  inert outputs.
- `dlc_factory/adapters.py`: local install, build, test, health, and rollback
  interfaces for the code-owned synthetic adapter.
- `dlc_factory/lease.py`: atomic checkout-local WIP=1 lease.
- `dlc_factory/receipt.py`: canonical content-addressed receipt creation and
  semantic verification.
- `dlc_factory/cli.py`: dependency-light command-line interface.
- `templates/`: fixed inert landing, distribution, README, and adapter outputs.
- `tests/test_factory.py`: maker-readable `LOCAL_REGRESSION` coverage.

No third-party package installation, network request, deployment, publication,
payment, outreach, credentials, customer data, or real target is needed.

## Local usage

Run from this directory:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest discover -s tests -p 'test_*.py' -v
python -m dlc_factory validate --spec examples/NON_PRODUCTION_unit_spec.valid.json
python -m dlc_factory preflight --spec examples/NON_PRODUCTION_unit_spec.valid.json
python -m dlc_factory run --spec examples/NON_PRODUCTION_unit_spec.valid.json
```

The unbound preflight intentionally exits `5` with
`UNKNOWN_UNBOUND_TARGET` and `license_compatibility_opinion: NONE`. That is the
truthful result, not a failed scaffold.

The mutating CLI exposes no run-root or output-root override. It always uses the
single checkout-local `runs/` root so callers cannot bypass WIP=1 by choosing a
different root. The Python API accepts an injected root only for isolated unit
tests.

## License and provenance boundary

The preflight interface is structural and byte-oriented:

- an unbound target returns `UNKNOWN_UNBOUND_TARGET`;
- a bound packet without supplied local license bytes stays on hold;
- supplied bytes are compared with the declared Git blob SHA-1 and SHA-256;
- a mismatch or `NOASSERTION` stays on hold;
- matching bytes become `BOUND_EVIDENCE_REQUIRES_DISTINCT_REVIEW`.

None of these states is a legal opinion, license-compatibility decision, target
admission, or authorization to build a target. `--license-file` reads only a
local file; preflight performs no network access.

## Deterministic inert outputs

The materializer renders exactly four files:

- `landing/index.html`, marked `noindex,nofollow` with no active form;
- `distribution/manifest.json`, with publishing and deployment disabled;
- `distribution/README.md`, explicitly labelled `NON_PRODUCTION`;
- `adapters/adapter_stub.py`, byte-equal to the code-owned adapter template.

Paths are allowlisted, traversal and reparse points fail closed, and output is
staged before atomic promotion. An existing output tree must match every
expected path and byte. Identical materialization is a no-op; differing output
is a collision and is never overwritten.

## Local lifecycle and rollback

The only executable adapter is `builtin.non_production`. It runs install,
build, test, and health locally with `shell=False`, a reduced environment, and
isolated Python (`-I -S`). A failed stage triggers exactly one rollback attempt.
The original failure and rollback exit are both retained; successful rollback
never turns the lifecycle green.

Every lifecycle receipt binds:

- the exact controller and frozen contract authority;
- canonical unit-spec and artifact-tree hashes;
- raw argument arrays, exit codes, stdout/stderr, and their hashes;
- a hash-linked, duplicate-resistant event sequence;
- remaining risk, honest flaw, and the verifier handoff;
- `LOCAL_REGRESSION`, `independent_verification: false`, and
  `target_admitted: false`.

Canonical receipt bytes are stored at
`runs/sha256/<sha256>/receipt.json`. The current maker receipt is
`c5a9fc6cfaff100f9f432f35105a3d49bbcbca8d29c9b35e3ed6add67f724d9c`.
Exact local commands and raw exits are preserved separately at
`runs/evidence/sha256/<sha256>/evidence.json`; the current evidence address is
`593b0fcc0c3d3bc775211395f6ecb364e2118924ed3c7f870e998f34ce5e16a5`.

Verify the lifecycle receipt with:

```powershell
python -m dlc_factory verify-receipt --sha256 c5a9fc6cfaff100f9f432f35105a3d49bbcbca8d29c9b35e3ed6add67f724d9c
```

## Exit codes

| Exit | Meaning |
|---:|---|
| `0` | Validation, materialization, local lifecycle, or receipt verification succeeded |
| `2` | CLI or local I/O failure |
| `3` | Invalid spec, traversal, or credential-like input rejected |
| `4` | WIP lease collision |
| `5` | Provenance preflight is truthfully on hold or unknown |
| `6` | Lifecycle failed and rollback completed |
| `7` | Lifecycle failed and rollback also failed |
| `8` | Receipt integrity failure |
| `9` | Existing materialization conflicts with deterministic output |

## Claim and effect ceiling

Maker tests prove only `LOCAL_REGRESSION`. This scaffold does not establish
`DEMO_READY`, `PILOT_READY`, `PRODUCTION_READY`, market validation, revenue,
user acceptance, license compatibility, target admission, or independent
verification. It performs no deployment, billing, publishing, directory
submission, outreach, credential use, spend, Slack effect, merge, default-branch
write, or schedule mutation.

## Honest limitations and verifier handoff

The WIP lease is atomic only inside one checkout. It cannot discover a maker in
another worktree or machine, so each wake must still inspect Git refs, candidate
PRs, and committed leases. Pattern-based secret rejection is defense in depth,
not proof that arbitrary future data is clean. The fixture, executor, command
log, and tests are maker-owned self-report rather than independent attestation.

The next consumer is distinct held-out verifier task
`019fc468-bce5-7ae3-889f-63783416eef2`. It must replay the exact candidate SHA
and return PASS or REVISE without treating this README, the maker receipt, PR
#9, or draft PR #10 as independent evidence or target admission.
