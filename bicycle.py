bicycle = [1,'second','third', 'fourth','last']

number = 1
print(bicycle[number].title())

number = 2
print(bicycle[number].lower())

number = -1     #backword counting // last // second last
print(bicycle[number].upper())

complete_message = "Hi, John. Your score is " + str(bicycle[3]).title() + " in gaming."
print(complete_message)

f_names = ['my-first-f','my-second-f','my-third-f','my-fourth-f']
print(f_names[0])
print(f_names[1])
print(f_names[2])
print(f_names[3])

f_names_message_1 = "You're good " +f_names[0] + " in whatever you don't do"
f_names_message_2 = "You're good " +f_names[1] + " in whatever you don't do"
f_names_message_3 = "You're good " +f_names[2] + " in whatever you don't do"

print(f_names_message_1)
print(f_names_message_2)
print(f_names_message_3)

cars = ['corolla' , 'motorlla', 'olivia']
wish_1 = "I'd like to buy " + cars[0]
wish_2 = "I'd like to sell " + cars[1]
wish_3 = "i'd like to apply " + cars[2]

print(wish_1)
print(wish_2)
print(wish_3)