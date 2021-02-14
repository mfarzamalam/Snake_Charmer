result = 0

while True:
    try:
        one = int(input("Enter first number: "))
    except:
        one = 0
        pass

    # try:
    #     two = int(input("Enter second number: "))
    # except:
    #     two = 0
    #     pass

    result += one 
    if result != 0:
        print(result)
    else:
        pass