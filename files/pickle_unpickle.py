import pickle           # too add and retrieve data in other files

class Student:
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age

    def disp(self):
        print("Name:",self.name,
              "Roll No:",self.roll,
              "Age:",self.age    
            )

n = int(input("How many data you wanna enter? "))

with open('student_data.txt',mode='wb') as f_obj:
    for i in range(n):
        name = input("Enter your name: ")
        rollno = input("Enter your Roll No: ")
        age = input("Enter your age: ")

        stu1 = Student(name,rollno,age)
        pickle.dump(stu1,f_obj)

    print("Pickle done!")

print()

with open('student_data.txt',mode='rb') as f_obj:
    while True:
        try:
            stu1 = pickle.load(f_obj)
            stu1.disp()
        except:
            print("Unpickle done!")
            break