filename = 'pi_digit.txt'

with open(filename) as fileObject:
    lines = fileObject.readlines()

pi_String = ''

for line in lines:
    pi_String += line.strip()

print(pi_String[:10] + "...")   # showing only first 10 digits
print(len(pi_String))

birthday = input("Enter your birthday in the form of mmddyy:\n")

if birthday in pi_String:
    print("Your birthday appears in the first million digit of pi")
else:
    print("Your birthday doesnot appear in the first million digit of pi")