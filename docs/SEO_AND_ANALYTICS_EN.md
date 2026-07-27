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
- [x] **Our own page counter** (2026-07-27) — `POST /pageview` on the relay; it runs
      without consent because there is nothing to consent to: no address, no user agent,
      no identifier, and nothing on the device but a `sessionStorage` flag that dies with
      the tab. The referrer is cut to its host, the width to a bucket. Own first-view
      key: `nb-seen`. Read in the panel on the "Page views" page.
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

- [x] `ANALYTICS_ID` = `G-K7EP39DDK9` set in the `production` environment
      (2026-07-27); dev and uat stay empty, hence no counter and no banner there.
      `SEARCH_CONSOLE_TOKEN` is left unset: the domain is verified by DNS.
- [x] The checks that need no production are closed by `landing/verify-seo.mjs` (the file
      is shared with sosed): run 2026-07-27 against a generated copy — 10 languages serve
      translated HTML without JS, every page carries 11 `hreflang` alternates and all of
      them exist, the 12-URL sitemap parses and holds no dead link.
- [x] Production shipped 2026-07-27; the domain is verified by a TXT record and the
      sitemap is submitted to Search Console (`https://neighbro.place/sitemap.xml`,
      12 URLs).
- [ ] Verify live in a browser: no requests to Google domains before consent (our own
      counter still runs — it needs none), no CSP violations in the console.
