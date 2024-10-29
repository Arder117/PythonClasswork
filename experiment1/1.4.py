# 1.4 输⼊⼀个⾃然数，输出它的⼆进制、⼋进制、⼗六进制表⽰形式

def base_conversion(n):
    print("二进制：" + bin(n))
    print("八进制：" + oct(n))
    print("十六进制：" + hex(n))


base_conversion(int(input("请输入一个自然数：")))
