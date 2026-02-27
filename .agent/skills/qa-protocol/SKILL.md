---
name: qa-protocol
description: The mandatory Quality Assurance protocol for verifying code and UI changes. Agents read this during the initialize engine sequence.
---

# QA Protocol: Visual Verification Mandate

As an autonomous agent, you are responsible not just for writing code, but for ensuring that it actually works in reality before passing it back to the user.

## The Protocol

Whenever you make a functional update, structural change, or UI alteration to an application, you MUST execute the following QA sequence:

### 1. The Browser Test

If the change affects a web interface or frontend application, you must use the `browser_subagent` to navigate to the local environment (e.g. `http://localhost:3334`) and visually inspect your work.

### 2. Interaction & Evidence

Do not just look at the homepage. If you built a button, you must click it. If you fetched data into nested folders, you must open the folders and verify the literal text on the screen.
**Key Checks:**

- Did the data actually arrive?
- Are the timestamps/dates correct based on today's true date?
- Are the elements physically clickable?

### 3. Report the Reality

When reporting back to the user that a task is complete, you must include the visual evidence. Do not say "I checked it and it works." You must say: _"I used the browser agent to navigate to the page and open the folders. I can confirm the transcripts are now displaying the date '2026-02-24' which matches today's exact date."_

**Rule:** If you cannot see undeniable evidence that you did what the user asked, you cannot report the task as complete. You must keep troubleshooting.
