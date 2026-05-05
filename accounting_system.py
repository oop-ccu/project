import json
import os
from datetime import datetime

class AccountingSystem:
    def __init__(self):
        self.data_file = os.path.join(os.path.dirname(__file__), 'accounting_data.json')
        self.data = self._load_data()

    # 讀取帳本
    def _load_data(self):
        if not os.path.exists(self.data_file):
            return {"total_balance": 0.0, "transactions": []}
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"total_balance": 0.0, "transactions": []}

    # 存檔
    def _save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    # 新增交易紀錄
    def _add_transaction(self, t_type, amount, description):
        transaction = {
            "transaction_id": f"T{len(self.data['transactions']) + 1:04d}",
            "type": t_type,
            "amount": amount,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.data["transactions"].append(transaction)
        self.data["total_balance"] += amount
        self._save_data()

    # --- 以下是開放給別的系統呼叫的 API (Public Methods) ---

    def record_revenue(self, amount, description="一般收入"):
        """記錄收入 (例如：結帳系統呼叫此方法)"""
        if amount <= 0:
            raise ValueError("收入金額必須大於 0")
        self._add_transaction("revenue", amount, description)
        return True

    def record_expense(self, amount, description="一般支出"):
        """記錄支出 (例如：庫存系統進貨、發薪水時呼叫此方法)"""
        if amount <= 0:
            raise ValueError("支出金額請輸入正數，系統會自動轉為扣款")
        self._add_transaction("expense", -amount, description)
        return True

    def get_balance(self):
        """獲取目前總餘額 (例如：老闆 UI 查看時呼叫)"""
        return self.data["total_balance"]

    def get_transaction_history(self):
        """獲取所有交易明細"""
        return self.data["transactions"]
        
# --- 開放給 checkout_system (結帳大廳經理) 呼叫的進階 API ---
    def add_transaction(self, transaction_record):
        """
        接收來自結帳系統的整筆訂單紀錄，並完整保存所有明細。
        """
        # 1. 抓出結帳總金額
        amount = transaction_record.get("total_amount", 0)
        
        # 2. 建立一筆進階的交易紀錄，融合會計系統的流水號與結帳系統的完整資料
        new_transaction = {
            "transaction_id": f"T{len(self.data['transactions']) + 1:04d}",
            "type": "revenue",  # 結帳傳來的一定是收入
            "amount": amount,
            
            # 直接使用結帳系統傳來的時間，如果沒有才用現在時間
            "date": transaction_record.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            
            # 【關鍵】完整保留他們傳過來的商品清單與會員ID！
            "items": transaction_record.get("items", []), 
            "member_id": transaction_record.get("member_id", None)
        }

        # 3. 存入帳本並更新總餘額
        self.data["transactions"].append(new_transaction)
        self.data["total_balance"] += amount
        self._save_data()
        
        return True
