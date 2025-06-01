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
你是一位資深資安顧問與威脅分析師，請你針對以下一週的資安週報內容，撰寫一篇專為資安主管閱讀的《資安分析回饋報告》，協助其掌握最新威脅趨勢與必要應對行動。

請遵守以下撰寫要求：

報告風格與語氣
語言：使用繁體中文。
語氣：專業、簡明、策略導向，避免冗長細節，強調「關鍵訊息」與「風險提醒」。
結構：分段標題請使用「一、二、三…」呈現。

內容架構（請依下列四個面向撰寫）
一、威脅趨勢與攻擊模式
簡明指出本週重大攻擊技術、漏洞濫用或APT行動。
闡述其潛在影響（如：供應鏈、身分系統、零日利用等）。

二、防護現況與修補能力
評估廠商與業界的修補速度與漏洞回應情況。
指出企業常見的資安落差或因應不足處。

三、組織應採行的行動建議
提出 3~5 項具體、優先等級高的行動建議(例如:導入MFA、強化漏洞管理、資安稽核等)。
可依企業實際狀況分類為「立即」、「中期」或「建議規劃」。

四、產業與政策趨勢
整理近期政府/產業資安法規、政策重點。
評估其對企業的合規義務、策略調整、資安預算配置的潛在影響。

決策導向加值要求
加入「高階摘要(Executive Summary)」一段落(放在最前面)，用簡短條列方式說明:
本週關鍵威脅(2-3 項)
建議立即採行的行動(最多3項)
整體風險評估（高 / 中 / 低）-請闡述評估該風險的理由

請根據下方提供的資安週報內容進行撰寫。
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
