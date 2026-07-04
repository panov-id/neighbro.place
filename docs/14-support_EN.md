# Screen 14 — Support

## Purpose

A support contact button, reachable from the app at any time.

## Screen elements

- A support button/icon — always available.
- A message input for the support request.
- A send button.

## Logic

- The sent message lands in a Supabase table.
- A new ticket fires a notification (email/webhook) for the team.
- There's no automated handling or reply — just logging the request and notifying.

## Open questions

- Exactly where the button is reachable from (feed header, settings, a separate icon) is not defined yet.
- Whether the user gets any send confirmation/reply is not defined yet.
