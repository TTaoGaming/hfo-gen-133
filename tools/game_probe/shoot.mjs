#!/usr/bin/env node
/**
 * Visual QA capture for the Suika DLC variants.
 *
 * The probe proves the game LOGIC fires; it says nothing about whether the art is
 * any good. This drives each live variant into a realistic mid-game board and
 * captures a mobile-viewport screenshot so the art can be judged by eye.
 */
import { chromium } from 'playwright-core';
import { mkdirSync } from 'node:fs';

const EXE = 'C:/Users/tommy/AppData/Local/ms-playwright/chromium-1234/chrome-win64/chrome.exe';
const OUT = 'outputs/staged_sends/games/_screenshots';
const VARIANTS = [
	{ n: 1, slug: 'norse' }, { n: 2, slug: 'crystal' },
	{ n: 3, slug: 'yinyang' }, { n: 4, slug: 'alchemy' },
];

mkdirSync(OUT, { recursive: true });
const browser = await chromium.launch({ executablePath: EXE, headless: true });

for (const v of VARIANTS) {
	const url = `https://hfo-suika-dlc-${v.n}-${v.slug}.pages.dev/`;
	// iPhone-ish portrait: this is how the operator will actually see it
	const page = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
	try {
		const r = await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 });
		if (!r || r.status() !== 200) { console.log(`SKIP v${v.n} ${v.slug}: HTTP ${r && r.status()}`); await page.close(); continue; }

		await page.screenshot({ path: `${OUT}/dlc${v.n}_${v.slug}_1_menu.png` });

		await page.evaluate(() => Game.startGame());
		await page.waitForTimeout(700);
		// build a realistic board: a spread of drops plus some guaranteed merges
		await page.evaluate(async () => {
			const w = Game.width;
			const xs = [0.3, 0.7, 0.45, 0.6, 0.35, 0.65, 0.5];
			for (const f of xs) { Game.addFruit(w * f); await new Promise(r => setTimeout(r, 700)); }
			for (let t = 0; t < 4; t++) {
				Matter.Composite.add(engine.world, Game.generateFruitBody(w * 0.5, 520, t));
				Matter.Composite.add(engine.world, Game.generateFruitBody(w * 0.5 + 4, 400, t));
				await new Promise(r => setTimeout(r, 1200));
			}
			await new Promise(r => setTimeout(r, 1500));
		});
		await page.screenshot({ path: `${OUT}/dlc${v.n}_${v.slug}_2_play.png` });
		const score = await page.evaluate(() => Game.score);
		console.log(`SHOT v${v.n} ${v.slug}: menu + play captured, live score=${score}`);
	} catch (e) {
		console.log(`FAIL v${v.n} ${v.slug}: ${e.message}`);
	} finally { await page.close(); }
}
await browser.close();
console.log(`\nscreenshots -> ${OUT}`);
