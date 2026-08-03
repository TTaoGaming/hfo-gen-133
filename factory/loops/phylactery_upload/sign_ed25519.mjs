#!/usr/bin/env node
/*
 * sign_ed25519.mjs — ed25519 keygen / sign / verify / verify_all.
 *
 * All ops driven by JSON on stdin (--stdin-json). Prints one JSON blob on
 * stdout, exits 0 on success (even for verify_all with mismatches — the
 * result carries per-file booleans; nonzero exit is reserved for infra
 * failure, not signature mismatch).
 *
 * Ops:
 *   { "op": "keygen", "out_path": "<path>" }
 *   { "op": "sign_batch", "tasks": [{"path": "<file>", "key_path": "<key.json>", "relpath": "<rel>"}, ...] }
 *   { "op": "verify_batch", "tasks": [{"path": "<file>", "sig_path": "<file.sig>", "pubkey_hex": "<hex>"}, ...] }
 *   { "op": "verify_all", "root": "<tree_root>", "keys_root": "<keys_root>" }
 *
 * Deps: @noble/ed25519 (only). Package.json alongside.
 */

import { readFile, writeFile, readdir, stat } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { createHash, randomBytes } from "node:crypto";
import * as ed from "@noble/ed25519";

// @noble/ed25519 needs sha512 wired
import { sha512 } from "@noble/hashes/sha512";
ed.etc.sha512Sync = (...m) => sha512(ed.etc.concatBytes(...m));

// ---------------------------------------------------------------------------
// stdin JSON
// ---------------------------------------------------------------------------
async function readStdin() {
  const chunks = [];
  for await (const c of process.stdin) chunks.push(c);
  return Buffer.concat(chunks).toString("utf8");
}

function toHex(u8) { return Buffer.from(u8).toString("hex"); }
function fromHex(h) { return new Uint8Array(Buffer.from(h.trim(), "hex")); }
function toB64(u8) { return Buffer.from(u8).toString("base64"); }

// ---------------------------------------------------------------------------
// key file format:
//   { "curve": "ed25519", "priv_hex": "...", "pub_hex": "...", "created_utc": "..." }
// ---------------------------------------------------------------------------
async function keygen(outPath) {
  const priv = ed.utils.randomPrivateKey();
  const pub = await ed.getPublicKeyAsync(priv);
  const obj = {
    curve: "ed25519",
    priv_hex: toHex(priv),
    pub_hex: toHex(pub),
    pub_b64: toB64(pub),
    created_utc: new Date().toISOString().replace(/\.\d+Z$/, "Z"),
  };
  await writeFile(outPath, JSON.stringify(obj, null, 2) + "\n", "utf8");
  return { ok: true, out_path: outPath, pubkey_hex: obj.pub_hex, pubkey_b64: obj.pub_b64 };
}

async function loadKey(keyPath) {
  const raw = await readFile(keyPath, "utf8");
  const j = JSON.parse(raw);
  if (j.curve !== "ed25519") throw new Error(`key ${keyPath} is not ed25519 (curve=${j.curve})`);
  return { priv: fromHex(j.priv_hex), pub: fromHex(j.pub_hex) };
}

async function signFile(filePath, keyPath) {
  const bytes = await readFile(filePath);
  const { priv, pub } = await loadKey(keyPath);
  const sig = await ed.signAsync(bytes, priv);
  return { sig_hex: toHex(sig), pubkey_hex: toHex(pub), size: bytes.length };
}

async function verifyFile(filePath, sigHex, pubHex) {
  const bytes = await readFile(filePath);
  const sig = fromHex(sigHex);
  const pub = fromHex(pubHex);
  return await ed.verifyAsync(sig, bytes, pub);
}

// ---------------------------------------------------------------------------
// verify_all — walk tree, for each <path>.sig verify against the pubkey of
// the owning lineage (or master fallback recorded in the sig sidecar).
// This function only handles the case where <path>.sig has a companion
// <path>.sig.meta.json listing the pubkey used. In the simplest deployment
// the runner writes only <path>.sig; verify_all then also loads the master
// pubkey and tries it.
// ---------------------------------------------------------------------------
async function walkFiles(root) {
  const out = [];
  async function inner(d) {
    for (const e of await readdir(d, { withFileTypes: true })) {
      if (e.name === ".git" || e.name === "node_modules") continue;
      const p = path.join(d, e.name);
      if (e.isDirectory()) await inner(p);
      else out.push(p);
    }
  }
  await inner(root);
  return out;
}

