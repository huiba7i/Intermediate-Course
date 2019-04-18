# -*- coding: UTF-8 -*-
import math

# 一、输入两个实数，计算他们的和，差，积，商，然后输出
one = int(input('一、请输入第一个实数:'))
two = int(input('请输入第二个实数:'))

print('和:', one+two)
print('差:', one-two)
print('积:', one*two)
print('商:', one/two)

# 二、用户输入圆的半径，然后打印出该圆的直径、周长和面积
radius = float(input('二、请输入圆的半径:'))
print('直径:', radius*2)
print('周长:', (2*math.pi)*radius)
print('面积:', math.pi*(radius*2))

"""
三、输入一个四位数，按照以下方式加密输出
将该数每一位上的数字加9，然后除以10取余，作为该位上的新数字，最后将第1位和第3位上的数字互换，第2位和第4位上的数字互换
"""
n = input('三、请输入四位的数字:')
d = []
for digit in n:
    d.append(str((int(digit)+9) % 10))
print('取余后的数字:', d)

d[0], d[1], d[2], d[3] = d[2], d[3], d[0], d[1]
print('位置互换后:', d)
print(int(d[0])*1000+int(d[1])*100+int(d[2])*10+int(d[3]))

"""
四、编写一个应用程序，用户从键盘输入一个浮点数据，将该浮点数保留两位小数位输出
"""
num = float(input('四、请输入一个数字'))
sum = int(num*100)/100
print(sum)
