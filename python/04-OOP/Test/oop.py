"""
    OOP
"""


class Student:
    """
        创建学生类
    """
    # 使用 __init__ 创建对象属性
    def __init__(self, name, sex, age, phone):
        """
        初始化对象属性
        :param name: 姓名
        :param sex: 性别
        :param age: 年龄
        """
        self.name = name
        self.sex = sex
        self.age = age
        self.phone = phone


    # 创建方法
    def info(self):
        """
            个人信息
        :return: 返回个人信息方法
        """
        return print(self.name, '是一位', self.sex, '生，今年', self.age, '岁了！', self.phone  )


class Phone():
    """
        创建电话类
    """
    def __init__(self, color, model):
        """
            初始化电话类属性
        :param color: 电话颜色
        :param model: 电话型号
        """
        self.color = color
        self.model = model


    def call(self):
        """
            打电话方法
        :return: 返回打电话信息
        """
        return print('在使用%s色的%s手机在打电话' %(self.color, self.model))



phone = Phone('红', '小米')
s1 = Student('小明', '男', 12, phone)
s1.info()