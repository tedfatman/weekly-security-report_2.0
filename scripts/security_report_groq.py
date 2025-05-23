import os
from groq import Groq

MERGED_FILE = "../data/security.md"
REPORT_FILE = "../data/security_report.md"

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
你是一位專業的資安新聞摘要助手，現在我提供給你一段來自「資安防護」分類的原始彙整內容。

這段內容已經整理為條列形式，但存在資訊重複、順序未整理、重要性不明等問題。

請你針對這段內容進行「進一步的彙整與優化」，使其更適合出現在正式的資安週報中。請務必遵守以下規範：

1. 使用繁體中文。
2. 僅保留具體有效的防護措施、更新行動、漏洞修補或政策公告。
3. 將相同廠商、相似類型的行動合併為一條或統整為同一區塊。
4. 每一項請使用 `* ` 作為條列起始符號，請勿使用數字、破折號。
5. 整理完的結果應簡潔、去除重複、語句一致、便於閱讀。

---

以下是原始「資安防護」內容（請僅整理其內容，無需修改標題）：

### 1. 資安防護
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
