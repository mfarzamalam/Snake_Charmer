class Restaurant():
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def restaurant_details(self):
        print(self.name +" has a cuisine of "+self.cuisine)

class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine):
        super().__init__(name,cuisine)

    def flavours(self,flavour = 'choclate'):
        print(self.name + " has a flavour of "+flavour)

first_rest = Restaurant('bbc','levish')
first_rest.restaurant_details()

second_rest = IceCreamStand('abc','strawberry')
second_rest.flavours()