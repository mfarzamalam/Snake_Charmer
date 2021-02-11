class Animals():
    def walk(self):
        print("Animals can walk")

class Duck(Animals):
    def walk(self):
        super().walk()      # call parent method with super keyword
        print("Duck can walk")  # Method overriding where we override method in child class

class Horse():
    def walk(self):
        print("Horse can walk")

class Cat():
    def talk(self):
        print("Cat can talk")


def check_legs(obj):
    if hasattr(obj,'walk'):     # We can check wether the object has a method or not
        obj.walk()
    else:
        print("Cant walk")

class Maths():
    def sum(self, a=0,b=0,c=0):     #Method overloading where we use default values like zero or none
        s = a+b+c
        print(s)

class Multi(Maths):
    def sum(self, a=1,b=1,c=1):
        super().sum(a,b,c)
        s = a*b*c
        print(s)

H = Horse()
check_legs(H)

D = Duck()
check_legs(D)

C = Cat()
check_legs(C)

M = Maths()
M.sum(1,100,22)
M.sum(22,22)
M.sum(22)

Mul = Multi()
Mul.sum(22,11)