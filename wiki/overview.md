---
type: synthesis
title: Overview of LLM Agents
tags: [overview]
sources: [wang2023-agent-survey, yao2023-react, schick2023-toolformer, shinn2023-reflexion, park2023-generative-agents]
updated: 2026-11-13
---
# Overview of LLM Agents

## What is an LLM agent?
An [[llm-based-agent]] uses an LLM as the central controller of a system that senses its environment and acts on it over time in pursuit of a goal ([[wang2023-agent-survey]] §1). Unlike plain question answering, an agent must play a role, perceive and learn from its environment, and evolve ([[wang2023-agent-survey]] §2.1).

## The backbone: a four-module architecture
This wiki organizes knowledge around the unified framework of [[wang2023-agent-survey]] (§2.1, Fig. 2):

| Module | Question it answers | Page |
|---|---|---|
| Profiling | Who is the agent? | [[profiling]] |
| Memory | What does it remember, and how does it retrieve it? | [[memory]] |
| Planning | How does it break down a task and adapt the plan? | [[planning]] |
| Action | What does it do, with which tools, and with what effect? | [[action]] |

Profiling shapes memory and planning; all three shape action ([[wang2023-agent-survey]] §2.1).

## The core loop: reasoning + acting
The most influential agent loop is [[react]]: the LLM alternates *Thought → Action → Observation*, so reasoning decides what to do and actions bring back facts that ground the reasoning ([[yao2023-react]] §1–2). Compared with pure [[chain-of-thought]], it trades hallucination (56% → 0% of failures on HotpotQA) for more reasoning errors and loops (16% → 47%) ([[yao2023-react]] Table 2), and it shines on interactive tasks such as [[alfworld]] (71% vs 45% for acting-only) ([[yao2023-react]] Table 3).

## Learning from mistakes without retraining
[[self-reflection]] lets an agent improve across attempts: after failing, it writes a lesson in plain language, stores it in [[memory]], and retries ([[shinn2023-reflexion]] §3). Wrapped around ReAct this solves 130/134 ALFWorld tasks and reaches 91% pass@1 on HumanEval ([[shinn2023-reflexion]] §4.1, Table 1) — but reflection only helps when the evaluation signal is reliable ([[shinn2023-reflexion]] Table 3).

## Simulating people: memory + reflection + planning together
[[park2023-generative-agents]] combines all three modules to simulate believable humans: a memory stream with recency/importance/relevance retrieval, periodic reflection that cites its evidence, and top-down hierarchical planning (§4). In [[smallville]], one seed idea led agents to spread party invitations from 1 to 13 agents and 5 to attend (§7.1.2); every removed module lowers believability (§6.5.1). See [[reflection-two-ways]] for how this reflection differs from Reflexion's.

## Tools: extending what an agent can do
[[tool-use]] lets an LLM compensate for weaknesses such as arithmetic, factual lookup and time awareness ([[schick2023-toolformer]] §1). Two routes so far: prompt the model to use tools step by step ([[react]]), or let it teach itself when a tool call helps through self-supervised fine-tuning ([[schick2023-toolformer]] §2) — compared in [[react-vs-toolformer]]. With tools, a 6.7B model beats GPT-3 175B on math and fact completion ([[schick2023-toolformer]] Tables 3–4).

## Where capability comes from
Architecture is the "hardware"; skills come from fine-tuning, prompt engineering or mechanism engineering — see [[capability-acquisition]] ([[wang2023-agent-survey]] §2.2).

## How agents are judged
Subjective (human annotation, Turing test) and objective (metrics, protocols, benchmarks) evaluation — see [[agent-evaluation]] ([[wang2023-agent-survey]] §4).

## Open challenges
Role-playing, generalized human alignment, prompt robustness, [[hallucination]], knowledge boundary, efficiency ([[wang2023-agent-survey]] §6).

## Reading roadmap (planned ingests)
- ✅ ReAct → planning with environmental feedback (ingested)
- ✅ Toolformer → action space / tool use (ingested)
- ✅ Reflexion → model feedback and memory (ingested)
- ✅ Generative Agents → memory reading, reflection, simulation (ingested)

All 5 planned sources ingested (2026-11-13). <!-- lint-ok: bookkeeping -->
