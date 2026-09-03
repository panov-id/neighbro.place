# Screen 14 — Support

## Purpose

A support contact button, reachable from the app at any time.

## Screen elements

- A support button/icon — always available. **With a mark when an answer is waiting** (decided 2026-08-29): a dot on the icon itself rather than in the inbox. The inbox collects conversations between people, and the platform's own voice in that list would read as one more neighbour. The price is named plainly: the dot is seen only by someone who looks there, and people look there rarely.
- **Common questions above the input** (added 2026-08-29): where a phrase went, why liking is unavailable, where a conversation disappeared to. These are the product's three most frequent "it broke" cases, which are in fact how it works. The price is named: a list in front of the field reads as an attempt to talk you out of writing, so it stays short and does not block the field.
- A message input for the support request.
- **A line about where the answer will arrive** (added 2026-08-29): "the answer comes here, into this application; leave an email if you might lose access to your identity". The warning belongs **here** rather than on the start-over screen: there the decision is already made, here the person is still choosing what to pay.
- **Your own tickets as a list** (added 2026-08-29): number, date, answer. Today the number is shown once and never again. The price is accepted: a product that erases everything gains a list that lives a year — which is honest, because the ticket is kept for a year anyway (`00-mechanics_EN.md` §7).
- A send button.

## Logic

- The sent message lands in a table of our own database, beside the node.
- A new ticket fires a notification (email/webhook) for the team.
- **No number is promised for the reply time — decided 2026-08-29.** The line tells the truth: "we read everything, we do not answer at once — there are few of us". A number here would be a promise held by one person on holiday. The exception is a report of something unlawful: it enters the notice register and takes its deadlines, and that is said in a line of its own, because those deadlines are the law's rather than ours.
- There's no automated handling — just logging the request and notifying the team.
- **A confirmation is shown immediately**, with a request number: a person has to see that they were heard (settled 2026-08-26).
- **The answer arrives in the app at the next visit — settled 2026-08-27.** No email is needed for that: the answer waits attached to the identity and is shown when the person comes back. The mechanism is not new — it is exactly how the legal spec delivers an Article 17 statement of reasons to someone with no contact (`xor.ad/docs/dsa/SPEC_EN.md` §7). The screen used to know one path only — email — and demanded it precisely where a person feels bad and is asking for help.

  The cost is named: the answer lives with the identity. Start over, or lose the device without the paper code, and the answer will not be seen, because there is nobody to show it to.
- **Email remains, optional**, and is asked of someone who wants the answer another way — waiting for it on a different device, say. The product lives without email by construction, and collecting it where it can be avoided means creating a record about a person for nothing.
- **A content report sent here is accepted as an Article 16 notice — settled 2026-08-27.** The law does not require the right form: if we were told about something illegal, that is "actual knowledge", whatever the channel is called (Article 16(3)). The message moves into the same register as notices from the form (screen 5) and gets the same deadlines. Sending a person off to retype their text into another form is not an option: some will simply leave, while the knowledge is already ours — which is the very case the article was written against.
- **A message is kept for a year** (`00-mechanics_EN.md` §7) and is tied to the identity, because otherwise there is nowhere to show the answer. On "start over" the link is broken: the message stays with us as a record of the review, and the new identity has nothing to do with it.

## Open questions

- ~~Exactly where the button is reachable from~~ — **from wherever a person is stuck** (decided 2026-09-02): a refusal state, an error, the settings. There will be no separate icon in the header of every screen — the entrance sits at the place of the event, as for the other screens. The promise that support is "always reachable from the app" holds because getting stuck only happens where the button is.
- ~~How a person learns an answer has arrived~~ — **by the mark on the support button** (decided 2026-08-29, above). The answer deliberately does not enter the inbox.
- ~~Confirmation and reply~~ — settled 2026-08-26 (above).
