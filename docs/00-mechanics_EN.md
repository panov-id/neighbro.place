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

**A chat is held up by what you write into it, and each side keeps its own
count.** Each person chooses how long **their own silence** may last before the
chat disappears for them — 10 minutes, 30 minutes, an hour, or "while we're
talking" — and that time runs from their own last message, not from anyone
else's.

Petya set ten minutes, Kolya two hours. Petya says nothing for ten minutes and the
chat is gone **for Petya**. Kolya says nothing for two hours and it is gone for
Kolya. The same conversation lives differently for the two of them, and that is
the design rather than a fault.

**Nobody's setting decides anything for you.** The other person can neither
extend nor shorten your chat; they govern their own side only. Which answers the
question that used to stand open here: shortening never applies retroactively to
anyone, because there is nothing of anyone else's to change.

**Reading is not speaking.** Only your own message resets your timer. Someone who
reads in silence for an hour loses the chat exactly as if they had left: it lives
on conversation, not on presence.

**"While we're talking" is the longest silence, not forever:** four hours and
twenty minutes, exactly as long as a message lives in the feed. A chat that began
from a message should not outlive it by much. Nothing in the product is
open-ended.

**The default is an hour.** It is not the most private of the four, and it is
chosen deliberately: someone who has not yet learned the rules should not lose
their very first exchange halfway through.

**Your own count is visible, the other's is not.** A chat always shows how much
is left **for you**: it is your setting and your last message, and there is
nothing to hide there. Of the other person neither the setting nor the number is
shown — only the fading of the last minutes, that is, "about to go". Knowing that
it is time to answer is necessary; reading someone's character off the length
they chose is not.

**When the chat has ended for the other person, one line says so.** Otherwise an
expired timer is indistinguishable from a snub: one falls silent and the other
believes they are being ignored. One line removes the misunderstanding and gives
away nothing beyond the fact.

**A chat that has ended cannot be written into.** If it is gone for Petya, Kolya
sees that and spends no words: nothing goes into the void. And nothing reaches
Petya — what disappeared is not revived by someone else's activity.

**The ending is announced in advance.** For its last minutes a message or a chat is
shown fading: you can see it going, and there is time to answer. The disappearance
itself is silent — no headstones, because what was promised is that nothing stays.

### Open

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

**A report does not touch the quota.** It does two things: it removes the message
from the feed for the person who reported it, and it adds one to that message's
report counter. For everyone else the message stays **while the counter is under
the threshold** — the whole rule is in §5.

**Blocking is what cuts the quota** — and only blocking. Whoever blocked stops
seeing that author, and the author's ceiling drops: while the block holds, they
have fewer than five messages alive at once.

**A message refused by moderation takes no slot — until the third one.** A message
that did not pass the filter never reached the feed, so it has nothing to occupy:
the first two refusals in a day cost nothing, the text is edited and sent again.
From the third refusal in that same day the ceiling drops by one until the day
ends. You may be wrong for free twice; tuning your wording against the filter, no.

**An offer does not take a slot.** Neighbourhood offers have their own quota — a system limit
on their share of the feed and a frequency cap per business (specification in
`xor.ad/docs/offers/`). Five live messages is about being a neighbour, and the owner of the
bakery stays a neighbour with their five even while an offer of theirs is up.

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

- **Rudeness** — a toxicity classifier. Fails, and it is not published.
- **Hazard** — threats, hostility towards a group, dealing in what is forbidden,
  approaching minors. Rejected outright.
- **Explicitness** — explicit content is invisible by default and is opened by a
  separate consent with an email (screen 11).

**The check runs on our own node, and the text does not leave it.** Nothing is
forwarded to Perspective, to somebody else's language model, or to any other
processor — so the privacy policy carries no line about moderation as a recipient
of data, there is no processing agreement to sign and no transfer abroad arises.
Perspective, which this used to be built on, is also closing on 2026-12-31.

**Naming a group does not make a message rude.** Rudeness is judged on the text
with the group's name — "gay", "Muslim", "migrant", "disabled" — replaced by an
ordinary word. So "our speakers are here and we're ready to start #gay20" goes
through: without the group's name there is nothing left in that sentence.

