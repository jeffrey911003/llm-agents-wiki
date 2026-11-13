# Log

## [2026-11-13] schema | Initial setup
- Created AGENTS.md, directory layout, index.md, log.md, overview.md.
- Decisions from interview: field = LLM Agents; English wiki; one-at-a-time ingest with discussion; every claim cited with section; author pages only for authors in >= 2 papers.

## [2026-11-13] ingest | Wang et al. — A Survey on LLM-based Autonomous Agents
- Discussed 5 takeaways with the human before writing; approved.
- Created: papers/wang2023-agent-survey; concepts/llm-based-agent, profiling, memory, planning, action, capability-acquisition, agent-evaluation.
- Updated: overview (four-module backbone + reading roadmap), index.
- Self-check: fixed 2 profiling claims that were paraphrased too loosely (LLM-generation, dataset alignment) after re-reading §2.1.1.
- Decision: CoT/ToT/ReAct etc. kept inside planning page for now; split into own pages when a second source covers them.
- Asset: extracted Fig. 2 (p.4) → assets/wang2023-fig2-agent-framework.png for the slide deck.
- Lint after ingest: 0 broken links, 0 orphan content pages.

## [2026-11-13] ingest | Yao et al. — ReAct: Synergizing Reasoning and Acting in Language Models
- Discussed 5 takeaways + survey/paper difference in emphasis with the human; approved.
- Created: papers/yao2023-react; concepts/react, chain-of-thought (split out now that 2 sources cover CoT); entities/hotpotqa, fever, alfworld, webshop.
- Updated: concepts/planning (note on survey vs paper emphasis, evidence section), action (language as action), agent-evaluation (benchmark table); overview (core loop section, roadmap); index.
- Not flagged as [!conflict]: survey classifies ReAct by feedback source, paper stresses internal reasoning — recorded as [!note].
- Asset: assets/yao2023-fig1-react-vs-baselines.png (full Fig. 1), assets/yao2023-fig1-hotpotqa-only.png (top half).

## [2026-11-13] ingest | Schick et al. — Toolformer: Language Models Can Teach Themselves to Use Tools
- Discussed 5 takeaways + ReAct comparison with the human; approved.
- Created: papers/schick2023-toolformer; concepts/tool-use (3 sources now); syntheses/react-vs-toolformer (first synthesis page); entities/lama.
- Updated: concepts/action (link to tool-use), capability-acquisition (examples section), agent-evaluation (LAMA row); overview (tools section, roadmap); index.
- Self-check: survey does not explicitly classify Toolformer under "LLM-generated datasets" — wording on capability-acquisition marked as wiki interpretation instead of a cited claim.
- Single-paper benchmarks (ASDiv, SVAMP, MLQA, TempLAMA, DATESET) kept on the paper page, no entity pages.
- Assets: assets/schick2023-fig1-tool-calls.png, assets/schick2023-fig2-pipeline.png.

## [2026-11-13] ingest | Shinn et al. — Reflexion: Language Agents with Verbal Reinforcement Learning
- Discussed 5 takeaways + links to ReAct/survey with the human; approved.
- Created: papers/shinn2023-reflexion; concepts/self-reflection; entities/humaneval, shunyu-yao, karthik-narasimhan (first use of the ">= 2 papers" author rule).
- Updated: concepts/memory (Reflexion example), planning (model-feedback evidence), react (how Reflexion fixes loops), agent-evaluation (table); entities/alfworld, hotpotqa; overview; index.
- Self-check: ALFWorld numbers from ReAct (71%, single attempt, PaLM) and Reflexion (130/134, up to 12 trials, GPT-3) are not comparable → added [!note] on alfworld instead of presenting them side by side.
- Venue: PDF itself says "Preprint. Under review" (v4); venue recorded with that caveat.
- Asset: assets/shinn2023-fig2-reflexion-loop.png.

