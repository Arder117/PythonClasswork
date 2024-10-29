# 编写程序，实现磁盘垃圾⽂件清理功能。要求程序运⾏时，通过命令⾏参数指定要清理的⽂件夹，
# 然后删除该⽂件夹及其⼦⽂件夹中所有扩展名为tmp、log、obj、txt以及⼤⼩为0的⽂件,但是不删除文件夹,并在删除前输出删除的文件名。

import os


def clean_folder(foldername):
    for root, dirs, files in os.walk(foldername): # 遍历文件夹，root为当前文件夹，dirs为当前文件夹下的子文件夹，files为当前文件夹下的文件
        for file in files: # 遍历当前文件夹下的文件
            if file.endswith('.tmp') or file.endswith('.log') or file.endswith('.obj') or file.endswith(
                    '.txt') or os.path.getsize(os.path.join(root, file)) == 0: # 判断文件是否符合要求，符合则删除
                print(f'Deleting {os.path.join(root, file)}') # 输出删除的文件名
                os.remove(os.path.join(root, file)) # 删除文件
        # 递归删除子文件夹的文件
        for dir in dirs: # 遍历子文件夹，递归删除子文件夹的文件
            clean_folder(os.path.join(root, dir))



if __name__ == '__main__':
    foldername = 'test'
    clean_folder(foldername)
