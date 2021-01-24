car = 'lamborgini'

print("Is car is lamborgini ? I predict True")
print(car == 'lamborgini')

person = "usama"
age = 18
gender = "Male"

if age > 17 and age < 22:
    if gender.lower() != 'female':
        print("Hi, " + person.title() + ". You're allowed in our community")
        
    if gender.lower() == 'female':
        print("Sorry. This is a male ONLY community")

persons = (19,20,21)

if 19 in persons:
    print("Grow up")


alien_color = "Green"

if alien_color.lower() == "red":
    print("Alien is dead")
elif alien_color.lower() == 'green':
    print("You earned 5 points")
elif alien_color.lower() == 'yellow':
    print("You earned 10 points")

else:
    print("Keep chasing")

person_age = 5

if person_age < 2 :
    print("the person is a baby.")
elif person_age >= 2 and person_age < 4:
    print("the person is a toddler.")
elif person_age >= 4 and person_age < 13:
    print("the person is a kid.")
elif person_age >= 13 and person_age < 20:
    print("the person is a teenager.")
elif person_age >= 20 and person_age < 65:
    print("the person is an adult.")
elif person_age >= 65:
    print("the person is an elder.")

fav_fruits = ['bananana','apple','orange','mango','grapes']

for fav_fruit in fav_fruits:
    if fav_fruit == 'bananana':
        print(fav_fruit.title() + " my fav. but i don't eat")
    if fav_fruit == 'apple':
        print("Corona a day keeps the " +fav_fruit.title() + " and doctor away.")
    if fav_fruit == 'orange':
        print(fav_fruit.title() + " is not in my range.")
    if fav_fruit == 'mango':
        print(fav_fruit.title() + " is not just a fruit. it's lubbbb <*)")
    if fav_fruit == 'grapes':
        print(fav_fruit.title() + " is all time love. it's not food only. it's a whole meem")