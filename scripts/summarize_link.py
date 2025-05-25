import os
import json

NEWS_LINKS_FILE = "../data/news_links_nonumber.json"
EXTRA_JSON_FOLDER = "../data"

# 允許的檔案結尾
ALLOWED_SUFFIXES = ["_NICS.json", "_TWCERT.json", "_TheHackersNews.json"]

def load_existing_links():
    if not os.path.exists(NEWS_LINKS_FILE):
        return []
    with open(NEWS_LINKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_links(links):
    with open(NEWS_LINKS_FILE, "w", encoding="utf-8") as f:
        json.dump(links, f, ensure_ascii=False, indent=4)

def extract_links_from_json_files(folder_path):
    links = []
    for filename in os.listdir(folder_path):
        if any(filename.endswith(suffix) for suffix in ALLOWED_SUFFIXES):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    link = data.get("link")
                    if link:
                        links.append(link)
                        print(f"✅ 讀取連結: {link}")
            except Exception as e:
                print(f"⚠️ 無法讀取 {filename}: {e}")
    return links

def merge_links():
    existing_links = load_existing_links()
    new_links = extract_links_from_json_files(EXTRA_JSON_FOLDER)

    # 合併並移除重複
    merged_links = list(dict.fromkeys(existing_links + new_links))
    
    save_links(merged_links)
    print(f"✅ 已更新 news_links.json，共 {len(merged_links)} 筆連結")

if __name__ == "__main__":
    merge_links()
