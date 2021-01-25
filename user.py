fav_lang = {
    'jen':'python',
    'sarah':'c',
    'edward':'java',
    'phill':'php',
    'john':'c'
}

for name,language in fav_lang.items():
    print(
        name.title() + " favourite language is "+language.title()
    )

friends = ['sarah']

for friend in friends:
    if friend in fav_lang:
        print("Hi " +friend.title() + ". I know your fav lang is " + fav_lang[friend].title())

if 'jacoob' not in fav_lang:
    print("Hey jacoob. Take the poll")

print("\nHere is the list of all the person who took the poll")
for person in fav_lang.keys():
    print(person.title())

print("\nHere is the list of all the programming language that people liked")
for language in fav_lang.values():
    print(language.title())

print("\nHere is the list of all the people in sorted way")
for names in sorted(fav_lang.keys()):
    print(names.title())

print("\nHere is the list of all the unique language using set function")
for lang in sorted(set(fav_lang.values())):
    print(lang.title())

words = {
    'dictionary': 'To store data in key-value-pair format',
    'tuple':'To store data which are constant in our program',
    'list':'A sets of data which can be changed dynamically',
    'slice':'The function which add, update and retrieve data in list',
    'strip':'The function which delete useless white spaces in the string'
}

for word, mean in words.items():
    print(
        "\nWhy we use " + word.title() + "?" + "\n\tAnswer: " + mean
    )

countries = {
    'israel':'tel-aviv',
    'pakistan':'islamabad',
    'india':'delhi'
}

for country, capital in countries.items():
    print("\n"+capital.title() + " is the capital of " + country.title())

polls = ['usama','jen','jacob','umer','john','tottem']

for poll in polls:
    if poll in fav_lang:
        print("\nThank you for joining the poll "+ poll.title())
    else:
        print("\n"+poll.title() +".PLease join our poll")