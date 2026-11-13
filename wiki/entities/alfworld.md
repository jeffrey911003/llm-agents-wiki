---
type: entity
title: ALFWorld
tags: [benchmark, text-game, embodied, decision-making]
sources: [yao2023-react, wang2023-agent-survey, shinn2023-reflexion]
updated: 2026-11-13
---
# ALFWorld

## What it is
A synthetic text-based household game aligned with the embodied ALFRED benchmark; 6 task types (e.g. "examine paper under desklamp") solved through text actions such as "go to coffeetable 1" ([[yao2023-react]] §4). Instances can have 50+ locations and need 50+ expert steps ([[yao2023-react]] §4).

## Used in
- [[yao2023-react]] — 134 unseen evaluation games; metric success rate (§4, Table 3).
- [[shinn2023-reflexion]] — same 134 environments, ReAct as Actor (§4.1).
- Listed by [[wang2023-agent-survey]] as a common agent-evaluation environment (§4.2).

## Key facts
- ReAct 71% (best of 6) vs Act 45% vs BUTLER 37% ([[yao2023-react]] Table 3).
- ReAct + Reflexion: 130/134 tasks over 12 trials ([[shinn2023-reflexion]] §4.1).
> [!note] Numbers are not directly comparable: ReAct reports single-attempt success with PaLM-540B; Reflexion counts tasks solved across up to 12 trials with GPT-3 ([[yao2023-react]] §2; [[shinn2023-reflexion]] §4.1).

Related: [[agent-evaluation]] · [[webshop]]
