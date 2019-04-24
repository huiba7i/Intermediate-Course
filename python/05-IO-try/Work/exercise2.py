"""
    写一个逐页显示文本文件的程序. 提示输入一个文件名,
    每次显示文本文件的 25 行, 暂停并向用户提示"按任意键继续.", 按键后继续执行
"""

user_input = input('请输入文件名，我们将逐页显示文件内容：\n')
user_input = user_input + '.txt'
row_number = 0
file = open(user_input, mode='r+', encoding='utf-8')

while True:
    info = file.readline()
    if info:
        row_number += 1
        print(info)
        if row_number == 25:
            input('按任意键继续...')
    else:
        break

file.close()