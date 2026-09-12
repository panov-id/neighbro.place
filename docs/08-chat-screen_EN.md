# Screen 8 — Conversation

## Purpose

A private conversation between two people, opened after both accepted the match (screen 6).

## Screen elements

- The header: the peer's **name and age**, and a **key-comparison mark** beside the name (added 2026-08-28). The mark exists because a guarantee nobody knows about works only on paper — and this one closes the single hole in the encryption: us substituting a key. Tapping the mark or the name opens the **safety code** — a string derived from both identities' long-term keys (`xor.ad/docs/chat_EN.md` §8.13), with an explanation of what it is for.
- The line of replies — short messages back and forth.
- **A "…" menu on the other person's line — added 2026-09-11.** Two actions: **block**
  and **report**. Screen 6 promised exactly this ("block them and report it"), while the
  conversation had no menu, no button and no route — the same class of gap fixed for the
  table on 2026-08-28 and for the offer on 2026-09-04: the legal path exists, the
  interface one does not. And this is the most closed place in the product: a
  conversation is not moderated by construction, so a report is the only protection.
  **Blocking** introduces nothing new: the mechanic is the one from the feed (screen 5),
  and it puts the conversation out for both.
  **A report goes with target kind `chat`, and the person writes the body themselves.**
  There is no snapshot and there cannot be — replies are encrypted on the devices and the
  node does not hold them; the notice gets `snapshot_state = not_accessible`, which the
  specification already knows and hands to a person
  (`xor.ad/docs/dsa/SPEC_EN.md`). The cost is accepted and named: **it will be examined
  on one side's word**, with no proof. That is a claim, not evidence, and it is treated
  accordingly.
  **The route is the support one (screen 14):** a quotation of the other person's line
  may contain the very thing being reported, and the WAF cuts such bodies on the way in.
  **No anonymity is promised here — written down 2026-09-11.** The target is a `chat_id`,
  and a conversation is known to two people: the other one will work out that it was you.
  The line "we do not attach who you are" from screen 5 is about the feed and is not
  carried over here; the decision still arrives only by email, if you left one.
- Lines about new likes between these two — right in the conversation (screen 6).
- **Lines about moves — in the same place (2026-09-09).** "Anya placed a tile on e4", "Petya flicked": these words used to exist for the screen reader alone, and now they stand in the conversation. They are not encrypted, unlike the replies beside them — they are part of the game state.
- **The score of the games — in the board's header, while the conversation lives.** It accumulates between games (3:2 after five) and goes out with the conversation: no history of wins, no mark on an identity.
- An input with a **256 character** counter.
- The silence-timer control in the header — 10 minutes, 30 minutes, an hour, or "while we're talking".
- A **🎲 "suggest a game"** button in the header — opens the shared board for two (screen 18).
- An **"end it"** button — closes the conversation for both at once, **with a confirmation** (settled 2026-08-27: "are you sure? the history disappears for both").
- What is left of your own timer: how long the conversation lives if you stay quiet.

## Logic

- **The product introduces people; keeping in touch is yours — said out loud
  2026-09-10.** This is the first place it is stated plainly, and stating it is needed
  because the product leads to a meeting — the terms warn outright that it ends in
  meeting a stranger — while after "seven, by the fountain" it offers nothing: no
  links, and the span counts from **your own** silence, so an hour of quiet before the
  meeting kills the conversation. Once you have agreed, swap whatever neighbours swap;
  the conversation here exists to decide whether it is worth swapping at all.
  **Why a longer span does not fix it.** Extending a conversation "until the meeting"
  would mean holding a record that two people intend to meet at a given hour — the
  first trace to outlive the feed, and the least pleasant one imaginable. Counting from
  the other side's message instead of your own would undo the decision of 2026-08-26
  and let a persistent person keep a conversation alive indefinitely. The cost is
  accepted and it is real: some conversations will move to other messengers by the
  second line, and it will be empty here.
- **The reply limit is 256 characters and it comes from the server** (`max_message_length`), not baked into the client. The counter is the client's; the node is what refuses.
  The second limit, **2048 bytes of ciphertext** (`max_ciphertext_bytes`), is not shown to the person: with an honest 256 characters it is unreachable — even a string of nothing but emoji comes to 1404 bytes, and hitting 2048 takes 378 characters. It guards against a forged client, not against a real conversation.
