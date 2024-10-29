# 输⼊两个集合 setA 和 setB，分别输出它们的交集、并集和差集 setA-setB。

# 输入时，集合元素之间用空格隔开，不含其他字符。

setA = set(input("请输入集合setA，用空格隔开：").split())
setB = set(input("请输入集合setB，用空格隔开：").split())

print("交集：" + str(setA & setB))
print("并集：" + str(setA | setB))
print("差集：" + str(setA - setB))