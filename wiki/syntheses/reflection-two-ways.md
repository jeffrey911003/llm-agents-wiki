---
type: synthesis
title: "Two kinds of reflection: Reflexion vs Generative Agents"
tags: [comparison, self-reflection, memory]
sources: [shinn2023-reflexion, park2023-generative-agents, wang2023-agent-survey]
updated: 2026-11-13
---
# Two kinds of reflection

## Question
Both papers call it "reflection". Is it the same mechanism?

## Side-by-side
| Dimension | [[shinn2023-reflexion]] | [[park2023-generative-agents]] |
|---|---|---|
| Purpose | fix mistakes on a task across trials (§1) | generalize experiences into higher-level beliefs (§4.2) |
| Trigger | Evaluator says the trial failed (§3, Alg. 1) | summed importance of recent events > 150 (§4.2) |
| Input | trajectory + reward signal (§3) | recent memories retrieved by self-generated questions (§4.2) |
| Output | a verbal lesson on what to do differently (§3) | 5 insights, each citing evidence records (§4.2) |
| Stored as | long-term memory, capped at 1–3 entries (§3) | memory objects in the stream, can form a tree (§4.2, Fig. 7) |
| Success measure | task success (ALFWorld, HotpotQA, pass@1) (§4) | human-rated believability (§6) |
| Ablation result | reflection + tests 0.68 vs base 0.60 on hard Rust (Table 3) | no-reflection drops TrueSkill 29.89 → 26.88 (§6.5.1) |

## Synthesis
- The survey's two roles for reflection map neatly onto these papers: Reflexion = **model feedback for planning**, Generative Agents = **memory reflection** that abstracts insights ([[wang2023-agent-survey]] §2.1.2–2.1.3).
- Both depend on a grounding signal: Reflexion needs a reliable evaluator (reflection without tests hurts, [[shinn2023-reflexion]] Table 3); Generative Agents forces each insight to cite its source memories ([[park2023-generative-agents]] §4.2).
- Both still hallucinate when grounding is weak: ReAct-only agents plateau at ~22% hallucination before Reflexion ([[shinn2023-reflexion]] Fig. 3); generative agents embellish memories ([[park2023-generative-agents]] §6.5.2).

## For the slide deck
"Reflection = the agent writes notes to itself. Reflexion writes *what went wrong*; Generative Agents writes *what this all means*."

Related: [[self-reflection]] · [[memory]]
