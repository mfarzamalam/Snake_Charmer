class Restaurant():
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number = 0

    def describe_restaurant(self):
        print("\n"+self.name + " has a cuisine named " +self.cuisine)

    def open_restaurant(self):
        print(self.name + " is open now")

    def close_restaurant(self):
        print(self.name + " is closed now")

    def number_saved(self,value):
        if self.number >= value:
            self.number = value

    def increement_number(self,value):
        self.number += value

    def show_served(self):
        print("The number of people served are "+str(self.number))


first_restaurant = Restaurant('kfc','borger')
second_restaurant = Restaurant('pizza hut','phee-ja')
third_restaurant = Restaurant('dhabba','chai')
fourth_restaurant = Restaurant('abc','paratha')

first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()
first_restaurant.close_restaurant()

second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()
second_restaurant.close_restaurant()

third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()
third_restaurant.close_restaurant()
third_restaurant.increement_number(12)
third_restaurant.increement_number(8)
third_restaurant.increement_number(12)
third_restaurant.show_served()