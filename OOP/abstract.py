from abc import ABC, abstractmethod

class Forces(ABC):
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun.")

class Army(Forces):
    def area(self):
        print("Army")

class Navy(Forces):
    def area(self):
        print("Navy")

class Airforce(Forces):
    def area(self):
        print("AirForce")


F = Army()
F.area()