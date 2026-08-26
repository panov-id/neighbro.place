# Screen 4 — Post Composer

## Purpose

The screen for composing a feed message, opened via the "add" button.

## Screen elements

- Text input — up to 128 characters.
- A group size selector — 1, 2, 3 ... N ("how many of you").
- A location blur radius slider — blurs the author's exact geoposition: the message is tied not to precise coordinates but to a blurred zone around them (a privacy setting, not a visibility setting for the post).
- A send button.

## Logic

- Text is required; group size and blur radius are optional settings on the post.
- The message is text-only — no image attachment. An image is only possible on a boosted/promoted message (see the README's "Beyond the alpha" — balance and boosting section).
- On send the message goes into the **moderation queue** rather than being checked on the spot: the node accepts the phrase at once, the composer closes, and it appears **to its author** muted and labelled as being checked. It is not in anyone else's feed yet. The verdict arrives later — a 2.8 second median, a maximum near 12 (`00-mechanics_EN.md` §5). Passed, it becomes ordinary; refused, it turns into an explanation with a cause, and the text stays at hand to be fixed and sent again.
- **A person's very first phrase waits on the name as well**: the name goes into the same queue, and the phrase reaches the feed only when both are accepted. If the name is refused the phrase lies waiting until it is fixed; its 4:20 counts from publication, so waiting costs it no life. While the first one waits, a second cannot be sent.
- Sending also runs through a per-IP rate limit on the node. It applies only to publishing in the feed, not to sending chat messages. There is no external captcha.

## Open questions

- Whether the separate city/country field from the earlier description is still kept, or replaced by the blur radius slider.
- Default values and bounds for the blur radius slider are not defined yet.
- The send button's form (icon vs. text) is not defined yet.
