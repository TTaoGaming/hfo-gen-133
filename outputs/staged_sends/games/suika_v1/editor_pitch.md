# HFO Suika Smash — Editor Pitch

**Live now:** https://hfo-suika-v1.pages.dev/
**Portfolio (21 more free HTML5 titles):** https://hfo-games.pages.dev/

## One-liner

A polished, obsidian-and-gold reskin of the viral Suika/Watermelon merge
formula — drop fruit, merge same-size pairs, chase a bigger fruit and a
higher score before the stack tops out. Pure JS + Matter.js, zero install,
mobile and desktop.

## Why it fits your catalog

- **Proven mechanic.** Suika-style merge games are one of the most
  consistently high-retention casual genres of the last two years — simple
  one-input control (aim + drop), satisfying physics-based feedback, and a
  natural "one more try" loop after a highscore chase.
- **Instant load, no dependencies.** Static HTML5 canvas + a single vendored
  physics library (Matter.js). No backend, no account, no ads baked in — a
  clean drop-in for any portal wrapper.
- **Mobile-first already.** Canvas auto-scales to the viewport (see the
  `resizeCanvas` logic); touch and mouse both drive the same input path.
- **Clean, honest lineage.** Built on `moonfloof/suika-game`
  (https://github.com/moonfloof/suika-game), itself a clone of the original
  Korean/Japanese "Suika Game," released under the Unlicense (public
  domain). Matter.js is MIT-licensed. Full attribution is in-page (footer)
  and in `manifest.json` — nothing here is unlicensed or ambiguous.

## What we changed

- Full obsidian-purple + gold visual reskin (CSS custom properties, canvas
  background, wall render colors) — distinct from the original peach/orange
  palette.
- Retitled to "HFO Suika Smash," added an HFO header and an attribution
  footer linking back to both the upstream repo and our own portfolio.
- No gameplay, physics, or scoring logic was touched — same merge feel that
  made the original format popular, verified locally (all assets 200,
  zero console errors, zero missing JS references) before deploy.

## Ask

Evaluate for portal placement (Poki / CrazyGames / itch.io). Happy to
provide a build without the HFO header/footer chrome if your submission
guidelines require a bare canvas, or to swap in portal-specific SDK hooks
(ad breakpoints, save-state callbacks) on request.

## Contact / more titles

Full free-to-browse portfolio, no login: https://hfo-games.pages.dev/
