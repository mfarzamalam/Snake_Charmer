from queue import Queue
from threading import Thread
from time import sleep

class Produce():
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(1,5):
            print("Item produced",i)
            self.q.put(i)
            sleep(1)

class Consume():
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        for i in range(1,5):
            print("Item received",self.prod.q.get(i))
            

p = Produce()
c = Consume(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()