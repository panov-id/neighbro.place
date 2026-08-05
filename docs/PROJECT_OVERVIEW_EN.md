# NEIGHBRO — Project Overview

> The global face of a hyperlocal, ephemeral neighbourhood network. A place to talk to the people right around you, right now — and then let it go.

---

## 1. In one paragraph

NEIGHBRO is not another social network with a permanent profile and a feed you scroll for years. You open the app, see short messages from people physically near you — in your building, office, block, district — and you can reply, like, and strike up a private chat. A few hours later it all disappears. No followers, no accumulated "profile", no archive trailing behind you for years. **Ephemerality is a feature, not a limitation.**

NEIGHBRO is the English-speaking, European-in-spirit face of the platform. Technically it is one of the frontends running on the shared `xor.ad` backend; its Russian-speaking twin is [sosed.place](https://github.com/panov-id/sosed.place). Both faces share one user pool, one feed and one database — they are different wrappers over the same data, not isolated audiences.

---

## 2. Positioning

The easiest way to understand NEIGHBRO is by what it is **not**:

| | Classic social | Dating apps | Neighbourhood nets (Nextdoor etc.) | **NEIGHBRO** |
|---|---|---|---|---|
| Profile | Permanent, accumulates | Permanent, bio | Address-bound, verified | **No permanent profile** |
| Content | Lives forever | — | Lives forever | **Vanishes in ~4 hours** |
| Sign-up | Email/phone/social | Verification, photos | Address check | **Birth year + name, no email/password** |
| Who's near | Friends/follows | Everyone in range | Verified neighbours | **People in your chosen radius, right now** |
| Motive | Status, reach | Dates | Ads, utilities, lost pets | **Light, spontaneous human contact** |

NEIGHBRO sits in an empty niche between "dating" and "district chat": not about dates, not about lost-cat notices, but about **spontaneous human contact with whoever is literally around you** — matched by mood and interest, not endless swipes.

---

## 3. Core functionality

### 3.1. Sign in without an account
- Pick any display name (no real name required) and a birth year — tap "enter". No email, no password.
- Under the hood the server generates an encrypted random UID bound to the birth year, name and a set of sufficiently unique browser-fingerprint parameters. You are recognised even after clearing caches.
- Bound to the browser: not a cross-device account. Another browser or a private window is a new identity.
- Birth year sets the feed age filter and enforces a hard split between adults and minors (see §6).

### 3.2. Location and radius
- The app can detect your position or you can set it manually.
- A map slider sets your radius of interest — from "my building" to "the whole city".

### 3.3. Feed
- Short messages from people nearby. New ones at the bottom, chat-style — not a stack of posts on top.
- AI detects each message's language: by default ~95% of the feed is in your language, ~5% in other languages spoken in your region (ratios configurable).
- Lively and slightly non-serious — closer to Pure than to a corporate wall.

### 3.4. Posting
- Up to 128 characters, optionally city/country and "how many of you".
- Protection: a per-IP rate limit on the node + content moderation in the same place. There is no external captcha.
- Everyone starts with a quota of 5 messages; the quota drops if other users report you.

### 3.5. Disappearance
- Messages live 4 hours 20 minutes by default, then vanish. TTL is configurable.

### 3.6. Like → match → chat
- Like a message in the feed. If they like you back, you're offered a private chat.
- A short live back-and-forth. **The chat history exists only between the two of you and nowhere else** (see §5).

### 3.7. Share an external contact
- Optionally attach any handle/link (Telegram, Instagram — anything, no fixed list) and choose to share it in chat — to keep in touch and as a light trust signal.
- The decision to share is made fresh each time, never on by default. Following it shows a leaving-the-site warning.

### 3.8. Support
- A support button is always available. Messages land in a table of our own database and notify the team.

---

## 4. Design

Black and white, high contrast, on purpose. Neo-brutalism: hard borders, sharp corners, blur-free shadows. Users control contrast and switch light/dark themes themselves. One accent colour per face over the monochrome base: NEIGHBRO uses **warm gold/bronze** (sosed.place uses red). Headings in the Unbounded typeface.

---

## 5. Privacy

Core principle: **sensitive data lives on the device, not the server.**

- Chat history sits in the browser's IndexedDB, **encrypted client-side** via the Web Crypto API before it is written.
- The backend receives the minimum — exactly what routing and limits require.
- The fingerprint-based UID exists for exactly one purpose: so quota reduction after reports can't be bypassed by clearing caches. It is abuse protection, not surveillance, and it recognises the browser, not the person across all devices.

---

## 6. Moderation and safety

Every message — feed or chat — is checked **before** it is published:

- **Toxicity** — a classifier on our own node. Fails the check → not published.
- **Tone** — subtext is classified in the same place. The text never leaves the
  node: moderation uses no external processor.
  - **Harassment, drugs, sex services** — fully rejected, never published.
  - **Sexual subtext** — invisible by default; to see it you must accept a separate agreement and provide an email.
- **Age separation.** An adult (18+) will never be shown people under 18. For a minor the slider maximum stays narrow and never widens to adults.
- **Quotas and reports.** Starting quota of 5, reduced on reports/blocks.

The bar: content stays within the norms of a calm, peaceful society.

---

## 7. Architecture (alpha)

- **Frontend:** React web app in the browser (no native app in the alpha).
- **Backend:** our own Deno node (the relay) — business logic, quotas, the age filter, moderation orchestration. State in our own Postgres beside the node, data in Bunny object storage. There is no managed backend: no vendor sits in the critical path.
- **Gate:** `xor.ad` — the shared entry domain in front of the relay; all frontends talk to it.
- **Language detection:** a local library right inside Edge Functions — no external API, no per-message cost.
- **Post protection:** a rate limit on the node (applied to posting only, not chat).
- **Deploy:** frontend via Bunny CDN; backend on our own nodes, released by tag through GitHub Actions.
- **Configuration:** every knob (char limit, starting quota, TTL, radius) via environment variables.
- **Admin panel:** a separate Refine app (`xor.ad/panel/`) — waitlist, reports, bans, quotas across both faces.

---

## 8. Who it's for

**User portraits:**

1. **New in town / relocator.** Just moved, no one nearby. NEIGHBRO offers an instant, low-commitment way into the local scene without "friends forever".
2. **Resident of a big building / campus / coworking.** Hundreds of people around, all anonymous. The app turns physical proximity into a chance to connect.
3. **Social-media-fatigued.** Doesn't want yet another permanent profile, a time-eating feed and a race for likes. Here everything vanishes — no weight.
4. **Traveller.** In a new city for a couple of days — wants to feel the "pulse of the place" and maybe cross paths here and now.
5. **Introvert / dating-app-wary.** "Post to the ether first, mutual like second" removes the pressure of a direct swipe and a bio.
6. **Ad-hoc local crowds.** A queue, a concert, a flight delay, a district during an event — a temporary surge of people with something to say to each other right now.

**Why it works as a product:** physical proximity + ephemerality + a low entry bar remove the three big barriers of ordinary networks — fear of permanence, bio fatigue, and the feeling of being judged. The niche between dating and district chat has almost no quality product in it.

---

## 9. Ideas for development

Grouped by horizon and risk. The core idea stays ephemeral — this is **not** a pivot into yet another permanent-profile social network.

### 9.1. Deepening the core (low risk, strengthens what exists)
- **Reactions beyond likes** — light emoji reactions (that don't drive matching) to enliven the feed.
- **Topics/moods** — pick a mood tag when posting (chatter / help / meet up / recommendation), filter the feed by it.
- **"Pulse of the place"** — the splash already shows live infographics; grow it into a district mini-dashboard: who's online, what's being talked about, activity spikes.
- **Voice flashes** — a short (≤10s) voice message, also ephemeral.
- **Better chat** — typing/read indicators, in-chat reactions, ephemeral photos in chat only (the feed stays text-only).

### 9.2. Neighbourhood offers (the only form of advertising)
- **An offer** — a post by a local business that must carry a discount, available to anyone who comes and asks. Publication is free: the platform takes no money and no barter. The mechanic lives in `xor.ad/docs/offers/`.
- **Images and links live only in offers.** Regular messages stay text-only and link-free, or the feed turns into spam within a month.
- **Decorative stickers** — a fixed catalogue managed from the admin panel, free, for messages and chat.

### 9.3. Growth and retention (medium risk)
- **Local "flash" events** — temporary rooms around an event (concert, match, festival) with an extended TTL for its duration.
- **Neighbourhood streaks** — a light mechanic: a district with a consistently lively feed earns a "living place" status (no personal profiles).
- **Multilingual bridges** — there's already a 5% foreign-language mix + AI detection; add optional tap-to-translate for a truly cross-lingual feed.

### 9.4. Platform and scale (longer horizon)
- **New faces (storefronts)** for new regions/languages on the same gate — an Asian face, a Latin American face, etc.
- **Native apps** (iOS/Android) once the web alpha proves the model. Push notifications about "the ether is coming alive nearby" are a strong return trigger.
- **Events API/SDK** — an event organiser embeds a NEIGHBRO ephemeral feed into their own venue.
- **B2B "pop-up neighbourhood"** — coworkings, hotels, conferences, cruises spin up a private ephemeral feed for their guests.

### 9.5. Bold experiments (high risk, test carefully)
- **AI district companion** — a bot that ephemerally "warms up" an empty district with conversation starters (clearly labelled as AI).
- **Themed radii** — not just geo, but an "interest radius" layered on top of geo.
- **Ephemeral micro-meetups** — "who's nearby wants coffee in 20 minutes"; the assembled group dissolves after the meet.

---

## 10. Rough one-year roadmap

> Starting point: a working web alpha, live dev/uat, a separate prod in progress, waitlist landings and an admin-panel MVP. Dates are guidance, not commitment.

### Q1 — Alpha stabilisation and private launch
- Bring NEIGHBRO's prod deploy to production-grade (DNS/SSL/email already partly ready).
- Close the waitlist funnel: invite emails, wave-based invites.
- Polish the core: feed, posting, match, chat, disappearance, support.
- Finish the admin panel: reports, bans, quotas in one place.
- Baseline analytics: activation, D1/D7 retention, "like → chat" conversion.
- **Goal:** a stable private alpha with real users in 2–3 pilot cities.

### Q2 — Open beta and a livelier feed
- Public launch of NEIGHBRO (drop the waitlist gate).
- Reactions, mood tags, "pulse of the place" — enliven the empty feed in smaller towns.
- Better chat (typing/read/reactions).
- Stickers from the admin-panel catalogue.
- A/B on message TTL, default radius, foreign-language share.
- **Goal:** a self-sustaining live feed in at least a few dense locations.

### Q3 — Local reach
- Neighbourhood offers — a pilot with a local business.
- "Flash" events (concerts/festivals) with extended TTL.
- Optional tap-to-translate — a genuinely cross-lingual feed.
- **Goal:** a proven free-offer model, growth via events.

### Q4 — Native apps and platform scale
- Native iOS/Android (web model proven) with push about nearby surges.
- Prepare a new face for a new region/language on the same gate.
- B2B pop-up neighbourhood (pilot: hotel/coworking/conference).
- Harden infrastructure for scale: moderation scaling, anti-spam, observability.
- **Goal:** native reach, a proven B2B channel, readiness to onboard new faces.

### Cross-cutting all year
- Continuous moderation tuning (balancing safety against feed liveliness).
- Legal support as new countries come online (GDPR — critical for a European face).
- Anti-abuse iterations (quotas, fingerprint, rate limits).
- Sync with sosed.place: shared features land in the shared backend; only tone/policy per face differs.

---

## 11. Risks and open questions

- **Cold start.** A hyperlocal product is dead without density. Hence the focus on dense pilot locations and "flash" events as an accelerant.
- **Moderation balance.** Too strict and the feed is sterile and boring; too loose and it drifts into toxicity / dating spam. Needs constant calibration.
- **Sustainability without revenue.** The platform deliberately takes no money: offers are free, there is no in-app balance, and the only money is voluntary donations. That shields ephemerality and privacy from the pressure of an ad model, but it also means infrastructure costs are covered by nothing, and growth runs into them.
- **Privacy vs. abuse.** The browser fingerprint is a trade-off: it enables anti-spam without real accounts, but must honestly stay protection, not surveillance.
- **Jurisdictions.** A European face → GDPR, age protection, local content requirements.

---

*This document describes NEIGHBRO as one face of the `xor.ad` platform. The full concept of the shared backend, architecture and moderation policy lives in [`xor.ad`](https://github.com/panov-id/xor.ad). The Russian-speaking sibling face is [`sosed.place`](https://github.com/panov-id/sosed.place).*
