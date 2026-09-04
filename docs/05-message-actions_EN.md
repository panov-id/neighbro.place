# Screen 5 — Feed Message Actions

## Purpose

The set of actions available on a message card in the feed: like, hide, block, report.

## Message card elements

- A like icon — visible right on the card, outside any menu.
- A **"…"** button on the card — opens three actions (settled 2026-08-26: long-press is unobvious and does not work with a mouse, a swipe fights the scroll). They run from the quietest to the loudest: **hide the phrase**, **block the person**, **report**.

## Logic

- **A like is available only if you have a live phrase of your own in the feed** (`00-mechanics_EN.md` §11). Otherwise the button is inactive and says why: a match counts only while both phrases are alive, so a like without one of your own would go nowhere.
- **A mutual like opens not a chat but an offer to talk**, accepted by both (screen 6).
- **Hide the phrase.** The quietest action: the phrase disappears from your feed and from nowhere else. The author learns nothing, their feed does not change, the like counter is untouched, and nothing goes into the moderation queue. It is a viewer's filter, not a sanction (`xor.ad/docs/chat_EN.md` §8.9). The action returned to this screen on 2026-08-27: the spec knew about it from the start and kept a `hidden_messages` table for it, but it had no interface — a person who simply did not want to see something was left with reporting, that is, sending a neighbour into the moderation queue for not being to their taste.
- **Block.** Hides that author's messages from you and separates the two of you: the check is symmetric, so they stop seeing yours as well. It also **puts out a pending match** and **closes a shared chat** if there was one (§8.9, flow 16). **It does not lower the author's ceiling — settled 2026-08-26:** cutting someone's quota with one tap would let a single person quietly narrow another's voice.
- **Hiding can be undone — decided 2026-08-28.** Hidden phrases sit in a list in the settings (screen 10) and come back from there. Until now the quietest of the three actions was also the most irreversible — for the rest of the phrase's life; irreversibility is above its rank, and the list is short by construction: a hidden phrase lives the same 4:20 as any other.
- **Blocking asks for confirmation — decided 2026-08-28**, and the confirmation names what will disappear: a pending match and an open chat with this person. One tap in a menu closed a whole conversation, and the person learned about it afterwards.
- **Report.** Immediately removes the message from your feed and adds one to that message's counter; when the counter reaches the threshold — a share of the audience, not a number — the message goes for everyone. **It does not touch the author's quota.**

  **The notifier does not pick a category — amended 2026-08-27, reversing the list of 2026-08-26.** "Rudeness, dangerous, explicit, spam" used to stand here, and it contradicted the legal spec (`xor.ad/docs/dsa/SPEC_EN.md` §3), which says plainly: any list would be incomplete, and a wrongly chosen category obstructs the review more than its absence does. This is not settled by taste: a report is an Article 16 notice, and the rules for accepting such notices live in the legal document.

  **The report form explains how a report differs from hiding — decided 2026-08-28.** The form's first line: "this goes to a moderator; if you simply do not want to see it, hide it", with a button beside it that hides and closes the form. The explanation belongs **here rather than in the menu**: the menu stays three words long, and the talking-out-of-it happens at the step where a person has already chosen the loud action.

  **A justification in the person's own words is mandatory.** Without it the form does not send: an empty notice creates no "actual knowledge" under Article 16(3) and gives nothing to work from. The cost is named: reporting takes a second longer than tapping a button.

  **One form, two outcomes — decided 2026-09-04 after the review panel.** Until this edit a single tap did two things at once: it voted for hiding by threshold and declared itself an Article 16 notice. The legal spec keeps them apart (`xor.ad/docs/dsa/SPEC_EN.md` §1: "a report about a message and a report about an offer are different entities"), and the published terms promise a person the same. Now the screen is built that way too:

  - **The vote always happens.** The phrase leaves your feed, the message's counter goes up, the audience-share threshold works as before. This is a viewer's filter; it needs no name, no email and no review.
  - **A checkbox, "I believe this is illegal", turns the report into an Article 16 notice.** It is not ticked by default. With it the form shows the remaining Article 16(2) fields — an optional name and email, and the good-faith confirmation ("the information is accurate and complete to the best of my knowledge") — along with the line from §5.1 of the spec: if the report concerns the sexual abuse of children, leave the name and email empty.
  - **A ticked box promises three things**, and the form says them plainly: the notice gets a number, the acknowledgement arrives immediately and automatically (Art. 16(4)), and the decision with its reason arrives the same way (Art. 16(5)). With no email, the acknowledgement is shown in the app at the next sign-in.

  **The menu stayed three words long, and that is a consequence rather than a compromise.** A fourth item would have been the longest and the rarest, while what needs separating is not the menu items but what happens after sending. Someone who simply does not want to see a phrase never reads about Article 16; someone who saw something illegal meets the checkbox where they have already decided to be loud.

  **The place fills itself in, and without it there would be nothing to review.** The form opens from the card with `target_kind=feed_message` and `target_id`, so the content snapshot is taken as the notice is created (`xor.ad/docs/dsa/SPEC_EN.md` §4). This is not convenience: a phrase lives 4:20, and a notice typed by hand from the storefront footer reaches the node when there is nothing left to capture — `snapshot_state = target_gone`, and the review has to work from a description instead of the phrase itself.

## Open questions

- ~~Whether a report hides the message personally~~ — it does, immediately (`00-mechanics_EN.md` §5).
- ~~How much a report or a block lowers the quota~~ — neither lowers it at all (2026-08-26).
- ~~What an inactive like looks like~~ — settled 2026-08-26: the icon is **visible but muted**; pressing it gives the line "to like, say something yourself" and a way into the composer. Hiding it is not allowed: a person would never learn that likes exist, nor why they should publish.
- ~~The report's category~~ — **there is none; a free-text justification instead** (2026-08-27, per the legal spec).
- ~~How hiding differs from reporting~~ — **said in the report form rather than in the menu** (decided 2026-08-28, above).
- How the list of hidden phrases looks in the settings — a line per phrase or a number that expands — is not drawn.
