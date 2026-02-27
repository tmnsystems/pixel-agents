---
description: Rule - always restart system components after stopping them
---

# System Component Restart Rule

**Rule:** Anytime you stop a system component (bot, database, server, etc.), you MUST restart it before finishing your work. Never leave a system component in a stopped state.

This applies to:
- The Telegram bot (`bun run index.ts` in AlwaysOnAgent)
- PostgreSQL (if you restart it for config changes)
- Ollama (if you restart it for model changes)
- Any dev server you start for testing
- Any background process you launched

## How to restart the bot
```bash
cd /Users/alethea/Documents/AntiGravity/MyFreedomBot && bun run index.ts
```

## Why this matters
Tina relies on the bot being available via Telegram. If you stop it and forget to restart, she has no way to reach the bot until the next IDE session. Always leave things running.
