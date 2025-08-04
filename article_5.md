Title: 【資安日報】7月29日，Scattered Spider鎖定VMware虛擬化平臺而來，並使用勒索軟體加密檔案

URL Source: https://www.ithome.com.tw/news/170302

Published Time: Tue, 29 Jul 2025 23:09:43 GMT

Markdown Content:
惡意昭彰的駭客組織Scattered Spider（0ktapus、UNC3944、Octo Tempest），從今年4月攻擊多家英國零售業者引起關注，後續該組織又將範圍延伸到美國，究竟這些駭客如何得逞？這段期間曾多次提出警告的Google，近日公布調查結果。

另一方面，與中國有關的駭客組織Sliver Fox，也有研究人員公布長期追蹤的結果，指出這些駭客在2年裡設置逾2,800個網域名稱，用來散布多種惡意程式，其中仍有近十分之一的網域迄今仍被用於攻擊行動。

### **【攻擊與威脅】**

[**Scattered Spider鎖定VMware vSphere而來，部署勒索軟體並竊取資料**](https://www.ithome.com.tw/news/170293)

[![Image 1](https://s4.itho.me/sites/default/files/images/ransomware-attack-chain_max-2200x2200.png)](https://s4.itho.me/sites/default/files/images/ransomware-attack-chain_max-2200x2200.png)

今年4月開始，被稱為Scattered Spider、0ktapus、UNC3944、Octo Tempest的駭客組織，傳出針對英國零售業者瑪莎百貨（Marks & Spencer，M&S）、連鎖超市Co-op、精品百貨公司哈洛德（Harrods）發動網路攻擊，這些駭客成為勒索軟體DragonForce的加盟主，利用這款惡意程式犯案，後續Google警告這些駭客轉移目標，針對美國零售業、航空與交通運輸業而來，最近他們公布詳細的調查結果，揭露這些駭客的攻擊手法。

Google旗下的威脅情報團隊（GITG）指出，Scattered Spider向來不使用軟體弱點做為入侵受害組織的管道，而是針對IT服務臺（Help Desk）撥打電話，依照經過驗證的劇本進行網釣攻擊，從而繞過常見的資安防護機制，並採取寄生攻擊（LoL）的策略從事後續活動。

一旦這些駭客在成功完成社交工程攻擊並取得有效使用者帳號，就會以此操縱受信任的管理系統，並透過控制AD來轉進VMware vSphere環境，建立從虛擬機器管理工具竊取機敏資料並部署勒索軟體的管道。GITG指出，這樣的做法完全不會產生入侵指標（IoC），並能繞過EDR等資安工具的偵測。

[**駭客組織Silver Fox針對中文用戶散布Windows惡意程式**](https://www.ithome.com.tw/news/170281)

專門蒐集網域情報的美國資安業者DomainTools最近揭露了駭客組織Silver Fox的惡意行為，指出位於中國時區的Silver Fox自2023年6月以來，便建立了超過2,800個用來散布Windows惡意程式的網域名稱，且直至今年6月，仍有266個網域積極參與惡意行動。

Silver Fox在註冊眾多的網站之後，將它們偽裝成程式下載頁面、更新提示、登入頁面、行銷及商業工具平臺，或是加密貨幣應用等，以誘導使用者下載惡意程式或輸入敏感資訊。包括Gmail、支付寶（Alipay）與Coinbase都是駭客假冒的對象。

駭客所使用的惡意程式家族涵蓋了遠端存取木馬Gh0stRAT、用來控制被駭裝置的ValleyRAT、商業化的遠端監控程式Remcos RAT、資訊竊取工具Lumma Stealer，以及可大量蒐集電腦帳密的RedLine Stealer等。

**其他攻擊與威脅**

◆**[勒索軟體BlackSuit成員傳出另起爐灶，打造Chaos並提供租用服務](https://www.darkreading.com/cyberattacks-data-breaches/chaos-ransomware-rises-blacksuit-falls)**

◆**[WordPress外掛Post SMTP存在高風險漏洞，20萬網站恐面臨挾持風險](https://securityaffairs.com/180484/security/critical-wordpress-post-smtp-plugin-flaw-exposes-200k-sites-to-full-takeover.html)**

◆**[法國國防業者Naval Group傳出遭駭，攻擊者竊得1 TB內部資料](https://www.bleepingcomputer.com/news/security/frances-warship-builder-naval-group-investigates-1tb-data-breach/)**

◆**[俄羅斯航空公司Aeroflot傳出遭網路攻擊，電腦系統面臨大規模中斷，被迫取消逾100個航班](https://www.securityweek.com/cyberattack-on-russian-airline-aeroflot-causes-the-cancellation-of-more-than-100-flights/)**

◆**[列印管理軟體PaperCut存在高風險漏洞，CISA警告已被用於攻擊行動](https://www.bleepingcomputer.com/news/security/cisa-flags-papercut-rce-bug-as-exploited-in-attacks-patch-now/)**

### **【漏洞與修補】**

[**Mitel整合式通訊系統MX-ONE存在重大漏洞，恐被用於繞過身分驗證**](https://www.ithome.com.tw/news/170271)

加拿大電信業者Mitel發布資安公告，指出企業通訊平臺MX-ONE存在重大層級的身分驗證繞過資安漏洞，影響7.3至7.8 SP1版，CVSS風險達到9.4，該公司也已針對此漏洞發布修補程式，呼籲用戶要儘速採取行動因應。

MX-ONE是對話啟動協定（Session Initiation Protocol，SIP）為基礎打造的通訊平臺，主要的功能是提供網路語音通訊，例如VoIP、語音路由，以及通話管理，其特色是具備高度延展性，可支援數十萬個使用者，而受到大型企業組織採用。

目前這項資安漏洞尚未取得CVE編號，該漏洞出現在MX-ONE的元件Provisioning Manager，起因是存取控制不當造成，一旦攻擊者成功利用，就能在未經授權的情況下進行身分驗證繞過攻擊，直接存取管理員的帳號。

### **【資安產業動態】**

[**強化Prompt安全性成當務之急，從MCP生命週期、Agentic系統構成看資安挑戰**](https://www.ithome.com.tw/news/170300)

隨著LLM（大型語言模型）的應用起飛，新技術帶來機會，也產生風險，今年Agentic AI的快速崛起，更進一步加劇這方面的風險，也引起全球企業的高度關注，因此，這一兩年以來，開始有越來越多廠商開發相關的資安防禦解決方案，像是AI護欄（AI Guardrails）、AI Gateway，Firewall for AI，而且，國外已有不少資安或新創廠商積極投入，國內卻寥寥可數，奧義智慧正是其中之一，7月1日宣布推出新世代AI防火牆安全模組。

相隔幾天之後，在該公司舉辦的第二屆AI年會上，資料科學研發處處長楊政霖提出這方面的說明，幫助大家更清楚理解Agentic AI時代的資安挑戰，也提出相應的防禦思維與建議。

[**Google釋出OSS Rebuild確保開源套件安全**](https://www.ithome.com.tw/news/170265)

Google釋出OSS Rebuild以協助開發人員確保開源套件的安全性，免於供應鏈攻擊，目前已支援PyPI、NPM和Crates.io套件。

該公司指出，開源軟體已成現代應用開發的重要工具，然而開源工具普及使用也使其成為新的攻擊目標，像是透過感染眾多人使用的套件進行供應鏈攻擊。開源社群也分別發展出安全工具，如OpenSSF推出的安全檢查工具Security Scorecard、PyPI的Trusted Publisher和npm原生支援由OpenSSF主導的SLSA（Supply-chain Levels for Software Artifacts）框架等。但是這些計畫都只能解決部分問題，使專案的工作負擔，都落在接手的發布者或維護者身上。

OSS Rebuild包括四個部分：自動建構定義、SLSA Provenance證明、建構驗證工具及可自行架設的基礎架構。技術層面而言，OSS Rebuild透過自動化與啟發式（heuristics）技術重建開源套件並驗證其來源與建構方式，以便使用者驗證套件來源、瞭解其建構流程，並可基於可信版本進行自訂建構或產生更詳細的SBOM（軟體物料清單）。

### **近期資安日報**

[**【7月28日】勒索軟體ShinyHunters傳出對保險公司安聯人壽發動攻擊**](https://www.ithome.com.tw/news/170280)

[**【7月25日】SharePoint零時差漏洞災情浮現，恐成為全球危機**](https://www.ithome.com.tw/news/170267)

[**【7月24日】微軟支援身障者無障礙用途的UI自動化機制首遭惡意程式濫用**](https://www.ithome.com.tw/news/170243)
