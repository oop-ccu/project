import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 匯入薪資系統當作物件跟函式庫使用 
import systems.salary_system.salary_system as ss

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear") # 增加相容性

current_worker = None   # 記錄目前登入的工作人員

def login():
    clear_screen()
    global current_worker

    print("=== Worker Log In ===")
    # 使用 worker_id 作為登入憑證 
    worker_id = input("  Worker ID: ")

    # 呼叫底層系統檢查資料
    worker = ss.check_salary_data(worker_id)

    if worker:
        current_worker = worker
        print(f"Login successful. Welcome, {current_worker.worker_name} ({current_worker.worker_role})!")
    else:
        print("Login failed. Worker ID not found.")

def logout():
    clear_screen()
    global current_worker

    if current_worker:
        print(f"{current_worker.worker_name} logged out.")
        current_worker = None
    else:
        print("No worker is currently logged in.")

def worker_menu():
    global current_worker

    while current_worker:
        clear_screen()
        print("=== Worker Menu ===")
        print(f"Welcome: {current_worker.worker_name} [{current_worker.worker_role}]")
        print("1. View Salary & Profile (查看個人薪資資訊)")
        print("2. Report Work Hours (回報/增加工時)")
        print("3. Manage Inventory (庫存管理 - 尚未串接)")
        print("4. Checkout System (收銀結帳 - 尚未串接)")
        print("5. Logout")

        choice = input("Choose: ")
        clear_screen()

        if choice == "1":
           
            current_worker.checkinfo()
            input("\nPress Enter to continue...")
        elif choice == "2":
            
            current_worker.update_hours()
            input("\nPress Enter to continue...")
        elif choice == "3":
            print("即將串接 inventory_system.py ...")
            input("\nPress Enter to continue...")
        elif choice == "4":
            print("即將串接 checkout_system.py ...")
            input("\nPress Enter to continue...")
        elif choice == "5":
            logout()
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice")
            input("\nPress Enter to continue...")

def main():
    while current_worker is None:
        print("\n=== Smart Store - Worker System ===")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            login()
        elif choice == "2":
            break
        else:
            print("Invalid choice")
    else:
        # 登入成功後進入員工選單
        worker_menu()

if __name__ == "__main__":
    # 確保系統啟動時，底層的薪資系統資料有被載入
    if not ss.salary_list:
        print("系統提示：目前沒有任何員工資料，請聯絡老闆 (Owner) 新增員工。")
    main()
