Title: 【資安日報】8月1日，俄羅斯駭客針對當地外交單位從事網路間諜活動

URL Source: https://www.ithome.com.tw/news/170359

Published Time: Fri, 01 Aug 2025 23:09:36 GMT

Markdown Content:
為了掌握其他國家的情報，國家級駭客從事網路間諜活動的情況，在國際局勢不斷升溫之際，一直有相關資安事故傳出，但最近微軟揭露的攻擊行動相當特別，俄羅斯駭客針對各國駐俄外交單位下手，而且，他們動用了ISP與電信業者的環境來接觸攻擊目標。

近期遭受執法壓力的勒索軟體BlackSuit也是本週受到關注的焦點，原因是思科發現，這些駭客早就做好準備，即使執法單位破壞他們的暗網網站，這些駭客疑似幾個月前就已另外成立新組織Chaos，並在駭客論壇尋找新的加盟主進行合作。

### 【攻擊與威脅】

[**俄羅斯駭客Secret Blizzard鎖定大使館而來，濫用ISP發動AiTM網釣**](https://www.ithome.com.tw/news/170355)

[![Image 1](https://s4.itho.me/sites/default/files/images/Figure-1_-Secret-Blizzard-AiTM-i.png)](https://s4.itho.me/sites/default/files/images/Figure-1_-Secret-Blizzard-AiTM-i.png)

自俄羅斯入侵烏克蘭之後，俄羅斯國家級駭客就不斷對協助烏克蘭的國家發動網路攻擊，如今他們為了收集其他國家的情報，竟然打算對各國駐俄大使館及外交單位，從事網路間諜活動，而且，還動用到網際網路服務供應商（ISP）的層級來犯案。

微軟揭露俄羅斯駭客自2024年開始的一系列網路間諜活動，發起這些攻擊的團體被稱為Secret Blizzard、Turla、Waterbug、Venomous Bear，他們利用對手中間人（AiTM）手法，攻擊位於莫斯科的大使館、外交單位，以及其他敏感的組織，散布名為ApolloShadow的惡意程式。這些被駭客鎖定的目標存在共通點，就是他們相當仰賴當地的網際網路服務供應商。微軟強調，這是他們首度看到Secret Blizzard將攻擊行動提升到ISP層級的情況，代表使用當地ISP或是電信服務的外交人員，都有可能是這些駭客下手的目標。

這起事故被發現的時間在今年2月，當時微軟觀察到該組織針對位於莫斯科的大使館從事網路間諜活動，而最引起研究人員注意的部分，在於駭客假借卡巴斯基防毒軟體的名義，在受害電腦安裝根憑證，因為這麼做駭客有機會突破TLS及SSL加密防護機制，以明文的方式存取受害者的上網內容，甚至能進一步取得他們的Token或是帳密資料。

[**勒索軟體BlackSuit成員傳出另起爐灶，打造Chaos並提供租用服務**](https://www.ithome.com.tw/news/170323)

[![Image 2](https://s4.itho.me/sites/default/files/images/data-src-image-bc13f8bb-852d-4a0d-84c0-4f9d26c215d2.jpeg)](https://s4.itho.me/sites/default/files/images/data-src-image-bc13f8bb-852d-4a0d-84c0-4f9d26c215d2.jpeg)

駭客組織遭受執法單位的壓力，在即將遭到圍剿的前夕另起爐灶，這樣的情況不時傳出，例如，7月宣布關閉業務的勒索軟體駭客組織Hunter International，今年初傳出已使用World Leaks的名號成立新的團隊，如今有另一個興起的勒索軟體Chaos，很可能就是近期執法單位出手的勒索軟體BlackSuit（Royal）前成員組成。

思科旗下的威脅情報團隊Talos近期揭露Chaos的攻擊手法，這些駭客通常運用洪水式垃圾郵件攻擊手法接觸受害者，藉著語音網釣得到受害組織的初期存取管道，並濫用遠端管理工具（RMM）持續連線，以及透過檔案共享軟體外傳竊得資料，這些駭客聲稱，他們大部分的受害組織位於美國，但英國、紐西蘭、印度也有企業組織受害。

針對攻擊者的身分，Talos指出，這個駭客組織與先前使用相同名稱的殭屍網路沒有直接關聯，他們根據勒索軟體加密機制、勒索訊息的結構、駭客使用的工具集，推測Chaos可能是BlackSuit前成員組成的新團體。

[**開源木馬程式AsyncRAT衍生逾30款分支惡意軟體**](https://www.ithome.com.tw/news/170093)

[![Image 3](https://s4.itho.me/sites/default/files/images/AsyncRAT-figure-8.png)](https://s4.itho.me/sites/default/files/images/AsyncRAT-figure-8.png)

許多自由軟體採用開放原始碼的方式，賦與使用者高度自由，不僅能夠使用，甚至能進一步修改、複製，以及散布，從而促使有能力開發的使用者加入改良的行列，而能夠帶來創新、降低成本、提升軟體的品質，然而這種開源的做法若是用於惡意軟體，就有可能加速這類工具的散布，導致造成的威脅變得更加廣泛。

例如，最近資安業者ESET公布對於惡意軟體AsyncRAT的身世調查，就是典型的例子。AsyncRAT是非同步遠端存取木馬程式的縮寫，以C#開發而成，於2019年在GitHub儲存庫發表，如今至少衍生出超過30款惡意程式，其中最廣泛受到利用的變種是DCRat和VenomRAT。

ESET特別提及，惡意程式數量居次的DCRat，其開發團隊對於AsyncRAT改良多項功能，其中一項是用於傳輸的資料結構，他們導入了另一個開源程式庫MessagePack，使得二進位資料序列化處理更有效率。

**其他攻擊與威脅**

◆**[美國警告Scattered Spider攻擊升溫，鎖定外包IT服務供應商而來](https://www.cisa.gov/news-events/alerts/2025/07/29/cisa-and-partners-release-updated-advisory-scattered-spider-group)**

◆**[與駭客組織Silk Typhoon有關的中國公司為網路間諜工具申請專利](https://thehackernews.com/2025/07/chinese-firms-linked-to-silk-typhoon.html)**

◆**[惡意軟體Jsceal冒充加密貨幣交易工具，透過臉書廣告散布](https://thehackernews.com/2025/07/hackers-use-facebook-ads-to-spread.html)**

### 【資料外洩及隱私保護】

[**ChatGPT分享連結功能可讓Google搜尋到用戶對話，OpenAI緊急關閉**](https://www.ithome.com.tw/news/170351)

一般而言，Google能搜尋到X或臉書平臺上張貼的內容，但如今Google竟然也可以搜尋到某些人和ChatGPT的私人對話，原因出在用戶使用了分享連結（share link）實驗性功能。

分享連結功能是ChatGPT的功能之一。分享連結允許用戶將他和這個聊天機器人的對話以連結形式分享給他人。擁有這個連結的人就能讀取這些對話內容。雖然OpenAI提醒使用者不要將隱私資訊輸入ChatGPT，但總是會有用戶忽略這項警告。如果用戶使用分享連結功能產生URL，並將URL張貼在社群網站或其他公開平臺上，就可能被Google或其他搜尋引擎索引，變成可被公開搜尋的內容。

近日Reddit用戶發現，只要在Google搜尋上限定搜尋「site:chatgpt/share」網站，再加上想要的關鍵詞，即可搜尋到其他用戶的ChatGPT對話內容。用戶運用這方法找到7萬多則內容，一旦這些內容被索引，用戶本人即使刪除自己的帳號，也無法收回已公開的資訊內容。消息曝光後，OpenAI已經將分享連結功能移除。

[**徵信社從駭客網站取得臺灣民眾個資，並轉賣給他人牟利**](https://www.ithome.com.tw/news/170357)

[![Image 4](https://s4.itho.me/sites/default/files/images/20250718-.jpg)](https://s4.itho.me/sites/default/files/images/20250718-.jpg)

2022年10月傳出有人在駭客論壇BreachForums兜售我國的戶政資料，引發軒然大波，後來一名電腦工程師因好奇買來比對遭到檢察管起訴，事隔兩年，有人透過創世紀市集（Genesis Market）取得國人個資，且其中資料範圍相當廣，涵蓋身分證字號、手機號碼、社群網站存取權限，以及電商網站蝦皮、露天的帳密資料，但嫌犯取得這些個資的目的尚不得而知，如今有徵信社購買這類資料用於相關業務，甚至進一步在網站上兜售牟利。

7月18日內政部警政署刑事警察局宣布，他們破獲徵信社販售個資的案件，曾擔任徵信社分公司的陳姓負責人透過公司雇用的工程師，於駭客網站買到9,300萬筆民眾個資，提供員工使用，並涉嫌在公司網站兜售。刑事局逮捕10人並移送檢方偵訊。

針對這起事故的調查緣由，刑事局表示他們接獲情資，有不法集團將非法取得的民眾個資存放於特定的私人網站主機，經過專案小組調查後發現，此資料庫為臺中知名徵信社所有，為廖姓網站工程師透過非法管道購買，以約新臺幣15萬元的加密貨幣的代價，購得逾9,300萬筆個資。該工程師架設網站並建置系統，只要有徵信社員工有業務需求，就能透過該系統調閱民眾個資進行徵信。此外，該名工程師也在網站上標售這批資料。

**其他漏洞與修補**

◆**[針對今年3月修補的macOS資安漏洞Sploitlight，通報此事的微軟公布細節](https://www.bleepingcomputer.com/news/security/microsoft-macos-sploitlight-flaw-leaks-apple-intelligence-data/)**

**其他資安產業動態**

◆**[CISA開源惡意軟體鑑識平臺Thorium](https://www.bleepingcomputer.com/news/security/cisa-open-sources-thorium-platform-for-malware-forensic-analysis/)**

### **近期資安日報**

[**【7月31日】駭客挾持ATM出奇招，於隔離網路部署實體後門**](https://www.ithome.com.tw/news/170345)

[**【7月30日】美國明尼蘇達州首府遭到網攻，進入緊急狀態、動員國民兵因應**](https://www.ithome.com.tw/news/170328)

[**【7月29日】Scattered Spider鎖定VMware虛擬化平臺而來，並使用勒索軟體加密檔案**](https://www.ithome.com.tw/news/170302)
