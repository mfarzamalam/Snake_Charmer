from threading import Thread, current_thread

class Booking():
    def __init__(self,available_seats):
        self.available_seats = available_seats

    def book_seat(self,demanded_seat):
        print("Available seats:",self.available_seats)
        if self.available_seats >= demanded_seat:
            name = current_thread().name
            print(demanded_seat,"seats has been alloted to",name)
            self.available_seats -= demanded_seat
            
        else:
            print("All seats are booked")

pass1 = Booking(4)
f1 = Thread(target=pass1.book_seat, args=(2,), name='akmal')
f2 = Thread(target=pass1.book_seat, args=(3,), name='ajmal')

f1.start()
f2.start()

# The result we are getting is highly unreliable