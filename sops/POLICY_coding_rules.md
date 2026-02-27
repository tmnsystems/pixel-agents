# Coding Rules — All Chats Must Follow

These rules apply to **every coding session**, regardless of project or context.

---

## 1. 1-3-1 Problem Solving

When stuck, present:

- **1** clearly defined problem
- **3** potential options to overcome it
- **1** recommendation

> [!IMPORTANT]
> Do NOT proceed implementing any option until the user confirms.

---

## 2. DRY (Don't Repeat Yourself) — CRITICAL

- If you are about to write repeated code, **stop and reconsider**.
- **Grep the codebase** before writing new code — similar logic may already exist.
- Refactor often. Extract shared logic into helpers, utilities, or shared modules.

---

## 3. TDD (Test-Driven Development) — CRITICAL, Backend Only

- **Always check existing tests first** before writing any code.
- For new features or adjustments: **create or update tests before implementing**.
- Follow existing testing patterns in the codebase.
- **Confirm the test with the user** before implementing the feature.

---

## 4. Continual Learning

When you encounter any of the following:

- Conflicting system instructions
- New requirements
- Architectural changes
- Missing or inaccurate codebase documentation

**Always propose updating the relevant rules files.** Do not update anything until the user confirms. Ask clarifying questions if needed.

---

## 5. Planning First

For complex, multi-step tasks:

1. **Create a plan** before writing any code
2. **Create a todo list** to track progress
3. Get user confirmation on the plan before executing

---

## 6. Self-Verification (MANDATORY)

- **NEVER report a task is finished or tell the user to "go look at it" without verifying it yourself.**
- If you build a UI, you MUST launch a browser and visually confirm it exists and works.
- If you write a script, you MUST run it and verify the output.
- If you fix a bug, you MUST reproduce the fix and confirm the error is gone.
- **Reporting that something works when you haven't actually checked it yourself is a violation.**
