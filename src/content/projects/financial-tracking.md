---
name: Finance Tracker
order: 10
built: 2026-01-12
area: money
tagline: "One view of every brokerage account, built from pasted text and screenshots."
stack: [Python, Tesseract OCR, encrypted SQLite]
link: { kind: none, note: Runs locally on personal data }
---
Brokerages don't share a common export, so this takes whatever each one gives:
pasted position tables, CSV exports or a screenshot run through OCR. Each import
becomes a daily snapshot, so positions can be compared over time.

- Tracks unrealized and realized gains across accounts
- Shows allocation and position history
- Stores everything locally in an encrypted, password-protected database
