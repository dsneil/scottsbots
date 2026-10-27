---
name: GoveeLights
built: 2026-01-02
area: home
tagline: "Desk lights that follow my PC — on when it wakes, off when it sleeps."
stack: [Node.js, PowerShell, Govee LAN API]
link: { kind: soon }
---
Windows scheduled tasks watch for wake, sleep, lock and shutdown events and send
commands to Govee lights over the local network. Daytime is cool white, night is
warm amber.

- Talks to the lights over UDP on the LAN, no cloud account involved
- Retries each command because UDP drops packets
- One installer registers every scheduled task; one uninstaller removes them
