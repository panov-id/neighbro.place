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
- On send, the message goes through the same AI check described in the Moderation section (Google Perspective API for toxicity + LLM tone classification: sexual subtext, LGBT-related topic) — it's published to the feed only after passing the check.
- Sending also runs through Cloudflare Turnstile (a captcha, invisible to the user in most cases) and an IP rate limit via Bunny Shield. Both checks apply only to publishing in the feed, not to sending chat messages.

## Open questions

- Whether the separate city/country field from the earlier description is still kept, or replaced by the blur radius slider.
- Default values and bounds for the blur radius slider are not defined yet.
- The send button's form (icon vs. text) is not defined yet.
