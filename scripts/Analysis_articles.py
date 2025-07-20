import json
import re
import requests
from datetime import datetime
import os

# === 設定 ===
ARTICLE_LIST_PATH = "../data/news_links.json"
TARGET_ID = 1
OUTPUT_PATH = "../data/structured_report.json"

# 讀取連結清單
with open(ARTICLE_LIST_PATH, "r", encoding="utf-8") as f:
    articles = json.load(f)

# 找出指定 ID 的文章連結
target_link = None
for article in articles:
    if article["id"] == TARGET_ID:
        target_link = article["link"]
        break

if not target_link:
    raise ValueError(f"找不到 id={TARGET_ID} 的文章連結")

# 下載 Markdown 或原始 HTML
response = requests.get(target_link)
if response.status_code != 200:
    raise Exception(f"無法取得文章內容，狀態碼 {response.status_code}")

md_content = response.text

# 可選：檢查是否是 Markdown 格式（這取決於你使用的 r.jina.ai 是否會轉換為 markdown）
# print(md_content[:500])  # 手動檢查一下格式

# 初始化整理資料結構
report = {
    "title": "",
    "source": target_link,
    "published_time": "",
    "sections": {}
}

# 擷取標題與時間（從 Markdown 中）
title_match = re.search(r"^Title:\s*(.*)", md_content, re.MULTILINE)
time_match = re.search(r"^Published Time:\s*(.*)", md_content, re.MULTILINE)

if title_match:
    report["title"] = title_match.group(1).strip()
if time_match:
    published_raw = time_match.group(1).strip()
    published_dt = datetime.strptime(published_raw, "%a, %d %b %Y %H:%M:%S %Z")
    report["published_time"] = published_dt.strftime("%Y-%m-%d %H:%M:%S")

# 擷取章節
section_pattern = r"^###\s+\*\*(.+?)\*\*"
sections = [(m.group(1), m.start()) for m in re.finditer(section_pattern, md_content, re.MULTILINE)]
sections.append(("EOF", len(md_content)))

# 處理章節內容
for i in range(len(sections) - 1):
    section_name = sections[i][0]

    # 跳過不要的章節
    if section_name.strip() == "近期資安日報":
        continue

    start = sections[i][1]
    end = sections[i+1][1]
    section_text = md_content[start:end]

    report["sections"][section_name] = []

    events = re.findall(r"\[\*\*(.*?)\*\*\]\((.*?)\)", section_text)
    for title, url in events:
        pattern = re.escape(f"[**{title}**]({url})") + r"\s*[\r\n]+(.*?)(?=\n\s*[\[\*]|$)"
        desc_match = re.search(pattern, section_text, re.DOTALL)
        description = desc_match.group(1).strip().replace("\n", " ") if desc_match else ""
        report["sections"][section_name].append({
            "title": title,
            "url": url,
            "description": description
        })

# 確保資料夾存在
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# 輸出結果
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"✅ 成功整理 id={TARGET_ID} 的文章，輸出到 {OUTPUT_PATH}")
