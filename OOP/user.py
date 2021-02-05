class User():
    def __init__(self,first,last,gender,nationality,age):
        self.first = first
        self.last = last
        self.gender = gender
        self.nationality = nationality
        self.age = age
        self.login = 0

    def fullname(self):
        self.fullname = self.first + " " + self.last

    def describe_user(self):
        print("\n"+self.fullname + " just logged in to our system. Details are")
        print(
            "First name is "+self.first+
            "\nLast name is "+self.last+
            "\nGender is "+self.gender+
            "\nNationality is "+self.nationality+
            "\nAge is "+str(self.age)
        )

    def greet_user(self):
        print("Welcome "+self.fullname)

    def login_attempt(self):
        self.login += 1
        
    def login_reset(self):
        self.login = 0
        return self.login

    def login_check(self):
        return self.login

first_user = User('carol','ark','female','american',49)

first_user.fullname()
first_user.describe_user()
first_user.greet_user()

second_user = User('rajesh','khanna','male','india',24)

second_user.fullname()
second_user.describe_user()
second_user.greet_user()

second_user.login_attempt()
second_user.login_attempt()
second_user.login_attempt()
second_user.login_attempt()

attempt = second_user.login_check()

if attempt >= 5:
    print("Sir you've reached the limit. We're resetting your password")
    attempt = second_user.login_reset()
else:
    print("Number of attempt remaining are "+str(5-attempt))

print("Login attempt  "+str(attempt))