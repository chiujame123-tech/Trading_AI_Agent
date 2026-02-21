# -*- coding: utf-8 -*-
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
import os

print("啟動中... 正在喚醒本地大腦 Qwen 2.5...")

# 1. 連結你本地嘅 Ollama 大腦 (qwen2.5:7b)
local_llm = Ollama(model="qwen2.5:7b")

# 2. 裝備搜尋上網工具
search_tool = DuckDuckGoSearchRun()
"C:\Users\kpchi\OneDrive\桌面\TradingExpertBrain\04_Trading_Strategies"
# ==========================================
# ⚠️ 請修改呢度：換成你 Obsidian 資料夾嘅真實路徑
# ==========================================
OBSIDIAN_FILE_PATH = "C:\\Users\\YourName\\Desktop\\TradingExpertBrain\\04_Trading_Strategies\\Qullamaggie_Latest_Tips.md" 

# 3. 建立你嘅專屬交易研究員 (Agent)
researcher = Agent(
    role='Senior Swing Trading Researcher',
    goal='在互聯網上搜尋最新、高質素的 Swing Trading (波段交易) 和 Qullamaggie 突破策略的討論與實戰心得。',
    backstory='你是一位頂級的量化對沖基金研究員。你擅長從繁雜的網絡資訊中，提煉出真正能賺錢的交易紀律、VCP 形態要點和心態管理技巧。',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=local_llm
)

# 4. 指派任務 (Task) 俾佢
task1 = Task(
    description='搜尋關於 "Qullamaggie breakout strategy tips 2026" 或 "Swing trading VCP setup advice" 的最新文章。總結當中的核心規則、止損技巧以及近期市場的實戰案例。',
    expected_output='一篇排版清晰的 Markdown 筆記。必須包含：1. 大標題 2. 核心策略要點 (Bullet points) 3. 風險管理建議 4. 總結。請全部用繁體中文撰寫。',
    agent=researcher,
    output_file=OBSIDIAN_FILE_PATH  # 自動寫入 Obsidian
)

# 5. 組建特工團隊並執行 (Kickoff)
crew = Crew(
    agents=[researcher],
    tasks=[task1],
    verbose=True,
    process=Process.sequential
)

print("🚀 特工已經出發上網搵料，請耐心等候幾分鐘...\n")
result = crew.kickoff()

print(f"\n✅ 任務完成！筆記已經成功寫入: {OBSIDIAN_FILE_PATH}")
