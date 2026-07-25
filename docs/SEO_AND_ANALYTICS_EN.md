# Landing SEO, indexing and analytics

Branch `day14`, repository `neighbro.place`. This is the work done on `sosed.place` carried
over — the landing engine is shared, so the decisions and the code are the same; what is
recorded here is the outcome and the differences. The reasoning behind each step lives in
`sosed.place/docs/SEO_AND_ANALYTICS_EN.md`.

Repositories:

- neighbro landing — <https://github.com/panov-id/neighbro.place>
- sosed landing — <https://github.com/panov-id/sosed.place>
- monorepo (panel, functions, scripts) — <https://github.com/panov-id/xor.ad>

## Differences from sosed

- **10 languages** (`en, fr, de, es, el, uk, be, kk, ka, ru`) instead of 17.
- The root **was already English**, so unlike sosed there is no change of the main page's
  language here — only the addresses of the other languages change.
- Its own storage keys: language in `lang`, consent in `nb-consent`, signup flag in
  `nb-wl-done`.
- Its own IndexNow key: `3d9b6e2c47f84a15b8c0d7e39a52f16b`.
- The source page has a richer head (`og:locale` with alternates, `twitter:*`), so the
  generator rewrites those tags instead of adding second copies. The same logic went into
  sosed's copy of the generator — the two files are kept identical.
- The brand in `title` is `neighbro` across all languages, rather than the translated
  `brand` key.
- No custom 404 page: on sosed it turned out that Bunny cannot substitute one for 404s
  coming from storage.

## Done

- [x] **Indexing.** `robots.txt` declaring the sitemap, a generated `sitemap.xml`, and a
      Search Console verification meta tag from `SEARCH_CONSOLE_TOKEN` (production only).
- [x] **10 language pages.** `landing/build-pages.mjs` plus the shared
      `landing/i18n-dictionary.mjs`, which `check-i18n.mjs` reads as well. English at the
      root, the rest in folders, each with `canonical`, a translated head, `og:locale` and
      reciprocal `hreflang` (verified: 11 alternates per page, every target exists).
- [x] **The language switcher navigates to a URL**, a soft browser-language redirect on the
      root, `<base href="/">` on language pages, and a generator-level ban on in-page
      anchors.
- [x] **GA4 behind the `analyticsId` flag** plus a `waitlist_signup` event; CSP widened for
      the Google domains.
- [x] **Consent banner** and a footer "cookies" button to withdraw; copy in all 10
      languages; `gtag.js` is not loaded without consent.
- [x] **A six-question FAQ** in all 10 languages plus `FAQPage` markup built by the
      generator from those same keys (verified on en, ru, ka).
- [x] **`Organization` / `WebSite`** in the head with `sameAs` to GitHub, and a repository
      icon in the footer.
- [x] **Non-production is not indexable:** `LANDING_ENV` across the three workflows,
      `Disallow: /` and `noindex` in every HTML file including language folders, sitemap
      removed.
- [x] **IndexNow** — the production deploy posts the sitemap's URL list to
      `api.indexnow.org`.
- [x] **Bunny, zone `neighbro-prod` (6123217):** the "seo: www to apex" edge rule — a 301
      from `www.neighbro.place` to the apex preserving the path; and "seo: short browser
      cache for html" — 300 seconds instead of thirty days for pages, `robots.txt` and
      `sitemap.xml`. Verified by request (rules take up to half a minute to propagate).
- [x] **Privacy policy** — GA4 added to the processors, the cookies section rewritten.
- [x] **SPEC** — sections on addresses and languages, and on analytics and consent.
- [x] **`deploy/run-node.sh`** — Node in a container locally, on the runner in CI.

## Remaining

- [ ] The `ANALYTICS_ID` and `SEARCH_CONSOLE_TOKEN` secrets in GitHub — without them
      production deploys without a counter and without verification.
- [ ] After the first production deploy: submit the sitemap to Search Console and verify
      live — language pages serve translated HTML, `hreflang` is reciprocal, no requests to
      Google without consent, no CSP violations in the console.
