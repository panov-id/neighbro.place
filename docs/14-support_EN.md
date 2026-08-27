# Screen 14 — Support

## Purpose

A support contact button, reachable from the app at any time.

## Screen elements

- A support button/icon — always available.
- A message input for the support request.
- A send button.

## Logic

- The sent message lands in a table of our own database, beside the node.
- A new ticket fires a notification (email/webhook) for the team.
- There's no automated handling — just logging the request and notifying the team.
- **A confirmation is shown immediately**, with a request number: a person has to see that they were heard (settled 2026-08-26).
- **The answer arrives in the app at the next visit — settled 2026-08-27.** No email is needed for that: the answer waits attached to the identity and is shown when the person comes back. The mechanism is not new — it is exactly how the legal spec delivers an Article 17 statement of reasons to someone with no contact (`xor.ad/docs/dsa/SPEC_EN.md` §7). The screen used to know one path only — email — and demanded it precisely where a person feels bad and is asking for help.

  The cost is named: the answer lives with the identity. Start over, or lose the device without the paper code, and the answer will not be seen, because there is nobody to show it to.
- **Email remains, optional**, and is asked of someone who wants the answer another way — waiting for it on a different device, say. The product lives without email by construction, and collecting it where it can be avoided means creating a record about a person for nothing.
- **A content report sent here is accepted as an Article 16 notice — settled 2026-08-27.** The law does not require the right form: if we were told about something illegal, that is "actual knowledge", whatever the channel is called (Article 16(3)). The message moves into the same register as notices from the form (screen 5) and gets the same deadlines. Sending a person off to retype their text into another form is not an option: some will simply leave, while the knowledge is already ours — which is the very case the article was written against.
- **A message is kept for a year** (`00-mechanics_EN.md` §7) and is tied to the identity, because otherwise there is nowhere to show the answer. On "start over" the link is broken: the message stays with us as a record of the review, and the new identity has nothing to do with it.

## Open questions

- Exactly where the button is reachable from (feed header, settings, a separate icon) is not defined yet.
- How a person learns an answer has arrived if they have not visited for a week: the inbox collects reasons about conversations and matches (§8.12), and a support answer is not yet on that list.
- ~~Confirmation and reply~~ — settled 2026-08-26 (above).
