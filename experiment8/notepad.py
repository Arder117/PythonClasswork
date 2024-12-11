import sys
from PyQt5.QtGui import QFont, QTextDocument
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QMenuBar, QMenu, QAction, QStatusBar, \
    QFileDialog, QFontDialog, QMessageBox, QLineEdit, QDialog, QVBoxLayout, QPushButton, QRadioButton


class Notepad(QMainWindow):

    # 初始化
    def __init__(self):
        super().__init__()

        self.upRadioButton = None
        self.replaceLabel = None
        self.replaceDialog = None
        self.downRadioButton = None
        self.findLabel = None
        self.findDialog = None
        self.menuBar = None
        self.statusBar = None
        self.plainTextEdit = None
        self.openFileName = '无标题.txt'
        self.isSaved = False
        self.font = QFont("宋体", 12)

        self.initializeUI()

    # 初始化界面
    def initializeUI(self):
        self.setWindowTitle("简易记事本")
        self.setGeometry(500, 400, 1600, 900)

        # 创建中央文本编辑器
        self.plainTextEdit = QPlainTextEdit(self)
        self.setCentralWidget(self.plainTextEdit)
        self.plainTextEdit.setFont(self.font)

        # 状态栏
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # 显示光标位置
        self.plainTextEdit.cursorPositionChanged.connect(self.updateCursorPosition)

        # 创建菜单
        self.menuBar = self.createMenuBar()
        self.setMenuBar(self.menuBar)

        self.show()

    # 创建菜单栏
    def createMenuBar(self):
        menu_bar = QMenuBar(self)

        # 创建文件菜单
        menu_file = QMenu("文件(&F)", self)
        self.createFileMenuActions(menu_file)
        menu_bar.addMenu(menu_file)

        # 创建编辑菜单
        menu_edit = QMenu("编辑(&E)", self)
        self.createEditMenuActions(menu_edit)
        menu_bar.addMenu(menu_edit)

        # 创建格式菜单
        menu_format = QMenu("格式(&O)", self)
        self.createFormatMenuActions(menu_format)
        menu_bar.addMenu(menu_format)

        return menu_bar

    # 创建文件菜单操作
    def createFileMenuActions(self, menu_file):
        # 新建文件
        menu_new = QAction("新建(&N)", self)
        menu_new.setShortcut("Ctrl+N")
        menu_new.triggered.connect(self.newFile)
        menu_file.addAction(menu_new)

        # 打开文件
        menu_open = QAction("打开(&O)", self)
        menu_open.setShortcut("Ctrl+O")
        menu_open.triggered.connect(self.openFile)
        menu_file.addAction(menu_open)

        # 保存文件
        menu_save = QAction("保存(&S)", self)
        menu_save.setShortcut("Ctrl+S")
        menu_save.triggered.connect(self.saveFile)
        menu_file.addAction(menu_save)

        # 另存为
        menu_save_as = QAction("另存为(&A)", self)
        menu_save_as.triggered.connect(self.saveAsFile)
        menu_file.addAction(menu_save_as)

        # 退出
        menu_exit = QAction("退出(&X)", self)
        menu_exit.triggered.connect(self.exit)
        menu_file.addAction(menu_exit)

    # 创建编辑菜单操作
    def createEditMenuActions(self, menu_edit):
        # 撤销
        menu_undo = QAction("撤销(&U)", self)
        menu_undo.setShortcut("Ctrl+Z")
        menu_undo.triggered.connect(self.undo)
        menu_edit.addAction(menu_undo)

        # 剪切
        menu_cut = QAction("剪切(&T)", self)
        menu_cut.setShortcut("Ctrl+X")
        menu_cut.triggered.connect(self.cut)
        menu_edit.addAction(menu_cut)

        # 复制
        menu_copy = QAction("复制(&C)", self)
        menu_copy.setShortcut("Ctrl+C")
        menu_copy.triggered.connect(self.copy)
        menu_edit.addAction(menu_copy)

        # 粘贴
        menu_paste = QAction("粘贴(&P)", self)
        menu_paste.setShortcut("Ctrl+V")
        menu_paste.triggered.connect(self.paste)
        menu_edit.addAction(menu_paste)

        # 查找
        menu_find = QAction("查找(&F)", self)
        menu_find.setShortcut("Ctrl+F")
        menu_find.triggered.connect(self.find)
        menu_edit.addAction(menu_find)

        # 替换
        menu_replace = QAction("替换(&R)", self)
        menu_replace.setShortcut("Ctrl+H")
        menu_replace.triggered.connect(self.replace)
        menu_edit.addAction(menu_replace)

    # 创建格式菜单操作
    def createFormatMenuActions(self, menu_format):
        # 设置字体
        menu_font = QAction("字体(&F)", self)
        menu_font.triggered.connect(self.changeFont)
        menu_format.addAction(menu_font)

    # 新建文件
    def newFile(self):
        if not self.isSaved:
            result = QMessageBox.question(self, "新建文件", "文件未保存，是否保存？",
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if result == QMessageBox.Yes:
                self.saveFile()
            elif result == QMessageBox.Cancel:
                return
        self.plainTextEdit.clear()
        self.setWindowTitle("无标题.txt - 简易记事本")
        self.isSaved = False

    # 打开文件
    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                self.plainTextEdit.setPlainText(file.read())
            self.setWindowTitle(f"{filename} - 简易记事本")
            self.isSaved = True

    # 保存文件
    def saveFile(self):
        if self.openFileName == '无标题.txt':
            self.saveAsFile()
        else:
            with open(self.openFileName, 'w', encoding='utf-8') as file:
                file.write(self.plainTextEdit.toPlainText())
            self.setWindowTitle(f"{self.openFileName} - 简易记事本")
            self.isSaved = True

    # 另存为
    def saveAsFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, "另存为", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            self.openFileName = filename
            self.saveFile()

    # 退出
    def exit(self):
        if not self.isSaved:
            result = QMessageBox.question(self, "退出", "文件未保存，是否退出？",
                                          QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                QApplication.quit()
        else:
            QApplication.quit()

    # 撤销
    def undo(self):
        self.plainTextEdit.undo()

    # 剪切
    def cut(self):
        self.plainTextEdit.cut()

    # 复制
    def copy(self):
        self.plainTextEdit.copy()

    # 粘贴
    def paste(self):
        self.plainTextEdit.paste()

    # 设置字体
    def changeFont(self):
        font, ok = QFontDialog.getFont(self.font, self)
        if ok:
            self.font = font
            self.plainTextEdit.setFont(self.font)

    # 查找
    def find(self):
        self.findDialog = QDialog(self)
        self.findDialog.setWindowTitle("查找")

        layout = QVBoxLayout(self.findDialog)
        self.findLabel = QLineEdit(self.findDialog)
        self.findLabel.setPlaceholderText("查找内容")
        layout.addWidget(self.findLabel)

        self.upRadioButton = QRadioButton("向上查找", self.findDialog)
        layout.addWidget(self.upRadioButton)

        self.downRadioButton = QRadioButton("向下查找", self.findDialog)
        layout.addWidget(self.downRadioButton)

        find_button = QPushButton("查找", self.findDialog)
        layout.addWidget(find_button)

        find_button.clicked.connect(self.findClicked)
        self.findDialog.setLayout(layout)

        self.findDialog.exec_()

    # 查找按钮点击事件
    def findClicked(self):
        text = self.findLabel.text()
        direction = "down" if self.downRadioButton.isChecked() else "up"
        self.findText(text, direction)

    # 查找文本
    def findText(self, text, direction):
        cursor = self.plainTextEdit.textCursor()
        document = self.plainTextEdit.document()

        if direction == "down":
            cursor = document.find(text, cursor)
        elif direction == "up":
            cursor = document.find(text, cursor, QTextDocument.FindBackward)

        if cursor.isNull():
            QMessageBox.information(self, "查找", "没有找到匹配的文本！")
        else:
            self.plainTextEdit.setTextCursor(cursor)

    # 替换
    def replace(self):
        self.replaceDialog = QDialog(self)
        self.replaceDialog.setWindowTitle("替换")

        layout = QVBoxLayout(self.replaceDialog)

        self.findLabel = QLineEdit(self.replaceDialog)
        self.findLabel.setPlaceholderText("查找内容")
        layout.addWidget(self.findLabel)

        self.replaceLabel = QLineEdit(self.replaceDialog)
        self.replaceLabel.setPlaceholderText("替换为")
        layout.addWidget(self.replaceLabel)

        self.upRadioButton = QRadioButton("向上查找", self.replaceDialog)
        layout.addWidget(self.upRadioButton)

        self.downRadioButton = QRadioButton("向下查找", self.replaceDialog)
        layout.addWidget(self.downRadioButton)

        find_button = QPushButton("查找", self.replaceDialog)
        layout.addWidget(find_button)

        replace_button = QPushButton("替换", self.replaceDialog)
        layout.addWidget(replace_button)

        find_button.clicked.connect(self.findClicked)
        replace_button.clicked.connect(self.replaceClicked)

        self.replaceDialog.setLayout(layout)

        self.replaceDialog.exec_()

    # 替换按钮点击事件
    def replaceClicked(self):
        find_text = self.findLabel.text()
        replace_text = self.replaceLabel.text()
        direction = "down" if self.downRadioButton.isChecked() else "up"
        self.replaceText(find_text, replace_text, direction)

    # 替换文本
    def replaceText(self, find_text, replace_text, direction):
        cursor = self.plainTextEdit.textCursor()
        document = self.plainTextEdit.document()

        if direction == "down":
            cursor = document.find(find_text, cursor)
        elif direction == "up":
            cursor = document.find(find_text, cursor, QTextDocument.FindBackward)

        if not cursor.isNull():
            cursor.insertText(replace_text)
            self.plainTextEdit.setTextCursor(cursor)
        else:
            QMessageBox.information(self, "替换", "没有找到匹配的文本！")

    # 更新光标位置
    def updateCursorPosition(self):
        cursor = self.plainTextEdit.textCursor()
        line = cursor.blockNumber() + 1
        column = cursor.columnNumber() + 1
        self.statusBar.showMessage(f"行: {line} 列: {column}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notepad()
    window.show()
    sys.exit(app.exec_())
