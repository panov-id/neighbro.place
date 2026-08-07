# Screen 13 — Devices

## Purpose

The screen showing every device of one identity, where a new one is connected and an unwanted one is disconnected. Opened from settings (screen 10).

## Elements

- The device list: a label such as "Chrome, Android", when it was connected, when it was last active, and a "this device" marker on the current one.
- A "connect a device" button — shows a QR code, with a link underneath for when there is no camera.
- The invite's countdown: two minutes, after which the code stops working.
- Every device except the current one has a "disconnect" button.

## Logic

- The invite is **single-use**: used or expired, it does nothing. A new one is made with the button.
- The key material sits **in the URL fragment**, after `#`. Browsers never send that to a server — not in the request, not in the referrer, not into logs. The key travels device to device past us.
- When a new device joins, the parent immediately **asks**: "a Chrome on Android device just joined — was that you?", with "yes" and "disconnect".
- A parent can disconnect its children; any device can disconnect itself.
- Disconnection takes effect **at once**: the device stops receiving and sending anything.

## What has to be said to the person

On the screen itself, not in small print:

> A disconnected device will not see a single new conversation. What is already open on it stays until those chats end.

This is not a disclaimer for legal tidiness — it is the truth about how the encryption works: the keys of already-open chats sit on that device, and they cannot be taken back (see `xor.ad/docs/chat_EN.md` §8.13).

The second thing said here:

> A connected device starts on an empty screen. Conversations opened before it joined will not appear on it.

## Open questions

- How long an invite should live — two minutes is a reasonable guess, untested on real people: is it enough time to reach the second device.
- Whether to show an approximate location of last activity in the list. It helps to spot someone else's device — but it is one more record about a person, which we do not keep today.
- What happens when the parent device is lost and a child remains: does the child become the parent.
