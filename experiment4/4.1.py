# 编写程序，要求输⼊⼀个字符串，然后输⼊⼀个整数作为凯撒加密算法的密钥，然后输出该字符串加密后的结果。

def caesar_cipher(s, key):
    result = ''
    for i in s:
        if i.isalpha():
            if i.islower():
                result += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
            else:
                result += chr((ord(i) - ord('A') + key) % 26 + ord('A'))
        else:
            result += i
    return result

s = input('请输入字符串：')
key = int(input('请输入密钥：'))
print('加密后的结果：' + caesar_cipher(s, key))
