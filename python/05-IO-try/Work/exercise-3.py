"""
    写一个比较两个文本文件的程序. 如果不同, 给出第一个不同处的行号和列号
"""

def compare_file(file_name1, file_name2):
    """
        比较不同之处
    :param file_name1: 文件一
    :param file_name2: 文件二
    :return: 返回不同之处的行号和列好
    """
    file1 = open(file_name1+'.txt', mode='r+', encoding='utf-8')
    file2 = open(file_name2 + '.txt', mode='r+', encoding='utf-8')

    row_number = 1
    col_number = 0

    while True:
        file1_read = file1.read(1)
        file2_read = file2.read(1)
        if file1_read:
            if file1_read == '\n':
                row_number += 1

            if file1_read != file2_read:
                col_number = file1.tell()
                return row_number, col_number
        else:
            return None


file1 = input('请输入第一个文件名:')
file2 = input('请输入第二个文件名:')
c = compare_file(file1, file2)

print('不同处行号:%s,列号:%s' %(c[0], c[1]))