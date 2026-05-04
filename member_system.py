FILE_NAME1 = 'member_data.json'
import json

class member:
    def __init__(self, name,email ,password, age, gender, coupon, point, total_spending):
        self.member_name = name
        self.member_email = email
        self.member_password = password
        self.member_age = age
        self.member_gender = gender
        self.member_coupon = coupon
        self.member_point = point
        self.member_total_spending = total_spending
    
    def checkinfo(self):
        print("Member information:")
        print("  Name: {}".format(self.member_name))
        print("  Email: {}".format(self.member_email))        
        print("  Age: {}".format(self.member_age))
        print("  Gender: {}".format(self.member_gender))
        print("  Coupon: {}".format(self.member_coupon))
        print("  Point: {}".format(self.member_point))
        print("  Total spending: {}".format(self.member_total_spending))
    
    def change_info(self):
        print("Change personal information:")
        self.member_name = input("  New Name: ")
        while True:
            new_email = input(" New Email: ")
            if new_email != self.member_email and any(m.member_email == new_email for m in members):
                print("Email already registered! Please enter a different email.")
            else:
                self.member_email = new_email
                break
        self.member_age = int(input("  New Age: "))
        self.member_gender = input("  New Gender: ")
        save_members(members)
        print("Information updated successfully!")

    def change_password(self):
        print("Change password:")
        old_password = input("  Please input previous password: ")
        if old_password != self.member_password:
            print("Wrong password! Try again.")
            return
        new_password = input("  Please input new password: ")
        confirm = input("  Confirm new password: ")
        if new_password != confirm:
            print("Passwords do not match.")
            return
        self.member_password = new_password
        save_members(members)
        print("Password changed successfully!")

    def to_dict(self):
        return {
            "name": self.member_name,
            "email": self.member_email,
            "password": self.member_password,
            "age": self.member_age,
            "gender": self.member_gender,
            "coupon": self.member_coupon,
            "point": self.member_point,
            "total_spending": self.member_total_spending,
        }

def create_member():
    print("Create Member:")
    name = input("  Name: ")
    while True:
        email = input(" Email: ")
        if any(m.member_email == email for m in members):
            print("Email already registered! Please enter a different email.")
        else:
            break
    while True:
        password = input("  Password: ")
        confirm_password = input("   Confirm Password: ")
        if password != confirm_password:
            print("Password not identical! Try again")
        else:
            break
    age = int(input("  Age: "))
    gender = input("  Gender: ")
    coupon = 0
    point = 0
    total_spending = 0

    new_member = member(name, email, password ,age, gender, coupon, point, total_spending)
    member_list.append(new_member)
    save_members(member_list)
    
def load_members():
    members = []
    try:
        with open(FILE_NAME1, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                members.append(
                    member(
                        item["name"],
                        item["email"],
                        item["password"],
                        item["age"],
                        item["gender"],
                        item["coupon"],
                        item["point"],
                        item["total_spending"],
                    )
                )
    except FileNotFoundError:
        print("Database file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")

    return members

def save_members(members):
    with open(FILE_NAME1, "w", encoding="utf-8") as file:
        json.dump([m.to_dict() for m in members], file, indent=4, ensure_ascii=False)

def check_data(email, password):
    for m in members:
        if m.member_email == email and m.member_password == password:
            return m
    return None
    
member_list = load_members()
members = member_list