- **Two statuses: accepted and error (rewritten 2026-09-12).** "✓" means "the node took it and answers for delivery": if the other person is offline, the message waits for them while the conversation lives. An error gives a line with a retry and means only that the node refused. **There is no "delivered" and no "read"** and will not be: either would tell you whether the other person is online and when they opened the conversation.
- **The silence timer is chosen here**, not when accepting the match, and can be changed at any moment. An hour by default. Each side has their own count and cannot see the other's (`00-mechanics_EN.md` §2).
- **Expiry is announced in advance**: in its last minutes the conversation is shown fading. When it has ended for the other person, one line says so — otherwise an expired timer is indistinguishable from being snubbed.
- **An expired conversation disappears for whoever's span ran out — amended 2026-08-27.** It used to say "for both", which held while the span was shared. The span is now each person's own (§5 of the spec), and for the other it stays until their own span, marked "ended" (screen 7). Whoever had it on screen at that moment keeps a headstone reading "the conversation has ended" until they tap it, and it does not return to the list.
- **The conversation key and the game board go out for both at the first death** (§8.13). **Clarified 2026-09-09:** the board goes out with the conversation, but no longer because its key did — the board no longer sits under it. It is held by the conversation's span rather than by its encryption, and it leaves together with the score. So neither side can write, even while the other still counts the conversation as alive: they keep their own history — it sits under the vault key, not the conversation key — but not the conversation.
- **"End it" is not the same as expiry.** Silence is not a decision; a button is, and so it works symmetrically: it ends the conversation for both at once. The confirmation is mandatory, because the other side loses its history without having agreed to it.
- **The peer has stepped away** (`00-mechanics_EN.md` §13) — a line saying **"stepped away"** replaces the input, with no time of return and no time of leaving. This is the only place in the whole product where anyone's presence is reported, and it is allowed because the person declared the state themselves rather than the system inferring it.
- **A broken connection is a state of the screen, not silence (added 2026-09-02).**
  The socket breaks on every node restart and every network change on the
  person's side; the protocol accounts for it (`xor.ad/docs/protocol_EN.md`
  §4.4) and the screen, until now, did not. What is seen:
  - **Reconnecting.** A bar in the conversation header, the input alive, what
    was typed kept. A reply sent at that moment queues on the device with the
    same error status as any undelivered one and goes out by itself once the
    connection is back.
  - **The identity moved to another device** (the node closed the socket with
    code `4002`). Reconnecting is pointless: the conversation closes and the
    person is told the identity now lives on another device.
  - **The conversation ended** (code `4003`) — not a connection error but the
    tombstone described above.
  - **The app is out of date** (code `4004`) — the node does not support this
    version; a line asks to update and no reconnect is attempted.
  Telling these four apart is mandatory: a client that does not either hammers a
  closed door or shows a live identity as dead.
- **The first load of a conversation is a state of its own (added 2026-09-02).**
  The history lives on the device and is decrypted with the vault key, which is
  not instant. While it runs — a skeleton of replies, not an empty screen: an
  empty screen, in a product where conversations disappear by themselves, reads
  as "everything was erased".
- **Conversations are not moderated** — neither for rudeness nor for explicitness: they never leave the pair of devices. Only what is published to the feed is checked (`00-mechanics_EN.md` §5).
- **There are no links in a conversation** — they are stripped, as in the feed; the one place a link lives is a neighbourhood offer (`00-mechanics_EN.md` §5).
- **Encryption happens on the devices**: the key is derived by the two of them and the node carries ciphertext (`xor.ad/docs/chat_EN.md` §8.13). A conversation is not merely unchecked — there is nothing to read it with.
  **A game is the exception, and a person is told so plainly (2026-09-09).** The board and the moves are outside end-to-end encryption: only whoever sees them can keep to the rules. The node knows what you play and how, and does not know what you say. The warning on screen 6 carries this line too, but it belongs here as well: the conversation is where a person lives rather than passes through.
- **History sits on the device** in IndexedDB, encrypted with the vault key made of the PIN and the node's share. It exists neither with us nor on another device.
- **A draft reply lives while the conversation is open and never reaches the disk — decided 2026-08-28.** Go out to the list and back, and the text is there; close the app, and it is gone. This **differs** from a phrase's draft (screen 4), which survives leaving the screen and sits in encrypted storage, and the difference is deliberate: publishing is an intention that outlives a screen, while a conversation disappears by itself, and a draft outliving it would outlive the thing that was meant to vanish.

## Open questions

- ~~Whether a conversation can be closed by hand~~ — it can, **for both at once and with a confirmation** (2026-08-26; the confirmation added 2026-08-27): the other person sees the same headstone as on expiry. Staying silent until it expires is a poor only way out of an unpleasant conversation, and a block is too large a step for it. The history on the device goes the same way as on expiry.
- ~~How long before the end the fading starts~~ — **in the last quarter of the span** (settled 2026-08-26). A fraction rather than fixed minutes: for a phrase that is the last hour-odd of 4:20, for an hour-long conversation a quarter of an hour, for a ten-minute one two and a half minutes. Fixed five minutes would put a ten-minute conversation half its life into fading.
