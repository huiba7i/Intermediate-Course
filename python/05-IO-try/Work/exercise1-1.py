"""
    提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.
    使用 file.readline()
"""

while True:
    try:
        row = int(input('请输入行数:'))
        name = input('请输入文件名:')
        file_name = name + '.txt'
        row_number = 0

        file = open(file_name, 'r+', encoding='utf-8')

        while True:
            read = file.read(1)
            if read:
                if read == '\n':
                    row_number += 1
            else:
                break

        if row > row_number:
            print('此文件没有 %s 行，请重新输入' % row)
            continue
        elif row < 0:
            print('不可以输入负数，请重新输入')
            continue

        file.seek(0, 0)
        for line in file.readlines()[0:row]:
            line = line.strip()
            print("读取的数据为: %s" % (line))

        file.close()

        break
    except (ValueError, NameError, FileNotFoundError):
        print('输入错误，请检查行数或文件名输入是否正确，再重新输入')




