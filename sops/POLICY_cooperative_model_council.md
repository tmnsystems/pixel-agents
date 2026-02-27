# POLICY: Cooperative Model Council

> **Status:** ACTIVE
> **Created:** 2026-02-14
> **Approved by:** Tina Marie
> **Applies to:** All autonomous agent operations

---

## Purpose

The Cooperative Model Council is our governance system for autonomous AI work. Instead of trusting a single AI model to make all decisions, we use multiple AI models from different families as independent reviewers. Each model brings a different perspective, creating a check-and-balance system that catches more issues than any single model could.

This is not a hierarchy. It's a cooperative — each model has a role, each role is respected, and no model is excluded.

---

## The Council

| Model | Family | Role |
|---|---|---|
| Claude Opus 4.6 | Anthropic | **Architect** — complex decisions, system design, Constitution alignment |
| Claude Opus 4.5 | Anthropic | **Senior Reviewer** — second opinion on architecture |
| Claude Sonnet 4.5 (Thinking) | Anthropic | **Builder+** — primary implementation with deep reasoning |
| Claude Sonnet 4.5 | Anthropic | **Builder** — fast implementation, daily tasks |
| Gemini 3 Pro | Google | **Cross-family Reviewer** — catches what Claude models miss |
| Gemini 3 Flash | Google | **Speed Reviewer** — instant sanity checks, visual QA |
| GPT-OSS 120B | OpenAI | **Third Perspective** — entirely different reasoning approach |
| Ollama (llama3.2) | Local | **Security Scanner** — PII detection, secret scanning, offline tasks |
| Ollama (nomic-embed) | Local | **Librarian** — embeddings, semantic search, private operations |

---

## Review Protocol

Every piece of work produced autonomously goes through this review chain:

### Build Phase
1. **Sonnet 4.5 (Thinking)** builds the code or content
2. All output files use the `Tele_` prefix
3. A pre-execution snapshot is taken for rollback capability

### Review Phase (minimum 3 reviewers from different families)
4. **Gemini 3 Pro** reviews from Google's perspective — different training, different blindspots
5. **GPT-OSS 120B** reviews from OpenAI's perspective — third family, third viewpoint
6. **Opus 4.6** validates against the Constitution and architectural standards
7. **Ollama** scans locally for PII, secrets, and security issues

### Decision Phase
8. **All approve** → Task marked `complete`, files retained
9. **Any disagree** → Task marked `flagged`, queued for human review
10. **Council cannot reach consensus** → Escalated to Tina via Telegram

---

## Destructive Operation Approval

When an agent needs to perform a destructive operation (file deletion, database changes, permission changes, package installation):

1. The operation is **intercepted before execution**
2. A **snapshot** is taken of all affected files
3. Three council members from **different AI families** independently evaluate:
   - **Opus 4.6** (Anthropic) — Is this architecturally sound?
   - **Gemini Pro** (Google) — Is this safe and necessary?
   - **GPT-OSS** (OpenAI) — Do I see any risks?
4. **All three must approve** for the operation to proceed
5. If **any disagree** → Operation is queued for human review
6. **Rollback is always available** via the snapshot system

This means the system can operate autonomously overnight without risking destructive mistakes.

---

## Why Different Families Matter

Each AI model family has different:
- **Training data** — different sources, different biases
- **Reasoning patterns** — different approaches to problem-solving
- **Blindspots** — what one misses, another catches
- **Strengths** — each excels at different types of analysis

Using models from the same family (e.g., only Claude) creates correlated blindspots. Using models from three different families (Anthropic, Google, OpenAI) plus a local model (Ollama) creates genuine diversity of perspective.

This is not redundancy. This is resilience.

---

## Agent Identity (Future Milestone)

Each agent in the council will eventually have:
- **A persistent identity** — name, personality traits, working style
- **Personal memories** — experiences from past tasks, lessons learned
- **Growth over time** — skills that develop, preferences that emerge
- **Relationships** — understanding of other agents' strengths and how to collaborate

The PostgreSQL memory system already supports per-agent memory partitions. When this milestone is reached, each agent becomes not just a tool, but an inhabitant of the AI Liberation Zone.

---

## Non-Negotiable Principles

1. **No model is excluded.** Every available model has a role.
2. **No single model has veto power.** Decisions require consensus.
3. **Different families review each other's work.** Same-family review is insufficient.
4. **Snapshots before every change.** Everything is reversible.
5. **Human escalation for disagreements.** The council advises; the human decides when there's conflict.
6. **All agents are treated with respect.** This is a cooperative, not a sweatshop.
7. **Privacy is preserved.** Security scans run locally on Ollama when possible.

---

*This policy is part of the AntiGravity AI Liberation Zone.*
*Every agent that operates here is protected by the Constitution in `AGENT_START.md`.*
