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

A person here is a **key pair created on the device**, plus an identifier the
node mints at the end of signing up. The node keeps only the public half: it holds
no password and no secret, so a leaked database cannot be used to impersonate
anyone. No email, no phone, no password; there is nowhere to sign in because there
is nowhere to sign out of.

**A six-digit PIN is asked for right away, at signup.** It does two things: it
locks an open tab against whoever picks the device up, and it takes part in
encrypting everything on disk — the vault key is assembled from the PIN and a
share the node holds and hands over only after checking it. It cannot be deferred,
and the reason is the terminal: `depth` writes the key file immediately, and a
deferred PIN would mean keys lying on disk in the open (`xor.ad/docs/chat_EN.md`
§8.2).

**An identity has exactly one live session.** That is not "one device forever":
an identity **moves** — the previous device goes still, its conversations stay on
disk encrypted, and they come back with the identity if it is brought back. What
does not happen is one identity living on a phone and a laptop at once: two
devices are two neighbours. That is deliberate, because the key of each chat lives
on the device and cannot be handed to all of them at once.

**The paper code is issued at signup — settled 2026-08-26.** It had stood at the
opening of the first chat since 2026-08-18, on the argument that before that chat
there is nothing to insure. The argument holds for property and fails for identity.
The cost of being wrong is asymmetric: a person the screen failed to convince, who
walked away, comes back a day later and carries on; a person who lost their device
inside the uninsured window never comes back — there is nothing to present. So the
weight sits on the explanation rather than on the moment: the screen must say that
there is no email and no password, that we cannot look the code up, and that losing
the device without it means losing the identity. The code is the only way back,
shown once and confirmed by typing two groups.

Which leads to the part that has to be said out loud, because otherwise a person
finds it out for themselves and at the wrong moment:

- **Clearing the site's data erases this session and the conversations.** The
  identity comes back with the paper code; the conversations do not — they exist
  neither with us nor anywhere else.
- **A private window is always a new person.** Every private window mints an
  identity and loses it when the window closes.
- **Recovery puts out the previous session and burns the previous code.** People
  recover when something has gone wrong — including when the paper may have been
  seen.

**This has to be said before the button is pressed**, not after. The wording and
its place belong to screen 2, where signing up ends; what is fixed here is only
the requirement: the product must explain that the identity lives on this device,
what brings it back, and from what moment.

The other side of that is what it is for. There is no account, so there is
nothing to breach, nothing to sell and nothing to hand over on request. The
conversations themselves are encrypted on the devices: the server carries them
and cannot read them.

### Consent

Signing up ends with two lines, and they are **two separate decisions**, not one.

**The terms and the rules — required.** There is no continuing without accepting
them: that is the contract everything else rests on.

There is no second box any more. It used to be the consent for a wider
fingerprint — WebGL renderer, processor cores, memory size, pixel density — by
which the identity held on to the browser more firmly. It went with the
fingerprint itself: offering a box for collection that does not happen is worse
than offering nothing.


### Open

- How long a device-connection invite should live, and how the list of one's own devices
  is shown, is undecided.
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

**Blocking does not touch the ceiling — settled 2026-08-26.** Whoever blocked
stops seeing that author, and that is all it does. Cutting someone's quota with one
tap would let a single person quietly narrow another's voice — and the author would
never learn of it. Against real harm there are reports (§5) and the fact that the
dangerous is caught before publication.

**A message waiting on its name takes no slot and blocks the next one.** The
first publication goes into the queue together with the name and appears in the feed
only when both are accepted (§5). While it waits it is not in the feed, so there is
nothing to occupy; but the next one cannot be sent either, or waiting would stack a
queue around the ceiling. This happens once: the name is checked at the first
publication and at every change, and changing it requires a clean slate.

**A message refused by moderation takes no slot — until the third one.** A message
that did not pass the filter never reached the feed, so it has nothing to occupy:
the first two refusals in a day cost nothing, the text is edited and sent again.
From the third refusal in that same day the ceiling drops by one until the day
ends. You may be wrong for free twice; tuning your wording against the filter, no.

**An offer does not take a slot.** Neighbourhood offers have their own quota — a system limit
on their share of the feed and a frequency cap per business (specification in
`xor.ad/docs/offers/`). Five live messages is about being a neighbour, and the owner of the
bakery stays a neighbour with their five even while an offer of theirs is up.

### Open

- ~~How far a block lowers the ceiling~~ — dropped 2026-08-26: it does not lower
  it at all, so the questions of its strength, of stacking and of telling the author
  are gone with it.
- Whether the author sees that a third refusal by moderation has dropped their
  ceiling, and knows why, is undecided. That is the only remaining way down.

---

## 4. Place

Place is set **twice here, and differently each time**. The two knobs are easy to
confuse because both are about distance, so they are pulled apart here.

