Title: 【資安日報】8月4日，西亞電信業去年遭中國駭客組織長期網攻

URL Source: https://www.ithome.com.tw/news/170411

Published Time: Mon, 04 Aug 2025 23:09:45 GMT

Markdown Content:
中國駭客鎖定全球各地電信業者的網路間諜活動，自去年爆發Salt Typhoon攻擊美國電信業者的事故之後，後續有Liminal Panda攻擊南亞和非洲，近期資安業者Palo Alto Networks揭露名為CL-STA-0969的駭客組織攻擊行動，是針對西亞的電信業者而來，但這份調查報告具體交代更多細節，例如，提及駭客使用的迴避偵測手法相當嚴密，使得相關攻擊難以察覺。

除了鎖定電信業者的攻擊行動之外，鎖定SonicWall防火牆零時差漏洞的勒索軟體攻擊態勢，相當值得留意，原因是駭客鎖定的弱點與SSL VPN模組有關，而對於該廠牌SSL VPN系統的資安事故，7月已有數起消息傳出，因此用戶也要提高警覺，採取相關防護措施因應。

### 【攻擊與威脅】

[**西亞電信業去年遭中國駭客CL-STA-0969長期網攻，採用近10種專屬工具輪番滲透**](https://www.ithome.com.tw/news/170407)

[![Image 1](https://s4.itho.me/sites/default/files/images/word-image-1348-148315-1.png)](https://s4.itho.me/sites/default/files/images/word-image-1348-148315-1.png)

中國駭客組織鎖定電信業者從事大規模網路間諜活動，藉此針對特定的政治人物進行情報收集，這樣的事故又以去年9月爆發的Salt Typhoon駭客攻擊行動受到高度關注，不僅傳出AT&T、Verizon、Lumen等多家大型業者受害，相關攻擊亦得到美國政府的證實，後續更傳出這些駭客也對其他國家電信業者下手的情況；另有資安業者揭露專門攻擊南亞、非洲電信業者的駭客組織Liminal Panda，如今又有資安業者揭露相關事故的最新調查結果。

上週資安業者Palo Alto Networks發布調查報告指出，名為CL-STA-0969的駭客於去年2月至11月，鎖定西亞電信產業發動數起攻擊行動，他們部署多種工具與通訊機制，以便透過更為彈性的方法來遠端控制特定物件。其中一種作案工具是Cordscan，用途是收集行動裝置地理位置的資料，因此該公司推測，駭客有可能以此跟蹤受害者。

針對這些駭客的來歷，Palo Alto Networks推測是與Liminal Panda高度相關的國家級駭客，但也有部分工具來自其他組織，例如：LightBasin、UNC3886、UNC2891，以及UNC1945。

[**SonicWall防火牆零時差漏洞攻擊升溫，勒索軟體Akira加入戰局**](https://www.ithome.com.tw/news/170409)

7月中旬Google威脅情報團隊（GTIG）揭露鎖定SonicWall SSL VPN設備的攻擊行動，駭客企圖部署惡意軟體Overstep，後續駭客組織World Leaks聲稱駭入電腦大廠Dell內部的產品展示及測試的環境，傳出入侵的管道，很可能就是上述的SSL VPN設備。如今資安業者Arctic Wolf指出，勒索軟體Akira也加入攻擊該廠牌的SSL VPN系統的行列。

Arctic Wolf指出，7月下旬駭客透過SonicWall防火牆取得初始入侵管道的勒索軟體活動，出現增加的跡象，這些事故的共通點在於，所有的入侵都是透過防火牆的SSL VPN系統進行存取。根據他們掌握的證據，駭客疑似使用零時差漏洞而得逞，但不排除有暴力破解、字典攻擊、帳號填充攻擊的情況。。對此，他們認為在SonicWall尚未發布修補程式之前，最好暫時停用SSL VPN服務因應。

**其他攻擊與威脅**

◆**[WordPress佈景主題Alone存在重大漏洞，已被用於實際攻擊行動](https://securityaffairs.com/180630/hacking/attackers-actively-exploit-critical-zero-day-in-alone-wordpress-theme.html)**

◆**[巴基斯坦駭客APT36鎖定印度鐵路、石油、政府系統而來，利用惡意PDF檔案犯案](https://gbhackers.com/apt36-hackers-target-indian-railways-oil-and-government-systems/)**

◆**[微軟OAuth應用程式遭冒充，駭客意圖竊取多因素驗證資料](https://gbhackers.com/threat-actors-impersonate-microsoft-oauth-apps/)**

◆**[中國駭客Silver Fox聲稱提供Google翻譯工具，意圖散布惡意程式](https://gbhackers.com/silver-fox-hackers-exploit-weaponized-google-translate-tools/)**

◆**[Windows、安卓用戶遭到勒索軟體Anubis鎖定，駭客不僅加密檔案，也竊取帳密](https://gbhackers.com/anubis-ransomware-targets-android-and-windows-users/)**

### 【漏洞與修補】

[**蘋果發布多個作業系統平臺更新，修補已遭利用的Chrome零時差漏洞**](https://www.ithome.com.tw/news/170408)

兩週前Google發布Chrome 138電腦版更新138.0.7204.157、138.0.7204.158，修補6項資安漏洞，其中存在於ANGLE（Almost Native Graphics Layer Engine）及GPU元件的高風險漏洞CVE-2025-6558，已經出現實際遭到利用的跡象，但這項漏洞並非只影響Chromium為基礎打造的瀏覽器，後續有其他科技業者跟進，修補這項資安漏洞。

蘋果於7月29、30日，針對旗下的行動裝置、電腦、穿戴裝置、電視盒，發布iOS 18.6、iPadOS 18.6與17.7.9、macOS Sequoia 15.6、watchOS 11.6、visionOS 2.6、tvOS 18.6，並為macOS Ventura與Sonoma用戶發布瀏覽器更新Safari 18.6，其中一項修補的資安漏洞，就是存在於Safari排版引擎WebKit的CVE-2025-6558，並指出一旦瀏覽器處理特製的惡意網頁內容，就有機會導致無預期當機的現象。蘋果提及此漏洞出現在他們採用的開放原始碼內容，由Google威脅分析團隊（TAG）通報。

### 【資安產業動態】

[**美國CISA開源Thorium惡意程式分析平臺**](https://www.ithome.com.tw/news/170400)

美國網路安全暨基礎架構管理署（CISA）宣布，開源自動化檔案分析平臺Thorium，將開放給政府機關及民間用於惡意程式和鑑識分析。

這項計畫是CISA和美國桑迪亞國家實驗室（Sandia National Laboratories）合作。Thorium為自動化檔案分析及資料生成的高擴充性分散式平臺，它允許分析團隊操作及整合任意商業、開源及自訂工具，自動化執行分析工作流程，支援軟體分析、數位鑑識和事件回應。

Thorium的整合性平臺上，允許分析人員上傳程式檔案，以Docker映像檔及VM形式整合指令行工具、利用標籤和全文搜尋篩選結果，並嚴格以群組為基礎的核准規則來管理存取。

[**IBM宣稱新一代Power11伺服器可在1分鐘內偵測勒索軟體**](https://www.ithome.com.tw/news/169959)

IBM發表其新一代的Power11伺服器，宣稱其正常運作時間達99.9999%，強調零停機維運能力，且搭配IBM Power Cyber Vault資安解決方案，能在1分鐘以內偵測到勒索軟體。IBM 預計於7月25日同步推出Power 11的入門、中階、高階及虛擬伺服器。

上一次IBM更新其Power伺服器是在2020年推出的Power 10，新登場的Power 11效能提升了10~20%，入門與中階系統擁有更多的核心數量，運算規模最高提升45%，並將成為首款支援 IBM Spyre Accelerator的IBM Power伺服器。

IBM Spyre Accelerator為該公司所開發的AI推論專用晶片，專為企業於混合雲環境中部署AI密集應用而設計，預計於今年第四季上市。

### **近期資安日報**

[**【8月1日】俄羅斯駭客針對當地外交單位從事網路間諜活動**](https://www.ithome.com.tw/news/170359)

[**【7月31日】駭客挾持ATM出奇招，於隔離網路部署實體後門**](https://www.ithome.com.tw/news/170345)

[**【7月30日】美國明尼蘇達州首府遭到網攻，進入緊急狀態、動員國民兵因應**](https://www.ithome.com.tw/news/170328)
