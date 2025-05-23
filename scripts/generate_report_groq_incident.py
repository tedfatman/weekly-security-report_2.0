import os
from groq import Groq

MERGED_FILE = "../data/incident.md"
REPORT_FILE = "../data/incident_report.md"

# ✅ API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ 環境變數 GROQ_API_KEY 未設定！")

client = Groq(api_key=GROQ_API_KEY)

# ✅ 讀取合併後內容
if not os.path.exists(MERGED_FILE):
    raise FileNotFoundError(f"❌ 找不到合併檔案：{MERGED_FILE}")

with open(MERGED_FILE, "r", encoding="utf-8") as f:
    merged_content = f.read()

# ✅ Prompt 設定
prompt = f"""
你是一位資安新聞彙整助手，我提供給你的是一週內彙整的「資安事件」段落原始內容。這些事件包含駭客攻擊、資安漏洞遭利用、資料外洩與勒索等情形，但內容可能存在資訊重複、敘述雜亂、時間標示不一致等問題。

請你協助我進行更進一步的彙整與優化，並請嚴格遵守以下規則：

1. 使用繁體中文。
2. 每一行事件請使用 `* ` 開頭（星號 + 空格），不要使用破折號、數字或段落。
3. 每則事件應包含以下要素（如有）：
   - 發生時間（西元年-月-日）
   - 被攻擊或揭露的對象
   - 攻擊手法或事件性質（例如：DDoS、勒索、漏洞利用、資料外洩）
   - 結果與影響（如：網站癱瘓、資料竊取、系統中斷）
4. 若同一事件多次出現，請合併為一條。
5. 若某些事件出現但缺乏明確時間，請保留但註記為「時間未說明」。
6. 請勿產生虛構資訊；僅彙整已提供的內容。
7. 彙整後的事件請依照時間由早至晚（升冪順序）排列，如無具體日期則排在最後，並標註為「時間未說明」。

---

以下是原始「資安事件」段落（請保留段落標題 `### 3. 資安事件`，僅整理內文）：

### 3. 資安事件
{merged_content}
"""

# ✅ 呼叫 Groq API
try:
    print("🧠 正在產生完整資安週報...")
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "你是專業的資安新聞分析師，請協助撰寫週報。"},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
    )

    weekly_report = chat_completion.choices[0].message.content.strip()

    # ✅ 儲存輸出
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(weekly_report)

    print(f"✅ 資安週報已儲存至：{REPORT_FILE}")

except Exception as e:
    print(f"❌ 週報產生失敗：{e}")
