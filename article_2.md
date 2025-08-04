Title: 【資安日報】7月31日，駭客挾持ATM出奇招，於隔離網路部署實體後門

URL Source: https://www.ithome.com.tw/news/170345

Published Time: Thu, 31 Jul 2025 23:09:46 GMT

Markdown Content:
本週有多家資安業者公布資安事故的調查結果，其中最為特別的是針對ATM的攻擊行動，揭露此事的資安業者Group-IB發現，駭客組織UNC2891透過嵌入式設備當做實體後門，從而對受害銀行的ATM系統上下其手，不過他們如何將設備部署到銀行內部？[資安新聞網站Bleeping Computer推測](https://www.bleepingcomputer.com/news/security/hackers-plant-4g-raspberry-pi-on-bank-network-in-failed-atm-heist/)，很可能是收買員工來達到目的。

鎖定軟體套件開發者的攻擊行動也相當值得留意，我們上週報導針對NPM套件開發者的網釣攻擊，本週PyPI針對套件維護者提出警告，他們發現有人打造假的PyPI網站，想要騙取帳密資料。再者，利用SAP NetWeaver滿分漏洞，以及VMware虛擬化平臺已知漏洞的攻擊手法，也有資安業者公布新的調查結果。

### 【攻擊與威脅】

[**駭客組織UNC2891打造挾持ATM的實體後門**](https://www.ithome.com.tw/news/170343)

[![Image 1](https://s4.itho.me/sites/default/files/images/UNC2891-4.png)](https://s4.itho.me/sites/default/files/images/UNC2891-4.png)

一般而言，駭客針對隔離網路環境發動攻擊，最常見的就是透過USB蠕蟲進行滲透，藉由USB儲存裝置被帶到隔離網路環境從事活動，但最近有資安業者發現相當不尋常的手法，竟是部署實體設備來達到目的。

本週資安業者Group-IB發布部落格文章，針對專門鎖定自動櫃員機（ATM）的駭客組織UNC2891公布調查結果，指出這些以經濟利益為動機的駭客使用相當獨特且隱密的手法，試圖破壞銀行的基礎設施，其中的反鑑識手法過往未曾出現，後門程式無法透過處理程序列表掌握，其中的關鍵之一，就是使用嵌入式設備滲透實體網路環境，這樣的做法極為罕見。

值得留意的是，Thales於2022年曾遭勒索軟體LockBit 3.0攻擊，導致資料外洩，因此Bleeping Computer推測，這批檔案很有可能源自當時外流的資料。

駭客架設冒牌PyPI網站，企圖竊取套件開發者的帳密資料

駭客不斷鎖定開發人員經常使用的套件庫NPM、PyPI發動攻擊，其中一種最常見的手法，是利用域名搶注手法上架有問題的套件，藉此於開發人員的電腦部署惡意軟體，但最近有一波是鎖定套件維護者的網釣攻擊，之前有針對NPM熱門套件開發者的攻擊行動，如今駭客將目標轉向PyPI套件的開發者，使得PyPI管理群特別提出警告。

7月28日PyPI基金會發布部落格提出警告，有人鎖定最近幾天發布專案的PyPI維護者而來，利用套件裡的中繼資料取得電子郵件信箱，假借電子郵件驗證的名義寄信，值得留意的是，該「驗證信」來自[noreply@pypj.org](mailto:noreply@pypj.org)。

一旦收信人依照指示點選信中連結來驗證電子郵件信箱，他們就會被帶往偽裝成PyPI的釣魚網站，並要求執行登錄，若是收信人照做，他們發出的請求就會傳給真正的PyPI網站，使得收信人以為自己成功登錄PyPI（並完成驗證），但實際上，這麼做會將帳密提供給釣魚網站。

[**SAP NetWeaver滿分漏洞遭到利用，駭客企圖散布惡意程式Auto-Color**](https://www.ithome.com.tw/news/170318)

[![Image 2](https://s4.itho.me/sites/default/files/images/6888a0eaa370406afd285b15_Screenshot%202025-07-29%20at%2011_20_41.png)](https://s4.itho.me/sites/default/files/images/6888a0eaa370406afd285b15_Screenshot%202025-07-29%20at%2011_20_41.png)

今年4月下旬SAP緊急修補應用程式伺服器NetWeaver重大層級資安漏洞CVE-2025-31324，由於這項漏洞被發現時，已被用於攻擊NetWeaver，再加上危險程度達到滿分10分，後續傳出中國駭客Chaya_004、CL-STA-0048、UNC5221、UNC5174、Earth Lamia，勒索軟體駭客「變臉（BianLian）」與RansomEXX也出手，將此漏洞用於實際攻擊，如今又有資安業者公布相關調查結果，指出他們看到駭客利用這項漏洞部署Linux後門程式。

美國一家化學公司於今年4月，遭受名為Auto-Color的Linux後門程式攻擊，駭客於3天的時間裡，成功入侵該公司的網路環境，下載有問題的檔案，並試圖與Auto-Color的惡意基礎設施進行通訊。揭露此事的資安業者Darktrace指出，他們封鎖相關惡意行為、進行深度調查，發現駭客利用CVE-2025-31324，趁機滲透這家化學公司的NetWeaver主機。

Darktrace之所以察覺這起事故，主要是因為他們的資安維運中心4月28日收到警報，有人從網際網路存取的主機下載可疑的ELF檔案，而此伺服器的用途，似乎是NetWeaver主機。經入侵指標（IoC）的比對，這個ELF執行檔就是Auto-Color。

[**駭客組織Fire Ant鎖定VMware虛擬化平臺而來，利用已知漏洞入侵虛擬機器**](https://www.ithome.com.tw/news/170299)

去年1月，Google揭露中國駭客UNC3886利用零時差漏洞CVE-2023-34048的攻擊行動，駭客從2021年開始用於對VMware虛擬化平臺vCenter下手，並在癱瘓VMware服務後的數分鐘內，部署後門程式。後續有其他駭客跟進，利用這項漏洞從事網路間諜活動。

資安業者Sygnia自今年初開始，追蹤及回應由駭客組織Fire Ant的長期網路間諜活動，這些駭客專門針對VMware ESXi、vCenter，以及網路設備而來，透過Hypervisor層級的攻擊手法來迴避偵測，並持續在受害組織活動。根據駭客使用的工具與手法，Sygnia研判Fire Ant與UNC3886有所關連。

針對駭客的攻擊途徑，Sygnia指出Fire Ant對於受害組織的ESXi主機與vCenter伺服器建立強大的控制機制，然後使用未經身分驗證的命令，從主機對用戶端下達，並透過特定帳密進行存取。這些駭客為了突破不同的網段並試圖存取隔離網路環境，採取複雜且隱密的手法，組成多階段攻擊鏈。他們運用虛擬化平臺及網路基礎設施作為初始存取、橫向移動、持續活動的管道。

**其他攻擊與威脅**

◆**[IT服務供應商Ingram Micro傳出遭攻擊，勒索軟體SafePay聲稱竊得3.5 TB資料](https://www.bleepingcomputer.com/news/security/safepay-ransomware-threatens-to-leak-35tb-of-ingram-micro-data/)**

### **【漏洞與修補】**

[**聯想桌機韌體存在可用以繞過開機防護的漏洞**](https://www.ithome.com.tw/news/170331)

聯想本周發布安全公告，提醒數款桌機韌體存在6項可讓攻擊者繞過安全開機（Secure Boot）防護機制的漏洞，可使其執行程式碼或讀取敏感資訊。

這6項漏洞包含CVE-2025-4421、CVE-2025-4422、CVE-2025-4423、CVE-2025-4424、CVE-2025-4425、CVE-2025-4426。這批漏洞皆存在聯想桌機內建的Insyde BIOS中，影響產品包括Lenovo IdeaCentre及Yoga AiO產品部分機種，可使具備權限的本地攻擊者升級權限以讀取系統管理記憶體（SMRAM）內容，或在系統管理模式（SMM）中執行任意程式碼。

這批漏洞是由資安廠商Binarly通報，對於這些漏洞帶來的影響，他們指出，一旦運用這些漏洞，攻擊者可提升權限由ring-0到ring-2、藉此讀取SMRAM內容，或是在SMM模式下執行任意程式碼。

**其他漏洞與修補**

◆**[蘋果針對旗下電腦、行動裝置、電視盒、VR裝置、智慧手錶發布更新，修補已遭利用的Chrome零時差漏洞](https://www.bleepingcomputer.com/news/security/apple-patches-security-flaw-exploited-in-chrome-zero-day-attacks/)**

◆**[針對6月思科公布的網路存取控制平臺ISE滿分漏洞，研究人員公布細節](https://www.bleepingcomputer.com/news/security/exploit-available-for-critical-cisco-ise-bug-exploited-in-attacks/)**

◆**[VMware虛擬機器元件存在重大漏洞VGAuth，攻擊者有機會得到完整存取權限](https://gbhackers.com/critical-vgauth-flaw-in-vmware-tools/)**

◆**[AI開發平臺Base44存在身分驗證漏洞，攻擊者有機會存取企業代管的應用程式](https://thehackernews.com/2025/07/wiz-uncovers-critical-access-bypass.html)**

### **【資安產業動態】**

[**Palo Alto Networks以250億美元併購身分安全業者CyberArk**](https://www.ithome.com.tw/news/170334)

資安大廠Palo Alto Networks周三（7月30日）宣布，已和CyberArk簽定近250億美元併購協議，進軍身分安全方案領域，特別是解決企業引進AI代理人帶來的安全問題。

這紙協議下，Palo Alto Networks上周五收盤股價溢價26%，總計以每股45美元及交換股票的方式買下CyberArk，總價近250億美元。本交易已獲得雙方董事會的無異議通過，視交易條件滿足進度而定，預計在Palo Alto Networks會計年度2026年第二季完成。

本案是近年金額最大的資安併購案之一。其他大型併購還包括：Google Cloud今年3月以320億美元的現金買下雲端安全平臺Wiz、思科以280億美元併購資料分析業者Splunk以強化安全產品。其他還有2021年私募基金業者Thoma Bravo以123億美元買下電子郵件安全平臺Proofpoint，以及2019年博通（Broadcom）以107億美元併購Symantec的企業安全部門。

### **近期資安日報**

[**【7月30日】美國明尼蘇達州首府遭到網攻，進入緊急狀態、動員國民兵因應**](https://www.ithome.com.tw/news/170328)

[**【7月29日】Scattered Spider鎖定VMware虛擬化平臺而來，並使用勒索軟體加密檔案**](https://www.ithome.com.tw/news/170302)

[**【7月28日】勒索軟體ShinyHunters傳出對保險公司安聯人壽發動攻擊**](https://www.ithome.com.tw/news/170280)
