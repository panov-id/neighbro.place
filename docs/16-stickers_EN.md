# Screen 16 — Stickers (Beyond the Alpha)

## Purpose

Decorative stickers **in a conversation** (see the README's "Beyond the alpha" section). Not part of day0/the alpha.

**In conversations only — settled 2026-08-27.** It used to say "for messages/chat", which argued with screen 4: the feed is text, image attachments are unavailable, and an image is possible only on a promoted message. A sticker in place of a phrase would be an image in the feed — an exception to a rule that holds precisely because it has none. The cost is accepted: the feed stays dry to look at, and the feed is the first thing a newcomer sees.

## Logic

- The sticker catalog is fixed: populated and edited from the admin panel (see `xor.ad/docs/panel_EN.md`), images live in Bunny object storage.
- Stickers are free: the product has no payments and no internal balance. A user picks a sticker from the catalog and uses it in a message/chat.
- Regular messages stay text-only — a sticker is a separate, decorative entity, not a free-form image attachment.
- **The node does not see which sticker was sent — settled 2026-08-27.** The client puts the sticker's identifier **inside the ciphertext**, under the same conversation key as the text; it fetches the image from the catalogue itself. Otherwise the sticker would travel as a plain field and the node would know a fragment of what two people are saying — the opposite of what §8.13 maintains. The single exception to end-to-end encryption stays single: the deck and the dice, where the node shuffles and sees the deal (§6).
- **The cost is named:** fetching an image from the catalogue is visible on the network by itself, so the catalogue is **preloaded whole**. A request for one image at the moment of sending would give the choice away no less than a plain field would.
- **A sticker disappears with the conversation**, like everything else: it is part of a line, and lines live only on the devices (§8.8). The catalogue keeps the sticker; the conversation keeps nothing.

## Open questions

- Where in the app the sticker catalog is opened from is not defined yet.
- The catalogue size at which preloading stops being free has not been measured: at a dozen stickers it is kilobytes, but no ceiling is named.
- ~~How many stickers per message~~ — **one, and instead of text** (settled 2026-08-26): a sticker is a reply of its own, not a decoration on a phrase.
