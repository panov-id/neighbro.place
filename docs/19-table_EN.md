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
- Who is sitting is visible, **and since 2026-09-10 that is two numbers: "N playing, M watching"**. A single number would have lied to expectation: somebody saw "six at the table", sat down and found two playing with a queue of four ahead of them. When anyone was last online is still not shown, as everywhere else.

## Logic

- **A table does not consume the posting quota — decided 2026-08-30.** The mechanics said as much about offers in plain words and stayed silent about tables, although they are placed from the same composer and stand in the same feed. Decided in favour of "does not": a table is a **meeting place, not an utterance**, and paying for it with a voice in the feed would be wrong. Putting up a table and speaking in phrases are different things, and one must not take the other away.
- **There is no per-person count of tables, but there is a share of the feed — decided 2026-09-02, and the price is named.** Offers have a share of their own (one card per ten ordinary ones); tables get no more than a quarter of the delivery's cards (in full below, among the open questions). Any number can be created and a table still spends no phrase quota: the limit sits on the showing, not on the person. The neighbourhood's feed is protected from being flooded with tables, and the author is not punished for calling people to play. **Edited 2026-09-04 after the review panel:** this said "no share of the feed… the limiter is not described", dated 2026-08-30 — the line argued with its own section below, where that limiter was settled three days later.
- **Stickers exist at a table, as they do in a conversation — decided 2026-08-30.** The same catalogue, the same "one sticker instead of a line" rule, the same name for the terminal and the screen reader (screen 16).
  **But there is a difference, and it is spoken on screen:** in a conversation the sticker's identifier travels inside the ciphertext and the node does not know which sticker was sent; **at a table there is no encryption by construction**, and the node sees the sticker exactly as it sees the lines and the board. Hiding that is out for the same reason the screen already states the visibility of speech: someone who read about stickers in a conversation will carry the expectation here.
  **A sticker needs no moderation queue** even here: the images and the names are ours, from the catalogue, and a user cannot send their own.
- **No hard cap on numbers.** As many as sit down, play; the limit is the readability of the board, not a rule.
- **A table lives from its last move — on one span shared by everyone** (clarified 2026-08-27). A move or a line from any sitter pushes it alike. This differs from a conversation, where each side has its own count: there two people are involved, while here the company changes, and a separate count would mean the table exists in different states for those sitting at it. When they leave it disappears with the board and everything said at it.
- **A table with one sitter is a normal state** (settled 2026-08-27): it is visible in the feed, people can pull up a chair, and that person is precisely waiting for company. It disappears on the same silence span. Closing it when the last guest stands up would take the table away from whoever set it up and is waiting for the first.
- **The node sees the speech and the board at a table — said plainly (2026-08-27).** The conversation key is derived for two and does not work here, while the lines are public and go through moderation — there is nothing to check in ciphertext. End-to-end encryption (`xor.ad/docs/chat_EN.md` §8.13) is about a conversation between two and does not extend to a table. This has to be on the screen: someone who read about encryption in a conversation will carry the expectation over.
- **Whoever joins does not see what came before.** The board arrives as it stands, the replies only from the moment they sat down (settled 2026-08-26). The same rule as moving an identity: history does not appear out of nowhere.
- **Talk at a table is public.** Replies go through the same moderation queue as the feed (`00-mechanics_EN.md` §5): strangers sit at a table, and "there are two of us, nobody sees" is not true here. The cost is named plainly: a 2.8 second median per reply is felt more at a table than in the feed.
- **Age bands — everyone with everyone.** You may join only if you are inside every sitter's band and they are inside yours (`xor.ad/docs/chat_EN.md` §8.2). The same rule as for a pair, applied to all at once.
- **"Play again" is a proposal, not a command (decided 2026-08-29).** A game has ended — the table stays; those who agree play on, and **whoever declines stops playing but stays as a spectator** (clarified 2026-09-09: with applications in place, sitting and playing are different things, and "not another game" stopped meaning "I am leaving these people"). To play again they apply like anybody else, and they may not be taken back. If one person is left, the table does not close but waits: that is the normal state described below. If everyone declines, the table goes with the game.
- **An undo at a table takes the agreement of everyone playing (decided 2026-08-29, clarified 2026-09-09, screen 18).** Everyone playing, not everyone seated: a spectator is not in the game, and letting them block a take-back would give power over a game to somebody who does not move in it. The more people, the more expensive it is to take a move back, and that is deliberate: a cheap undo in company is precisely how somebody else's game gets spoiled.
- **A move has a deadline — 5 minutes, then a pass (decided 2026-09-10).** The
  engine has been checking the turn order since 2026-09-09, so the game used to
  stop on whoever was not there: left, shown out, or with the phone put down —
  the others waited for the table to die. A missed move becomes a pass, and
  **3 passes in a row make a spectator** — the same as an unconfirmed roster.
  The five minutes are **chosen, not measured**, and chosen at the upper bound:
  that is how long you may think in chess without being absent. The cost is
  named: a pass will land on someone who was thinking.
