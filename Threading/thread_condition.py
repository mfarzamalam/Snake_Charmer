from threading import *
from time import *

product = []

def produce():
    cv.acquire()
    for i in range(1,7):
        product.append(i)
        sleep(.5)
        print("Item produce")
    
    cv.notify()     # this notify the consume function
    cv.release()

def consume():
    cv.acquire()
    cv.wait(timeout=0)  # this will get alert once notified
    cv.release()   
    print(product)    


cv = Condition()
t1 = Thread(target=produce)
t2 = Thread(target=consume)
t1.start()
t2.start()