"""
    银行类
"""
import Account

name = 'Bank'

class Bank:
    """
        银行类
    """
    def __init__(self, accounts):
        """
            初始化银行类属性
        :param accounts: 所有的账户信息
        """
        self.accounts = accounts
        self.accounts = []



    def add_account(self, account):
        """
            新增银行卡功能
        :param account: 新增银行卡的所有信息
        :return: 返回新增银行卡的信息
        """
        self.accounts.append(account)
        return self.accounts

    def remove_account(self, account):
        """
            删除银行卡功能，需要验证
        :param account: 删除银行卡信息
        :return: 返回已删除信息
        """
        pass


    def select(self, card, password):
        """
            根据卡号和密码查询银行卡信息
        :param card: 需要查询的卡号
        :param password: 需要查询的卡号密码
        :return: 返回查询到的信息
        """
        pass


    def select_card(self, card):
        """
            根据卡号查询银行卡信息
        :param card: 需要查询的银行卡信息
        :return: 返回查询到的信息
        """
        pass