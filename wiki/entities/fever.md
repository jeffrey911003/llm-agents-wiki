---
type: entity
title: FEVER
tags: [benchmark, fact-verification]
sources: [yao2023-react]
updated: 2026-11-13
---
# FEVER

## What it is
A fact-verification benchmark: each claim is labelled SUPPORTS, REFUTES or NOT ENOUGH INFO depending on whether a Wikipedia passage verifies it ([[yao2023-react]] §3.1).

## Used in
- [[yao2023-react]] — question-only setup with a Wikipedia API; metric accuracy (§3.1, Table 1).

## Key facts
- ReAct beats CoT here (60.9 vs 56.3), since claims can differ only slightly and retrieving accurate knowledge matters ([[yao2023-react]] §3.3).
- Best: CoT-SC → ReAct 64.6 vs supervised SoTA 89.5 ([[yao2023-react]] Table 1).

Related: [[agent-evaluation]] · [[hotpotqa]]
