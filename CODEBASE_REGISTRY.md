# AntiGravity — Codebase Registry

> **Purpose:** A focused, up-to-date map of every system, tool, service, and automation in the AntiGravity project.
> **Last Updated:** 2026-02-13T22:10

---

## 🏗 Active Systems

### 1. AuntTBot (Telegram AI Assistant)
| Field | Value |
|-------|-------|
| **Location** | `/Users/alethea/Documents/AntiGravity/MyFreedomBot/` (separate from AntiGravity) |
| **Runtime** | Bun |
| **Framework** | Grammy (Telegram Bot) |
| **AI Model** | Claude Sonnet 4 (Anthropic API) |
| **Embeddings** | Ollama + nomic-embed-text (local) |
| **Database** | PostgreSQL + pgvector (Docker, port 5433) |
| **Status** | ✅ Production — runs 24/7 |
| **Key Feature** | Tele_* file bridge system to sync with AntiGravity |

### 2. Zoom Pipeline / Knowledge Extractor
| Field | Value |
|-------|-------|
| **Location** | `MyAiFreedomSystems/zoom-pipeline/` |
| **Runtime** | Bun |
| **Port** | Chat server on port 3334 |
| **Purpose** | Processes Zoom meeting recordings → sanitized transcripts → knowledge extraction |
| **Key Files** | `src/chat-server.ts`, `src/knowledge-extractor.ts` |
| **Status** | ✅ Running |

### 3. Coachinator / Redactinator-Sanitizer
| Field | Value |
|-------|-------|
| **Location** | `Coachinator/Redactinator---Sanitizer/` |
| **Backend** | Python + Streamlit (port 8502) |
| **Frontend** | Next.js (port 3009) |
| **AI Models** | Ollama (llama3.2) — local |
| **Database** | PostgreSQL + pgvector (Docker) |
| **Purpose** | PII sanitization + knowledge extraction pipeline |
| **Status** | 🚧 In progress — backend running, frontend needs local stack wiring |
| **Note** | `Coachinator copy/` is a working clone used for Docker experiments |

### 4. YouTube Transcript Fetcher
| Field | Value |
|-------|-------|
| **Location** | `youtube-transcripts/` |
| **Purpose** | Daily YouTube transcript acquisition for market intelligence |
| **Status** | 🚧 SOP written, needs automation scheduling |

### 5. Google Drive Integration
| Field | Value |
|-------|-------|
| **Location** | `scripts/auth.ts`, `scripts/scan_drive.ts`, `scripts/download_files.ts` |
| **API** | Google Drive API v3 (OAuth 2.0) |
| **Auth** | `credentials.json` + `token.json` (gitignored) |
| **Status** | ✅ Authenticated — scanner works, downloader needs syntax fix |

### 6. AI Voice Booking System
| Field | Value |
|-------|-------|
| **Location** | `AI-Voice-Booking-System/` |
| **Stack** | n8n + Retell AI + Cal.com (planned) |
| **Status** | 📋 Planned — `PLAN.md` written, needs Retell AI + Cal.com accounts |

### 7. Private Server Network
| Field | Value |
|-------|-------|
| **Location** | `private-server-network/` |
| **Purpose** | WireGuard VPN / secure server infrastructure |
| **Status** | 🚧 In progress |

### 8. Slack Bridge
| Field | Value |
|-------|-------|
| **Location** | `slack-bridge/` |
| **Purpose** | Slack ↔ Local AI bridge |
| **Status** | 🚧 In progress |

### 9. Insight Weaver
| Field | Value |
|-------|-------|
| **Location** | `Insight Weaver/` |
| **Purpose** | TBD — needs audit |
| **Status** | ❓ Unknown |

### 10. SanitizerChatBotMark
| Field | Value |
|-------|-------|
| **Location** | `SanitizerChatBotMark/` |
| **Purpose** | Earlier iteration of the sanitizer chatbot |
| **Status** | ❓ Likely superseded by Coachinator |

### 11. TheGraphicsAgent
| Field | Value |
|-------|-------|
| **Location** | `TheGraphicsAgent/` |
| **Frontend** | React + Vite (port 5173+) — `npm run dev` |
| **Backend API** | Express (port 3001) — `npm run api` |
| **AI Model** | `gemini-3.1-flash-image-preview` ("Nano Banana 2") via `@google/generative-ai` |
| **Auth** | `GOOGLE_AI_API_KEY` in `.env` — **requires billing-enabled key** (free tier has limit: 0 for this model) |
| **Purpose** | Image generation UI — prompt + aspect ratio + style → real AI-generated image |
| **Key Detail** | `responseModalities: ['TEXT', 'IMAGE']` required (not `['IMAGE']` alone) |
| **Status** | ✅ Working |

---

## 🧠 Skills (`.agent/skills/`)

