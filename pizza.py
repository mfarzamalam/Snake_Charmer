def pizza(*topping):
    for topping in topping:
        print("-"+topping)

pizza('pepparoni','extra cheese','green peppers','extra ketchup')

def pizza_order(size,*topping):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in topping:
        print("-"+topping.title())

pizza_order(12,'pepparoni','extra cheese','green peppers','extra ketchup')
pizza_order(18,'pepparoni','extra cheese','green peppers','extra ketchup')


def sandwich(*items):
    print("\nThe type of sandwich we have:")

    for item in items:
        print("-"+item.title())

sandwich('chicken','beef','narcotics')
sandwich('drugs','hasheesh','antibiotics')


def staff_in_a_restaurant(
    first_staff,second_staff,third_staff,
    fourth_staff,fifth_staff,sixth_staff,
):