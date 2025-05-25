import requests
import os
import json


# 讀取環境變數
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
NEWS_LINKS_FILE = "../data/news_links_nonumber.json"  # JSON 檔來源改成你的 news_links.json

def send_discord_message():
    if not DISCORD_WEBHOOK_URL:
        print("❌ 錯誤: 未設定 DISCORD_WEBHOOK_URL 環境變數")
        return

    if not os.path.exists(NEWS_LINKS_FILE):
        print(f"❌ 錯誤: 檔案不存在: {NEWS_LINKS_FILE}")
        return

    # 讀取 JSON 內容（應該是一個 list of strings）
    with open(NEWS_LINKS_FILE, "r", encoding="utf-8") as f:
        news_links = json.load(f)

    if not news_links:
        print("⚠️ 提醒：news_links.json 沒有任何連結")
        return

    # 組合訊息
    message_lines = ["📢 **資安新聞週報連結** 📢\n"]
    for link in news_links:
        message_lines.append(f"- {link}")

    message_text = "\n".join(message_lines)

    # Discord 單則訊息限制 2000 字
    if len(message_text) > 2000:
        message_text = message_text[:1997] + "..."

    # 發送至 Discord Webhook
    payload = {
        "content": message_text
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

    if response.status_code == 204:
        print("✅ 訊息已成功發送至 Discord！")
    else:
        print(f"❌ Discord 發送失敗，錯誤碼: {response.status_code}, 錯誤訊息: {response.text}")

if __name__ == "__main__":
    send_discord_message()
