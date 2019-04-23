"""
    继承
"""

class a():
    sty = 'hahahah'

    def __init__(self, name, color):
        self.name = name
        self.color = color


    def sound(self):
        print(self.name, self.color)


class b(a):
    # 重写
    def __init__(self, name):
        self.name = name

        a.__init__(self, color)

    def ex(self):
        return  print(self.name)


b1 = b('潇潇兮', '红色')
b1.ex()