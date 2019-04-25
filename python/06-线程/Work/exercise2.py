"""
假设有5个文件，请使用5个线程统计所有的文件中包含的指定字符的个数。
"""
from exercise1 import lookup
import threading

class tatal_number(threading.Thread):

    def __init__(self, character, file_name):
        threading.Thread.__init__(self)
        self.character = character
        self.file_name = file_name

    def run(self):
        sum = lookup(self.character, self.file_name)
        self.sum = sum


i = 1
ts = []
inp = input('请输入需要查找的字符')
while i <= 5:
    s = tatal_number(inp, str(i))
    i += 1
    ts.append(s)

for t in ts:
    t.start()

for t in ts:
    t.join()

sum = 0
for t in ts:
    sum += t.sum

print('总共出现次数为%s' % sum)