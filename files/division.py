print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first = input("Enter the first number: ")
    if first.lower() == 'q':
        break

    second = input("Enter the second number: ")
    if second.lower() == 'q':
        break

    try:
        result = int(first) / int(second)
        print(result)
    except:
        print("You can't divide it to zero cunt")