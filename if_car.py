cars = ['audi','bmw','ferrari','ffx']

for car in cars:
    if car == "ffx":
        print(car.upper())

    else:
        print(car.title())

car = 'BMW'

print(car.lower() == 'bmw')
print(car.lower() != 'bwm')

users = ['ali','marie','usama','marie','andrew','david']

if len(users) > 0:
    length = len(users)
    print("There are " + str(length) + " users in our website")

    if 'ali' in users:
        print("Ali you're banned in our forum for a week")

    if 'caroline' not in users:
        print("We just kicked caroline from our forum.")

else:
    print("No users!")