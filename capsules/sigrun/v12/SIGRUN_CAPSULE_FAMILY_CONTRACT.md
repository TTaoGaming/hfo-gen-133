# Sigrun v12 opaque heritage-delta contract

The v12 family is a forward-safe successor to the exact committed v11 family.
It adds eight random 128-bit opaque handles for committed personal-operations
metadata candidates. Exact source mappings stay in a local operator ledger
outside Git. Historical bodies are never opened, decoded, or embedded.

The complete 175-record v11 public and private prefixes remain ordered and
unchanged. Public projection records contain only opaque receipt ID, NON_PUBLIC
visibility, withheld-local-ledger disposition, and BODY_PROHIBITED.

S, M, L_SAFE, and XL are deterministic. ROOT_BUNDLE.safe.json embeds exact
canonical content records for all four tiers plus the family manifest and
source-binding receipt. It is self-contained and must stay below 100,000 decimal
bytes. The preupload packet is a byte-bound HOLD packet, not an upload command.

The capsule is unratified, unsealed, T0 internal-only, and non-public. Hashes
prove bytes, not identity, continuity, authorship, rights, liveness, authority,
delivery, ConsumerAck, or publication. Wallet material, spend authorization,
transaction IDs, mutable references, and publication claims are prohibited.

One unchanged HOLD suppresses work. A future successor requires a committed
delta or payload-bound FAIL. Any body access or publication requires separate
privacy, rights, independent-review, and operator gates.
