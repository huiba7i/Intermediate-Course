"""
    定义一系列的类，类用来封装和数据库对应的数据
    一个类对应一个数据库，类名和表名一致，类名是字母大写
    类中定义对象属性和表中的列相同
"""


class Login:
    def __init__(self, id, username, userpwd, usertel, usersex):
        """
            用户登录表
        :param id: 用户ID
        :param username: 用户姓名
        :param userpwd: 用户密码
        :param usertel: 用户联系方式
        :param usersex: 用户性别
        """
        self.id = id
        self.username = username
        self.userpwd = userpwd
        self.usertel = usertel
        self.usersex = usersex

    def __str__(self):
        return "{'id': %d, 'username': %s, 'userpwd': %s, 'usertel': %s, 'usersex': %s}" % (
            self.id, self.username, self.userpwd, self.usertel, self.usersex)


class User:
    def __init__(self, id, name, province, city, address, zip, date):
        """
            用户表
        :param id: 用户ID
        :param name: 用户姓名
        :param province: 用户所在省份
        :param city: 用户所在城市
        :param address: 用户所在地址
        :param zip: 用户所在地址邮编
        :param date: 用户出生日期
        """
        self.id = id
        self.name = name
        self.province = province
        self.city = city
        self.address = address
        self.zip = zip
        self.date = date

    def __str__(self):
        return "{'id': %d, 'name': %s, 'province': %s, 'city': %s, 'address': %s, 'zip': %s, 'data': %s}" % (
            self.id, self.name, self.province, self.city, self.address, self.zip, self.date)


class Backstage_login:
    """
        后台用户登录表
    """

    def __init__(self, id, name, pwd):
        self.id = id
        self.name = name
        self.pwd = pwd

    def __str__(self):
        return "{'id': %d, 'name': %s, 'pwd': %s}" % (self.id, self.name, self.pwd)
