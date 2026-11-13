---
type: synthesis
title: "ReAct vs Toolformer: two routes to tool-using LLMs"
tags: [comparison, tool-use]
sources: [yao2023-react, schick2023-toolformer, wang2023-agent-survey]
updated: 2026-11-13
---
# ReAct vs Toolformer

## Question
Both papers let an LLM use external tools. How do their approaches differ, and what does each get right?

## Side-by-side
| Dimension | [[yao2023-react]] | [[schick2023-toolformer]] |
|---|---|---|
| Capability acquisition | Prompting, 1–6 examples, frozen PaLM-540B (§2) | Self-supervised fine-tuning of GPT-J 6.7B (§2, §4.1) |
| Supervision | human-written trajectories (§2) | few demos per API; model annotates its own data (§2) |
| Explicit reasoning | thoughts interleaved with actions (§2) | none — API calls inserted inline into text (§2) |
| Tool interaction | multi-step loop, can re-search after failure (Fig. 1) | ≤ 1 call per input; no chaining or interaction (§4.2, §7) |
| Tools | Wikipedia search/lookup; game & web actions (§3.1, §4) | QA, Wikipedia search, calculator, calendar, MT (§3) |
| Typical setting | agents in environments (ALFWorld, WebShop) (§4) | general LM text generation, zero-shot tasks (§4.2) |
| Main weakness | reasoning loops, needs informative search (§3.3) | no chaining/interaction; prompt sensitivity (§7) |

## Synthesis
- **Complementary strengths.** ReAct shows *how* to use tools over many steps with explicit reasoning; Toolformer shows *how a model can learn by itself when a tool is worth calling*. Toolformer's own limitations (no chaining, no interactive search) are exactly what ReAct's loop provides ([[schick2023-toolformer]] §7; [[yao2023-react]] §2).
- **Both point to fine-tuning.** Fine-tuned ReAct beats much larger prompted models ([[yao2023-react]] §3.3, Fig. 3), and Toolformer's whole method is fine-tuning ([[schick2023-toolformer]] §2) — in the survey's terms, both move from prompt engineering towards fine-tuning for [[capability-acquisition]] ([[wang2023-agent-survey]] §2.2).
- **Tool quality is a shared bottleneck.** Weak retrieval hurts both ([[yao2023-react]] Table 2; [[schick2023-toolformer]] §4.2.3).

## For the slide deck
A one-line takeaway for beginners: *ReAct = "think, then use a tool, then look at the result, repeat"; Toolformer = "the model learns on its own where a tool call helps."*

Related: [[tool-use]] · [[react]] · [[action]]
