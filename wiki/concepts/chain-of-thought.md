---
type: concept
title: Chain-of-Thought (CoT) and Self-Consistency (CoT-SC)
tags: [reasoning, prompting, planning]
sources: [wang2023-agent-survey, yao2023-react]
updated: 2026-11-13
---
# Chain-of-Thought (CoT)

## Definition
Prompting an LLM with step-by-step reasoning examples so it produces intermediate reasoning before answering ([[wang2023-agent-survey]] §2.1.3). Zero-shot-CoT triggers this with phrases like "think step by step", without examples ([[wang2023-agent-survey]] §2.1.3).

## Variants
- **CoT-SC (self-consistency)** — sample several reasoning paths and take the majority answer; a multi-path method ([[wang2023-agent-survey]] §2.1.3). ReAct's baseline samples 21 CoT trajectories at temperature 0.7 ([[yao2023-react]] §3.2).
- Tree of Thoughts and others extend this into tree/graph search — see [[planning]] ([[wang2023-agent-survey]] §2.1.3).

## In the agent taxonomy
Single-path reasoning under *planning without feedback* ([[wang2023-agent-survey]] §2.1.3).

## Limitations
- Relies only on internal knowledge — a "static black box" not grounded in the external world, prone to fact hallucination and error propagation ([[yao2023-react]] §1).
- On HotpotQA, hallucination is CoT's main failure mode (56% of failures) ([[yao2023-react]] Table 2).
- But CoT is more flexible in structuring reasoning than [[react]], making fewer reasoning errors (16% vs 47% of failures) ([[yao2023-react]] Table 2, §3.3).

## Related concepts
[[react]] · [[planning]] · [[hallucination]]
