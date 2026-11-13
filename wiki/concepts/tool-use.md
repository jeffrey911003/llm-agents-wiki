---
type: concept
title: Tool Use
tags: [action, tool-use]
sources: [wang2023-agent-survey, yao2023-react, schick2023-toolformer]
updated: 2026-11-13
---
# Tool Use

## Definition
Letting an LLM call external tools (APIs, search engines, calculators, databases, other models) as part of its [[action]] space ([[wang2023-agent-survey]] §2.1.4).

## Why agents need tools
- LLMs struggle in domains needing expert knowledge and with hallucinations they cannot fix themselves ([[wang2023-agent-survey]] §2.1.4).
- They are weak at arithmetic, factual lookup, recent information, low-resource languages and time awareness — exactly where simple tools excel ([[schick2023-toolformer]] §1).

## Kinds of tools (survey taxonomy)
APIs (e.g. HuggingGPT, WebGPT, Toolformer), databases & knowledge bases (e.g. ChatDB with SQL), and external models ([[wang2023-agent-survey]] §2.1.4).

## Two ways to teach tool use
| | Prompting — [[react]] | Self-supervised fine-tuning — Toolformer |
|---|---|---|
| How | few in-context trajectories ([[yao2023-react]] §2) | model annotates its own corpus, keeps calls that lower future-token loss, fine-tunes ([[schick2023-toolformer]] §2) |
| Calls per task | multi-step, interactive ([[yao2023-react]] §3–4) | at most one per input ([[schick2023-toolformer]] §4.2) |
| Explicit reasoning | yes, thoughts ([[yao2023-react]] §2) | no ([[schick2023-toolformer]] §2) |

Details and discussion: [[react-vs-toolformer]].

## Findings
- Even a weak tool helps: ReAct's 3-action Wikipedia API grounds reasoning and removes hallucination as a failure mode on HotpotQA ([[yao2023-react]] §3.1, Table 2).
- Tool use lets a 6.7B model beat GPT-3 175B on math and fact-completion tasks ([[schick2023-toolformer]] Tables 3–4).
- Tool-use ability emerges only around 775M parameters ([[schick2023-toolformer]] §4.4).
- Tool quality and the ability to interact with the tool both matter: a poor search engine and no query reformulation limit QA gains ([[schick2023-toolformer]] §4.2.3); uninformative search causes 23% of ReAct failures ([[yao2023-react]] Table 2).

## Open problems
Chaining tools, interactive tool use, sensitivity to prompt wording, and tool cost awareness ([[schick2023-toolformer]] §7).

## Related concepts
[[action]] · [[react]] · [[capability-acquisition]] · [[planning]] · [[hallucination]]
