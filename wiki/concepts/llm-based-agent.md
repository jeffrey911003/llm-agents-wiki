---
type: concept
title: LLM-based Agent
tags: [definition, core]
sources: [wang2023-agent-survey]
updated: 2026-11-13
---
# LLM-based Agent

## Definition
An autonomous agent is "a system situated within and a part of an environment that senses that environment and acts on it, over time, in pursuit of its own agenda" (Franklin & Graesser 1997, quoted in [[wang2023-agent-survey]] §1). An **LLM-based agent** uses an LLM as the central controller of such a system ([[wang2023-agent-survey]] §1).

## How it differs from a plain LLM
- A plain LLM answers questions; an agent must fulfil a role, perceive and learn from its environment, and evolve over time ([[wang2023-agent-survey]] §2.1).
- To bridge this gap, the LLM is wrapped in modules: [[profiling]], [[memory]], [[planning]], [[action]] ([[wang2023-agent-survey]] §2.1, Fig. 2).

## How it differs from RL agents
- Compared with reinforcement-learning agents, LLM-based agents carry broad internal world knowledge, so they can act sensibly without domain-specific training, and they offer natural-language interfaces that are more flexible and explainable ([[wang2023-agent-survey]] §1).

## Related concepts
[[capability-acquisition]] · [[agent-evaluation]]
