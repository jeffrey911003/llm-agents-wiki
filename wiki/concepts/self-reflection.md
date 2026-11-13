---
type: concept
title: Self-Reflection
tags: [memory, feedback, learning]
sources: [wang2023-agent-survey, shinn2023-reflexion, park2023-generative-agents]
updated: 2026-11-13
---
# Self-Reflection

## Definition
The agent reviews its own past behaviour and writes higher-level conclusions in natural language, which it later uses to act better. The survey treats it both as a **memory operation** (summarizing memories into abstract insights) ([[wang2023-agent-survey]] §2.1.2) and as **model feedback** for planning ([[wang2023-agent-survey]] §2.1.3).

## How it works — Reflexion version
1. Act (Actor), 2. score the attempt (Evaluator), 3. turn the score + trajectory into a verbal lesson (Self-Reflection), 4. store it in long-term memory, 5. retry ([[shinn2023-reflexion]] §3, Algorithm 1).
- The lesson acts as a "semantic gradient" — a concrete direction for improvement instead of a scalar reward ([[shinn2023-reflexion]] §1).
- No weight updates: learning lives in memory ([[shinn2023-reflexion]] Abstract).

## Variants
- **Memory reflection** — derive abstract insights from many low-level memories, possibly hierarchically; e.g. Generative Agents, GITM, ExpeL ([[wang2023-agent-survey]] §2.1.2).
- **Self-Refine** — output → feedback → refine loop within one generation; Reflexion argues it is limited to single-generation tasks ([[wang2023-agent-survey]] §2.1.3; [[shinn2023-reflexion]] §2).

## How it works — Generative Agents version
- Triggered when recent importance sums past 150; the agent asks itself 3 high-level questions, retrieves evidence, and writes 5 insights that cite the supporting memories ([[park2023-generative-agents]] §4.2).
- Reflections can build on reflections, forming a tree from observations up to self-concepts ([[park2023-generative-agents]] §4.2, Fig. 7).
- Comparison with Reflexion: [[reflection-two-ways]].

## Evidence
- Removing reflection lowers believability (TrueSkill 29.89 → 26.88) ([[park2023-generative-agents]] §6.5.1).
- Reflection beats plain episodic memory (replaying the last trajectory) by 8% on HotpotQA ([[shinn2023-reflexion]] §4.2).
- Without reflection, ReAct on ALFWorld plateaus with ~22% hallucination; with it, 130/134 tasks solved ([[shinn2023-reflexion]] §4.1, Fig. 3).

## Key caveat: reflection is only as good as the evaluator
- Reflection without self-generated tests *hurts* coding accuracy (0.52 vs 0.60 baseline); tests without reflection do not help (0.60) ([[shinn2023-reflexion]] Table 3).
- Unreliable tests (16.3% false positives on MBPP Python) make Reflexion lose to GPT-4 there ([[shinn2023-reflexion]] §4.3).
- The method depends on the LLM's self-evaluation ability and has no success guarantee ([[shinn2023-reflexion]] §1).

## Related concepts
[[memory]] · [[planning]] · [[react]] · [[agent-evaluation]] · [[reflection-two-ways]]