- **The majority of those sitting can ask someone to leave.** Two out of three say "enough" and the person stands up. Nobody owns a table: the neighbour who started the game does not become its master.
- **Sitting down and playing are different things (decided 2026-09-09).** Whoever
  sits down gets **the chat and the board**; to play, they apply **for the next
  round**. A game in progress is not interrupted by anyone arriving — otherwise
  "sit down" would mean stepping into other people's game halfway through.
  **A spectator sees the whole board except the hands.** A hand is private by
  construction and visible only to its owner (`xor.ad/docs/chat_EN.md` §6), so a
  spectator cannot whisper anybody's cards — nobody but the holder sees them.
- **The play is visible in the table's conversation — decided 2026-09-09.** Every
  move becomes a line ("Anya placed a tile on e4") and stands in the table's feed
  alongside the speech. It needs no moderation queue: the engine composes the text
  from the class of board and a coordinate. It is cut off at the moment of sitting
  down, like everything else: somebody who sat down does not see the moves made
  before them. **Why:** a spectator sees the board but could not tell what had
  happened, and somebody returning to a table starts from nothing and catches up
  through the lines.
  **There is no "…" menu on lines of play (2026-09-10):** there is nothing to report and nothing to hide — the text is machine-made, it has no author, and it is never the target of an Article 16 notice.
- **Game state and the score at a table live in the database — decided 2026-09-09**
  (`table_games` and `table_scores`, `xor.ad/docs/chat_EN.md` §6.1). In a pair the
  game sits in a cache with the conversation's span; here it sits beside the
  table — at a table speech and board
  are public by construction, and there is nobody to hide the state from. **The read cuts
  out what is hidden — three kinds of it, clarified 2026-09-10:** the hand, the
  undrawn stock (boneyard, deck) and the guessed word. The node sees everything and
  hands over only what is declared open — your own hand and the backs of the others, and this is the only
  place where the answer depends on who is asking.
- **The line-up for a new game is confirmed — 30 seconds (decided 2026-09-09).**
  Once "play again" is pressed, everyone who was playing and everyone whose
  application was accepted gets a confirmation: **30 seconds** to say "I am here".
  Whoever does not confirm is not thrown out — they **become a spectator**, and can
  return to the game by applying.
  **A game, a round and a move are different things:** the confirmation is asked
  per game, not per round, or dominoes would turn into a questionnaire.
  **In a pair there is no count at all — decided 2026-09-10:** "1 of 2 confirmed"
  is a binary answer about a named person — "my opponent is at their screen" —
  exactly the presence indicator the product does not have. In a pair a button
  and a countdown remain, and the other side's confirmation shows as a result:
  the game started, or it did not. The cost: thirty seconds of silence in a pair
  read as a freeze.
  **The others see a count without names** — "2 of 4 confirmed" and a countdown. A
  list by name would be the very presence indicator the product has nowhere (see
  above on "when somebody was last online").
  Thirty seconds are **chosen, not measured**: enough for somebody with the phone
  in hand, not enough for somebody who put it down — and the second is what needs
  filtering out.
- **A "congratulate the winner" button (2026-09-09)** — an addressed gesture, not a
  verdict: the engine knows no rules and cannot decide a winner. Whoever presses it
  picks who they congratulate, and a line appears at the table. No score and no
  history of wins is kept.
- **The application is opening words, the refusal is an explanation, and both are
  visible to everyone at the table.** Ordinary lines: the same moderation queue,
  the same 128 characters, the same report. An addressed application "to the
  players only" would have introduced a private message to a stranger with no
  mutual like — which exists nowhere. The price is accepted and it is unpleasant:
  a public "we are not taking you, because…" is read by everyone sitting there.
- **The players decide, and a silent refusal is not allowed.** Those in the game
  vote; spectators do not decide who gets in. The refuse button stays inactive
  until an explanation is written. The deadline is **the start of the next
  round**: whoever has not objected by then did not object.
  **An application is only made for a free seat — decided 2026-09-10.** No seats and
  the button is inactive, saying why: "no seats, wait for the game to end".
  Otherwise a table for two with twenty hopefuls gathered twenty public lines and
  the conversation at the table drowned in them. The cost: whoever taps at the right
  moment sits down, not whoever waited longest; a table of neighbours has no queue
  with a number and a deadline.
  **What lets you in is a free seat, not silence — clarified 2026-09-10.** This
  used to mean that anyone unopposed was taken: consent cost nothing, a refusal
  cost public words. Now a game has its own number of seats (chess two, dominoes
  up to four), and those unopposed sit down **in the order they applied**, while
  seats last. Whoever does not fit is not refused: they are an applicant for the
  next round.
- **One table at a time (decided 2026-09-09).** Sitting down at a second table
  without standing up from the first is refused. That is also what guards the feed
  against being buried: set up as many tables as you like, but sit at one, and a
  table nobody is sitting at does not reach the feed.
