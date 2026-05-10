###function

🛍 Customer（顧客）

首頁英雄區塊 + 商品網格（來自 inventory_system.py）
搜尋、類別篩選、購物車側欄
會員登入（member_system.py）、註冊（自動分配 ID）
結帳時自動套用會員折扣（bronze/silver/gold/vip），並更新點數與消費紀錄
Demo 帳號：alice@demo.com / 1234

⚙ Worker（員工）

用 Worker ID 登入（W001、W002、W003）
新增庫存商品、查看現有庫存
登錄工時、查看自己的薪資明細
對應 worker_ui.py + salary_system.py

👔 Owner（老闆）

帳號：admin / admin
總覽儀表板（餘額、收入、支出、人員/庫存數量）
全部交易明細（accounting_system.py）
會員管理、庫存總覽
薪資管理 —— 可新增員工、一鍵發薪（自動記帳）
手動記錄支出

所有資料都是 in-memory 共享的，切換角色後資料會同步（例如顧客結帳後，老闆的交易紀錄立即更新）。Smart store
----------------------------------------------------------------------------------------------------------------------------------------
####如何執行
下載 zip 後，解壓縮，然後在資料夾裡按住 Shift + 滑鼠右鍵，選「在這裡開啟 PowerShell 視窗」或「在終端機中開啟」，執行這兩行：
npm install
npm run dev

然後在chrome開啟終端機顯示的網址（通常是 http://localhost:5173）。
