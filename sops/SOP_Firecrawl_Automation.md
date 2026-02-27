# Firecrawl Automation Process

This Standard Operating Procedure (SOP) outlines the process for setting up an automated web scraping and content generation workflow using Firecrawl MCP, OpenAI, and Gmail within Antigravity.

Based on: [This Scraper Changes Everything | Google Antigravity Tutorial](https://www.youtube.com/watch?v=kirtFabtWno)

## Prerequisites

*   Firecrawl Account & API Key
*   OpenAI Account & API Key
*   Google Cloud Console Account
*   Antigravity Environment

## 1. Agent Instruction Setup (The "Brain")

1.  Create an instruction file (e.g., `gemini.md` or similar instruction file in your workspace).
2.  Define the persona and objectives for the AI agent to ensure consistent behavior for scraping and content generation.

## 2. Connect Firecrawl MCP

This enables the agent to scrape websites.

1.  **Access MCP Configuration**:
    *   In Antigravity, click the three dots (top right) -> **MCP Servers**.
    *   If Firecrawl is listed, install it. If not, proceed to manual configuration.
2.  **Manual Configuration** (if needed):
    *   Go to the Firecrawl dashboard.
    *   Copy the provided MCP integration code snippet.
    *   In Antigravity, click **View Raw Config** (or ask the agent to add it).
    *   Paste the configuration.
    *   **CRITICAL**: Replace the API Key placeholder in the config with your actual Firecrawl API Key.
    *   Save the file (`Command + S`).
    *   Refresh Antigravity. Firecrawl should now appear as a connected tool.

## 3. Identify Data Sources

1.  Instruct the agent to find reliable sources.
    *   *Prompt Example*: "Search for 5-10 reliable AI news sites using Firecrawl and return the links."
2.  Verify the links provided by the agent. These will be the targets for the daily scrape.

## 4. Connect OpenAI (The Processor)

This allows the agent to process scraped data and generate content.

1.  Go to [platform.openai.com](https://platform.openai.com).
2.  Navigate to **API Keys** -> **Create new secret key**.
3.  Name it (e.g., "Scraper").
4.  Copy the key.
5.  Add the key to your Antigravity environment (e.g., via `.env` file or secure agent instructions).
    *   *Security Note*: Ensure API keys are stored securely and not exposed in public repositories.

## 5. Connect Gmail (The Delivery Mechanism)

This enables the agent to email the generated reports/posts to you.

1.  **Google Cloud Console Setup**:
    *   Go to Google Cloud Console.
    *   Create a **New Project** (name it e.g., "Scraper").
    *   Select the project.
2.  **Enable Gmail API**:
    *   Go to **APIs & Services** -> **Library**.
    *   Search for "Gmail API" and **Enable** it.
3.  **OAuth Consent Screen**:
    *   Go to **OAuth consent screen**.
    *   User Type: **External**.
    *   Fill in required fields (App Name: "Scraper", Support Email, Developer Contact).
    *   **Test Users**: Add your own email address as a test user. This is critical for testing without full verification.
    *   Save and Continue.
4.  **Create Credentials**:
    *   Go to **Credentials** -> **Create Credentials** -> **OAuth client ID**.
    *   Application Type: **Desktop app**.
    *   Name: "Antigravity Scraper".
    *   Click **Create**.
    *   **Download JSON**: Download the client secret JSON file.
5.  **Authenticate in Antigravity**:
    *   Drag and drop the downloaded JSON file into your Antigravity workspace.
    *   Instruct the agent: "I added the client secret. I would like to connect my Gmail."
    *   Follow the authentication flow (browser popup) to allow the app to send emails on your behalf.
    *   Confirm to the agent that authentication is done.

## 6. Define the Workflow

1.  **Scrape & Summarize**:
    *   Instruct the agent to use Firecrawl to scrape the identified news sites.
2.  **Generate Content**:
    *   Ask OpenAI to process the content.
    *   *Prompt Example*:
        *   "Create an in-depth analysis of AI news for me (technical)."
        *   "Create 3 conversational/viral LinkedIn posts based on these news items for my community."
3.  **Email Delivery**:
    *   Instruct the agent to compile the analysis and posts into an email.
    *   send this email to your inbox every morning (or on trigger).

## 7. Execution

*   Run the workflow functionality to generate the posts.
*   Review the output (e.g., "I like variants 3 and 4, but remove hashtags").
*   Confirm the final version.
