---
type: concept
title: Profiling (agent profile / role)
tags: [architecture, module]
sources: [wang2023-agent-survey, park2023-generative-agents]
updated: 2026-11-13
---
# Profiling

## Definition
The profiling module specifies the agent's role (e.g. coder, teacher, domain expert), usually written into the prompt to steer the LLM's behaviour ([[wang2023-agent-survey]] §2.1.1).

## How it works
- **Profile contents:** demographic information (age, gender, career), personality/psychology information, and social information (relationships between agents); which to use depends on the application ([[wang2023-agent-survey]] §2.1.1).
- **Generation strategies** ([[wang2023-agent-survey]] §2.1.1):
  - *Handcrafting* — write it manually, e.g. "you are an outgoing person"; used by Generative Agents, MetaGPT, ChatDev.
  - *LLM-generation* — state generation rules, optionally give a few seed profiles, then let an LLM generate the rest (e.g. RecAgent); cheap at scale but less controllable.
  - *Dataset alignment* — build profiles from real-world data, e.g. demographic backgrounds of ANES survey participants.

## Example
Generative Agents: one hand-written paragraph per agent (occupation, relationships); each semicolon-separated phrase becomes a seed memory ([[park2023-generative-agents]] §3.1).

## Role in the architecture
The profile influences [[memory]] and [[planning]], and through them [[action]] ([[wang2023-agent-survey]] §2.1).

## Open problems
Role-playing beyond common roles remains hard for LLMs ([[wang2023-agent-survey]] §6.1).

## Related concepts
[[llm-based-agent]]
