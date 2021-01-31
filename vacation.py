users = {}

again = True

while again:

    name = input("What is your name ? \n")
    location = input("Which location would you like to visit? \n:")

    users[name] = location.lower()

    repeat = input("Would you like to add another person ? \n:")
    if repeat.lower() == 'no':
        again = False

for name,location in users.items():
    print(name.title() + " would like to visit " +location.title())