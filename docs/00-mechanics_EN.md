# Mechanics

The rules every screen shares. The screen documents point here and do not repeat
what is written here: if a rule shows up on two screens, it belongs in this file.

This document is the single source of the rules. The screens used to point at
"Moderation" and "Privacy" sections of the README, which do not exist there; those
references now lead here.

Read alongside:

- [`01`…`17`](./) — the screens: what is on each and what it offers.
- [`../design/interface/`](../design/interface/) — the same screens, drawn.

---

## 1. Who a person is

A person here is an **encrypted UID** the server mints at the end of signing up.
It is made of three things: the year of birth, the name that was typed, and the
browser's fingerprint. No email, no phone, no password; there is nowhere to sign
in because there is nowhere to sign out of.

The fingerprint is not there to prevent forgery — it is what ties the identity
down. It means the identity lives **in this browser on this device** and nowhere
else. Another browser, another device, a private window: that is a different
person from scratch, with their own quota, their own feed, and none of the chats.

Which leads to the part that has to be said out loud, because otherwise a person
finds it out for themselves and at the wrong moment:

- **Clearing the site's data erases the identity.** Not "signs you out" — erases.
  There is nothing to restore: the server knows the UID and not who it belonged to.
- **There is no way to carry it over.** No code, no link, no export. Chats that ran
  in the old browser are gone from the new one for good — they stay with the other
  person, and not with you.
- **A private window is always a new person.** Every private window mints an
  identity and loses it when the window closes.

**This has to be said before the button is pressed**, not after. The wording and
its place belong to screen 2, where signing up ends; what is fixed here is only the
requirement: the product must warn that the identity is tied to this browser and
that it cannot be moved.

The other side of that tie is what it is for. There is no account, so there is
nothing to breach, nothing to sell and nothing to hand over on request: the link
between a person and their messages ends at a browser fingerprint that is never
sent anywhere in its original form.

### Consent

Signing up ends with two lines, and they are **two separate decisions**, not one.

**The terms and the rules — required.** There is no continuing without accepting
them: that is the contract everything else rests on.

**The wider fingerprint — optional.** A separate box, unticked by default. Tick it
and the identity is assembled from more signals and holds on to the browser more
firmly. Leave it and **everything works exactly the same**: the feed, the chats,
the quota, publishing. One thing is weaker: the UID falls off more often when the
browser updates or the window changes, and then a person becomes a new person by
the rules above.

**What goes into each set.**

| | Signals |
|---|---|
| **narrow** — no box | year of birth, name, user agent, browser language, time zone |
| **wider** — with the box | the same plus four: the WebGL renderer, the core count, the memory size, the screen's pixel density |

Four of them, not "additional device information": the consent names them one by
one, or it is about nothing. All four change rarely and are read in a single call —
no canvas drawing and no font enumeration here.

Some browsers withhold or fake these: Firefox and Safari hide the memory size and
mask the renderer. There the wider set adds less and the identity holds worse — not
a fault, but a consequence of which browser someone chose.

The split is not a formality. Consent you are not let in without is not consent but
a condition of entry, and in Europe it does not count: it has to be informed,
separate and refusable. One box for everything would be simpler on the screen and
worse in every other way.

The same decision closes a question screen 15 left open: **an explicit consent at
signup is needed**, and this is its shape.

> Where the legal line falls — what exactly belongs in the "wider" set, and whether
> this wording carries it — is worth checking before launch, not after.

### Open

- How well the narrow fingerprint survives a browser update has not been measured.
  That is settled by trying it, not by reasoning about it.
- Whether the warning is shown once at signup or stays reachable afterwards — in
  settings, say — is undecided.

---

## 2. Time

Everything here ends by itself. What separates the feed from a chat is **who
decides when**.

**A message in the feed lives 4 hours and 20 minutes** from the moment it is
published. Nothing extends it: not a like, not a reply, not the fact that someone
is reading it right now. Its author can take it down early by hand (screen 9), but
cannot keep it up any longer.

**A chat lives as long as whichever of the two set the shorter time.** Each side
picks how long until the chat is deleted — 10 minutes, 30 minutes, an hour, or
never — and the **shorter** of the two applies. Neither can extend the chat on the
other's behalf: the other person's setting is a ceiling you may go under and may
not go over.

The setting is changed **during the conversation**, not only at its start. Either
side can shorten it at any moment, and it shortens at once, for both.

