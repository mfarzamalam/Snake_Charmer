class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " can sit and it's age is " +str(self.age))

    def roll_over(self):
        print(self.name + " can roll over and it's age is " +str(self.age))

    def gender(self,sex):
        print(self.name + " is a " +sex)


my_first_dog = Dog('willie',6)
my_second_dog = Dog('callie',9)

print("My first dog name is "+my_first_dog.name+ " and my second dog name is "+my_second_dog.name)
print("My first dog age is "+str(my_first_dog.age)+ " and my second dog age is "+str(my_second_dog.age))

my_second_dog.sit()
my_second_dog.roll_over()
my_second_dog.gender('male')