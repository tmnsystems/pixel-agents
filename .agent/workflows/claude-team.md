---
description: Spawn a Parallel Agent Team (Lead + Specialists) using Claude Code
---

# Claude Code Agent Team Workflow

This workflow spawns Claude Code CLI with custom agents to work on tasks autonomously.

## Prerequisites
- Claude Code CLI installed (`which claude`)
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in ~/.zshrc (already set)

## How To Use

Run from terminal or have Antigravity invoke it:

```bash
# Basic: Single task with agents
claude -p --model sonnet --permission-mode bypassPermissions \
  --agents '{"researcher": {"description": "Reads and analyzes files", "prompt": "You are a research specialist."}, "reviewer": {"description": "Reviews output quality", "prompt": "You are a quality reviewer."}}' \
  "YOUR TASK HERE"

# With budget cap ($2 max):
claude -p --model sonnet --permission-mode bypassPermissions \
  --max-budget-usd 2 \
  --agents '{"builder": {"description": "Builds code", "prompt": "You are a code builder."}, "tester": {"description": "Tests code", "prompt": "You are a QA tester."}}' \
  "YOUR TASK HERE"
```

## Key Flags
- `-p` / `--print` — Non-interactive, outputs result and exits
- `--model sonnet` — Use Sonnet (cheaper). Use `opus` for complex reasoning
- `--permission-mode bypassPermissions` — Let agents write files without prompts
- `--agents '{...}'` — Define specialist agents as JSON
- `--max-budget-usd N` — Cap spend per run
- `--allowedTools "Read,List,Search"` — Restrict agents to read-only (safer)

## Agent Templates

### Research Team
```json
{"researcher": {"description": "Deep file analysis", "prompt": "Read files thoroughly and extract key insights."}, "summarizer": {"description": "Creates concise summaries", "prompt": "Take research findings and create actionable summaries."}}
```

### Build Team  
```json
{"architect": {"description": "Plans the implementation", "prompt": "Design the architecture before coding."}, "builder": {"description": "Writes code", "prompt": "Implement the design with clean, tested code."}, "reviewer": {"description": "Code review", "prompt": "Review for bugs, security, and best practices."}}
```

### Content Team
```json
{"writer": {"description": "Drafts content", "prompt": "Write in Tina Marie's voice - direct, specific, no fluff."}, "editor": {"description": "Polishes output", "prompt": "Check for AI writing patterns, eliminate them. Make it human."}}
```

## Example: Process All Files in User Outbox

// turbo
```bash
cd /Users/alethea/Documents/AntiGravity && claude -p --model sonnet --permission-mode bypassPermissions --max-budget-usd 2 --agents '{"researcher": {"description": "Reads files", "prompt": "You are a research specialist."}}' "List all files in 'User Outbox/archive/', read each one, and create a digest summary for each in 'AlwaysOnAgent/workspace/knowledge-base/'"
```
