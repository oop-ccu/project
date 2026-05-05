import sys
import os


# 匯入老闆會用到的系統
from systems.accounting_system.accounting_system import AccountingSystem
from systems.salary_system import salary_system as ss

# 初始化你的會計系統！
accounting = AccountingSystem()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

is_logged_in = False

def login():
    clear_screen()
    global is_logged_in
    print("=== Owner Login ===")
    username = input(" Username: ")
    password = input(" Password: ")

    # 老闆帳號通常是最高權限，為了 Demo 方便，先設定簡單的預設帳密 admin/admin
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

def view_revenue():
    """查看店鋪總營收 (呼叫你的會計系統)"""
    clear_screen()
    print("=== Store Revenue ===")
    balance = accounting.get_balance()
    print(f"Current Total Balance: ${balance}")
    input("\nPress Enter to continue...")

def view_transaction_history():
    """查看所有交易明細 (呼叫你的會計系統)"""
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
    """查看員工薪水 (呼叫組員的薪水系統)"""
    clear_screen()
    print("=== Manage Salaries ===")
    print("1. View Worker Salary Profile")
    print("2. Return to Main Menu")
    
    choice = input("Choose: ")
    if choice == "1":
        worker_id = input("Enter Worker ID (e.g., W001): ")
        # 呼叫 salary_system 的功能
        worker = ss.check_salary_data(worker_id) 
        if worker:
            worker.checkinfo()
        else:
            print("Worker not found.")
        input("\nPress Enter to continue...")

def owner_menu():
    global is_logged_in

    while is_logged_in:
        clear_screen()
        print("=== Owner Menu ===")
        print("Welcome, Boss!")
        print("1. View Total Revenue (Accounting)")
        print("2. View Transaction History (Accounting)")
        print("3. View Worker Salaries (Salary System)")
        print("4. Logout")

        choice = input("Choose: ")

        if choice == "1":
            view_revenue()
        elif choice == "2":
            view_transaction_history()
        elif choice == "3":
            manage_salaries()
        elif choice == "4":
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
