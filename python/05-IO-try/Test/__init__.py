"""
    IO
"""
f = open('1.txt', encoding='utf8')
# print('全部', f.read())  # 打开全部内容
# print('指定字节', f.read(10))  # 打开10个字节内容
print('第一行', f.readlines(1))  # 打开第一行内容
