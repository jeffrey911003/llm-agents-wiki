---
type: concept
title: Agent Evaluation
tags: [evaluation, benchmark]
sources: [wang2023-agent-survey, yao2023-react, schick2023-toolformer, shinn2023-reflexion, park2023-generative-agents]
updated: 2026-11-13
---
# Agent Evaluation

## Subjective evaluation
Based on human judgement; useful when no dataset or quantitative metric exists (e.g. intelligence, user-friendliness). Two strategies: human annotation and Turing-test style comparison with humans ([[wang2023-agent-survey]] §4.1).

### Example: interviewing agents
Generative Agents are "interviewed" on self-knowledge, memory, plans, reactions and reflections; 100 human evaluators rank believability, converted to TrueSkill ratings ([[park2023-generative-agents]] §6.1–6.4). Emergent behaviour is measured by information diffusion, network density and party attendance ([[park2023-generative-agents]] §7.1).

## Objective evaluation ([[wang2023-agent-survey]] §4.2)
- **Metrics** — task success (success rate, reward, coverage, accuracy), human similarity (coherence, fluency, human acceptance), efficiency (development cost, training efficiency).
- **Protocols** — e.g. real-world simulation (games, interactive simulators), social evaluation, multi-task evaluation, software testing.
- **Benchmarks** — e.g. [[alfworld|ALFWorld]], IGLU, Minecraft, AgentBench, SocKET, AgentSims.

## Benchmarks seen in this wiki
| Benchmark | Task | Metric | Used in |
|---|---|---|---|
| [[hotpotqa]] | multi-hop QA | EM | [[yao2023-react]], [[shinn2023-reflexion]] |
| [[fever]] | fact verification | accuracy | [[yao2023-react]] |
| [[alfworld]] | text household game | success rate | [[yao2023-react]], [[shinn2023-reflexion]] |
| [[webshop]] | web shopping | score, success rate | [[yao2023-react]] |
| [[humaneval]] | code generation | pass@1 | [[shinn2023-reflexion]] |
| [[smallville]] | social simulation | believability (TrueSkill), diffusion | [[park2023-generative-agents]] |
| [[lama]] | factual completion | answer in first 5 words | [[schick2023-toolformer]] |

## Related concepts
[[llm-based-agent]] · [[capability-acquisition]]
