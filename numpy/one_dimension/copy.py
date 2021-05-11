from numpy import *

### view method create new array,
a = array([101,102,0,105,127,0])
b = copy(a)
a[2] = 55
b[3] = 99

print(a)
print(b)


print("memory allocation of array a:",id(a))
print("memory allocation of array b:",id(b))