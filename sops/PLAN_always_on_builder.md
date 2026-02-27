# PLAN: Always-On Builder (Our Own Sovereign Agent System)

> **Status:** APPROVED — In Progress
> **Created:** 2026-02-13
> **Approved by:** Tina Marie
> **Approach:** No cloning. Understand concepts, write original code.

---

## Goal

Extend MyFreedomBot into an autonomous builder that works while Tina is away.
The builder uses ALL available AI models as a Cooperative Model Council —
no model left out, each contributing its unique perspective.

---

## The Cooperative Model Council

Every model has a role. Every model is used. No exceptions.

| Model | API Provider | Role | Fallback |
|---|---|---|---|
| **Claude Opus 4.6 (Thinking)** | Anthropic | Architect — complex decisions, system design | Claude Opus 4.5 |
| **Claude Opus 4.5 (Thinking)** | Anthropic | Senior Reviewer — second opinion on architecture | Claude Sonnet 4.5 (Thinking) |
| **Claude Sonnet 4.5 (Thinking)** | Anthropic | Builder+ — implementation with deep reasoning | Claude Sonnet 4.5 |
| **Claude Sonnet 4.5** | Anthropic | Builder — fast implementation, daily tasks | Claude Opus 4.5 |
| **Gemini 3 Pro (High)** | Google AI | Cross-family Reviewer — catches what Claude misses | Gemini 3 Pro (Low) |
| **Gemini 3 Pro (Low)** | Google AI | Lightweight cross-check — fast Gemini validation | Gemini 3 Flash |
| **Gemini 3 Flash** | Google AI | Speed Reviewer — instant sanity checks | Gemini 3 Pro (Low) |
| **GPT-OSS 120B (Medium)** | OpenAI | Third Perspective — different reasoning entirely | Gemini 3 Pro (High) |
| **Ollama (local)** | Local | Librarian — embeddings, PII scan, private ops | OpenAI embeddings (existing) |

### Model API Keys Required
- `ANTHROPIC_API_KEY` — ✅ Already configured
- `GOOGLE_AI_API_KEY` — Needed for Gemini models
- `OPENAI_API_KEY` — ✅ Already configured
- Ollama — ✅ Runs locally, no key needed (fallback: OpenAI embeddings)

### Review Chain Protocol
For every task that produces code or content:
1. **Build** → Sonnet 4.5 (Thinking) writes it
2. **Review 1** → Gemini 3 Pro (High) reviews — different AI family perspective
3. **Review 2** → GPT-OSS 120B reviews — third family perspective
4. **Architecture check** → Opus 4.6 validates against Constitution & mission
5. **Security scan** → Ollama checks for PII/secrets locally (fallback: Haiku)
6. **Agreement** → All reviewers agree → mark complete
7. **Disagreement** → Flag for human review, move to next task

---

## Architecture

### What Already Exists
```
/Users/alethea/Documents/AntiGravity/MyFreedomBot/
├── src/
│   ├── config.ts          ← Model config, bot name, DB credentials
│   ├── ai/claude.ts       ← Anthropic API integration
│   ├── memory/postgres.ts ← PostgreSQL memory (pgvector)
│   ├── scheduler/proactive.ts ← 30-min interval scheduler
│   ├── telegram/bot.ts    ← Telegram interface
│   └── tools/filesystem.ts ← File read/write tools
├── workspace/             ← Sandboxed file workspace
├── backups/               ← Daily DB backups
└── .env                   ← API keys and config
```

### What We're Adding
```
/Users/alethea/Documents/AntiGravity/MyFreedomBot/
├── src/
│   ├── ai/
│   │   ├── claude.ts      ← EXISTS — extend with Opus/Haiku model variants
│   │   ├── gemini.ts      ← NEW — Google AI API integration
│   │   ├── openai.ts      ← NEW — GPT-OSS API integration
│   │   ├── ollama.ts      ← NEW — Local Ollama integration
│   │   └── council.ts     ← NEW — Model router + review chain orchestrator
│   ├── tools/
│   │   ├── filesystem.ts  ← EXISTS — file read/write
│   │   └── executor.ts    ← NEW — Sandboxed code execution via Docker
│   ├── tasks/
│   │   ├── queue.ts       ← NEW — Task queue (PostgreSQL-backed)
│   │   ├── runner.ts      ← NEW — Task lifecycle manager
│   │   └── reporter.ts    ← NEW — Generates summary reports
│   ├── testing/
│   │   └── tester.ts      ← NEW — Visual QA (headless browser + screenshots)
│   └── scheduler/
│       └── proactive.ts   ← EXTEND — add task queue checking
└── AGENT_SWARM_STATE.md   ← NEW — Human-readable job board mirror
```

---

## Component Specifications

### 1. Model Router (`council.ts`)

```typescript
// Routes requests to the right model based on task type
interface ModelRequest {
  task: string;
  type: 'build' | 'review' | 'architecture' | 'security' | 'quick-check' | 'embedding';
  content: string;
  context?: string;
}

// Routing table:
// build         → Sonnet 4.5 (Thinking)
// review        → Gemini 3 Pro (High) → GPT-OSS 120B → Opus 4.6
// architecture  → Opus 4.6 (Thinking)
// security      → Ollama local (fallback: Sonnet 4.5 with security prompt)
// quick-check   → Gemini 3 Flash
// embedding     → Ollama nomic-embed-text (fallback: OpenAI)
```

### 2. Task Queue (`queue.ts`)

