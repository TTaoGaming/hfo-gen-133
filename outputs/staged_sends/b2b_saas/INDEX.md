# B2B Vertical Workflow Starters - Gen-133 Batch 1

Eight vertical proposal-to-cash starters are staged and eight matching Cloudflare Pages landings are live. Each offer is priced at **$1,500 setup + $249/month managed care** (year-one offer value: **$4,488**). No live Stripe product, charge, customer send, customer deployment, or cold outreach was created.

## Authority and provenance

- Gen-133 worktree: `C:\Dev\hfo_gen_133_forge`
- Branch: `agent/sigrun-gen133-spec-20260730`
- Local and remote branch head at batch start: `f362525eb4fccfbc1aad1ab3f6a0a224f9b498aa`
- Selected base commits: Activepieces `8d29bbe6fdd572b15398adc67dff74b2e30d3a3d`; Cal.com `038381aeca6261635357957d66b8ba85cdb29737`; Trigger.dev `8f66af6e18b73ceaf4a8c2d198bb662a7bb85202`
- Clones are sparse, shallow working trees with the upstream Git remote preserved. Run `git sparse-checkout disable` inside a starter to materialize its complete upstream tree.

## Ranked offer queue

Scores are bounded heuristics, not measured market results. Each factor uses 1 (weak) to 5 (strong); rank score is `buyer accessibility x ACV capacity x HFO stack fit`. ACV capacity estimates the vertical's ability to sustain this offer, not an observed average contract value.

| Rank | Vertical | Buyer signal | Access | ACV capacity | HFO fit | Score | Live landing |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | HVAC dispatcher | Owner/dispatcher rekeys each job into estimate, calendar, dispatch notes, and invoice | 4 | 5 | 5 | 100 | [Open](https://hfo-hvac-dispatcher-b2b.pages.dev) |
| 2 | Freelance contract sender | Freelancer rebuilds scope/terms and reconciles signature, acceptance, and invoices by hand | 5 | 4 | 5 | 100 | [Open](https://hfo-freelance-contract-sender-b2b.pages.dev) |
| 3 | Real-estate proposal | Listing agent repeatedly assembles seller presentations from intake, comps, and branded files | 4 | 4 | 5 | 80 | [Open](https://hfo-real-estate-proposal-b2b.pages.dev) |
| 4 | Auto detailer intake | Owner quotes from scattered photo threads and manually reconciles deposit, route, and calendar | 5 | 3 | 5 | 75 | [Open](https://hfo-auto-detailer-intake-b2b.pages.dev) |
| 5 | Coach booking | Coach duplicates goals, package, billing, cadence, notes, and renewal context | 5 | 3 | 5 | 75 | [Open](https://hfo-coach-booking-b2b.pages.dev) |
| 6 | Tattoo studio booking | Studio manager reconciles DMs, reference images, artist fit, deposits, and calendars | 4 | 3 | 5 | 60 | [Open](https://hfo-tattoo-studio-booking-b2b.pages.dev) |
| 7 | Dog groomer booking | Groomer screens coat, behavior, allergies, duration, and schedule fit through messages | 5 | 2 | 5 | 50 | [Open](https://hfo-dog-groomer-booking-b2b.pages.dev) |
| 8 | Dental appointment SMS | Front desk repeats reminder calls and routes reschedules/balance tasks across queues | 3 | 4 | 3 | 36 | [Open](https://hfo-dental-appointment-sms-b2b.pages.dev) |

Tie break: HVAC ranks above freelance because the dispatch-to-invoice pain is repeated at higher frequency and has greater multi-seat operational leverage; this is still a hypothesis requiring buyer evidence.

## What each starter contains

- upstream sparse clone and exact Git commit
- `vertical_starter/workflow.json` with five proposal-to-cash steps and human gates
- `vertical_starter/stripe_pricing_preset.json` with `live_mode: false` and `api_calls_allowed: false`
- `vertical_starter/templates/proposal_template.pdf`
- root `landing.html` plus standalone `landing/` deploy directory
- vertical buyer signal, landing copy, FAQ, and Cal.com embed integration point

## Evidence status

- **Verified:** 8 upstream clone heads and root license files; 8 valid workflow/price/site JSON sets; 8 one-page PDF renders; 8 local HTTP 200 pages; 8 public HTTP 200 Pages sites and matching deployed `site.json`.
- **Partial:** these are starter configurations, not imported and executed customer workflows. No distinct independent verifier has reviewed the batch.
- **Known hold:** the Cal.com embed code is present, but `cal_link` remains `REPLACE_WITH_OPERATOR_CAL_LINK`. The guessed `ttao/30min` route returned 404 and was not used.

## Exactly one next safe action

Operator provides the exact Cal.com event link; replace the placeholder in all eight `landing/site.json` files and redeploy only the static landing directories.
