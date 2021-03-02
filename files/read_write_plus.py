# read then write
f = open('student.txt',mode='r+')
data = f.read()
f.write('read')
print(data)
f.close()


# overwrite then read
f = open('student.txt',mode='w+')
data2 = f.read()
f.write('overwrite')
print(data2)
f.close()


# append then read
f = open('student.txt',mode='w+')
data3 = f.read()
f.write('append')
print(data3)
f.close()