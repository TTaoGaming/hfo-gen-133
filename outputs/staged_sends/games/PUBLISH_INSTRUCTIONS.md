# Publish instructions — 21 games to itch.io (draft-first)

Staged, not published. Every step below is yours to click — this batch is
class-envelope PATCH+STAGE only, nothing was submitted anywhere.

## 0. Before you start

Each title's actual game file lives at
`C:\Dev\hfo_dev_2026_3\omega_games\{slug}\index.html` (self-contained, no
external calls — safe to zip as-is). The 21 folders under
`outputs\staged_sends\games\{seq}_{slug}\itch_manifest.json` hold the text
itch.io wants; nothing is uploaded yet. Thumbnails are missing for all 21
(see `notes.md`) — grab at least one screenshot per game before you upload,
or use a placeholder for the first pass.

## 1. Sign in

Go to **https://itch.io/user/settings** (sign up first at
**https://itch.io/register** if you don't have an account) and confirm
you're logged in.
*[screenshot: your itch.io dashboard header should show your username top-right]*

## 2. Per title (repeat 21x, ~5 min each once you're warmed up)

1. Go to **https://itch.io/game/new**
2. Fill the form from that title's `itch_manifest.json`:
   - **Title** → `title`
   - **Short description / tagline** → `short_description`
   - **Description** (the big rich-text box) → paste `long_description`
   - **Classification** → Games
   - **Kind of project** → **HTML** *(this is the important one — it makes
     itch.io host the file in-browser instead of offering it as a download)*
   - **Release status** → Released
   - **Pricing** → set to "No payments" or "$0 or donate" (`pricing` field
     says `free_or_donation` — either works, your call)
   - **Genre** → `genre`
   - **Tags** → paste each entry in `tags`
3. Scroll to **Uploads** → click "Upload files" → select the game's
   `index.html` (or a `.zip` if you bundled it) → itch.io will show a
   checkbox "This file will be played in the browser" — **check it**, and
   set width/height from `embed_options` (640x480).
   *[screenshot: the upload row should show a small "play in browser"
   checkbox next to the filename once the upload finishes]*
4. Add the cover image / screenshots once you have them (see `notes.md`).
5. **Visibility**: set to **Draft** (bottom of page) — do NOT click
   "Save & view page" with Public/Restricted selected yet.
6. Click **Save**.

Repeat for all 21. itch.io keeps drafts private — nobody sees them until
you flip visibility yourself.

## 3. Go live, whenever you're ready

Once all 21 are staged as drafts and you've checked each one plays
correctly (open the draft page, click play, confirm the game loads in the
embedded frame):

- Open each game's edit page → change **Visibility** from Draft to
  **Public** → Save.
- You can do this one at a time, spread over days, or all at once — there's
  no batch cost either way.

## 4. Optional: bulk automation with butler

itch.io has a CLI (`butler`) that can push updates without the web form,
useful once you're iterating on a title after the first manual upload:

1. Install: **https://itch.io/docs/butler/installing.html**
2. `butler login` (opens a browser auth flow, one-time)
3. `butler push <path-to-folder-or-zip> <your-username>/<game-slug>:html`

Butler still requires the *first* upload/project creation to happen through
the web form above — it's for pushing new builds to an existing project,
not for the initial submission.

## Acceptance test

**One named person on itch.io comments on, rates, or downloads any of the
21 titles by 2026-08-16 = external signal.** Anything before that date is
just staging.
