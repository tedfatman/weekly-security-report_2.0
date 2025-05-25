import os
from groq import Groq

MERGED_FILE = "../data/conclude.md"
REPORT_FILE = "../data/conclude_report.md"

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
你是一位資安顧問與威脅分析師，請你針對以下一週的資安週報內容，撰寫一篇具深度的「分析回饋報告」。

請遵守以下要求：

1. 使用繁體中文，語氣專業、理性、中立。
2. 不要重複週報原文內容，而是從資安實務角度出發，進行觀察、評估與風險提醒。
3. 請針對以下 4 個面向，逐項評論：
   - 威脅趨勢與攻擊模式（如駭客技術、APT 活動、漏洞濫用）
   - 防護現況與修補能力（如修補速度、通報機制、組織因應能力）
   - 組織應採行的行動建議（如政策調整、技術部署、教育訓練）
   - 產業與政策趨勢（如政府措施、國際法規、產業鏈變動）

4. 可用分段標題（如一、二、三…）清楚呈現各面向評論。

請針對以下資安週報內容進行分析回饋
{merged_content}
"""

# ✅ 呼叫 Groq API
try:
    print("🧠 正在產生完整資安週報...")
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "你是專業的資安顧問與威脅分析師，請協助撰寫分析回饋報告。"},
            {"role": "user", "content": prompt}
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
    )

    weekly_report = chat_completion.choices[0].message.content.strip()

    # ✅ 儲存輸出
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(weekly_report)

    print(f"✅ 資安週報已儲存至：{REPORT_FILE}")

except Exception as e:
    print(f"❌ 週報產生失敗：{e}")
