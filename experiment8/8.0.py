import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("科学计算器")
        self.geometry("400x600")

        self.expression = ""  # 用来存储当前输入的表达式
        self.result = tk.StringVar()  # 用来显示结果

        # 显示屏
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2, relief="solid", width=18, textvariable=self.result, justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        # 按钮定义
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('sqrt', 5, 2), ('^', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('ln', 7, 0), ('pi', 7, 1), ('e', 7, 2), ('C', 7, 3),
        ]

        # 为每个按钮创建并放置到 grid 中
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 14), width=6, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        """处理按钮点击事件"""
        if char == "=":
            try:
                # 计算表达式
                result = self.calculate_expression(self.expression)
                self.result.set(result)
                self.expression = str(result)
            except Exception as e:
                self.result.set("错误")
                self.expression = ""
        elif char == "C":
            # 清除显示屏
            self.expression = ""
            self.result.set("")
        else:
            # 更新表达式
            self.expression += str(char)
            self.result.set(self.expression)

    def calculate_expression(self, expr):
        """计算数学表达式"""
        expr = expr.replace("^", "**")  # 处理幂运算符
        expr = expr.replace("sqrt", "math.sqrt")  # 处理平方根
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("ln", "math.log")
        expr = expr.replace("pi", str(math.pi))
        expr = expr.replace("e", str(math.e))
        try:
            return eval(expr)  # 计算数学表达式
        except Exception:
            raise ValueError("无效的表达式")

# 运行程序
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