This is not a courtesy but the same line the section opens with. A classifier
trained on ordinary data judges such messages more harshly by itself — measured:
the word "gay" raised a score to 0.29 against 0.001 for a neutral word in the same
sentence, 457 times higher. A model trained specifically against that bias scored
0.288, so retraining does not cure it. Classifying nothing, formally, the service
would still block those messages more often — which is exactly the effect topic
classification was removed to avoid.

**An attack on a group is judged on the original.** The substitution erases the
attack along with the trigger: "gays should not be allowed near our children"
stops being anything at all once "gays" is gone. So hostility towards a group is
judged by a separate label on the unchanged text, at a threshold **above anything
neutral sentences reach and below anything real attacks reach**.

Measured on the probe sets: of 60 neutral sentences naming a group, **none** is
blocked; of 5 attacks, **all five** are.

**There is no topic classification.** The "LGBT-related" label has been removed
from the classifier along with the filtering that used it: it inferred an author's
orientation, which is special-category data and cannot be processed by default. It
is gone from screen 4 in both storefronts and from neighbro's overview.

**The label is not stored.** Classification happens as the message is sent, decides
the outcome, and is not written down beside it.

**A chat is not checked at all.** Neither for toxicity nor for explicitness: what
is written inside a chat is checked by nothing at all and never
leaves the pair of devices. Moderation governs what is published to the feed, where
strangers see it; two people talking is not publication.

**Ordinary messages carry no links.** Not in the feed, not in a chat: a link is stripped and
the person is told so. The single place a link is allowed is a neighbourhood offer, and there
it goes through our own redirect, which can be killed (specification in
`xor.ad/docs/offers/`). The reason is plain: without that rule the feed turns into spam within
a month, and there is nothing to check every link with.

**Captcha and rate limit are feed-only too.** Cloudflare Turnstile and the Bunny
Shield IP limit govern publishing.

**A refusal is explained.** If a message is not published, the person is told, and
told why. That is not politeness but a requirement for platforms carrying
user-generated content.

### A report

**A report is a vote against showing a message, not a verdict.** Whoever reports
stops seeing the message at once, with no hearing and no waiting. At the same
time their report adds **one to that message's counter**.

**When the counter reaches the threshold, the message leaves the feed for
everyone.** The threshold is not a number but a **share of how many people could
have seen the message at all**: of those whose zone it fell into. Otherwise one
rule would mean different things in different places — five in a village is
nearly everybody, five in a city is nobody.

The denominator is the message's possible audience rather than the whole
district: everyone picks their own zone (§4), so two messages from the same spot
have different audiences, and their thresholds honestly differ.

The share and the floor are configurable. The starting values are **5% of the
audience, but never fewer than three people**. The floor is not optional: without
it the share rounds down to one in a small zone, and a single person starts
deciding for everyone.

**People are counted, not taps.** Five reports from one person are one report.

**A report from someone the author has blocked does not count.** Blocking parts
the two of them completely: a private feud does not turn into votes against the
feed. The price is stated plainly: it takes a voice away from whoever is being
harassed — they can block everyone able to report them and keep writing. What
works against that is other people's reports, and hazards, which are caught
before publication.

**Hiding does not touch the author's ceiling.** In neither direction: the slot
stays taken until the message's time runs out (§3), and the number of messages
they may keep alive does not drop. There is one punishment — the message is not
seen — and it does not accumulate. Otherwise
hiding would work as a gift: the more you are reported, the sooner you are free to
write again.

**The author is told the message was hidden, and why.** Same rule as §10: a
refusal names its cause. Hiding by report is not a secret measure.

**A report re-checks nothing.** It sends the text to no model: the check happened
before publication, and a report is the opinion of people, not a second run of a
machine.

### Open

- The wording of the refusals is unwritten. There need to be as many as there are
  classes of refusal.
- **There is no appeal** — settled. A refusal is final; the text is edited and
  sent again. The price is measured and stated plainly: about 7% of ordinary
  messages are blocked for nothing, and their authors have nowhere to go. What
  softens it is that a refusal names its cause (§10) and that the text is not
  lost.
- Whether chat messages are checked as strictly as feed messages — the documents
  say "the same" but without the captcha; whether to soften the rest is undecided.
