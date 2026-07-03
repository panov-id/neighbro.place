# Screen 7 — Chat List

## Purpose

An overview screen of all the user's active matches/chats — shown once there's more than one match.

## Screen elements

- A list of chats: one entry per match.
- Tapping an entry opens that specific chat.

## Logic

- A new match adds a new entry to the list, without replacing existing chats.
- The list stays current for as long as the chats themselves stay active (see screen 8 — chat lifetime).

## Open questions

- What exactly is shown per list entry (name, last message preview, unread indicator) is not defined yet.
- The list's sort order (by last message time, by match time) is not defined yet.
