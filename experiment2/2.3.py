def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("请输入一个大于 2 的自然数："))
print("筛选法输出小于该数字的所有素数组成的列表：")
prime_set = set(i for i in range(2, n) if is_prime(i))
print(prime_set)

print("素数列表之和：" + str(sum(prime_set)))