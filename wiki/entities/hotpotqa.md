---
type: entity
title: HotpotQA
tags: [benchmark, question-answering]
sources: [yao2023-react, shinn2023-reflexion]
updated: 2026-11-13
---
# HotpotQA

## What it is
A multi-hop question-answering benchmark that requires reasoning over two or more Wikipedia passages ([[yao2023-react]] §3.1).

## Used in
- [[shinn2023-reflexion]] — 100 questions, binary EM feedback between trials (§4.2, Fig. 4).
- [[yao2023-react]] — question-only setup with a Wikipedia API; metric EM (§3.1, Table 1).

## Key facts
- Best ReAct-family result (PaLM-540B prompting): 35.1 EM with ReAct → CoT-SC, vs supervised SoTA 67.5 ([[yao2023-react]] Table 1).
- Reflexion improves ~20% over baselines across trials ([[shinn2023-reflexion]] §1).
- Some questions may have outdated labels ([[yao2023-react]] §3.3).

Related: [[agent-evaluation]] · [[fever]]
