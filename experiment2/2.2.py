# 输⼊⼀个⼤于 2 的⾃然数，然后⽤筛选法输出⼩于该数字的所有素数组成的列表(⽤迭代器和列表推导式)。求素数列表之和（⽤⽣成器表达式),


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("请输入一个大于 2 的自然数："))
print("筛选法输出小于该数字的所有素数组成的列表：")

# 用迭代器
prime_list = filter(is_prime, range(2, n))
print("迭代器：")
print(list(prime_list))

# 用列表推导式
prime_list = [i for i in range(2, n) if is_prime(i)] #
print("列表推导式：")
print(prime_list)

# 求素数列表之和
print("素数列表之和：" + str(sum(i for i in range(2, n) if is_prime(i))))


