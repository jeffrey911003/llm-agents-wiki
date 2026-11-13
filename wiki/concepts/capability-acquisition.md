---
type: concept
title: Capability Acquisition
tags: [training, prompting]
sources: [wang2023-agent-survey, schick2023-toolformer, yao2023-react]
updated: 2026-11-13
---
# Capability Acquisition

## Definition
How an agent gains task-specific skills and experience — the "software" running on the architecture's "hardware" ([[wang2023-agent-survey]] §2.2).

## Strategies ([[wang2023-agent-survey]] §2.2, Fig. 4)
- **With fine-tuning** — on human-annotated, LLM-generated, or real-world datasets.
- **Without fine-tuning**
  - *Prompt engineering* — put useful information (e.g. examples, reasoning steps) into the prompt.
  - *Mechanism engineering* — design specialized modules or working rules so the agent improves itself: trial-and-error, crowd-sourcing, experience accumulation, self-driven evolution.

## Examples in this wiki
- **Fine-tuning on model-generated data:** Toolformer has the LM annotate its own corpus with API calls, keeps only helpful ones, and fine-tunes on the result ([[schick2023-toolformer]] §2). *(Wiki interpretation: this matches the survey's "LLM-generated datasets" category; the survey itself lists Toolformer under action-space tools, §2.1.4.)*
- **Fine-tuning on agent trajectories:** fine-tuning PaLM-8B/62B on 3,000 ReAct trajectories beats prompting much larger models ([[yao2023-react]] §3.3).
- **Prompt engineering:** ReAct prompting with 1–6 examples ([[yao2023-react]] §2).

## Shift across eras
Traditional ML: capability lives in parameters learned from data. LLM era: parameters *or* prompts. Agent era: fine-tuning, prompt engineering, *and* mechanism engineering ([[wang2023-agent-survey]] §2.2, Fig. 4).

## Related concepts
[[llm-based-agent]] · [[memory]] · [[planning]] · [[tool-use]] · [[react-vs-toolformer]]
