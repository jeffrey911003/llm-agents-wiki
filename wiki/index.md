---
type: index
updated: 2026-11-13
---
# Index

## Overview
- [[overview]] — big-picture synthesis of LLM agents research, organized by the four-module architecture

## Papers
- [[wang2023-agent-survey]] — survey proposing the profiling/memory/planning/action framework; capability acquisition, applications, evaluation, challenges
- [[yao2023-react]] — ReAct: interleaving thoughts and actions; HotpotQA/FEVER/ALFWorld/WebShop results; error analysis vs CoT
- [[schick2023-toolformer]] — Toolformer: self-supervised learning of API calls; 5 tools; 6.7B beats GPT-3 on math/facts; limits (no chaining)
- [[shinn2023-reflexion]] — Reflexion: Actor/Evaluator/Self-Reflection loop with verbal memory; ALFWorld 130/134, HumanEval 91%; evaluator-quality caveat
- [[park2023-generative-agents]] — Generative Agents: memory stream, reflection tree, hierarchical planning; 25-agent Smallville; believability ablations

## Concepts
- [[llm-based-agent]] — definition; how agents differ from plain LLMs and RL agents
- [[profiling]] — defining the agent's role; handcrafted, LLM-generated or data-aligned profiles
- [[memory]] — short/long-term structures, formats, reading (recency·relevance·importance), writing, reflection
- [[planning]] — single/multi-path reasoning, external planners, planning with environment/human/model feedback
- [[action]] — action goal, production, space (tools vs internal knowledge), impact
- [[capability-acquisition]] — fine-tuning vs prompt engineering vs mechanism engineering
- [[react]] — Thought→Action→Observation loop; strengths, failure modes, CoT combinations
- [[chain-of-thought]] — step-by-step reasoning prompts, CoT-SC; hallucination vs flexibility trade-off
- [[self-reflection]] — learning from mistakes via verbal lessons stored in memory; depends on evaluator quality
- [[hallucination]] — false confident outputs; how each paper sees it and mitigations (grounding, feedback, reflection, citing evidence)
- [[tool-use]] — why agents need tools; prompting vs fine-tuning routes; findings and open problems
- [[agent-evaluation]] — subjective and objective evaluation; metrics, protocols, benchmarks

## Entities
- [[hotpotqa]] — multi-hop QA benchmark (EM)
- [[fever]] — fact-verification benchmark (accuracy)
- [[alfworld]] — text-based household game (success rate)
- [[webshop]] — web shopping environment (score, success rate)
- [[lama]] — factual-knowledge completion probe
- [[humaneval]] — code-generation benchmark (pass@1)
- [[smallville]] — sandbox town for 25 generative agents
- [[shunyu-yao]] — author (ReAct, Reflexion)
- [[karthik-narasimhan]] — author (ReAct, Reflexion)

## Syntheses
- [[react-vs-toolformer]] — prompting vs self-supervised fine-tuning for tool use; complementary strengths
- [[reflection-two-ways]] — Reflexion (learn from failure) vs Generative Agents (abstract insights) reflection
