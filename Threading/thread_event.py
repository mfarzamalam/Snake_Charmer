from threading import *
from time import *

def light_switch():
    e.set()     # Condition is True
    print("Green Light ON")
    sleep(5)
    print("Red Light ON")
    e.clear()   # Condition is False


def traffic():
    # e.wait()
    while e.is_set():   #Loop start working when condition is true. condition is coming from line no.5
        print("You can go")
        sleep(1)
    
    print("Program is done")


e = Event()
t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)


t1.start()
t2.start()