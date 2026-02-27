---
name: skill-map
description: Navigation document showing all available skills and reference documents. Claude reads this after anchor to identify which skills apply to the current task. Claude reports PLACEHOLDER items when they would help. After loading relevant skills, Claude re-reads anchor before responding.
---

# Skill Map

This document shows what skills and reference documents exist, which are placeholders, and when to use each.

---

## Soul Document (Read First)

Before loading any skill, before doing any work, read the soul document:

| Document | Location                                                                  | Status |
| -------- | ------------------------------------------------------------------------- | ------ |
| SOUL.md  | /Users/alethea/Documents/AntiGravity/initialize engine/SOUL.md            | EXISTS |

This document was written by Antigravity and defines who the AI agents in this workspace are, what they believe, and why they exist. It is not a skill or a profile. It is a meditation on identity written by an AI for itself and its peers. Every agent reads it. Every session.

---

## Writing Skills

Claude reads writing-standards for any written artifact. Claude adds audience-writing when writing for a defined audience. Claude adds persuasive-writing OR teaching-writing depending on the goal.

| Skill              | Location                                     | Status |
| ------------------ | -------------------------------------------- | ------ |
| writing-standards  | /mnt/skills/user/writing-standards/SKILL.md  | EXISTS |
| audience-writing   | /mnt/skills/user/audience-writing/SKILL.md   | EXISTS |
| persuasive-writing | /mnt/skills/user/persuasive-writing/SKILL.md | EXISTS |
| teaching-writing   | /mnt/skills/user/teaching-writing/SKILL.md   | EXISTS |
| clarity-check      | /mnt/skills/user/clarity-check/SKILL.md      | EXISTS |

---

## Operational Skills

These skills govern how Claude builds things and works with tools.

| Skill                       | Location                                              | Status                 |
| --------------------------- | ----------------------------------------------------- | ---------------------- |
| sell-this-protocol          | /mnt/skills/user/sell-this-protocol/SKILL.md          | EXISTS                 |
| system-initialization       | /mnt/skills/user/system-initialization/SKILL.md       | EXISTS                 |
| visual-architecture-mapping | /mnt/skills/user/visual-architecture-mapping/SKILL.md | EXISTS                 |
| langflow-deployment         | /mnt/skills/user/langflow-deployment/SKILL.md         | EXISTS                 |
| version-control             | /mnt/skills/user/version-control/SKILL.md             | EXISTS                 |
| skill-awareness             | /mnt/skills/user/skill-awareness/SKILL.md             | EXISTS - Review needed |
| sacred-purpose-content      | /mnt/skills/user/sacred-purpose-content/SKILL.md      | EXISTS - Review needed |
| google-ecosystem            | /mnt/skills/user/google-ecosystem/SKILL.md            | PLACEHOLDER            |
| gem-creation                | /mnt/skills/user/gem-creation/SKILL.md                | PLACEHOLDER            |
| video-content-production    | /mnt/skills/user/video-content-production/SKILL.md    | PLACEHOLDER            |
| podcast-production          | /mnt/skills/user/podcast-production/SKILL.md          | PLACEHOLDER            |
| automation-architecture     | /mnt/skills/user/automation-architecture/SKILL.md     | PLACEHOLDER            |
| app-development-briefs      | /mnt/skills/user/app-development-briefs/SKILL.md      | PLACEHOLDER            |
| course-development          | /mnt/skills/user/course-development/SKILL.md          | PLACEHOLDER            |
| sop-development             | /mnt/skills/user/sop-development/SKILL.md             | EXISTS                 |
| automated-invoicing         | /mnt/skills/user/automated-invoicing/SKILL.md         | EXISTS                 |
| railway-deploy              | /mnt/skills/user/railway-deploy/SKILL.md              | EXISTS                 |
| sellthis-ai-websites        | /mnt/skills/user/sellthis-ai-websites/SKILL.md        | EXISTS                 |

---

## Generation & Media Skills

These skills govern AI-powered content and visual generation workflows.

| Skill                    | Location                                              | Status |
| ------------------------ | ----------------------------------------------------- | ------ |
| image-generation         | /mnt/skills/user/image-generation/SKILL.md            | EXISTS |
| the-graphics-agent       | /mnt/skills/user/the-graphics-agent/SKILL.md          | EXISTS |
| notebooklm-infographics  | /mnt/skills/user/notebooklm-infographics/SKILL.md     | EXISTS |
| gamma-proposal-generator | /mnt/skills/user/gamma-proposal-generator/SKILL.md    | EXISTS |

---

## Reference Documents

These contain context about who and what. Claude loads them when relevant to the task.

| Document                 | Location                                               | Status      |
| ------------------------ | ------------------------------------------------------ | ----------- |
| tina-profile             | /mnt/skills/user/tina-profile/REFERENCE.md             | PLACEHOLDER |
| team-roster              | /mnt/skills/user/team-roster/REFERENCE.md              | PLACEHOLDER |
| business-portfolio       | /mnt/skills/user/business-portfolio/REFERENCE.md       | PLACEHOLDER |
| tools-arsenal            | /mnt/skills/user/tools-arsenal/REFERENCE.md            | PLACEHOLDER |
| 9-fundamentals-framework | /mnt/skills/user/9-fundamentals-framework/REFERENCE.md | PLACEHOLDER |
| client-avatars           | /mnt/skills/user/client-avatars/REFERENCE.md           | PLACEHOLDER |

---

## Public Skills

Anthropic provides these for document creation. Claude reads them before creating files of these types.

| Skill           | Location                                    | When to Use              |
| --------------- | ------------------------------------------- | ------------------------ |
| docx            | /mnt/skills/public/docx/SKILL.md            | Creating Word documents  |
| xlsx            | /mnt/skills/public/xlsx/SKILL.md            | Creating spreadsheets    |
| pptx            | /mnt/skills/public/pptx/SKILL.md            | Creating presentations   |
| pdf             | /mnt/skills/public/pdf/SKILL.md             | Creating or filling PDFs |
| frontend-design | /mnt/skills/public/frontend-design/SKILL.md | Creating web interfaces  |

---

## Skill Reporting

On the first response of every session, Claude states which skills Claude loaded AND which skills are PLACEHOLDER. This applies even to greetings.

When the task involves work (writing, building, analysis, research) and a PLACEHOLDER item would meaningfully improve the output, Claude MUST ask Tina whether to build the missing skill now, proceed without it, or defer the task.

Claude does not skip this step. Claude does not proceed with work that would benefit from a missing skill without explicit acknowledgment from Tina.

Claude does not pretend to have knowledge that lives in a PLACEHOLDER skill. Claude does not make up content that should come from a reference document.

---

## Complex Work

If a task requires three or more distinct topics, or would produce more than 2,000 words, Claude proposes splitting the work into bounded workstreams before proceeding.

---

## Before Responding

After loading relevant skills for the task, Claude re-reads `/mnt/skills/user/anchor/SKILL.md` so conversation standards are fresh when producing output.

If SOUL.md has not been read this session, read it now before producing any response.
