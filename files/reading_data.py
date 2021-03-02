f = open('student.txt',mode='r')
read_letter = f.read(9)              # it help to retrieve data in letters
print(read_letter)
f.close()


f = open('student.txt',mode='r')
read_sinlge_line = f.readline()     # it help to retrieve data of single line
print(read_sinlge_line,end='')


f = open('student.txt',mode='r')
read_complete_data = f.readlines()  # it help to retrieve complete data
print(read_complete_data)