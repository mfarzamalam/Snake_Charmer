f = open('student.txt',mode='r')
print(f.tell())     # checking where is the cursor initially

data = f.read(5)    # moving the cursor forward to 5 words
print(f.tell())     # check again where is the cursor

data = f.read(5)    # moving the cursor forward again to 5 words
print(f.tell())     # checking again where is the cursor
f.seek(5)           # start the cursor after 5 words
data = f.read()     # reading all data after 5 words
print(data)