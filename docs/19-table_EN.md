# Screen 19 — A table: pull up a chair and play together

## Purpose

A table is a shared board several neighbours sit around. The screen was created on 2026-08-26 from the "pull up a chair" idea: a game for two (screen 18) works as a way to start talking, but a group is more fun — and there was nothing in the product to gather one with.

**A table is not a conversation.** It is a separate thing beside the feed and lives by the feed's rules rather than the chat's. That is deliberate: otherwise the pairwise chat would have to be rewritten (`pair_key` is unique per pair) along with group encryption, while private talk between two should stay as it is.

## How it looks and how to join

- A table shows up **in the feed**, among the phrases, to those whose viewing circle caught its zone — marked as a table, with the name of the game and how many are sitting.
- **The games at a table are the same classes as for two** (screen 18): dominoes and cards gather a group best, a grid board usually stays pairwise, and flick-draughts physics works with any number of players.
- **A table is set up from the composer** (screen 4, the "table" tab): the game, the zone, a "set it up" button. Until 2026-08-27 that path did not exist — this screen described pulling up a chair to a table nobody could put there.
- A **"pull up a chair"** button — open to anyone within the radius, with no invitation and no application.
- Who is sitting is visible; when anyone was last online is not, as everywhere else.

## Logic

- **No hard cap on numbers.** As many as sit down, play; the limit is the readability of the board, not a rule.
- **A table lives from its last move**, like a conversation: while people play it lives, and when they leave it disappears with the board and everything said around it.
- **Whoever joins does not see what came before.** The board arrives as it stands, the replies only from the moment they sat down (settled 2026-08-26). The same rule as moving an identity: history does not appear out of nowhere.
- **Talk at a table is public.** Replies go through the same moderation queue as the feed (`00-mechanics_EN.md` §5): strangers sit at a table, and "there are two of us, nobody sees" is not true here. The cost is named plainly: a 2.8 second median per reply is felt more at a table than in the feed.
- **Age bands — everyone with everyone.** You may join only if you are inside every sitter's band and they are inside yours (`xor.ad/docs/chat_EN.md` §8.2). The same rule as for a pair, applied to all at once.
- **The majority of those sitting can ask someone to leave.** Two out of three say "enough" and the person stands up. Nobody owns a table: the neighbour who started the game does not become its master.
- **A block hides the table entirely.** If someone you blocked is sitting there, the table is not shown to you at all. The cost is named: one person can hide someone else's game from you simply by joining it.

## Open questions

- How a table looks in the feed: a card with the board, a line with the game's name, the number of sitters — undefined.
- What happens to a table when one person is left: does it close at once or wait out the silence timer.
- How many replies a returning person sees if they left and came back: from scratch, or from where they left.
- Whether a table is visible to those outside the bands — greyed out without a button, or not at all.
