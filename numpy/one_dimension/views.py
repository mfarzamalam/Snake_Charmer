from numpy import *

### view method copy the array and save it to new location, however if any of array modified. changes will reflect to both of them
a = array([101,102,0,105,127,0])
b = a.view()
a[2] = 55
b[3] = 99

print(a)
print(b)


print("memory allocation of array a:",id(a))
print("memory allocation of array b:",id(b))