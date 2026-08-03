#!/usr/bin/env node
/**
 * HFO Suika DLC behavioral runtime probe.
 *
 * Anti-L_DEPLOY_WITHOUT_RUNTIME gate: a page that returns HTTP 200 is NOT a
 * passing game. This probe boots the real page in headless Chromium, drives the
 * real Matter.js physics loop, and asserts the game logic actually fires.
 *
 * Usage:
 *   node tools/game_probe/probe.mjs --url http://localhost:8101 --variant 1
 *   node tools/game_probe/probe.mjs --url https://x.pages.dev --variant 2 --json out.json
 *
 * Exit 0 = all checks PASS. Exit 1 = at least one FAIL.
 */
import { chromium } from 'playwright-core';
import { writeFileSync } from 'node:fs';

const CHROME_CANDIDATES = [
	'C:/Users/tommy/AppData/Local/ms-playwright/chromium-1234/chrome-win64/chrome.exe',
	'C:/Users/tommy/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe',
	'C:/Users/tommy/AppData/Local/ms-playwright/chromium-1223/chrome-win/chrome.exe',
];

function arg(name, dflt = null) {
	const i = process.argv.indexOf(`--${name}`);
	return i === -1 ? dflt : process.argv[i + 1];
}

const url = arg('url');
const variant = Number(arg('variant', '1'));
const jsonOut = arg('json');
if (!url) {
	console.error('FATAL: --url required');
	process.exit(2);
}

const checks = [];
function check(id, pass, detail) {
	checks.push({ id, status: pass ? 'PASS' : 'FAIL', detail: String(detail) });
	console.log(`${pass ? 'PASS' : 'FAIL'}  ${id}  ${detail}`);
}

const exe = (await import('node:fs')).existsSync(CHROME_CANDIDATES[0])
	? CHROME_CANDIDATES[0]
	: CHROME_CANDIDATES.find(p => (require('node:fs')).existsSync(p));

const browser = await chromium.launch({ executablePath: exe, headless: true });
const page = await browser.newPage({ viewport: { width: 700, height: 1000 } });

const consoleErrors = [];
const failedRequests = [];
// favicon.ico is a browser-initiated request the game never asks for, and Playwright
// does not surface it through page.on('response') — ignore it in BOTH directions so it
// neither fakes a RED nor hides a real asset 404.
const isBenign = u => /\/favicon\.ico(\?|$)/.test(u || '');
page.on('console', m => {
	if (m.type() !== 'error') return;
	const loc = m.location() || {};
	if (isBenign(loc.url)) return;
	consoleErrors.push(m.text() + (loc.url ? ` @ ${loc.url}` : ''));
	// cross-check: console-visible 404s that the response listener missed still count
	if (/status of 40\d|status of 5\d\d/.test(m.text()) && loc.url) failedRequests.push(`console ${loc.url}`);
});
page.on('pageerror', e => consoleErrors.push('pageerror: ' + e.message));
page.on('response', r => { if (r.status() >= 400 && !isBenign(r.url())) failedRequests.push(`${r.status()} ${r.url()}`); });
page.on('requestfailed', r => { if (!isBenign(r.url())) failedRequests.push(`requestfailed ${r.url()}`); });

