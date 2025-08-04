Title: 【資安日報】7月25日，SharePoint零時差漏洞災情浮現，恐成為全球危機

URL Source: https://www.ithome.com.tw/news/170267

Published Time: Fri, 25 Jul 2025 23:09:39 GMT

Markdown Content:
本週最重大的資安事故，莫過於SharePoint零時差漏洞CVE-2025-53770（ToolShell）攻擊，這兩天陸續有新的消息傳出，其中一個是中國駭客Storm-2603用於入侵受害組織，並部署勒索軟體Warlock而產生破壞；另一個消息，則是美國能源部旗下的核安管理署（NNSA）傳出受害，這樣的情況很可能引發核能安全危機。

另一個值得留意事故的是，在上週奢華品牌Louis Vuitton（LV）全球多家分公司接連傳出遭到入侵，並出現客戶資料外流的現象後，同樣隸屬LVMH集團的迪奧（Christian Dior Couture），本週開始向受影響的客戶通知資料外洩事故，並向美國3個州檢察長通報。

### **【攻擊與威脅】**

[**中國駭客Storm-2603從事SharePoint零時差漏洞攻擊，意圖散布勒索軟體Warlock**](https://www.ithome.com.tw/news/170266)

[![Image 1](https://s4.itho.me/sites/default/files/images/Storm-2603.png)](https://s4.itho.me/sites/default/files/images/Storm-2603.png)

上週末爆發的SharePoint零時差漏洞攻擊事故，攻擊者利用被稱為ToolShell的資安漏洞CVE-2025-53770發動攻擊，時間最早可追溯到7月7日，微軟22日指出他們確認有3組中國駭客從事漏洞利用活動，這些組織分別是：Linen Typhoon、Violet Typhoon，以及Storm-2603，但當時僅有說明這些駭客如何利用ToolShell，以及他們偏好攻擊的目標，並未對相關攻擊事故透露有關細節，隔天表示在他們的積極追蹤下，確認Storm-2603用於從事Warlock勒索軟體攻擊活動。

這些駭客會尋找可透過網際網路存取的SharePoint伺服器，並透過spinstall0.aspx有效酬載（Web Shell）建立初期的存取管道，進而運用w3wp.exe處理程序執行命令。微軟看到駭客下達了一系列的命令，包含whoami來進行偵察，並找出所有使用者並確認權限層級。接著，他們運用CMD和批次指令碼，以及公用程式PsExec進行更廣泛的活動。為了能讓攻擊不受阻礙，駭客濫用services.exe竄改機碼，從而停用內建防毒Microsoft Defender。

[**美國核武機構NNSA傳出遭遇SharePoint漏洞攻擊**](https://www.ithome.com.tw/news/170248)

7月中SharePoint零時差漏洞CVE-2025-53770（ToolShell）遭駭事件受害層面逐漸擴大，如今傳出有受害組織的身分曝光美國核安管理署（National Nuclear Security Administration，NNSA）在內的美國政府機構。

荷蘭資安業者Eye Security上周末首先公開數十家機構SharePoint伺服器發生濫用漏洞事件，後來其中較重大的漏洞被命名為CVE-2025-53770，而其濫用漏洞的手法則稱為ToolShell。多家資安業者估計，初期受害者涵括美國政府機構。

美國能源部向彭博社證實，能源部下他們旗下的國家核安管理署（NNSA）網路上周遭駭客存取。事件發生在7月18日。能源部發言人說，由於Microsoft 365及其網路安全系統的普及，能源部難免受影響。但他強調，NNSA只有極少數系統受影響，而且所有受影響的系統都已恢復營運。

[**時尚美妝品牌Dior向客戶通知年初資料外洩事件**](https://www.ithome.com.tw/news/170260)

LVMH集團旗下迪奧（Christian Dior Couture）本周向客戶寄發通知信件，告知他們受到半年前的客戶資料外洩事件影響，其中包含加州、德州及華盛頓州消費者。

Dior起初在5月透過網站公告這起事件，但直到7月18日才向受影響的客戶發送個別通知信件。這起事件實際發生於今年1月，Dior 5月7日證實遭未經授權的第三方人士存取特定資料庫，竊走儲存的客戶資料。這次事件外洩的客戶個資包含住家地址、出生日期、社會安全號碼、電子郵件信箱，部份客戶更有護照或身份證件資料被存取。

共有多少分公司受害目前不得而知，但有加州、德州及華盛頓州州檢察長公告Dior於1月的資安事件。共有9716名德州及10878名華盛頓州民受影響，加州居民受影響人數不詳。

[**熱門NPM套件遭到挾持，駭客上架新套件散布惡意程式，起因是維護者遭網釣導致Token外流**](https://www.ithome.com.tw/news/170262)

[![Image 2](https://s4.itho.me/sites/default/files/images/468168199-591bdf7b-7767-45ca-8532-35a2579b8e58.png)](https://s4.itho.me/sites/default/files/images/468168199-591bdf7b-7767-45ca-8532-35a2579b8e58.png)

鎖定開發人員的惡意NPM套件攻擊經常發生，其中大部分駭客都是透過假冒知名冒件的方式，使用極為相似的名稱騙過開發人員，導致他們不慎下載惡意軟體，但最近一波攻擊行動引起軟體開發圈的關注，原因是駭客先針對套件維護者下手，取得他們的NPM帳號來發布新版套件。

根據資安新聞網站Bleeping Computer的報導，每週被下載超過3千萬次的熱門套件eslint-config-prettier，在上週末遭遇供應鏈攻擊，套件維護人員JounQin遭受網釣攻擊，導致他的NPM帳號Token外流，攻擊者得逞後，以他的名義在NPM套件庫上架有問題的套件。

這起事故發現的過程，起因是7月18日有開發人員安裝特定版本的eslint-config-prettier之後，電腦出現不尋常的行為，這些新版套件存在怪異的共通點，那就是維護者雖然在NPM儲存庫上架，卻並未在GitHub專案更新對應的內容，這種情況隨即引起開源軟體社群的注意。

[**Ivanti SSL VPN系統零時差漏洞遭到利用，駭客用來散布MDifyLoader、Cobalt Strike**](https://www.ithome.com.tw/news/170149)

[![Image 3](https://s4.itho.me/sites/default/files/images/ivanti_cs01-800wri.png)](https://s4.itho.me/sites/default/files/images/ivanti_cs01-800wri.png)

今年1月、4月資安業者Ivanti修補旗下SSL VPN系統Ivanti Connect Secure（ICS）重大層級資安漏洞CVE-2025-0282、CVE-2025-22457（CVSS風險皆為9.0），臺灣資安業者杜浦數位安全（TeamT5）今年3月偵測到中國APT駭客用來發動大規模攻擊，在臺灣、日本、韓國等12個國家造成災情，駭客攻擊的範圍涵蓋近20個不同的產業，並提及駭客可能仍持續控制受害組織的環境，最近有資安組織公布新的調查結果，指出利用這兩個漏洞相關的攻擊行動，在去年就已出現。

日本電腦緊急應變小組（JPCERT/CC）指出，他們針對今年2月、4月公布的惡意軟體SpawnChimera、DslogdRAT著手進行深度調查，結果找到更多專門針對ICS零時差漏洞而來的惡意程式及作案工具，駭客從去年12月開始，利用CVE-2025-0282與CVE-2025-22457從事攻擊，散布惡意程式MDifyLoader、Cobalt Strike、Vshell、Fscan，值得留意的是，相關活動迄今仍在持續進行。

[**新加坡關鍵基礎設施遭中國駭客UNC3886鎖定，或透過路由器與資安設備滲透**](https://www.ithome.com.tw/news/170195)

新加坡網路安全局（CSA）發布聲明指出，近期在新加坡部分關鍵基礎設施偵測到的網路攻擊活動，其背後可能與中國背景的進階持續性威脅（APT）組織UNC3886有關。CSA表示，目前正持續追蹤並調查此一攻擊事件，並強調已啟動跨單位合作與威脅情報共享機制，以協助受影響的機構進行相關防禦措施，但基於調查考量，暫不會公開攻擊行動的技術細節。

CSA此次聲明僅簡短指出，UNC3886的攻擊手法具備長期潛伏、高針對性，以及難以短時間內根除的特性，因此未來相關應對與調查工作將持續一段時間。UNC3886此前被資安公司Mandiant以及部分業界報告認為與中國有高度關聯，該組織曾多次透過入侵VPN、路由器、邊界防火牆等重要網路設備，以取得持續性的內部網路通道，並監控特定國家的政府機構或基礎設施營運商。

**其他攻擊與威脅**

◆**[駭客組織Fire Ant鎖定VMware虛擬化平臺而來，部署後門程式](https://thehackernews.com/2025/07/fire-ant-exploits-vmware-flaw-to.html)**

◆**[中國駭客聲稱提供達賴喇嘛應用程式，對圖博從事間諜活動](https://thehackernews.com/2025/07/china-based-apts-deploy-fake-dalai-lama.html)**

◆**[駭客組織EncryptHub假借提供搶先體驗的遊戲，意圖散布惡意軟體](https://www.bleepingcomputer.com/news/security/hacker-sneaks-infostealer-malware-into-early-access-steam-game/)**

**其他漏洞與修補**

◆**[SonicWall SMA 100系列設備存在任意檔案上傳漏洞](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-critical-rce-flaw-in-sma-100-VPN-appliances/)**

◆**[Mitel整合式通訊系統MX-ONE存在重大漏洞，恐被用於繞過身分驗證](https://www.bleepingcomputer.com/news/security/mitel-warns-of-critical-mivoice-mx-one-authentication-bypass-flaw/)**

### **近期資安日報**

[**【7月24日】微軟支援身障者無障礙用途的UI自動化機制首遭惡意程式濫用**](https://www.ithome.com.tw/news/170243)

[**【7月23日】3組中國駭客使用SharePoint零時差漏洞從事攻擊**](https://www.ithome.com.tw/news/170231)

[**【7月22日】Dell傳出遭World Leaks勒索，測試環境資料外洩**](https://www.ithome.com.tw/news/170211)
