class User():
    def __init__(self,first,last,gender):
        self.first = first
        self.last = last
        self.gender = gender

class Admin(User):
    def __init__(self,first,last,gender):
        super().__init__(first,last,gender)

    def show_privilage(self):
        print(self.first +" is admin now.\nHe can post.\nHe can create.\nHe can delete")

first_user = Admin('farzam','alam','male')
first_user.show_privilage()