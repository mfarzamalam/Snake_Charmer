available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'olives', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + " to your pizza")
    else:
        print("Sorry, we don't have " + requested_topping + " in our list")

print ("\nFinishing your pizza\n")

users = ['admin','akim222','xavier446','tiptoed1','xor']
new_user = ['capcha']

if users:
    for user in users:
        if user in new_user:
            print(user + " is already in use. You're not welcome")
        else:
            if user.lower() == 'admin':
                print ("Hello " +user + ".Would you like to see the status ?\n")
            elif user.lower() != 'admin':
                print ("Welcome " +user)
else:
        print("We need to find some users!")

numbers = []

for value in range(1,10):
    if value == 1:
        numbers.append("1st")
    if value == 2:
        numbers.append("2nd")
    if value == 3:
        numbers.append("3rd")
    if value > 3:
        numbers.append(str(value) + "th")

print(numbers)