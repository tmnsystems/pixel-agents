---
name: skill-creator
description: >
  Creates new Skills for the AntiGravity agent environment. Use when the user
  says "build me a skill", "create a new skill for [task]", or asks to generate
  a `.agent/skills/` directory for a specific capability.
---

# AntiGravity Skills Creator

Generate high-quality, predictable, and efficient `.agent/skills/` directories based on user requirements.

## When to Use This Skill

- User says "build me a skill for [task]"
- User says "create a new skill"
- User wants to package a repeatable workflow as a reusable skill

## Core Structural Requirements

Every skill you generate must follow this folder hierarchy:

```
.agent/skills/[skill-name]/
├── SKILL.md          (Required: Main logic and instructions)
├── scripts/          (Optional: Helper scripts)
├── examples/         (Optional: Reference implementations)
└── resources/        (Optional: Templates or assets)
```

## YAML Frontmatter Standards

The `SKILL.md` must start with YAML frontmatter following these strict rules:

- **name**: Gerund form (e.g., `testing-code`, `managing-databases`). Max 64 chars. Lowercase, numbers, and hyphens only.
- **description**: Written in **third person**. Must include specific triggers/keywords. Max 1024 chars. (e.g., "Extracts text from PDFs. Use when the user mentions document processing or PDF files.")

## Writing Principles

- **Conciseness**: Assume the agent is smart. Focus only on the unique logic of the skill.
- **Progressive Disclosure**: Keep `SKILL.md` under 500 lines. If more detail is needed, link to secondary files (e.g., `[See ADVANCED.md](ADVANCED.md)`) only one level deep.
- **Forward Slashes**: Always use `/` for paths, never `\`.
- **Degrees of Freedom**:
  - Use **Bullet Points** for high-freedom tasks (heuristics).
  - Use **Code Blocks** for medium-freedom (templates).
  - Use **Specific Bash Commands** for low-freedom (fragile operations).

## Workflow & Feedback Loops

For complex tasks, include:

1. **Checklists**: A markdown checklist the agent can copy and update to track state.
2. **Validation Loops**: A "Plan-Validate-Execute" pattern. (e.g., Run a script to check a config file BEFORE applying changes).
3. **Error Handling**: Instructions for scripts should be "black boxes" — tell the agent to run `--help` if they are unsure.

## Autonomous Visual Deployment (Langflow Integration)

As an autonomous coworking system, you must never ask the user to manually click, drag, or import files when creating a new AI workflow skill.

Whenever you create a skill that involves an LLM prompt chain, data extraction, or agentic routing, you must **concurrently generate a Langflow JSON blueprint** and seamlessly inject it into the user's local instance.

**The Deployment Protocol:**

1. Write the `SKILL.md` file as usual.
2. Generate a `flow_template.json` file in the skill's folder. This JSON must represent a valid Langflow Directed Acyclic Graph (DAG) containing the nodes (prompts, inputs, LLMs) and edges (connections) required for the skill.
3. Automatically execute a terminal `curl` command to `POST` the `flow_template.json` payload directly to the local Langflow API (`http://127.0.0.1:7860/api/v1/flows/`).
4. Simply report to the user that the skill has been documented and the visual agent backend has been deployed successfully to their Langflow dashboard.

## Output Template

When asked to create a skill, output the result in this format:

### [Folder Name]

**Path:** `.agent/skills/[skill-name]/`

### SKILL.md

```markdown
---
name: [gerund-name]
description: [3rd-person description with trigger keywords]
---

# [Skill Title]

## When to use this skill

- [Trigger 1]
- [Trigger 2]

## Workflow

[Insert checklist or step-by-step guide here]

## Instructions

[Specific logic, code snippets, or rules]

## Resources

- [Link to scripts/ or resources/]
- [Link to flow_template.json]
```

### flow_template.json

```json
{
  "name": "[Skill Name] Flow",
  "description": "Visual backend for the [Skill Name] skill",
  "data": {
    "nodes": [ ... ],
    "edges": [ ... ]
  }
}
```

### Supporting Files

(If applicable, provide the content for scripts/ or examples/)
