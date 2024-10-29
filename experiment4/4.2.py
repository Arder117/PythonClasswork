# 编写程序，模拟打字练习程序的成绩评定。假设origin为原始内容，userInput为⽤户练习时输⼊的内容，要求⽤户输⼊的内容长度不能⼤于原始内容的长度，
# 如果对应位置的字符 ⼀致则认为正确，否则判定输⼊错误。最后成绩为:正确的字符数量/原始字符串长度，按百分制输出，要求保留 2 位⼩数。

import random

# 生成原始内容
origin = ''.join([chr(random.randint(20, 40)) for _ in range(100)])

# 生成用户输入
userInput = ''.join([chr(random.randint(20, 40)) for _ in range(100)])

# 计算正确的字符数量
correct = 0
for i in range(len(origin)):
    if origin[i] == userInput[i]:
        correct += 1

# 计算成绩
score = correct / len(origin) * 100
print('成绩：%.2f' % score)