- **The machine catches about half.** Measured on human-labelled data across nine
  languages: 0.55 of what people call offensive is caught, and 0.07 of ordinary
  messages are blocked for nothing. Reports take the other half — without them
  moderation does not work, and they are part of it rather than an addition to it.
- The gap the group-attack threshold sits in is **narrow**: 0.53 against 0.77 on
  the probe sets. On live data it may narrow further — measure again.
- The list of group names is **English only**, because the decision is made by the
  arm that reads the translation. If the original-text arm ever decides, the list
  is needed per language.
- For eight languages (az, be, hy, ka, kk, ky, tg, uz) there is no public labelled
  data at all: quality there is unmeasured, and cannot be measured until reports
  arrive.
- The German set, the only one available, is labelled on political tweets rather
  than neighbourhood talk. Its 0.26 measures a mismatch of tasks, not the work of
  moderation.
- Whether reports count from people the author has blocked — otherwise blocking
  protects nobody, and a feud between two turns into five votes.
- Whether hiding lowers the author's ceiling the way blocking does (§3).
- What to do with reports arriving on a message that is already hidden.
**Settled, so it is not raised again:** there are no help contacts here and there
will not be — the Service is not about that. A message saying someone feels bad
passes as any other does: it endangers nobody, and there is nothing to erase it
for.

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

Feed message text goes nowhere: moderation runs on our own node (§5). IPs go to
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
| business profile: email, name, address, status | server | not to post an envelope again | **a year from the last offer**, then deleted along with the complaints about it |
| a complaint about an offer | server | to tell whether complaints are systematic | as long as the profile |
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
- How long a report waits "until reviewed" if no review happens.
- Backups: if they exist, everything we deleted lives on inside them. Their
  lifetime is undecided.

---

## 8. Language

In a seaside district the neighbours speak different languages, and that is not
an obstacle but a condition of the problem. The rule is simple: **by default a
person sees the feed in their own language, but the district is not hidden from
them**.

**Up to three languages may be chosen.** The default comes from the browser —
`navigator.languages`, a value from the narrow set in §1, so there is nothing to ask
separately — but the person edits the list themselves. The automatic guess knows the language
of the system, not the language someone writes in: the phone is in English, they write in
Russian.

Three, rather than one or all: in Cyprus the real set is Greek, English and Russian — exactly
three. One makes half the district invisible, and with no cap the filter stops filtering,
though filtering is the whole reason it exists.

**A message's language is decided by the node** — with a local library, at home,
without calling any outside service. No text leaves us in order to be
classified, and nobody bills us per message for it. The detected language is
kept with the message (§7) and serves only as a filter.

**The filter sits in the feed header and comes off with one tap.** Under a
filtered feed there is always a line: "another N messages in other languages —
show". That line matters: a person always knows the district is livelier than
their feed, and never mistakes the silence of a filter for the silence of the
district. With the filter off they see everything, each message carrying a
language tag.

**Interface language and feed language are different things.** The first decides
what the labels say; the second decides whose messages are shown. Someone who
reads Greek but keeps their phone in English should not lose their neighbours
over it.

**The language filter does not hide an offer.** Neighbourhood offers are shown whatever the
language: the Greek bakery across the road is just as useful to a Russian-speaking neighbour.
It is the only exception to the filter, and it is named plainly so it does not look like an
oversight.

**We do not translate.** Translation would mean a neighbour's text going to an
outside translator: one more processor in the policy, one more agreement, and
one more place where other people's words sit with a third party. For a product
that promises nothing is left behind, that is a bad trade. If translation ever
appears, it appears as a deliberate change of policy, not as a convenient
button.

### Which way the writing runs

Arabic, Hebrew, Persian and Urdu run right to left. None of the declared
languages does — but people write in whatever they write in, and one such message
will land in a feed where everything else runs left to right.

**Direction is a property of the message, not of the page.** We already detect a
message's language (above), direction follows from it, and it costs no extra
work. A single Arabic message in a Greek feed lays itself out right to left
without asking anything of the rest of the page.

**One message does not mirror the layout.** Which side a chat bubble sits on
means who is speaking, not which way the text runs: an Arabic speaker's bubble
stays where it was, and only the text inside aligns right. The whole layout
mirrors when the **interface** runs right to left, not when one line does.

