---
type: entity
title: WebShop
tags: [benchmark, web-navigation, decision-making]
sources: [yao2023-react]
updated: 2026-11-13
---
# WebShop

## What it is
An online-shopping website environment with 1.18M real products and 12k human instructions; the agent must buy a product matching an instruction through web actions (search, click options, buy) ([[yao2023-react]] §4).

## Used in
- [[yao2023-react]] — 500 test instructions; metrics average score and success rate (§4, Table 4).

## Key facts
- Success rate: ReAct 40.0, Act 30.1, IL 29.1, IL+RL 28.7, human experts 59.6 ([[yao2023-react]] Table 4).

Related: [[agent-evaluation]] · [[alfworld]]
