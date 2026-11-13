---
type: paper
title: "Generative Agents: Interactive Simulacra of Human Behavior"
authors: [Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein]
year: 2023
venue: UIST 2023
arxiv: "2304.03442"
tags: [simulation, memory, reflection, planning, multi-agent, believability]
sources: [park2023-generative-agents]
updated: 2026-11-13
---
# Generative Agents (Park et al., 2023)

## TL;DR
Generative agents are LLM-driven characters that simulate **believable** human behaviour. An architecture of memory stream, reflection and planning lets 25 agents in a Sims-like town ([[smallville]]) live their days, form relationships and coordinate a Valentine's Day party from a single seed idea (Abstract, §1). Ablations show each component matters for believability (Abstract, §6.5).

## Problem
LLMs can simulate behaviour at a single moment, but long-term coherence needs an architecture that manages ever-growing memories, retrieves the relevant ones, reflects to generalize, and plans (§1, §4). Prompting with the whole memory distracts the model and does not fit the context window (§4.1).

## Method (§4; LLM = gpt-3.5-turbo)
- **Profile:** one hand-written paragraph per agent (occupation, relationships), each phrase loaded as a seed memory (§3.1).
- **Memory stream** — a list of natural-language memory objects with creation and last-access timestamps (§4.1).
  - Retrieval score = α·recency + α·importance + α·relevance, each min-max normalized; all α = 1 (§4.1).
  - Recency: exponential decay (factor 0.995 per game hour since last access) (§4.1).
  - Importance: the LLM rates 1–10 (e.g. cleaning the room → 2, asking a crush out → 8) (§4.1).
  - Relevance: cosine similarity of embeddings with the query (§4.1).
- **Reflection** — triggered when summed importance of recent events exceeds 150 (≈ 2–3 times per day) (§4.2):
  1. From the 100 most recent memories, ask for the 3 most salient high-level questions.
  2. Retrieve memories for each question; ask for 5 insights, **each citing the evidence records** ("because of 1, 5, 3").
  3. Store insights as memories with pointers; reflections on reflections form a tree (§4.2, Fig. 7).
- **Planning and reacting** — top-down: day plan in 5–8 chunks → hour-long chunks → 5–15-minute actions; plans are stored in memory (§4.3). Each time step the agent decides whether to continue its plan or react; reacting regenerates the plan; dialogue is conditioned on memories about the other agent (§4.3.1–4.3.2).

## Experiments & Key Results
**Controlled evaluation** (§6): agents are "interviewed" on self-knowledge, memory, plans, reactions, reflections; 100 human evaluators rank believability; scored with TrueSkill (§6.1–6.4).

| Condition | TrueSkill μ (Fig. 8, §6.5.1) |
|---|---|
| Full architecture | **29.89** |
| No reflection | 26.88 |
| No reflection, no planning | 25.64 |
| Human crowdworkers | 22.95 |
| No memory/reflection/planning (prior state of the art) | 21.21 |

- Full vs prior-work condition: effect size d = 8.16 (§6.5.1). All pairwise differences significant except crowdworker vs fully ablated (§6.5.1).
- Reflection is needed for synthesis, e.g. choosing a birthday gift based on what a friend cares about (§6.5.3).

**End-to-end** (25 agents, 2 game days) (§7.1.2):
- Party awareness 1 → 13 agents (4% → 52%); mayoral candidacy 1 → 8 (4% → 32%); no hallucinated claims among those.
- Network density 0.167 → 0.74; 1.3% (6/453) of "do you know X" answers hallucinated.
- 5 of 12 invited agents attended the party (§7.1.2, Fig. 9).

## Failure modes
- Retrieval failures and incomplete memory fragments (§6.5.2).
- **Embellishment**: adding details never experienced (e.g. "he's going to make an announcement tomorrow") or importing world knowledge (neighbour Adam Smith "authored Wealth of Nations") (§6.5.2).
- Odd location choices as memory grows; violating physical norms (one-person bathroom, closed shops); overly formal and overly cooperative behaviour, likely from instruction tuning (§7.2).

## Limitations (§8.2)
- Cost: simulating 25 agents for two days cost thousands of dollars in tokens and took multiple days.
- Short evaluation timescale; crowdworker baseline is not maximal human performance.
- Robustness unknown: prompt hacking, memory hacking, hallucination; inherited LLM biases.
- Ethics: risk of parasocial relationships; agents should disclose they are computational (§8.3).

## Connections
- Core concepts: [[memory]], [[self-reflection]], [[planning]], [[profiling]]; contrast with Reflexion in [[reflection-two-ways]].
- The survey uses this paper as its example of handcrafted profiles, three-score memory reading (α = β = γ = 1) and the question→insight reflection process ([[wang2023-agent-survey]] §2.1.1–2.1.2) — consistent with the paper (§3.1, §4.1–4.2).
- Evaluation style = subjective/human evaluation in [[agent-evaluation]]; environment: [[smallville]].
