"""
练习生产者消费者模型例子
1.进货 2.售货 3.退出
"""
import threading


class Shop:
    def __init__(self, max):
        """
        初始化
        :param max: 最大库存
        :param num: 当前库存
        """
        self.max = max
        self.num = 0
        self.condition = threading.Condition()

    def stock(self, num):
        """
        进货
        :param num: 进货数量
        :return:
        """
        with self.condition:
            while num + self.num > self.max:
                print('进货失败，请等待，进货数量%d，当前库存%d' % ( num, self.num))
                self.condition.wait()
            self.num += num
            print("进货成功，进货数量%d, 当前库存%d" % ( num, self.num))
            self.condition.notify_all()

    def sell(self, num):
        """
        售货
        :param num: 售货数量
        :return:
        """
        with self.condition:
            while self.num < num:
                print('售货失败，请等待，进货数量%d，当前库存%d' % ( num, self.num))
                self.condition.wait()
            self.num -= num
            print('售货成功，售货数量%d，当前库存%d' % ( num, self.num))
            self.condition.notify_all()


class Stock(threading.Thread):
    """ 进货线程 """

    def __init__(self, shop, num):
        """
            初始化
        :param shop: 进货商店
        :param num: 进货数量
        """
        threading.Thread.__init__(self)
        self.shop = shop
        self.num = num

    def run(self):
        self.shop.stock(self.num)


class Sell(threading.Thread):
    """ 售货线程 """

    def __init__(self, shop, num):
        """
            初始化
        :param shop: 进货商店
        :param num: 售货数量
        """
        threading.Thread.__init__(self)
        self.shop = shop
        self.num = num

    def run(self):
        self.shop.stock(self.num)


shop = Shop(100)

while True:
    inp = input('请输入1.进货 2.售货 3.退出')
    if inp == '1':
        n = int(input('请输入进货数量:'))
        Stock(shop, n).start()
    elif inp == '2':
        n = int(input('请输入售货数量:'))
        Sell(shop, n).start()
    elif inp == '3':
        break
