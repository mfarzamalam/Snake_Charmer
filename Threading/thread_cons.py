from threading import *

class ChildThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("child thread Constructor")

    def runing(self):
        print("Just run child")
    
    def walk(self):
        print("Just walk child")

t = ChildThread()
t.start()

print("<mAiN>")


class Show_city():
    def disp(self,city,country):
        print(city,country)

loc = Show_city()
method = loc.disp('karachi,','Pakistan')

t = Thread(target=method)
t.start()