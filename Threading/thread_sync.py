from threading import *

class Flight():
    def __init__(self,availaible_seats):
        self.availaible_seats = availaible_seats
        self.lock = Lock()     # Lock force the program to run one thread at a time

    def book_now(self,req_seats):
        self.lock.acquire()     # starting the lock using acquire method

        print("Available seats:",self.availaible_seats)
        name = current_thread().name        
        if req_seats <= self.availaible_seats:
            print(req_seats,"seats alloted to",name)
            self.availaible_seats -= req_seats
        else:
            print("No seats for",name)
        
        self.lock.release()     # ending the lock using release method

f1 = Flight(3)
t1 = Thread(target=f1.book_now,args=(1,),name='akram')
t2 = Thread(target=f1.book_now,args=(2,),name='aslam')
t3 = Thread(target=f1.book_now,args=(1,),name='atif')

t1.start()  
t2.start()
t3.start()

# using the join method to force the program to run all thread except Main thread
t1.join()
t2.join()
t3.join()

print("Main")