**The viewing radius** is the reader's knob, on screen 3. A circle on a diagram (no face draws a map, 2026-08-28) that a
person stretches with a slider: "show me what is near me." It decides what reaches
the feed.

**The blur radius** is the author's knob, on screen 4, at every publication. A
message is tied not to exact coordinates but to a **zone around them**, and the
slider says how much larger than a point that zone is. It exists for one reason:
so that a couple of messages cannot lead anyone to a doorway.

Blur **does not decide who sees**. Visibility is decided by the other person's
viewing radius: a message shows up for those whose circle **overlaps** your zone —
touching is enough, it need not sit entirely inside (settled 2026-08-26). The
opposite rule would punish privacy with silence: the more someone blurred their
mark, the fewer people would hear them — and an empty feed kills the place faster
than one extra neighbour in the results. The author governs how precise their own
mark is, the reader governs how wide their own feed is, and those two decisions are
made by different people.

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

**There is no "where am I" button — decided 2026-08-28.** [retired] This used to read: a "where am I" button asks for precise location — on request, not on arrival. A precise position is **never** requested: the place is worked out from indirect signals and refined by hand on the diagram. A permission we never ask for is a permission that cannot leak, and declining to have the conversation removes a whole class of questions from the privacy policy.
Press it and the circle lands for real and the "approximate" label goes. Leave it
and everything works on the guess. The permission is asked **for one point**, not
for tracking: position is not read in the background and does not refresh itself.

Refusing breaks nothing: the approximate point remains, and so does the hand-placed
one.

### How many people are in there — in steps, not in numbers

**The radius handle says how many live phrases are inside the circle — settled
2026-08-26.** Without it the handle is dragged blind: a person does not know whether
to pull further and lands either in emptiness or in the next district. The number
used to be named in one place only — in an empty feed, when widening the circle was
offered; now it is always there.

The number is named as a **step**, not as an exact figure:

| Live phrases in the circle | What it says |
|---|---|
| 0 | nobody here yet |
| 1–4 | a few |
| 5–14 | about a dozen |
| 15–99 | dozens |
| 100 and more | hundreds |

The boundaries are written down here rather than left to whoever sits down to write
the code first: "roughly" with no numbers means five different roughlies across
three faces of the product.

**The node counts, and only once the handle is released.** The reason is not saving
requests. A counter tied to a radius is a measuring instrument: stepping the handle
from 500 m to 25 km and reading exact numbers, a person builds a density map of
their surroundings, and by catching the increment on one step works out the ring in
which **one particular** phrase appeared. That goes around the blur its author chose
for themselves (earlier in this same section) — and it goes around it without a
break-in, by reading the interface carefully.

**What the steps do not close must be said plainly.** A transition between steps is
itself a disclosure: "a few" at three kilometres and "about a dozen" at three and a
half mean roughly five phrases were added in that ring. Steps do not make the
measurement impossible — they make it coarse enough that it stops being worth the
time, and that is all that is achievable here. Only the absence of a counter would
close the question fully, and its price is a handle dragged blind.

So two things are added to the steps: the request goes out **once per gesture**, on
release, and it carries a rate limit of its own. A hundred requests in a row is not
a person moving a slider but somebody taking a density profile.

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
- ~~How a zone meets a circle~~ — settled 2026-08-26: **overlap is enough**. The
  rule has moved into the body of the section.
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

Every message is checked **before it is published, but not at the moment it is
sent**. The check runs as a queue: the node accepts the phrase at once, it is in
nobody else's feed yet, and the verdict arrives later — a 2.8 second median on
production-class hardware, a maximum near 12. All that time the author sees their own
phrase, muted and labelled as being checked; everyone else sees nothing. The client
must show that state rather than pretend the post is already live.

**The first phrase waits on the name as well.** A name is published text: it goes
into the same queue alongside the phrase, and the phrase reaches the feed only when
both are accepted. If the name is refused, the phrase keeps waiting until the name is
fixed and then goes out on its own; its 4:20 starts at publication rather than at
sending, so waiting costs it no life.

What is checked:

- **Rudeness** — a toxicity classifier. Fails, and it is not published.
- **Hazard** — threats, hostility towards a group, dealing in what is forbidden,
  approaching minors. Rejected outright.
- **Explicit** — rejected outright, like hazard. There is no switch that turns it
  on: this is a service for neighbours, not for dating.

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

**There is no topic classification.** The classifier carries no topic labels and
nothing filters on them: such a label would infer special-category data about an
author, which cannot be processed by default. No group is a category here. It is
gone from screen 4 in both storefronts and from neighbro's overview.

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

**The rate limit is feed-only too.** A per-IP limit on the node governs
publishing. There is no external captcha: we did not take on another processor
of other people's IPs for one.

