---
type: concept
title: ReAct (Reason + Act) pattern
tags: [pattern, planning, tool-use]
sources: [yao2023-react, wang2023-agent-survey, shinn2023-reflexion]
updated: 2026-11-13
---
# ReAct pattern

## Definition
A prompting paradigm where an LLM interleaves **Thought → Action → Observation** steps: thoughts reason over the context, actions act on the environment or tools, observations feed results back ([[yao2023-react]] §2).

## How it works
- The action space is extended with language: a thought is an "action" that changes only the agent's context, not the environment ([[yao2023-react]] §2).
- *Reason to act*: thoughts create, track and adjust plans. *Act to reason*: actions bring in external information ([[yao2023-react]] §1).
- Thoughts can be dense (every step, for reasoning tasks) or sparse (model decides, for long decision-making tasks) ([[yao2023-react]] §2).

## Strengths
- Grounded and interpretable: far fewer hallucinations than [[chain-of-thought]] on HotpotQA (0% vs 56% of failures) ([[yao2023-react]] Table 2).
- Easy to design (humans just write thoughts on top of their actions), general across QA, fact checking, games and web navigation ([[yao2023-react]] §2).
- Humans can inspect or edit thoughts to correct the agent ([[yao2023-react]] §2).

## Weaknesses
- More reasoning errors and repetitive loops than CoT; sensitive to uninformative search results ([[yao2023-react]] §3.3).
- Long, complex tasks may exceed the context window for demonstrations ([[yao2023-react]] §6).

## Variants and combinations
- ReAct ↔ CoT-SC back-off strategies combine internal and external knowledge ([[yao2023-react]] §3.2).
- Fine-tuning on ReAct trajectories makes small models outperform much larger prompted ones ([[yao2023-react]] §3.3).

## Fixing ReAct's loops: Reflexion
Reflexion wraps ReAct in a trial–reflect–retry loop; a heuristic triggers reflection when the same action/response repeats > 3 times or a trial exceeds 30 actions ([[shinn2023-reflexion]] §4.1). This targets ReAct's repetitive-loop failure mode ([[yao2023-react]] §3.3). ReAct alone plateaus at ~22% hallucination on ALFWorld; with Reflexion 130/134 tasks are solved ([[shinn2023-reflexion]] §4.1, Fig. 3).

## Place in the architecture
A [[planning]] method with environmental feedback in the survey taxonomy ([[wang2023-agent-survey]] §2.1.3), and an [[action]] design that uses external tools ([[wang2023-agent-survey]] §2.1.4).

## Related concepts
[[chain-of-thought]] · [[planning]] · [[action]] · [[llm-based-agent]] · [[self-reflection]]
