# 1.3 输⼊任意⼤的⾃然数，输出各位数字之和。

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


print("各位数字累加和为：" + str(sum_digits(int(input("请输入一个自然数：")))))