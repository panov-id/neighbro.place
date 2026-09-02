# Screen 16 — Stickers (Beyond the Alpha)

## Purpose

Decorative stickers **in a conversation and at a table** (see the README's "Beyond the alpha" section). Not part of day0/the alpha.

**In a conversation and at a table — clarified 2026-08-30.** It was first recorded as "in a conversation only"; a table is not a conversation, and the question would have surfaced in code. At a table the stickers are the same and follow the same rules, but **the node sees them**: a table has no end-to-end encryption by construction (screen 19). There are still no stickers in the feed.

**Not in the feed — settled 2026-08-27.** It used to say "for messages/chat", which argued with screen 4: the feed is text, image attachments are unavailable, and an image is possible only on a promoted message. A sticker in place of a phrase would be an image in the feed — an exception to a rule that holds precisely because it has none. The cost is accepted: the feed stays dry to look at, and the feed is the first thing a newcomer sees.

## Logic

- The sticker catalog is fixed: populated and edited from the admin panel (see `xor.ad/docs/panel_EN.md`), images live in Bunny object storage.
- Stickers are free: the product has no payments and no internal balance. A user picks a sticker from the catalog and sends it **in a conversation** ([retired] this used to say "in a message/chat" — the wording outlived its own retirement of 2026-08-27 by two paragraphs and was removed on 2026-08-29).
- Regular messages stay text-only — a sticker is a separate, decorative entity, not a free-form image attachment.
- **The node does not see which sticker was sent — settled 2026-08-27.** The client puts the sticker's identifier **inside the ciphertext**, under the same conversation key as the text; it fetches the image from the catalogue itself. Otherwise the sticker would travel as a plain field and the node would know a fragment of what two people are saying — the opposite of what §8.13 maintains. The single exception to end-to-end encryption stays single: the deck and the dice, where the node shuffles and sees the deal (§6).
- **Every sticker has a name — decided 2026-08-29.** A short word sits beside the image in the catalogue: "waving", "asleep", "brought coffee". One decision closes two different failures at once.
  **The terminal.** `depth` is a text client, and "one sticker, instead of text" makes a line it cannot render at all; until 2026-08-29 the word "sticker" did not appear in its document once. Now it prints `[waving]` — not an image and not a blank, but what the person meant.
  **The screen reader.** A sticker is not decoration inside a phrase but a **whole line**, and a line without a single word reads as empty space. The name is its text alternative, and it is the same text the terminal prints: one string, two consumers.
  **The name travels in the catalogue, not in the line** — which matters, or this decision would break the previous one. Inside the ciphertext there is still only an identifier; the client takes the name from the catalogue it already has. The node learns neither the image nor the word.
  **The names are ours, not a user's**, so they need no moderation queue: they are written by whoever fills the catalogue from the panel.
  **The price is accepted:** the name has to be translated into every storefront language, or a Georgian conversation grows an English island. Same case as the community guidelines: machine translation now, a native speaker improving it later (`xor.ad/docs/accessibility-and-i18n_EN.md`).
- **The cost is named:** fetching an image from the catalogue is visible on the network by itself, so the catalogue is **preloaded whole**. A request for one image at the moment of sending would give the choice away no less than a plain field would.
- **The catalogue's ceiling is 150 KB over the wire, decided 2026-08-29.** The number is anchored to a measurement rather than a feeling: the storefront's first page weighs **71 KB over the wire** (`https://dev.sosed.panov.id/`, 2026-08-29), and a catalogue fetched whole before the first sticker must not cost more than two such pages. **Beyond that the catalogue splits into packs**, and a pack is fetched **whole** as well — otherwise the saving would restore exactly the leak preloading exists to prevent: a request for one image gives the choice away.
  **What is not measured is said plainly:** the weight of one sticker. There are no stickers yet; at 3–4 KB per image, 150 KB is around forty of them, but that is arithmetic on an assumption, not a measurement.
- **A sticker disappears with the conversation**, like everything else: it is part of a line, and lines live only on the devices (§8.8). The catalogue keeps the sticker; the conversation keeps nothing.

## Open questions

- ~~Where the sticker catalogue is opened from~~ — **from the conversation's input field** (decided 2026-09-02). A sticker is a reply of its own rather than a decoration, so it is picked where a reply is written; there is no catalogue section of its own in the app.
- ~~The catalogue size at which preloading stops being free~~ — **the ceiling is named: 150 KB over the wire** (decided 2026-08-29, above). The weight of a single image is not measured — there is nothing to measure yet.
- **Reporting a sticker is narrowed, not closed (2026-08-29).** With a name in the catalogue, an Article 16 notice can carry the sticker's identifier and name without revealing a word of the conversation: both sit publicly in the catalogue. What that looks like in the form, and what goes into the snapshot, is not described in `xor.ad/docs/dsa/SPEC_EN.md`.
- ~~How many stickers per message~~ — **one, and instead of text** (settled 2026-08-26): a sticker is a reply of its own, not a decoration on a phrase.
