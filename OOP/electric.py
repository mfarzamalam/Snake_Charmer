class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        print(self.model+ " is made in the year "+str(self.year))


class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("The car has a " + str(self.battery_size) + "-KWH battery")

    def get_range(self):
        if self.battery_size <= 70:
            range = 220
        elif self.battery_size <= 90:
            range = 290

        message = "This car can go "+str(range) +" miles"
        print(message)


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.buttery = Battery()

