---
type: concept
title: Agent Memory
tags: [architecture, module]
sources: [wang2023-agent-survey, shinn2023-reflexion, park2023-generative-agents]
updated: 2026-11-13
---
# Memory

## Definition
The memory module stores information perceived from the environment and uses it to support future actions, helping the agent accumulate experience, self-evolve and behave consistently ([[wang2023-agent-survey]] §2.1.2).

## Structures
Inspired by human memory: short-term memory ≈ the LLM context window; long-term memory ≈ external (e.g. vector) storage ([[wang2023-agent-survey]] §2.1.2).
- **Unified memory** — short-term only, written directly into the prompt; simple but limited by context length ([[wang2023-agent-survey]] §2.1.2).
- **Hybrid memory** — explicit short-term + long-term; e.g. Generative Agents and Reflexion ([[wang2023-agent-survey]] §2.1.2).
- Long-term-only designs are rarely documented, likely because consecutive actions are highly correlated, making short-term memory indispensable ([[wang2023-agent-survey]] §2.1.2, Remark).

## Formats
Natural language, embeddings, databases (queried via SQL), structured lists; formats are often combined, e.g. embedding keys with natural-language values ([[wang2023-agent-survey]] §2.1.2).

## Operations
- **Reading** — pick memories by recency, relevance and importance:
  `m* = argmax_m [ α·s_rec(q,m) + β·s_rel(q,m) + γ·s_imp(m) ]` ([[wang2023-agent-survey]] §2.1.2, Eq. 1). Many systems use relevance only (α = γ = 0); Generative Agents weights all three equally ([[wang2023-agent-survey]] §2.1.2).
- **Writing** — must handle *duplicated* memories (merge/condense) and *overflow* (delete, e.g. FIFO) ([[wang2023-agent-survey]] §2.1.2).
- **Reflection** — summarize low-level memories into higher-level insights, possibly hierarchically; e.g. Generative Agents generates questions from recent memories, retrieves evidence, and writes insights ([[wang2023-agent-survey]] §2.1.2).

## Example: Generative Agents' memory stream
- A natural-language list of memory objects, each with creation and last-access timestamps ([[park2023-generative-agents]] §4.1).
- Retrieval implements the survey's three scores concretely: recency = exponential decay (0.995 per game hour), importance = LLM rating 1–10, relevance = embedding cosine similarity; min-max normalized and weighted equally ([[park2023-generative-agents]] §4.1).
- Plans and reflections are also stored in the stream and retrieved alongside observations ([[park2023-generative-agents]] §4.2–4.3).
- Failure modes: missing or partial retrieval, and embellished memories ([[park2023-generative-agents]] §6.5.2).

## Example: Reflexion's memory
- Short-term = the current trajectory; long-term = verbal self-reflections, capped at 1–3 entries because of context limits ([[shinn2023-reflexion]] §3).
- Reflections beat raw episodic memory (last trajectory) by 8% on HotpotQA ([[shinn2023-reflexion]] §4.2).
- Authors suggest richer long-term stores (vector DB, SQL) as future work ([[shinn2023-reflexion]] §5) — matching the survey's embedding/database formats ([[wang2023-agent-survey]] §2.1.2).
- Memory **reflection** as an operation: see [[self-reflection]].

## Related concepts
[[planning]] · [[action]] · [[profiling]] · [[self-reflection]]
