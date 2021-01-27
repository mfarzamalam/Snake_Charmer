print("Hi. Welcome to the mike french fries")

fries_order = 0
fries = []

while True:
    try:
        ask_price = input("\nHow much rupee fries do you need? 30/50 or 100\n:")
        price = int(ask_price)

        if price == 30 or price == 50 or price == 100:
            fries_order = price

            ask_mayo = input("\nPress Y if you want me to add mayoneese or pess enter to skip\n:")
            if ask_mayo == 'y' or ask_mayo == 'Y':
                fries.append('mayoneese') 

            ask_ketchup = input("\nPress Y if you want me to add ketchup or pess enter to skip\n:")
            if ask_ketchup == 'y' or ask_ketchup == 'Y':
                fries.append('ketchup')

            ask_sauce = input("\nPress Y if you want me to add sauce or pess enter to skip\n:")
            if ask_sauce == 'y' or ask_sauce == 'Y':
                fries.append('sauce')

            ask_spices = input("\nPress Y if you want me to add spices or pess enter to skip\n:")
            if ask_spices == 'y' or ask_spices == 'Y':
                fries.append('spices')

            print("\nYou've order " +str(fries_order) + "rs fries with ")

            for fri in fries:
                print(fri.title())
            break

        else:
            print("Sorry we've only 30/50 and 100rs fries")
            continue

    except ValueError:
        print("Please write the number properly")