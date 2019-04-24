"""
    提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.
    使用 file.readlines()
"""

while True:
    try:
        row = int(input('请输入行数:'))
        name = input('请输入文件名:')
        file_name = name + '.txt'

        file = open(file_name, 'r+', encoding='utf-8')

        l = len(file.readlines())
        if row > l:
            print('此文件没有 %s 行，请重新输入' % row)
            continue
        elif row < 0:
            print('不可以输入负数，请重新输入')
            continue

        break
    except (ValueError, NameError, FileNotFoundError):
        print('输入错误，请检查行数或文件名输入是否正确，再重新输入')

file.seek(0, 0)  # 在读取文件中，读取文件后“光标”会保留在末尾，在后面再次需要读取文件时，注意移动光标
for line in file.readlines()[0:row]:
    line = line.strip()
    print("读取的数据为: %s" % (line))

file.close()
