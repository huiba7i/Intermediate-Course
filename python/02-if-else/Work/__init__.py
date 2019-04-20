"""
    Python 基础二 作业
"""


# 1、输入一个正整数n，计算 1 + 1/2! +....+ 1/n!的值
def factorial(n):
    """
    计算阶乘
    :param n: 用户输入的数
    :return: 结果
    """
    s = 0
    sum = 1
    i = 1
    if n <= 0:
        return print('负数没有阶乘')
    else:
        while i <= n:
            sum = sum * i
            s += 1 / sum
            i += 1
    return  s


result = int(input('1、请输入一个数:'))
r = factorial(result)
print(r)


# 2、输入四个整数，输出其中的最小值
i = 1
nums = []
while ( i < 5 ):
    a = int(input('2、请依次输入四个整数第%d个:' % i))
    nums.append(a)
    i += 1

def max_minFun(nums):
    """
    三、多个返回值函数，计算最大、最小值
    :param nums: 传入的数据 List类型
    :return: 返回结果 Tuple类型
    """
    max_num = nums[0]  # 最大值
    min_num = nums[0]  # 最小值
    for i in nums:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    return min_num,max_num


min = max_minFun(nums)
print("最小值%s,最大值%s" %(min[0], min[1]))


# 3、输入一个长度为5的整型数组，求其中所有奇数的和
k = 0
intArr = []
while ( True ):
    k += 1
    nums = int(input('3、请依次整数第%d个:' % k))
    intArr.append(nums)
    if len(intArr) >= 5: break

k = 0
arrLen = len(intArr)
oddSum = 0
while ( k < arrLen ):
    if ( int(intArr[k]) % 2 != 0 ):
        oddSum += int(intArr[k])
    k += 1

print("奇数的和为%s" %oddSum)


# 4、计算x+y的值（依次输入数字x、运算符号（如+、-、*、/）、运算数字y
xyNum = 0
x = int(input('4、请输入X的值:'))
symbol = input('请输入运算符号:')
y = int(input('请输入Y的值:'))

if symbol == '+':
    xyNum = x + y
elif symbol == '-':
    xyNum = x - y
elif symbol == '*':
    xyNum = x * y
elif symbol == '/':
    xyNum = x / y
elif symbol == '%':
    xyNum = x % y

print('%s %s %s = %s' %(x, symbol, y, xyNum))

# 5、输出一张99乘法口诀表
print('5、输出一张99乘法口诀表')
row = 1
while (row <= 9):
    col = 1
    while (col <= row):
        print('%s×%s=%s' % (row, col, row * col), end=' ')
        col += 1
    print()
    row += 1

# 6、屏幕输入一个年份，判断是否为闰年
# 注意逻辑
year = int(input('6、请输入年份:'))
if (year % 4 == 0) and (year % 100 != 0) or ( year % 400 == 0 ):
    print('%s年是闰年' % year)
else:
    print('%s年不是闰年' % year)

# 7、屏幕输入一个正整数m，如果它是素数，输出”YES”，否则，输出”NO”（只能被自己和1整除的数为素数）
primeNumber = int(input('7、请输入一个正整数: '))


def isPrime(n):
    """
    屏幕输入一个正整数m，如果它是素数，输出”YES”，否则，输出”NO”（只能被自己和1整除的数为素数）
    :param n: 用户输入的数字
    :return: 是素数返回Yes，不是返回No
    """
    if n <= 1:
        return 'No'
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 'No'
        i += 1
    return 'Yes'


print(isPrime(primeNumber))

# 8、输入一个一维数字数组，输出数组中的最大值及下标
def findMax(mylist):
    """
    输入一个一维数字数组，输出数组中的最大值及下标
    :param mylist: list列表
    :return:  列表中最大的值 以及其索引  返回的是tuple类型的对象
    """

    size = len(mylist)
    i = 0
    max = i
    while i < size:
        if mylist[i] > mylist[max]:
            max = i
        i += 1

    return mylist[max], max

print('8、输入一个一维数字数组，输出数组中的最大值及下标')
print(findMax([1, 2, 8, 10, 20, 30, 0]))
