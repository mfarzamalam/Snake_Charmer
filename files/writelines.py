f = open('student.txt',mode='w')

lst = ['first','second','third','fourth']
f.writelines(lst)

f.close()
print("Success")