async function verifyAll(root, keysRoot) {
  // Load candidate pubkeys
  const candidates = {};
  const master = path.join(keysRoot, "hfo_gen133_master_ed25519.json");
  if (existsSync(master)) {
    const k = await loadKey(master);
    candidates["master"] = toHex(k.pub);
  }
  // apex + valkyries
  for (const cat of ["apex", "valkyries"]) {
    const dir = path.join(keysRoot, cat);
    if (!existsSync(dir)) continue;
    for (const e of await readdir(dir, { withFileTypes: true })) {
      if (!e.isFile() || !e.name.endsWith("_ed25519.json")) continue;
      const callsign = e.name.replace(/_ed25519\.json$/, "");
      try {
        const k = await loadKey(path.join(dir, e.name));
        candidates[`${cat}/${callsign}`] = toHex(k.pub);
      } catch { /* ignore */ }
    }
  }

  const results = [];
  const files = await walkFiles(root);
  const sigs = files.filter(f => f.endsWith(".sig"));
  for (const sigPath of sigs) {
    const filePath = sigPath.slice(0, -4);
    if (!existsSync(filePath)) {
      results.push({ sig: sigPath, ok: false, reason: "no companion file" });
      continue;
    }
    const rel = path.relative(root, filePath).split(path.sep).join("/");
    // decide expected signer id
    let expected = "master";
    const parts = rel.split("/");
    if (parts[0] === "apex" && parts.length >= 3) expected = `apex/${parts[1]}`;
    if (parts[0] === "valkyries" && parts.length >= 3) expected = `valkyries/${parts[1]}`;

    const sigHex = (await readFile(sigPath, "utf8")).trim();
    const tryPubs = [];
    if (candidates[expected]) tryPubs.push({ id: expected, pub: candidates[expected] });
    if (expected !== "master" && candidates["master"]) tryPubs.push({ id: "master", pub: candidates["master"] });

    let matched = null;
    let reason = "no pubkey to try";
    for (const { id, pub } of tryPubs) {
      try {
        const ok = await verifyFile(filePath, sigHex, pub);
        if (ok) { matched = id; break; }
        reason = "sig mismatch";
      } catch (e) { reason = String(e.message || e); }
    }
    results.push({ file: rel, sig: rel + ".sig", ok: !!matched, signer: matched, reason: matched ? "ok" : reason });
  }
  const allOk = results.every(r => r.ok);
  return { all_ok: allOk, checked: results.length, results };
}

// ---------------------------------------------------------------------------
// main
// ---------------------------------------------------------------------------
async function main() {
  const args = process.argv.slice(2);
  if (!args.includes("--stdin-json")) {
    process.stderr.write("usage: node sign_ed25519.mjs --stdin-json  (JSON on stdin)\n");
    process.exit(64);
  }
  const raw = await readStdin();
  const req = JSON.parse(raw);
  let resp;
  try {
    if (req.op === "keygen") {
      resp = await keygen(req.out_path);
    } else if (req.op === "sign_batch") {
      const results = [];
      for (const t of req.tasks) {
        try {
          const r = await signFile(t.path, t.key_path);
          results.push({ relpath: t.relpath, sig_hex: r.sig_hex, pubkey_hex: r.pubkey_hex, size: r.size });
        } catch (e) {
          results.push({ relpath: t.relpath, sig_hex: null, error: String(e.message || e) });
        }
      }
      resp = { op: "sign_batch", results };
    } else if (req.op === "verify_batch") {
      const results = [];
      for (const t of req.tasks) {
        try {
          const sigHex = t.sig_hex || (await readFile(t.sig_path, "utf8")).trim();
          const ok = await verifyFile(t.path, sigHex, t.pubkey_hex);
          results.push({ path: t.path, ok });
        } catch (e) {
          results.push({ path: t.path, ok: false, error: String(e.message || e) });
        }
      }
      resp = { op: "verify_batch", results };
    } else if (req.op === "verify_all") {
      resp = await verifyAll(req.root, req.keys_root);
    } else {
      throw new Error(`unknown op: ${req.op}`);
    }
  } catch (e) {
    process.stderr.write(`sign_ed25519 error: ${e.message || e}\n`);
    process.exit(1);
  }
  process.stdout.write(JSON.stringify(resp) + "\n");
}

main();
