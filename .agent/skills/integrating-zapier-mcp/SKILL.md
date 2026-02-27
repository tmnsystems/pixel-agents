---
name: integrating-zapier-mcp
description: The step-by-step protocol for installing and configuring the Zapier Model Context Protocol (MCP). Use this when the user is ready to connect their AntiGravity system to external apps like Gmail, Calendar, or Google Tasks via Zapier.
---

# ⚡ Integrating Zapier MCP

This skill outlines the exact steps to give AntiGravity native read/write access to Gmail, Google Calendar, Google Docs, Google Tasks, and 8,000+ other apps without writing custom OAuth code.

## When to use this skill

- The user declares they are ready to "set up Zapier" or "connect the Zapier MCP".
- The user wants to integrate Google ecosystems after getting frustrated with n8n or failing API handshakes.

---

## 🛠️ The Setup Protocol (For the User)

Since this requires authenticating Google accounts in a secure browser window, you (the AI) cannot do Phase 1 autonomously. **Instruct the user to follow these steps** when they are ready:

### Phase 1: Authentication (Manual)

1. Open your browser and navigate to: [mcp.zapier.com/servers](https://mcp.zapier.com/servers)
2. Sign in or create a free Zapier account.
3. Once logged in, click **Add tool** (e.g., search for `Gmail` or `Google Tasks`).
4. Select all the tool capabilities you want AntiGravity to have.
   - _For Gmail:_ Select `Find Email`, `Create Draft`, `Create Email`, `Send Email`, `Get Attachments`.
5. Click **Connect** and go through the `Open Authorization` pop-up to allow Zapier to access your Google Account.
6. Once authorized, click **Add [X] Tools**. The server is now listening.

### Phase 2: Configuration Injection (Agentic)

Once the user confirms Phase 1 is done, you (the AI) must inject the MCP configuration into the local AntiGravity environment.

1. **Verify the Config Path**:
   Find the user's `mcp_config.json` depending on their IDE. (If they are using Claude Code globally or Cursor/Windsurf, the config path varies, but generally lives in `~/Library/Application Support/`). _Ask the user to point you to their mcp config if unknown._

2. **Inject the Server Block**:
   Append the Zapier server block to their MCP configuration:

   ```json
   "zapier": {
     "command": "npx",
     "args": [
       "-y",
       "@zapier/mcp-server"
     ],
     "env": {
       "ZAPIER_NLA_API_KEY": "YOUR_ZAPIER_API_KEY_HERE"
     }
   }
   ```

   _Note: Remind the user they will need to generate a Zapier NLA (Natural Language Actions) API key from their developer portal and paste it into the `.env` or config._

### Phase 3: The Smoke Test

Once the config is saved, reboot the agent IDE/Terminal.
Tell the user to run a test message to confirm the handshake:

> _"Hey, what is the subject line of the latest email in my inbox? You can use the Zapier MCP to check."_

If the AI accurately reads the inbox, the integration is complete. The system can now act as your absolute personal assistant.

---

## 🚫 Rate Limits & Context Rot Warning

**Critical Rule for the AI:** The Zapier MCP can add dozens of tools into the LLM context window at once. If not managed carefully, this will drain context windows incredibly fast.

Whenever the user is NOT actively using the Zapier tools for a specific task workflow, propose using a "Lazy Loader" or deactivating unused Zapier apps from the config to preserve speed and avoid loops.
