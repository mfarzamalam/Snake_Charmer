alien_0 = {
    'name':'xavier',
    'color':'green',
    'point': 55
}

print(alien_0['name'])

alien_0_points = alien_0['point']

print("Your final score is : " + str(alien_0_points))

alien_0['x-axis'] = 24
alien_0['y-axis'] = 22

print(alien_0)

alien_1 = {}

alien_1['name'] = 'tor'
alien_1['color'] = 'red'
alien_1['point'] = 20
alien_1['color'] = 'purple'

print(alien_1['color'])

alien_2 = {
    'name' : 'captain',
    'x-axis' : 30,
    'y-axis' : 56,
    'speed' : 'Slow'
}


print("Alien speed is " + str(alien_2['speed']) + "\nAlien x-axis position is : "+str(alien_2['x-axis']))

if alien_2['speed'].lower() == 'slow':
    x = 10
elif alien_2['speed'] == 'medium':
    x = 20
else:
    x = 35

alien_2['x-axis'] = alien_2['x-axis'] + x 

print("New x-axis position : " +str(alien_2['x-axis']))

print(alien_2)
del alien_2['name']
print(alien_2)

persons = {
    'first_name' : 'jack',
    'last_name' : 'maa',
    'age' : 25 ,
    'city' : 'karachi'
}

print("\nFirst name: " +str(persons['first_name']) 
    +"\nLast name: " +str(persons['last_name']) 
    +"\nAge: " +str(persons['age'])
    +"\nCity: " +str(persons['city'])
)

fav_number = {
    'first_person':'usama',
    'second_person':'jake',
    'third_person':'jolly',
    'first_number':22,
    'second_number':32,
    'third_number':45
}

print(
    "\nFirst person: " +str(fav_number['first_person'])+
    "\nFirst person number: " +str(fav_number['first_number'])+
    "\nSecond person: " +str(fav_number['second_person'])+
    "\nSecond person number: " +str(fav_number['second_number'])+
    "\nThird person: " +str(fav_number['third_person'])+
    "\nThird person number: " +str(fav_number['third_number'])
)

words = {
    'dictionary': 'To store data in key-value-pair format',
    'tuple':'To store data which are constant in our program',
    'list':'A sets of data which can be changed dynamically',
    'slice':'The function which add, update and retrieve data in list',
    'strip':'The function which delete useless white spaces in the string'
}

print(
    "\nWhy we use dictionary? \n\tAnswer: " +str(words['dictionary'])+
    "\n\nWhy we use tuple? \n\tAnswer: "+str(words['tuple'])+
    "\n\nWhy we use list? \n\tAnswer: "+str(words['list'])+
    "\n\nWhy we use slice? \n\tAnswer: "+str(words['slice'])+
    "\n\nWhy we use strip? \n\tAnswer: "+str(words['strip'])
)