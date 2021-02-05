class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odemeter = 0

    def get_descriptive_name(self):
        long_format = self.make + ' ' + self.model + ' ' + str(self.year)
        return long_format

    def read_odemeter(self):
        print("The car has " + str(self.odemeter) + " miles on it")

    def update_odometer(self,value):
        if value >= self.odemeter:
            self.odemeter = value
        else:
            print("You cant roll back the value")

    def increement_odemeter(self,value):
        self.odemeter += value

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.increement_odemeter(500)
my_new_car.read_odemeter()

my_new_car.increement_odemeter(100)
my_new_car.read_odemeter()