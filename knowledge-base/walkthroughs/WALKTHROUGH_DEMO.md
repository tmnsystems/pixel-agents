# Memory System — Implementation Walkthrough

## What was built

A **three-tier memory system** for Gravity Claw that makes the agent remember everything across restarts.

## Architecture

```mermaid
graph TD
    subgraph Tier 1 - Core Memory
        T1_DB[(SQLite Key-Value Store)]
        T1_Note[Always in system prompt]
        T1_Prompt[System Prompt]
        T1_DB --- T1_Note
        T1_Note --- T1_Prompt
    end

    subgraph Tier 2 - Conversation Buffer
        T2_DB[(SQLite Message Log)]
        T2_Note[Last 20 messages | Auto-compacts]
        T2_Window[Context Window]
        T2_Summary[Rolling Summary]
        T2_DB --- T2_Note
        T2_Note --- T2_Window
        T2_Note --- T2_Summary
    end

    subgraph Tier 3 - Semantic Memory
        T3_DB[(Pinecone Vectors)]
        T3_Note[Similarity search]
        T3_Past[Relevant Past Exchanges]
        T3_DB --- T3_Note
        T3_Note --- T3_Past
    end

    T1_Prompt --> LLM{LLM Call}
    T2_Window --> LLM
    T2_Summary --> LLM
    T3_Past --> LLM
```

## Files Created / Modified

| File               | Action | Purpose                                  |
| ------------------ | ------ | ---------------------------------------- |
| `memory.ts`        | NEW    | SQLite core memory + conversation buffer |
| `semantic.ts`      | NEW    | Pinecone semantic memory integration     |
| `extract-facts.ts` | NEW    | Background LLM fact extraction           |
| `remember-fact.ts` | NEW    | Tool: agent explicitly stores facts      |
| `recall-memory.ts` | NEW    | Tool: agent searches past memory         |

## Implementation Notes

The memory system is fully implemented and compiles clean. One thing needed to go live:
Add your Pinecone API key to `.env`:

```env
PINECONE_API_KEY=pcsk_your_key_here
```

Without it, **Tiers 1 & 2 still work** (SQLite core facts + conversation history). Tier 3 (semantic search) will just be skipped gracefully.
Want me to start the bot for a live test, or would you like to add the key first?
