"""
    Python 基础02
"""

# if else
# inp = int(input('请输入一个数字:'))
# if inp % 2 == 0:
#     print('偶数')
# else:
#     print('奇数')

# while
# n = 1
# line = 5
# while n <= line:
#     print(' '*(line-n), end='')
#     print('*'*((n-1)*2+1))
#     n += 1

# Function
# def defaultFun():
#     """
#     一、默认函数
#     :return: 无返回值
#     """
#     n = 1
#     line = 5
#     while n <= line:
#         print(' ' * (line - n), end='')
#         print('*' * ((n - 1) * 2 + 1))
#         n += 1
#
#
# defaultFun()

# def parametriceFun(num1, num2):
#     """
#     二、有参函数，计算和并返回结果
#     :param num1: 参数一
#     :param num2: 参数二
#     :return: 总和
#     """
#     return num1+num2
#
#
# p = parametriceFun(1, 30)
# print(p)


# def multipleValueFun(nums):
#     """
#     三、多个返回值函数，计算最大、最小值
#     :param nums: 传入的数据 List类型
#     :return: 返回结果 Tuple类型
#     """
#     max_num = nums[0]  # 最大值
#     min_num = nums[0]  # 最小值
#     for i in nums:
#         if i > max_num:
#             max_num = i
#         if i < min_num:
#             min_num = i
#     return min_num, max_num
#
#
# result = multipleValueFun([1, 2, 5, 10, -90, 100])
# print(result)


# def dog(keeper, name, age):
#     """
#     四、关键字参数
#     :param keeper: 饲养人
#     :param name: 姓名
#     :param age: 年龄
#     :return:
#     """
#     print("%s养了一条狗，它的名字叫做%s，它今年%d岁了" % (keeper, name, age))
#
#
# dog("小明", "考拉", 2)  # 按照参数位置调用
# dog("小明", age=3, name="考拉")  # 按照参数关键字传入参数


# def defaultValut(name, age=18, sex="男"):
#     """
#     五、默认值参数
#     :param name: 姓名
#     :param age: 年龄
#     :param sex: 性别
#     :return:
#     """
#     print("name =", name)
#     print("age =", age)
#     print("sex =", sex)
#
#
# defaultValut('小明', 222)


# def variableFun(*args, a):
#     """
#     六、可变参数
#     :param args: 元组接收多个参数
#     :param a: 关键字参数形式传入
#     :return:
#     """
#     print(args)
#     print(a)
#
#
# variableFun(1, 2, 3, 5, a=10)


# def dictionnariesFun(**kwargs):
#     """
#     七、字典参数，传入的参数以key=value形式传入
#     :param kwargs: 以字典对象接收所有的参数
#     :return:
#     """
#     print(kwargs)
#
#
# dictionnariesFun(name="Tom", age=19, sex="男")


# def hello(name):
#     print("hello,", name)
#
#
# def functionTransferFun(func, name):
#     """
#     八、函数传递
#     :param func: 调用函数
#     :param name: 传入参数
#     :return:
#     """
#     func(name)
#
#
# functionTransferFun(hello, 11111111)


# def closureFun():
#     """
#     九、嵌套函数（闭包）
#     :return:
#     """
#     num = 10
#
#     def inner():
#         return num + 10  # 使用了外部函数的局部变量num
#
#     return inner  # 将闭包返回
#
#
# inner = closureFun()  # 得到闭包函数对象
# print(inner())  # 调用闭包函数


# 十、匿名函数
# a = lambda x, y: x + y  # a相当于函数的名字
# print(a(1, 2))
#
#
# def test(func, x, y):
#     return func(x, y)
#
#
# resultTest = test(lambda x, y: x-y, 10, 20)
# print(resultTest)
