# 编写程序，使⽤正则表达式查找txt⽂件中AABB形式的中文词语,形如整整齐齐,。

import re


def findAABB(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            pattern = re.compile(r'(\w)\1(\w)\2')
            result = pattern.findall(line)
            for i in result:
                tem = i[0] + i[0] + i[1] + i[1]
                print(tem)


filename = 'D:/Projects/PyCharmProject/classwork/experiment4/test'
findAABB(filename)
