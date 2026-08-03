#!/usr/bin/env node
/*
 * keygen_wallet.mjs — generate a new Arweave JWK wallet OR verify an existing one.
 *
 * Default behavior: create keys/hfo_gen133_master.json unless it already exists.
 * Prints the wallet address (safe to share; needed to fund the wallet).
 *
 * Usage:
 *   node keygen_wallet.mjs                       # create at default path if missing
 *   node keygen_wallet.mjs --out <path>          # custom path
 *   node keygen_wallet.mjs --address-of <path>   # print address of existing JWK
 *   node keygen_wallet.mjs --force               # overwrite existing (danger)
 */

import { writeFile, readFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import Arweave from "arweave";

const DEFAULT_OUT = "areas/phylactery/arweave/keys/hfo_gen133_master.json";

function argv(name) {
  const i = process.argv.indexOf(name);
  return i >= 0 ? process.argv[i + 1] : null;
}
function hasFlag(name) { return process.argv.includes(name); }

async function addressOf(jwk) {
  const arweave = Arweave.init({});
  return await arweave.wallets.jwkToAddress(jwk);
}

async function main() {
  const outPath = argv("--out") || DEFAULT_OUT;
  const addrOnly = argv("--address-of");
  const force = hasFlag("--force");

  if (addrOnly) {
    const jwk = JSON.parse(await readFile(addrOnly, "utf8"));
    const addr = await addressOf(jwk);
    console.log(JSON.stringify({ wallet_path: addrOnly, address: addr }, null, 2));
    return;
  }

  if (existsSync(outPath) && !force) {
    const jwk = JSON.parse(await readFile(outPath, "utf8"));
    const addr = await addressOf(jwk);
    console.log(JSON.stringify({
      wallet_path: outPath,
      address: addr,
      note: "already exists; --force to overwrite (rotates the wallet — new address, new funding required)",
    }, null, 2));
    return;
  }

  const arweave = Arweave.init({});
  const jwk = await arweave.wallets.generate();
  await writeFile(outPath, JSON.stringify(jwk, null, 2) + "\n", "utf8");
  const addr = await addressOf(jwk);
  console.log(JSON.stringify({
    wallet_path: outPath,
    address: addr,
    note: "WROTE new wallet. Fund it at https://turbo.ardrive.net (search by address).",
  }, null, 2));
}

main().catch(e => {
  process.stderr.write(`keygen_wallet fatal: ${e && e.stack ? e.stack : e}\n`);
  process.exit(1);
});
