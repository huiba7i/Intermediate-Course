"""
    1.开户 2.存钱 3.取钱 4.查询 5.销户 6.退出
"""


# import Bank     # 导入银行模块
# import Account  # 导入账户模块

class Account:
    """
        银行账户类
    """

    def __init__(self, card, password, name):
        """
            银行账户类，初始化属性
        :param card: 卡号
        :param password: 密码
        :param name: 姓名
        """
        self.card = card
        self.password = password
        self.name = name
        self.money = 0.0

    def in_money(self, m):
        """
            存钱方法
        :param m: 需要存入的金额
        :return: 返回结果
        """
        self.money += m
        return "存钱成功，账户余额:%.2f" % self.money

    def out_money(self, money):
        """
            取钱方法
        :param money: 需要取出的金额
        :return:  返回结果
        """
        if (self.money - money) < 0:
            return "账户余额不足"
        else:
            self.money -= money
            return "取钱成功，账户余额:%.2f" % self.money


class Bank:
    """
        银行类
    """

    def __init__(self):
        """
            初始化银行类属性
        :param accounts: 所有的账户信息
        """
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
        if account.money > 0:
            return '%s 账户有余额，不能销户' % account.name
        else:
            self.accounts.remove(account)
            return '%s 已销户' % account.name

    def select(self, card, password):
        """
            根据卡号和密码查询银行卡信息
        :param card: 需要查询的卡号
        :param password: 需要查询的卡号密码
        :return: 返回查询到的信息
        """
        for acc in self.accounts:
            if card == acc.card and password == acc.password:
                return acc
        return None

    def select_card(self, card):
        """
            根据卡号查询银行卡信息
        :param card: 需要查询的银行卡信息
        :return: 返回查询到的信息
        """
        for acc in self.accounts:
            if card == acc.card:
                return acc
        return None


bank = Bank()
while True:
    result = input('1.开户 2.存钱 3.取钱 4.查询 5.销户 6.退出')
    if result == '1':
        info = input('请依次输入卡号、密码和开户人姓名，以一个空格隔开: \n')
        bank_info = info.split()

        card = bank_info[0]
        password = bank_info[1]
        name = bank_info[2]

        acc = Account(card, password, name)
        bank.add_account(acc)
        print('恭喜开户成功')
    elif result == '2':
        card_code = input('请输入卡号: \n')
        acc = bank.select_card(card_code)
        if acc:
            m = float(input('请输入存钱金额: \n'))
            r = acc.in_money(m)
            print(r)
        else:
            print('输入的卡号不存在')
    elif result == '3':
        card_code = input('请输入卡号: \n')
        pwd = input('请输入密码: \n')
        acc = bank.select(card_code, pwd)
        if acc:
            m = float(input('请输入取钱金额: \n'))
            r = acc.out_money(m)
            print(r)
        else:
            print('输入卡号或密码不正确')
    elif result == '4':
        card_code = input('请输入卡号: \n')
        pwd = input('请输入密码: \n')
        acc = bank.select(card_code, pwd)
        if acc:
            print('卡号:', acc.card, '\t密码:', acc.password, '\t账户名:', acc.name, '\t余额:', acc.money)
        else:
            print('输入卡号不存在')
    elif result == '5':
        card_code = input('请输入卡号: \n')
        pwd = input('请输入密码: \n')
        acc = bank.select(card_code, pwd)
        if acc:
            remove = bank.remove_account(acc)
            print(remove)
        else:
            print('输入卡号不存在')
    elif result == '6':
        break
