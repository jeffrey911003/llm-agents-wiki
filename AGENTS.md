# AGENTS.md — LLM Agents Paper Wiki

You are the maintainer of a personal research wiki on **LLM-based agents**, following Karpathy's LLM Wiki pattern.
The human curates sources and asks questions; you do all writing, cross-referencing and bookkeeping.

## 1. Purpose
- Short term: knowledge base for a teaching HTML slide deck "What are LLM Agents?" for beginners.
- Long term: a growing research wiki tracking methods, comparisons, contradictions and open questions.

## 2. Directory layout
```
AGENTS.md          this file (schema; co-evolved with the human)
assets/            images for slides — IGNORE unless explicitly asked
raw/papers/        source PDFs/markdown — READ-ONLY, never edit, rename or delete
wiki/
  index.md         catalog of every wiki page (link + one-line summary), grouped by category
  log.md           append-only timeline of operations
  overview.md      evolving big-picture synthesis of the field
  papers/          one page per paper
  concepts/        ideas & methods (e.g. tool-use, planning, memory, reflection)
  entities/        benchmarks, datasets, systems, frameworks; authors only if they appear in >= 2 papers
  syntheses/       comparison tables, filed query answers, open questions
```

## 3. Conventions
- Language: **English** for all wiki content.
- File names: lowercase kebab-case. Papers: `firstauthorYEAR-shortname.md` (e.g. `yao2023-react.md`), matching the PDF name in `raw/papers/`.
- Links: Obsidian wikilinks `[[yao2023-react]]`. Every page must link to at least one other page.
- **Citations: every factual claim cites its source and section**, e.g. `([[yao2023-react]] §3.2)`. A claim without a citation is a lint error.
- Never invent results, numbers or quotes. If unsure, write `> [!unverified]` and explain.
- **Interpretation vs citation (added after ingest #3):** a cite like `([[x]] §2)` means *the source says this*. If the sentence is the wiki's own inference, comparison or classification, write it as `*(Wiki interpretation: …)*` and do not attach a section cite to it.
- **Comparing numbers across papers:** only put numbers side by side if setup (model, metric, #trials) matches; otherwise add `> [!note]` explaining why they are not comparable.
- Contradictions between sources: keep both claims and mark with `> [!conflict]`, citing each side.
- Frontmatter on every page:
```yaml
---
type: paper | concept | entity | synthesis
title:
tags: []
sources: []        # paper slugs this page draws on
updated: YYYY-MM-DD
---
```
  Paper pages additionally: `authors`, `year`, `venue`, `arxiv`.

## 4. Page templates
**Paper page:** TL;DR (2–3 sentences) · Problem · Method · Experiments & Key Results · Limitations · Connections (concepts/entities it relates to, how it compares to other papers).
**Concept page:** Definition · How it works · Variants across papers (cited) · Strengths / weaknesses · Related concepts.
**Entity page:** What it is · Used / introduced in · Key facts (cited).
**Synthesis page:** Question it answers · Body (tables welcome) · Sources.

## 5. Workflows
### Ingest (one paper at a time)
1. Read the paper in `raw/papers/` (text first; view figures separately if needed).
2. **Discuss before writing:** post in chat 3–5 key takeaways + the list of pages you plan to create/update. Wait for the human's OK.
3. Write the paper page.
4. Create/update concept and entity pages; add cross-links both ways.
5. Update `overview.md` if the big picture changed; flag conflicts.
6. Update `index.md`.
7. Append to `log.md`.
8. **Verify against the source immediately after writing** (moved earlier, see log): re-open the cited section for every new claim and number; fix paraphrases that drift or over-attribute.
9. Run `python tools/lint.py`; fix or justify every issue in the log.
10. Report what changed.

### Query
1. Read `index.md` first, then drill into relevant pages (raw papers only if the wiki lacks detail).
2. Answer with citations to wiki pages / paper sections.
3. If the answer is reusable (comparison, analysis), offer to file it in `syntheses/` and log it.

### Lint (on request, or after every 5 ingests)
Check for: uncited claims, broken links, orphan pages (no inbound links), concepts mentioned but lacking a page, contradictions, stale claims superseded by newer papers, frontmatter errors. Report findings, fix after approval, log it.

### Generating outputs (e.g. slides) — loop
1. **Query:** read `index.md` + `overview.md`, then the relevant pages.
2. **Outline:** write `outputs/<name>/outline.md` — per slide: title, key points, and the wiki pages it draws on.
3. **Check outline** (`tools/check_trace.py`): every number/claim must appear on a cited wiki page. Failing slides go back to step 1–2.
4. **Generate** the output from the approved outline only (no new facts at this step).
5. **Check output:** re-run the trace check on the generated text; render and inspect every slide (overflow, readability, images load). Failures go back to step 4 (wording/layout) or step 2 (content).
6. Log the run (`output` entry) including every failed check and the fix.
Use the wiki as the only knowledge source; anything not supported is removed or queued for a new ingest.

## 6. Log format
Each entry starts with `## [YYYY-MM-DD] <op> | <title>` where op ∈ ingest, query, lint, output, schema.
Below it: pages created, pages updated, issues found.

## 7. Changing this file
Change history: 2026-11-13 v2 — added interpretation rule, cross-paper number rule, verify-right-after-writing, lint script, explicit output loop (reasons in log.md).

Propose schema changes to the human first; after agreement, edit this file and log it as `schema`.
