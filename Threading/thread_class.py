from threading import Thread

class My_method(Thread):
    def run(self):
        for i in range(5):
            print("run this method")

class My_second_method(Thread):
    def run(self):
        for i in range(5):
            print("another method")

t2 = My_second_method()
t2.start()
t2.join()       # join() method force the thread to run first completely

t = My_method()
t.start()
# t.join()

for i in range(5):
    print("MAIN")