filename = 'guestName.txt'
filename2 = 'guestVisit.txt'

name = input("What is your name?\n:")
visit = input("Would you like to visit? Yes/No\n:")

with open(filename,'a') as fileObject:
    fileObject.write("\n"+name)

with open(filename2,'a') as fileObject:
    fileObject.write("\nName:"+ name + ", Visit:" + visit)

print("\nWelcome "+name)