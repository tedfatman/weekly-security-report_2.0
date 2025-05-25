import os

ARTICLE_DIR = "../data"
OUTPUT_PATH = "../data/conclude.md"

# 每個分類對應的檔案名稱
file_map = {
    "資安防護": "security_report.md",
    "資安威脅態勢": "threat_report.md",
    "資安事件": "incident_report.md",
    "未來趨勢": "future_report.md"
}

# 儲存各分類內容
sections = {section: "" for section in file_map.keys()}

# 讀取每個分類的來源檔案
for section_name, filename in file_map.items():
    path = os.path.join(ARTICLE_DIR, filename)
    if not os.path.exists(path):
        print(f"⚠️ 找不到檔案：{path}，跳過")
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        sections[section_name] = content

# 合併並儲存
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    for i, (section_name, content) in enumerate(sections.items(), start=1):
        f.write(content + "\n\n")

print(f"✅ 已完成彙整，儲存至：{OUTPUT_PATH}")
