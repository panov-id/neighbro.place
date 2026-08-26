# Screen 4 — Post Composer

## Purpose

The screen for composing a feed message, opened via the "add" button.

## Screen elements

- Text input — up to 128 characters.
- **Mode — three buttons: alone / company / party** (edit of 2026-08-26). A selector of numbers, "1, 2, 3 … N", used to stand here, but the node stores exactly the mode (`mode` = `alone | company | party`), and that is what the match card shows. An exact headcount changes nothing and adds a detail about the company that the product does not need.
- A blur slider — ties the phrase to a zone rather than a point. **300 m by default, from 100 m to 2 km** (settled 2026-08-26): three hundred metres hide the doorway while leaving the block recognisable. It is a privacy setting rather than a visibility one: who sees it is decided by the reader's radius, and the zone need only overlap their circle.
- A send button.

## Logic

- Text is required; group size and blur radius are optional settings on the post.
- The message is text-only — no image attachment. An image is only possible on a boosted/promoted message (see the README's "Beyond the alpha" — balance and boosting section).
- On send the message goes into the **moderation queue** rather than being checked on the spot: the node accepts the phrase at once, the composer closes, and it appears **to its author** muted and labelled as being checked. It is not in anyone else's feed yet. The verdict arrives later — a 2.8 second median, a maximum near 12 (`00-mechanics_EN.md` §5). Passed, it becomes ordinary; refused, it turns into an explanation with a cause, and the text stays at hand to be fixed and sent again.
- **A person's very first phrase waits on the name as well**: the name goes into the same queue, and the phrase reaches the feed only when both are accepted. If the name is refused the phrase lies waiting until it is fixed; its 4:20 counts from publication, so waiting costs it no life. While the first one waits, a second cannot be sent.
- Sending also runs through a per-IP rate limit on the node. It applies only to publishing in the feed, not to sending chat messages. There is no external captcha.

## Open questions

- The send button's form (icon vs. text) is not defined yet.
