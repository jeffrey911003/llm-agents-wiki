---
type: concept
title: Agent Action
tags: [architecture, module, tool-use]
sources: [wang2023-agent-survey, yao2023-react, schick2023-toolformer]
updated: 2026-11-13
---
# Action

## Definition
The action module turns the agent's decisions into concrete outcomes; it sits most downstream, interacts directly with the environment, and is influenced by [[profiling]], [[memory]] and [[planning]] ([[wang2023-agent-survey]] §2.1.4).

## Four perspectives ([[wang2023-agent-survey]] §2.1.4)
1. **Action goal** (before action) — task completion, communication with agents/humans, environment exploration.
2. **Action production** (before action) — via *memory recollection* (retrieve relevant memories, e.g. Generative Agents) or *plan following* (execute a pre-made plan, e.g. DEPS, GITM).
3. **Action space** (in action) — *external tools* (APIs such as HuggingGPT, WebGPT, Toolformer; databases/knowledge bases; external models) or the LLM's *internal knowledge*.
4. **Action impact** (after action) — changing the environment, altering internal states (e.g. updating memory), triggering new actions.

## Language as an action
[[react]] extends the action space with language (Â = A ∪ L): a "thought" is an action that only updates the agent's context and returns no observation ([[yao2023-react]] §2). Even a minimal tool set — `search`, `lookup`, `finish` on Wikipedia — is enough to ground reasoning ([[yao2023-react]] §3.1).

## Why tools
Tools help in domains needing expert knowledge and mitigate hallucinations the LLM cannot fix by itself ([[wang2023-agent-survey]] §2.1.4). Full treatment, including how models learn tool use: [[tool-use]].

## Related concepts
[[planning]] · [[memory]] · [[llm-based-agent]] · [[react]] · [[tool-use]]
