import os
import member_system as ms

def clear_screen():
    os.system("cls")

current_user = None   # 記錄目前登入者

def login():
    clear_screen()
    global current_user

    email = input("Email: ")
    password = input("Password: ")

    user = ms.check_data(email, password)

    if user:
        current_user = user
        print(f"Login successful. Welcome, {current_user.member_name}!")
    else:
        print("Login failed. Incorrect email or password.")


def logout():
    clear_screen()
    global current_user

    if current_user:
        print(f"{current_user.member_name} logged out.")
        current_user = None
    else:
        print("No user is currently logged in.")

def register():
    clear_screen()
    print("\n=== Register ===")
    ms.create_member()

    print("Registration successful!")

def member_menu():
    global current_user

    while current_user:
        clear_screen()
        print("=== Member Menu ===")
        print("Welcome:", current_user.member_name)
        print("1. View Profile")
        print("2. Change personal Information")
        print("3. Change password")
        print("4. Logout")


        choice = input("Choose: ")
        clear_screen()

        if choice == "1":
            current_user.checkinfo()
            input("\nPress Enter to continue...")
        elif choice == "2":
            current_user.change_info()
        elif choice == "3":
            current_user.change_password()
        elif choice == "4":
            logout()
        else:
            print("Invalid choice")
            input("Press Enter to continue...")

def main():
    while current_user is None:
        print("\n=== Customer System ===")
        print("1. Login")
        print("2. Reigister")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            break
        else:
            print("Invalid choice")
    else:
        member_menu()

if __name__ == "__main__":
    main()