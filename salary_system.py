import json
import os

FILE_NAME = os.path.join(os.path.dirname(__file__), 'salary_data.json')

class Salary:
    def __init__(self, worker_id, name, role, base_salary, hours_worked, bonus, deductions):
        self.worker_id = worker_id
        self.worker_name = name
        self.worker_role = role
        self.base_salary = base_salary
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.deductions = deductions

    def calculate_net_salary(self):
        #底薪 + 獎金 - 扣薪
        return self.base_salary + self.bonus - self.deductions

    def checkinfo(self):
        print("Salary Information:")
        print("  ID: {}".format(self.worker_id))
        print("  Name: {}".format(self.worker_name))
        print("  Role: {}".format(self.worker_role))
        print("  Base Salary: ${}".format(self.base_salary))
        print("  Hours Worked: {}".format(self.hours_worked))
        print("  Bonus: ${}".format(self.bonus))
        print("  Deductions: ${}".format(self.deductions))
        print("  Net Salary: ${}".format(self.calculate_net_salary()))

    def update_hours(self):
        print("Update work hours:")
        try:
            add_hours = float(input("  Enter hours to add: "))
            self.hours_worked += add_hours
            save_salaries(salary_list)
            print("Hours updated successfully!")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def update_bonus_deductions(self):
        print("Update Bonus and Deductions:")
        try:
            self.bonus = float(input("  New Bonus: $"))
            self.deductions = float(input("  New Deductions: $"))
            save_salaries(salary_list)
            print("Salary details updated successfully!")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def to_dict(self):
        # 轉換為字典，方便存 JSON
        return {
            "worker_id": self.worker_id,
            "worker_name": self.worker_name,
            "worker_role": self.worker_role,
            "base_salary": self.base_salary,
            "hours_worked": self.hours_worked,
            "bonus": self.bonus,
            "deductions": self.deductions
        }

def create_worker_salary():
    print("Create Worker Salary Profile:")
    while True:
        worker_id = input("  Worker ID: ")
        if any(s.worker_id == worker_id for s in salary_list):
            print("Worker ID already exists! Please enter a different ID.")
        else:
            break
    
    name = input("  Name: ")
    role = input("  Role (e.g., Cashier, Manager): ")
    
    try:
        base_salary = float(input("  Base Salary: "))
        hours_worked = 0.0
        bonus = 0.0
        deductions = 0.0

        new_salary = Salary(worker_id, name, role, base_salary, hours_worked, bonus, deductions)
        salary_list.append(new_salary)
        save_salaries(salary_list)
        print("Worker salary profile created successfully!")
    except ValueError:
        print("Invalid input for salary. Profile creation failed.")

def load_salaries():
    salaries = []
    if not os.path.exists(FILE_NAME):
        # 如果檔案不存在，先建立一個空的 JSON 陣列
        with open(FILE_NAME, "w") as file:
            json.dump([], file)
        return salaries

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            for item in data:
                salaries.append(
                    Salary(
                        item["worker_id"],
                        item["worker_name"],
                        item["worker_role"],
                        item["base_salary"],
                        item["hours_worked"],
                        item["bonus"],
                        item["deductions"]
                    )
                )
    except (FileNotFoundError, json.JSONDecodeError):
        print("Database file not found or corrupted.")

    return salaries

def save_salaries(salaries):
    os.makedirs(os.path.dirname(FILE_NAME), exist_ok=True)
    
    data_to_save = [s.to_dict() for s in salaries]
    with open(FILE_NAME, "w") as file:
        json.dump(data_to_save, file, indent=4)

def check_salary_data(worker_id):
    for s in salary_list:
        if s.worker_id == worker_id:
            return s
    return None

# 初始化
salary_list = load_salaries()
