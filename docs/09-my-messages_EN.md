# Screen 9 — My Messages

## Purpose

A screen listing the user's own active messages currently in the feed.

## Screen elements

- A list of messages the user has published that haven't disappeared yet.
- A countdown timer to disappearance on each message.
- A manual delete button on each message.
- The remaining posting quota (how many of the 5 messages are still available).

## Logic

- A message can be deleted manually at any point before its timer runs out.
- A manually deleted message disappears from the feed immediately.
- The timer and remaining quota are the same values that apply in the feed and at posting time (see screens 3 and 4, and the Moderation section).

## Open questions

- Whether manually deleting a message restores the quota, or deletion has no effect on quota.
- How this screen is opened from the main interface (an icon in the feed, a separate menu item) is not defined yet.
