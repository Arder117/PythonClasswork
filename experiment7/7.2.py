# 运⾏下⾯的程序，在当前⽂件夹中⽣成饭店营业额模拟数据⽂件data.csv。

import csv
import random
import datetime

fn = 'data.csv'
with open(fn, 'w', encoding='UTF-8') as fp:
    # 创建 csv 文件写入对象
    wr = csv.writer(fp)
    # 写入表头
    wr.writerow(['日期', '销量'])
    # 生成模拟数据
    startDate = datetime.date(2017, 1, 1)
    # 生成 365 个模拟数据，可以根据需要进行调整
    for i in range(365):
        # 生成一个模拟数据，写入 csv 文件
        amount = 300 + i * 5 + random.randrange(100)
        wr.writerow([str(startDate), amount])
        # 下一天
        startDate = startDate + datetime.timedelta(days=1)

import pandas as pd
from matplotlib import pyplot as plt

from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

# 1)使⽤ pandas读取⽂件data.csv中的数据，创建DataFrame对象，并删除其中所有缺失值;

df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df)

# 2)使⽤ matplotlib ⽣成折线图，反应该饭店每天的营业额情况，并把图形保存为本地⽂件first.jpg;
plt.plot(df['日期'], df['销量'])

data = df['日期'].str.split('-', expand=True)
df['日期'] = data[1] + '-' + data[2]
plt.xticks(range(0, len(df), 30), df['日期'][::30])

plt.xlabel('日期',loc='right')
plt.ylabel('销量',loc='top')
plt.savefig('first.jpg')

# 3)按⽉份进⾏统计，使⽤matplotlib绘制柱状图显⽰每个⽉份的营业额，并把图形按⽉份进⾏统计，找出相邻两个⽉最⼤涨幅，并把涨幅最⼤的⽉份写⼊⽂件maxMonth.txt;
plt.clf()
df = pd.read_csv('data.csv')
df.dropna(inplace=True)
df['日期'] = pd.to_datetime(df['日期'])
df['月份'] = df['日期'].dt.month
monthly_sales = df.groupby('月份')['销量'].sum()
plt.bar(monthly_sales.index, monthly_sales.values)
plt.xticks(monthly_sales.index)
plt.xlabel('月份',loc='right')
plt.ylabel('销量',loc='top')
plt.savefig('second.jpg')

max_increase = 0
max_month = None
monthly_sales[0] = 0
for i in range(2, 12):
    increase = monthly_sales[i] - monthly_sales[i - 1]
    if increase > max_increase:
        max_increase = increase
        max_month = i
with open('maxMonth.txt', 'w') as f:
    f.write(str(max_month))


# 4)按季度统计该饭店2017年的营业额数据，使⽤ matplotlib ⽣成饼状图显⽰ 2017 年4个季度的营业额分布情况，并把图形保存为本地⽂件third.jpg。
plt.clf()
df['日期'] = pd.to_datetime(df['日期'])
df['月份'] = df['日期'].dt.month
df['季度'] = df['月份'].apply(lambda x: (x - 1) // 3 + 1)
quarterly_sales = df.groupby('季度')['销量'].sum()
plt.pie(quarterly_sales, labels=['第一季度', '第二季度', '第三季度', '第四季度'], autopct='%1.1f%%')
plt.savefig('third.jpg')



