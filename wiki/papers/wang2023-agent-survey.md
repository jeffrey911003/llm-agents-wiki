---
type: paper
title: A Survey on Large Language Model based Autonomous Agents
authors: [Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhi-Yuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen]
year: 2023
venue: Frontiers of Computer Science (2025); arXiv v7
arxiv: "2308.11432"
tags: [survey, architecture, taxonomy, evaluation]
sources: [wang2023-agent-survey]
updated: 2026-11-13
---
# A Survey on LLM-based Autonomous Agents (Wang et al.)

## TL;DR
A broad survey that organizes LLM-based agent research around three questions: how agents are **constructed**, where they are **applied**, and how they are **evaluated** (§1). Its main contribution is a unified architecture with four modules — profiling, memory, planning, action — that the authors argue covers most prior work (§2.1, Fig. 2).

## Problem
Earlier autonomous agents used simple heuristic policies learned in isolated, restricted environments, which keeps them far from human-level decision-making in open domains (§1). LLMs bring broad world knowledge and natural-language interfaces, triggering a surge of independently proposed agent systems that lacked a common framework (§1).

## Method (taxonomy)
- **Agent construction** (§2) is split into two problems, framed by analogy to ML: *architecture design* ≈ defining the network structure ("hardware"), *capability acquisition* ≈ learning parameters ("software") (§2, §2.2).
  - Architecture: [[profiling]] → [[memory]] + [[planning]] → [[action]]; the profile influences memory and planning, and all three influence action (§2.1).
  - Capability: fine-tuning vs. no fine-tuning (prompt engineering, mechanism engineering) — see [[capability-acquisition]] (§2.2).
- **Applications** (§3): social science (e.g. psychology, social simulation, jurisprudence, research assistants), natural science (e.g. experiment assistants, science education) and engineering (e.g. software engineering, industrial automation) (§3.1–3.3).
- **Evaluation** (§4): subjective (human annotation, Turing test) and objective (metrics, protocols, benchmarks) — see [[agent-evaluation]].

## Experiments & Key Results
Not an empirical paper; no new experiments. Fig. 1 charts the cumulative number of LLM-agent papers from Jan 2021 to Aug 2023, grouped into categories such as tool, simulation, embodied, game, web and assistant agents (§1, Fig. 1).

## Limitations
- Taxonomy reflects papers up to roughly 2023 (Fig. 1 ends Aug 2023); newer work (e.g. reasoning models, computer-use agents) is outside its scope. > [!unverified] scope of later revisions not checked section by section.
- Open challenges listed by the authors: role-playing capability, generalized human alignment, prompt robustness, hallucination, knowledge boundary, efficiency (§6.1–6.6).

## Connections
- Defines the backbone used across this wiki: [[llm-based-agent]], [[profiling]], [[memory]], [[planning]], [[action]], [[capability-acquisition]], [[agent-evaluation]].
- Cites ReAct as the example of planning with environmental feedback (§2.1.3), Reflexion for model feedback and hybrid memory (§2.1.2–2.1.3), Toolformer for tool use (§2.1.4), and Generative Agents for memory reading/reflection (§2.1.2) — to be cross-checked when those papers are ingested.