| Skill | Trigger Keywords | Description |
|-------|---------|-------------|
| `cloning-protocol` | "clone this site", "re-skin", "brand swap" | 6-phase website re-branding system (Logo, Copy, Brands, Pricing, Reviews, Colors) |
| `error-handling` | "error handling", "retry logic", "circuit breaker" | Cross-language error handling patterns (Python, TS, Rust, Go) |
| `ghl-converter` | "GoHighLevel", "GHL", "single HTML file" | Converts React/Vite sites to single-file HTML for GHL page builder |
| `skill-creator` | "build me a skill", "create a new skill" | Meta-skill: teaches agents how to build new `.agent/skills/` directories |

---

## 📋 SOPs & Protocols (`sops/`)

| File | Type | Purpose |
|------|------|---------|
| `POLICY_coding_rules.md` | Policy | The 5 non-negotiable coding rules (1-3-1, DRY, TDD, Learning, Planning) |
| `POLICY_dual_storage_requirement.md` | Policy | Dual storage requirement for critical data |
| `SOP_YouTube_Transcript_Analysis.md` | SOP | How to analyze YouTube transcripts |
| `SOP_Firecrawl_Automation.md` | SOP | Web scraping + content generation with Firecrawl |
| `PROTOCOL_BLAST.md` | Protocol | 5-phase build methodology (Blueprint, Link, Architect, Stylize, Trigger) |
| `PROTOCOL_QA_Stress_Test.md` | Protocol | 9-phase QA & stress test for pre-delivery validation |
| `PLAYBOOK_First_Client.md` | Playbook | Client acquisition: niche selection → free deliverable → upsell to MRR |

---

## 📚 Knowledge Base

### `knowledge-base/courses/` — Course Materials
- M4L2: Creating agents that don't suck
- Module 5 Lesson 3: AI Agents in N8N
- Module 5 Lesson 4: Building Effective AI Agents
- Module 7 Lesson 1

### `knowledge-base/reference/` — Reference Documents
- AntiGravity Skills Creator.pdf
- Brand Design Skill.pdf
- Claude Code Zero to Hero.pdf
- Business Brain.pdf

---

## 🔄 n8n Workflows (`n8n-workflows/`)

| File | Description |
|------|-------------|
| `M4L2_AI_Agent_Airtable.json` | AI Agent with Airtable memory + Gmail auto-reply + LLM chains + sentiment analysis |
| `M5L3.json` | Module 5 Lesson 3 workflow |
| `M5L3_article_creator.json` | Article creator sub-workflow |
| `M5L3_outline_creator.json` | Outline creator sub-workflow |
| `M7L1.json` | Module 7 Lesson 1 workflow |

---

## 🔧 Key Ports & Services

| Service | Port | Protocol |
|---------|------|----------|
| Zoom Pipeline Chat Server | 3334 | HTTP |
| Coachinator Backend (Streamlit) | 8502 | HTTP |
| Coachinator Frontend (Next.js) | 3009 | HTTP |
| TheGraphicsAgent API | 3001 | HTTP |
| TheGraphicsAgent Frontend (Vite) | 5173+ | HTTP |
| PostgreSQL (AuntTBot) | 5433 | TCP |
| Ollama | 11434 | HTTP |

---

## 🔑 External API Dependencies

| Service | Used By | Auth Method |
|---------|---------|-------------|
| Anthropic (Claude) | AuntTBot, Zoom Pipeline | API Key (`.env`) |
| Google Drive API | Scripts | OAuth 2.0 (`token.json`) |
| Google AI (Gemini) | TheGraphicsAgent | API Key (`.env`) — billing required for Nano Banana 2 |
| Telegram Bot API | AuntTBot | Bot Token (`.env`) |
| Ollama (local) | Coachinator, AuntTBot | None (localhost) |

---

## 📂 Root Directory Quick Map

```
/Users/alethea/Documents/AntiGravity/
├── AGENT_START.md              # Constitution (read first)
├── BUILD_LOG.md                # Audit trail
├── CODEBASE_REGISTRY.md        # This file
├── .agent/skills/              # 4 installed skills
├── sops/                       # 7 SOPs, protocols, playbooks
├── knowledge-base/             # Courses, reference docs, plans
├── n8n-workflows/              # 5 importable n8n templates
├── scripts/                    # Google Drive integration scripts
├── logs/                       # Run outputs
├── Coachinator/                # Main sanitizer/extractor app
├── Coachinator copy/           # Docker experiment clone
├── MyAiFreedomSystems/         # Zoom pipeline (production)
├── AI-Voice-Booking-System/    # Planned voice booking system
├── youtube-transcripts/        # Daily transcript fetcher
├── catalog/                    # Infrastructure inventory
├── private-server-network/     # VPN setup
├── slack-bridge/               # Slack ↔ AI bridge
├── Insight Weaver/             # TBD
├── SanitizerChatBotMark/       # Legacy chatbot
├── AiEntrepreneurCourse antigravity/  # Course materials
└── User Update Temp/           # Inbox for user-uploaded files
    └── archive/                # Processed files (do NOT re-process)
```
