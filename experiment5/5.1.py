# 编写⼀个程序 demo.py，要求运⾏该程序后，⽣成 demo_new.py ⽂件，其中内容与demo.py ⼀样，只是在每⼀⾏的后⾯加上⾏号。
# 要求⾏号以#开始，并且所有⾏的#符号垂直对齐。

def add_line_number(filename):
    with open(filename + '.py', 'r', encoding="UTF-8") as f:
        lines = f.readlines()

    max_len = max([len(line) for line in lines])

    with open(filename + '_new.py', 'w', encoding="UTF-8") as f:
        for i, line in enumerate(lines):
            f.write(line.rstrip() + ' ' * (max_len - len(line) + 1) + '#' + str(i + 1) + '\n')


filename = '//experiment5/5.1'
add_line_number(filename)
