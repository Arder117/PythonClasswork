# 编写程序，读取 Word ⽂件中的所有⽂本，然后输出其中所有红⾊的⽂本和加粗的⽂本以及同时具有这两种属性的⽂本。

import docx


def get_bold_red_text(filename, red_text, bold_text, bold_red_text, ):
    doc = docx.Document(filename)
    for para in doc.paragraphs:
        for run in para.runs:
            if run.bold and run.font.color.rgb == docx.shared.RGBColor(255, 0, 0):
                bold_red_text.append(run.text)
            elif run.bold:
                bold_text.append(run.text)
            elif run.font.color.rgb == docx.shared.RGBColor(255, 0, 0):
                red_text.append(run.text)


if __name__ == '__main__':
    filename = "test.docx"
    red_text = []
    bold_text = []
    bold_red_text = []
    get_bold_red_text(filename, red_text, bold_text, bold_red_text)
    print("红色文本：")
    for text in red_text:
        print(text)
    print("加粗文本：")
    for text in bold_text:
        print(text)
    print("红色加粗文本：")
    for text in bold_red_text:
        print(text)