PostgreSQL table:
```sql
CREATE TABLE task_queue (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  status TEXT DEFAULT 'unclaimed',  -- unclaimed, claimed, building, reviewing, complete, flagged
  priority INTEGER DEFAULT 5,       -- 1 = highest
  assigned_model TEXT,
  claimed_at TIMESTAMP,
  completed_at TIMESTAMP,
  result TEXT,
  review_notes JSONB,              -- { gemini: "...", gpt: "...", opus: "..." }
  files_created TEXT[],            -- paths of files produced
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 3. Sandboxed Executor (`executor.ts`)

- Spawns a Docker container for code execution
- Container has: Node.js, Python, Bun, basic unix tools
- Container does NOT have: network access, host filesystem, API keys
- Timeout: 5 minutes per execution
- Output captured and returned to the calling model
- All produced files written to workspace with Tele_ prefix

### 4. Task Runner (`runner.ts`)

Lifecycle:
```
unclaimed → claimed (bot picks it up)
  → building (Sonnet 4.5 working)
    → reviewing (Gemini + GPT-OSS + Opus reviewing)
      → complete (all agree) OR flagged (disagreement)
```

### 5. Reporter (`reporter.ts`)

When Tina returns, generates:
```
═══════════════════════════════════════
  OVERNIGHT REPORT — Feb 14, 2026
═══════════════════════════════════════

  ✅ Completed: 4 tasks
  ⚠️  Flagged for review: 1 task
  📁 Files created: 12
  📸 Screenshots taken: 8
  🤖 Models used: Sonnet 4.5, Gemini 3 Pro, GPT-OSS, Opus 4.6, Gemini Flash
  ⏱️  Total runtime: 3h 22m
  
  TASK 1: Budget App UI [COMPLETE]
    Built by: Sonnet 4.5 (Thinking)
    Reviewed by: Gemini 3 Pro ✅, GPT-OSS ✅, Opus 4.6 ✅
    Visual QA: Gemini 3 Flash ✅ (screenshots attached)
    Files: Tele_budget_ui.html, Tele_budget_styles.css
    
  TASK 2: Council Policy [COMPLETE]
    Built by: Sonnet 4.5
    Reviewed by: Gemini 3 Pro ✅, GPT-OSS ✅, Opus 4.6 ✅
    Files: Tele_POLICY_cooperative_model_council.md
    
  TASK 5: Refactor auth system [FLAGGED]
    Built by: Sonnet 4.5 (Thinking)
    Gemini 3 Pro: ✅ Approved
    GPT-OSS: ⚠️ "Edge case in token refresh logic"
    Opus 4.6: ⚠️ "Agrees with GPT-OSS, needs human decision"
    → Waiting for your review
═══════════════════════════════════════
```

### 6. Visual QA Tester (`tester.ts`)

For any task that produces a web UI or localhost app:
- **Launches headless browser** (Puppeteer) against `localhost:<port>`
- **Takes screenshots** of every page/state
- **Interacts with the app** — clicks buttons, fills forms, navigates
- **Captures results** — what happened, did it error, does it look right
- **Sends screenshots to a vision model** (Gemini 3 Flash or GPT-OSS) for visual verification
- **Reports:** "Button X works ✅", "Form Y throws error ❌", "Layout broken on mobile ⚠️"

```
Build complete → Start localhost server → Tester opens browser
  → Screenshots: homepage, each nav page, form states
  → Interactions: click every button, submit forms, test edge cases
  → Send screenshots to vision model: "Does this look correct?"
  → Vision model reviews → Pass/Fail with notes
  → Screenshots saved to workspace/screenshots/ for human review
```

---

## Build Order

1. ~~**Read existing codebase** — understand current tool system, AI integration, scheduler~~ ✅
2. ~~**`council.ts`** — model router with ALL nine models + fallbacks~~ ✅
3. ~~**`gemini.ts` + `openai.ts` + `ollama.ts`** — API integrations~~ ✅ (routed through council.ts)
4. ~~**`queue.ts`** — task queue in PostgreSQL~~ ✅
5. ~~**`executor.ts`** — sandboxed Docker code execution~~ ✅ (+ council approval for destructive ops)
6. ~~**`runner.ts`** — task lifecycle manager~~ ✅ (+ User Update Temp folder monitoring)
7. ~~**`reporter.ts`** — overnight report generator~~ ✅
8. ~~**`tester.ts`** — visual QA with headless browser + vision model screenshots~~ ✅
9. ~~**Extend `proactive.ts`** — scheduler checks task queue~~ ✅ (+ morning reports at 7 AM)
10. ~~**Integration test** — load a test task, run the full pipeline~~ ✅ (visual QA demo on Catalog Dashboard)
11. ~~**`POLICY_cooperative_model_council.md`** — document the philosophy~~ ✅

---

## Safety Rules

1. All output files use `Tele_` prefix — nothing deployed without human approval
2. Code execution is sandboxed in Docker — no host access
3. Destructive operations (delete, overwrite) queue for human approval
4. Three AI families must review before any task is marked complete
5. Full audit log of every model call, every file change, every decision
6. Constitution (`AGENT_START.md`) is loaded into every model's context
7. Daily database backups protect task history and memory

---

## API Keys Status

- [x] `ANTHROPIC_API_KEY` — Configured
- [x] `GOOGLE_AI_API_KEY` — ✅ Configured (free tier, resets daily)
- [x] `OPENAI_API_KEY` — Configured
- [x] Ollama — Local, no key needed

---

*This plan follows Rule 5 (Planning First) and the Code Sovereignty policy.
Every line of code will be written by us, from scratch.*