- **Tables reach the quarter of the feed at random, and the quarter is counted
  after blocks (decided 2026-09-09).** Not "the liveliest first": a table with one
  person sitting at it makes no moves — it is waiting for a guest — and any order
  by activity would bury exactly the tables this screen exists for. The price: the
  selection is not stable between refreshes and a table you saw can be lost —
  there is a way back to your own, the line in the header. The quarter is counted
  against what a person can see, or whoever blocked somebody would see fewer
  tables than their neighbour, and a block would quietly punish the person who
  used it.
- **Being shown out is not being locked out — decided 2026-09-08** (`xor.ad/docs/chat_EN.md` §6). No "may not return" list is kept: that is a trace about a person, and the product promises no trace is left. Until somebody blocks, the person shown out sits back down with the same gesture, as often as they like.
  What locks the door is not a list but a **block**, and it is stronger than it looks: the check is symmetric, so one side is enough. One person at the table blocks, and the table disappears not only for them but for the person shown out, who then has nowhere to come back to. The price is accepted: between the eviction and the block there is a gap, and in it an eviction is a request to leave rather than a lock.
- **A block separates at the seat — rewritten 2026-09-10.** A table with someone you blocked at it is still not shown to you, and **sitting down beside each other is refused both ways**: neither them into a table where you sit, nor you into one where they do. This used to read "one person can hide someone else's game from you simply by joining it" — and that was not the whole cost: by joining a game in progress, an outsider cut it off for you mid-move, and for the others at the table for no reason at all.
  **A table does not vanish and come back instantly — decided 2026-09-10:** the set
  of visible tables is computed when the feed is opened. Otherwise "block, look,
  unblock" would answer whether a named person is at a table right now — and the
  product shows nowhere who is at their screen. The cost: after lifting a block you
  will not see the table straight away.
  **If the block happens while you are already at the same table,** the game ends and the one who leaves is **whoever did the blocking**. That is said before the button, not after: the cost falls on whoever made the decision.
- **Someone outside the bands does not see the table at all — settled 2026-08-27.** No greyed card, no "you cannot join" line: such a card would itself report who is sitting where, and would tease a teenager with what is off limits. The cost is accepted: a person may not understand why a neighbour is talking about a table they cannot see.

## Open questions

- ~~There is no limiter on the number of tables~~ — **a share of the delivery: no more than a quarter of the feed's cards (decided 2026-09-02)**. Any number can be created and a table still spends no phrase quota: the limit sits on the showing, not on the person. The feed is protected and the author is not punished for calling people to play. The price is accepted: the delivery gains one more rule, and the question "why is my table not visible" now needs an answer (`00-mechanics_EN.md` §4).
- How a table looks in the feed: a card with the board, a line with the game's name, the number of sitters — undefined.
- ~~How many replies a returning person sees~~ — **from scratch, as a newcomer** (decided 2026-09-02). One rule for everyone, and it is already in the schema: the reply feed is cut by the moment of sitting down, and someone who left sits down anew. The price is named outright: step away for a minute and you lose the thread; a per-person mark of leaving would break the simplicity of "a newcomer sees nothing from before".
- ~~What a person sees when they are told "come sit at the table" and the table is invisible to them by the bands~~ — **the same as for anything that does not exist: the table is not there, and no reason is given** (decided 2026-09-03). The rule follows the one taken above: a table outside your bands is not shown at all, because a greyed-out card would itself say who is sitting where. A line saying "this table is not for your age" would say exactly the same thing, in words.
  The price is accepted and it is unpleasant: someone who was invited walks into nothing and does not know why. That is cheaper than confirming the table exists and how old the people at it are, and whoever invited them can see them and will explain.
- **A line at a table carries the same "…" menu, with two items — decided 2026-08-28:** block the person and report. There is no "hide" here: you are sitting at the table, and hiding a line in a shared conversation makes no sense — what you leave is the table, not the line.
  **The report threshold does not apply at a table, and that is said plainly.** The threshold is a share of the possible audience with a floor of three people (§5 of the mechanics), and at a table the audience *is* three. Automatic hiding would mean one person removing a line from someone else's game; so a report here does two things — hides the line for whoever reported it and goes off as an Article 16 notice (`xor.ad/docs/dsa/SPEC_EN.md`, target `table_line`) — and there is no counter with a threshold at a table.
  **Blocking works as everywhere, but the consequence is larger:** the blocked person is sitting at this table, and the table disappears for you entirely (below).
- ~~How to report a line at a table~~ — **decided 2026-08-28, above.** The earlier note: Speech at a table is public and goes through the moderation queue, and on 2026-08-28 the DSA spec gave it a notice target of its own, `table_line` — so the lawful path exists while the interface path does not: no "…" menu, no button, no line on the screen. The fork is real, so it is not settled here: "hide" makes no sense at a table you are sitting at, "block" already hides the whole table, and what remains is a report — but a report means something different at a table, because the threshold counts against the audience, and at a table the audience is the three people seated.