**The ending is announced in advance.** For its last minutes a message or a chat is
shown fading: you can see it going, and there is time to answer. The disappearance
itself is silent — no headstones, because what was promised is that nothing stays.

### Open

- **"Never" argues with the promise.** If both sides pick never, the chat does not
  end at all — and this product is built on everything melting. Whether that stays
  or "never" becomes a long finite value is undecided.
- Whether shortening applies retroactively: if the other person sets 10 minutes in
  a chat that has been running for three hours, does everything older than ten
  minutes go — or does the rule only govern what comes next.
- The default value is undecided.
- Whether the other side is told that the timer changed, and how, is undecided.
- How long before the end the fading starts is undecided. It may differ between a
  message and a chat.

---

## 3. The quota

**The quota is five messages alive at once, not five a day.** It says how much of
yours is standing in the feed right now.

A slot frees the moment a message goes, and it does not matter how it went:

- its 4:20 ran out;
- you took it down by hand on screen 9.

The second is immediate: delete, and the slot is free that instant, and you can
write again. The delete key does not punish, it makes room; otherwise changing
your mind would cost you the chance to say it differently.

While all five are taken, publishing is unavailable. That is not a refusal and not
an error — it is a feed full of your own messages, and there are two ways out:
wait, or take one down.

**A report does not touch the quota.** It does two things: it flags the message for
moderation, and it removes it from the feed for the person who reported it. For
everyone else the message stays.

**Blocking is what cuts the quota** — and only blocking. Whoever blocked stops
seeing that author, and the author's ceiling drops: while the block holds, they
have fewer than five messages alive at once.

> **Contradiction.** Screen 5 currently says a report lowers the quota too. The
> rule above overrides that; the screen 5 document needs bringing into line.

### Open

- How far a block lowers the ceiling, and for how long, is undecided.
- Whether blocks from different people stack, and whether there is a floor the
  ceiling never goes below, is undecided.
- Whether the author sees that their ceiling has dropped, and knows why, is
  undecided.

---

## 4. Place

Place is set **twice here, and differently each time**. The two knobs are easy to
confuse because both are about distance, so they are pulled apart here.

**The viewing radius** is the reader's knob, on screen 3. A circle on a map that a
person stretches with a slider: "show me what is near me." It decides what reaches
the feed.

**The blur radius** is the author's knob, on screen 4, at every publication. A
message is tied not to exact coordinates but to a **zone around them**, and the
slider says how much larger than a point that zone is. It exists for one reason:
so that a couple of messages cannot lead anyone to a doorway.

Blur **does not decide who sees**. Visibility is decided by the other person's
viewing radius: a message shows up for those whose circle caught your zone. The
author governs how precise their own mark is, the reader governs how wide their own
feed is, and those two decisions are made by different people.

**No location permission is asked for on arrival.** The first point is worked
out from indirect signals, and that is enough for the feed to open at once. A
person asks for a real fix themselves, with a button, when they want one — how,
below.

### Where the first point comes from

First, **without asking for anything**, out of what the browser and the network
hand over by themselves:

| Signal | What it gives | What it is worth |
|---|---|---|
| the time zone, `Europe/Berlin` | a region | the steadiest of the three: a VPN does not change it unless someone changed it by hand |
| the IP, server-side | country, region, often a city | a city at best; VPNs, mobile carriers and shared addresses get it wrong routinely |
| the language, `navigator.languages` | country and language variant | confirms or contradicts the other two |

The zone gives the region, the IP narrows it to a city, the language checks both.
**A zone and an IP that disagree are themselves a signal**: that is almost always a
VPN, and it means the IP cannot be trusted.

**A point obtained this way is called approximate, and it looks it.** It is labelled
as a guess, and the default circle is drawn **wider** than it would be for a real
fix. A person has to see the difference between "we worked it out" and "we measured
you" — otherwise they either decide they were tracked, or trust a circle that is a
kilometre off.

**A "where am I" button** asks for precise location — on request, not on arrival.
Press it and the circle lands for real and the "approximate" label goes. Leave it
and everything works on the guess. The permission is asked **for one point**, not
for tracking: position is not read in the background and does not refresh itself.

Refusing breaks nothing: the approximate point remains, and so does the hand-placed
one.

### What else is read without asking

