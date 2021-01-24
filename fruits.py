my_fruit = ['apple','banana','orange']

my_friend_fruit = my_fruit[:]

print("My fruits are :")
print(my_fruit)

print("\nMy friends fruit are : ")
print(my_friend_fruit)


my_fruit.append("mango")
my_friend_fruit.append("ice cream")

print("My updated fruits are ")
print(my_fruit)

print("\nMy friend updated fruit are")
print(my_friend_fruit)


food = ['food1','food2','food3','food4','food5','food6','food7','food8','food9','food10','food11']


print(food[-3:])    #last three item of the list
print(food[:3])    #first three item of the list
print(food[4:-4])   #middle item of the list


my_pizza = ['pizza1','pizza2','pizza3']
my_friend_pizza = my_pizza[:]

print(my_pizza)
print(my_friend_pizza)

my_pizza.append('pizza4')
my_friend_pizza.append('pizza5')

print("My new pizza list :")
for pizza in my_pizza:
    print(pizza)

print("\nMy new friend pizza list : ")
for pizza in my_friend_pizza:
    print(pizza)