**We have no right-to-left interface.** Not one of the seventeen declared
languages is written that way, so there is nothing to mirror the interface for.
That is a decision rather than an omission: add such a language to the list and
the mirrored layout comes with it.

**Mixed direction inside one phrase** — a Latin word in an Arabic line, a house
number, a time — needs isolating. Without it the punctuation jumps to the
opposite end of the line and the phrase reads as broken.

### Open

- Browser language is not the language a person writes in. Some keep the system
  in English and write in Russian. Whether a manual feed-language choice is
  needed alongside the automatic one is undecided.
- What to do when detection is unsure: a short "ok" or "👍" has no language at
  all. Whether to show those to everyone or hide them is undecided.
- The "another N in other languages" counter reveals district activity to
  someone who has published nothing. Whether we count that as a leak is
  undecided.

---

## 9. What stays on the device

Identity lives in the browser (§1), so the browser has to remember something.
The rule: **the device holds exactly what the product cannot work without, and
holds it for the same periods as the server**.

**What stays:**

| What | Where | Until when |
|---|---|---|
| the encrypted UID | local storage | until the person clears the browser |
| settings: conversation lifetime, language filter, zone | local storage | same |
| the consent choice and its date | local storage | same — it is the proof of consent |
| conversations: messages, times, status | IndexedDB, encrypted with Web Crypto | until the conversation expires (§2) |

**A conversation is erased on the device by the same rule as on the server** — by
your own silence (§2). Not "at roughly the same time", but by the same number.
Here it shows most plainly: for the other person the chat may still be alive at
that moment, because their count is their own. The timer fires even when the app is closed: the next time it
opens, the first thing it does is erase everything that expired, before anything
is shown.

**The feed does not settle on the device.** It arrives from the server and lives
in the tab's memory. Otherwise someone else's message would outlive its 4:20 on
my phone — and that is precisely the promise the product makes to its author.

**Clearing the browser destroys the identity for good.** There is nothing to
restore it with: no email, no password, no code — by the design in §1 there
should not be. This has to be said plainly at sign-up, not discovered later. The
pleasant converse follows from the same fact: **the "delete everything" button
really does delete everything**, immediately, with no letters and no
confirmations.

### Open

- Where the conversation encryption key is kept and what protects it. If it sits
  next to the data in the same store, encryption defends against a look in the
  debugger but not against whoever is holding the phone.
- The browser may evict IndexedDB on its own when space runs out. The
  conversation would vanish early — whether that counts as normal behaviour or
  deserves a warning.
- Several tabs at once: whose timer is authoritative and how they agree.
- Whether an explicit "forget this device" is needed separately from "delete
  everything".

---

## 10. Refusals

The app regularly cannot do what is asked: the quota ran out, moderation did not
pass it, there is no network, the conversation expired. One rule: **a refusal
names its cause and the nearest action**. Nobody should have to guess what
happened or what to do about it.

| Refusal | What is said | What next |
|---|---|---|
| quota (§3) | all five slots are taken, when the next one frees | wait, or take one down |
| moderation (§5) | what exactly did not pass | edit the text and send again |
| no network | there is no connection, what you wrote is kept | retry when there is |
| conversation expired (§2) | the time ran out, the exchange is gone | go back to the feed |

**What was written is not lost to a refusal.** The text stays in the field: a
person spent time on it, and a refusal is no reason to take that work away. This
matters most for a moderation refusal, after which the text is meant to be
edited rather than retyped.

**A moderation refusal names its cause** — insult, threat, advertising spam —
and we knowingly pay for that by hinting at how to get around the filter. The
trade is fair: there are many people who simply put something bluntly and would
not understand a bare refusal, and few who tune their wording against the
filter, and those are caught by a report anyway (§5).

**A refusal is not an error.** "The quota ran out" is a rule working correctly,
not a breakage. A breakage looks different and speaks differently: "that did not
work on our side, try again". These two tones must never be mixed, or the design
of the product reads as a malfunction.

### Open

- Whether a moderation refusal can be appealed, and where that goes.
- The exact wordings are not written. They belong to the UX layer; only the rule
  belongs here.
- How specific the moderation cause is: a category ("this reads as an insult")
  or a pointer at the actual word.
