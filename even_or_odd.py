determine = int(input("Add a number to determine wether it is even or odd \n:"))
value = determine % 2

if value == 0:
    print("The number "+ str(determine) + " is Even")
else:
    print("The number "+ str(determine) + " is Odd")