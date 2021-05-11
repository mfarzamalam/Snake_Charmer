from numpy import *

### Using For loop

# user = int(input("How many user do you have?\n:"))
# rollno = zeros(user, dtype=int)

# print("Enter their Roll Number's\n")
# for i in range(user):
#     ids = int(input(":"))
#     rollno[i] = ids

# print(rollno)


### Using While Loop
user = int(input("How many user do you have?\n:"))
rollno = zeros(user, dtype=int)

print("Enter their Roll Number's\n")
i=0
while i < user:
    ids = int(input(":"))
    rollno[i] = ids
    i+=1

print(rollno)