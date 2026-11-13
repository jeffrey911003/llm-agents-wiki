---
type: paper
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
authors: [Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao]
year: 2023
venue: ICLR 2023
arxiv: "2210.03629"
tags: [prompting, planning, tool-use, reasoning]
sources: [yao2023-react]
updated: 2026-11-13
---
# ReAct (Yao et al., 2023)

## TL;DR
ReAct prompts an LLM to interleave free-form **reasoning traces** ("thoughts") with **task actions**, so reasoning guides what to do next and actions fetch information that grounds the reasoning (§1, §2). With only 1–6 in-context examples it beats acting-only and imitation/RL baselines on interactive tasks and reduces hallucination compared with [[chain-of-thought]] (Abstract, §3.3, §4).

## Problem
- Chain-of-thought reasoning is a "static black box": it relies only on internal knowledge, so it can hallucinate facts and propagate errors (§1, Fig. 1(1b)).
- Prior LLM acting/planning work predicts actions but does not reason abstractly about high-level goals or keep a working memory (§1).

## Method
- Agent setup: at step *t* the agent sees observation *o_t* and picks action *a_t* from context *c_t* (§2).
- ReAct augments the action space with language: Â = A ∪ L. A **thought** does not change the environment and returns no observation; it updates the context to support later reasoning or acting (§2).
- Thought types: decompose goals/make plans, inject commonsense, extract key info from observations, track progress, handle exceptions and adjust plans (§2).
- Prompting a frozen PaLM-540B with human-written thought–action–observation trajectories (§2). Dense thoughts (alternating every step) for reasoning tasks; sparse thoughts, placed by the model, for long decision-making tasks (§2).
- Knowledge tasks use a deliberately weak Wikipedia API: `search[entity]`, `lookup[string]`, `finish[answer]` (§3.1).
- Hybrid strategies: ReAct → CoT-SC (fall back if no answer within 7/5 steps) and CoT-SC → ReAct (fall back if the majority answer appears in < n/2 of samples) (§3.2).
- Fine-tuning variant: 3,000 correct ReAct trajectories used to fine-tune PaLM-8B/62B (§3.2).
- See [[react]] for the general pattern.

## Experiments & Key Results
**Knowledge-intensive reasoning** — [[hotpotqa]] (EM) / [[fever]] (accuracy), PaLM-540B prompting (Table 1):

| Method | HotpotQA EM | FEVER Acc |
|---|---|---|
| Standard | 28.7 | 57.1 |
| CoT | 29.4 | 56.3 |
| CoT-SC | 33.4 | 60.4 |
| Act | 25.7 | 58.9 |
| ReAct | 27.4 | 60.9 |
| CoT-SC → ReAct | 34.2 | **64.6** |
| ReAct → CoT-SC | **35.1** | 62.0 |
| Supervised SoTA | 67.5 | 89.5 |

- ReAct > Act on both tasks; ReAct beats CoT on FEVER but slightly trails it on HotpotQA (§3.3).
- Human error analysis of 200 HotpotQA trajectories (Table 2, §3.3):
  - Hallucination: 56% of CoT failures vs 0% of ReAct failures; false positives among successes 14% (CoT) vs 6% (ReAct).
  - Reasoning errors: 47% of ReAct failures vs 16% of CoT — includes a ReAct-specific loop of repeating earlier thoughts/actions.
  - Uninformative search: 23% of ReAct failures.
- Combined ReAct + CoT-SC reaches CoT-SC's 21-sample performance with only 3–5 samples (§3.3, Fig. 2).
- Fine-tuning: prompted ReAct is worst at 8B/62B, but fine-tuned ReAct is best; fine-tuned 62B ReAct beats all 540B prompting methods (§3.3, Fig. 3).

**Interactive decision making** (§4):
- [[alfworld]] success rate: ReAct best-of-6 71% vs Act 45% vs BUTLER 37%; even the worst ReAct trial (48%) beats the best of both (Table 3, §4).
- [[webshop]] success rate: ReAct 40.0 vs Act 30.1, IL 29.1, IL+RL 28.7; human experts 59.6 (Table 4). Authors report ~10% absolute improvement over the previous best success rate (§4).
- Ablation ReAct-IM (Inner-Monologue-style dense environment feedback as thoughts): 53% vs ReAct 71% on ALFWorld; failures came from missing goal decomposition and commonsense reasoning (§4, Table 3).

## Limitations
- Structural constraint of interleaving reduces reasoning flexibility → more reasoning errors and repetitive loops than CoT (§3.3).
- Strongly depends on informative retrieval; bad search results derail reasoning (§3.3).
- Complex tasks with large action spaces need more demonstrations than fit in the context window (§6).
- Prompting is still far from supervised SoTA on HotpotQA/FEVER (Table 1, §3.3).

## Connections
- Pattern: [[react]]; reasoning baseline: [[chain-of-thought]].
- Architecture mapping: [[planning]] (planning with feedback), [[action]] (language added to the action space; tool use via APIs).
- Survey view: [[wang2023-agent-survey]] cites ReAct as the example of planning with environmental feedback (§2.1.3) — see the note on [[planning]] about emphasis.
- Benchmarks: [[hotpotqa]], [[fever]], [[alfworld]], [[webshop]]; see [[agent-evaluation]].
