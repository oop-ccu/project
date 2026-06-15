### 1. 系統架構設計

本系統採用 **模組化 (Modular) 與微服務雛型架構**。系統分為純後端邏輯層、終端機前端介面層，以及一個負責外部對接的 Flask API 閘道器。

#### 1.1 核心模組 (Core Modules)

* `accounting_system.py`：會計模組，處理總餘額計算及交易明細的新增與讀取。
* `salary_system.py`：薪資模組，包含 `Salary` 類別，負責工時更新、淨薪資計算 (底薪+獎金-扣款)。
* `inventory_system.py`：庫存模組，包含 `item` 類別，管理商品名稱、數量與總值。
* `member_system.py`：(參照程式碼推斷) 會員模組，處理會員認證與折扣邏輯。
* `checkout_system.py`：結帳核心，負責協調庫存、會員與會計系統完成交易。

#### 1.2 介面層 (UI Layer)

* `owner_ui.py`：調用 `accounting`、`salary`、`member`、`inventory` 模組，作為店長的整合儀表板。
* `worker_ui.py`：依賴 `salary_system`，提供員工自我管理的終端機介面。
* `customer_ui.py`：依賴 `member_system`，提供顧客操作介面。

#### 1.3 服務層 (API Layer)

* `api.py`：使用 Flask 實作，將 JSON 資料庫的讀寫包裝成 HTTP 端點，支援跨來源資源共用 (CORS)。

### 2. 資料庫設計 (Data Design)

系統使用本地端 JSON 檔案儲存資料，以下為各檔案結構規劃：

* **`accounting_data.json`**
* `total_balance` (Float): 當前帳戶總餘額。
* `transactions` (List): 交易明細陣列，包含 `transaction_id`, `type` (revenue/expense/checkout revenue), `amount`, `description`, `date`, `items`, `member_id`。


* **`salary_data.json`**
* 包含員工物件陣列：`worker_id`, `worker_name`, `worker_role`, `base_salary`, `hours_worked`, `bonus`, `deductions`。


* **`inventory_data.json`**
* 包含商品物件陣列：`id`/`name`, `quantity`/`stock`, `value`/`price`, `total_value`, `date`。


* **`member_data.json`**
* 包含會員物件陣列：`id`, `name`, `email`, `password`, `age`, `gender`, `level`, `total_spending`。



### 3. 系統互動流程設計 (Sequence & Logic)

#### 3.1 結帳處理流程 (Checkout Flow)

結帳系統 (`CheckoutSystem`) 扮演 Facade (外觀模式) 的角色，隱藏了多系統互動的複雜性。

1. **掃描商品**：`scan_item()` 呼叫 `inventory_system.get_item()` 驗證庫存，成功後加入 `cart`。
2. **綁定會員**：`set_member()` 呼叫 `member_system.get_member()` 獲取會員資訊與折扣率。
3. **計算金額**：`calculate_total()` 計算 `(商品單價 * 數量) * 會員折扣率`。
4. **處理付款** (`process_payment`):
* 通知 `inventory_system` 減少庫存 (`reduce_stock`)。
* 封裝交易紀錄，傳送至 `accounting_system.add_transaction()`。
* 清空購物車，回傳找零金額。



#### 3.2 發放薪資流程 (Salary Payment Flow)

1. 店長於 `owner_ui` 輸入 Worker ID 查詢員工 (`ss.check_salary_data`)。
2. 呼叫 `worker.calculate_net_salary()` 取得應發放總額。
3. 調用 `accounting.record_expense()` 將薪資紀錄為商店支出，會計系統自動更新餘額並儲存至 JSON。
4. 重置該員工 `Salary` 物件內的 `hours_worked`, `bonus`, `deductions` 為 0。
5. 呼叫 `ss.save_salaries()` 覆寫 `salary_data.json`，完成發放。
