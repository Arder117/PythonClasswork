# 编写程序，⽣成 50 个 Excel ⽂件，每个⽂件中包含 5 列数据，其中每个单元格内的内容随机⽣成，并且每个 Excel ⽂件的数据⾏数不相同。
# 然后创建⼀个 SQLite 数据库，其结构与 Excel ⽂件相符合，最后把前⾯⽣成的 50 个 Excel ⽂件中的数据导⼊到这个数据库中

import os
import random
import sqlite3
import string

import pandas as pd


# 生成随机字符串
def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


# 生成随机数据
def generate_random_data(num_rows):
    data = {
        'Column1': [random_string() for _ in range(num_rows)],
        'Column2': [random.randint(1, 100) for _ in range(num_rows)],
        'Column3': [random.uniform(1.0, 100.0) for _ in range(num_rows)],
        'Column4': [random.choice(['A', 'B', 'C', 'D']) for _ in range(num_rows)],
        'Column5': [random_string(5) for _ in range(num_rows)],
    }
    return pd.DataFrame(data)


# 创建 Excel 文件
def create_excel_files(num_files=50):
    for i in range(num_files):
        num_rows = random.randint(5, 20)  # 每个文件的行数在5到20之间
        df = generate_random_data(num_rows)
        df.to_excel(f'file_{i + 1}.xlsx', index=False)


# 创建 SQLite 数据库
def create_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS data (
            Column1 TEXT,
            Column2 INTEGER,
            Column3 REAL,
            Column4 TEXT,
            Column5 TEXT
        )
    ''')
    conn.commit()
    return conn


# 导入 Excel 数据到 SQLite
def import_excel_to_db(conn):
    for i in range(50):
        df = pd.read_excel(f'file_{i + 1}.xlsx')
        df.to_sql('data', conn, if_exists='append', index=False)


# 主程序
if __name__ == "__main__":
    # 确保输出目录存在
    if not os.path.exists('excel_files'):
        os.makedirs('excel_files')

    # 设置工作目录
    os.chdir('excel_files')

    # 创建 Excel 文件
    create_excel_files()

    # 创建数据库并导入数据
    conn = create_database()
    import_excel_to_db(conn)

    # 关闭数据库连接
    conn.close()

    print("Excel 文件生成及数据导入完成！")
