FILE_NAMES = [
    "member_data.json",
    "inventory_data.json",
]

# 建立檔案（如果不存在）
def init_database():
    import json
    for filename in FILE_NAMES:
        try:
            with open(filename, "x", encoding="utf-8") as f:
                json.dump([], f, indent=4)
            print(f"Created {filename}.")
        except FileExistsError:
            pass

