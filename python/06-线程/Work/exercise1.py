"""
创建一个函数，给出一个字符和一个文件名（作为参数或用户输入），然后显示文件中该字符出现的次数。
"""


def lookup(character, file_name):
    """
    查找文件中符出现的次数
    :param character: 需要查找的字符
    :param file_name: 需要查找的文件名
    :return: 返回字符出现的次数
    """
    file = open(file_name + '.txt', mode='r+', encoding='utf-8')
    number = 0
    n = 0

    while True:
        file_read = file.read(1)
        if file_read:
            if character == file_read:
                number += 1
        else:
            break

    return number


character = input('请输入需要查找的字符:')
file_name = input('请输入需要查找的文件名:')

l = lookup(character, file_name)
print('次数为%s' % l)
