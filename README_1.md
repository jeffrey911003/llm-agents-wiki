# LLM Agents Wiki

以 Karpathy 的 **LLM Wiki** 模式建立的論文知識庫，主題是 **LLM Agents**（以大型語言模型為核心的自主代理）。
先讓 AI 訪談我、確認需求後才建檔（`AGENTS.md`），再一篇一篇 ingest 論文；最後只用這個 Wiki 當知識來源，產生一份教學 HTML 簡報。

## 連結

| 項目 | 連結 |
|---|---|
| 教學 HTML 簡報（15 張，繁中） | https://jeffrey911003.github.io/llm-agents-wiki/outputs/slides/index.html |
| Loop / Graph 流程圖、執行紀錄、反思 | [docs/loop-and-reflection.md](docs/loop-and-reflection.md) |
| Wiki 入口（目錄） | [wiki/index.md](wiki/index.md) |
| Wiki 總覽 | [wiki/overview.md](wiki/overview.md) |
| 完整操作紀錄 | [wiki/log.md](wiki/log.md) |
| Wiki 規則書 | [AGENTS.md](AGENTS.md) |

## Ingest 的 5 篇論文

| 論文 | Wiki 頁面 |
|---|---|
| Wang et al. — A Survey on Large Language Model based Autonomous Agents | [wang2023-agent-survey](wiki/papers/wang2023-agent-survey.md) |
| Yao et al. — ReAct: Synergizing Reasoning and Acting in Language Models (ICLR 2023) | [yao2023-react](wiki/papers/yao2023-react.md) |
| Schick et al. — Toolformer: Language Models Can Teach Themselves to Use Tools | [schick2023-toolformer](wiki/papers/schick2023-toolformer.md) |
| Shinn et al. — Reflexion: Language Agents with Verbal Reinforcement Learning | [shinn2023-reflexion](wiki/papers/shinn2023-reflexion.md) |
| Park et al. — Generative Agents: Interactive Simulacra of Human Behavior (UIST 2023) | [park2023-generative-agents](wiki/papers/park2023-generative-agents.md) |

論文 PDF 不放在公開 repo 中，下載連結見 [raw/papers/DOWNLOAD.md](raw/papers/DOWNLOAD.md)。

## 資料夾結構

```
AGENTS.md          Wiki 規則書（頁面格式、引用規則、ingest / lint / 產生簡報的流程）
raw/papers/        原始論文（只讀，PDF 不上傳）
assets/            從論文擷取的圖，供簡報使用
wiki/
  index.md         所有頁面目錄
  log.md           每次 ingest、lint、schema 修改、產生簡報的紀錄
  overview.md      整個領域的總覽
  papers/          論文頁（5）
  concepts/        概念頁（12）：memory、planning、react、tool-use、self-reflection、hallucination…
  entities/        benchmark、環境、作者（9）
  syntheses/       綜合比較頁（2）：react-vs-toolformer、reflection-two-ways
outputs/slides/    簡報：outline.md（大綱＋每張來源）、template.html、index.html
tools/             lint.py（Wiki 健康檢查）、check_trace.py（簡報內容溯源檢查）、build_slides.py
docs/              loop / graph 說明與反思
```

## 流程摘要

取得資料 → 讀論文 → **先和人類討論重點** → 寫入 Wiki → **逐句比對原文** → **lint 檢查** → 更新 index / log
→ 查詢 Wiki → 整理大綱（每張投影片標來源）→ **溯源檢查** → 產生 HTML → **溯源 + 渲染檢查** → 發布

Wiki 中每一句都標註出處（論文章節、表格或圖），簡報上的每個數字和名詞都可以追溯到 Wiki 頁面。
