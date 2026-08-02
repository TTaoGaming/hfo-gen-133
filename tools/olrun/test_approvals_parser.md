# approvals_parser.py — verification vectors

Handwritten test vectors so the SAFE-PUBLISH loop can be validated
end-to-end without a full test harness. Each vector is a (gate_file
contents, expected resolved list) pair with a fixed `--now`.

Bash was unavailable at write time, so these vectors were computed
by inspection of `resolve()`. Run once when bash returns:

    python3 tools/olrun/approvals_parser.py \
        --gate <(printf '%s\n' "$VECTOR_GATE") \
        --index outputs/staged_sends/OPERATOR_APPROVAL_INDEX_20260803.md \
        --now 2026-08-04T12:00:00Z

The stderr summary line MUST match the # resolved= count below.

---

## V1 — empty gate

Gate:
```
# nothing approved
```
Expected: `# resolved=0 gate_lines=0 index_rows=150 now=...`
Rationale: no non-comment lines. D1 halts safely.

## V2 — single instance

Gate:
```
contracts:001
```
Expected: 1 row for contracts seq 001 (DrSwarm). source_line=`contracts:001`, class_name=null.

## V3 — instance for expired grants row

Gate:
```
grants:007
```
`--now 2026-08-04T12:00:00Z`
Expected: `# resolved=0`. Row 007 expires 2026-08-02T23:59:59Z, so `_parse_utc(row.expires_utc) <= now` filters it out. This is the safety property: no expired publishes.

## V4 — class contracts_hn quota=40, seq_range=001-149

Gate:
```
class:contracts_hn:quota=40:seq_range=001-149:expires=2026-08-08T23:00:00Z
```
`--now 2026-08-04T12:00:00Z`
Expected: 40 contracts rows (seq 001, 005, 009, 013, 017, 021, 025, 029, 033, 037, 041, 045, 049, 053, 057, 061, 065, 069, 073, 077, 081, 085, 089, 093, 097, 101, 105, 109, 113, 117, 121, 124, 127, 130, 133, 136, 139, 142, 145, 148). source_line=class..., class_name=contracts_hn. All within seq_range and expires 2026-08-09.

## V5 — class + explicit reject

Gate:
```
class:contracts_hn:quota=40:seq_range=001-149:expires=2026-08-08T23:00:00Z
!contracts:061
```
Expected: 39 contracts rows (seq 061 = "secret" REJECTED_NO_SIGNAL is skipped).

## V6 — class expired

Gate:
```
class:contracts_hn:quota=40:seq_range=001-149:expires=2026-08-01T12:00:00Z
```
`--now 2026-08-04T12:00:00Z`
Expected: `# resolved=0`. Class window closed.

## V7 — quota under-set

Gate:
```
class:contracts_hn:quota=5:seq_range=001-149:expires=2026-08-08T23:00:00Z
```
Expected: 5 contracts rows (the first 5 in index scan order: seq 001, 005, 009, 013, 017). Quota stops the class scan early.

## V8 — instance + class quota interaction

Gate:
```
contracts:081
class:contracts_hn:quota=5:seq_range=001-149:expires=2026-08-08T23:00:00Z
```
Expected: 5 rows total. Instance 081 published first with class_name=null.
The class-line loop initializes `class_used["contracts_hn"] = 1` (the
already-published 081 counts), then adds seq 001, 005, 009, 013 —
total 5, halting before seq 017.

## V9 — class name not in CLASS_TO_MARKET

Gate:
```
class:unmapped_class:quota=10:seq_range=001-999:expires=2026-08-08T23:00:00Z
```
Expected: `# resolved=0`. `CLASS_TO_MARKET.get(g.class_name)` returns
None, class silently skipped. Extend the map before use.

---

## Contract with Codex LOOP D1 SAFE-PUBLISH-BATCH

D1's publish loop should be:

```python
from tools.olrun.approvals_parser import parse_gate_file, load_index, resolve

gate = parse_gate_file(Path("state/experiments/approvals/latest.txt"))
index = load_index(Path("outputs/staged_sends/OPERATOR_APPROVAL_INDEX_20260803.md"))
resolved = resolve(gate, index, dt.datetime.now(tz=dt.timezone.utc))

for row in resolved:
    receipt = publish_by_market(row["market"], row["package_path"])
    write_publication(receipt)                    # -> state/experiments/publications.jsonl
    if receipt["http_status"] >= 400:
        halt("4xx/5xx halt gate", row)            # stop-gate per approvals_parser docstring
```

Compatibility with the pre-2026-08-03 D1 (instance-only): resolve()
returns the same list if given only instance lines, so operator can
switch back by removing class lines. No breaking change.
