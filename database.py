FILE_NAME1 = "member_data.txt"


# 建立檔案（如果不存在）
def init_database():
    try:
        open(FILE_NAME1, "x")  # x = 不存在才建立
        print("Database created.")
    except FileExistsError:
        pass

