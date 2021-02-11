class A:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def show_student_detail(self):
        print("Student Name:",self.name)
        print("Student RollNo:",self.roll)

# passing the value of one class to another
class B:
    @staticmethod
    def show(user):
        print("S Name:",user.name)
        print("S RollNo:",user.roll)
        user.show_student_detail()


mike = A('mike',47)

B.show(mike)