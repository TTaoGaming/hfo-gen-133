#!/usr/bin/env node
// build.mjs — substitute placeholders and stage a dist/ tree for Cloudflare Pages.
//
// Placeholders read from .placeholder-config.json (created by copy-unit.mjs
// or hand-written per unit). Template files under src/ and public/ are read
// as UTF-8 and every {{TOKEN}} literal is replaced with config[TOKEN].
//
// Usage:
//   node scripts/build.mjs
//   TOOL_SLUG=my-tool ROOT_DOMAIN=example.com node scripts/build.mjs   # override

import { readFile, writeFile, mkdir, readdir, stat, copyFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname, relative } from 'node:path';

const ROOT = process.cwd();
const SRC = join(ROOT, 'src');
const PUB = join(ROOT, 'public');
const OUT = join(ROOT, 'dist');
const CFG_PATH = join(ROOT, '.placeholder-config.json');

const cfg = existsSync(CFG_PATH)
  ? JSON.parse(await readFile(CFG_PATH, 'utf8'))
  : {};
for (const [k, v] of Object.entries(process.env)) {
  if (k === k.toUpperCase() && typeof v === 'string' && !(k in cfg)) cfg[k] = v;
}

const TEXT_EXT = new Set(['.html', '.css', '.js', '.txt', '.xml', '.json', '.svg', '.md']);

function sub(str) {
  return str.replace(/\{\{([A-Z0-9_]+)\}\}/g, (_, k) =>
    (k in cfg && cfg[k] != null) ? String(cfg[k]) : `[[MISSING:${k}]]`);
}

async function walk(dir, base = dir) {
  const out = [];
  for (const entry of await readdir(dir)) {
    const p = join(dir, entry);
    const st = await stat(p);
    if (st.isDirectory()) out.push(...await walk(p, base));
    else out.push({ abs: p, rel: relative(base, p) });
  }
  return out;
}

async function process_tree(src) {
  if (!existsSync(src)) return;
  for (const { abs, rel } of await walk(src)) {
    const dest = join(OUT, rel);
    await mkdir(dirname(dest), { recursive: true });
    const dot = rel.lastIndexOf('.');
    const ext = dot === -1 ? '' : rel.slice(dot).toLowerCase();
    if (TEXT_EXT.has(ext)) {
      const raw = await readFile(abs, 'utf8');
      await writeFile(dest, sub(raw), 'utf8');
    } else {
      await copyFile(abs, dest);
    }
  }
}

await mkdir(OUT, { recursive: true });
await process_tree(SRC);
await process_tree(PUB);

// Missing-placeholder audit: fail loud so nothing ships with [[MISSING:X]] on screen.
const missing = new Set();
for (const { abs, rel } of await walk(OUT)) {
  const dot = rel.lastIndexOf('.');
  const ext = dot === -1 ? '' : rel.slice(dot).toLowerCase();
  if (!TEXT_EXT.has(ext)) continue;
  const txt = await readFile(abs, 'utf8');
  for (const m of txt.matchAll(/\[\[MISSING:([A-Z0-9_]+)\]\]/g)) missing.add(m[1]);
}
if (missing.size) {
  console.error('[build] MISSING placeholders — add these to .placeholder-config.json:');
  for (const k of missing) console.error('  -', k);
  process.exit(2);
}
console.log(`[build] ok — ${cfg.TOOL_SLUG || '(no slug)'} → dist/`);
