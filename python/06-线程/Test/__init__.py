from test import num
import threading

# t1 = threading.Thread(target=num, args=('线程一', ))
# t1.start()
#
# t2 = threading.Thread(target=num, args=('线程二', ))
# t2.start()

class PrintThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        num(self.name)


t1 = PrintThread('线程1')
t2 = PrintThread('线程2')

t1.start()
t2.start()