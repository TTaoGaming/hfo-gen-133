# Gen133 preupload command — staged, not authorized

Current effect ceiling: `NO_UPLOAD_NO_DEPLOY_NO_SPEND_NO_CREDENTIALS`.

The exact candidate to review is:

```text
permaweb/staging/GEN133_PREUPLOAD_CANDIDATE.json
```

After a distinct public-safety review and operator-typed authorization, choose
one supported signed upload route and record its provider receipt. Do not paste
a wallet or private key into this repository, shell history, Slack, or an
agent prompt.

Illustrative operator-side flow only:

```text
1. Recompute exact byte count and SHA-256.
2. Confirm the candidate is below the chosen service's current free threshold.
3. Upload the exact file with the operator's external signing route.
4. Preserve provider receipt and immutable transaction ID.
5. Fetch the transaction through two independently operated gateways.
6. Compare exact bytes and SHA-256.
7. Commit the readback receipt to Git; obtain ConsumerAck.
8. Optionally update an ArNS pointer only after the immutable receipt is green.
```

There is intentionally no executable command here. This machine has no
verified upload client, signing route, wallet authority, ArNS registration, or
operator authorization receipt.
