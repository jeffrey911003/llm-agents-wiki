---
type: paper
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
authors: [Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom]
year: 2023
venue: NeurIPS 2023; arXiv v1 (Feb 2023)
arxiv: "2302.04761"
tags: [tool-use, fine-tuning, self-supervised]
sources: [schick2023-toolformer]
updated: 2026-11-13
---
# Toolformer (Schick et al., 2023)

## TL;DR
Toolformer teaches a language model to decide **which API to call, when, with what arguments, and how to use the result**, via self-supervised fine-tuning from only a handful of demonstrations per tool (Abstract, §1). A 6.7B GPT-J model with tools often matches or beats the 175B GPT-3 in zero-shot settings without losing language-modeling ability (Abstract, §4).

## Problem
LMs struggle with basic skills where small tools excel — arithmetic, factual lookup, up-to-date information, low-resource languages, awareness of time (§1). Prior tool-use approaches needed large human annotation or were limited to task-specific settings (§1).

## Method (§2, Fig. 2)
- API calls are written inline as text: `<API> name(input) → result </API>` (in practice `[`, `]`, `->`) (§2).
- **1. Sample** — a prompt with a few examples per tool makes the LM itself annotate a large text corpus with candidate API calls at positions where it assigns high probability to starting a call (§2, Fig. 3).
- **2. Execute** — run every candidate call and get a text result (§2).
- **3. Filter** — keep a call only if giving the model the call *and* its result lowers the loss on the following tokens by at least τ_f, compared with no call or a call without result: `L⁻ − L⁺ ≥ τ_f` (§2).
- **4. Fine-tune** the same LM on the augmented corpus; the text is otherwise unchanged, so general LM ability is preserved (§2).
- **Inference** — decode normally; when the model emits `→`, pause, call the API, insert the result and continue (§2).
- Setup: GPT-J (6.7B) on a CCNet subset (§4.1). Decoding starts an API call if `<API>` is among the top-k=10 tokens, at most one call per input (§4.2).

## Tools (§3)
| Tool | Implementation |
|---|---|
| Question answering | Atlas (retrieval-augmented LM fine-tuned on Natural Questions) |
| Wikipedia search | BM25 over KILT Wikipedia dump |
| Calculator | four basic operations, rounded to 2 decimals |
| Calendar | returns current date, no input |
| Machine translation | NLLB 600M, any language → English |

## Experiments & Key Results (zero-shot, §4.2)
| Task (metric per §4.2) | GPT-J | Toolformer | GPT-3 175B | Tool mostly used |
|---|---|---|---|---|
| [[lama]] T-REx | 31.9 | **53.5** | 39.8 | QA (98.1% of cases) (Table 3) |
| ASDiv (math) | 7.5 | **40.4** | 14.0 | calculator (97.9%) (Table 4) |
| SVAMP (math) | 5.2 | **29.4** | 10.0 | calculator (Table 4) |
| WebQuestions | 18.5 | 26.3 | **29.0** | Wikipedia search (99.3%) (Table 5) |
| Natural Questions | 12.8 | 17.7 | **22.6** | Wikipedia search (Table 5) |
| DATESET (dates) | 3.9 | **27.3** | 0.8 | calendar (54.8%) (Table 7) |

- QA: still behind GPT-3, attributed to a weak search engine and the inability to reformulate queries or browse results (§4.2.3).
- Multilingual QA (MLQA): tools help every language, but Toolformer does not consistently beat plain GPT-J because CCNet fine-tuning hurts some languages (§4.2.4, Table 6).
- No perplexity cost: with API calls disabled, perplexity equals the model fine-tuned without API calls (WikiText 10.3, CCNet 10.5) (§4.3, Table 8).
- **Scaling:** the ability to use tools emerges only at ~775M parameters; smaller GPT-2 models perform the same with or without tools (§4.4, Fig. 4).
- With greedy decoding (k=1) the model is partly calibrated — it calls APIs on examples it would otherwise get wrong — but this calibration is lost at larger k (§5, Table 9).

## Limitations (§7)
- Cannot **chain** tools (one tool's output as another's input), because calls were sampled independently.
- Cannot use tools **interactively** (browse results, refine a search query).
- Sensitive to the exact wording of inputs when deciding whether to call an API.
- Sample-inefficient for some tools (over a million documents → only a few thousand useful calculator calls).
- Ignores the computational cost of an API call.

## Connections
- [[tool-use]] — main concept; compared with [[react]] in [[react-vs-toolformer]].
- [[capability-acquisition]] — an example of acquiring capability by fine-tuning on model-generated data.
- [[action]] — cited by [[wang2023-agent-survey]] as an example of an agent action space using external APIs (§2.1.4).