Not to recognise a person, but to avoid asking questions the browser has already
answered:

- `prefers-color-scheme` — the theme is right immediately, with no flash and no
  toggle-hunting on the first visit.
- `prefers-reduced-motion` — fades and the splash animation switch off for people
  they make ill.
- `pointer` and `hover` — a finger or a mouse; swipe or hover depends on it.
- screen size, pixel density, window size — layout, and which images to fetch.
- `navigator.connection` — how good the network is and whether to fetch the heavy
  things. Chromium only, so a hint and nothing more.
- `storage.estimate` — how much room there is for chat history in IndexedDB.
- `onLine` — whether there is a network right now.

**What we do not read by default.** WebGL, canvas, the font list, core count,
memory size — all available without permission, all of it makes a UID steadier.
Without the box ticked at signup (§1) we do not take it.

The line falls exactly along purpose. Everything above is read **so as not to
ask** — to place a circle, to guess the theme, to pick a layout. The wider set is
read **in order to recognise**, and so it is asked for separately, unticked by
default, and used for nothing but holding an identity together. It does not reach
analytics, feed ranking or advertising.

> **Legal.** Reading any of the above is harmless on its own, but assembling
> signals into a stable identifier is profiling, and in Europe that needs consent.
> It is asked for at signup (§1). What exactly belongs in the wider set has to be
> listed before the consent can be worded.

### Open

- The defaults and bounds of both knobs are undecided: neither the viewing radius
  nor the amount of blur.
- **How a zone meets a circle** is undecided. Does a message reach the feed when
  its zone sits entirely inside the reader's circle, or is overlap enough? The
  answer decides what someone at the edge sees: on overlap a heavily blurred
  message reaches almost everyone, on containment almost nobody.
- Whether a hand-placed or a measured point is remembered between visits is
  undecided.
- What happens when a person has physically moved and the point has not is
  undecided. An approximate point recomputes itself; a measured one does not.
- How much wider the default circle is for an approximate point is undecided. That
  needs a number, not the word "wider".

---

## 5. Moderation

What is judged is **the behaviour of a message, not the belonging of its author**.
That is a position, and it is also a legal line: inferring which group a person
belongs to is special-category data, while inferring whether a text is abusive is
not.

Every message is checked **before it is published**:

- **Toxicity** — Google Perspective API. Fails, and it is not published.
- **Explicitness** — an LLM classification. Explicit content is invisible by
  default and is opened by a separate consent with an email (screen 11).
- **Harassment, drugs, sex work** — rejected outright.

**There is no topic classification.** The "LGBT-related" label has been removed
from the classifier along with the filtering that used it: it inferred an author's
orientation, which is special-category data and cannot be processed by default. It
is gone from screen 4 in both storefronts and from neighbro's overview.

**The label is not stored.** Classification happens as the message is sent, decides
the outcome, and is not written down beside it.

**A chat is not checked at all.** Neither for toxicity nor for explicitness: what
is written inside a chat goes to neither Perspective nor a language model and never
leaves the pair of devices. Moderation governs what is published to the feed, where
strangers see it; two people talking is not publication.

**Captcha and rate limit are feed-only too.** Cloudflare Turnstile and the Bunny
Shield IP limit govern publishing.

**A refusal is explained.** If a message is not published, the person is told, and
told why. That is not politeness but a requirement for platforms carrying
user-generated content.

### Open

- The wording of the refusals is unwritten. There need to be as many as there are
  classes of refusal.
- Whether a decision can be appealed is undecided.
- Whether chat messages are checked as strictly as feed messages — the documents
  say "the same" but without the captcha; whether to soften the rest is undecided.

---

## 6. Legal bases and risks

A map: what we do, on what basis, and where it is thin.

### What the processing rests on

| What | Basis |
|---|---|
| identity, feed, chats, publishing | contract — the person asked for the service |
| the narrow fingerprint, IndexedDB writes | necessary for the service requested |
| **the wider fingerprint** | **consent**, its own box (§1) |
| explicit content | a separate consent with an email (screen 11) |
| captcha and rate limit | legitimate interest — abuse prevention |

### Where data goes

Message text goes to Google Perspective and to an LLM provider. IPs go to
Cloudflare Turnstile and Bunny Shield. Storage is our own Postgres beside the node
and Bunny object storage. **Chat text does not leave**: that was the most
sensitive transfer, and now there is none.

