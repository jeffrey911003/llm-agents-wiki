---
type: entity
title: LAMA
tags: [benchmark, factual-knowledge]
sources: [schick2023-toolformer]
updated: 2026-11-13
---
# LAMA

## What it is
A probe of factual knowledge: complete a short statement with a missing fact such as a date or place; subsets include SQuAD, Google-RE and T-REx ([[schick2023-toolformer]] §4.2.1).

## Used in
- [[schick2023-toolformer]] — only examples whose mask is the final token; counted correct if the answer appears in the first five predicted words; Wikipedia search disabled to avoid an unfair advantage (§4.2.1).

## Key facts
- T-REx: Toolformer 53.5 vs GPT-J 31.9 vs GPT-3 175B 39.8 ([[schick2023-toolformer]] Table 3).

Related: [[agent-evaluation]] · [[tool-use]]
