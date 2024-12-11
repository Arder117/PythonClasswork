# 编写⼀个程序 demo.py，要求运⾏该程序后，⽣成 demo_new.py ⽂件，其中内容与demo.py ⼀样，只是在每⼀⾏的后⾯加上⾏号。                     #1
# 要求⾏号以#开始，并且所有⾏的#符号垂直对齐。                                                                      #2
                                                                                               #3
def add_line_number(filename):                                                                 #4
    with open(filename + '.py', 'r', encoding="UTF-8") as f:                                   #5
        lines = f.readlines()                                                                  #6
                                                                                               #7
    max_len = max([len(line) for line in lines])                                               #8
                                                                                               #9
    with open(filename + '_new.py', 'w', encoding="UTF-8") as f:                               #10
        for i, line in enumerate(lines):                                                       #11
            f.write(line.rstrip() + ' ' * (max_len - len(line) + 1) + '#' + str(i + 1) + '\n') #12
                                                                                               #13
                                                                                               #14
filename = '//experiment5/5.1'  #15
add_line_number(filename)                                                                      #16
