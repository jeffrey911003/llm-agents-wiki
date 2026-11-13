---
type: entity
title: HumanEval
tags: [benchmark, code-generation]
sources: [shinn2023-reflexion]
updated: 2026-11-13
---
# HumanEval

## What it is
A benchmark measuring function-body generation accuracy from natural-language descriptions; reported as pass@1 ([[shinn2023-reflexion]] §4.3). A Rust version is built by translating problems with MultiPL-E ([[shinn2023-reflexion]] §4.3).

## Used in
- [[shinn2023-reflexion]] — Python and Rust (hardest 50 problems) (§4.3, Tables 1–3).

## Key facts
- Python pass@1: Reflexion 91.0 vs GPT-4 80.1 ([[shinn2023-reflexion]] Table 1).

Related: [[agent-evaluation]]