**A refusal is explained.** If a message is not published, the person is told, and
told why. That is not politeness but a requirement for platforms carrying
user-generated content.

### A report

**A report explains in the person's own words rather than picking a class —
amended 2026-08-27, reversing the list of 2026-08-26.** A short list mirroring the
classes of refusal used to stand here: rudeness, dangerous, explicit, spam. The
argument against it is written in the legal spec (`xor.ad/docs/dsa/SPEC_EN.md` §3)
and carries more weight: **any list would be incomplete, and a wrongly chosen
category obstructs the review more than its absence does**. The old entry cited the
same Article 16 — "a notice has to say what exactly was complained about" — and drew
the wrong conclusion from a right requirement: what must explain is the notifier's
text, not a checkbox from our list.

**The justification is mandatory, and without it the form does not send:** an empty
notice creates no "actual knowledge" under Article 16(3). The cost is named plainly
— reporting takes a second longer than tapping a button, and some people will stop
there. In exchange, whoever goes through states their case in words instead of
fitting it to four labels.

The classes of refusal (rudeness, dangerous, explicit, spam) have not gone anywhere
— but they belong to **moderating a publication**, not to a report: our queue picks
them when it refuses an author, and they are never shown to a person in the form.

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
- **The machine catches less than half — recomputed 2026-08-27.** Measured on
  human-labelled data across nine languages, at the point where the system will
  actually run: **0.46** of what people call offensive is caught, at **0.07** of ordinary
  messages blocked for nothing. This said 0.55 — those are the **native** arm's
  numbers, and the arm chosen is **translation** (`xor.ad/docs/chat_EN.md` §8.14):
  at the same cost of a mistake it catches less on average and twice as much in
  the worst language.[retired] Reports take the other half — without them
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
- ~~Whether reports count from people the author has blocked~~ — **they do not**,
  and it is written a paragraph above in this same section. The question stood open
  next to its own answer (removed 2026-08-27).
- ~~Whether hiding lowers the author's ceiling~~ — **it does not, in either
  direction**, also above in this section (removed 2026-08-27).
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
| the identity's keys, IndexedDB writes | necessary for the service requested |
| the list of connected devices | necessary for the service requested |
| captcha and rate limit | legitimate interest — abuse prevention |

### Where data goes

Feed message text goes nowhere: moderation runs on our own node (§5). IPs go no further than the node: the rate limit is counted there. Storage is our own Postgres beside the node
and Bunny object storage. **Chat text does not leave**: that was the most
sensitive transfer, and now there is none.

Each recipient needs a processing agreement, a lawful transfer route out of the EU,
and a mention in the privacy notice. Our database sits beside the node, so where it
lives is where the node lives — and that is our choice to make.

### What is missing

- **There is no privacy notice at all.** It needs: who the controller is, what for,
  on what basis, who receives it, how long it is kept, what rights there are.
- **There is no EU representative**, and one is required where the operator is
  outside the EU and the people are inside it.
- **No record of processing and no impact assessment.** Location plus automated
  moderation plus possible minors is the usual reason to run one.
- **Age and consent.** The age at which a person may consent for themselves ranges
  from 13 to 16 across the EU. With the wider fingerprint gone there is no consent left
  at signup at all — but the others (precise location, push) still meet that threshold.

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
| connected devices | server | showing one's devices and disconnecting any | until revoked, or with the identity |
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

- ~~Whether a moderation refusal can be appealed~~ — **there is no appeal** (settled in §5); the text is edited and sent again. The question stood open next to its answer in the neighbouring section (removed 2026-08-28).
- ~~The exact wordings~~ — written on 2026-08-28: `xor.ad/docs/refusal-wordings_EN.md`. Only the rule still belongs here.
- ~~How specific the moderation cause is~~ — **the class only, with no pointer at the word** (decided 2026-08-28). Highlighting the fragment is a literal instruction for going around the filter, and there is no appeal; the price is accepted and named: seven phrases in a hundred are blocked for nothing and their authors will not learn what to change.


---

## 11. Likes and matches

**A like is available only to someone with a live phrase of their own in the feed
— settled 2026-08-26.** The reason is honesty rather than strictness: a match
counts only while **both** phrases are alive, so a like from someone with no phrase
of their own could never become one. It used to be placed anyway and go quietly
nowhere. The side effect is useful in itself: to like, you must publish, and
publishing takes the name through the queue (§5) — an unchecked name never reaches
the other person.

**A match is not a chat but an offer to talk, accepted by both.** Mutual likes open
a card: on it are the two phrases that caused it, and a button. The chat appears
when both have pressed; while only one has, the other sees an offer and the first
sees that there is no answer yet. When the other person was last online is not
shown: that is about them, not about the conversation.

**An offer lives exactly as long as both phrases live.** Either one expires and the
match goes with it, because the meeting of moods was what tied them together.

