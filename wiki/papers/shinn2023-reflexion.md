---
type: paper
title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
authors: [Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao]
year: 2023
venue: NeurIPS 2023; PDF is arXiv v4 preprint (Oct 2023)
arxiv: "2303.11366"
tags: [self-reflection, memory, feedback, coding]
sources: [shinn2023-reflexion]
updated: 2026-11-13
---
# Reflexion (Shinn et al., 2023)

## TL;DR
Reflexion improves an LLM agent across repeated trials **without updating weights**: after each attempt the agent verbally reflects on the feedback it got and stores that reflection in memory for the next attempt (Abstract, §1). It boosts ReAct/CoT agents on ALFWorld, HotpotQA and coding, reaching 91% pass@1 on HumanEval (Abstract, Table 1).

## Problem
Agents struggle to learn quickly from trial and error, because traditional RL needs many samples and expensive fine-tuning (Abstract). Scalar rewards also make credit assignment hard (§1).

## Method (§3, Fig. 2, Algorithm 1)
- **Actor** — an LLM (CoT or [[react]]) that generates text/actions, conditioned on memory (§3).
- **Evaluator** — scores a trajectory: exact match (reasoning), heuristics or an LLM (decision making), self-generated unit tests (coding) (§3, §4).
- **Self-Reflection** — an LLM that turns sparse feedback (e.g. success/fail) plus the trajectory into specific verbal feedback, described as a "semantic gradient" (§1, §3).
- **Memory** — short-term = current trajectory; long-term = stored reflections, capped at Ω (usually 1–3) to fit the context window (§3).
- Loop: act → evaluate → reflect → append to memory → retry, until the Evaluator passes or max trials (§3, Algorithm 1).
- Claimed advantages over RL: lightweight (no fine-tuning), more nuanced feedback, explicit and interpretable episodic memory (§1). Drawback: depends on the LLM's self-evaluation ability; no formal success guarantee (§1).

## Experiments & Key Results
**ALFWorld** (134 tasks, ReAct as Actor, GPT-3) (§4.1):
- ReAct + Reflexion solves 130/134 tasks; ReAct alone stops improving between trials 6 and 7 (§4.1).
- Heuristic trigger for reflection: same action and response repeated > 3 cycles, or > 30 actions (§4.1).
- ReAct-only converges to a ~22% hallucination rate (e.g. believing it holds an item it doesn't) with no recovery; Reflexion eliminates almost all such cases (§4.1, Fig. 3).

**HotpotQA** (100 questions) (§4.2, Fig. 4):
- ~20% improvement over strong baselines (§1, §4).
- Baselines (ReAct-only, CoT-only) never solve a task they failed in trial 1, even with temperature 0.7 (§4.2).
- With ground-truth context, CoT still misses 39% of questions; Reflexion raises accuracy by 14% (§4.2).
- Self-reflection adds an 8% absolute boost over simply keeping the last trajectory as episodic memory (§4.2).

**Programming** — pass@1 (Table 1):

| Benchmark | Previous / GPT-4 | Reflexion |
|---|---|---|
| [[humaneval]] (Python) | 80.1 (GPT-4) | **91.0** |
| HumanEval (Rust) | 60.0 | **68.0** |
| MBPP (Python) | **80.1** | 77.1 |
| MBPP (Rust) | 70.9 | **75.4** |
| LeetcodeHard (Python) | 7.5 | **15.0** |

- MBPP Python loses because self-generated tests give false positives 16.3% of the time (vs 1.4% on HumanEval Python) (§4.3, Table 2).
- Ablation on 50 hardest HumanEval Rust problems: baseline 0.60; reflection without tests 0.52; tests without reflection 0.60; full Reflexion 0.68 (Table 3). Without tests the agent cannot tell whether code is correct and makes harmful edits (§4.3).

## Limitations (§5)
- Natural-language policy optimization can get stuck in local minima.
- Long-term memory is only a small sliding window; vector or SQL memory left for future work.
- Test-driven self-evaluation struggles with non-deterministic, impure, hardware-dependent or concurrent code.
- Generated code runs unvalidated — use sandboxed execution (§8).

## Connections
- [[self-reflection]] — core concept; also [[memory]] (hybrid memory) and [[planning]] (model feedback).
- Builds on [[react]] and [[chain-of-thought]] as Actors; addresses ReAct's repetitive-loop failure ([[yao2023-react]] §3.3).
- Shares authors with ReAct: [[shunyu-yao]], [[karthik-narasimhan]].
- Survey classification matches: hybrid memory and model feedback ([[wang2023-agent-survey]] §2.1.2–2.1.3).
- Benchmarks: [[alfworld]], [[hotpotqa]], [[humaneval]].
