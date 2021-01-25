users = {
    'aeinstein':{
        'first':'albert',
        'second':'einstein',
        'location':'princton'
    },
    'mcurie':{
        'first':'marie',
        'second':'curie',
        'location':'paris',
    }
}

for username,user_info in users.items():
    print("@" +username.lower() +":")
    full_name = user_info['first'] + " " + user_info['second']
    location = user_info['location']

    print("\tFull name: " +full_name)
    print("\tLocation: " +location)


persons = {
    'amad':{
        'age':21,
        'height':6,
        'weight':72,
        'gender':'male'
    },
    'jenny':{
        'age':33,
        'height':4,
        'weight':63,
        'gender':'female'
    }
}

for name,other_details in persons.items():
    print(
        "\nFullname:" +name.title() + 
        "\nAge:" +str(other_details['age'])+
        "\nGender:"+str(other_details['gender'])+
        "\nHeight:"+str(other_details['height'])
    )

pets = {
    'cat':{
        'color':'white',
        'kind':'persian',
        'weight':22
    },
    'dog':{
        'color':'black',
        'kind':'husky',
        'weight':22
    }
}


for pet_name,pet_details in pets.items():
    print("\nWhat pet do you own?\n-"+pet_name)
    print("What color it has?\n-"+pet_details['color'])
    print("What's your pet kind?\n-"+pet_details['kind'])

friends = {
    'mickel':['america','canada','france'],
    'julie':['australia','paris'],
    'alfred':['uk','switzerland','denmark','newyork']
}

for name,friends_visits in friends.items():
    print("\nMy friend "+name+ " like to visit:")

    for friends_visit in friends_visits:
        print("-"+friends_visit.title())


cities = {
    'delhi':{
        'country':'india',
        'population':'46M',
        'fact':'about to invaded by pakistan'
        },
    'tel-aviv':{
        'country':'israel',
        'population':'32M',
        'fact':'about to invaded by israel'
    }
}

for name,city in cities.items():
    print(
        "\nCity name: "+name.title()+
        "\nCountry: "+city['country'].title()+
        "\nPopulation: "+city['population']
    )