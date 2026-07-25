# Spec — neighbro.place Landing Page (Waitlist)

## Purpose

A single-page pre-launch teaser — testing demand via conversion into a waitlist (see `xor.ad/docs/marketing-plan_EN.md`). Not a full site, not the app.

## Section structure

1. **Headline + pitch + waitlist form** — already implemented (`index.html`): name, one-line pitch, email field, send button, a note about premium early-user status.
2. **How it works** — feature block(s), short and simple:
   - Write a short message — people nearby see it.
   - A like matches — a private chat opens.
   - The message disappears on its own after a few hours — nothing piles up.
3. **Waitlist form again** (at the bottom of the page) — the same form as in the header, for anyone who scrolls all the way down.

## Tone and style

Copy and visual tone follow neighbro.place's European-flavored identity (see the README's "The faces" section). The structure and the set of features in block 2 are shared with sosed.place — the difference is only in language and tone, not in which features are covered.

## Technical constraints

- Static — a single source HTML file with inline styles. The only build step is `landing/build-pages.mjs`, which fans it out per language at deploy time (below). Node runs only through `deploy/run-node.sh`: in a container locally, directly on the runner in CI.
- The waitlist form keeps submitting email to the relay backend (`POST /waitlist`, see the existing `index.html`); block 2 is purely informational, no logic of its own.

## Languages and addresses

Translations live in a single `T` dictionary inside `index.html`, which stays the single source of truth. At deploy time the generator turns that page into 10 static pages:

- `neighbro.place/` — English, and the `x-default` target;
- `neighbro.place/ru/`, `/de/`, `/fr/`, `/es/`, `/el/`, `/uk/`, `/be/`, `/kk/`, `/ka/`.

Each page carries its own `canonical`, translated `title`/`description`/`og:*`/`twitter:*`, its own `og:locale` with the alternates listed, reciprocal `hreflang`, and `FAQPage` markup in its own language. Language pages rely on `<base href="/">`, which means **in-page anchors (`href="#…"`) are forbidden on the landing** — the generator fails deliberately if one appears.

On generated pages the language switcher navigates to a URL; in the raw source (local development without the generator) it still swaps text in place. A first-time visitor landing on the root with another language is redirected once to their own page, if we publish that language.

## Analytics and consent

- GA4 is switched on by the `analyticsId` flag in `config.js`, which deploy fills from `ANALYTICS_ID`. Empty means no counter and no banner — which is exactly how dev and uat run.
- Without explicit consent `gtag.js` is never downloaded. Declining means zero outbound requests. The choice is stored in `nb-consent`.
- Consent can be withdrawn through the "cookies" button in the footer, which brings the banner back.
- Only production is indexable: any `LANDING_ENV` other than `prod` gets `Disallow: /`, a `noindex` meta tag in every HTML file (language folders included), and no sitemap.

## Open questions

- Exact copy for the "how it works" block hasn't been written yet.
- Illustrations/icons for the feature block are not defined yet (see also the open question about icons in `docs/01-splash-screen_EN.md`).
- Whether footer links to the legal documents (`legal/`) are needed at the teaser stage, or can wait for the full site — not decided.
