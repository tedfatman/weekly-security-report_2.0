import os
from groq import Groq

MERGED_FILE = "../data/threat.md"
REPORT_FILE = "../data/threat_report.md"

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
你是一位資安新聞彙整助手，以下是我彙整出來的一週「資安威脅態勢」原始內容。內容包含大量 CVE 漏洞、攻擊手法與行動代號，結構雜亂、資訊重複，請你協助進行完整的統整與優化。

請你依照以下規則進行整理：

1. 使用繁體中文。
2. 每一行條列開頭請使用 `* `（星號+空格），不要使用數字或破折號。
3. 針對相同系統、相同攻擊手法的 CVE，請合併整理為同一條或群組。
4. 每一條內容需包含漏洞編號（若有）、影響平台、攻擊技術（如：RCE、XSS、提權等），並註明是否**已遭利用**或有**攻擊行動**。
5. 針對明確的攻擊行動（如 Mirai、Interlock、LZRD、APT 組織）請另列條目，指出其目標與手法。
6. 資訊要簡潔、完整、無重複，適合放入正式資安週報的「威脅態勢」段落中。

---

以下是原始「資安威脅態勢」段落（請保留 `### 2. 資安威脅態勢` 開頭）：

### 2. 資安威脅態勢
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
