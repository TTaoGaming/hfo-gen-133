# Sigrun v10 opaque heritage-delta contract

The v10 family is a forward-safe successor to v9. It admits only random opaque
handles for 45 newly bounded committed candidates. Exact source metadata stays
in a local operator ledger outside Git; historical bodies are never opened or
embedded by the builder.

Public records contain exactly four fields: opaque receipt ID, visibility
class, disposition, and body-embedding policy. The handles are random 128-bit
values and are not derived from paths, hashes, or content.

The capsule remains unratified, unsealed, and T0 internal-only. Hashes establish
bytes, not authorship, identity, continuity, rights, liveness, or authority.
Correlated review carries zero independent quorum weight. The historical v6
protected-metadata exposure remains disclosed and is not erased by v9 or v10.
All retained personal-operations candidates remain QUARANTINE. Gen132 exact
authority was refreshed; the two legacy local refs retain UNKNOWN remote
currency.

Budgets:

- S: at most 4 KiB
- M: at most 8 KiB
- L_SAFE: at most 32 KiB
- XL index: less than 100,000 decimal bytes and explicitly not self-contained

One unchanged HOLD suppresses work. A future successor requires a committed
heritage delta or a payload-bound FAIL. Slack requires exact-thread readback;
Arweave upload and spend remain operator-only.
