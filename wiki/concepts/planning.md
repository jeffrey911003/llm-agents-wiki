---
type: concept
title: Agent Planning
tags: [architecture, module, reasoning]
sources: [wang2023-agent-survey, yao2023-react, shinn2023-reflexion, park2023-generative-agents]
updated: 2026-11-13
---
# Planning

## Definition
The planning module lets an agent decompose a complex task into simpler subtasks, as humans do ([[wang2023-agent-survey]] §2.1.3). The survey classifies methods by whether the agent receives feedback while planning ([[wang2023-agent-survey]] §2.1.3).

## Planning without feedback
- **Single-path reasoning** — a chain of steps, each leading to one next step: [[chain-of-thought|Chain-of-Thought (CoT)]], Zero-shot-CoT ("think step by step"), ReWOO, HuggingGPT ([[wang2023-agent-survey]] §2.1.3, Fig. 3).
- **Multi-path reasoning** — tree/graph of steps: Self-consistent CoT (majority vote over paths), Tree of Thoughts (BFS/DFS over LLM-evaluated "thoughts"), Graph of Thoughts, RAP (MCTS with a world model) ([[wang2023-agent-survey]] §2.1.3, Fig. 3).
- **External planner** — translate the task into PDDL and let a classical planner solve it (LLM+P, LLM-DP) ([[wang2023-agent-survey]] §2.1.3).

## Planning with feedback
Needed for long-horizon tasks, because a perfect plan up front is hard and execution can be disrupted by unpredictable dynamics ([[wang2023-agent-survey]] §2.1.3).
- **Environmental feedback** — e.g. [[react|ReAct]]'s thought–act–observation loop; Voyager uses execution progress, errors and self-verification ([[wang2023-agent-survey]] §2.1.3).
- **Human feedback** — subjective signal that helps alignment and reduces hallucination (e.g. Inner Monologue) ([[wang2023-agent-survey]] §2.1.3).
- **Model feedback** — the agent critiques itself: Self-Refine (output → feedback → refine loop), Reflexion (detailed verbal feedback instead of scalar rewards) ([[wang2023-agent-survey]] §2.1.3). Reflexion's own results: ReAct + reflection solves 130/134 ALFWorld tasks, and the gain depends on a reliable evaluator ([[shinn2023-reflexion]] §4.1, Table 3) — see [[self-reflection]].

> [!note] Different emphasis between sources
> [[wang2023-agent-survey]] files ReAct under *planning with environmental feedback* (§2.1.3). The ReAct authors stress that the key ingredient is **internal reasoning**, not just reacting to feedback: an Inner-Monologue-style variant that only verbalizes environment feedback (ReAct-IM) reaches 53% vs ReAct's 71% on ALFWorld, failing at goal decomposition and commonsense ([[yao2023-react]] §4, Table 3). Not a contradiction — the survey classifies by feedback source, the paper explains why it works.

## Evidence on feedback vs no feedback
- On HotpotQA, CoT (no feedback) hallucinates far more than ReAct (56% vs 0% of failures), but ReAct makes more reasoning errors (47% vs 16%) ([[yao2023-react]] Table 2).
- Combining both (ReAct ↔ CoT-SC back-off) works best for prompting ([[yao2023-react]] Table 1).

## Hierarchical planning for long horizons
Generative Agents plan top-down: a day agenda in 5–8 chunks, recursively split into hour-long and then 5–15-minute actions; plans are stored in memory and regenerated when the agent decides to react to a new observation ([[park2023-generative-agents]] §4.3). Without planning, an agent may eat lunch at 12, 12:30 and 1 pm ([[park2023-generative-agents]] §4.3); removing planning (on top of reflection) lowers believability 26.88 → 25.64 ([[park2023-generative-agents]] §6.5.1).

## Trade-off
Planning without feedback is simple but suited to tasks with few reasoning steps; planning with feedback needs careful design but handles complex, long-range tasks much better ([[wang2023-agent-survey]] §2.1.3, Remark).

## Related concepts
[[memory]] · [[action]] · [[llm-based-agent]] · [[react]] · [[chain-of-thought]] · [[self-reflection]]
