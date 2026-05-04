# 位於: smart_store_system/systems/checkout_system/checkout_system.py

from datetime import datetime

class CheckoutSystem:
    def __init__(self, inventory_system, member_system, accounting_system):
        """
        初始化結帳系統，並接收其他系統的實例作為依賴。
        這樣結帳系統就不需要自己去讀寫其他人的 JSON 檔案，維持系統封裝性。
        """
        self.inventory_sys = inventory_system
        self.member_sys = member_system
        self.accounting_sys = accounting_system
        
        # 暫存當前交易的狀態
        self.cart = []            # 存放購物車內的商品 dict
        self.current_member = None # 當前結帳的會員資訊

    def scan_item(self, item_id, quantity=1):
        """掃描商品加入購物車"""
        # 1. 向庫存系統查詢商品資訊與庫存量
        item_info = self.inventory_sys.get_item(item_id)
        
        if not item_info:
            return False, "商品不存在"
            
        if item_info['stock'] < quantity:
            return False, f"庫存不足，目前僅剩 {item_info['stock']} 件"

        # 2. 加入購物車
        self.cart.append({
            "item_id": item_id,
            "name": item_info['name'],
            "price": item_info['price'],
            "quantity": quantity
        })
        return True, f"已加入 {item_info['name']} x {quantity}"

    def set_member(self, member_id):
        """設定結帳會員（以獲取折扣）"""
        member_info = self.member_sys.get_member(member_id)
        if member_info:
            self.current_member = member_info
            return True, f"歡迎，會員 {member_info['name']}"
        return False, "會員不存在"

    def calculate_total(self):
        """計算總金額（包含會員折扣）"""
        subtotal = sum(item['price'] * item['quantity'] for item in self.cart)
        
        discount = 1.0
        if self.current_member:
            # 假設會員系統有提供獲取折扣率的方法
            discount = self.member_sys.get_discount_rate(self.current_member['level'])
            
        total = int(subtotal * discount) # 計算折扣後總價
        return total, subtotal

    def process_payment(self, payment_amount):
        """處理付款與完成結帳"""
        if not self.cart:
            return False, "購物車是空的"

        total, _ = self.calculate_total()
        
        if payment_amount < total:
            return False, f"金額不足，需付款 {total} 元"

        # 1. 扣除庫存 (通知 inventory_system)
        for item in self.cart:
            self.inventory_sys.reduce_stock(item['item_id'], item['quantity'])

        # 2. 紀錄帳務 (通知 accounting_system)
        transaction_record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": self.cart,
            "total_amount": total,
            "member_id": self.current_member['id'] if self.current_member else None
        }
        self.accounting_sys.add_transaction(transaction_record)

        # 3. 計算找零並清空購物車
        change = payment_amount - total
        self.clear_cart()
        
        return True, f"結帳成功！找零: {change} 元"

    def clear_cart(self):
        """清空購物車與當前會員狀態"""
        self.cart = []
        self.current_member = None
