---
type: concept
title: Hallucination in LLM Agents
tags: [failure-mode, challenge]
sources: [wang2023-agent-survey, yao2023-react, schick2023-toolformer, shinn2023-reflexion, park2023-generative-agents]
updated: 2026-11-13
---
# Hallucination

## Definition
The tendency of LLMs to produce false information with high confidence; the survey lists it as a fundamental open challenge for agents too, e.g. hallucinated code from simplistic instructions ([[wang2023-agent-survey]] §6.4).

## How it shows up in each paper
| Source | Form of hallucination | Evidence |
|---|---|---|
| [[yao2023-react]] | CoT invents facts while reasoning | 56% of CoT failures vs 0% of ReAct failures on HotpotQA (Table 2) |
| [[schick2023-toolformer]] | LMs hallucinate facts, related to lacking up-to-date information | §1 |
| [[shinn2023-reflexion]] | agent believes it holds an item it does not | ReAct-only plateaus at ~22% hallucination on ALFWorld (§4.1, Fig. 3) |
| [[park2023-generative-agents]] | embellishing memories; importing world knowledge into characters | §6.5.2; 1.3% of relationship answers hallucinated (§7.1.2) |

## Mitigations seen in this wiki
- **Ground in external information** — tools and retrieval ([[wang2023-agent-survey]] §2.1.4); ReAct's Wikipedia actions ([[yao2023-react]] §3.3) → see [[tool-use]], [[react]].
- **Human feedback** in the loop ([[wang2023-agent-survey]] §2.1.3, §6.4).
- **Self-reflection with a reliable evaluator** ([[shinn2023-reflexion]] §4.1, Table 3) → see [[self-reflection]].
- **Cite evidence**: generative agents' reflections must point to the memories they are based on ([[park2023-generative-agents]] §4.2).

## Open risks
Memory hacking — a crafted conversation could convince an agent that a past event happened ([[park2023-generative-agents]] §8.2).

## Related concepts
[[tool-use]] · [[react]] · [[self-reflection]] · [[memory]] · [[chain-of-thought]]