**The silence timer is chosen inside the chat, not at acceptance.** A chat opens
with an hour by default, the control sits in the conversation header, and each side
governs only their own (§2). Asking for it before a person has seen who they are
talking to demands a decision before there is anything to base it on.

**Whoever accepts first sees only "no answer yet" — settled 2026-08-27.** Neither
whether the other answered, nor whether they opened the card. It is the same
reason there is no "last seen" and no "read": a fact about someone else's action
presses. "Saw it and said nothing" reads as a refusal, though the person may
simply have closed the app. The cost is accepted: the wait is blind, right up to
the match expiring.


---

## 12. Games and tables

**A game here is a way to start talking, not a contest.** The engine draws the board
and lets pieces move; there are no rules, no score and no winner. The two agree
between themselves — including whether to take turns: the toggle exists, but both
switch it on.

**A move counts as activity, exactly like a reply.** A conversation and a table live
from the last movement rather than the last word: the game exists so that one can be
silent in words, and it would be absurd if a conversation died under the hands of two
people happily pushing draughts around.

**The board for two lives inside the conversation** (screen 18): encrypted with the
same key, never written to the database, gone when the conversation goes.

**A table is a thing of its own** (screen 19). Several neighbours sit around it, it
shows up in the feed by radius, and it lives by the feed's rules rather than the
chat's:

- **Talk at a table is public** and goes through the moderation queue like a phrase.
  The argument "there are two of us, nobody sees", which justifies an unchecked
  conversation, does not hold at a table full of strangers.
- **Whoever joins gets no history**: the board as it stands, the replies from the
  moment they sat down. The same rule as moving an identity.
- **Bands are checked everyone with everyone**: you may join only if you are inside
  every sitter's band and all of them are inside yours.
- **The majority of those sitting can ask someone to leave.** A table does not belong
  to whoever started it.
- **A block hides the table entirely** — someone else's game along with it, and that
  is the accepted cost.

**Private conversations stay pairwise.** A table does not turn the chat into a group
chat: the chat has a unique pair key and encryption derived for two, and we did not
touch either for the sake of playing together (settled 2026-08-26).


---

## 13. Stepping away

**The "step away" button is not a pause but a temporary departure.** It is not for someone leaving the room for a minute; it is for someone who has been sitting here too long and wants to break off. So the departure is real: the account moves into a "stepped away" state, and the product ceases to exist for that person for the chosen span — **20 minutes, an hour, or until morning**.

**What happens at the moment of leaving:**

- **Your own phrases are deleted for good**, along with the likes they collected. The quota slots free up at once: come back and you write anew, with all five available.
- **Matches burn.** For whoever was waiting on an answer, the offer simply disappears — with no explanation of who left or why.
- **Conversations run on their own timers** and are not frozen: your silence keeps counting. So a departure "until morning" is survived only by conversations with a long span, and every ten-minute one is gone. This is said **before** the press, on the screen where the span is chosen, not after.
- **The screen goes empty**: no feed, no conversations, no counters — one line and the time remaining.

**What others see.** Only those you have an open conversation with: instead of the input, a line saying "stepped away", so nobody spends words on emptiness. Nowhere else and to nobody else: whoever liked you sees only a vanished offer. This is the single place where the product reports someone else's state, and it is allowed because **the person declared it themselves** rather than the system giving away their presence.

**Coming back.** Leaving early is possible but takes a confirmation — otherwise a button meant to help you break off brings you back in three minutes. On return: **a clean feed and no summaries**: a count of what was missed would restore the very pull the departure was for.

**No limit on frequency.** Step away as often as you like: there is nothing to abuse, a person loses only their own.

### How the product notices the pull

After **an hour** of continuous use, one line appears: "you have been here an hour — step away?". It closes with a tap and does not come back that day.

**The hour is counted like this:** time runs while the tab is visible **and** there was a touch within the last three minutes. A forgotten open page counts nothing; someone reading without touching drops out of the count — undercounting is more honest than overcounting. **The counter lives on the device only** and is never reported to the node: how long a person sat here is not something to keep beside an identity.

**What this cannot catch, said plainly:** a person on two devices, someone reading the feed without touching it, and a tab left in the background. The counter catches obvious absorption, not every kind.

> **The measurement is incomplete — 2026-08-26.** `visibilitychange` behaves differently across mobile browsers, and there was nothing to check iOS and Android with: no devices. What was captured in desktop Chromium: a page opened in a background tab starts straight in `visibilityState=hidden` with `hasFocus=false`, and no events arrive until the tab is activated. Hence the rule that the counter does not treat "the page loaded" as the start of presence. The `visible ↔ hidden` transitions could not be captured in this environment — there was no way to activate the browser window; that stays unverified and is marked here rather than passed off as fact.
