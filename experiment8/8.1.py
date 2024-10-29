import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("科学计算器")
        self.geometry("400x700")

        # 当前输入的表达式和结果显示
        self.expression = ""
        self.result = tk.StringVar()

        # 默认角度模式：弧度
        self.angle_mode = "radian"

        # 创建显示屏
        self.create_display()

        # 创建按钮
        self.create_buttons()

        # 绑定键盘事件
        self.bind_keys()

    def create_display(self):
        """创建显示屏"""
        display_frame = tk.Frame(self)
        display_frame.pack(expand=True, fill="both")

        # 输入和结果显示
        self.display = tk.Entry(display_frame, font=("Arial", 20), textvariable=self.result, justify="right", bd=5, relief="ridge")
        self.display.pack(expand=True, fill="both")

    def create_buttons(self):
        """创建按钮"""
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True, fill="both")

        # 按钮布局
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('sinh', 7, 0), ('cosh', 7, 1), ('tanh', 7, 2), ('sqrt', 7, 3),
            ('pi', 8, 0), ('e', 8, 1), ('|x|', 8, 2), ('fact', 8, 3),
            ('Rad/Deg', 9, 0), ('ln', 9, 1), ('%', 9, 2), ('DEL', 9, 3)
        ]

        # 动态创建按钮
        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=("Arial", 14), width=6, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def bind_keys(self):
        """绑定键盘事件"""
        self.bind("<Key>", self.on_key_press)

    def on_key_press(self, event):
        """处理键盘输入"""
        key = event.keysym.lower()

        # 数字和运算符映射
        if key in "0123456789":
            self.on_button_click(key)
        elif key in "+-*/^":
            self.on_button_click(key)
        elif key == "equal":
            self.on_button_click("=")
        elif key == "backspace":
            self.on_button_click("DEL")
        elif key == "return":  # 回车键
            self.on_button_click("=")
        elif key == "c":
            self.on_button_click("C")
        elif key == "period":
            self.on_button_click(".")
        elif key == "parenleft":
            self.on_button_click("(")
        elif key == "parenright":
            self.on_button_click(")")
        elif key == "r":
            self.on_button_click("Rad/Deg")
        elif key == "s":
            if event.char.lower() == "s":
                self.on_button_click("sin")
        elif key == "l":
            if event.char.lower() == "l":
                self.on_button_click("log")
        elif key == "f":
            self.on_button_click("fact")
        elif key == "t":
            self.on_button_click("tan")

    def on_button_click(self, char):
        """处理按钮点击事件"""
        if char == "=":
            self.calculate_result()
        elif char == "C":
            self.expression = ""
            self.result.set("")
        elif char == "DEL":
            self.expression = self.expression[:-1]
            self.result.set(self.expression)
        elif char == "Rad/Deg":
            self.toggle_angle_mode()
        else:
            self.expression += str(char)
            self.result.set(self.expression)

    def toggle_angle_mode(self):
        """切换角度和弧度模式"""
        if self.angle_mode == "radian":
            self.angle_mode = "degree"
        else:
            self.angle_mode = "radian"
        self.result.set(f"模式: {self.angle_mode}")

    def calculate_result(self):
        """计算表达式结果"""
        try:
            # 替换表达式中的科学运算符
            expr = self.expression.replace("^", "**")
            expr = expr.replace("sqrt", "math.sqrt")
            expr = expr.replace("sin", f"math.sin" if self.angle_mode == "radian" else "math.sin(math.radians")
            expr = expr.replace("cos", f"math.cos" if self.angle_mode == "radian" else "math.cos(math.radians")
            expr = expr.replace("tan", f"math.tan" if self.angle_mode == "radian" else "math.tan(math.radians")
            expr = expr.replace("sinh", "math.sinh")
            expr = expr.replace("cosh", "math.cosh")
            expr = expr.replace("tanh", "math.tanh")
            expr = expr.replace("log", "math.log10")
            expr = expr.replace("ln", "math.log")
            expr = expr.replace("pi", str(math.pi))
            expr = expr.replace("e", str(math.e))
            expr = expr.replace("fact", "math.factorial")
            expr = expr.replace("|x|", "abs")

            # 计算表达式
            result = eval(expr)
            self.result.set(result)
            self.expression = str(result)
        except Exception as e:
            self.result.set("错误")
            self.expression = ""

# 运行程序
if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
