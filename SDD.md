根據您提供的程式碼與架構，我按照軟體設計說明書（Software Design Description, SDD）的標準模板，為此 **Smart Store System（智慧商店系統）** 撰寫了一份完整的設計文件。

---

# 智慧商店系統 (Smart Store System) 軟體設計說明書 (SDD)

## 1. 簡介 (Introduction)

### 1.1 目的
本文件旨在詳細說明「智慧商店系統」的軟體架構、模組設計、資料結構及介面定義。本系統為一整合性零售管理解決方案，涵蓋會員管理、庫存控制、財務會計、員工薪資及前端收銀結帳功能。

### 1.2 系統範圍
本系統包含：
*   **後端邏輯層**：由 Python 編寫的五大核心子系統。
*   **資料持久層**：使用 JSON 檔案進行輕量化資料儲存。
*   **通訊層**：Flask RESTful API 提供前後端分離之對接。
*   **使用者介面層**：
    *   CLI (Command Line Interface)：供開發與管理使用的終端機介面。
    *   Web UI (React)：供顧客與員工使用的現代化網頁介面。

---

## 2. 系統架構設計 (System Architecture)

### 2.1 總體架構
本系統採用 **模組化架構 (Modular Architecture)** 與 **分層設計 (Layered Design)**：

1.  **UI Layer**: 負責與使用者互動 (CLI: `owner_ui`, `worker_ui`, `customer_ui` / Web: React)。
2.  **API Layer**: `api.py` 負責處理 HTTP 請求並呼叫對應系統模組。
3.  **Business Logic Layer**: 核心子系統 (`Member`, `Inventory`, `Accounting`, `Salary`, `Checkout`)。
4.  **Data Layer**: 持久化儲存 (`.json` 檔案)。

### 2.2 模組關係圖 (Component Interaction)
*   **Checkout System** 為核心調度者，結帳時會同時呼叫：
    *   `Inventory System`：扣除庫存。
    *   `Member System`：計算折扣與更新點數。
    *   `Accounting System`：記錄營收帳務。

---

## 3. 子系統詳細設計 (Detailed Module Design)

### 3.1 會員系統 (Member System)
*   **類別：** `member`
*   **屬性：** `name`, `email`, `password`, `age`, `gender`, `coupon`, `point`, `total_spending`, `level` (bronze/silver/gold/vip)。
*   **關鍵功能：**
    *   `check_data(email, password)`：驗證登入。
    *   `save_members()` / `load_members()`：JSON 序列化。
    *   等級制折扣邏輯。

### 3.2 庫存系統 (Inventory System)
*   **類別：** `item`
*   **屬性：** `id`, `name`, `quantity`, `value` (price), `date`。
*   **關鍵功能：**
    *   `add_item()`：新增商品。
    *   `reduce_stock(id, qty)`：結帳時扣除庫存。
    *   `change_info()`：修改商品資訊。

### 3.3 會計系統 (Accounting System)
*   **類別：** `AccountingSystem`
*   **關鍵功能：**
    *   `record_revenue(amount, desc)`：記錄收入。
    *   `record_expense(amount, desc)`：記錄支出（如租金、薪資）。
    *   `add_transaction(record)`：接收結帳系統傳來的完整交易明細（含品項）。
    *   自動計算 `total_balance`。

### 3.4 薪資系統 (Salary System)
*   **類別：** `Salary`
*   **屬性：** `worker_id`, `worker_name`, `base_salary`, `hours_worked`, `bonus`, `deductions`。
*   **關鍵功能：**
    *   `calculate_net_salary()`：計算實發薪資 (底薪 + 獎金 - 扣除額)。
    *   `update_hours()`：員工回報工時。
    *   一鍵發薪：將發薪結果連動至會計系統記錄為支出。

### 3.5 結帳系統 (Checkout System)
*   **功能：** 扮演大廳經理 (Manager) 角色。
*   **流程：**
    1.  掃描商品 (Scan Item)。
    2.  讀取會員 (Identify Member) 並計算折扣率。
    3.  計算總金額。
    4.  確認付款並觸發「跨系統資料同步」。

---

## 4. 資料設計 (Data Design)

系統使用 4 個主要的 JSON 檔案作為資料庫：

| 檔案名稱 | 描述 | 關鍵欄位 |
| :--- | :--- | :--- |
| `member_data.json` | 會員資料 | email, password, level, points |
| `inventory_data.json` | 商品庫存 | id, name, price, stock |
| `accounting_data.json` | 財務帳本 | total_balance, transactions_list |
| `salary_data.json` | 員工薪酬 | worker_id, base_salary, hours |

---

## 5. 介面設計 (Interface Design)

### 5.1 角色介面定義
1.  **Owner (老闆)**：
    *   功能：全店總覽 (Dashboard)、查看營收、發放員工薪資、管理會員。
2.  **Worker (員工)**：
    *   功能：登入、回報工時、庫存檢視、簡易結帳。
3.  **Customer (顧客)**：
    *   功能：商品瀏覽、註冊/登入、個人資料管理、購物車結帳。

### 5.2 API 路由設計 (RESTful API)
*   `GET /api/members`：取得所有會員。
*   `POST /api/accounting/transactions`：新增交易紀錄。
*   `PUT /api/inventory/<id>`：更新庫存。
*   `GET /api/salary`：管理薪資發放。

---

## 6. 系統安全與維護

1.  **資料完整性**：在 `AccountingSystem` 與 `SalarySystem` 中，每次讀取前皆會呼叫 `_load_data()` 以確保獲取最新 JSON 狀態。
2.  **併發處理**：API 採用 Flask 處理同步請求。
3.  **錯誤處理**：系統內建 `try-except` 捕捉 `JSONDecodeError` 與 `FileNotFoundError`，避免資料毀損導致系統崩潰。

---

**核准日期：** 2024年5月  
**版本：** v1.0.0  
**開發團隊：** Smart Store Project Team
