f = open('student.txt',mode='wb+',encoding='utf-8')
print("File name:",f.name)
print("File mode:",f.mode)
print("File read:",f.readable())
print("File write:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)