let hardFail = null;
try {
	const resp = await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 });
	check('P0-HTTP200', resp && resp.status() === 200, `status=${resp && resp.status()}`);

	// --- P1: the game object actually booted (script-scoped const, resolves by name)
	const booted = await page.evaluate(() => typeof Game !== 'undefined' && Array.isArray(Game.fruitSizes));
	check('P1-BOOT', booted, `Game object present with fruitSizes=${booted}`);
	if (!booted) throw new Error('Game did not boot; remaining checks are meaningless');

	// --- P2: every tier sprite resolves to a real decoded image (not a 404 placeholder)
	const sprites = await page.evaluate(async () => {
		const srcs = Game.fruitSizes.map(f => f.img);
		const results = await Promise.all(srcs.map(src => new Promise(res => {
			const im = new Image();
			im.onload = () => res({ src, ok: im.naturalWidth > 0 || src.endsWith('.svg'), w: im.naturalWidth });
			im.onerror = () => res({ src, ok: false, w: 0 });
			im.src = src;
		})));
		return results;
	});
	const badSprites = sprites.filter(s => !s.ok);
	check('P2-SPRITES', badSprites.length === 0 && sprites.length >= 11,
		`${sprites.length - badSprites.length}/${sprites.length} tier sprites decoded; bad=${JSON.stringify(badSprites.map(b => b.src))}`);

	// --- P3: theme actually changed off the upstream default
	const theme = await page.evaluate(() => ({
		dlc: typeof Game.dlc === 'undefined' ? null : Game.dlc,
		title: document.title,
		names: Game.fruitSizes.map(f => f.name || null),
	}));
	check('P3-THEME', !!theme.dlc && theme.dlc.variant === variant && !!theme.dlc.theme,
		`Game.dlc=${JSON.stringify(theme.dlc && { variant: theme.dlc.variant, theme: theme.dlc.theme })} title="${theme.title}"`);
	check('P3-TIERNAMES', theme.names.filter(Boolean).length >= 11,
		`named tiers=${theme.names.filter(Boolean).length}/11 e.g. ${JSON.stringify(theme.names.slice(0, 3))}`);

	// --- P4: start the real game loop
	await page.evaluate(() => Game.startGame());
	await page.waitForTimeout(600);
	const ready = await page.evaluate(() => Game.stateIndex);
	check('P4-START', ready === 1, `stateIndex=${ready} (1=READY)`);

	// --- P5: THE core behavioral assertion. Inject two same-tier bodies that must
	// collide under real gravity, and assert the merge handler fired + score moved.
	const merge = await page.evaluate(async () => {
		const before = Game.score;
		const beforeMerged = Game.fruitsMerged.reduce((a, b) => a + b, 0);
		// Inject down the middle of a PLAYABLE column. Variants that change world
		// geometry (e.g. twin pots) expose their containers via Game.dlc.pots; using
		// the active pot's centre keeps this a fair merge test instead of silently
		// imposing a single-pot layout on every variant.
		const injectX = (Game.dlc && Array.isArray(Game.dlc.pots) && Game.dlc.pots.length)
			? Game.dlc.pots[Game.dlc.activePot || 0].centerX
			: Game.width / 2;
		// two tier-0 bodies dropped down the same column: they must stack and merge
		Matter.Composite.add(engine.world, Game.generateFruitBody(injectX, 500, 0));
		Matter.Composite.add(engine.world, Game.generateFruitBody(injectX + 4, 380, 0));
		await new Promise(r => setTimeout(r, 2500));
		return {
			before, beforeMerged,
			after: Game.score,
			afterMerged: Game.fruitsMerged.reduce((a, b) => a + b, 0),
			bodyCount: Matter.Composite.allBodies(engine.world).length,
		};
	});
	check('P5-MERGE-RUNTIME', merge.afterMerged > merge.beforeMerged && merge.after > merge.before,
		`merges ${merge.beforeMerged}->${merge.afterMerged}, score ${merge.before}->${merge.after}`);

	// --- P6: drop path works through the real input handler
	const drop = await page.evaluate(async () => {
		const n0 = Matter.Composite.allBodies(engine.world).length;
		Game.addFruit(Game.width * 0.35);
		await new Promise(r => setTimeout(r, 800));
		Game.addFruit(Game.width * 0.65);
		await new Promise(r => setTimeout(r, 800));
		return { n0, n1: Matter.Composite.allBodies(engine.world).length };
	});
	check('P6-DROP', drop.n1 > drop.n0, `bodies ${drop.n0}->${drop.n1} after 2 addFruit calls`);

	// ================= VARIANT-SPECIFIC MECHANIC (runtime, not source grep) =========
	if (variant === 1) {
		// DLC-1 is the CONTROL. It must prove the mechanic is UNCHANGED.
		const control = await page.evaluate(() => ({
			tiers: Game.fruitSizes.length,
			radii: Game.fruitSizes.map(f => f.radius),
			scores: Game.fruitSizes.map(f => f.scoreValue),
			isControl: !!(Game.dlc && Game.dlc.control === true),
		}));
		const UPSTREAM_R = [24, 32, 40, 56, 64, 72, 84, 96, 128, 160, 192];
		const UPSTREAM_S = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66];
		check('M1-CONTROL-UNCHANGED',
			JSON.stringify(control.radii) === JSON.stringify(UPSTREAM_R) &&
			JSON.stringify(control.scores) === JSON.stringify(UPSTREAM_S) && control.isControl,
			`radii/scores identical to upstream=${JSON.stringify(control.radii) === JSON.stringify(UPSTREAM_R)}, dlc.control=${control.isControl}`);
	}

	if (variant === 2) {
		// DLC-2 CASCADE: a merge landing next to a same-tier body must auto-chain
		// and the multiplier must escalate. Assert on live state, not source text.
		const cascade = await page.evaluate(async () => {
			Game.dlc.chain.max = 0;
			Game.dlc.chain.current = 0;
			const scoreBefore = Game.score;
			const w = Game.width, y = 780;
			// three tier-0 in a row -> first merge makes a tier-1 that should find
			// the pre-placed tier-1 neighbour and cascade.
			Matter.Composite.add(engine.world, Game.generateFruitBody(w / 2 - 130, y, 1));
			await new Promise(r => setTimeout(r, 700));
			Matter.Composite.add(engine.world, Game.generateFruitBody(w / 2 + 30, y - 40, 0));
			Matter.Composite.add(engine.world, Game.generateFruitBody(w / 2 + 34, y - 160, 0));
			await new Promise(r => setTimeout(r, 3500));
			return {
				maxChain: Game.dlc.chain.max,
				lastMultiplier: Game.dlc.chain.lastMultiplier,
				scoreBefore, scoreAfter: Game.score,
				events: (Game.dlc.chain.log || []).length,
			};
		});
		check('M2-CASCADE-CHAIN', cascade.maxChain >= 2,
			`max chain length=${cascade.maxChain} (need >=2), events=${cascade.events}`);
		check('M2-CASCADE-MULTIPLIER', cascade.lastMultiplier >= 2 && cascade.scoreAfter > cascade.scoreBefore,
			`multiplier=${cascade.lastMultiplier}x, score ${cascade.scoreBefore}->${cascade.scoreAfter}`);
	}

	if (variant === 3) {
		// DLC-3 TWIN CONTAINER: two pots, alternating placement, shared score.
		const twin = await page.evaluate(async () => {
			const potsAtStart = Game.dlc.pots.length;
			const seq = [];
			for (let i = 0; i < 4; i++) {
				seq.push(Game.dlc.activePot);
				Game.addFruit(Game.dlc.pots[Game.dlc.activePot].centerX);
				await new Promise(r => setTimeout(r, 900));
			}
			return {
				potsAtStart, seq,
				sharedScore: Game.score,
				potBodies: Game.dlc.pots.map(p => Matter.Composite.allBodies(engine.world)
					.filter(b => !b.isStatic && b.position.x >= p.left && b.position.x <= p.right).length),
			};
		});
		check('M3-TWIN-POTS', twin.potsAtStart === 2, `Game.dlc.pots.length=${twin.potsAtStart}`);
		check('M3-ALTERNATION', twin.seq.length === 4 && twin.seq[0] !== twin.seq[1] && twin.seq[1] !== twin.seq[2],
			`activePot sequence across 4 drops = ${JSON.stringify(twin.seq)}`);
		check('M3-BOTH-POTS-USED', twin.potBodies.every(n => n > 0),
			`live bodies per pot = ${JSON.stringify(twin.potBodies)}`);
	}

	if (variant === 4) {
		// DLC-4 POWER-UPS: spawn at merge threshold, cap at 3, and actually fire.
		const power = await page.evaluate(async () => {
			const threshold = Game.dlc.spawnEveryMerges;
			// force the merge counter to threshold-1, then cause one real merge
			Game.dlc.mergeCount = threshold - 1;
			Game.dlc.powerups.length = 0;
			const w = Game.width;
			Matter.Composite.add(engine.world, Game.generateFruitBody(w / 2, 520, 0));
			Matter.Composite.add(engine.world, Game.generateFruitBody(w / 2 + 4, 400, 0));
			await new Promise(r => setTimeout(r, 2500));
			const afterSpawn = Game.dlc.powerups.slice();
			// cap test
			for (let i = 0; i < 6; i++) Game.dlc.grantPowerup('BOMB');
			const capped = Game.dlc.powerups.length;
			// activation test: BOMB must remove a body
			Game.dlc.powerups[0] = { type: 'BOMB' };
			const bodiesBefore = Matter.Composite.allBodies(engine.world).filter(b => !b.isStatic).length;
			Game.dlc.activatePowerup(0);
			await new Promise(r => setTimeout(r, 600));
			const bodiesAfter = Matter.Composite.allBodies(engine.world).filter(b => !b.isStatic).length;
			return { threshold, afterSpawn, capped, bodiesBefore, bodiesAfter, types: Game.dlc.powerupTypes };
		});
		check('M4-SPAWN-AT-THRESHOLD', power.afterSpawn.length >= 1,
			`powerups after crossing merge threshold ${power.threshold} = ${JSON.stringify(power.afterSpawn.map(p => p.type))}`);
		check('M4-INVENTORY-CAP', power.capped === 3, `inventory capped at ${power.capped} (need 3)`);
		check('M4-ACTIVATE-EFFECT', power.bodiesAfter < power.bodiesBefore,
			`BOMB removed a body: ${power.bodiesBefore}->${power.bodiesAfter}`);
		check('M4-THREE-TYPES', Array.isArray(power.types) && power.types.length >= 3,
			`powerupTypes=${JSON.stringify(power.types)}`);
	}

	// --- P9: no runtime errors anywhere in that whole session
	check('P9-NO-CONSOLE-ERRORS', consoleErrors.length === 0, `errors=${JSON.stringify(consoleErrors.slice(0, 3))}`);
	check('P9-NO-404S', failedRequests.length === 0, `failed=${JSON.stringify(failedRequests.slice(0, 5))}`);
} catch (e) {
	hardFail = e.message;
	check('PROBE-COMPLETED', false, `probe aborted: ${e.message}`);
} finally {
	await browser.close();
}

const failed = checks.filter(c => c.status === 'FAIL');
const summary = { url, variant, total: checks.length, passed: checks.length - failed.length, failed: failed.length, hardFail, checks };
if (jsonOut) writeFileSync(jsonOut, JSON.stringify(summary, null, 2));
console.log(`\n=== ${failed.length === 0 ? 'GREEN' : 'RED'}  variant=${variant}  ${summary.passed}/${summary.total} passed  ${url}`);
process.exit(failed.length === 0 ? 0 : 1);