Each recipient needs a processing agreement, a lawful transfer route out of the EU,
and a mention in the privacy notice. Our database sits beside the node, so where it
lives is where the node lives — and that is our choice to make.

### What is missing

- **There is no privacy notice at all.** It needs: who the controller is, what for,
  on what basis, who receives it, how long it is kept, what rights there are.
- **There is no list of what the wider fingerprint contains** — without it the
  consent is about nothing.
- **There is no EU representative**, and one is required where the operator is
  outside the EU and the people are inside it.
- **No record of processing and no impact assessment.** Location plus automated
  moderation plus possible minors is the usual reason to run one.
- **Age and consent.** The age at which a person may consent for themselves ranges
  from 13 to 16 across the EU. The simplest course is not to offer the wider
  fingerprint to anyone whose stated age is below the threshold.

### What already counts in our favour

There are no accounts, so there is nothing to leak and nothing to hand over.
Everything expires by itself, so the retention policy is written by the product.
Coordinates are blurred by design. Consent is split into the required and the
optional, and refusing the optional breaks nothing. Topic classification is gone.

---

## 7. What is kept, for how long, and why

Two clocks are easy to confuse, so they are pulled apart: **the product's clock** —
how long a thing is visible to a person; and **the system's clock** — how long it
sits in storage. Where they disagree, the promise that everything melts becomes
untrue, and here they do not disagree anywhere except where it says so.

### The product

| What | Where | Why | How long |
|---|---|---|---|
| a feed message: text, zone, people count, language | server | to show the feed | **4:20, then deleted outright** — not hidden, erased |
| the "how many there were" counter | server | statistics | indefinitely, **without text and without author** |
| chat messages | **the device**, IndexedDB, Web Crypto | the conversation | the shorter of the two settings (§2) |
| chat in transit | server | delivery | **not stored**; if the other side is offline, until delivered or until the chat's life ends, whichever comes first |
| likes and matches | server | to open a chat | as long as the chat lives |
| reports and blocks | server | moderation and personal hiding | a block while it holds; a report until it is reviewed |
| the quota | server | the limit | derived from live messages, not stored separately |
| identity: the UID | server | recognition between visits | until the browser is lost |
| year of birth, name | server, inside the UID | age separation, a byline | with the identity |
| consent to the wider fingerprint | server | to prove it was asked for | with the identity |
| email and consent for explicit content | server | to open explicit content | with the identity |
| the link to you | server | to share inside a chat | with the identity |
| a support message | our own database | to answer and investigate | 1 year |

### The storefront and the plumbing

| What | Where | Why | How long |
|---|---|---|---|
| a waitlist email | Bunny Storage | to invite at launch | **until launch plus a year**, then deleted |
| a page view: path, language, referrer host, viewport | Bunny Storage | to know what is read | **14 days**, pruned daily |
| the daily view counter | database | "how many" | indefinitely, **without the detail** |
| the audit log: who changed what in the panel | database | settling disputes, and our own protection | **1 year** |
| server logs | the node | incident review | **30 days** |
| client errors | Bunny Storage | incident review | **30 days** |
| panel users: email, role | database | access | while the access exists |

### Rules, not only durations

**Personal data is not written to logs.** Not an email, not a message, not a UID.
Logs exist to explain a breakage and outlive everything else — so what we promised
not to keep must not land in them.

> **Found, and needs fixing.** In `relay/node/src/routes/waitlist.ts`, when storage
> is disabled the email is written to the log: `log("error", …, { email })`. That is
> exactly the case — data going where it lives longer and by other rules.

**What is left when a person loses their identity.** Nothing that could be given
back to them. Messages expire by themselves, chats lived on their device, the UID
is on the server but tied to nothing that identifies anyone. It cannot be restored
not out of strictness but because there is nothing to restore it from.

**Who does the deleting.** Every duration needs a doer — a job, not an intention.
Today there are two: the page-view prune and message expiry. The other durations
have no doer yet.

### Open

- The pruning jobs for the waitlist, the logs, the client errors and the audit log
  are unwritten. A duration without a job is not a duration.
- Whether Perspective and the LLM provider keep the texts we send them, and for how
  long, needs finding out and writing down here.
- How long a report waits "until reviewed" if no review happens.
- Backups: if they exist, everything we deleted lives on inside them. Their
  lifetime is undecided.
