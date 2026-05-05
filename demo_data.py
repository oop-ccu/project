import accounting_system as acc
import salary_system as ss
from datetime import datetime, timedelta

def seed_data():
    print("🚀 Starting Data Seeding...")
    
    # 1. 初始化系統
    accounting = acc.AccountingSystem()
    
    # 2. 模擬幾筆一般的收入與支出
    # 模擬店面租金與水電支出
    accounting.record_expense(20000, "Monthly Store Rent")
    accounting.record_expense(3500, "Electricity and Water Bill")
    
    # 模擬採購店內使用的平板設備 (假設買了跟 Tesla 介面一樣酷的控制螢幕)
    accounting.record_expense(12000, "Store Management Tablet")

    # 3. 模擬「結帳系統」傳過來的複雜交易 (使用 add_transaction)
    # 交易 A：一位會員買了電子零件
    mock_record_1 = {
        "timestamp": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
        "items": [
            {"item_id": "P001", "name": "USB-C Adapter", "price": 500, "quantity": 2},
            {"item_id": "P002", "name": "Network Cable", "price": 150, "quantity": 5}
        ],
        "total_amount": 1750,
        "member_id": "M001"
    }
    accounting.add_transaction(mock_record_1)

    # 交易 B：另一位買家買了高單價商品
    mock_record_2 = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": [
            {"item_id": "P003", "name": "High-Speed Router", "price": 4500, "quantity": 1}
        ],
        "total_amount": 4500,
        "member_id": "M002"
    }
    accounting.add_transaction(mock_record_2)

    # 4. 模擬薪資系統發放記錄
    # 假設老闆發了第一筆薪水給員工 W001
    accounting.record_expense(32000, "Personnel Cost - Worker W001 Salary")

    print("✅ Data Seeding Completed!")
    print("Files 'accounting_data.json' and 'salary_data.json' are now ready for Demo.")

if __name__ == "__main__":
    seed_data()
