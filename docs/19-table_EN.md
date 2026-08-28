# Screen 19 — A table: pull up a chair and play together

## Purpose

A table is a shared board several neighbours sit around. The screen was created on 2026-08-26 from the "pull up a chair" idea: a game for two (screen 18) works as a way to start talking, but a group is more fun — and there was nothing in the product to gather one with.

**A table is not a conversation.** It is a separate thing beside the feed and lives by the feed's rules rather than the chat's. That is deliberate: otherwise the pairwise chat would have to be rewritten (`pair_key` is unique per pair) along with group encryption, while private talk between two should stay as it is.

## How it looks and how to join

- A table shows up **in the feed**, among the phrases, to those whose viewing circle caught its zone — marked as a table, with the name of the game and how many are sitting.
- **The games at a table are the same classes as for two** (screen 18): dominoes and cards gather a group best, a grid board usually stays pairwise, and flick-draughts physics works with any number of players.
- **A table is set up from the composer** (screen 4, the "table" tab): the game, the zone, a "set it up" button. Until 2026-08-27 that path did not exist — this screen described pulling up a chair to a table nobody could put there.
- **Getting back to a table goes through the line in the feed header** (settled 2026-08-27). A table is not in the conversations list: it is not a conversation. The cost is named: narrow the circle or leave the radius and the line still returns you, but finding the table in the feed again will not work.
- A **"pull up a chair"** button — open to anyone within the radius, with no invitation and no application.
- Who is sitting is visible; when anyone was last online is not, as everywhere else.

## Logic

- **No hard cap on numbers.** As many as sit down, play; the limit is the readability of the board, not a rule.
- **A table lives from its last move — on one span shared by everyone** (clarified 2026-08-27). A move or a line from any sitter pushes it alike. This differs from a conversation, where each side has its own count: there two people are involved, while here the company changes, and a separate count would mean the table exists in different states for those sitting at it. When they leave it disappears with the board and everything said at it.
- **A table with one sitter is a normal state** (settled 2026-08-27): it is visible in the feed, people can pull up a chair, and that person is precisely waiting for company. It disappears on the same silence span. Closing it when the last guest stands up would take the table away from whoever set it up and is waiting for the first.
- **The node sees the speech and the board at a table — said plainly (2026-08-27).** The conversation key is derived for two and does not work here, while the lines are public and go through moderation — there is nothing to check in ciphertext. End-to-end encryption (`xor.ad/docs/chat_EN.md` §8.13) is about a conversation between two and does not extend to a table. This has to be on the screen: someone who read about encryption in a conversation will carry the expectation over.
- **Whoever joins does not see what came before.** The board arrives as it stands, the replies only from the moment they sat down (settled 2026-08-26). The same rule as moving an identity: history does not appear out of nowhere.
- **Talk at a table is public.** Replies go through the same moderation queue as the feed (`00-mechanics_EN.md` §5): strangers sit at a table, and "there are two of us, nobody sees" is not true here. The cost is named plainly: a 2.8 second median per reply is felt more at a table than in the feed.
- **Age bands — everyone with everyone.** You may join only if you are inside every sitter's band and they are inside yours (`xor.ad/docs/chat_EN.md` §8.2). The same rule as for a pair, applied to all at once.
- **The majority of those sitting can ask someone to leave.** Two out of three say "enough" and the person stands up. Nobody owns a table: the neighbour who started the game does not become its master.
- **A block hides the table entirely.** If someone you blocked is sitting there, the table is not shown to you at all. The cost is named: one person can hide someone else's game from you simply by joining it.
- **Someone outside the bands does not see the table at all — settled 2026-08-27.** No greyed card, no "you cannot join" line: such a card would itself report who is sitting where, and would tease a teenager with what is off limits. The cost is accepted: a person may not understand why a neighbour is talking about a table they cannot see.

## Open questions

- How a table looks in the feed: a card with the board, a line with the game's name, the number of sitters — undefined.
- How many replies a returning person sees if they left and came back: from scratch, or from where they left.
- What a person sees when they are told "come sit at the table" and the table is invisible to them by the bands — no separate explanation exists on the screen.
- **A line at a table carries the same "…" menu, with two items — decided 2026-08-28:** block the person and report. There is no "hide" here: you are sitting at the table, and hiding a line in a shared conversation makes no sense — what you leave is the table, not the line.
  **The report threshold does not apply at a table, and that is said plainly.** The threshold is a share of the possible audience with a floor of three people (§5 of the mechanics), and at a table the audience *is* three. Automatic hiding would mean one person removing a line from someone else's game; so a report here does two things — hides the line for whoever reported it and goes off as an Article 16 notice (`xor.ad/docs/dsa/SPEC_EN.md`, target `table_line`) — and there is no counter with a threshold at a table.
  **Blocking works as everywhere, but the consequence is larger:** the blocked person is sitting at this table, and the table disappears for you entirely (below).
- ~~How to report a line at a table~~ — **decided 2026-08-28, above.** The earlier note: Speech at a table is public and goes through the moderation queue, and on 2026-08-28 the DSA spec gave it a notice target of its own, `table_line` — so the lawful path exists while the interface path does not: no "…" menu, no button, no line on the screen. The fork is real, so it is not settled here: "hide" makes no sense at a table you are sitting at, "block" already hides the whole table, and what remains is a report — but a report means something different at a table, because the threshold counts against the audience, and at a table the audience is the three people seated.
