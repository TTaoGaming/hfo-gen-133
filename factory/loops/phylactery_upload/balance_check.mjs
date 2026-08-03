#!/usr/bin/env node
/*
 * balance_check.mjs — report Turbo credit balance + on-chain AR balance for a wallet.
 *
 * Usage:
 *   node balance_check.mjs --wallet <path>
 *   node balance_check.mjs --wallet <path> --json
 */

import { readFile } from "node:fs/promises";
import { TurboFactory, ArweaveSigner } from "@ardrive/turbo-sdk";
import Arweave from "arweave";

function argv(name) {
  const i = process.argv.indexOf(name);
  return i >= 0 ? process.argv[i + 1] : null;
}
function hasFlag(name) { return process.argv.includes(name); }

async function main() {
  const walletPath = argv("--wallet");
  const asJson = hasFlag("--json");
  if (!walletPath) {
    process.stderr.write("usage: node balance_check.mjs --wallet <path> [--json]\n");
    process.exit(2);
  }

  const jwk = JSON.parse(await readFile(walletPath, "utf8"));
  const signer = new ArweaveSigner(jwk);
  const turbo = TurboFactory.authenticated({ signer });

  let balanceCredits = null;
  let balanceError = null;
  try {
    const b = await turbo.getBalance();
    balanceCredits = b;
  } catch (e) {
    balanceError = String(e.message || e);
  }

  const arweave = Arweave.init({ host: "arweave.net", port: 443, protocol: "https" });
  const address = await arweave.wallets.jwkToAddress(jwk);
  let arBalance = null;
  let arError = null;
  try {
    const winston = await arweave.wallets.getBalance(address);
    arBalance = Number(arweave.ar.winstonToAr(winston));
  } catch (e) {
    arError = String(e.message || e);
  }

  const out = {
    address,
    balance_credits: balanceCredits,
    balance_credits_error: balanceError,
    balance_ar: arBalance,
    balance_ar_error: arError,
    checked_utc: new Date().toISOString().replace(/\.\d+Z$/, "Z"),
  };
  if (asJson) console.log(JSON.stringify(out));
  else console.log(JSON.stringify(out, null, 2));
  process.exit(0);
}

main().catch(e => {
  process.stderr.write(`balance_check fatal: ${e && e.stack ? e.stack : e}\n`);
  process.exit(1);
});
