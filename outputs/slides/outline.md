# Outline — 「LLM Agents 是什麼？」教學簡報（15 張，繁中）
Audience: 完全不熟悉 AI Agent 的初學者。Rule: only facts from the wiki; each slide lists its wiki sources.

## S1 封面：LLM Agents 是什麼？
- 副標：從「會聊天」到「會做事」的 AI
- 本簡報內容全部來自自建的 LLM Wiki（5 篇論文）
sources: overview, index

## S2 一般 LLM vs. LLM Agent
- 一般 LLM：你問、它答，一次就結束
- Agent：扮演角色、感知環境、採取行動、隨時間學習
- 定義：身處環境中、感知環境並對其行動、追求自己目標的系統（Franklin & Graesser 1997）
- LLM Agent = 用 LLM 當「大腦」的這種系統
sources: llm-based-agent

## S3 為什麼光有 LLM 不夠？
- 弱點：算數、查事實、不知道最新資訊、不知道今天幾號
- 幻覺：很有自信地講錯的事
- 解法方向：加上記憶、規劃、工具、反思
sources: tool-use, hallucination, schick2023-toolformer

## S4 Agent 的四大模組（核心圖）
- Profile 角色 → Memory 記憶 + Planning 規劃 → Action 行動
- 圖：Survey Fig. 2
sources: wang2023-agent-survey, overview
image: wang2023-fig2-agent-framework.png

## S5 ① Profile：我是誰？
- 把角色寫進 prompt：基本資料、個性、人際關係
- 三種做法：手寫、讓 LLM 生成、從真實資料對齊
- 例：Generative Agents 每個角色一段手寫描述，每句變成初始記憶
sources: profiling

## S6 ② Memory：記得什麼、想起什麼？
- 短期記憶 ≈ context window；長期記憶 ≈ 外部資料庫
- 想起哪段記憶看三件事：多近（recency）、多重要（importance）、多相關（relevance）
- 例：重要性由 LLM 打 1–10 分 — 打掃房間 2 分，約暗戀對象 8 分
sources: memory, park2023-generative-agents

## S7 ③ Planning：怎麼拆解任務？
- 不看回饋：Chain-of-Thought 一步一步想；Tree of Thoughts 走多條路
- 看回饋：來自環境、人、模型自己
- 階層規劃：一天大綱 → 每小時 → 每 5–15 分鐘
- 反例：沒有規劃的 Agent 會在 12 點、12:30、1 點各吃一次午餐
sources: planning, chain-of-thought

## S8 ④ Action：真的去做
- 行動目標：完成任務、溝通、探索
- 行動空間：外部工具（API、資料庫、其他模型）或 LLM 自身知識
- 行動影響：改變環境、改變自己（例如更新記憶）、觸發新行動
sources: action, tool-use

## S9 經典做法一：ReAct ＝ 想一想 → 做一下 → 看結果
- Thought → Action → Observation 不斷循環
- 只要 1–6 個示範例子，不用訓練
- 圖：同一題，CoT 自己瞎猜答錯，ReAct 查 Wikipedia 答對
sources: react, yao2023-react
image: yao2023-fig1-hotpotqa-only.png

## S10 ReAct 的成績單
- HotpotQA 失敗原因：CoT 有 56% 是幻覺，ReAct 是 0%
- 代價：ReAct 推理錯誤 47%（CoT 16%），容易原地打轉
- ALFWorld 成功率：ReAct 71% vs 只行動 45% vs 模仿學習 BUTLER 37%
sources: yao2023-react, react, alfworld

## S11 經典做法二：Toolformer ＝ 自己學會用工具
- 模型在文本中自己插入 API 呼叫 → 執行 → 只留下「真的有幫助」的
- 5 種工具：問答、Wikipedia 搜尋、計算機、行事曆、翻譯
- 6.7B 小模型在數學 ASDiv 拿 40.4，贏過 175B 的 GPT-3（14.0）
- 限制：每題最多呼叫 1 次、不能串接工具
sources: schick2023-toolformer, tool-use, react-vs-toolformer
image: schick2023-fig1-tool-calls.png

## S12 經典做法三：Reflexion ＝ 從失敗中學習
- 失敗 → 用文字寫下反省 → 存進記憶 → 再試一次（不用重新訓練）
- ALFWorld：134 題解出 130 題
- HumanEval 寫程式：91.0%（GPT-4 80.1%）
- 但：沒有可靠的檢查（自寫測試），反省反而更差：52% vs 60%
sources: shinn2023-reflexion, self-reflection
image: shinn2023-fig2-reflexion-loop.png

## S13 經典做法四：Generative Agents ＝ 會過生活的 AI 小鎮
- 25 個 Agent 住在 Smallville：記憶流 + 反思 + 規劃
- 只告訴一個人「想辦情人節派對」→ 兩天後 13 人知道、12 位受邀者中 5 位出席
- 拿掉反思、規劃，「像真人」的分數一路下降：29.89 → 26.88 → 25.64
sources: park2023-generative-agents, smallville
image: park2023-fig9-party-diffusion.png

## S14 怎麼評估 Agent？還有哪些挑戰？
- 主觀：請人評分、訪談 Agent、圖靈測試
- 客觀：成功率、benchmark（HotpotQA、ALFWorld、WebShop、HumanEval）
- 挑戰：幻覺、角色扮演、對齊人類價值、prompt 穩健性、效率
sources: agent-evaluation, hallucination, wang2023-agent-survey

## S15 重點回顧
- Agent = LLM ＋ 角色 ＋ 記憶 ＋ 規劃 ＋ 行動
- ReAct（邊想邊做）、Toolformer（自學工具）、Reflexion（從錯中學）、Generative Agents（模擬人）
- （Wiki 綜合觀點）共同關鍵：把 LLM 接上真實資訊與可靠的檢查，才能減少幻覺
- 參考文獻：5 篇論文
sources: overview, hallucination, react-vs-toolformer, reflection-two-ways, wang2023-agent-survey, yao2023-react, schick2023-toolformer, shinn2023-reflexion, park2023-generative-agents
