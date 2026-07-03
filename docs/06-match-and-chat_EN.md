# Screen 6 — Match and Chat

## Purpose

What happens on a mutual like, and how new-like notifications show up in the chat between users who already matched.

## Logic

- **Match.** When a like turns out to be mutual, a match animation plays — showing exactly which message matched (the one both sides liked) — and a private chat opens between the two users right away.
- **Likes after a match.** If one of two already-matched users likes another message of the other person in the feed, this doesn't trigger a new match or create a separate chat — the like shows up right inside the existing chat as a notification: "this message got liked."

## Open questions

- The visual form of the match animation is not defined yet.
- The format of the in-chat like notification (text/message card/icon) is not defined yet.
