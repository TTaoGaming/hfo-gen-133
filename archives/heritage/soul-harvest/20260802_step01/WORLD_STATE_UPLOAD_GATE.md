# World-state upload gate — Step 1/N

## Verdict

**Do not upload the current `CURRENT.md` as tonight's world state.** It is the canonical projection,
but its `valid_time` is `2026-07-30T04:57:52Z`, while the observed Gen-133 branch head before this
batch was `eb42cb72418d49eec7883478c66946c40523e43d` on `2026-08-02`.

The world-state payload must be regenerated from current receipts. An old canonical projection is
still stale; permanence would turn a repairable projection defect into an immutable historical error.

## Required input set

1. `CURRENT.md` as the standing-decision base, blob `13a7c92ba2093711366cca59fe6a17d6b120fc85`.
2. Current Gen-133 branch head and all material receipts after `2026-07-30T04:57:52Z`.
3. Current Scheduled Tasks inventory and active seat map.
4. Current spatial-factory, operator-relief, connector, and identity states.
5. Explicit list of closed loops versus partial artifacts.
6. Exact unresolved contradictions and expiries.
7. Distinct-provider verification and named ConsumerAck.

## Release conditions

- one file; no competing world-state root;
- absolute UTC valid time and Git transaction pointer;
- every nontrivial claim has an exact receipt;
- verified and unverified claims separated;
- no receipt count or wake count substituted for outcomes;
- no protected/private details in the public payload;
- raw SHA-256 and canonical digest reproduced by the local node;
- external verifier returns `STOOD`;
- operator gives fresh explicit Arweave upload authority.

## Stop condition

Any stale projection, unbound claim, missing verifier, private-data leak, or payload/hash mismatch is
`HOLD`. The correct output is no upload, not a best-effort permanent object.
