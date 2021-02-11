class Mobile:
    version = '3.0'     # class variable

    def __init__(self):
        self.name = 'Realme'        # instance variable
    
    def show_details(self):         # instance method 
        self.price = 1000

        print("Name:",self.name,"Price:",self.price)

    @classmethod                    # class decorator to access class variable
    def show_version(cls):          # class method

        print("Version:",cls.version)

realme_one = Mobile()
realme_one.show_details()
Mobile.show_version()

redmi_one = Mobile()
geek_one = Mobile()

Mobile.version = '2.0'
realme_one.show_version()
redmi_one.show_version()
geek_one.show_version()


class Human:
    def __init__(self):
        self.name = 'mike'

    def get_name(self):
        return self.name
    
    def set_name(self,n):
        self.name = n
        return self.name

    @staticmethod               # decorator
    def view_all(m,n):          # static method
        print(m,n)

person = Human()
my_name = person.get_name()

take_name = input("PLease enter your name:\n")
change_name = person.set_name(take_name)

print(my_name)
print(change_name)

person = Human()
Human.view_all(1,2)