import os
import accounting_system as acc
import salary_system as ss
import member_system as ms      # 新增：載入會員系統
import inventory_system as inv  # 新增：載入庫存系統

accounting = acc.AccountingSystem()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

is_logged_in = False

def login():
    clear_screen()
    global is_logged_in
    print("=== Owner Login ===")
    username = input(" Username: ")
    password = input(" Password: ")

    if username == "admin" and password == "admin":
        is_logged_in = True
        print("Login successful. Welcome, Boss!")
        input("\nPress Enter to continue...")
    else:
        print("Login failed. Incorrect credentials.")
        input("\nPress Enter to continue...")

def logout():
    clear_screen()
    global is_logged_in
    is_logged_in = False
    print("Owner logged out.")
    input("\nPress Enter to continue...")

# --- 新增功能：全店總覽 Dashboard ---
def view_overview():
    clear_screen()
    print("=== Store Overview (全店總覽) ===")
    
    # 1. 取得會計餘額
    balance = accounting.get_balance()
    print(f"💰 Current Total Balance: ${balance}")
    
    # 2. 取得會員總數 (為了確保拿到最新資料，可以重新載入)
    ms.member_list = ms.load_members()
    total_members = len(ms.member_list)
    print(f"👥 Total Members: {total_members} 人")
    
    # 3. 取得庫存商品種類總數
    inv.item_list = inv.load_items()
    total_items = len(inv.item_list)
    print(f"📦 Total Product Types: {total_items} 項")
    
    # 4. 取得員工總數
    ss.salary_list = ss.load_salaries()
    total_workers = len(ss.salary_list)
    print(f"⚙️  Total Workers: {total_workers} 人")
    
    input("\nPress Enter to continue...")
# -----------------------------------

def view_revenue():
    clear_screen()
    print("=== Store Revenue ===")
    balance = accounting.get_balance()
    print(f"Current Total Balance: ${balance}")
    input("\nPress Enter to continue...")

def view_transaction_history():
    clear_screen()
    print("=== Transaction History ===")
    history = accounting.get_transaction_history()
    if not history:
        print("No transactions yet. The store just opened!")
    else:
        for t in history:
            print(f"[{t['date']}] {t['type'].upper()} | Amount: ${t['amount']} | Detail: {t['description']}")
    input("\nPress Enter to continue...")

def manage_salaries():
    clear_screen()
    print("=== Manage Salaries ===")
    
    # 為了確保抓到最新的打卡時數，先重新載入
    ss.salary_list = ss.load_salaries()
    
    worker_id = input("Enter Worker ID (e.g., W001): ")
    worker = ss.check_salary_data(worker_id) 
    
    if not worker:
        print("Worker not found.")
        input("\nPress Enter to continue...")
        return

    while True:
        clear_screen()
        print(f"--- Managing Worker: {worker.worker_name} ({worker.worker_role}) ---")
        print("1. View Worker Salary Profile (查看薪資明細)")
        print("2. Pay Salary (發放薪資並記帳)")
        print("3. Return to Main Menu (返回主選單)")
        
        choice = input("Choose: ")
        
        if choice == "1":
            print("\n")
            worker.checkinfo()
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            net_salary = worker.calculate_net_salary()
            if net_salary <= 0:
                print("此員工目前不需發放薪資 (或扣款大於薪水)。")
            else:
                # 1. 呼叫會計系統支出 API
                description = f"Personnel Cost - Paid salary to {worker.worker_name} ({worker_id})"
                accounting.record_expense(net_salary, description)
                
                # 2. 【Bug 修復】發薪後將時數、獎金與扣除額歸零，並更新薪資資料庫
                worker.hours_worked = 0.0
                worker.bonus = 0.0
                worker.deductions = 0.0
                ss.save_salaries(ss.salary_list) # 儲存回 JSON
                
                print(f"\n成功發放薪資 ${net_salary} 給 {worker.worker_name}！")
                print("系統已自動從會計帳本中扣除該筆款項，並重置該員工的本月工時。")
            
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            break
        else:
            print("Invalid choice")
            input("\nPress Enter to continue...")

def owner_menu():
    global is_logged_in

    while is_logged_in:
        clear_screen()
        print("=== Owner Menu ===")
        print("Welcome, Boss!")
        print("1. View Store Overview (全店總覽)  <-- [NEW]")
        print("2. View Total Revenue (Accounting)")
        print("3. View Transaction History (Accounting)")
        print("4. View Worker Salaries (Salary System)")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            view_overview()
        elif choice == "2":
            view_revenue()
        elif choice == "3":
            view_transaction_history()
        elif choice == "4":
            manage_salaries()
        elif choice == "5":
            logout()
        else:
            print("Invalid choice")
            input("\nPress Enter to continue...")

def main():
    while not is_logged_in:
        clear_screen()
        print("\n=== Owner System ===")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            login()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
            input("\nPress Enter to continue...")
    else:
        owner_menu()

if __name__ == "__main__":
    main()
