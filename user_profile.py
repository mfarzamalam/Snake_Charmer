def build_profile(first,last,**other_info):
    profile={}
    profile['first']=first
    profile['last']=last

    for key,value in other_info.items():
        profile[key] = value

    return profile

profile = build_profile('albert','einstein',age=57,gender='male')
print(profile)


def my_profile(firstName,LastName,age,**other_details):
    me = {}
    me['first'] = firstName
    me['last'] = LastName
    for key,value in other_details.items():
        me[key] = value

    return me

first = my_profile('rick','grimes',52,gender='male',occupation='officer',relationship='married')
second = my_profile('zack','ramsey',32,gender='male',occupation='singer',relationship='single')

print(first,"\n",second)

def car_details(manufacturer,model_name,**other_details):
    cars = {}
    cars['manufacture'] = manufacturer
    cars['model'] = model_name

    for key,value in other_details.items():
        cars[key] = value

    return cars

car = car_details('subaru','outback',color='blue',seats=4)
print(car)