## [2026-11-13] ingest | Park et al. — Generative Agents: Interactive Simulacra of Human Behavior
- Discussed 5 takeaways, survey consistency check, Reflexion contrast with the human; approved.
- Created: papers/park2023-generative-agents; entities/smallville; syntheses/reflection-two-ways.
- Updated: concepts/memory (memory stream), self-reflection (GA version + evidence), planning (hierarchical planning), profiling (example), agent-evaluation (interview method, table); overview (simulation section, roadmap complete); index.
- Cross-check: survey's description of GA (handcrafted profile, α=β=γ=1, 3 questions → 5 insights) verified against paper §3.1, §4.1–4.2 — consistent, no conflict.
- Not created: author pages (no GA author appears in another wiki paper).
- Assets: assets/park2023-fig7-reflection-tree.png, assets/park2023-fig9-party-diffusion.png.
- Milestone: 5/5 planned sources ingested.

## [2026-11-13] lint | Full wiki health check after 5 ingests
- Tool: tools/lint.py (broken links, orphans, frontmatter, uncited numeric claims, pages missing from index, frequently-mentioned concepts without a page).
- Run 1: 13 "uncited" hits → all false positives from digits inside wikilinks (e.g. [[yao2023-react]]); fixed the script to strip links first.
- Run 2: 3 uncited (catalog table rows + overview bookkeeping line; accepted, opt-out marker added) and 1 real gap: "hallucination" mentioned on 12 pages with no concept page.
- Fix: created concepts/hallucination (5 sources) and linked from overview, index, chain-of-thought, tool-use.
- Contradictions: none found. Known non-comparable numbers already flagged with [!note] (alfworld). Differences in emphasis flagged on planning (survey vs ReAct).

## [2026-11-13] schema | AGENTS.md v2 — move checks earlier
- Why: across 5 ingests the WRITE step produced all real errors (2 loose paraphrases in #1, 1 over-attribution in #3, 1 near-miss non-comparable numbers in #4); all were caught only by a self-check at the end of an ingest.
- Changes: (1) "Wiki interpretation" marker rule; (2) cross-paper number comparison rule; (3) ingest step 8 = verify each claim against source right after writing; (4) step 9 = run tools/lint.py; (5) output generation written as an explicit loop with a trace check before and after generation.
- Proposed to the human before the slide run (they asked to finish ingesting first); applied right before building slides.

## [2026-11-13] output | 教學 HTML 簡報「LLM Agents 是什麼？」(15 slides, zh-TW)
Followed AGENTS.md v2 output loop. Files: outputs/slides/{outline.md, template.html, deck.html, index.html}; tools/check_trace.py, tools/build_slides.py.
- Step 1 Query: index.md + overview.md, then 24 cited pages.
- Step 2 Outline: 15 slides, each with its wiki sources.
- Step 3 Check outline (check_trace.py) — run 1: 13/15 PASS.
  - S1 FAIL: "31 個 Wiki 頁面" not on any cited page (meta fact) → removed.
  - S12 FAIL: "52%" vs wiki "0.52" → checker false negative; taught checker that 52% == 0.52.
  - Manual review: S15 "共同關鍵…" is the wiki's own inference → labelled （Wiki 綜合觀點） per interpretation rule.
  - Run 2: 15/15 PASS.
- Step 4 Generate HTML from outline.
- Step 5 Check output — trace run 1: S15 FAIL (14 terms): reference list was added during generation but S15 did not cite the 5 paper pages → back to Step 2 (sources updated in outline and HTML) → outline + HTML both 15/15 PASS.
- Step 5 Render check (Playwright, 1280×800 light/dark + 390px phone): no overflow, all images load, 0px horizontal scroll on phone. Visual review: text and figures too small, lower third empty → back to Step 4 (type +~15%, figure height 26→31cqw) → re-render: PASS.
- Published as artifact (private link); standalone index.html kept in outputs/slides/.
