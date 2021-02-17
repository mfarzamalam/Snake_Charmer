from name_function import *

print("Press q anytime to quit")
while True:
    firstname = input("Enter your first name\n:")
    if firstname.lower() == 'q':
        break
    lastname = input("Enter your lastname name\n:")
    if lastname.lower() == 'q':
        break

    formatted_name = get_formatted_name(firstname,lastname)
    print("\tYour neatly formatted name:"+formatted_name)