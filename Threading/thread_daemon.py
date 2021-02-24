from threading import Thread, current_thread
from time import sleep

def show():
    print("Show function")

def disp():
    print("Disp Function from t1")
    t2 = Thread(target=show)            # creating second thread
    print("T2:",t2.isDaemon())          # printing the value
    t2.start()                          # starting the thread

mt = current_thread()                   # getting main thread name
print("Name of thread:",mt.getName())   # got main thread name
print("Before:",mt.isDaemon())          # checking wether the main thread is daemon or not

t1 = Thread(target=disp)                # creating a first thread and calling the disp() function
print("T1 before:",t1.isDaemon())       # printing first thread daemon value
t1.setDaemon(True)                      # setting the first thread value true
print("T1 After:",t1.isDaemon())        # printing again the value

t1.start()                              # starting the first thread
t1.join()                               # since t1 and t2 start simoultaneously. we restrict that t1 start first by using join method

# if the child thread is daemon and want to terminate itself. we use main thread which is not daemon
def teacher():
    for i in range(1,10):
        print("Teaching",i)
        sleep(1)

ct = current_thread()                   # getting the main thread
print(ct.name,":",ct.isDaemon())        # getting the name of main thread
ct.setDaemon(True)
print(ct.name,":",ct.isDaemon())        # getting the name of main thread

t1 = Thread(target=teacher)             # creating a thread of teacher
print("t1:",t1.isDaemon())              # checking if the thread is daemon or not
t1.setDaemon(True)                      # setting daemon to true
t1.start()                              # starting the thread
sleep(6)                                # delaying 6 second sleep


print("t1:",t1.isDaemon())              # checking again the value