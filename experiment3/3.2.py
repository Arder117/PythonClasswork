# 编写程序，模拟抓狐狸⼩游戏。假设⼀共有⼀排5个洞口，小狐狸最开始的时候在其中⼀个洞口，然后玩家随机打开⼀个洞口，
# 如果里面有狐狸就抓到了。如果洞口⾥没有狐狸就第二天再来抓，但是第二天狐狸会在玩家来抓之前跳到隔壁洞口里。

import random

holes = [0, 0, 0, 0, 0, 0]
fox = random.randint(1, 5)
holes[fox] = 1
print("洞口情况：" + str(holes))
print("狐狸在第" + str(fox) + "个洞口。")

while True:
    hole = int(input("请输入要打开的洞口（1-5）："))
    if holes[hole] == 1:
        print("抓到了！")
        break
    else:
        print("没有抓到，狐狸跳到了隔壁洞口。")
        # 狐狸跳到隔壁洞口
        if fox == 1:
            holes[2] = 1
            fox = 2
            holes[1] = 0
        elif fox == 5:
            holes[4] = 1
            fox = 4
            holes[5] = 0
        else:
            if random.randint(0, 1) == 0:
                holes[fox - 1] = 1
                holes[fox] = 0
                fox -= 1
            else:
                holes[fox + 1] = 1
                holes[fox] = 0
                fox += 1
        print("洞口情况：" + str(holes))
        print("狐狸在第" + str(fox) + "个洞口。")
