from threading import Thread, current_thread

def disp(a,b):
    for i in range(5):
        print("Child thread",a,b)

t = Thread(target=disp,args=(10,20))
t.start()


def name_of_thread():
    print()
    print("Another thread",current_thread().getName())
    current_thread().setName('Name changed')
    print("Another thread",current_thread().getName())

t2 = Thread(target=name_of_thread)
t3 = Thread(target=name_of_thread)
t2.start()
t3.start()


def check_name_of_thread():
    print("View name:",current_thread().name)

t4 = Thread(target=check_name_of_thread)
t4.start()


for i in range(5):
    print("Default Main thread")