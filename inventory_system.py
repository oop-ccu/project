FILE_NAME2 = 'inventory_data.json'
import json

class item:
    def __init__(self, name, quanity, value, date):
        self.item_name = name
        self.item_quanity = quanity
        self.item_value = value
        self.item_total_value = quanity * value
        self.item_date = date

    def check_info(self):
        print("Item information:")
        print("  Name: {}".format(self.item_name))
        print("  Quantity: {}".format(self.item_quanity))
        print("  Value: {}".format(self.item_value))
        print("  Total Value: {}".format(self.item_total_value))
        print("  Date: {}".format(self.item_date))

    def change_info(self):
        print("Change item information:")
        self.item_name = input("  New Name: ")
        self.item_quanity = int(input("  New Quantity: "))
        self.item_value = float(input("  New Value: "))
        self.item_total_value = self.item_quanity * self.item_value  # Recalculate total value
        self.item_date = input("  New Date: ")
        print("Item information updated successfully!")

    def to_dict(self):
        return {
            "name": self.item_name,
            "quantity": self.item_quanity,
            "value": self.item_value,
            "total_value": self.item_total_value,
            "date": self.item_date,
        }

def add_item():
    print("Add Item:")
    name = input("  Name: ")
    quantity = int(input("  Quantity: "))
    value = float(input("  Value: "))
    date = input("  Date: ")
    
    new_item = item(name, quantity, value, date)
    item_list.append(new_item)
    save_items(item_list)
    print("Item added successfully!")

def load_items():
    items = []
    try:
        with open(FILE_NAME2, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item_data in data:
                items.append(
                    item(
                        item_data["name"],
                        item_data["quantity"],
                        item_data["value"],
                        item_data["date"],
                    )
                )
    except FileNotFoundError:
        print("Inventory database file not found.")
    except json.JSONDecodeError:
        print("Error decoding inventory JSON file.")

    return items

def save_items(items):
    with open(FILE_NAME2, "w", encoding="utf-8") as file:
        json.dump([i.to_dict() for i in items], file, indent=4, ensure_ascii=False)

# Initialize item list
item_list = load_items()
items = item_list