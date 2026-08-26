# Screen 14 — Support

## Purpose

A support contact button, reachable from the app at any time.

## Screen elements

- A support button/icon — always available.
- A message input for the support request.
- A send button.

## Logic

- The sent message lands in a table of our own database, beside the node.
- A new ticket fires a notification (email/webhook) for the team.
- There's no automated handling — just logging the request and notifying the team.
- **A confirmation is shown immediately**, with a request number: a person has to see that they were heard (settled 2026-08-26).
- **Email is optional and asked only of those who want an answer.** The product lives without email by construction, and collecting it where it can be avoided means creating a record about a person for nothing. For Article 16 complaints an answer is mandatory — that is where the address will be needed.

## Open questions

- Exactly where the button is reachable from (feed header, settings, a separate icon) is not defined yet.
- ~~Confirmation and reply~~ — settled 2026-08-26 (above).
