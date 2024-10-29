# 假设⼀段楼梯共 15 个台阶，⼩明⼀步最多能上 3 个台阶。编写程序计算⼩明上这段楼 梯⼀共有多少种⽅法。要求给出递推法和递归法两种代码。

# 递归法
def climb_stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2) + climb_stairs(n - 3)

print("递归法：小明上这段楼梯一共有" + str(climb_stairs(15)) + "种方法。")

# 递推法
def climb_stairs1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        a, b, c = 1, 2, 4
        for i in range(4, n + 1):
            a, b, c = b, c, a + b + c
        return c

print("递推法：小明上这段楼梯一共有" + str(climb_stairs1(15)) + "种方法。")