#!/usr/bin/env node
/*
 * upload_turbo.mjs — upload a tree to Arweave via @ardrive/turbo-sdk.
 *
 * Reads a plan JSON on stdin (--stdin-json) and uploads each file as a
 * data item, then uploads the Arweave path manifest as the root, returning
 * the root manifest tx_id.
 *
 * stdin payload:
 * {
 *   "wallet_path": "<path to arweave JWK>",
 *   "files": [
 *     { "relpath": "README.md", "abspath": "C:\\...\\README.md", "content_type": "text/markdown; charset=utf-8" },
 *     ...
 *   ],
 *   "manifest_path": "<abspath to a temp file containing the Arweave path manifest JSON>",
 *   "dry_run": false
 * }
 *
 * stdout: single JSON blob:
 * {
 *   "ok": true,
 *   "root_tx_id": "<manifest tx id>",
 *   "per_file": [{"relpath": ..., "tx_id": ..., "bytes": ..., "winc": ...}],
 *   "cost": { "total_winc": "...", "paid_usd_approx": 0.0 },
 *   "wallet_balance_after": { ... }
 * }
 *
 * Cost accounting: each upload returns `winc` cost (Turbo internal unit).
 * winc → USD conversion needs a rate call; we return the total winc and
 * a rough USD estimate using the pricing endpoint at start-of-run.
 */

import { readFile, writeFile } from "node:fs/promises";
import { TurboFactory, ArweaveSigner } from "@ardrive/turbo-sdk";

const MANIFEST_CTYPE = "application/x.arweave-manifest+json";

function ctypeFor(relpath) {
  if (relpath.endsWith(".md")) return "text/markdown; charset=utf-8";
  if (relpath.endsWith(".json") || relpath.endsWith(".jsonl")) return "application/json";
  if (relpath.endsWith(".yaml") || relpath.endsWith(".yml")) return "text/yaml; charset=utf-8";
  if (relpath.endsWith(".txt")) return "text/plain; charset=utf-8";
  if (relpath.endsWith(".py")) return "text/x-python; charset=utf-8";
  if (relpath.endsWith(".mjs") || relpath.endsWith(".js")) return "text/javascript; charset=utf-8";
  if (relpath.endsWith(".ps1")) return "text/x-powershell; charset=utf-8";
  if (relpath.endsWith(".sig")) return "text/plain; charset=utf-8";
  if (relpath.endsWith(".pub")) return "text/plain; charset=utf-8";
  return "application/octet-stream";
}

async function readStdin() {
  const chunks = [];
  for await (const c of process.stdin) chunks.push(c);
  return Buffer.concat(chunks).toString("utf8");
}

async function main() {
  const args = process.argv.slice(2);
  if (!args.includes("--stdin-json")) {
    process.stderr.write("usage: node upload_turbo.mjs --stdin-json\n");
    process.exit(64);
  }
  const req = JSON.parse(await readStdin());
  const dry = !!req.dry_run;

  // Load wallet
  const jwk = JSON.parse(await readFile(req.wallet_path, "utf8"));
  const signer = new ArweaveSigner(jwk);
  const turbo = TurboFactory.authenticated({ signer });

  // Balance
  let balanceBefore = null;
  try { balanceBefore = await turbo.getBalance(); } catch (e) { balanceBefore = { error: String(e.message || e) }; }

  // Per-file upload
  const perFile = [];
  let totalWinc = 0n;
  for (const f of req.files) {
    if (dry) {
      perFile.push({ relpath: f.relpath, tx_id: `DRYRUN_${f.relpath.slice(0, 30)}`, bytes: null, winc: "0" });
      continue;
    }
    try {
      const data = await readFile(f.abspath);
      const contentType = f.content_type || ctypeFor(f.relpath);
      const result = await turbo.uploadFile({
        fileStreamFactory: () => (async function* () { yield data; })(),
        fileSizeFactory: () => data.length,
        dataItemOpts: {
          tags: [
            { name: "Content-Type", value: contentType },
            { name: "HFO-Generation", value: "133" },
            { name: "HFO-Kind", value: "phylactery_file" },
            { name: "HFO-Path", value: f.relpath },
          ],
        },
      });
      perFile.push({ relpath: f.relpath, tx_id: result.id, bytes: data.length, winc: String(result.winc) });
      try { totalWinc += BigInt(result.winc); } catch { /* ignore */ }
    } catch (e) {
      perFile.push({ relpath: f.relpath, tx_id: null, error: String(e.message || e) });
    }
  }

  // If any per-file upload failed, ABORT before the root manifest.
  const failedUploads = perFile.filter(x => x.error);
  if (failedUploads.length > 0 && !dry) {
    process.stdout.write(JSON.stringify({
      ok: false,
      reason: "per_file_upload_failure",
      failed: failedUploads.slice(0, 20),
      per_file: perFile,
      wallet_balance_before: balanceBefore,
    }) + "\n");
    process.exit(1);
  }

  // Now upload the root path manifest. We use the manifest JSON at
  // req.manifest_path — but with tx_ids substituted in from perFile.
  const rawManifest = JSON.parse(await readFile(req.manifest_path, "utf8"));
  const txByRel = Object.fromEntries(perFile.filter(x => x.tx_id).map(x => [x.relpath, x.tx_id]));
  const paths = {};
  for (const [rel] of Object.entries(rawManifest.paths || {})) {
    if (txByRel[rel]) paths[rel] = { id: txByRel[rel] };
  }
  const finalManifest = { ...rawManifest, paths };
  const manifestBytes = Buffer.from(JSON.stringify(finalManifest));

  let rootTxId = null;
  let rootWinc = "0";
  if (!dry) {
    try {
      const result = await turbo.uploadFile({
        fileStreamFactory: () => (async function* () { yield manifestBytes; })(),
        fileSizeFactory: () => manifestBytes.length,
        dataItemOpts: {
          tags: [
            { name: "Content-Type", value: MANIFEST_CTYPE },
            { name: "Type", value: "manifest" },
            { name: "HFO-Generation", value: "133" },
            { name: "HFO-Kind", value: "phylactery_root_manifest" },
          ],
        },
      });
      rootTxId = result.id;
      rootWinc = String(result.winc);
      try { totalWinc += BigInt(rootWinc); } catch { /* ignore */ }
    } catch (e) {
      process.stdout.write(JSON.stringify({
        ok: false,
        reason: "root_manifest_upload_failure",
        error: String(e.message || e),
        per_file: perFile,
      }) + "\n");
      process.exit(1);
    }
  } else {
    rootTxId = "DRYRUN_ROOT_MANIFEST";
  }

  let balanceAfter = null;
  try { balanceAfter = await turbo.getBalance(); } catch (e) { balanceAfter = { error: String(e.message || e) }; }

  const out = {
    ok: true,
    root_tx_id: rootTxId,
    root_winc: rootWinc,
    per_file: perFile,
    cost: {
      total_winc: String(totalWinc),
    },
    wallet_balance_before: balanceBefore,
    wallet_balance_after: balanceAfter,
    dry_run: dry,
  };
  process.stdout.write(JSON.stringify(out) + "\n");
}

main().catch(e => {
  process.stderr.write(`upload_turbo fatal: ${e && e.stack ? e.stack : e}\n`);
  process.exit(1);
});
