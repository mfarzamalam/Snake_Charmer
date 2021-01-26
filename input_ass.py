### Find a customer favourite car 
rental_car = input("So tell me which car would you like me to find? \n:")

print("Let me find the "+ rental_car.title() +" and i'll get back to you")


### confrm the seats if it's less than 8
seats_confrm = int(input("How many seats you need ? \n:"))

if seats_confrm > 8:
    print("Sorry, you'll have to wait for a while. We are not ready to serve "+ str(seats_confrm) + " people")
else:
    print("Come with your guest. we are ready to serve " + str(seats_confrm) + " people")


### Check to see wether a number is divisible by 10 or not
div_by_10 = int(input("Write a number to see wether it is divisible by 10 or not \n:"))
check = div_by_10 % 10

if div_by_10 > 10:
    if check == 0:
        print("Yes. The number " + str(div_by_10) + " is divisible by 10")
    else:
        print("No. The number " + str(div_by_10) + " is not divisible by 10")
else:
    print("please write a number that is greater than 10")