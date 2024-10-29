# 假设某学校所有课程每学期允许多次考试，学⽣可随时参加考试，系统⾃动将每次成绩添加到Excel⽂件(包含 3 列:姓名，课程，成绩)中，
# 现期末要求统计所有学⽣每门课程的最⾼成绩。编写程序,模拟⽣成若⼲同学的成绩并写⼊ Excel ⽂件，其中学⽣姓名和课程名称均可重复，
# 也就是允许出现同⼀门课程的多次成绩，最后统计所有学⽣每门课程的最⾼成绩，并写⼊新的 Excel ⽂件。

import pandas as pd


# 生成数据,写入Excel文件
def generate_data(data):
    df = pd.DataFrame(data) # 生成DataFrame对象,
    df.to_excel('data.xlsx', index=False)


# 统计每门课程的最高成绩,写入Excel文件
def max_score(filename):
    df = pd.read_excel(filename)
    df = df.groupby(['姓名', '课程']).max().reset_index() # 按姓名和课程分组,取最大值,重置索引
    df.to_excel('max_score.xlsx', index=False)


data = {
    '姓名': ['张三', '李四', '王五', '张三', '李四', '王五', '张三', '李四', '王五','张三'],
    '课程': ['语文', '语文', '语文', '数学', '数学', '数学', '英语', '英语', '英语','数学'],
    '成绩': [80, 90, 85, 85, 95, 90, 90, 85, 95, 100]
}
generate_data(data)
print('数据生成完成')
max_score('data.xlsx')
print('最高成绩统计完成')
