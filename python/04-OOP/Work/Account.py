"""
    银行账户类
"""
name = 'Account'

class Account:
    """
        银行账户类
    """
    def __init__(self, card, password, name, money):
        """
            银行账户类，初始化属性
        :param card: 卡号
        :param password: 密码
        :param name: 姓名
        :param money: 账户金额，默认为0
        """
        self.card = card
        self.password = password
        self.name = name
        self.money = money
        self.money = 0.0


    def in_money(self, money):
        """
            存钱方法
        :param money: 需要存入的金额
        :return: 返回结果
        """
        self.money + float(money)
        return  "存钱成功，账户余额:%.2f" % self.money


    def out_money(self, money):
        """
            取钱方法
        :param money: 需要取出的金额
        :return:  返回结果
        """
        if ( self.money -money ) < 0:
            return  "账户余额不足"
        else:
            self.money -= money
            return "取钱成功，账户余额:%.2f" % self.money

