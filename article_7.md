Title: 【資安日報】7月24日，微軟支援身障者無障礙用途的UI自動化機制首遭惡意程式濫用

URL Source: https://www.ithome.com.tw/news/170243

Published Time: Thu, 24 Jul 2025 23:09:52 GMT

Markdown Content:
為了避免攻擊活動東窗事發，濫用合法、系統內建的公用程式，已是駭客經常會使用的策略，在今天的資安新聞裡，惡意軟體Coyote最值得留意，因為駭客運用協助身障人士的桌面應用程式自動化框架UI Automation（UIA），而相關手法，能廣泛對執行Windows XP以上電腦下手。

除此之外，濫用合法工具的情況，也發生在針對Magento、Docker的攻擊行動上，駭客以多種手法隱匿活動；駭客組織APT41、HazyBeacon濫用SharePoint主機、AWS Lambda的函數URL功能也值得留意。

### **【攻擊與威脅】**

[**首度發現UI Automation遭濫用！Coyote惡意軟體瞄準民眾金融帳密下手**](https://www.ithome.com.tw/news/170237)

[![Image 1](https://s4.itho.me/sites/default/files/images/active-exploitation-coyote-malware-first-ui-automation-abuse-in-the-wild-one.png)](https://s4.itho.me/sites/default/files/images/active-exploitation-coyote-malware-first-ui-automation-abuse-in-the-wild-one.png)

一般而言，駭客迴避端點電腦的防毒軟體和EDR系統，最常見的手法是濫用合法、存在已知弱點的驅動程式，從事自帶驅動程式（BYOVD）攻擊，癱瘓這些端點防護機制的運作，但近期駭客也發展出一些非典型的手法，例如：藉由特定廠牌EDR端點代理程式的本機安裝流程瑕疵，透過升級或降級作業來進行「自帶安裝程式（Bring Your Own Installer）」攻擊，現在又發展出新型態的手法，濫用作業系統內建的公用程式來達到目的。

最近資安業者Akamai揭露惡意軟體Coyote新一波攻擊行動，就是這樣的例子。此惡意軟體鎖定巴西使用者而來，目標涵蓋75家銀行及加密貨幣交易所的用戶，最特殊的地方在於，駭客濫用了微軟在Windows作業系統提供的桌面應用程式自動化框架UI Automation（UIA），而這是首度有惡意軟體攻擊運用這種公用程式的情形。

[**Docker、電商平臺Magento遭到鎖定，駭客運用多種隱密的手法挖礦、架設代理伺服器**](https://www.ithome.com.tw/news/170240)

[![Image 2](https://s4.itho.me/sites/default/files/images/mimo-graph.png)](https://s4.itho.me/sites/default/files/images/mimo-graph.png)

今年5月，以經濟利益為目標的駭客組織Mimo（或稱Mimo'lette）鎖定內容管理平臺Craft CMS而來，利用滿分已知漏洞CVE-2025-32432從事攻擊，於受害主機植入惡意程式載入工具Mimo Loader、挖礦軟體、代理伺服器軟體，濫用伺服器的算力及流量牟利，如今雲端安全及監控業者Datadog發現，這些駭客將攻擊目標延伸到組態不當的Docker，以及電商網站平臺Magento，而且，手法變得更加隱密。

Datadog指出，他們近日針對電商網站遭入侵的事故進行調查，這些攻擊涉及一系列工作負載（Workload）被駭，駭客利用未公布的PHP FastCGI Process Manager（PFP-FPM）資安漏洞來危害Magento，經過比對，確認攻擊者的身分是先前資安業者Sekoia揭露的Mimo。針對這樣的攻擊策略轉變，Datadog認為駭客不光只是鎖定不同目標，還有引入新的迴避偵測手法，以及在受害主機持續活動的機制，凸顯了該組織在戰術、手法、流程（TTP）出現重大變化。

[**中國駭客APT41鎖定非洲政府IT基礎設施而來，入侵SharePoint伺服器充當C2**](https://www.ithome.com.tw/news/170241)

[![Image 3](https://s4.itho.me/sites/default/files/images/apt41-in-africa2.png)](https://s4.itho.me/sites/default/files/images/apt41-in-africa2.png)

上週末SharePoint零時差漏洞CVE-2025-53770（ToolShell）攻擊引起全球關注，微軟確認有三組中國駭客Linen Typhoon、Violet Typhoon、Storm-2603從事相關活動，巧合的是，資安業者卡巴斯基也發現另一起與SharePoint有關的資安事故，攻擊者的身分是惡名昭彰的中國駭客APT41。

這起事故駭客針對非洲政府的IT服務而來，他們在惡意軟體裡嵌入內部服務名稱、IP位址、代理伺服器的資料，特別的是，其中一個C2伺服器，竟是濫用受害組織基礎設施裡的SharePoint主機。

附帶一提的是，APT41如果在初步偵察後認為受害電腦對後續活動具有重要價值，他們就會試圖建置Command Shell存取管道，藉由下載惡意的HTA檔案，執行嵌入的JavaScript指令碼，於受害電腦下載惡意程式，以及後續攻擊所需的其他工具。

[**HazyBeacon濫用AWS Lambda隱匿活動，意圖竊取東南亞政府關稅貿易資料**](https://www.ithome.com.tw/news/170119)

[![Image 4](https://s4.itho.me/sites/default/files/images/word-image-881439-146273-2.png)](https://s4.itho.me/sites/default/files/images/word-image-881439-146273-2.png)

有許多組織運用無伺服器（Serverless）的運算服務，部分駭客也盯上這類服務並用於攻擊行動，例如，2022年資安業者Cado Security揭露名為Denonia的惡意軟體，駭客就是針對名為AWS無伺服器服務Lambda下手，部署挖礦軟體牟利，如今又有濫用這項服務的資安事故傳出。

例如，由駭客組織CL-STA-1020發起的攻擊行動，就是這樣的例子。揭露此事的資安業者Palo Alto Networks指出，他們從2024年底追蹤這些駭客的活動，對方的攻擊目標是東南亞政府機關，目的是收集敏感資訊，特別是關於關稅與貿易爭端的資料。

在這波攻擊活動裡，駭客運用名為HazyBeacon的後門程式引起Palo Alto Networks的注意，因為該後門程式濫用AWS Lambda的函數URL功能建立C2通訊。此功能的主要用途，是讓使用者能直接透過HTTPS呼叫無伺服器運算的功能，一旦攻擊者濫用這種合法功能，就能建立具備可靠、可延伸的通道，但難以察覺相關惡意行為。

**其他攻擊與威脅**

◆**[美國核武機構傳出遭遇SharePoint零時差漏洞攻擊](https://www.bleepingcomputer.com/news/security/us-nuclear-weapons-agency-hacked-in-microsoft-sharepoint-attacks/)**

◆**[伊朗駭客假借提供VPN應用程式，意圖散布安卓惡意軟體DCHSpy](https://thehackernews.com/2025/07/iran-linked-dchspy-android-malware.html)**

◆**[約2千臺MCP伺服器缺乏存取控制，恐影響AI模型安全](https://www.darkreading.com/vulnerabilities-threats/2000-mcp-servers-security)**

◆**[網釣手法PoisonSeed可突破FIDO金鑰防護](https://www.darkreading.com/remote-workforce/poisonseed-attacker-fido-keys)**

### **【漏洞與修補】**

[**Sophos修補防火牆軟體RCE、指令注入漏洞**](https://www.ithome.com.tw/news/170236)

Sophos本周釋出軟體更新，修補存在防火牆產品Sophos Firewall可造成遠端程式碼執行及指令注入的 5項重大及高風險漏洞，分別是：重大層級的CVE-2025-6704、CVE-2025-7624，以及中高風險的CVE-2025-7382、CVE-2024-13974和CVE-2024-13973。

其中CVE-2025-6704為存在Secure PDF eXchange（SPX）功能的任意檔案寫入漏洞。如果防火牆以高可用性（High Availability，HA）模式執行，配合啟動SPX特定配置，就可能導致前驗證（Pre-auth）遠端程式碼執行，估計影響0.05%該廠牌防火牆裝置。

CVE-2025-7624為透通模式SMTP代理伺服器的SQL注入漏洞。如果Email的隔離政策啟動，且SFOS是由21.0 GA版本升級的話，可能導致遠端程式碼執行，影響0.73%裝置。

### **【資安產業動態】**

[**強化雲端組態安全，3大公有雲CIS Benchmark是資安專家推薦首選**](https://www.ithome.com.tw/news/170220)

近年臺灣企業上雲比例大幅增加，面對雲端安全管理方面的挑戰，特別是3大公有雲環境中，如何確保正確的組態設定，以及啟用關鍵的日誌記錄服務，一直是資安專家反覆強調的議題。

特別的是，企業可參考的雲端安全組態相關標準或最佳實務已有不少，CIS Benchmark是經常提及的資源之一，只是，過往少有單一針對此標準的內容探討，在今年2025臺灣雲端大會上，Google Cloud客戶解決方案架構師鄭家明進一步解析這部分內容，幫助大家掌握其重點。

CIS Benchmark是針對特定作業系統、應用程式與硬體設備而來，所制定相應的安全組態最佳實務指引，目前已推出數十種版本，涵蓋Microsoft IIS、MongoDB、NGINX、PostgreSQL等，亦包含AWS、Azure、GCP等主要雲端平臺。

**其他資安產業動態**

◆**[為保護用戶隱私，Brave加入封鎖Windows 11 Recall功能的行列](https://www.bleepingcomputer.com/news/security/brave-blocks-windows-recall-from-screenshotting-your-browsing-activity/)**

### **近期資安日報**

[**【7月23日】3組中國駭客使用SharePoint零時差漏洞從事攻擊**](https://www.ithome.com.tw/news/170231)

[**【7月22日】Dell傳出遭World Leaks勒索，測試環境資料外洩**](https://www.ithome.com.tw/news/170211)

[**【7月21日】SharePoint驚傳零時差漏洞攻擊，逾85臺伺服器受害**](https://www.ithome.com.tw/news/170174)
