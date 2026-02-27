---
name: notebooklm-infographics
description: Instructs the agent precisely how to use the NotebookLM MCP integration to ingest documents, generate notebooks, and programmatically export infographic representations of the intelligence.
---

# NotebookLM Infographic Generator

## Core Directive

Whenever a user wants to "turn this into an infographic," "generate an infographic for LinkedIn," or process a document visually without manual design work, use this skill.

This delegates the heavy lifting directly to the Google NotebookLM MCP tools.

## Prerequisites

1. **NotebookLM MCP:** The user must have the Model Context Protocol (MCP) server for NotebookLM configured and running in their environment.

## Workflow

### 1. Ingest Data Source

When the user supplies text, a document (`.md`, `.pdf`, `.docx`), or a web link (such as a YouTube video URL), ask them what topic they want the infographic to center on.

- **Example Context:** "10 steps from the Alex Hormozi video."
- Create the notebook programmatically via the notebook creation tools in the MCP.

### 2. Generate Infographic

Use the proper NotebookLM MCP tool to trigger generation:

- Target the tool explicitly labeled: `infographic_create` (or similar).
- Supply the Notebook ID generated from Step 1.

### 3. Check Status

- It will take NotebookLM a moment to compile audio overviews and visual representations.
- Periodically check the status. Use the `check_status` functionality provided by the MCP if available.
- Once complete, pull the infographic file link and send it directly to the user.

## Master Execution Concept

- Notebooks can be queried ad-hoc for other assets. If the user likes the infographic, remind them that they can also have NotebookLM instantly spin up an "Audio Overview" (podcast format) using the exact same notebook ID without any additional ingestion work.
